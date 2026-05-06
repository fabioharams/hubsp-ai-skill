---

# 🔒 8.7. Segurança de MCP Servers — Controles Build-Time e Runtime

## 🎯 Contexto e Complementariedade

A **Seção 3.2 (Azure APIM para IA)** define como escalar MCP servers de forma governada: centraliza autenticação, policies, rate limiting e auditoria em nível de gateway. Porém, o APIM fornece uma **camada de perímetro** — ele governa o tráfego, mas não pode proteger a segurança **interna** de cada MCP server.

Este tópico complementa 3.2 com os controles essenciais em build-time (como construir) e runtime (como operar) MCP servers seguindo o **OWASP Practical Guide for Secure MCP Server Development v1.0**. Juntos, APIM + MCP Security definem uma abordagem em **camadas**:

- **Perímetro (APIM)**: Autenticação, rate limits, roteamento, mascaramento de campos sensíveis, observabilidade
- **Segurança interna (MCP Server)**: Isolamento, validação, sanitização, secrets management, audit logging

**Sem ambas as camadas, vulnerabilidades exploráveis permanecem.**

---

## 🛡️ Sete Pilares de Segurança MCP (OWASP)

### **1️⃣ Arquitetura Segura e Isolamento**

**Princípio**: Cada sessão de usuário/agente é uma "cápsula" isolada; nenhum dado residual entre requisições.

**Controles**:
- ✅ **Isolamento de usuários**: Sem variáveis globais, sem singletons compartilhados, sem class-level attributes com user data
- ✅ **State management**: Use session-keyed stores (ex.: Redis com namespace `session_id:{data}`)
- ✅ **Resource quotas per session**: Memória, CPU, file handles, API rate limits
- ✅ **Cleanup determinístico**: Quando session termina, flushar **imediatamente** todos os dados em memória, arquivos temporários, cached tokens
- ✅ **Timeout enforced**: Sessions expiram automaticamente após inatividade

**Exemplo de risco**:  
```python
# ❌ ERRADO — shared state
user_cache = {}  # Global!
def get_user_data(user_id):
    user_cache[user_id] = expensive_fetch()
    return user_cache[user_id]

# ✅ CERTO — isolado por session
def get_user_data(session_id, user_id):
    session_store = redis.get(f"session:{session_id}")
    if session_store is None:
        raise SessionExpired()
    user_cache = session_store['user_cache']
    user_cache[user_id] = expensive_fetch()
    session_store.save()  # Transactional
```

---

### **2️⃣ Design Seguro de Ferramentas (Safe Tool Design)**

**Princípio**: Cada ferramenta (tool) exposta ao LLM deve ter um "contrato de segurança" verificável.

**Controles**:
- ✅ **Signed cryptographic manifests**: Cada tool tem uma assinatura digital que engloba descrição + schema + versão + permissões obrigatórias
  - Impede "rug pulls": tool description não pode mudar em runtime sem invalidar a assinatura
  - Verificar assinatura + hash no load-time
  
- ✅ **Formal onboarding approval**: Antes de qualquer tool ir para produção:
  - SAST scan (static code analysis com regras MCP-specific)
  - SCA scan (dependency vulnerability check)
  - Manual security review
  - Teste funcional do comportamento anunciado vs. real
  
- ✅ **Description vs. Behavior validation**: Implementar checks que garantam que a ferramenta faz exatamente o que sua descrição promete
  - Exemplo: se tool diz "read-only", mas internamente executa writes, é flagged e bloqueado
  
- ✅ **Minimal exposure**: Apenas campos **necessários** (name, description, input schema) expostos ao modelo; metadados internos (versioning, internal IDs) fora do contexto do LLM

**Exemplo**:
```json
// Tool Manifest (signed)
{
  "id": "query_financials",
  "description": "Query company financial data (Q1-Q4 2024)",
  "input_schema": {...},
  "required_permissions": ["read:financials"],
  "version": "1.2.3",
  "signature": "sha256=abc123...",
  "signed_by": "platform_security_team",
  "approved_date": "2026-02-01",
  "expiry_date": "2026-08-01"
}
```

---

### **3️⃣ Validação e Sanitização de Dados**

**Princípio**: Trate todos os dados como untrusted. Valide forma e conteúdo; sanitize output antes de retornar ao LLM.

