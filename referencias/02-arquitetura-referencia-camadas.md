## 🏗️ 2. Arquitetura de Referência (Visão Geral)

```mermaid
graph TD
    A["<b>Work IQ</b><br/>(User Layer)<br/>─────────────────<br/>Copilot, Teams, Apps<br/>Interfaces de Consumo"] 
    B["<b>Foundry IQ</b><br/>(Agents Layer)<br/>─────────────────<br/>Orquestração de agentes<br/>workflows, reasoning"]
    C["<b>Fabric IQ</b><br/>(Data Intelligence)<br/>─────────────────<br/>Semântica, ontologia<br/>métricas unificadas"]
    D["<b>Microsoft Fabric</b><br/>(Data Platform)<br/>─────────────────<br/>OneLake, Data Products<br/>Lakehouse, Warehouse"]
    
    E["🛡️ Guard Rails<br/>Controle"]
    F["✅ Evaluators<br/>Qualidade"]
    
    A --> B
    B --> C
    C --> D
    
    D -.-> E
    D -.-> F
    
    style A fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style B fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style C fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style D fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style E fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style F fill:#6BCB77,stroke:#54A05F,color:#fff,stroke-width:2px
```

### 🧠 Papel de cada camada

#### 💼 **Work IQ (User Layer)**
A camada de interface com o usuário final. Integra o **Microsoft 365 Copilot** em ferramentas já usadas cotidianamente (Teams, Word, Outlook, Excel, PowerPoint). Seu papel é:
- Fazer IA invisível: os usuários não veem complexidade, apenas resultados
- Fornecer contexto ao usuário: grounding com dados do Microsoft Graph e SharePoint
- Iniciar orquestração: encaminha solicitações complexas para camadas abaixo quando necessário
- Manter experiência familiar: nenhuma interface nova para treinar usuários

**Exemplo:** Um diretor escreve no Word "resuma esta reunião" — o Copilot (Work IQ) busca a transcrição no OneDrive, resume e insere no documento.

---

#### 🤖 **Foundry IQ (Agents Layer)**
A camada de **inteligência agêntica** — onde a lógica de decisão, reasoning e orquestração acontecem. Hospedada no **Microsoft Foundry** e **Copilot Studio**, seu papel é:
- Executar raciocínio encadeado: Claude Opus 4.6 processa contexto de 1M tokens e decide qual tool call fazer
- Orquestrar multi-agent systems: agentes comunicam entre si (via A2A protocol) para resolver problemas complexos
- Aplicar lógica de negócio: implementa regras que Work IQ não pode executar sozinha
- Fazer tool calls controlados: integra com APIs, Fabric, e MCP servers com autenticação Entra ID
- Implementar guardrails em runtime: bloqueia ou redirecionam requisições perigosas

**Exemplo:** Um agente recebe "analise por que a margem caiu" → realiza tool call 1 (busca dados financeiros no Fabric) → tool call 2 (busca benchmarks do setor via MCP) → raciocina sobre contexto → gera análise estruturada.

---

#### 📊 **Fabric IQ (Data Intelligence)**
A camada de **semântica e contexto** que enriquece os dados com significado corporativo. Constrói a verdade única sobre métricas, dimensões e relacionamentos. Seu papel é:
- Criar modelos semânticos: definem métricas (receita, margem, COGS) uma única vez
- Mapear ontologia: relacionamentos entre entidades (produtos, clientes, regiões, períodos)
- Garantir consistência: todos os agentes usam a mesma definição de "margem", "cliente", "Q3"
- Acelerar desenvolvimento: novos agentes reutilizam modelos existentes em vez de reconstruir
- Ativar análise natural: usuários perguntam em linguagem natural, modelos semânticos traduzem para SQL

**Exemplo:** Fabric IQ define que "Margem = (Receita - COGS) / Receita". Quando um agente é consultado sobre margem, ele não precisa saber a fórmula — consome a métrica já calculada.

---

#### 🗄️ **Microsoft Fabric (Data Platform)**
A base — plataforma unificada que armazena, governa e entrega dados para todas as camadas acima. Seu papel é:
- Armazenar (OneLake): repositório lógico único por tenant, construído sobre ADLS Gen2
- Transformar (Spark, Python, SQL): pipelines ETL que alimentam Bronze → Silver → Gold
- Servir (SQL Analytics Endpoint): expõe dados via endpoint T-SQL para agentes executarem queries
- Governar: integra com Purview (classificação), Entra ID (identidade), Defender (segurança)
- Viabilizar BI: Power BI acessa o mesmo Fabric sem duplicação de dados

**Exemplo:** Dados brutos (Bronze) → transformações (Silver) → Data Products prontos para agentes (Gold) → SQL Analytics Endpoint → Agentes consultam em tempo real com row-level security.

---

#### 🛡️ **Guard Rails (Transversal)**
Camada de **controle e segurança** que permeia todas as operações de agentes. Seu papel é:
- Detectar ataques: Prompt Shields bloqueia prompt injection
- Filtrar conteúdo: Content Safety verifica categorias de risco (violência, NSFW, etc.)
- Validar acesso a dados: Purview labels controlam qual agente acessa qual dado
- Sanitizar respostas: PII Detection remove informações sensíveis antes de retornar
- Auditabilidade: toda ação é registrada em Audit Logs para conformidade

**Exemplo:** Um agente tenta acessar dados rotulados como "Highly Confidential" → Guard Rail intercepta, registra tentativa, bloqueia acesso → log enviado ao Purview para auditoria.

---

#### ✅ **Evaluators (Transversal)**
Camada de **medição contínua** que valida se os agentes estão operando corretamente. Seu papel é:
- Avaliar qualidade: groundedness, task adherence, toxicity, riscos de segurança
- Detectar drift: modelo começa a performar pior? Evaluators disparam alertas
- Gerar feedback: resultados da avaliação alimentam retraining ou ajustes de prompts
- Suportar decisões: dados de qualidade justificam promote para produção ou rollback
- Integrar conformidade: Purview logs de acesso a dados sensíveis viram métricas de qualidade

**Exemplo:** Avaliador valida que resposta sobre margem usou dados corretos (groundedness = 95%), explicação foi clara (task adherence = 98%), sem vazamento de dados detectado no teste (segurança = alta) → resposta aprovada para usuário.

---

### 📌 Como Trabalham em Conjunto

```mermaid
flowchart TD
    A["👤 Usuário<br/><b>Work IQ Layer</b><br/>Solicita ação natural"]
    B["🤖 Agente (Foundry IQ)<br/>Interpreta e planeja"]
    C{"🛡️ Guard Rails<br/>Validam permissões<br/>e segurança"}
    D["📞 Tool Call<br/>Agente busca dados"]
    E["📊 Fabric IQ<br/>Semântica: traduz<br/>pergunta → query"]
    F["🗄️ Microsoft Fabric<br/>Serve dados com<br/>Row-Level Security"]
    G["🧠 Reasoning<br/>Agente combina<br/>contextos"]
    H{"✅ Evaluators<br/>Validam:<br/>Qualidade | Segurança<br/>Compliance"}
    I["📤 Resposta<br/><b>Work IQ</b><br/>Entrega ao usuário"]
    
    A -->|"solicita"| B
    B -->|"planeja"| C
    C -->|"✅ aprovam"| D
    C -->|"❌ bloqueiam"| Z["🚫 Acesso Negado<br/>+ Log Auditoria"]
    D -->|"query natural"| E
    E -->|"SQL otimizado"| F
    F -->|"dados + metadados"| G
    G -->|"análise + contexto"| H
    H -->|"✅ qualidade OK"| I
    H -->|"⚠️ rejeitar"| W["🔄 Feedback Loop<br/>Improve Prompts"]
    W -->|"retrain"| B
    I -->|"insight pronto"| A
    
    style A fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style B fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style C fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style D fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style E fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style F fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style G fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style H fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style I fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style Z fill:#D32F2F,stroke:#991212,color:#fff,stroke-width:2px
    style W fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:2px
```

**Insight:** Fabric fornece a base de verdade dos dados. Guard Rails ajudam a assegurar que apenas os agentes certos acessem os dados adequados. Evaluators reforçam a confiabilidade da resposta. Foundry IQ e Work IQ viabilizam que o usuário receba valor pronto para ação.

---

## 🔧 2.1. Especificações Técnicas por Camada

### 🗄️ Microsoft Fabric — OneLake e Delta Lake

#### 📍 **OneLake: O Lago Unificado da Organização**

**O que é:**
OneLake é um **único lago de dados lógico por tenant**, construído automaticamente sobre **Azure Data Lake Storage Gen2 (ADLS Gen2)**. É o equivalente corporativo do OneDrive para dados — provisionado por padrão quando você ativa Fabric, sem configuração adicional.

**Características principais:**
- 🎯 **Centralização:** Todos os dados de analytics da organização em um único local lógico
- 📦 **Multi-tenant:** Suporta múltiplos workspaces (departamentos, domínios) dentro do mesmo OneLake
- 🔗 **Interoperabilidade:** Acessível por todos os engines de Fabric (Spark, SQL, Power BI) simultaneamente
- 📊 **Redução de duplicação:** Evita silos de dados, reduz custos de armazenamento
- 🔐 **Governança unificada:** Políticas de acesso, classificação e conformidade aplicadas centralmente via Purview

