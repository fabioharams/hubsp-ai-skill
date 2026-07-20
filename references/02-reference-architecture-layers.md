## 🏗️ 2. Reference Architecture (Overview)

> This is a capability map, not a mandatory product stack. Select only the context, runtime, framework, hosting and data components that a documented current requirement justifies. Start with an existing SaaS capability or deterministic automation and escalate through direct LLM, RAG, single agent and multi-agent only when the preceding option cannot reliably meet the requirement.

```mermaid
graph TD
    X["<b>Experiences</b><br/>─────────────────<br/>Copilot, Teams, Apps<br/>Business channels"]
    A["<b>Work IQ</b><br/>(Work Context)<br/>─────────────────<br/>Emails, chats, files<br/>meetings, workflows"]
    B["<b>Foundry IQ</b><br/>(Enterprise Knowledge)<br/>─────────────────<br/>Knowledge bases<br/>agentic retrieval"]
    C["<b>Fabric IQ</b><br/>(Data Intelligence)<br/>─────────────────<br/>Semantics, ontology<br/>unified metrics"]
    W["<b>Web IQ</b><br/>(Web Context Layer)<br/>─────────────────<br/>Near-real-time web grounding<br/>external evidence"]
    R["<b>Managed Agent Platform</b><br/>─────────────────<br/>Foundry Agent Service<br/>or Copilot Studio"]
    H["<b>Application Hosting</b><br/>─────────────────<br/>Required for Agent Framework<br/>unless deployed as a hosted agent"]
    D["<b>Microsoft Fabric</b><br/>(Data Platform)<br/>─────────────────<br/>OneLake, Data Products<br/>Lakehouse, Warehouse"]
    
    E["🛡️ Guard Rails<br/>Control"]
    F["✅ Evaluators<br/>Quality"]
    
    X --> R
    X --> H
    A --> R
    B --> R
    C --> R
    W --> R
    A --> H
    B --> H
    C --> H
    W --> H
    C --> D
    D --> C
    
    D -.-> E
    D -.-> F
    
    style A fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style B fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style C fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style W fill:#00A3A3,stroke:#006D6D,color:#fff,stroke-width:2px
    style R fill:#E85D04,stroke:#A33F00,color:#fff,stroke-width:2px
    style H fill:#E85D04,stroke:#A33F00,color:#fff,stroke-width:2px
    style D fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style E fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style F fill:#6BCB77,stroke:#54A05F,color:#fff,stroke-width:2px
```

### 🧠 Role of each layer

#### 💼 **Work IQ (Work Context)**
The contextual intelligence workload for Microsoft 365. It captures how work happens across emails, chats, meetings, documents, people and workflows, subject to the user's identity and permissions. Its role is to:
- Supply current work context to agents and copilots
- Connect collaboration signals across Microsoft 365
- Support knowledge and actions through Microsoft 365 tools
- Preserve user-context and permission boundaries

**Example:** An executive types "summarize this meeting" in Word — Copilot (Work IQ) fetches the transcript from OneDrive, summarizes it and inserts it into the document.

---

#### 📚 **Foundry IQ (Enterprise Knowledge)**
The managed, permission-aware enterprise knowledge workload. It is backed by Azure AI Search knowledge bases and agentic retrieval. Its role is to:
- Operate a permission-aware corporate knowledge base with structured and unstructured sources
- Execute agentic retrieval: decomposes questions into sub-queries, parallel search and re-ranks evidence with citations
- Enforce permissions and labels for supported sources and configurations; support varies by connector, API, region and feature status
- Connect Azure, SharePoint, OneLake and web in the same enterprise grounding plane

**Example:** An agent asks a shared knowledge base for the policies and authoritative documents relevant to a margin investigation. Foundry IQ plans retrieval, enforces supported source permissions and returns grounded evidence with citations.

---

#### 🤖 **Agent Platform, Framework and Hosting**
The execution layer is separate from the IQ context workloads. **Microsoft Foundry Agent Service** and **Microsoft Copilot Studio** provide managed agent platforms. **Microsoft Agent Framework** is a development framework, not a hosting service; its application requires an explicit hosting and scaling choice unless it is deployed as a Foundry hosted agent. The selected platform or hosted application can:
- Interpret intent and plan multi-step execution
- Invoke models, knowledge sources, tools, MCP servers and other agents
- Maintain conversation state and apply approval checkpoints
- Trace, evaluate, version and operate agents

**Example:** A Foundry agent receives "analyze why the margin dropped," retrieves policies through Foundry IQ, obtains governed metrics through Fabric IQ/Fabric, optionally adds external evidence through Web IQ, and composes a controlled response.

---

#### 🌐 **Web IQ (Web Context Layer)**
The **external grounding** layer of Microsoft IQ for up-to-date public web context. Access is currently limited and should be treated as a conditional dependency with an availability check and fallback. Its role is to:
- Bring web evidence (pages, news, images and videos) into agentic flows
- Operate with a focus on grounding quality, low latency and token efficiency
- Deliver denser passages/evidence to improve multi-step reasoning precision
- Respect publisher controls and web conventions (including robots and access preferences)
- Complement, without replacing, governed corporate data (Fabric IQ + Foundry IQ)

**Example:** When investigating a margin variation, the agent combines internal metrics (Fabric) with external market signals (Web IQ), maintaining a separate evidence trail for internal data and public sources.

---

#### 📊 **Fabric IQ (Data Intelligence)**
The **semantics and context** layer that enriches data with corporate meaning when shared analytical definitions are required. It can provide governed definitions for metrics, dimensions and relationships without replacing authoritative operational or domain systems. Its role is to:
- Create semantic models: define metrics (revenue, margin, COGS) once and only once
- Map ontology: relationships between entities (products, customers, regions, periods)
- Ensure consistency: all agents use the same definition of "margin", "customer", "Q3"
- Accelerate development: new agents reuse existing models instead of rebuilding
- Enable natural analysis: users ask in natural language, semantic models translate to SQL

**Example:** Fabric IQ defines that "Margin = (Revenue - COGS) / Revenue". When an agent is queried about margin, it does not need to know the formula — it consumes the already-calculated metric.

---

#### 🗄️ **Microsoft Fabric (Data Platform)**
An optional unified analytics platform for scenarios that require analytical consolidation, shared semantics or reusable data products. Other scenarios can retain governed Microsoft 365, operational, domain, API or search authorities. When selected, Fabric can:
- Store (OneLake): single logical repository per tenant, built on ADLS Gen2
- Transform (Spark, Python, SQL): ETL pipelines feeding Bronze → Silver → Gold
- Serve (SQL Analytics Endpoint): exposes data via T-SQL endpoint for agents to run queries
- Govern: integrates with Purview (classification), Entra ID (identity), Defender (security)
- Enable BI: Power BI accesses the same Fabric without data duplication

**Example:** Raw data (Bronze) → transformations (Silver) → Data Products ready for agents (Gold) → SQL Analytics Endpoint → Agents query in real time with row-level security.

---

#### 🛡️ **Guard Rails (Cross-cutting)**
The **control and security** layer that permeates all agent operations. Its role is to:
- Detect attacks: Prompt Shields blocks prompt injection
- Filter content: Content Safety checks risk categories (violence, NSFW, etc.)
- Enforce explicit application and runtime policies in addition to source authorization
- Sanitize responses: PII Detection removes sensitive information before returning
- Auditability: every action is recorded in Audit Logs for compliance