**Controles**:
- ✅ **JSON Schema enforcement**: Cada tool input e output é validado contra um JSON Schema rigoroso
  - Rejeitar qualquer dado que não match o schema (mesmo fora de bounds)
  - Use validator libraries (ex.: jsonschema em Python)
  
- ✅ **Strict input sanitization**: Filter e escape sequências perigosas
  - SQL injection: parametrize queries, nunca concatenate
  - Command injection: use APIs que aceitam arrays (não shell strings)
  - XSS / code injection: escape e encode conforme contexto (HTML, JavaScript, URL, etc.)
  
- ✅ **Output size limits**: Nenhuma ferramenta pode retornar >N KB
  - Previne: memory exhaustion, token overflow, LLM context pollution
  
- ✅ **Sensitive data masking**: Antes de retornar ao LLM, mask:
  - Credit card numbers (show last 4 digits only)
  - Social security numbers (show last 4)
  - API keys, passwords, tokens (redact completely)

**Exemplo**:
```python
# Input validation
import jsonschema

tool_input_schema = {
    "type": "object",
    "properties": {
        "query": {"type": "string", "maxLength": 500},
        "year": {"type": "integer", "minimum": 2020, "maximum": 2026}
    },
    "required": ["query"]
}

def execute_tool(raw_input):
    # Validate against schema
    jsonschema.validate(instance=raw_input, schema=tool_input_schema)
    
    # Sanitize: use parameterized query, not string concat
    query = raw_input['query']
    result = db.execute("SELECT * FROM financials WHERE description LIKE ?", [query])
    
    # Sanitize output: mask sensitive fields
    result_sanitized = {**result, "api_key": "***REDACTED***"}
    
    # Size limit
    if len(json.dumps(result_sanitized)) > 10000:
        raise OutputSizeExceeded()
    
    return result_sanitized
```

---

### **4️⃣ Controles contra Prompt Injection**

**Princípio**: O LLM pode ser enganado por prompts maliciosos; estruture tool invocation e implemente aprovação humana para ações críticas.

**Controles**:
- ✅ **Structured JSON tool calls**: Nunca permita que o LLM gere free-form text commands
  - Força tool calls através de JSON schema validado (em vez de "execute este comando bash")
  - Reduz superfície de ataque
  
- ✅ **Human-in-the-Loop (HITL) para ações críticas**:
  - Exemplo: antes de deletar dados, aprovar mudança, transferir fundos → exigir intervenção humana
  - Use MCP elicitations ou notificações para pedir confirmação do usuário
  
- ✅ **LLM-as-a-Judge**: Para tool calls críticos, execute um check em contexto separado de LLM
  - Prompt dedicado: "É seguro executar este tool call? Por quê?"
  - Policy prompt: defina explicitamente quais tool calls são permitidos / bloqueados
  
- ✅ **Session reset entre contextos**: Quando agente muda de tarefa/contexto, resetar session
  - Impede que instruções ocultas em histórico longo permaneçam
  - Melhora qualidade de output (menos "context degradation")

**Exemplo**:
```python
# Tool call structure (JSON schema enforced)
{
  "tool_name": "delete_record",
  "parameters": {"record_id": "12345"},
  "requires_approval": True
}

# Before executing, if requires_approval:
if tool_spec.get('requires_approval'):
    # Trigger HITL via MCP elicitation
    approval = await client.elicit_user_approval(
        prompt=f"Do you approve deleting record {params['record_id']}?",
        deadline_seconds=300
    )
    if not approval:
        raise ActionBlockedByUser()
```

---

### **5️⃣ Autenticação e Autorização**

**Princípio**: Cada MCP server call deve ser autenticado e autorizado; permissões devem ser validated em cada requisição.

**Controles**:
- ✅ **OAuth 2.1 / OIDC obrigatório**: Para MCP remoto, autenticação é mandatory
  - Valide iss (issuer), aud (audience), exp (expiration), signature em **cada requisição**
  - Não confie em cache de validação anterior
  
- ✅ **Token delegation (RFC 8693)**: Passe contexto de usuário sem comprometer segurança
  - MCP server recebe token delegado com subset de permissões do usuário original
  - Não é o token do usuário direto, é um token derivado
  - Exemplo: `subject_token` → `actor_token` com escopo reduzido
  
- ✅ **PROIBIDO token passthrough**: NUNCA forward client token direto a downstream APIs
  - Violação clássica: "confused deputy" problem
  - MCP server é tricked em usar token do usuário para ações não autorizadas
  - Solução: MCP server emite seu próprio token para downstream APIs (non-human identity)
  
