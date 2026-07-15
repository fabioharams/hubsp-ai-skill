## ⚖️ 4. Adoption Strategies (A vs B)

### 🅰️ Scenario A — Self-Service Agents

**✅ Pros**
- high innovation
- speed
- flexibility

**❌ Cons**
- shadow AI risk
- inconsistency
- variable cost

### 🅱️ Scenario B — Curated Data

**✅ Pros**
- governance
- consistency
- control

**❌ Cons**
- lower agility
- IT dependency

### 📊 Visual Comparison of Scenarios

```mermaid
graph TB
    subgraph ScenarioA ["🅰️ CENÁRIO A - Self-Service (Shadow AI)"]
        A1["📂 Dados Variados<br/>─────────────────<br/>ERP, CRM, Planilhas<br/>APIs públicas"]
        A2["⚡ Sem Classificação<br/>─────────────────<br/>Busca rápida<br/>Sem workflow"]
        A3["🤖 Agentes Livres<br/>─────────────────<br/>Acessam dados<br/>brutos direto"]
        A4["⚠️ Riscos<br/>─────────────────<br/>❌ Vazamento PII<br/>❌ Inconsistência<br/>❌ Sem auditoria<br/>❌ Shadow IT"]
        A5["✅ Vantagens<br/>─────────────────<br/>✓ Rápido<br/>✓ Inovativo<br/>✓ Flexível"]
        
        A1 --> A2
        A2 --> A3
        A3 --> A4
        A3 --> A5
    end
    
    subgraph ScenarioB ["🅱️ CENÁRIO B - Dados Tratados (Governed)"]
        B1["📊 Dados Estruturados<br/>─────────────────<br/>Fabric Lakehouse<br/>Medallion Pattern"]
        B2["🏷️ Classificação<br/>Purview + Entra<br/>─────────────────<br/>Public/Confidential<br/>Row-Level Security"]
        B3["🔐 Agentes Controlados<br/>─────────────────<br/>Acessam dados<br/>Gold via SQL Endpoint"]
        B4["✅ Benefícios<br/>─────────────────<br/>✓ Governança<br/>✓ Consistência<br/>✓ Auditável<br/>✓ Compliance"]
        B5["⚠️ Desafios<br/>─────────────────<br/>❌ Mais lento<br/>❌ Depende TI<br/>❌ Planejamento"]
        
        B1 --> B2
        B2 --> B3
        B3 --> B4
        B3 --> B5
    end
    
    style A1 fill:#FFB347,stroke:#FF8C00,color:#000
    style A2 fill:#FF6347,stroke:#CC5555,color:#fff
    style A3 fill:#FF4444,stroke:#CC0000,color:#fff
    style A4 fill:#DC143C,stroke:#8B0000,color:#fff
    style A5 fill:#FFD93D,stroke:#CCB030,color:#000
    
    style B1 fill:#87CEEB,stroke:#4682B4,color:#000
    style B2 fill:#4A90E2,stroke:#2E5C8A,color:#fff
    style B3 fill:#3D7E6B,stroke:#2D5E4B,color:#fff
    style B4 fill:#50C878,stroke:#3A9B5C,color:#fff
    style B5 fill:#FFD93D,stroke:#CCB030,color:#000
```

### 🎯 Conclusion
The ideal model is **hybrid and evolutionary**:
- **Short term (0-4 months)**: Start with **Scenario B** (M365 Copilot + curated data) to establish guardrails
- **Medium term (4-10 months)**: Evolve to **controlled Scenario A** (Self-service with governance)
- **Long term (10+ months)**: **Mature hybrid** (some free agents, but in sandbox; majority governed)

**Rule**: Security and consistency first, fast innovation within established guardrails.

---

> Content moved to [references/03-roi-ai-vs-man-hour.md](references/03-roi-ai-vs-man-hour.md) — ROI Model — AI vs. Person-Hour Cost.

