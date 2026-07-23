# Reference 02b — Microsoft Fabric: Medallion Architecture

> Part of the layered reference architecture. See `references/02-reference-architecture-layers.md` for the layer overview. Continues `references/02a-fabric-onelake-delta-shortcuts.md`. Load this file only when Bronze/Silver/Gold (medallion) data organization is in scope.

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
