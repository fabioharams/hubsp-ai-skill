## 🧩 16. Instructions and Skills in Corporate Architecture

### 🎯 Official concepts and practical interpretation

Based on Microsoft's official documentation for agents, an agent's behavior depends on the combination of:
1. **Instructions**: central guidelines that define scope, boundaries, response policy and criteria for deciding when to use knowledge, tools, topics or other agents.
2. **Skills**: reusable capabilities that extend the agent to execute specialized tasks. Depending on the platform, they may appear as pro-code skills embedded at runtime, or as actionable components (tools, topics, actions, connectors) within generative orchestration.

In architectural terms:
- **Instructions** control the "how to decide".
- **Skills** control the "how to execute".

### 🧭 Diagram 1 - How Instructions and Skills relate in the flow

```mermaid
flowchart LR
    U[Usuario ou Sistema] --> O[Orquestrador do Agente]
    I[Instructions<br/>Escopo, limites, politicas] --> O
    K[Conhecimento e contexto<br/>Dados, documentos, memoria] --> O

    O --> D{Decisao}
    D -->|Responder direto| R[Resposta fundamentada]
    D -->|Executar acao| S[Selecionar Skill]

    S --> S1[Skill de Leitura<br/>Busca, consulta, recuperacao]
    S --> S2[Skill de Acao<br/>Atualizacao, automacao, integracao]

    S1 --> C[Compor resposta]
    S2 --> C
    C --> R
```

### 🏗️ How this impacts each layer of this architecture

| Corporate architecture layer | Instructions impact | Skills impact |
|---|---|---|
| **Work IQ (experience)** | Defines tone, conversational guardrails, escalation criteria and user response boundaries. | Enables productivity actions and business flows (e.g., queries, triggers and automations) with consistent experience. |
| **Foundry IQ (orchestration)** | Defines planning policy: when to retrieve context, when to call tools and when to request human confirmation. | Materializes execution capabilities: tool calling, connectors, functions, MCP and specialized integrations. |
| **Fabric IQ/Fabric (data)** | Defines rules for use of trusted sources, governed data priority and grounding criteria. | Enables data access skills (search, SQL query, semantic retrieval) with defined scope and purpose. |
| **Guard Rails (control)** | Explicitly states prohibitions, action limits and blocking conditions to reduce abuse and behavioral drift. | Restricts skills by profile, risk and policy; separates read skills from skills with write effects. |
| **Evaluators (continuous improvement)** | Measures adherence to instructions (task adherence, policy adherence, groundedness). | Measures skill effectiveness and safety (tool call quality, execution error, fallback rate, operational impact). |

### 🛡️ Diagram 2 - Execution governance and continuous improvement

```mermaid
flowchart TD
    IN[Instructions ativas] --> PLAN[Planejamento da resposta]
    PLAN --> CALL[Chamada de Skill ou resposta direta]

    CALL --> GR{Guard Rails}
    GR -->|Aprovado| OUT[Resposta ou acao executada]
    GR -->|Bloqueado| FB[Fallback seguro ou escalonamento humano]

    OUT --> OBS[Observabilidade e telemetria]
    FB --> OBS

    OBS --> EV[Evaluators<br/>Aderencia, groundedness, risco, custo]
    EV --> ADJ[Ajuste de Instructions]
    EV --> CAT[Ajuste do catalogo de Skills]

    ADJ --> IN
    CAT --> IN
```

### 📊 Diagram 3 - Executive matrix (Instructions x Skills x Risk x Control)

```mermaid
flowchart LR
    I1[Instructions claras e especificas] --> S1[Skills minimas e especializadas]
    I1 --> S2[Skills excessivas ou sobrepostas]
    I2[Instructions ambiguas ou incompletas] --> S1
    I2 --> S2

    S1 --> R1[Risco baixo a moderado]
    S2 --> R2[Risco operacional elevado]

    R1 --> C1[Controles:
    Guardrails por perfil
    Evaluators de aderencia
    Observabilidade continua]

    R2 --> C2[Controles reforcados:
    Aprovacao humana para acoes criticas
    Segmentacao de permissao por skill
    Revisao de catalogo e desativacao de skills]
```

### 🔄 Recommended design pattern (consistent with Microsoft)

1. **Define Instructions first**: objective, scope boundary, language, constraints and escalation criteria.
2. **Attach only necessary Skills**: reduce overlap and operational risk.
3. **Describe each skill clearly**: name and description influence the orchestrator's decision on when to invoke each capability.
4. **Tie Instructions to real sources and skills**: avoid instructions for unconfigured resources.
5. **Apply validation and observability**: measure quality, safety, adherence and cost per skill.
6. **Evolve by evidence**: adjust instructions and skills catalogue based on evaluator results.

### ⚠️ Risks when Instructions and Skills are not aligned

- Ambiguous instructions: increases incorrect tool/skill calls.
- Excessive or overlapping skills: degrades orchestration and raises risk of unintended actions.
- Skills without explicit boundary: exposes the agent to operational side effects.
- Instructions misaligned with knowledge sources: reduces groundedness and trust.

### ✅ Expected outcome for the organization

When Instructions and Skills are treated as architectural assets (not just prompt configuration), the architecture gains:
1. **Predictability**: agents decide more consistently.
2. **Operational security**: smaller surface for unintended action.
3. **Scalability with governance**: new capabilities enter via controlled catalogue.
4. **Measurable evolution**: continuous improvement guided by evaluators and observability.

### 🔗 Microsoft References para Instructions e Skills

- [AI agent adoption - componentes do agente (instructions, retrieval, actions, memory)](https://learn.microsoft.com/azure/cloud-adoption-framework/ai-agents/)
- [Write agent instructions - Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/authoring-instructions)
- [Configure high-quality instructions for generative orchestration](https://learn.microsoft.com/microsoft-copilot-studio/guidance/generative-mode-guidance)
- [Use skills in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/advanced-use-skills)
- [Use skills in Foundry (preview)](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/skills)
- [Tool best practices for Microsoft Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/concepts/tool-best-practice)

---

