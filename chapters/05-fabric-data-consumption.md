## 🔗 5. Fabric Data Consumption by Multiple Agents

### 🧠 Central Insight — OneLake as a Shared Corporate Asset

**Fonte oficial:** [Microsoft Fabric - OneLake Overview](https://learn.microsoft.com/fabric/onelake/onelake-overview)

> **"OneLake is a unified, enterprise-level data lake integrated with Microsoft Fabric that serves as the centralized storage layer for all of the organization's data workloads"**

#### Why this matters for agents:
- **A single source of truth:** All agents query the same data, reducing inconsistencies and conflicts
- **No duplication:** OneLake uses Zero-Copy Access — data remains in a single location while multiple agents access via **Shortcuts** (virtual references) and **SQL Analytics Endpoint**
- **Reuse by design:** Each agent (Copilot, Claude, AgentA, AgentB) leverages the same data asset, reducing ETL and complexity
- **Centralized governance:** Policies (sensitivity labels, RLS, audit) are applied once in OneLake and inherited by all consumers

**Consequence:** From "data in silos per agent" to "agents as consumers of governed data".

---

### 🏗️ Architecture — Three Consumption Layers

#### **Layer 1: Unified Storage (OneLake)**

```mermaid
graph TD
    A["☁️ OneLake<br/>(ADLS Gen2 – SaaS)<br/>─────────────<br/>Tenant único<br/>Centralizado"]
    
    B1["🏢 Workspace 1<br/>Sales"]
    B2["🏢 Workspace 2<br/>Finance"]
    
    C1["📊 Lakehouse Sales"]
    C2["📊 Lakehouse Finance"]
    
    D1["🟤 Bronze<br/>Dados Brutos<br/>As-is"]
    D2["🟡 Silver<br/>Dados Validados<br/>Delta Tables"]
    D3["🟢 Gold<br/>Negócio Pronto<br/>Ready-to-consume"]
    
    E["🟢 Gold Layer<br/>Dados Financeiros<br/>Consolidado"]
    
    F["🔗 Cross-Workspace<br/>Shortcuts<br/>─────────────<br/>Acessos virtuais<br/>Zero-copy<br/>Sem duplicação"]
    
    A --> B1
    A --> B2
    A --> F
    
    B1 --> C1
    B2 --> C2
    
    C1 --> D1
    C1 --> D2
    C1 --> D3
    
    C2 --> E
    
    style A fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:3px
    style B1 fill:#87CEEB,stroke:#4682B4,color:#000,stroke-width:2px
    style B2 fill:#87CEEB,stroke:#4682B4,color:#000,stroke-width:2px
    style C1 fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style C2 fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style D1 fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style D2 fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style D3 fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style E fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style F fill:#FFB347,stroke:#FF8C00,color:#000,stroke-width:2px
```

**Technical characteristics** (Microsoft Fabric official):
- **Unique hierarchy:** One OneLake per tenant, multiple workspaces, multiple lakehouses
- **Delta Lake standard:** All table data is stored in Delta Parquet format (ACID transactions, schema enforcement, time-travel)
- **Shortcuts (zero-copy):** Data in external ADLS Gen2 or other workspaces appears as local tables — no ETL, no duplication
- **Automatic provisioning:** Each lakehouse automatically creates /Tables and /Files, without infrastructure complexity

#### **Layer 2: Multiple Access Interfaces**
```mermaid
graph TB
    subgraph OL["☁️ ONELAKE (Unified Tenant Data Lake)"]
        BRONZE["🟤 Bronze<br/>Raw Data<br/>As-is Format"]
        SILVER["🟡 Silver<br/>Clean Data<br/>Delta Tables"]
        GOLD["🟢 Gold<br/>Business Data<br/>Ready-to-consume"]
    end
    
    SAE["📊 SQL Analytics<br/>Endpoint<br/>─────────────<br/>T-SQL Interface<br/>RLS-enabled"]
    
    SC["🔗 Shortcuts<br/>─────────────<br/>Zero-copy<br/>Virtual refs<br/>Cross-workspace"]
    
    COPILOT["🤖 M365 Copilot<br/>Teams/Word/Excel"]
    AGENTA["🤖 Agent A<br/>Microsoft Foundry<br/>Claude/GPT"]
    AGENTB["🤖 Agent B<br/>Copilot Studio<br/>Low-code"]
    BI["📈 Power BI<br/>Visualização"]
    
    BRONZE --> SILVER
    SILVER --> GOLD
    GOLD --> SAE
    GOLD --> SC
    GOLD --> BI
    
    SAE --> COPILOT
    SAE --> AGENTA
    SAE --> AGENTB
    SC --> AGENTA
    SC --> AGENTB
    
    style OL fill:#E8F4F8,stroke:#4A90E2,color:#000,stroke-width:3px
    style BRONZE fill:#8B6F47,stroke:#664D2A,color:#fff,stroke-width:2px
    style SILVER fill:#C9A961,stroke:#9B7E48,color:#fff,stroke-width:2px
    style GOLD fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style SAE fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style SC fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style COPILOT fill:#FF9999,stroke:#CC6666,color:#fff
    style AGENTA fill:#FF9999,stroke:#CC6666,color:#fff
    style AGENTB fill:#FF9999,stroke:#CC6666,color:#fff
    style BI fill:#FFD93D,stroke:#CCB030,color:#000
```

**Interfaces de acesso:**
1. **SQL Analytics Endpoint (recomendado para agentes)**
   - Interface T-SQL nativa (SELECT, JOINs, stored procs)
   - Row-Level Security integrada (filtra por identidade do agente)
   - Automatic sync with Delta tables
   - Native Entra ID authentication

2. **Shortcuts (for cross-workspace references)**
   - Data in another lakehouse/workspace appears as local tables
   - No ETL, no COPY — direct fetch from ADLS Gen2
   - Centralized governance maintained at source
   - Ideal for data mesh and cross-domain sharing

3. **Microsoft Graph API (for Work IQ)**
   - Access to SharePoint, OneDrive, Exchange data
   - Authentication via OAuth 2.0 Entra ID
   - Contextual data for each user

#### **Layer 3: Per-Agent Consumption Pattern**

| Agent Type | Interface | Data Consumed | Authentication | Governance |
|---|---|---|---|---|
| **M365 Copilot (Work IQ)** | Microsoft Graph API | SharePoint, OneDrive, Teams | User context (Entra) | Purview labels |
| **Claude via Microsoft Foundry** | SQL Analytics Endpoint | OneLake Gold (Delta) | Managed Identity | RLS + Labels |
| **Copilot Studio** | SQL Analytics Endpoint or Connectors | OneLake Gold or SaaS APIs | User token or MI | RLS + Labels |
| **Custom Agent (Python/Node)** | SQL driver (pyodbc, mssql) | OneLake Gold (Delta) | Entra ID auth | RLS + Labels |

---

### ✅ Benefits — Why This Architecture Works

#### **1. Data Consistency (Single Source of Truth)**
- All 3 areas (Copilot, Agent A, Agent B) query the **same Gold layer** in OneLake
- Reduction of "conflicting versions" of the same data
- Decisions based on a single corporate truth

**Impact:** Reduces errors, conflicts and rework

#### **2. Reuse without Duplication (Zero-Copy)**
- Data ingested **once** into OneLake
- Agents, BI, Data Science access via SQL Analytics Endpoint or Shortcuts
- **No COPY, no replication, no duplication** — saves 40-60% in storage vs data silos

**Impact:** Reduces cost (less storage), reduces latency (fresher data)

#### **3. Automatically Inherited Governance**
- Sensitivity labels applied in Purview once
- Row-Level Security (RLS) configured in SQL Analytics Endpoint once
- All agents inherit these policies — no repeated reconfigurations

**Impact:** Compliance, security, audit "for free" for each new agent

#### **4. Horizontal Scalability**
- Adding 10 new agents **does not require** copying data 10 times
- Each agent is a consumer, not an isolated producer
- OneLake scales automatically (ADLS Gen2 as backbone)

**Impact:** Viable Data Mesh — domains can collaborate without complex infrastructure

---

### 📍 Real Reuse Example

**Scenario:** Tim from Sales wants "customer ranking by revenue"; Finance wants "margin analysis by customer"; Marketing wants "segmentation by lifetime value"

**Without Fabric (data silos):**
- Tim creates Sales table with 5M records
- Finance creates Margins table with same 5M records (DUPLICATES)
- Marketing creates LTV table with same 5M records (TRIPLICATES)
- 3x storage, 3x ETL, inconsistent security policies

**With Fabric (OneLake unified):**
- Bronze: ingest customer data once
- Silver: validate once → single Delta table
- Gold: create dim_Customer once
- Tim, Finance, Marketing query the same dim_Customer via SQL or Shortcuts
- Automatic RLS: Tim sees only his region, Finance sees consolidated, etc.

**Result:** -60% storage, -40% ETL time, elevated consistency

---