**Example:** Entra identity, resource authorization and source permissions deny an unauthorized request. A deterministic guard rail can additionally block a disallowed tool or action, and the audit path records the decision.

---

#### ✅ **Evaluators (Cross-cutting)**
The **continuous measurement** layer that validates whether agents are operating correctly. Its role is to:
- Assess quality: groundedness, task adherence, toxicity, security risks
- Detect drift: is the model starting to perform worse? Evaluators trigger alerts
- Generate feedback: evaluation results feed into retraining or prompt adjustments
- Support decisions: quality data justifies promoting to production or rolling back
- Integrate compliance: Purview logs of access to sensitive data become quality metrics

**Example:** Evaluators measure whether margin responses use the correct evidence and meet release thresholds. Runtime blocking occurs only when the architecture deliberately implements a deterministic policy or evaluated-response gate; evaluators do not replace source authorization.

---

### 📌 How They Work Together

```mermaid
flowchart TD
    A["👤 User<br/><b>Copilot / Teams / App</b><br/>Requests natural action"]
    B["🤖 Agent Runtime<br/>Interprets and plans"]
    K["📚 Microsoft IQ Context<br/>Work IQ | Foundry IQ<br/>Fabric IQ | Web IQ"]
    C{"🔐 Authorization + Guard Rails<br/>Validate identity, permissions<br/>policy and action risk"}
    D["📞 Tool Call<br/>Agent fetches data"]
    E["📊 Fabric IQ<br/>Semantics: translates<br/>question → query"]
    F["🗄️ Microsoft Fabric<br/>Serves data with<br/>Row-Level Security"]
    G["🧠 Reasoning<br/>Agent combines<br/>contexts"]
    H["✅ Evaluators<br/>Measure quality, security<br/>and release readiness"]
    I["📤 Response<br/><b>Work IQ</b><br/>Delivered to user"]
    
    A -->|"requests"| B
    B -->|"retrieves context"| K
    K -->|"permission-aware evidence"| B
    B -->|"plans"| C
    C -->|"✅ approve"| D
    C -->|"❌ block"| Z["🚫 Access Denied<br/>+ Audit Log"]
    D -->|"natural query"| E
    E -->|"optimized SQL"| F
    F -->|"data + metadata"| G
    G -->|"analysis + context"| H
    H --> I
    H --> W["🔄 Feedback Loop<br/>Improve Prompts"]
    W -->|"retrain"| B
    I -->|"ready insight"| A
    
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

**Insight:** The selected governed authority supplies data. Microsoft IQ capabilities add complementary work, knowledge, business or web context only when needed. A managed agent platform or hosted Agent Framework application plans and executes when an agent is justified. Authorization and guard rails constrain behavior; evaluators measure reliability and inform release decisions.

### 🧭 Adoption criteria: Copilot Studio, Foundry or mixed solution

| Option | When to prioritize | Main limitation |
|---|---|---|
| **Copilot Studio** | Business domain with well-defined conversational flow, low/medium technical effort and fast delivery in channels like Teams/web | Less control for advanced reasoning scenarios and complex engineering |
| **Microsoft Foundry** | Cases with deep technical integration, advanced tool calling, multi-step/multi-agent and need for pro-code control | Higher engineering and operational governance effort |
| **Mixed solution (Studio + Foundry)** | A measured requirement needs both a Copilot Studio experience boundary and Foundry capabilities that one platform cannot satisfy | Highest integration, identity, latency, cost and observability burden |

**Conditional target-architecture selection:**
1. Use an existing Microsoft/SaaS capability or deterministic workflow when it meets the outcome.
2. Add only the required context workload: Work IQ for Microsoft 365 work context, Foundry IQ for managed enterprise knowledge, Fabric IQ for shared business semantics, or Web IQ for approved external context.
3. When an agent is required, select one managed platform: Copilot Studio for low-code business experiences or Foundry Agent Service for managed pro-code agents.
4. Use Microsoft Agent Framework only with an explicit application-hosting choice or as a Foundry hosted agent.
5. Add Microsoft Fabric only for an analytical consolidation, semantic reuse or governed data-product requirement.
6. Combine platforms or agents only when evaluation proves that one bounded platform cannot meet independently justified requirements.

**Official Microsoft sources:**
- Microsoft Copilot Studio documentation: https://learn.microsoft.com/microsoft-copilot-studio/
- Microsoft Foundry documentation: https://learn.microsoft.com/azure/foundry/
- Foundry IQ documentation: https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq
- Fabric IQ documentation: https://learn.microsoft.com/fabric/iq/overview
- Microsoft 365 Copilot documentation: https://learn.microsoft.com/microsoft-365-copilot/
- Microsoft Fabric documentation: https://learn.microsoft.com/fabric/

### 📰 Recent Microsoft IQ updates (2025-2026)

- **Microsoft IQ** is now explicitly described as the corporate intelligence layer with **Work IQ, Foundry IQ, Fabric IQ and Web IQ**.
- **Work IQ** exposes work intelligence through chat, context, tools and workspaces; availability can differ by integration.
- **Foundry IQ** consolidates knowledge bases and agentic retrieval with citations and supported source permissions; capability status varies between GA and preview.
- **Fabric IQ** includes an IQ workload and items whose status varies; ontology, Plan and Graph capabilities require current preview and regional checks.
- **Web IQ** expands external grounding for agents but remains a limited-access dependency that requires an availability check and fallback.

---

## 🔧 2.1. Technical Specifications by Layer

### 🗄️ Microsoft Fabric — OneLake and Delta Lake

#### 📍 **OneLake: The Organization's Unified Lake**

**What it is:**
OneLake is a **single logical data lake per tenant**, automatically built on **Azure Data Lake Storage Gen2 (ADLS Gen2)**. It is the corporate equivalent of OneDrive for data — provisioned by default when you activate Fabric, with no additional configuration.

**Key characteristics:**
- 🎯 **Centralization:** All of the organization's analytics data in a single logical location
- 📦 **Multi-workspace:** Supports multiple workspaces (departments, domains) within the same OneLake
- 🔗 **Interoperability:** Accessible by all Fabric engines (Spark, SQL, Power BI) simultaneously
- 📊 **Duplication reduction:** Avoids data silos, reduces storage costs
- 🔐 **Unified governance:** Access, classification and compliance policies applied centrally via Purview

**Physical structure:**
When you create a **Lakehouse** in Fabric, two main folders are automatically provisioned in OneLake:
- `/Tables` — Stores managed tables in Delta format (ideal for structured data)
- `/Files` — Stores data in any format (CSV, Parquet, images, documents)

**Storage example:**

```mermaid
graph TD
    A["☁️ <b>OneLake</b><br/>(Single Tenant)<br/>─────────────────<br/>Logical Data Lake<br/>powered by ADLS Gen2"]
    
    B["🏢 Workspace-Finance<br/>─────────────────<br/>Department: Finance"]
    C["📊 Lakehouse-GL<br/>General Ledger"]
    D["📁 /Tables<br/>Delta Tables<br/>Managed"]
    E["📄 /Files<br/>PDFs, CSVs<br/>Imported"]
    
    F["🏢 Workspace-Sales<br/>─────────────────<br/>Department: Sales"]
    G["📦 Lakehouse-Orders<br/>Orders & Customers"]
    H["📁 /Tables<br/>fct_Orders<br/>dim_Customers"]
    I["📄 /Files<br/>Customer<br/>Uploads"]
    
    J["🏢 Workspace-Analytics<br/>─────────────────<br/>Shared"]
    K["🔗 Cross-Workspace Shortcuts<br/>Copy-free references<br/>for cross-analysis"]
    
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
    K -.->|"Virtual access to"| D
    K -.->|"Finance Data"| H
    K -.->|"Sales Data"| I
    
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