**Estrutura física:**
Quando você cria um **Lakehouse** em Fabric, duas pastas principais são provisionadas automaticamente em OneLake:
- `/Tables` — Armazena tabelas gerenciadas em formato Delta (ideal para dados estruturados)
- `/Files` — Armazena dados em qualquer formato (CSV, Parquet, imagens, documentos)

**Exemplo de armazenamento:**

```mermaid
graph TD
    A["☁️ <b>OneLake</b><br/>(Tenant Único)<br/>─────────────────<br/>Logical Data Lake<br/>powered by ADLS Gen2"]
    
    B["🏢 Workspace-Finance<br/>─────────────────<br/>Departamento: Finanças"]
    C["📊 Lakehouse-GL<br/>General Ledger"]
    D["📁 /Tables<br/>Delta Tables<br/>Gerenciadas"]
    E["📄 /Files<br/>PDFs, CSVs<br/>Importados"]
    
    F["🏢 Workspace-Sales<br/>─────────────────<br/>Departamento: Vendas"]
    G["📦 Lakehouse-Orders<br/>Pedidos & Clientes"]
    H["📁 /Tables<br/>fct_Orders<br/>dim_Customers"]
    I["📄 /Files<br/>Uploads de<br/>Clientes"]
    
    J["🏢 Workspace-Analytics<br/>─────────────────<br/>Compartilhado"]
    K["🔗 Shortcuts Cross-Workspace<br/>Referências sem cópia<br/>para análise cruzada"]
    
    A --> B
    A --> F
    A --> J
    
    B --> C
    C --> D
    C --> E
    
    F --> G
    G --> H
    G --> I
    
    J --> K
    K -.->|"Acesso virtual a"| D
    K -.->|"Dados Finance"| H
    K -.->|"Dados Sales"| I
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:3px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style D fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style E fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style F fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style G fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style H fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style I fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style J fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style K fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:2px
```

**Leitura do diagrama:**
- 🔴 **OneLake (topo):** Tenant único, automaticamente provisionado
- 🔵 **Workspaces:** Isolam dados por departamento/domínio
- 🟣 **Lakehouses:** Concretos (Finance-GL, Sales-Orders) em cada workspace
- 🟢 **/Tables:** Armazena Delta tables gerenciadas (estruturadas)
- 🟡 **/Files:** Armazena qualquer formato (bruto)
- 🟠 **Shortcuts:** Criam referências cross-workspace sem duplicação física

---

#### 🔄 **Delta Lake: O Formato Padrão de Armazenamento**

**O que é:**
**Delta Lake** é um formato open-source mantido pela Linux Foundation que adiciona camada de transações ACID, validação de schema e histórico a arquivos Parquet. Fabric padroniza em Delta Lake — todo engine (Spark, SQL, Data Warehouse, Power BI) que escreve dados cria automaticamente Delta tables.

**Propriedades técnicas (Delta Lake vs Parquet puro):**

| Propriedade | Parquet | Delta Lake |
|---|---|---|
| **ACID Transactions** | ❌ Não | ✅ Sim (Atomicity, Consistency, Isolation, Durability) |
| **Schema Enforcement** | ❌ Não | ✅ Sim (evita dados "sujos") |
| **Time Travel** | ❌ Não | ✅ Sim (consulta dados de qualquer ponto no tempo) |
| **Data Rollback** | ❌ Não | ✅ Sim (reversão de escritas ruins) |
| **Unified Read** | ✅ Sim | ✅ Sim (todos os engines leem a mesma cópia) |
| **Query Performance** | Básico | **V-Order optimization** (muito mais rápido) |
| **Auditoria e Conformidade** | ❌ Não | ✅ Sim (Delta Lake table history) |

**Benefícios específicos para agentes de IA:**
- **Confiabilidade:** Agentes confiam que dados estão corretos (ACID previne corrupção)
- **Consistência:** Múltiplos agentes lendo simultaneamente tendem a ver versão consistente
- **Rastreabilidade:** Histórico completo de quando/quem alterou dados (auditoria)
- **Sem duplicação:** Spark transforma dados → SQL lê → Power BI visualiza **da mesma cópia**

**Exemplo:**
```
Um agente escreve dados de "margem" em Delta:
  ✅ Margem = (Receita - COGS) / Receita
  ✅ Schema enforce: se alguém tenta escrever "margens" (typo), é bloqueado
  ✅ Outro agente lê simultaneamente, vê dados consisten
  ✅ Se erro descoberto, time-travel volta para versão anterior
```

---

#### 🔗 **Shortcuts: Dados Virtualizados Sem Cópia**

**O que é:**
Shortcuts são **referências virtuais** (como links simbólicos) para dados externos. Agentes consultam dados como se estivessem no OneLake, mas são servidos de fontes externas sem cópia física.

**Fontes suportadas:**
- ✅ Azure Data Lake Storage Gen2 (ADLS Gen2)
- ✅ Amazon S3
- ✅ Google Cloud Storage
- ✅ Dataverse (Microsoft dynamics 365)
- ✅ Outros lakehouses/workspaces (cross-workspace)

**Benefícios:**
- 💰 **Zero copy:** Não duplica dados, economiza armazenamento
- ⚡ **Dados frescos:** Agentes tendem a ver a versão mais atual da fonte
- 🔐 **Segurança integrada:** Purview labels são herdados automaticamente
- 📍 **Governança centralizada:** Uma máscara de dados serve a todos os consumidores

**Exemplo:**
```
Dados de HR vivem em ADLS Gen2 externo (gerenciado por outro time)
Você cria Shortcut → aparece como tabela em seu Lakehouse
Agente executa: SELECT * FROM HR.Employees
  ↓ Fetch direto de ADLS Gen2, autenticado, com RLS aplicada
  ↓ Sem ETL, sem duplicação, governança centralizada
```

---

#### 🔍 **SQL Analytics Endpoint: Interface T-SQL para Dados**

**O que é:**
Cada Lakehouse em Fabric **provisiona automaticamente** um **SQL Analytics Endpoint** — é um endpoint TDS (Tabular Data Stream) que expõe Delta tables como tabelas SQL padrão, consultáveis com T-SQL.

**Características:**
- 🚀 **Automático:** Criado junto com o Lakehouse, zero setup
- 📖 **Read-only:** Não suporta INSERT/UPDATE/DELETE (use Spark para modificar dados)
- ⚡ **Alto performance:** Powered pelo mesmo engine do Fabric Data Warehouse
- 🔐 **Row & Column Security:** Aplica SQL granular permissions (RLS, column masking)
- 📊 **Metadata Auto-Sync:** Delta tables aparecem automaticamente como tabelas SQL
- 🔗 **Cross-workspace:** Pode consultar dados via Shortcuts de outros workspaces

**Capacidades:**
✅ `SELECT` contra Delta tables (incluindo via Shortcuts)  
✅ Criar views, funções, stored procedures em T-SQL  
✅ Aplicar row-level security (RLS) e column security  
✅ Conectar Power BI diretamente para reports  
✅ Executar queries via Azure Data Studio, SQL Server Management Studio (SSMS), qualquer cliente TDS  

**Exemplo de uso por agente:**
```sql
-- Agente no Foundry executa:
SELECT 
    p.ProductName,
    SUM(s.Amount) as TotalSales,
    AVG(s.Amount) as AvgPrice
FROM Gold.Products p
INNER JOIN Gold.Sales s ON p.ProductID = s.ProductID
WHERE s.Date >= DATEADD(month, -3, GETDATE())
GROUP BY p.ProductName
ORDER BY TotalSales DESC

-- Resultado é retornado via TDS ao agente
-- Row-level security já filtrou dados conforme permissão do agente (Entra ID)
```

**Performance considerations:**
- Sincronização automática entre Lakehouse (Spark) e SQL Analytics Endpoint: **< 1 minuto** tipicamente
- Usa **V-Order optimization:** Spark escreve Parquet otimizado para leituras SQL rápidas
- Índices automáticos: Fabric mantém estatísticas e histogramas sem ação do usuário

---

#### 🏗️ **Arquitetura Medallion: Organização em Camadas**

##### 📖 **O que é Medallion Architecture?**

A **Medallion Architecture** (também conhecida como "Bronze-Silver-Gold" ou "Delta Lake Medallion") é um **padrão de organização de dados** recomendado pela Microsoft para estruturar Lakehouses de forma escalável, governável e reutilizável. É um modelo **comprovado em escala de petabytes** (a Microsoft IDEAS, por exemplo, usa Medallion para 4 PiB de dados).

**Princípios fundamentais:**
- 🎯 **Progresso de qualidade:** Cada camada aumenta qualidade, validação e valor dos dados
- 🔄 **Reutilização:** Dados transformados uma vez, consumidos por múltiplos consumers (agentes, BI, apps)
- 🏗️ **Separação de responsabilidades:** Bronze = ingestão, Silver = transformação, Gold = negócio
- 📊 **Escalabilidade:** Suporta crescimento de terabytes a petabytes sem reorganização
- 🔐 **Governança estratificada:** Cada camada tem política própria (isolamento de workspace)

**Alternativas que Medallion não substitui:**
- ✅ Medallion funciona bem em **Data Lake** (Bronze→Silver→Gold com Spark)
- ✅ Medallion funciona bem em **Data Warehouse** (modelagem dimensional, slowly changing dimensions)
- ✅ Fabric permite **combinação:** Bronze+Silver como lakehouses, Gold como data warehouse
- ✅ Para casos muito descentralizados: **Data Mesh** (múltiplos domínios, cada com seu Medallion)

