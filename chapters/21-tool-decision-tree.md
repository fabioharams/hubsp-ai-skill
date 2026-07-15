## 🌳 C. Decision Tree — When to Choose Which Tool

```mermaid
graph TD
    A["🎯 Você precisa de um agente de IA"]
    
    B{Complexidade<br/>técnica?}
    B1["Baixa"]
    B2["Média"]
    B3["Alta"]
    
    C["M365 Copilot<br/>✅ Embed em Teams/Word<br/>✅ Baixo risco<br/>✅ Sem código"]
    D["Copilot Studio<br/>✅ Low-code<br/>✅ Conversacional<br/>✅ Skills/Topics"]
    E["Foundry<br/>✅ Code-first<br/>✅ Reasoning avançado<br/>✅ Multi-agent"]
    
    F{Seu time?}
    F1["Operadores"]
    F2["Analistas"]
    F3["Engenheiros"]
    
    A --> B
    B --> B1
    B --> B2
    B --> B3
    
    B1 --> F
    B2 --> D
    B3 --> E
    
    F --> F1
    F --> F2
    F --> F3
    
    F1 --> C
    F2 --> D
    F3 --> E
    
    style C fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:3px
    style D fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:3px
    style E fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:3px
```

| Tool | When | Ideal team | Time |
|---|---|---|---|
| **M365 Copilot** | Simple cases, M365 data | End users | < 1 month |
| **Copilot Studio** | Conversational agents | Analysts | 1-3 months |
| **Foundry** | Complex reasoning | Engineers | 2-6 months |

---