**Diagram reading:**
- 🔴 **OneLake (top):** Single tenant, automatically provisioned
- 🔵 **Workspaces:** Isolate data by department/domain
- 🟣 **Lakehouses:** Concrete (Finance-GL, Sales-Orders) in each workspace
- 🟢 **/Tables:** Stores managed Delta tables (structured)
- 🟡 **/Files:** Stores any format (raw)
- 🟠 **Shortcuts:** Create cross-workspace references without physical duplication

---

#### 🔄 **Delta Lake: The Standard Storage Format**

**What it is:**
**Delta Lake** is an open-source format maintained by the Linux Foundation that adds an ACID transactions layer, schema validation and history to Parquet files. Fabric standardizes on Delta Lake — every engine (Spark, SQL, Data Warehouse, Power BI) that writes data automatically creates Delta tables.

**Technical properties (Delta Lake vs pure Parquet):**

| Property | Parquet | Delta Lake |
|---|---|---|
| **ACID Transactions** | ❌ No | ✅ Yes (Atomicity, Consistency, Isolation, Durability) |
| **Schema Enforcement** | ❌ No | ✅ Yes (prevents "dirty" data) |
| **Time Travel** | ❌ No | ✅ Yes (query data from any point in time) |
| **Data Rollback** | ❌ No | ✅ Yes (revert bad writes) |
| **Unified Read** | ✅ Yes | ✅ Yes (all engines read the same copy) |
| **Query Performance** | Basic | **V-Order optimization** (much faster) |
| **Audit and Compliance** | ❌ No | ✅ Yes (Delta Lake table history) |

**Specific benefits for AI agents:**
- **Reliability:** Agents trust that data is correct (ACID prevents corruption)
- **Consistency:** Multiple agents reading simultaneously tend to see a consistent version
- **Traceability:** Complete history of when/who changed data (audit)
- **No duplication:** Spark transforms data → SQL reads → Power BI visualizes **from the same copy**

**Example:**
```
An agent writes "margin" data to Delta:
  ✅ Margin = (Revenue - COGS) / Revenue
  ✅ Schema enforcement: if someone tries to write "margins" (typo), it is blocked
  ✅ Another agent reads simultaneously, sees consistent data
  ✅ If an error is discovered, time-travel reverts to the previous version
```

---

#### 🔗 **Shortcuts: Virtualized Data Without Copying**

**What it is:**
Shortcuts are **virtual references** (like symbolic links) to external data. Agents query data as if it were in OneLake, but it is served from external sources without physical copying.

**Supported sources:**
- ✅ Azure Data Lake Storage Gen2 (ADLS Gen2)
- ✅ Amazon S3
- ✅ Google Cloud Storage
- ✅ Dataverse (Microsoft dynamics 365)
- ✅ Other lakehouses/workspaces (cross-workspace)

**Benefits:**
- 💰 **Zero copy:** Does not duplicate data, saves storage
- ⚡ **Fresh data:** Agents tend to see the most current version from the source
- 🔐 **Explicit security:** Access is the intersection of permissions on the shortcut path and target path; identity passthrough or delegated authentication depends on shortcut type and query engine
- 📍 **Governed access:** Configure OneLake roles, source permissions, connection identity, labels and downstream SQL/semantic-model controls for the selected path

**Example:**
```
HR data lives in an external ADLS Gen2 (managed by another team)
You create a Shortcut → it appears as a table in your Lakehouse
The agent runs: SELECT * FROM HR.Employees
  ↓ Direct fetch from ADLS Gen2, authenticated, with RLS applied
  ↓ No ETL, no duplication, centralized governance
```

---

#### 🔍 **SQL Analytics Endpoint: T-SQL Interface for Data**

**What it is:**
Each Lakehouse in Fabric **automatically provisions** a **SQL Analytics Endpoint** — a TDS (Tabular Data Stream) endpoint that exposes Delta tables as standard SQL tables, queryable with T-SQL.

**Characteristics:**
- 🚀 **Automatic:** Created together with the Lakehouse, zero setup
- 📖 **Read-only:** Does not support INSERT/UPDATE/DELETE (use Spark to modify data)
- ⚡ **High performance:** Powered by the same engine as the Fabric Data Warehouse
- 🔐 **Row & Column Security:** Applies granular SQL permissions (RLS, column masking)
- 📊 **Metadata Auto-Sync:** Delta tables automatically appear as SQL tables
- 🔗 **Cross-workspace:** Can query data via Shortcuts from other workspaces

**Capabilities:**
✅ `SELECT` against Delta tables (including via Shortcuts)  
✅ Create views, functions, stored procedures in T-SQL  
✅ Apply row-level security (RLS) and column security  
✅ Connect Power BI directly for reports  
✅ Run queries via Azure Data Studio, SQL Server Management Studio (SSMS), any TDS client  

**Agent usage example:**
```sql
-- Agent in Foundry runs:
SELECT 
    p.ProductName,
    SUM(s.Amount) as TotalSales,
    AVG(s.Amount) as AvgPrice
FROM Gold.Products p
INNER JOIN Gold.Sales s ON p.ProductID = s.ProductID
WHERE s.Date >= DATEADD(month, -3, GETDATE())
GROUP BY p.ProductName
ORDER BY TotalSales DESC

-- Result is returned via TDS to the agent
-- Row-level security has already filtered data according to the agent's permission (Entra ID)
```

**Performance considerations:**
- Metadata synchronization between a Lakehouse and its SQL analytics endpoint is asynchronous; measure propagation delay for the selected workload instead of assuming a fixed interval
- Uses **V-Order optimization:** Spark writes optimized Parquet for fast SQL reads
- Automatic indexes: Fabric maintains statistics and histograms without user action

---

#### 🏗️ **Medallion Architecture: Layered Organization**

##### 📖 **What is Medallion Architecture?**

The **Medallion Architecture** (also known as "Bronze-Silver-Gold" or "Delta Lake Medallion") is a **data organization pattern** recommended by Microsoft for structuring Lakehouses in a scalable, governable and reusable way. It is a model **proven at petabyte scale** (Microsoft IDEAS, for example, uses Medallion for 4 PiB of data).

**Core principles:**
- 🎯 **Quality progression:** Each layer increases data quality, validation and value
- 🔄 **Reuse:** Data transformed once, consumed by multiple consumers (agents, BI, apps)
- 🏗️ **Separation of concerns:** Bronze = ingestion, Silver = transformation, Gold = business
- 📊 **Scalability:** Supports growth from terabytes to petabytes without reorganization
- 🔐 **Stratified governance:** Each layer has its own policy (workspace isolation)

**Alternatives Medallion does not replace:**
- ✅ Medallion works well in a **Data Lake** (Bronze→Silver→Gold with Spark)
- ✅ Medallion works well in a **Data Warehouse** (dimensional modeling, slowly changing dimensions)
- ✅ Fabric allows **combination:** Bronze+Silver as lakehouses, Gold as data warehouse
- ✅ For highly decentralized cases: **Data Mesh** (multiple domains, each with its own Medallion)

---

##### 🌍 **General Flow: From Raw Data to Insights**