---

##### 🌍 **Fluxo Geral: De Dados Brutos a Insights**

```mermaid
graph LR
    A["🚀 Fonte de Dados<br/>─────────────────<br/>ERP, CRM, APIs,<br/>Uploads, Sensores"]
    
    B["🟤 BRONZE<br/>RAW DATA<br/>─────────────────<br/>Formato original<br/>Sem limpeza"]
    
    C["⚙️ Spark/Python<br/>Transformação<br/>Validação"]
    
    D["🟡 SILVER<br/>CLEAN DATA<br/>─────────────────<br/>Dados validados<br/>Estruturados"]
    
    E["⚙️ Spark/SQL<br/>Agregação<br/>Semântica"]
    
    F["🟢 GOLD<br/>BUSINESS DATA<br/>─────────────────<br/>Pronto para<br/>consumo"]
    
    G["📊 Consumo<br/>─────────────────<br/>Agentes, BI,<br/>Apps, Reports"]
    
    A -->|"Ingerir (as-is)"| B
    B -->|"Transformar"| C
    C -->|"Validar, limpar"| D
    D -->|"Agregar"| E
    E -->|"Semantificar"| F
    F -->|"SQL Analytics<br/>Endpoint"| G
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style C fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style D fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style E fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style F fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style G fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
```

---

##### 🟤 **Bronze Layer — RAW DATA (Dados Brutos)**

**Propósito:**
- ✅ Capturar dados **como chegam**, em formato original
- ✅ Permitir **auditoria** (rastreamento até origem)
- ✅ Permitir **reprocessamento** (se lógica Silver/Gold mudar)
- ✅ Manter histórico completo (compliance, GDPR, etc.)

**Características:**

| Aspecto | Detalhe |
|---|---|
| **Formatos** | CSV, JSON, Parquet, Delta, AVRO, imagens, PDFs — qualquer um |
| **Validação** | ❌ Nenhuma — "trust but verify later" |
| **Duplicação** | Pode ter linhas duplicadas |
| **Schema** | Loose (pode evoluir sem quebra) |
| **Retenção** | Típica: 90 dias a 2 anos (compliance) |
| **Workspace** | Privado (Bronze-Workspace) |
| **Owner** | Data Engineers (ingestão) |
| **Tecnologia** | Data Factory, Mirroring, Synapse Spark, Dataflows |

**Exemplo de conteúdo Bronze:**

```mermaid
graph TD
    A["🟤 BRONZE LAYER<br/>─────────────────<br/>Raw Data Storage<br/>Workspace: Bronze-Workspace"]
    
    B["📄 /invoices_raw/<br/>─────────────────<br/>Origem: Email, FTP<br/>Formato: CSV"]
    C["📁 2026-05-01/<br/>invoices_batch_001.csv<br/>invoices_batch_002.csv<br/>..."]
    
    D["📊 /customers_dump/<br/>─────────────────<br/>Origem: DB Export<br/>Formato: JSON"]
    E["📋 export_2026_05_01.json<br/>export_2026_04_01.json<br/>..."]
    
    F["📈 /erp_api_logs/<br/>─────────────────<br/>Origem: Streaming API<br/>Formato: JSON"]
    G["🔄 2026-05-01T*.json<br/>Logs estruturados<br/>timestamp baseado"]
    
    H["📎 /uploads/<br/>─────────────────<br/>Origem: User Uploads<br/>Formato: Mixed"]
    I["📄 contracts/ → PDFs<br/>📷 receipts/ → Imagens<br/>🗂️ other/ → Diversos"]
    
    A --> B
    A --> D
    A --> F
    A --> H
    
    B --> C
    D --> E
    F --> G
    H --> I
    
    style A fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:3px
    style B fill:#A0826D,stroke:#6F5A4A,color:#fff,stroke-width:2px
    style C fill:#C4B5A0,stroke:#9B8C7E,color:#333,stroke-width:1px
    style D fill:#A0826D,stroke:#6F5A4A,color:#fff,stroke-width:2px
    style E fill:#C4B5A0,stroke:#9B8C7E,color:#333,stroke-width:1px
    style F fill:#A0826D,stroke:#6F5A4A,color:#fff,stroke-width:2px
    style G fill:#C4B5A0,stroke:#9B8C7E,color:#333,stroke-width:1px
    style H fill:#A0826D,stroke:#6F5A4A,color:#fff,stroke-width:2px
    style I fill:#C4B5A0,stroke:#9B8C7E,color:#333,stroke-width:1px
```

**Características deste exemplo:**

| Pasta | Origem | Formato | Tamanho | Frequência | Qualidade |
|---|---|---|---|---|---|
| `/invoices_raw/` | Email, FTP manual | CSV | 10-500 MB/dia | Diária | ❌ Pode ter erros, duplicatas |
| `/customers_dump/` | DB Export (nightly) | JSON | 100 MB | Diária (1x) | ⚠️ Pode haver caracteres especiais |
| `/erp_api_logs/` | Streaming API | JSON | 5-50 GB/dia | Contínuo | ⚠️ Timestamps podem desincronizar |
| `/uploads/` | User uploads | Variado (PDF, IMG) | 1-10 GB/dia | On-demand | ❌ Pode ter vírus, corrupção |

**Fluxo recomendado para Bronze:**
1. **Mirroring** (ideal): Replicação near real-time de DB → OneLake (suporta SQL Server, MySQL, PostgreSQL, Snowflake)
2. **Data Factory:** Pipelines com 200+ conectores nativos
3. **Shortcuts:** Referenciar dados de ADLS Gen2/S3 sem cópia
4. **Dataflow Gen2:** Interface visual, transformações leves

---

##### 🟡 **Silver Layer — CLEAN DATA (Dados Validados e Estruturados)**

**Propósito:**
- ✅ **Validar** integridade: duplicatas, nulls, tipos de dados
- ✅ **Limpar** dados: padronizar formatos, remover valores inválidos
- ✅ **Estruturar** para análise: desnormalizações, agregações leves
- ✅ **Integrar** múltiplas fontes: invoices + customers + products em tabelas coerentes
- ✅ Servir como **single source of truth** para analistas e agentes

**Características:**

| Aspecto | Detalhe |
|---|---|
| **Formatos** | ✅ **Padrão: Delta Lake** (ACID, schema enforcement) |
| **Validação** | ✅ Sim — integridade referencial, tipos, ranges |
| **Duplicação** | ❌ Removidas (distinct keys garantidas) |
| **Schema** | Strict (schema enforcement — rejeita dados inválidos) |
| **Retenção** | Indefinido (dados de produção) |
| **Workspace** | Semi-privado (Silver-Workspace, acesso controlado) |
| **Owner** | Data Engineers (transformação ELT) |
| **Tecnologia** | Spark (Python, SQL, Scala), Synapse notebooks |

**Transformações típicas Bronze → Silver:**

```mermaid
graph LR
    subgraph BRONZE ["🟤 BRONZE (Raw)<br/>─────────────────"]
        A1["invoices_batch_001.csv"]
        A2["invoices_batch_002.csv"]
        A3["invoices_batch_003.csv"]
        B1["customers_dump.json"]
        B2["customers_old.json"]
        C1["products_api_export"]
        C2["products_catalog.csv"]
    end
    
    subgraph SPARK_PROCESS ["⚙️ SPARK TRANSFORMATIONS<br/>─────────────────"]
        T1["📊 Invoices<br/>DataFrame<br/><br/>1️⃣ Deduplicate<br/>2️⃣ Validate >0<br/>3️⃣ Std. dates<br/>4️⃣ Remove nulls"]
        T2["👥 Customers<br/>DataFrame<br/><br/>1️⃣ SCD Type 1<br/>2️⃣ Email format<br/>3️⃣ Join address<br/>4️⃣ Latest only"]
        T3["📦 Products<br/>DataFrame<br/><br/>1️⃣ Merge by PK<br/>2️⃣ Cost > 0<br/>3️⃣ Currency<br/>4️⃣ Active only"]
    end
    
    subgraph SILVER ["🟡 SILVER (Validated)<br/>─────────────────<br/>Always Delta Lake"]
        D1["fct_Invoices<br/>(Delta)<br/>Fact Table"]
        D2["dim_Customers<br/>(Delta)<br/>Dimension"]
        D3["dim_Products<br/>(Delta)<br/>Dimension"]
    end
    
    A1 --> T1
    A2 --> T1
    A3 --> T1
    
    B1 --> T2
    B2 --> T2
    
    C1 --> T3
    C2 --> T3
    
    T1 -->|"Write Delta<br/>with schema"| D1
    T2 -->|"Write Delta<br/>with schema"| D2
    T3 -->|"Write Delta<br/>with schema"| D3
    
    style BRONZE fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style SPARK_PROCESS fill:#FFE4B5,stroke:#FFD93D,color:#333,stroke-width:2px
    style SILVER fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    
    style A1 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style A2 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style A3 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style B1 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style B2 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style C1 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style C2 fill:#A0826D,stroke:#6F5A4A,color:#fff
    
    style T1 fill:#FFE4B5,stroke:#FFD93D,color:#333
    style T2 fill:#FFE4B5,stroke:#FFD93D,color:#333
    style T3 fill:#FFE4B5,stroke:#FFD93D,color:#333
    
    style D1 fill:#C4B5A0,stroke:#9B8C7E,color:#333
    style D2 fill:#C4B5A0,stroke:#9B8C7E,color:#333
    style D3 fill:#C4B5A0,stroke:#9B8C7E,color:#333
```

