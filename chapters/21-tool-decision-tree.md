## 🌳 C. Decision Tree — Select the Pattern Before the Tool

```mermaid
graph TD
    A["Business requirement"] --> B{"Existing Microsoft or SaaS<br/>capability meets it"}
    B -->|Yes| C["Configure and validate SaaS"]
    B -->|No| D{"Predictable rules or API<br/>workflow meets it"}
    D -->|Yes| E["Deterministic automation"]
    D -->|No| F{"One-step generative<br/>work without grounding"}
    F -->|Yes| G["Direct LLM application"]
    F -->|No| H{"Grounded answers without<br/>autonomous actions"}
    H -->|Yes| I["RAG or built-in retrieval"]
    H -->|No| J{"Bounded multi-step<br/>reasoning or tools"}
    J -->|Yes| K["Single AI Agent"]
    J -->|No| L{"Independent specialists or<br/>runtimes required now"}
    L -->|Yes with evidence| M["Multi-agent or mixed exception"]
    L -->|No| N["Keep simpler pattern<br/>and define escalation trigger"]

    style C fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:3px
    style E fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:3px
    style I fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:3px
    style K fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:3px
    style M fill:#E85D04,stroke:#A33F00,color:#fff,stroke-width:3px
```

After the pattern is selected, compare Microsoft products by required capability, data path, identity, engineering skill, channel, capacity, cost, region and feature status. Team profile and delivery speed are constraints, not substitutes for architecture requirements. Every production recommendation requires a **Fit**, **Conditional fit** or **Not fit** capacity verdict.

---