```mermaid
graph LR
    A["🚀 Data Source<br/>─────────────────<br/>ERP, CRM, APIs,<br/>Uploads, Sensors"]
    
    B["🟤 BRONZE<br/>RAW DATA<br/>─────────────────<br/>Original format<br/>No cleaning"]
    
    C["⚙️ Spark/Python<br/>Transformation<br/>Validation"]
    
    D["🟡 SILVER<br/>CLEAN DATA<br/>─────────────────<br/>Validated data<br/>Structured"]
    
    E["⚙️ Spark/SQL<br/>Aggregation<br/>Semantics"]
    
    F["🟢 GOLD<br/>BUSINESS DATA<br/>─────────────────<br/>Ready for<br/>consumption"]
    
    G["📊 Consumption<br/>─────────────────<br/>Agents, BI,<br/>Apps, Reports"]
    
    A -->|"Ingest (as-is)"| B
    B -->|"Transform"| C
    C -->|"Validate, clean"| D
    D -->|"Aggregate"| E
    E -->|"Semanticize"| F
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

##### 🟤 **Bronze Layer — RAW DATA**

**Purpose:**
- ✅ Capture data **as it arrives**, in original format
- ✅ Enable **audit** (traceability to origin)
- ✅ Enable **reprocessing** (if Silver/Gold logic changes)
- ✅ Maintain complete history (compliance, GDPR, etc.)

**Characteristics:**

| Aspect | Detail |
|---|---|
| **Formats** | CSV, JSON, Parquet, Delta, AVRO, images, PDFs — any |
| **Validation** | ❌ None — "trust but verify later" |
| **Duplication** | May have duplicate rows |
| **Schema** | Loose (can evolve without breaking) |
| **Retention** | Typical: 90 days to 2 years (compliance) |
| **Workspace** | Private (Bronze-Workspace) |
| **Owner** | Data Engineers (ingestion) |
| **Technology** | Data Factory, Mirroring, Synapse Spark, Dataflows |

**Bronze content example:**

```mermaid
graph TD
    A["🟤 BRONZE LAYER<br/>─────────────────<br/>Raw Data Storage<br/>Workspace: Bronze-Workspace"]
    
    B["📄 /invoices_raw/<br/>─────────────────<br/>Source: Email, FTP<br/>Format: CSV"]
    C["📁 2026-05-01/<br/>invoices_batch_001.csv<br/>invoices_batch_002.csv<br/>..."]
    
    D["📊 /customers_dump/<br/>─────────────────<br/>Source: DB Export<br/>Format: JSON"]
    E["📋 export_2026_05_01.json<br/>export_2026_04_01.json<br/>..."]
    
    F["📈 /erp_api_logs/<br/>─────────────────<br/>Source: Streaming API<br/>Format: JSON"]
    G["🔄 2026-05-01T*.json<br/>Structured logs<br/>timestamp-based"]
    
    H["📎 /uploads/<br/>─────────────────<br/>Source: User Uploads<br/>Format: Mixed"]
    I["📄 contracts/ → PDFs<br/>📷 receipts/ → Images<br/>🗂️ other/ → Miscellaneous"]
    
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

**Example characteristics:**

| Folder | Source | Format | Size | Frequency | Quality |
|---|---|---|---|---|---|
| `/invoices_raw/` | Email, FTP manual | CSV | 10-500 MB/day | Daily | ❌ May have errors, duplicates |
| `/customers_dump/` | DB Export (nightly) | JSON | 100 MB | Daily (1x) | ⚠️ May have special characters |
| `/erp_api_logs/` | Streaming API | JSON | 5-50 GB/day | Continuous | ⚠️ Timestamps may desync |
| `/uploads/` | User uploads | Mixed (PDF, IMG) | 1-10 GB/day | On-demand | ❌ May have viruses, corruption |

**Recommended flow for Bronze:**
1. **Mirroring** (ideal): Near real-time replication from DB → OneLake (supports SQL Server, MySQL, PostgreSQL, Snowflake)
2. **Data Factory:** Pipelines with 200+ native connectors
3. **Shortcuts:** Reference data from ADLS Gen2/S3 without copying
4. **Dataflow Gen2:** Visual interface, lightweight transformations

---

##### 🟡 **Silver Layer — CLEAN DATA (Validated and Structured Data)**

**Purpose:**
- ✅ **Validate** integrity: duplicates, nulls, data types
- ✅ **Clean** data: standardize formats, remove invalid values
- ✅ **Structure** for analysis: denormalizations, lightweight aggregations
- ✅ **Integrate** multiple sources: invoices + customers + products into coherent tables
- ✅ Serve as a governed, reusable analytical authority for analysts and agents within the defined domain and scope

**Characteristics:**

| Aspect | Detail |
|---|---|
| **Formats** | ✅ **Standard: Delta Lake** (ACID, schema enforcement) |
| **Validation** | ✅ Yes — referential integrity, types, ranges |
| **Duplication** | ❌ Removed (distinct keys guaranteed) |
| **Schema** | Strict (schema enforcement — rejects invalid data) |
| **Retention** | Policy-defined from legal, recovery, cost and operational requirements |
| **Workspace** | Semi-private (Silver-Workspace, controlled access) |
| **Owner** | Data Engineers (ELT transformation) |
| **Technology** | Spark (Python, SQL, Scala), Synapse notebooks |

**Typical Bronze → Silver transformations:**

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

**Flow by category:**

| Source | Spark Processing | Validations | Silver Output |
|---|---|---|---|
| **Invoices** (multiple CSVs) | Spark DataFrame merge | ✅ Dedup by ID<br/>✅ Amount > 0<br/>✅ Date standard<br/>✅ Remove nulls | **fct_Invoices** (Delta) |
| **Customers** (JSON exports) | Spark DataFrame merge | ✅ Latest version (SCD1)<br/>✅ Email format<br/>✅ Join address data<br/>✅ Active only | **dim_Customers** (Delta) |
| **Products** (API export) | Spark DataFrame merge | ✅ Merge by ProductID<br/>✅ Cost > 0<br/>✅ Currency aligned<br/>✅ Active flag | **dim_Products** (Delta) |

**Silver quality guarantees:**
- 🔐 **ACID transactions** — no partial or corrupted data
- 🔑 **Primary key unique** — no duplicates by ID
- 📊 **Schema strict** — rejects data outside expected type
- ✅ **Data completeness** — no NULL in critical columns
- 🔄 **Referential integrity** — FK relationships validated

**Typical Silver structure:**