**Fluxo por categoria:**

| Origem | Processamento Spark | Validações | Saída Silver |
|---|---|---|---|
| **Invoices** (múltiplos CSVs) | Spark DataFrame merge | ✅ Dedup by ID<br/>✅ Amount > 0<br/>✅ Date standard<br/>✅ Remove nulls | **fct_Invoices** (Delta) |
| **Customers** (JSON exports) | Spark DataFrame merge | ✅ Latest version (SCD1)<br/>✅ Email format<br/>✅ Join address data<br/>✅ Active only | **dim_Customers** (Delta) |
| **Products** (API export) | Spark DataFrame merge | ✅ Merge by ProductID<br/>✅ Cost > 0<br/>✅ Currency aligned<br/>✅ Active flag | **dim_Products** (Delta) |

**Garantias de qualidade Silver:**
- 🔐 **ACID transactions** — nenhum dado parcial ou corrompido
- 🔑 **Primary key unique** — sem duplicatas por ID
- 📊 **Schema strict** — rejeita dados fora do tipo esperado
- ✅ **Data completeness** — nenhum NULL em colunas críticas
- 🔄 **Referential integrity** — FK relationships validadas

**Estrutura típica Silver:**

```mermaid
graph TD
    A["🟡 SILVER LAYER<br/>─────────────────<br/>Dados Validados"]
    
    B["📊 FACTS<br/>(Medidas)"]
    C["fct_Invoices<br/>fct_Orders<br/>fct_Sales"]
    
    D["🔑 DIMENSIONS<br/>(Contexto)"]
    E["dim_Customers<br/>dim_Products<br/>dim_Calendar"]
    
    F["⏰ METADATA<br/>(Lineage)"]
    G["tbl_LoadHistory<br/>tbl_DataQuality<br/>tbl_Lineage"]
    
    A --> B
    A --> D
    A --> F
    
    B --> C
    D --> E
    F --> G
    
    style A fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style B fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style C fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style D fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style E fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style F fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style G fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
```

---

##### 🟢 **Gold Layer — BUSINESS DATA (Dados Prontos para Negócio)**

**Propósito:**
- ✅ **Agregar** dados em dimensões de negócio (produto, região, período)
- ✅ **Calcular** métricas (receita, margem, COGS, KPIs)
- ✅ **Semantificar** dados com nomes e lógica corporativa compreensível
- ✅ Expor como **Data Products** consumíveis por agentes, BI, apps
- ✅ Garantir **performance** (dados pré-agregados, índices, estatísticas)

**Características:**

| Aspecto | Detalhe |
|---|---|
| **Formatos** | ✅ **Padrão: Delta Lake** (com V-Order optimization) |
| **Agregação** | ✅ Sim — fatos agregados por dimensões de negócio |
| **Cálculos** | ✅ Métricas corporativas pré-calculadas |
| **Schema** | Semantic — nomes de negócio (não técnicos) |
| **Retenção** | Indefinido (dados de histórico completo) |
| **Workspace** | Público/Semi-público (Gold-Workspace, acesso amplo) |
| **Owner** | Analytics Engineers / Business Analysts |
| **Exposure** | SQL Analytics Endpoint, Power BI, APIs para agentes |
| **Tecnologia** | Spark (agregações), SQL (views, stored procs), Power BI (semantic models) |

**Estrutura típica Gold (Data Products):**

```mermaid
graph TD
    A["🟢 GOLD LAYER<br/>─────────────────<br/>Data Products<br/>Business Ready"]
    
    B["📈 PRODUCT: Revenue"]
    C["fct_DailyRevenue<br/>(Product × Region × Day)"]
    D["fct_MonthlyRevenue<br/>(Product × Region × Month)"]
    E["dim_Product<br/>dim_Region<br/>dim_Calendar"]
    
    F["💰 PRODUCT: Profitability"]
    G["fct_Margins<br/>(COGS, Gross, Operating, Net)"]
    H["fct_CostCenter<br/>(Cost allocation)"]
    I["dim_CostCenter<br/>dim_GLAccount"]
    
    J["👥 PRODUCT: Customers"]
    K["dim_Customer360<br/>(Lifetime Value, Segment)"]
    L["fct_CustomerActivity<br/>(Orders, Spend, Churn)"]
    
    M["📊 Consumption<br/>─────────────────<br/>Agentes, BI, Apps"]
    
    A --> B
    A --> F
    A --> J
    
    B --> C
    B --> D
    B --> E
    
    F --> G
    F --> H
    F --> I
    
    J --> K
    J --> L
    
    C --> M
    D --> M
    G --> M
    K --> M
    L --> M
    
    style A fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:3px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style D fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style E fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style F fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style G fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style H fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style I fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style J fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style K fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style L fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style M fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
```

**Exemplos de tabelas Gold:**

```mermaid
graph TD
    A["🟢 GOLD LAYER<br/>─────────────────<br/>Data Products<br/>Business Ready"]
    
    B1["📈 PRODUCT: Revenue<br/>─────────────────"]
    B2["📊 fct_DailyRevenue"]
    B3["📋 Columns:<br/>Date, ProductID, RegionID<br/>RevenueAmount, UnitsSold, COGS<br/>─────────────────<br/>📌 SLA: Daily 2 AM UTC<br/>🔐 Sensitivity: Internal"]
    
    C1["💰 PRODUCT: Profitability<br/>─────────────────"]
    C2["📊 fct_Margins"]
    C3["📋 Columns:<br/>Date, ProductID<br/>GrossMargin, OperatingMargin, NetMargin<br/>─────────────────<br/>⚙️ Formula: (Revenue-COGS)/Revenue<br/>📌 SLA: Daily 3 AM UTC<br/>🔐 Sensitivity: Confidential<br/>(RLS by cost center)"]
    
    D1["👥 PRODUCT: Customer 360<br/>─────────────────"]
    D2["👤 dim_Customer"]
    D3["📋 Columns:<br/>CustomerID, Segment<br/>Lifetime Value, Churn Risk<br/>─────────────────<br/>🔒 RLS: By region<br/>🔐 Sensitivity: Confidential (PII)<br/>📌 SLA: Daily 4 AM UTC"]
    
    E["SQL Analytics Endpoint<br/>─────────────────<br/>Read-only access<br/>All Gold products"]
    
    A --> B1
    A --> C1
    A --> D1
    
    B1 --> B2
    B2 --> B3
    
    C1 --> C2
    C2 --> C3
    
    D1 --> D2
    D2 --> D3
    
    B3 --> E
    C3 --> E
    D3 --> E
    
    style A fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:3px
    style B1 fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style B2 fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style B3 fill:#A5D6A7,stroke:#81C784,color:#333,stroke-width:2px
    style C1 fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C2 fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style C3 fill:#A5D6A7,stroke:#81C784,color:#333,stroke-width:2px
    style D1 fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style D2 fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style D3 fill:#A5D6A7,stroke:#81C784,color:#333,stroke-width:2px
    style E fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:3px
```

**Resumo de Data Products Gold:**

| Product | Tabela | Propósito | Atualizado | Acesso |
|---|---|---|---|---|
| **Revenue** | `fct_DailyRevenue` | Receita por produto-região-dia | 2 AM UTC | 🔵 Internal |
| **Profitability** | `fct_Margins` | Margens bruta, operacional, líquida | 3 AM UTC | 🟡 Confidential (RLS) |
| **Customer 360** | `dim_Customer` | Cliente + lifetime value + churn risk | 4 AM UTC | 🔴 Confidential (PII + RLS) |

**Garantias por Data Product:**
- ✅ **Documentação:** Dicionário de dados, fórmulas, lineage
- ✅ **SLA:** Horário garantido de atualização diária
- ✅ **Segurança:** Sensitivity labels + Row-level security automática
- ✅ **Descoberta:** Indexado em Data Catalog (Purview)
- ✅ **Auditoria:** Acesso registrado em Audit Logs

---

##### 🏢 **Workspace Isolation (Recomendação Microsoft)**

Microsoft recomenda **criar cada camada em workspace separado** para melhor governança:

```mermaid
graph LR
    A["🏢 Workspace-Bronze<br/>─────────────────<br/>Acesso: Privado<br/>Owner: Data Engineers"]
    B["🏢 Workspace-Silver<br/>─────────────────<br/>Acesso: Semi-privado<br/>Owner: Data Engineers"]
    C["🏢 Workspace-Gold<br/>─────────────────<br/>Acesso: Público<br/>Owner: Analytics Eng."]
    D["👥 Agentes/BI/Apps<br/>─────────────────<br/>Consumem Gold<br/>via SQL Endpoint"]
    
    A -->|"Data moves via<br/>Spark jobs"| B
    B -->|"Data moves via<br/>Spark jobs"| C
    C -->|"Read-only via<br/>SQL Endpoint"| D
    
    style A fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style B fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style C fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style D fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
```

**Benefícios:**
- 🔐 **Isolamento:** Bronze (raw) não exposto a usuários finais
- 👥 **RBAC granular:** Diferentes permissões por layer
- 📊 **Billing separado:** Rastrear custos de cada fase do pipeline
- 🚀 **Performance:** Capacity dedicada para cada workload
- 🔄 **Evolução:** Mudar Silver/Gold sem afetar ingestão Bronze

---

##### 📚 **Padrões de Implementação em Fabric**