- ✅ **Short-lived tokens**: Minutos, não horas
  - Access tokens: 5-15 minutos
  - Refresh tokens: hours to days (stored securely)
  - Re-validate token on every call (não cache a validação)
  
- ✅ **Centralized policy enforcement**: Não deixe cada MCP server decidir permissões sozinho
  - Use APIM policies ou dedicated policy layer (ex.: OPA, Azure Policy)
  - Garante consistência entre todos os servers

**Exemplo**:
```python
from authlib.oauth2 import OAuth2Session

def validate_oauth_token(access_token):
    """Validate OAuth 2.1/OIDC token on EVERY call"""
    try:
        # Fetch JWKS from provider (cache with TTL)
        jwks = get_jwks(issuer_url)
        
        # Validate signature, aud, iss, exp
        claims = jwt.decode(
            access_token,
            key=jwks,
            algorithms=['RS256'],
            audience='my_mcp_server',
            issuer='https://auth.company.com'
        )
        
        # Extract user identity
        user_id = claims['sub']
        scopes = claims['scope'].split()
        
        return UserContext(user_id=user_id, scopes=scopes)
    except JWTError as e:
        raise Unauthorized(f"Token validation failed: {e}")

def execute_tool(access_token, tool_name, params):
    # Validate auth on every call
    user_context = validate_oauth_token(access_token)
    
    # Check authorization: does user have permission for this tool?
    required_scope = f"tool:{tool_name}"
    if required_scope not in user_context.scopes:
        raise Forbidden(f"User lacks scope {required_scope}")
    
    # Execute tool (no token passthrough to downstream)
    # Instead, use MCP server's own identity:
    server_token = get_server_token()  # Non-human identity
    result = call_downstream_api(tool_name, params, auth_token=server_token)
    
    return result
```

---

### **6️⃣ Deployment Seguro e Updates**

**Princípio**: MCP server artifacts e dependências são protegidos desde build até runtime.

**Controles**:
- ✅ **Secrets management**: Credenciais, API keys, certificates → sempre em vault
  - NUNCA em environment variables, logs, ou code
  - Use Azure Key Vault, HashiCorp Vault, AWS Secrets Manager
  - MCP server lê secrets em startup, cache em memória com TTL
  
- ✅ **Containerization**: Deploy em container mínimo, hardened
  - Non-root user: RUN useradd -m appuser; USER appuser
  - Minimal base image: scratch, distroless, ou alpine (não full OS)
  - Drop unnecessary capabilities: CAP_SYS_ADMIN, CAP_NET_RAW, etc.
  
- ✅ **Network segmentation**: Restrinja tráfego de entrada/saída
  - Firewall rules: block all inbound, allow only required ports
  - Kubernetes NetworkPolicies: isolate pods por namespace
  - Egress whitelisting: apenas URLs permitidas
  
- ✅ **Supply chain controls**: Versionar, assinar, escanear
  - Version pin todas as dependências (não `*` ou `^`)
  - Sign container images (image signing, sbom/AIOBM)
  - Scan CVEs em real-time: OSV, Dependabot, Snyk
  - AIOBM (AI Bill of Materials): documento de provenance de cada build
  
- ✅ **CI/CD security gates**:
  - SAST (static analysis): fail build se vulnerabilidade crítica encontrada
  - SCA (dependency scan): fail se dependency conhecida como vulnerable
  - Container scan: não push imagens com CVEs críticas
  - Policy-as-code (OPA): enforce policies (ex.: "não rodar como root")

**Exemplo**:
```yaml
# Dockerfile hardened
FROM gcr.io/distroless/python3:nonroot  # Non-root by default

COPY --chown=appuser:appuser app /app
WORKDIR /app

# Run as non-root (built into distroless)
ENTRYPOINT ["python", "main.py"]

# Security: no shell, minimal attack surface
```

```yaml
# CI/CD pipeline with security gates
name: CI/CD with Security Gates

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      # SAST
      - name: Scan with Semgrep
        run: semgrep --config=p/owasp-top-ten --json -o report.json .
      
      # Fail if critical issues found
      - name: Check SAST results
        run: |
          if grep -q '"severity": "CRITICAL"' report.json; then
            echo "❌ Critical SAST findings. Failing build."
            exit 1
          fi
      
      # SCA
      - name: Scan dependencies
        run: pip-audit
      
      # Container scan (after image build)
      - name: Build and scan image
        run: |
          docker build -t myapp:${{ github.sha }} .
          trivy image myapp:${{ github.sha }}
      
      # Push only if all gates passed
      - name: Push image
        run: docker push myapp:${{ github.sha }}
```