```mermaid
graph TD
    A["🟡 SILVER LAYER<br/>─────────────────<br/>Validated Data"]
    
    B["📊 FACTS<br/>(Measures)"]
    C["fct_Invoices<br/>fct_Orders<br/>fct_Sales"]
    
    D["🔑 DIMENSIONS<br/>(Context)"]
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

##### 🟢 **Gold Layer — BUSINESS DATA (Business-Ready Data)**

**Purpose:**
- ✅ **Aggregate** data into business dimensions (product, region, period)
- ✅ **Calculate** metrics (revenue, margin, COGS, KPIs)
- ✅ **Semanticize** data with comprehensible corporate names and logic
- ✅ Expose as **Data Products** consumable by agents, BI, apps
- ✅ Guarantee **performance** (pre-aggregated data, indexes, statistics)

**Characteristics:**

| Aspect | Detail |
|---|---|
| **Formats** | ✅ **Standard: Delta Lake** (with V-Order optimization) |
| **Aggregation** | ✅ Yes — facts aggregated by business dimensions |
| **Calculations** | ✅ Pre-calculated corporate metrics |
| **Schema** | Semantic — business names (not technical) |
| **Retention** | Policy-defined; retain only the history required by the scenario |
| **Workspace** | Controlled consumer access with least privilege |
| **Owner** | Analytics Engineers / Business Analysts |
| **Exposure** | SQL Analytics Endpoint, Power BI, APIs for agents |
| **Technology** | Spark (aggregations), SQL (views, stored procs), Power BI (semantic models) |

**Typical Gold structure (Data Products):**

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
    
    M["📊 Consumption<br/>─────────────────<br/>Agents, BI, Apps"]
    
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

**Gold table examples:**

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

**Gold Data Products summary:**

| Product | Table | Purpose | Updated | Access |
|---|---|---|---|---|
| **Revenue** | `fct_DailyRevenue` | Revenue by product-region-day | 2 AM UTC | 🔵 Internal |
| **Profitability** | `fct_Margins` | Gross, operating, net margins | 3 AM UTC | 🟡 Confidential (RLS) |
| **Customer 360** | `dim_Customer` | Customer + lifetime value + churn risk | 4 AM UTC | 🔴 Confidential (PII + RLS) |

**Required service commitments per Data Product:**
- ✅ **Documentation:** Data dictionary, formulas, lineage
- ✅ **Freshness objective:** Defined update target with measured evidence and an accountable owner
- ✅ **Security:** Sensitivity labels plus explicitly configured identity, item, OneLake, SQL, RLS/CLS and sharing controls as applicable
- ✅ **Discovery:** Indexed in Data Catalog (Purview)
- ✅ **Audit:** Access recorded in Audit Logs

---

##### 🏢 **Workspace Isolation (Microsoft Recommendation)**

Microsoft recommends **creating each layer in a separate workspace** for better governance:

```mermaid
graph LR
    A["🏢 Workspace-Bronze<br/>─────────────────<br/>Access: Private<br/>Owner: Data Engineers"]
    B["🏢 Workspace-Silver<br/>─────────────────<br/>Access: Semi-private<br/>Owner: Data Engineers"]
    C["🏢 Workspace-Gold<br/>─────────────────<br/>Access: Public<br/>Owner: Analytics Eng."]
    D["👥 Agents/BI/Apps<br/>─────────────────<br/>Consume Gold<br/>via SQL Endpoint"]
    
    A -->|"Data moves via<br/>Spark jobs"| B
    B -->|"Data moves via<br/>Spark jobs"| C
    C -->|"Read-only via<br/>SQL Endpoint"| D
    
    style A fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style B fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style C fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style D fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
```

**Benefits:**
- 🔐 **Isolation:** Bronze (raw) not exposed to end users
- 👥 **Granular RBAC:** Different permissions per layer
- 📊 **Separate billing:** Track costs of each pipeline phase
- 🚀 **Performance:** Dedicated capacity for each workload
- 🔄 **Evolution:** Change Silver/Gold without affecting Bronze ingestion

---

##### 📚 **Implementation Patterns in Fabric**

There are **3 main patterns** recommended by Microsoft for implementing Medallion in Fabric. The choice depends on **team maturity, data complexity and BI requirements**.

---

###### **OPTION 1️⃣ — Three Lakehouses (one per layer)**

**When to use:**
- ✅ **Pure Data Engineering** teams (no traditional BI)
- ✅ **Broadly open** architecture (Delta Lake, no dimensional schema)
- ✅ Focus on **exploratory analyses and AI agents**
- ✅ Teams that master **Spark/Python** more than SQL

**Architecture:**

```mermaid
graph TD
    A["🏢 Workspace-Bronze<br/>─────────────────<br/>Access: Private"]
    B["📦 Lakehouse-Raw<br/>Bronze Layer"]
    C["📁 /Tables<br/>Delta raw"]
    D["📄 /Files<br/>Any format"]
    
    E["🏢 Workspace-Silver<br/>─────────────────<br/>Access: Semi-private"]
    F["📦 Lakehouse-Curated<br/>Silver Layer"]
    G["📁 /Tables<br/>Delta validated"]
    
    H["🏢 Workspace-Gold<br/>─────────────────<br/>Access: Public"]
    I["📦 Lakehouse-Products<br/>Gold Layer"]
    J["📁 /Tables<br/>Delta aggregated"]
    K["📊 SQL Analytics<br/>Endpoint"]
    
    L["👥 Consumers<br/>─────────────────<br/>Agents, BI, Apps"]
    
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

**Characteristics:**

| Aspect | Detail |
|---|---|
| **Lakehouses** | 3 separate (Bronze, Silver, Gold) |
| **Formats** | Bronze: multiple, Silver: Delta, Gold: Delta |
| **Compute** | Spark (transformation), SQL (queries) |
| **BI Support** | Limited — SQL Analytics Endpoint only |
| **Scalability** | ⭐⭐⭐⭐⭐ Excellent for data lakes |
| **Governance** | ⭐⭐⭐⭐ Workspace isolation |
| **Complexity** | Medium (3 lakehouses to maintain) |
| **Cost** | Workspace count does not determine capacity count; assign workspaces to capacity based on measured isolation, performance and governance needs |

**Real use cases:**
- Big Data agencies serving multiple clients
- Organizations with Data Science culture (Python/R dominant)
- Large-scale processing where representative workload tests validate the selected Fabric capacity
- Exploratory analyses and machine learning

---

###### **OPTION 2️⃣ — Bronze+Silver Lakehouse, Gold Data Warehouse** ⭐ **RECOMMENDED**

**When to use:**
- ✅ Teams with **traditional BI experience** (star schema, dimensional modeling)
- ✅ Need for **Power BI + SQL Reports** as consumers
- ✅ **Structured and repeatable** analyses (not exploratory)
- ✅ Teams that master **SQL/DAX** more than Spark/Python

**Architecture:**

```mermaid
graph TD
    A["🏢 Workspace-Silver<br/>─────────────────<br/>Access: Semi-private"]
    B["📦 Lakehouse-Staging<br/>Bronze+Silver"]
    C["📁 /Files<br/>Bronze raw<br/>Any format"]
    D["📁 /Tables<br/>Silver validated<br/>Delta tables"]
    
    E["⚡ ELT Pipeline<br/>─────────────────<br/>Spark/Python<br/>Dataflows"]
    
    F["🏢 Workspace-Gold<br/>─────────────────<br/>Access: Public"]
    G["🏗️ Data Warehouse<br/>Gold Layer<br/>Dimensional Schema"]
    
    H["📊 Fact Tables"]
    I["fct_Sales<br/>fct_Orders<br/>fct_Inventory"]
    
    J["🔑 Dimension Tables"]
    K["dim_Product<br/>dim_Customer<br/>dim_Calendar"]
    
    L["📈 Power BI<br/>─────────────────<br/>Direct Lake Mode"]
    
    M["📋 SQL Reports<br/>─────────────────<br/>Warehouse endpoint"]
    
    N["🤖 AI Agents<br/>─────────────────<br/>SQL queries"]
    
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

**Characteristics:**

| Aspect | Detail |
|---|---|
| **Lakehouses** | 1 (Bronze+Silver combined) |
| **Warehouses** | 1 (Gold in dimensional DW) |
| **Formats** | Bronze: multiple, Silver: Delta, Gold: DW schema |
| **Compute** | Spark (ETL), SQL (DW queries) |
| **BI Support** | ⭐⭐⭐⭐⭐ Native Power BI + SQL Reports |
| **Scalability** | ⭐⭐⭐⭐ Good for enterprise BI |
| **Governance** | ⭐⭐⭐⭐ Bronze/Silver vs Gold isolation |
| **Complexity** | Medium (1 Lakehouse + 1 DW) |
| **Cost** | Lakehouse and warehouse can share or use separate capacities; validate CUs, concurrency, isolation and cost with the Capacity Metrics app |

**Real use cases:**
- Organizations with mature BI (Power BI at scale)
- Companies transitioning from a traditional data warehouse
- Structured analyses with dimensional models
- Repeatable operational reports

**Unique benefit:** Uses Power BI **Direct Lake mode** — loads data directly from Delta tables in the DW, reducing the need for expensive Import dataset refreshes.

---

###### **OPTION 3️⃣ — Medallion + Data Mesh** (For large organizations)

**When to use:**
- ✅ **Large federated organizations** with independently owned data domains
- ✅ **Multiple autonomous domains** (Finance, Sales, Operations, HR, etc.)
- ✅ Need for **data federation** (each domain owns its data)
- ✅ Each domain operates its own **complete Medallion**

**Architecture:**

```mermaid
graph TB
    A["📊 DATA MESH TOPOLOGY<br/>─────────────────<br/>Federated Domains<br/>Each domain = complete Medallion"]
    
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
    
    E["🏢 Domain-Analytics<br/>─────────────────<br/>Shared Workspace"]
    E1["🔗 Shortcuts<br/>Cross-Domain"]
    E2["📊 Data Catalog<br/>(Purview)"]
    E3["🔐 Governance<br/>Hub"]
    
    F["👥 Consumers<br/>─────────────────<br/>Agents, BI, Apps"]
    
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