Existem **3 padrões principais** recomendados pela Microsoft para implementar Medallion em Fabric. A escolha depende da **maturidade do time, complexidade dos dados e requisitos de BI**.

---

###### **OPÇÃO 1️⃣ — Três Lakehouses (um por camada)**

**Quando usar:**
- ✅ Times de **Data Engineering puros** (sem BI tradicional)
- ✅ Arquitetura **amplamente aberta** (Delta Lake, sem esquema dimensional)
- ✅ Foco em **análises exploratórias e agentes de IA**
- ✅ Equipes que dominam **Spark/Python** mais que SQL

**Arquitetura:**

```mermaid
graph TD
    A["🏢 Workspace-Bronze<br/>─────────────────<br/>Acesso: Privado"]
    B["📦 Lakehouse-Raw<br/>Bronze Layer"]
    C["📁 /Tables<br/>Delta raw"]
    D["📄 /Files<br/>Any format"]
    
    E["🏢 Workspace-Silver<br/>─────────────────<br/>Acesso: Semi-privado"]
    F["📦 Lakehouse-Curated<br/>Silver Layer"]
    G["📁 /Tables<br/>Delta validated"]
    
    H["🏢 Workspace-Gold<br/>─────────────────<br/>Acesso: Público"]
    I["📦 Lakehouse-Products<br/>Gold Layer"]
    J["📁 /Tables<br/>Delta aggregated"]
    K["📊 SQL Analytics<br/>Endpoint"]
    
    L["👥 Consumers<br/>─────────────────<br/>Agentes, BI, Apps"]
    
    A --> B
    B --> C
    B --> D
    
    E --> F
    F --> G
    
    H --> I
    I --> J
    I --> K
    
    G -->|"Spark ETL"| J
    K -->|"SQL Query"| L
    
    style A fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style B fill:#A0826D,stroke:#6F5A4A,color:#fff,stroke-width:2px
    style C fill:#C4B5A0,stroke:#9B8C7E,color:#333
    style D fill:#C4B5A0,stroke:#9B8C7E,color:#333
    
    style E fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style F fill:#D4B896,stroke:#A68A6F,color:#fff,stroke-width:2px
    style G fill:#E5D7C8,stroke:#B5A696,color:#333
    
    style H fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style I fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style J fill:#A5D6A7,stroke:#81C784,color:#333
    style K fill:#81C784,stroke:#66BB6A,color:#fff
    
    style L fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
```

**Características:**

| Aspecto | Detalhe |
|---|---|
| **Lakehouses** | 3 separados (Bronze, Silver, Gold) |
| **Formatos** | Bronze: múltiplos, Silver: Delta, Gold: Delta |
| **Computação** | Spark (transformação), SQL (queries) |
| **BI Support** | Limitado — SQL Analytics Endpoint apenas |
| **Escalabilidade** | ⭐⭐⭐⭐⭐ Excelente para data lakes |
| **Governança** | ⭐⭐⭐⭐ Isolamento por workspace |
| **Complexidade** | Média (3 lakehouses para manter) |
| **Custo** | 💰 3 capacidades = custos 3x |

**Casos de uso reais:**
- Agências de Big Data que servem múltiplos clientes
- Organizações com cultura Data Science (Python/R dominant)
- Processamento de petabytes com Spark
- Análises exploratórias e machine learning

---

###### **OPÇÃO 2️⃣ — Lakehouse Bronze+Silver, Data Warehouse Gold** ⭐ **RECOMENDADO**

**Quando usar:**
- ✅ Times com **experiência em BI tradicional** (Star schema, dimensional modeling)
- ✅ Necessidade de **Power BI + SQL Reports** como consumidores
- ✅ Análises **estruturadas e repetíveis** (não exploratórias)
- ✅ Equipes que dominam **SQL/DAX** mais que Spark/Python

**Arquitetura:**

```mermaid
graph TD
    A["🏢 Workspace-Silver<br/>─────────────────<br/>Acesso: Semi-privado"]
    B["📦 Lakehouse-Staging<br/>Bronze+Silver"]
    C["📁 /Files<br/>Bronze raw<br/>Any format"]
    D["📁 /Tables<br/>Silver validated<br/>Delta tables"]
    
    E["⚡ ELT Pipeline<br/>─────────────────<br/>Spark/Python<br/>Dataflows"]
    
    F["🏢 Workspace-Gold<br/>─────────────────<br/>Acesso: Público"]
    G["🏗️ Data Warehouse<br/>Gold Layer<br/>Dimensional Schema"]
    
    H["📊 Fact Tables"]
    I["fct_Sales<br/>fct_Orders<br/>fct_Inventory"]
    
    J["🔑 Dimension Tables"]
    K["dim_Product<br/>dim_Customer<br/>dim_Calendar"]
    
    L["📈 Power BI<br/>─────────────────<br/>Direct Lake Mode"]
    
    M["📋 SQL Reports<br/>─────────────────<br/>Warehouse endpoint"]
    
    N["🤖 Agentes IA<br/>─────────────────<br/>SQL queries"]
    
    A --> B
    B --> C
    B --> D
    
    D --> E
    E --> F
    
    F --> G
    G --> H
    G --> J
    H --> I
    J --> K
    
    I --> L
    K --> L
    
    I --> M
    K --> M
    
    I --> N
    K --> N
    
    style A fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style B fill:#D4B896,stroke:#A68A6F,color:#fff,stroke-width:2px
    style C fill:#E5D7C8,stroke:#B5A696,color:#333
    style D fill:#E5D7C8,stroke:#B5A696,color:#333
    
    style E fill:#FFE4B5,stroke:#FFD93D,color:#333,stroke-width:2px
    
    style F fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style G fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    
    style H fill:#81C784,stroke:#66BB6A,color:#fff
    style I fill:#A5D6A7,stroke:#81C784,color:#333
    
    style J fill:#81C784,stroke:#66BB6A,color:#fff
    style K fill:#A5D6A7,stroke:#81C784,color:#333
    
    style L fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style M fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style N fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
```

**Características:**

| Aspecto | Detalhe |
|---|---|
| **Lakehouses** | 1 (Bronze+Silver combinados) |
| **Warehouses** | 1 (Gold em DW dimensional) |
| **Formatos** | Bronze: múltiplos, Silver: Delta, Gold: DW schema |
| **Computação** | Spark (ETL), SQL (DW queries) |
| **BI Support** | ⭐⭐⭐⭐⭐ Native Power BI + SQL Reports |
| **Escalabilidade** | ⭐⭐⭐⭐ Bom para BI enterprise |
| **Governança** | ⭐⭐⭐⭐ Isolamento Bronze/Silver vs Gold |
| **Complexidade** | Média (1 Lakehouse + 1 DW) |
| **Custo** | 💰💰 2 capacidades (mais eficiente) |

**Casos de uso reais:**
- Organizações com BI maduro (Power BI em escala)
- Empresas em transição de data warehouse tradicional
- Análises estruturadas com modelos dimensionais
- Relatórios operacionais repetíveis

**Benefício único:** Usa **Direct Lake mode** do Power BI — carrega dados diretamente de Delta tables no DW, reduzindo a necessidade de refreshes caros de datasets Import.

---

###### **OPÇÃO 3️⃣ — Medallion + Data Mesh** (Para grandes organizações)

**Quando usar:**
- ✅ Organizações **muito grandes** (200+ dados engineers)
- ✅ **Múltiplos domínios** autônomos (Finance, Sales, Operations, HR, etc.)
- ✅ Necessidade de **federação de dados** (cada domínio possui seus dados)
- ✅ Cada domínio opera seu próprio **Medallion completo**

**Arquitetura:**

```mermaid
graph TB
    A["📊 DATA MESH TOPOLOGY<br/>─────────────────<br/>Federated Domains<br/>Cada domínio = Medallion completo"]
    
    B["🏢 Domain-Finance<br/>─────────────────"]
    B1["🟤 Bronze"]
    B2["🟡 Silver"]
    B3["🟢 Gold<br/>Data Products:<br/>Revenue, Costs,<br/>Margins"]
    
    C["🏢 Domain-Sales<br/>─────────────────"]
    C1["🟤 Bronze"]
    C2["🟡 Silver"]
    C3["🟢 Gold<br/>Data Products:<br/>Orders, Pipeline,<br/>Forecast"]
    
    D["🏢 Domain-Operations<br/>─────────────────"]
    D1["🟤 Bronze"]
    D2["🟡 Silver"]
    D3["🟢 Gold<br/>Data Products:<br/>Inventory,<br/>Logistics"]
    
    E["🏢 Domain-Analytics<br/>─────────────────<br/>Workspace Compartilhado"]
    E1["🔗 Shortcuts<br/>Cross-Domain"]
    E2["📊 Data Catalog<br/>(Purview)"]
    E3["🔐 Governance<br/>Hub"]
    
    F["👥 Consumers<br/>─────────────────<br/>Agentes, BI, Apps"]
    
    A --> B
    A --> C
    A --> D
    A --> E
    
    B --> B1
    B --> B2
    B --> B3
    
    C --> C1
    C --> C2
    C --> C3
    
    D --> D1
    D --> D2
    D --> D3
    
    B3 -->|"Shortcut"| E1
    C3 -->|"Shortcut"| E1
    D3 -->|"Shortcut"| E1
    
    E --> E1
    E --> E2
    E --> E3
    
    E1 --> F
    E2 --> F
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:3px
    
    style B fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style B1 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style B2 fill:#C9A961,stroke:#9B7E48,color:#fff
    style B3 fill:#50C878,stroke:#3A9B5C,color:#fff
    
    style C fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style C1 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style C2 fill:#C9A961,stroke:#9B7E48,color:#fff
    style C3 fill:#50C878,stroke:#3A9B5C,color:#fff
    
    style D fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style D1 fill:#A0826D,stroke:#6F5A4A,color:#fff
    style D2 fill:#C9A961,stroke:#9B7E48,color:#fff
    style D3 fill:#50C878,stroke:#3A9B5C,color:#fff
    
    style E fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style E1 fill:#7B68EE,stroke:#5A4DB0,color:#fff
    style E2 fill:#FF9800,stroke:#E65100,color:#fff
    style E3 fill:#FF9800,stroke:#E65100,color:#fff
    
    style F fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
```