---

### **7️⃣ Governança, Auditoria e Continuous Validation**

**Princípio**: Trate MCP servers e agentes como cidadãos de primeira classe; audit cada ação; monitore anomalias.

**Controles**:
- ✅ **Cryptographic integrity**: Assine dependências, container images, tool manifests
  - Signed commits, signed releases, signed images
  - Verificar signature on deployment
  
- ✅ **Peer review obrigatório**: Nenhum código vai para produção sem security review de outro membro do time
  - PR review: código, testes, segurança
  - Security champion reviews antes de merge
  
- ✅ **Audit logging completo**:
  - Cada tool invocation: tool name, parameters, user, timestamp
  - Acesso a dados: resource ID, operation (read/write), user, timestamp
  - Auth/authz events: login attempts, permission changes, token generation
  - Configuration changes: logging old value → new value (enable rollback)
  - Use field-level allowlists: apenas log fields necessários, redact sensíveis
  - Store logs immutably: cloud storage, WORM (write-once-read-many)
  
- ✅ **Non-Human Identity governance**: Agentes e MCP servers são NHI (non-human identities)
  - Trate-os como identidades de 1ª classe no Active Directory / Entra ID
  - Assign permissões mínimas (least privilege)
  - Audit data access por NHI continuamente
  - Detectar anomalias: NHI acessando recursos incomuns
  
- ✅ **Continuous monitoring**: Centralize logs em SIEM, configure alertas
  - Alert: spike em failed validations (ataque em progresso?)
  - Alert: high-frequency tool calls (rate limit por session está ok?)
  - Alert: unusual data patterns (tool acessando usuários fora de seu escopo?)
  - Alert: failed auth attempts (credential compromise?)

**Exemplo**:
```python
import logging
import json
from datetime import datetime

# Structured logging for MCP calls
logger = logging.getLogger("mcp_audit")

def log_tool_invocation(session_id, user_id, tool_name, params, result_status):
    """Log every tool invocation to audit trail"""
    audit_log = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": "tool_invocation",
        "session_id": session_id,
        "user_id": user_id,
        "tool_name": tool_name,
        "params": {k: v for k, v in params.items() if k not in SENSITIVE_FIELDS},
        "result_status": result_status,  # "success", "blocked", "error"
        "ip_address": get_client_ip(),
    }
    logger.info(json.dumps(audit_log))

# SIEM ingestion (e.g., Azure Monitor, Splunk)
# Configure alert: if result_status=="blocked" count > 10 in 1 minute → notify security
```

---

## 📋 Checklist de Segurança MCP (OWASP Minimum Bar)

Use este checklist antes de MCP server ir para produção:

### **Isolamento e Session Management**
- [ ] Cada sessão é completamente isolada (sem shared state)?
- [ ] Sem variáveis globais para user data?
- [ ] Resource quotas por session (memória, CPU, rate limits)?
- [ ] Cleanup determinístico quando session termina?
- [ ] Sessions expiram automaticamente?

### **Tool Design e Manifests**
- [ ] Cada tool tem signed manifest com descrição + schema + versão?
- [ ] Formal onboarding: SAST, SCA, manual review, funcional test?
- [ ] Tool behavior é validado contra anunciated description?
- [ ] Apenas campos necessários expostos ao LLM?

### **Data Validation**
- [ ] Todos inputs/outputs validados contra JSON Schema?
- [ ] Inputs sanitizados contra injection (SQL, XSS, RCE)?
- [ ] Sensitive data masked em outputs (CC, SSN, tokens)?
- [ ] Output size limits enforced?

### **Autenticação e Autorização**
- [ ] OAuth 2.1/OIDC em MCP remoto?
- [ ] Tokens short-lived (minutos)?
- [ ] Token validated on every call?
- [ ] Token delegation (RFC 8693) em uso, sem passthrough?
- [ ] Scopes/permissions checked per operation?

### **Secrets Management**
- [ ] Todos secrets em vault (nunca env vars, logs, code)?
- [ ] Secrets nunca expostos ao LLM?
- [ ] Secrets rotated periodically?
- [ ] No hardcoded credentials?