**Characteristics:**

| Aspect | Detail |
|---|---|
| **Domains** | 3+ (each one = complete Medallion) |
| **Ownership** | Each domain = autonomous team |
| **Integration** | Shortcuts + OneLake cross-workspace |
| **Governance** | Centralized hub (Purview) |
| **Scalability** | High potential, subject to selected capacity, data layout, concurrency and representative load validation |
| **Autonomy** | ⭐⭐⭐⭐⭐ Maximum independence |
| **Complexity** | High (requires discipline) |
| **Cost** | 💰💰💰 Multiple capacities |

**Data Mesh principles:**
1. **Domain ownership:** Each domain = owner of its data
2. **Data as product:** Gold layers are "Data Products" with SLA
3. **Self-serve infrastructure:** Each domain provisions its own Medallion
4. **Federated governance:** Central policies (Purview), local implementation

**Real use cases:**
- Large conglomerates (multiple subsidiaries, geographies)
- Fintech organizations (each service = independent domain)
- Organizations with multiple autonomous data-product teams and federated governance
- Media industry (multiple studios/platforms)

---

##### 📋 **Decision Matrix: Which Pattern to Choose?**

```mermaid
graph TD
    A["What is your case?"]
    
    B{"Is the team<br/>Spark-first or<br/>SQL-first?"}
    C{"Organization<br/>size?"}
    
    D{"Spark/Python<br/>dominant"}
    E{"SQL/BI<br/>dominant"}
    F{"Small<br/>10-50 eng"}
    G{"Large<br/>100+ eng"}
    
    B -->|"Spark"| D
    B -->|"SQL"| E
    
    C -->|"Small"| F
    C -->|"Large"| G
    
    D -->|"+ exploratory<br/>analyses"| H["✅ OPTION 1<br/>Three Lakehouses"]
    E -->|"+ Power BI<br/>reports"| I["✅ OPTION 2<br/>Lakehouse +<br/>Warehouse<br/><br/><br/>⭐ RECOMMENDED"]
    
    F -->|"No BI"| J["✅ OPTION 1<br/>Three Lakehouses"]
    G -->|"Multiple<br/>domains"| K["✅ OPTION 3<br/>Data Mesh"]
    
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

**Microsoft References:**

> **Source status:** Microsoft architecture, Fabric, Microsoft IQ, Agent Framework, Agent ID and security sources in this reference were rechecked on **2026-07-20**. Preview status, regional availability, licensing, authentication behavior and limits must be revalidated for each production design.
- [Understand medallion lakehouse architecture for Microsoft Fabric with OneLake](https://learn.microsoft.com/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [Lakehouse end-to-end scenario: overview and architecture](https://learn.microsoft.com/fabric/data-engineering/tutorial-lakehouse-introduction)
- [Data Platform end-to-end with Microsoft Fabric](https://learn.microsoft.com/azure/architecture/example-scenario/dataplate2e/data-platform-end-to-end)

---

#### 📊 **Data Products: Data Packages for Reuse**

**What it is:**
A **Data Product** is a curated set of Gold tables with clear semantics, documentation, and a quality SLA — ready to be reused by multiple agents and users.

**Characteristics:**
- 📖 **Documented:** Data dictionary, lineage, clear business rules
- 🎯 **Semantically clear:** "Revenue = Sales Price × Quantity", unambiguous
- 🔐 **Secure:** Sensitivity labels classify data; explicitly configured OneLake, item, SQL, RLS/CLS and sharing controls enforce access
- ⚙️ **Operationalized:** Refresh pipelines help keep data fresh, with an update SLA
- 📈 **Versioned:** Schema changes are controlled, compatibility maintained
- 📣 **Discoverable:** The catalog (Data Catalog in Purview) indexes and describes it

**Data Product example:**

```mermaid
graph TD
    A["🎁 Data Product: Sales Analytics<br/>─────────────────<br/>Owner: Sales Analytics Team<br/>Sensitivity: Internal"]
    
    B["📊 GOLD TABLES<br/>─────────────────"]
    
    C["📈 fct_Orders<br/>(Fact Table)"]
    C1["Columns:<br/>OrderID, CustomerID,<br/>ProductID, OrderAmount,<br/>OrderDate"]
    C2["Metrics:<br/>TotalRevenue<br/>AverageOrderValue<br/>UnitsSold"]
    
    D["👥 dim_Customers<br/>(Dimension)"]
    D1["Columns:<br/>CustomerID, Name<br/>Segment, Region"]
    D2["🔒 RLS:<br/>By region<br/>Agents only see<br/>their region"]
    
    E["📖 DOCUMENTATION<br/>─────────────────"]
    E1["📝 Business Rules:<br/>Revenue = SUM(OrderAmount)<br/>in local currency<br/><br/>Segment = Behavioral<br/>classification updated monthly"]
    
    F["⏰ OPERATIONALIZATION<br/>─────────────────"]
    F1["📌 Freshness SLA:<br/>Updated nightly 2 AM UTC<br/>&lt; 1 hour after source refresh<br/><br/>🔄 Versioning:<br/>Schema changes controlled<br/>Compatibility maintained"]
    
    G["🔍 DISCOVERY<br/>─────────────────"]
    G1["📚 Data Catalog<br/>(Purview)<br/>Indexed and discoverable<br/>Lineage visible"]
    
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

**Data Product components:**

| Component | What it is | Responsibility |
|---|---|---|
| **Fact Tables** | `fct_Orders` — measures (OrderAmount, UnitsSold) | Analytical core |
| **Dimensions** | `dim_Customers` — context (Name, Segment) | Business context |
| **Metrics** | TotalRevenue, AverageOrderValue | Pre-calculated KPIs |
| **RLS** | Row-level security by region | Security + compliance |
| **Documentation** | Business rules, formulas, glossary | Clear semantics |
| **SLA** | Updated 2 AM UTC, < 1h lag | Reliability |
| **Versioning** | Schema changes with compatibility | Controlled evolution |
| **Catalog** | Purview indexes and describes | Discovery |