**Características:**

| Aspecto | Detalhe |
|---|---|
| **Domínios** | 3+ (cada um = Medallion completo) |
| **Propriedade** | Cada domínio = team autônomo |
| **Integração** | Shortcuts + OneLake cross-workspace |
| **Governança** | Hub centralizado (Purview) |
| **Escalabilidade** | ⭐⭐⭐⭐⭐ Petabyte-scale |
| **Autonomia** | ⭐⭐⭐⭐⭐ Máxima independência |
| **Complexidade** | Alta (requer disciplina) |
| **Custo** | 💰💰💰 Múltiplas capacidades |

**Princípios Data Mesh:**
1. **Domain ownership:** Cada domínio = proprietário de seus dados
2. **Data as product:** Gold layers são "Data Products" com SLA
3. **Self-serve infrastructure:** Cada domínio provisiona seu próprio Medallion
4. **Federated governance:** Políticas centrais (Purview), implementação local

**Casos de uso reais:**
- Grandes conglomerados (múltiplas filiais, geografias)
- Organizações fintech (cada serviço = domínio independente)
- Empresas em scaling (100+ engenheiros de dados)
- Indústria de mídia (múltiplos estúdios/plataformas)

---

##### 📋 **Matriz de Decisão: Qual Padrão Escolher?**

```mermaid
graph TD
    A["Qual é o seu caso?"]
    
    B{"Time é<br/>Spark-first ou<br/>SQL-first?"}
    C{"Tamanho da<br/>organização?"}
    
    D{"Spark/Python<br/>dominant"}
    E{"SQL/BI<br/>dominant"}
    F{"Pequeno<br/>10-50 eng"}
    G{"Grande<br/>100+ eng"}
    
    B -->|"Spark"| D
    B -->|"SQL"| E
    
    C -->|"Pequeno"| F
    C -->|"Grande"| G
    
    D -->|"+ análises<br/>exploratórias"| H["✅ OPÇÃO 1<br/>Três Lakehouses"]
    E -->|"+ Power BI<br/>reports"| I["✅ OPÇÃO 2<br/>Lakehouse +<br/>Warehouse<br/><br/><br/>⭐ RECOMENDADO"]
    
    F -->|"Sem BI"| J["✅ OPÇÃO 1<br/>Três Lakehouses"]
    G -->|"Múltiplos<br/>domínios"| K["✅ OPÇÃO 3<br/>Data Mesh"]
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style C fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style D fill:#4A90E2,stroke:#2E5C8A,color:#fff
    style E fill:#4A90E2,stroke:#2E5C8A,color:#fff
    style F fill:#4A90E2,stroke:#2E5C8A,color:#fff
    style G fill:#4A90E2,stroke:#2E5C8A,color:#fff
    style H fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style I fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:3px
    style J fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style K fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
```

---