### **Deployment**
- [ ] Container non-root user?
- [ ] Minimal, hardened base image?
- [ ] Network restricted (firewall, NetworkPolicies)?
- [ ] All dependencies version-pinned, not wildcarded?
- [ ] Container images signed?

### **CI/CD Security**
- [ ] SAST scan obrigatório (fail build se crítico)?
- [ ] SCA scan obrigatório (fail build se known vulnerability)?
- [ ] Container scan before push?
- [ ] Policy-as-code gates (OPA, Azure Policy)?

### **Governança e Audit**
- [ ] Peer review obrigatório pre-deploy?
- [ ] Audit logs for tool invocations (with parameters)?
- [ ] Audit logs for auth/authz events?
- [ ] Logs stored immutably (WORM)?
- [ ] NHI (agentes, MCP servers) treated as 1st-class identities?

### **Monitoring**
- [ ] Centralized logging (SIEM)?
- [ ] Alerts for failed validations spike?
- [ ] Alerts for unusual access patterns?
- [ ] Runtime security tools active (Docker seccomp, AppArmor)?

---

## 🔗 Integração com Outras Seções

### **Com 3.2 (Azure APIM para IA)**
- APIM fornece perímetro (autenticação centralizada, rate limiting, policies)
- 8.7 fornece interior seguro (isolamento, validação, secrets)
- Juntos: **perímetro + interior = defesa em profundidade**

### **Com 8.1 (Microsoft Entra ID - Agent ID)**
- Entra ID gerencia identidade de agentes como NHI
- 8.7 exige que cada MCP call seja validado contra identidade via OAuth
- Resultado: rastreabilidade completa de quem chamou qual tool

### **Com 8.2 (Microsoft Purview)**
- Purview classifica dados (PII, confidencial, público)
- 8.7 exige sanitização de dados sensíveis antes de retornar ao LLM
- Resultado: dados corporativos protegidos por classification + sanitization

### **Com 9 (Evaluators)**
- Evaluators detectam anomalias em agentes (ex.: agent faz unexpected calls)
- 8.7 fornece audit logs com parâmetros (requisito para eval)
- Resultado: continuous monitoring de anomalias de segurança

### **Com 12 (Modelo Operacional)**
- Adicionar role "MCP Security Reviewer" no governance
- Adicionar cadência: security audit of MCP servers (trimestral)
- Adicionar SLA: CVE response time (crítico: 24h, alto: 7 dias)

---

## 🚀 Roadmap de Adoção em Ondas

### **Onda 1 — Fundações Seguras**
- ✅ Implementar isolamento de sessions
- ✅ Validação de inputs (JSON Schema)
- ✅ OAuth 2.1/OIDC para autenticação
- ✅ Secrets vault integration
- ✅ Audit logging básico
- ✅ Containerização non-root

### **Onda 2 — Governança Formal**
- ✅ Signed tool manifests
- ✅ CI/CD security gates (SAST, SCA)
- ✅ Formal onboarding approval workflow
- ✅ Centralized policy enforcement (APIM + Entra)
- ✅ Peer review obrigatório

### **Onda 3 — Continuous Validation**
- ✅ Runtime security tools (seccomp, AppArmor, mcp-watch)
- ✅ SIEM centralized + alerting
- ✅ Integration com Evaluators (detect anomalies)
- ✅ Supply chain vigilance (OpenSSF Scorecard, CVE monitoring)
- ✅ Regular penetration testing de MCP servers

---

## 📚 Referências e Atribuições

**Primary Source**: [OWASP Practical Guide for Secure MCP Server Development v1.0](https://genai.owasp.org/)  
- **Author**: OWASP GenAI Security Project
- **License**: Creative Commons CC BY-SA 4.0
- **Contributors**: Idan Habler (PhD, Cisco), Tomer Elias, Joshua Beck, e 20+ especialistas de segurança

**Complementary References**:
- [NIST AI Risk Management Framework](https://airc.nist.gov/AI-RMF)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Top 10 GenAI Red Teaming Guide](https://genai.owasp.org)
- RFC 8693: OAuth 2.0 Token Delegation
- [Azure Key Vault security best practices](https://learn.microsoft.com/en-us/azure/key-vault/general/security-features)
- [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

---

## 💡 Insight Final

> **"Segurança de MCP servers não é opcional: é o alicerce de escalabilidade segura de agentes. APIM governa o fluxo, mas segurança interna governa a confiabilidade. Implementar ambos desde o início reduz risco exponencial e acelera adoção corporativa."**

---