**Usage by an Agent:**
```python
# Agent in Foundry
from azure.ai.projects import AIProjectClient
import pyodbc

# Connect via SQL Analytics Endpoint (authenticated with Agent ID via Entra)
conn = pyodbc.connect(
    'Driver=ODBC Driver 17 for SQL Server;'
    'Server=fabric.database.windows.net;'
    'Database=Sales_Analytics;'
    'Authentication=ActiveDirectoryMSI'
)

# Query the Gold Data Product (RLS must be configured and validated)
cursor = conn.cursor()
cursor.execute('''
    SELECT OrderAmount, CustomerSegment, OrderDate
    FROM fct_Orders
    WHERE OrderDate >= DATEADD(month, -3, GETDATE())
''')

# Agent reasons over the data
data = cursor.fetchall()
# ... Claude processes context, generates analysis
```

---

#### 🔐 **Governance Integration (Purview + Entra)**

The integration between **Microsoft Entra Agent ID**, **Microsoft Purview** and **Microsoft Fabric** creates a multi-level security architecture where each agent is authenticated as a distinct corporate identity (not just a generic application), and every data access is governed by sensitivity classification and access control rules.

##### 🪪 **Entra ID Agent Identity - Identities for AI**

Microsoft Entra Agent ID is an identity and security framework for AI agents. Agent identities are specialized Entra identity constructs; the effective controls depend on the identity type, token flow, licensing and configured security capabilities.

| Aspect | Service Principal (Legacy) | Entra Agent ID (New) |
|---------|-------------------------|---------------------|
| **Purpose** | General workload/application identity | Agent identity created from an agent identity blueprint |
| **Authentication** | Supported workload credential or federation | OAuth 2.0 token flow through the supported blueprint/agent identity pattern |
| **Authorization** | Resource permissions and application roles | The same resource authorization remains required; agent-specific security can add risk and lifecycle controls |
| **Audit** | Entra sign-in and audit signals | Agent sign-in and audit signals for supported identity flows |
| **Governance** | Workload lifecycle controls | Blueprint and agent lifecycle controls when configured and licensed |
| **Conditional Access** | Workload identity controls vary | Agent Conditional Access requires supported identity flows, configuration and licensing |

**How Agent ID works:**

1. **Creation:** Each agent receives a unique identity in Entra ID (e.g., `eng-sales-agent-001`)
2. **Authentication:** The application obtains an OAuth token through the supported agent identity flow; prefer managed credentials or workload identity federation over long-lived secrets
3. **The JWT contains:**
   - `app_displayname`: "Eng Sales Agent"
   - `appid`: unique GUID of the agent
   - `roles`: ["Data Explorer", "Contributor"] 
   - `oid`: object ID of the agent
4. **Zero Trust:** The target resource validates the token and enforces its own permissions; configured Entra security capabilities can add risk-based controls
5. **Renewal:** Token lifetime follows the effective Entra policy and token flow; do not assume a universal one-hour lifetime

**JWT Payload example:**
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

##### 🏷️ **Purview Sensitivity Labels - Hierarchy and Classification**

Sensitivity labels in Purview provide multi-level classification with progressive protection:

| Label | Description | Use Scenario | Protection | Access by Agent |
|-------|-----------|---|----------|---|
| **Public** | No restriction, can be shared externally | Public marketing data, public prices | No encryption | ✅ Automatic |
| **Internal** | Internal use only, not sensitive | Operational documents, announcements | Watermark | ✅ Automatic |
| **Confidential** | Sensitive business data, restricted to authorized employees | Contracts, sales plans, internal analyses | Encryption + Access Restriction | ⚠️ Requires Conditional Access |
| **Highly Confidential** | Extremely sensitive data, maximum protection | Financial data, PII, trade secrets | Strong encryption + Strict restriction | ❌ Blocked (human-in-loop required) |

**Label Hierarchy in Purview:**

```mermaid
graph TD
    A["Microsoft Purview<br/>Sensitivity Labels"]
    B["Public"]
    C["Internal"]
    D["Confidential"]
    E["Highly Confidential"]
    
    B1["No protection<br/>No restriction"]
    C1["Internal watermark<br/>Visible in metadata"]
    D1["Encryption<br/>Restricted access<br/>Requires Co-Author"]
    E1["Maximum protection<br/>Requires approval<br/>Internal use only"]
    
    D2["Confidential \ All Employees<br/>Everyone can view"]
    D3["Confidential \ Specific People<br/>Only specified"]
    
    E2["Highly Confidential \ Restricted<br/>Maximum restriction"]
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

**Applying Labels in Fabric:**

When data is ingested into OneLake, Purview can apply labels automatically:

```mermaid
graph TD
    A["☁️ OneLake<br/>─────────────<br/>Single Tenant"]
    
    B["🏢 Sales_Analytics<br/>Workspace"]
    C["📊 Warehouse"]
    
    D["📋 fct_Orders<br/>🟡 Confidential<br/>Sales data"]
    E["👥 dim_Customer<br/>🔴 Highly Confidential<br/>PII: CPF, email, phone"]
    F["📦 dim_Product<br/>🟢 Public<br/>Public catalog"]
    G["💰 fct_Revenue<br/>🟡 Confidential<br/>Financial data"]
    
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

##### 🔒 **Row-Level Security (RLS) - Filtering by Agent Context**

The SQL Analytics Endpoint in Fabric supports RLS via `EXECUTE AS` with Agent ID:

```sql
-- Base table: fct_Orders
SELECT 
    OrderID, 
    Amount, 
    CustomerID, 
    OrderDate,
    SensitivityLabel  -- Column added by Purview
FROM [dbo].[fct_Orders]

-- RLS policy applied to Agent "eng-sales-agent-001"
CREATE SECURITY POLICY SalesRLS
    ADD FILTER PREDICATE dbo.fn_securitypredicate(SalesRegion)
    ON dbo.fct_Orders
    AFTER INSERT, AFTER UPDATE;

-- Function that defines the filter
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

-- Agent connects with context
EXECUTE sp_set_session_context @key=N'SalesRegion', @value=N'LATAM,EMEA';
SELECT * FROM fct_Orders;  -- Returns only LATAM + EMEA
```

**RLS Flow for an Agent:**

```mermaid
sequenceDiagram
    actor Agent as "🤖 Agent<br/>eng-sales-001"
    participant Entra as "🪪 Entra ID"
    participant Purview as "🏷️ Purview"
    participant SQL as "📊 SQL Analytics<br/>Endpoint"
    participant Table as "📋 fct_Orders<br/>Table"
    
    Agent->>Entra: Request JWT token<br/>ClientID + Secret
    Entra-->>Agent: Return JWT with roles
    Agent->>SQL: SELECT FROM fct_Orders<br/>(JWT in header)
    SQL->>Entra: Validate JWT token
    SQL->>Purview: Query label of fct_Orders<br/>(Confidential)
    SQL->>SQL: Retrieve SalesRegion of Agent<br/>via SESSION_CONTEXT
    SQL->>Table: Apply RLS filter<br/>WHERE SalesRegion IN (LATAM,EMEA)
    Table-->>SQL: Return 1,245 rows<br/>(was 5,000)
    SQL-->>Agent: Result with RLS<br/>Only LATAM+EMEA
    Agent->>Purview: Access log recorded
    Purview-->>Purview: Audit trail: Agent->Table->Confidential->Success
```

---

##### 🔐 **Conditional Access - Adaptive Policies**