**Referências Microsoft:**
- [Understand medallion lakehouse architecture for Microsoft Fabric with OneLake](https://learn.microsoft.com/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [Lakehouse end-to-end scenario: overview and architecture](https://learn.microsoft.com/fabric/data-engineering/tutorial-lakehouse-introduction)
- [Data Platform end-to-end with Microsoft Fabric](https://learn.microsoft.com/azure/architecture/example-scenario/dataplate2e/data-platform-end-to-end)

---

#### 📊 **Data Products: Pacotes de Dados para Reutilização**

**O que é:**
Um **Data Product** é um conjunto curado de tabelas Gold com semântica clara, documentação, e SLA de qualidade — pronto para ser reutilizado por múltiplos agentes e usuários.

**Características:**
- 📖 **Documentado:** Dicionário de dados, lineage, business rules claras
- 🎯 **Semanticamente claro:** "Revenue = Sales Price × Quantity", não ambíguo
- 🔐 **Seguro:** Row-level security aplicado automaticamente via Purview labels
- ⚙️ **Operacionalizado:** Pipelines de refresh ajudam a manter dados frescos, com SLA de atualização
- 📈 **Versionado:** Mudanças de schema são controladas, compatibilidade mantida
- 📣 **Descobrível:** Catálogo (Data Catalog in Purview) indexa e descreve

**Exemplo de Data Product:**

```mermaid
graph TD
    A["🎁 Data Product: Sales Analytics<br/>─────────────────<br/>Owner: Sales Analytics Team<br/>Sensitivity: Internal"]
    
    B["📊 TABELAS GOLD<br/>─────────────────"]
    
    C["📈 fct_Orders<br/>(Fact Table)"]
    C1["Columns:<br/>OrderID, CustomerID,<br/>ProductID, OrderAmount,<br/>OrderDate"]
    C2["Metrics:<br/>TotalRevenue<br/>AverageOrderValue<br/>UnitsSold"]
    
    D["👥 dim_Customers<br/>(Dimension)"]
    D1["Columns:<br/>CustomerID, Name<br/>Segment, Region"]
    D2["🔒 RLS:<br/>Por região<br/>Agentes veem<br/>só sua região"]
    
    E["📖 DOCUMENTAÇÃO<br/>─────────────────"]
    E1["📝 Business Rules:<br/>Revenue = SUM(OrderAmount)<br/>em moeda local<br/><br/>Segment = Behavioral<br/>classification updated monthly"]
    
    F["⏰ OPERACIONALIZAÇÃO<br/>─────────────────"]
    F1["📌 Freshness SLA:<br/>Updated nightly 2 AM UTC<br/>&lt; 1 hour após source refresh<br/><br/>🔄 Versioning:<br/>Schema changes controlled<br/>Compatibilidade mantida"]
    
    G["🔍 DESCOBERTA<br/>─────────────────"]
    G1["📚 Data Catalog<br/>(Purview)<br/>Indexado e descobrível<br/>Lineage visível"]
    
    A --> B
    A --> E
    A --> F
    A --> G
    
    B --> C
    B --> D
    
    C --> C1
    C --> C2
    
    D --> D1
    D --> D2
    
    E --> E1
    F --> F1
    G --> G1
    
    style A fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:3px
    style B fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style C fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style C1 fill:#A5D6A7,stroke:#81C784,color:#333
    style C2 fill:#A5D6A7,stroke:#81C784,color:#333
    style D fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style D1 fill:#A5D6A7,stroke:#81C784,color:#333
    style D2 fill:#FF9800,stroke:#E65100,color:#fff
    style E fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style E1 fill:#CE93D8,stroke:#AB47BC,color:#fff
    style F fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style F1 fill:#CE93D8,stroke:#AB47BC,color:#fff
    style G fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style G1 fill:#CE93D8,stroke:#AB47BC,color:#fff
```

**Componentes do Data Product:**

| Componente | O que é | Responsabilidade |
|---|---|---|
| **Fact Tables** | `fct_Orders` — medidas (OrderAmount, UnitsSold) | Núcleo analítico |
| **Dimensions** | `dim_Customers` — contexto (Name, Segment) | Contexto de negócio |
| **Metrics** | TotalRevenue, AverageOrderValue | KPIs pré-calculados |
| **RLS** | Row-level security por região | Segurança + conformidade |
| **Documentação** | Business rules, fórmulas, glossário | Semântica clara |
| **SLA** | Updated 2 AM UTC, < 1h lag | Confiabilidade |
| **Versionamento** | Schema changes com compatibilidade | Evolução controlada |
| **Catálogo** | Purview indexa e descreve | Descoberta |

**Uso por Agente:**
```python
# Agente no Foundry
from azure.ai.projects import AIProjectClient
import pyodbc

# Conecta via SQL Analytics Endpoint (autenticado com Agent ID via Entra)
conn = pyodbc.connect(
    'Driver=ODBC Driver 17 for SQL Server;'
    'Server=fabric.database.windows.net;'
    'Database=Sales_Analytics;'
    'Authentication=ActiveDirectoryMSI'
)

# Consulta Data Product Gold (RLS automática)
cursor = conn.cursor()
cursor.execute('''
    SELECT OrderAmount, CustomerSegment, OrderDate
    FROM fct_Orders
    WHERE OrderDate >= DATEADD(month, -3, GETDATE())
''')

# Agent raciocina com dados
data = cursor.fetchall()
# ... Claude processa contexto, gera análise
```

---

#### 🔐 **Integração com Governança (Purview + Entra)**

A integração entre **Microsoft Entra Agent ID**, **Microsoft Purview** e **Microsoft Fabric** cria uma arquitetura de segurança multinível onde cada agente é autenticado como uma identidade corporativa distinta (não apenas um aplicativo genérico), e cada acesso a dados é governado por classificação de sensibilidade e regras de controle de acesso.

##### 🪪 **Entra ID Agent Identity - Identidades para IA**

Microsoft Entra Agent ID é um framework de segurança propositalmente construído para agentes de IA autônomos. Diferentemente de um service principal tradicional, o Agent ID oferece:

| Aspecto | Service Principal (Legado) | Entra Agent ID (Novo) |
|---------|-------------------------|---------------------|
| **Propósito** | Aplicativo genérico | Agente de IA específico |
| **Contexto** | Sem identidade real | Identidade Zero Trust com contexto |
| **Autenticação** | Username/senha ou certificado | JWT + contexto de risco |
| **Autorização** | Baseado em função (RBAC) | Baseado em função + risco + contexto |
| **Auditoria** | Logs básicos | Logs estruturados de agente com intenção |
| **Governança** | Manual por grupo | Automática via policy de ciclo de vida |
| **Conditional Access** | Limitado | Suporta policies por agent |

**Como funciona Agent ID:**

1. **Criação:** Cada agente recebe uma identidade única no Entra ID (ex: `eng-sales-agent-001`)
2. **Autenticação:** Agent solicita token JWT usando `ClientSecret` ou `Certificate`
3. **JWT contém:**
   - `app_displayname`: "Eng Sales Agent"
   - `appid`: GUID único do agent
   - `roles`: ["Data Explorer", "Contributor"] 
   - `oid`: ID de objeto do agent
4. **Zero Trust:** Token é enviado a cada request com contexto de risco
5. **Renovação:** Token expira (1h padrão) e agent deve re-autenticar

**Exemplo de JWT Payload:**
```json
{
  "aud": "https://database.windows.net",
  "iss": "https://sts.windows.net/12345678-1234-1234-1234-123456789012/",
  "iat": 1704067200,
  "nbf": 1704067200,
  "exp": 1704070800,
  "acr": "1",
  "appid": "87654321-4321-4321-4321-210987654321",
  "appidacr": "1",
  "email": "eng-sales-agent-001@company.onmicrosoft.com",
  "name": "Engineering Sales Agent",
  "oid": "11111111-1111-1111-1111-111111111111",
  "roles": ["Data Explorer", "Contributor"],
  "rh": "0.ARcAoP...",
  "scp": "user_impersonation",
  "sub": "oL....",
  "tid": "12345678-1234-1234-1234-123456789012",
  "unique_name": "eng-sales-agent-001@company.onmicrosoft.com",
  "upn": "eng-sales-agent-001@company.onmicrosoft.com",
  "uti": "....",
  "ver": "1.0"
}
```

---

##### 🏷️ **Purview Sensitivity Labels - Hierarquia e Classificação**

Sensitivity labels em Purview fornecem classificação multinível com proteção progressiva:

| Label | Descrição | Cenário de Uso | Proteção | Acesso por Agente |
|-------|-----------|---|----------|---|
| **Public** | Sem restrição, pode ser compartilhado externamente | Dados públicos de marketing, preços públicos | Nenhuma criptografia | ✅ Automático |
| **Internal** | Apenas para uso interno, não sensível | Documentos operacionais, comunicados | Marca de água | ✅ Automático |
| **Confidential** | Dados comerciais sensíveis, restrito a funcionários autorizados | Contratos, planos de vendas, análises internas | Criptografia + Restrição de Acesso | ⚠️ Requer Conditional Access |
| **Highly Confidential** | Dados extremamente sensíveis, máxima proteção | Dados financeiros, PII, segredos comerciais | Criptografia forte + Restrição rígida | ❌ Bloqueado (human-in-loop obrigatório) |

**Hierarquia de Labels em Purview:**

```mermaid
graph TD
    A["Microsoft Purview<br/>Sensitivity Labels"]
    B["Public"]
    C["Internal"]
    D["Confidential"]
    E["Highly Confidential"]
    
    B1["Sem proteção<br/>Sem restrição"]
    C1["Marca de água interna<br/>Visível em metadados"]
    D1["Criptografia<br/>Acesso restrito<br/>Requires Co-Author"]
    E1["Máxima proteção<br/>Requer aprovação<br/>Apenas uso interno"]
    
    D2["Confidential \ All Employees<br/>Todos podem visualizar"]
    D3["Confidential \ Specific People<br/>Apenas especificados"]
    
    E2["Highly Confidential \ Restricted<br/>Máxima restrição"]
    E3["Highly Confidential \ Executive<br/>C-level only"]
    
    A --> B
    A --> C
    A --> D
    A --> E
    
    B --> B1
    C --> C1
    D --> D1
    E --> E1
    
    D --> D2
    D --> D3
    
    E --> E2
    E --> E3
    
    style B fill:#90EE90,stroke:#228B22,color:#000
    style C fill:#87CEEB,stroke:#0047AB,color:#fff
    style D fill:#FFB347,stroke:#FF8C00,color:#000
    style E fill:#FF6347,stroke:#CC0000,color:#fff
```

**Aplicação de Labels em Fabric:**

Quando dados são ingeridos no OneLake, Purview pode aplicar labels automaticamente:

```mermaid
graph TD
    A["☁️ OneLake<br/>─────────────<br/>Tenant Único"]
    
    B["🏢 Sales_Analytics<br/>Workspace"]
    C["📊 Warehouse"]
    
    D["📋 fct_Orders<br/>🟡 Confidential<br/>Dados de vendas"]
    E["👥 dim_Customer<br/>🔴 Highly Confidential<br/>PII: CPF, email, fone"]
    F["📦 dim_Product<br/>🟢 Public<br/>Catálogo público"]
    G["💰 fct_Revenue<br/>🟡 Confidential<br/>Dados financeiros"]
    
    A --> B
    B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:3px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style D fill:#FFB347,stroke:#FF8C00,color:#000
    style E fill:#FF6347,stroke:#CC0000,color:#fff
    style F fill:#90EE90,stroke:#228B22,color:#000
    style G fill:#FFB347,stroke:#FF8C00,color:#000
```

---

##### 🔒 **Row-Level Security (RLS) - Filtragem por Contexto do Agente**

O SQL Analytics Endpoint em Fabric suporta RLS via `EXECUTE AS` com Agent ID:

```sql
-- Tabela base: fct_Orders
SELECT 
    OrderID, 
    Amount, 
    CustomerID, 
    OrderDate,
    SensitivityLabel  -- Coluna adicionada por Purview
FROM [dbo].[fct_Orders]

-- Política RLS aplicada ao Agent "eng-sales-agent-001"
CREATE SECURITY POLICY SalesRLS
    ADD FILTER PREDICATE dbo.fn_securitypredicate(SalesRegion)
    ON dbo.fct_Orders
    AFTER INSERT, AFTER UPDATE;

-- Função que define o filtro
CREATE FUNCTION dbo.fn_securitypredicate(@SalesRegion AS nvarchar(max))
    RETURNS TABLE
    WITH SCHEMABINDING
AS
RETURN SELECT 1 AS fn_securitypredicate_result
WHERE @SalesRegion IN (
    SELECT value FROM STRING_SPLIT(
        SESSION_CONTEXT(N'SalesRegion'), ','
    )
);

-- Agent conecta com contexto
EXECUTE sp_set_session_context @key=N'SalesRegion', @value=N'LATAM,EMEA';
SELECT * FROM fct_Orders;  -- Retorna apenas LATAM + EMEA
```

**Fluxo de RLS para Agente:**

```mermaid
sequenceDiagram
    actor Agent as "🤖 Agent<br/>eng-sales-001"
    participant Entra as "🪪 Entra ID"
    participant Purview as "🏷️ Purview"
    participant SQL as "📊 SQL Analytics<br/>Endpoint"
    participant Table as "📋 fct_Orders<br/>Table"
    
    Agent->>Entra: Solicita token JWT<br/>ClientID + Secret
    Entra-->>Agent: Retorna JWT com roles
    Agent->>SQL: SELECT FROM fct_Orders<br/>(JWT no header)
    SQL->>Entra: Valida token JWT
    SQL->>Purview: Consulta label de fct_Orders<br/>(Confidential)
    SQL->>SQL: Recupera SalesRegion do Agent<br/>via SESSION_CONTEXT
    SQL->>Table: Aplica RLS filter<br/>WHERE SalesRegion IN (LATAM,EMEA)
    Table-->>SQL: Retorna 1.245 linhas<br/>(antes eram 5.000)
    SQL-->>Agent: Resultado com RLS<br/>Somente LATAM+EMEA
    Agent->>Purview: Log de acesso registrado
    Purview-->>Purview: Audit trail: Agent->Table->Confidential->Success
```

---

##### 🔐 **Conditional Access - Políticas Adaptativas**

Quando um Agent tenta acessar dados **Confidential** ou **Highly Confidential**, Entra ID avalia políticas de Conditional Access:

**Exemplos de Políticas:**

| Cenário | Condição | Ação |
|---------|----------|------|
| Agent em IP corporativo + horário comercial | `TrustedLocation AND 09:00-18:00` | ✅ Permitir |
| Agent em horário fora do comercial | `After 18:00 OR Weekend` | ⚠️ Requer MFA + PIM approval |
| Agent acessando Highly Confidential | Por política corporativa | ❌ Bloquear + Notificar admin |
| Agent com comportamento anômalo | Risco elevado detectado | ⚠️ Step-up (MFA, manual approval) |

**Política de Exemplo (em Entra):**

```
Name: High Sensitivity Data Access
Applies to: All agents
Conditions:
  - Cloud apps: Azure Data Warehouse, SQL Database
  - Users: Service principals (agents)
  - Sensitivity: >= Confidential

Grant Controls:
  - Require multi-factor authentication
  - Require device to be marked as compliant
  - Require app protection policies
  
Session Controls:
  - Use app enforced restrictions
  - Sign-in frequency: 1 hour
```

**Integração com PIM (Privileged Identity Management):**

Para acessar dados Highly Confidential, o Agent precisa de aprovação:

```
Request Flow:
1. Agent tenta SELECT * FROM dim_Customer (Highly Confidential)
2. Entra detecta risco elevado
3. PIM requer aprovação de Security Admin
4. Admin recebe notificação:
   "Agent 'eng-sales-001' requests access to 'Highly Confidential' data.
    Reason: [Agent enviou]. Approve? [Yes/No]"
5. Se aprovado: Acesso concedido por 15 minutos
6. Se rejeitado: Acesso bloqueado + Alert

Timeout: Token expira após 15 minutos ou quando PIM approval expira
```

---

##### 📋 **Audit & Compliance - Rastreamento Completo**

Purview e Entra registram tudo:

**O que é auditado:**

| Evento | Quem | Quando | O quê | Resultado |
|--------|------|--------|-------|----------|
| Agent authentication | Entra ID | 2024-01-15 10:32:45Z | Agent `eng-sales-001` autenticou | ✅ Success |
| Query execution | Fabric RLS | 2024-01-15 10:33:12Z | SELECT fct_Orders (Confidential) | ✅ 1.245 rows |
| Label check | Purview | 2024-01-15 10:33:12Z | Sensibility: Confidential, RLS: Applied | ✅ Pass |
| Conditional Access | Entra | 2024-01-15 10:33:12Z | IP: 192.168.1.100, Location: Trust, Risk: Low | ✅ Allow |
| Data export | Purview DLP | 2024-01-15 10:35:00Z | Agent exportou 1.245 rows para CSV | ❌ Bloqueado (DLP) |
| Failed access | Fabric + Purview | 2024-01-15 10:45:00Z | Agent tentou Highly Confidential (PIM pending) | ❌ Denied |

**Exemplo de Audit Log:**

```json
{
  "timestamp": "2024-01-15T10:33:12.456Z",
  "auditEventType": "DataAccessAudit",
  "actor": {
    "type": "ServicePrincipal",
    "id": "87654321-4321-4321-4321-210987654321",
    "displayName": "eng-sales-agent-001"
  },
  "resource": {
    "type": "Table",
    "id": "fct_Orders",
    "workspace": "Sales Analytics",
    "sensitivity": "Confidential"
  },
  "action": {
    "type": "Query",
    "query": "SELECT OrderID, Amount, CustomerID FROM fct_Orders",
    "result": "Success"
  },
  "security": {
    "authentication": "EntraID_JWT",
    "authenticationResult": "Success",
    "rls_applied": true,
    "rls_filter": "SalesRegion IN ('LATAM','EMEA')",
    "rows_returned": 1245,
    "conditional_access": "Allow",
    "risk_level": "Low"
  },
  "compliance": {
    "regulatory_framework": ["LGPD", "SOC2", "ISO27001"],
    "data_residency": "BR-South",
    "encryption": "AES-256"
  }
}
```

**Retenção de Logs:**

- Entra ID Sign-in logs: 30 dias (default) → 90 dias com Azure Log Analytics
- Fabric Audit logs: 90 dias (default) → Retenção ilimitada com Long Term Retention
- Purview DLP logs: 1 ano (default) → Configurável até 10 anos

---

##### 🔄 **Fluxo Completo de Acesso (4 Camadas de Validação)**

```mermaid
flowchart TD
    A["🤖 Agent Request<br/>eng-sales-001<br/>SELECT FROM dim_Customer"]
    
    B["🪪 CAMADA 1: ENTRA ID<br/>Agent Authentication"]
    B1["Valida JWT token<br/>Verifica assinatura<br/>Verifica expiração"]
    B2{Token válido?}
    
    C["🔒 CAMADA 2: CONDITIONAL ACCESS<br/>Adaptive Security"]
    C1["Avalia contexto:<br/>IP, Hora, Risco,<br/>Device, Location"]
    C2{Acesso permitido?}
    
    D["🏷️ CAMADA 3: PURVIEW LABELS<br/>Data Classification"]
    D1["Consulta label da tabela<br/>dim_Customer →<br/>Highly Confidential"]
    D2{Qual label?}
    
    E["🔐 CAMADA 4: RLS + PIM<br/>Row-Level Security<br/>Privilege Management"]
    E1["Public/Internal →<br/>RLS aplicada<br/>Acesso direto"]
    E2["Confidential →<br/>RLS + Conditional Access<br/>Acesso verificado"]
    E3["Highly Confidential →<br/>RLS + PIM approval<br/>Requer humano"]
    E4{Aprovado?}
    
    F["✅ SQL Query<br/>Executa com RLS<br/>Retorna dados filtrados"]
    
    G["📋 Audit Logging<br/>Purview + Entra<br/>Registra tudo"]
    
    H["📤 Resultado<br/>Retorna ao Agent<br/>Com metadata"]
    
    I["❌ Acesso Negado<br/>Agent para<br/>Alert enviado"]
    
    A --> B
    B --> B1
    B1 --> B2
    B2 -->|Não| I
    B2 -->|Sim| C
    
    C --> C1
    C1 --> C2
    C2 -->|Não| I
    C2 -->|Sim| D
    
    D --> D1
    D1 --> D2
    
    D2 -->|Public/Internal| E1
    D2 -->|Confidential| E2
    D2 -->|Highly Confidential| E3
    
    E1 --> F
    E2 --> C2
    E3 --> E4
    E4 -->|Sim| F
    E4 -->|Não| I
    
    F --> G
    G --> H
    I --> G
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style D fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style E fill:#50C878,stroke:#2D7A4A,color:#fff,stroke-width:2px
    style F fill:#66BB6A,stroke:#4CAF50,color:#fff,stroke-width:2px
    style G fill:#9B59B6,stroke:#6A3980,color:#fff,stroke-width:2px
    style H fill:#3498DB,stroke:#2471A3,color:#fff,stroke-width:2px
    style I fill:#E74C3C,stroke:#A93226,color:#fff,stroke-width:2px
    style E1 fill:#52D273,stroke:#2D7A4A,color:#fff
    style E2 fill:#F39C12,stroke:#C87F0A,color:#fff
    style E3 fill:#E74C3C,stroke:#A93226,color:#fff
    style E4 fill:#E74C3C,stroke:#A93226,color:#fff
```

---

##### 🔗 **Referências Microsoft**

- [**Microsoft Entra Agent ID**](https://learn.microsoft.com/entra/agent-id/what-is-microsoft-entra-agent-id) - Framework de segurança para agentes de IA (Preview)
- [**Conditional Access for Agents**](https://learn.microsoft.com/entra/identity/conditional-access/agent-id) - Políticas adaptativas para identidades de agente
- [**Microsoft Entra Authentication in Fabric**](https://learn.microsoft.com/fabric/data-warehouse/entra-id-authentication) - Autenticação Zero Trust para SQL Analytics Endpoint
- [**Sensitivity Labels in Fabric**](https://learn.microsoft.com/fabric/governance/protected-sensitivity-labels) - Classificação de dados com proteção automática
- [**Row-Level Security in Fabric**](https://learn.microsoft.com/fabric/security/service-admin-row-level-security) - Filtragem de dados por contexto de usuário/agente
- [**Data Governance with Purview**](https://learn.microsoft.com/azure/cloud-adoption-framework/data/governance-security-baselines-purview-data-estate-unify-data-platform) - Classificação, governança e conformidade
- [**Audit Logging in Purview**](https://learn.microsoft.com/purview/compliance-portal) - Rastreamento e conformidade regulatória
- ⏹️ **Conditional Access:** Aprovações para dados sensíveis

### 📋 Resumo Técnico — De Dados Brutos a Insights de IA

| Componente | Função | Agentes Usam? |
|---|---|---|
| **OneLake** | Armazenamento lógico único, sem silos | Implicitamente (via SQL endpoint) |
| **Delta Lake** | Garantia ACID, confiabilidade, time-travel | Implicitamente (através de tabelas) |
| **Shortcuts** | Acesso a dados externos sem cópia | ✅ Sim (veem como tabelas locais) |
| **SQL Analytics Endpoint** | Interface T-SQL para consultas | ✅ Sim (principal forma de acesso) |
| **Medalha Medallion (Bronze→Silver→Gold)** | Organização e qualidade progressiva | ✅ Sim (acessam Gold layer) |
| **Data Products** | Pacotes curados para reutilização | ✅ Sim (principal consumidor) |
| **Purview Labels** | Classificação e governança de dados | ✅ Sim (define quem acessa o quê) |
| **Entra ID (Agent ID)** | Identidade e autenticação de agentes | ✅ Sim (autenticação + auditoria) |

**Referências Microsoft:**
- [Understand medallion lakehouse architecture for Microsoft Fabric with OneLake](https://learn.microsoft.com/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [What is a lakehouse in Microsoft Fabric?](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)
- [What is the SQL analytics endpoint for a lakehouse?](https://learn.microsoft.com/fabric/data-engineering/lakehouse-sql-analytics-endpoint)
- [Delta Lake table format interoperability](https://learn.microsoft.com/fabric/fundamentals/delta-lake-interoperability)

---