When an Agent tries to access **Confidential** or **Highly Confidential** data, Entra ID evaluates Conditional Access policies:

**Policy Examples:**

| Scenario | Condition | Action |
|---------|----------|------|
| Agent on corporate IP + business hours | `TrustedLocation AND 09:00-18:00` | ✅ Allow |
| Agent outside business hours | `After 18:00 OR Weekend` | ⚠️ Requires MFA + PIM approval |
| Agent accessing Highly Confidential | Per corporate policy | ❌ Block + Notify admin |
| Agent with anomalous behavior | Elevated risk detected | ⚠️ Step-up (MFA, manual approval) |

**Example Policy (in Entra):**

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

**Integration with PIM (Privileged Identity Management):**

To access Highly Confidential data, the Agent needs approval:

```
Request Flow:
1. Agent tries SELECT * FROM dim_Customer (Highly Confidential)
2. Entra detects elevated risk
3. PIM requires approval from a Security Admin
4. Admin receives notification:
   "Agent 'eng-sales-001' requests access to 'Highly Confidential' data.
    Reason: [Agent provided]. Approve? [Yes/No]"
5. If approved: Access granted for 15 minutes
6. If rejected: Access blocked + Alert

Timeout: Token expires after 15 minutes or when PIM approval expires
```

---

##### 📋 **Audit & Compliance - Complete Traceability**

Purview and Entra record everything:

**What is audited:**

| Event | Who | When | What | Result |
|--------|------|--------|-------|----------|
| Agent authentication | Entra ID | 2024-01-15 10:32:45Z | Agent `eng-sales-001` authenticated | ✅ Success |
| Query execution | Fabric RLS | 2024-01-15 10:33:12Z | SELECT fct_Orders (Confidential) | ✅ 1,245 rows |
| Label check | Purview | 2024-01-15 10:33:12Z | Sensitivity: Confidential, RLS: Applied | ✅ Pass |
| Conditional Access | Entra | 2024-01-15 10:33:12Z | IP: 192.168.1.100, Location: Trust, Risk: Low | ✅ Allow |
| Data export | Purview DLP | 2024-01-15 10:35:00Z | Agent exported 1,245 rows to CSV | ❌ Blocked (DLP) |
| Failed access | Fabric + Purview | 2024-01-15 10:45:00Z | Agent tried Highly Confidential (PIM pending) | ❌ Denied |

**Audit Log example:**

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

**Log retention requirements:**

- Verify each Entra, Fabric, Purview and Azure Monitor retention setting against the tenant's current license, region, workspace configuration and official service documentation.
- Record the required investigation and regulatory period, current configured retention, archive or export path, deletion behavior, owner and source access date.
- Do not assume that a default retention period or an external archive provides complete evidence until retrieval and access controls are tested.

---

##### 🔄 **Complete Access Flow (4 Validation Layers)**

```mermaid
flowchart TD
    A["🤖 Agent Request<br/>eng-sales-001<br/>SELECT FROM dim_Customer"]
    
    B["🪪 LAYER 1: ENTRA ID<br/>Agent Authentication"]
    B1["Validate JWT token<br/>Verify signature<br/>Verify expiration"]
    B2{Token valid?}
    
    C["🔒 LAYER 2: CONDITIONAL ACCESS<br/>Adaptive Security"]
    C1["Evaluate context:<br/>IP, Time, Risk,<br/>Device, Location"]
    C2{Access allowed?}
    
    D["🏷️ LAYER 3: PURVIEW LABELS<br/>Data Classification"]
    D1["Query table label<br/>dim_Customer →<br/>Highly Confidential"]
    D2{Which label?}
    
    E["🔐 LAYER 4: RLS + PIM<br/>Row-Level Security<br/>Privilege Management"]
    E1["Public/Internal →<br/>RLS applied<br/>Direct access"]
    E2["Confidential →<br/>RLS + Conditional Access<br/>Verified access"]
    E3["Highly Confidential →<br/>RLS + PIM approval<br/>Requires human"]
    E4{Approved?}
    
    F["✅ SQL Query<br/>Runs with RLS<br/>Returns filtered data"]
    
    G["📋 Audit Logging<br/>Purview + Entra<br/>Records everything"]
    
    H["📤 Result<br/>Returns to Agent<br/>With metadata"]
    
    I["❌ Access Denied<br/>Agent stops<br/>Alert sent"]
    
    A --> B
    B --> B1
    B1 --> B2
    B2 -->|No| I
    B2 -->|Yes| C
    
    C --> C1
    C1 --> C2
    C2 -->|No| I
    C2 -->|Yes| D
    
    D --> D1
    D1 --> D2
    
    D2 -->|Public/Internal| E1
    D2 -->|Confidential| E2
    D2 -->|Highly Confidential| E3
    
    E1 --> F
    E2 --> C2
    E3 --> E4
    E4 -->|Yes| F
    E4 -->|No| I
    
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

##### 🔗 **Microsoft References**

- [**Microsoft Entra Agent ID**](https://learn.microsoft.com/entra/agent-id/what-is-microsoft-entra-agent-id) - Identity foundation for AI agents; licensing and individual feature status vary
- [**Conditional Access for Agents**](https://learn.microsoft.com/entra/identity/conditional-access/agent-id) - Adaptive policies for agent identities
- [**Microsoft Entra Authentication in Fabric**](https://learn.microsoft.com/fabric/data-warehouse/entra-id-authentication) - Zero Trust authentication for SQL Analytics Endpoint
- [**Sensitivity Labels in Fabric**](https://learn.microsoft.com/fabric/governance/protected-sensitivity-labels) - Data classification with automatic protection
- [**Row-Level Security in Fabric**](https://learn.microsoft.com/fabric/security/service-admin-row-level-security) - Data filtering by user/agent context
- [**Data Governance with Purview**](https://learn.microsoft.com/azure/cloud-adoption-framework/data/governance-security-baselines-purview-data-estate-unify-data-platform) - Classification, governance and compliance
- [**Audit Logging in Purview**](https://learn.microsoft.com/purview/audit-solutions-overview) - Tracking and regulatory compliance
- ⏹️ **Conditional Access:** Approvals for sensitive data

### 📋 Technical Summary — From Raw Data to AI Insights

| Component | Function | Do Agents Use It? |
|---|---|---|
| **OneLake** | Single logical storage, no silos | Implicitly (via SQL endpoint) |
| **Delta Lake** | ACID guarantee, reliability, time-travel | Implicitly (through tables) |
| **Shortcuts** | Access to external data without copying | ✅ Yes (see them as local tables) |
| **SQL Analytics Endpoint** | T-SQL interface for queries | ✅ Yes (primary access method) |
| **Medallion (Bronze→Silver→Gold)** | Progressive organization and quality | ✅ Yes (access the Gold layer) |
| **Data Products** | Curated packages for reuse | ✅ Yes (primary consumer) |
| **Purview Labels** | Data classification and governance | ✅ Yes (define who accesses what) |
| **Entra ID (Agent ID)** | Agent identity and authentication | ✅ Yes (authentication + audit) |

**Microsoft References:**
- [Understand medallion lakehouse architecture for Microsoft Fabric with OneLake](https://learn.microsoft.com/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [What is a lakehouse in Microsoft Fabric?](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)
- [What is the SQL analytics endpoint for a lakehouse?](https://learn.microsoft.com/fabric/data-engineering/lakehouse-sql-analytics-endpoint)
- [Delta Lake table format interoperability](https://learn.microsoft.com/fabric/fundamentals/delta-lake-interoperability)

---

