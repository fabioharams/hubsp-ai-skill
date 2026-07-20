## 🔀 17. Agent Orchestration — Patterns, Implementation and Governance

### 📌 Definition

**Agent orchestration** is the process of coordinating multiple specialized AI agents to solve complex problems that no single agent can solve completely. Each agent executes its task within its domain, passes the result to the next, and a **central orchestrator** manages the flow, routing decisions, error handling and final response composition.

**Differentiation:**
- **Single agent**: Responds to a request with an LLM + tools. Fast, low latency, but limited to one domain.
- **Orchestrated multi-agent**: Multiple specialized agents solve different aspects of the problem. More powerful, but more complex to govern and with higher latency.

### 🎯 When Orchestration Is Worth It

```mermaid
graph TD
    A["❓ Problema requer<br/>múltiplos domínios?"]
    
    B["Não → Use agente único"]
    C["Sim → Múltiplos especialistas?"]
    
    D["Não (um agente faz tudo) → Agente único"]
    E["Sim → Multi-agent Orchestration"]
    
    A -->|Não| B
    A -->|Sim| C
    C -->|Não| D
    C -->|Sim| E
    
    B --> F["✅ Simple, fast,<br/>easy to govern"]
    D --> F
    E --> G["✅ Powerful,<br/>domain-expert,<br/>but complex"]
    
    style B fill:#90EE90,stroke:#228B22,color:#000,stroke-width:2px
    style D fill:#90EE90,stroke:#228B22,color:#000,stroke-width:2px
    style E fill:#87CEEB,stroke:#4682B4,color:#000,stroke-width:2px
    style F fill:#FFD700,stroke:#DAA520,color:#000,stroke-width:2px
    style G fill:#FFD700,stroke:#DAA520,color:#000,stroke-width:2px
```

**Examples of complex problems:**
- ✅ **Support request**: Triage Agent → Analysis Agent → Resolution Agent → Notifier
- ✅ **Contract analysis**: Parser Agent → Risk Agent → Compliance Agent → Summarizer
- ✅ **Demand forecasting**: Data Agent → Model Agent → Business Rules Agent → Planner

### 🏗️ Four Orchestration Patterns

#### **Pattern 1: Sequential (Pipeline)**

Agents execute one after another, passing results from one to the next.

```mermaid
flowchart LR
    A["👤 User Input"] --> B["Agent 1<br/>─────<br/>Classify<br/>& Parse"]
    B --> C["Agent 2<br/>─────<br/>Analyze<br/>& Enrich"]
    C --> D["Agent 3<br/>─────<br/>Recommend<br/>Solution"]
    D --> E["📤 Final<br/>Response"]
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style D fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style E fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
```

**Characteristics:**
- ✓ Simple to implement and debug
- ✓ Predictable latency (sum of latencies)
- ✗ Failure in one agent breaks everything
- ✗ No parallelism

**Ideal use:** Linear workflows (support → analysis → resolution).

---

#### **Pattern 2: Parallel (Fan-out)**

Multiple agents execute simultaneously, then results are consolidated.

```mermaid
flowchart TD
    A["👤 User Input:<br/>Avaliar requisição"] --> B["🎯 Dispatcher<br/>─────<br/>Route & Split"]
    
    B --> C["💰 Finance Agent<br/>─────<br/>Verificar orçamento"]
    B --> D["⚠️ Risk Agent<br/>─────<br/>Avaliar risco"]
    B --> E["👥 Approval Agent<br/>─────<br/>Checar permissões"]
    
    C --> F["🏁 Consolidator<br/>─────<br/>Merge decisions"]
    D --> F
    E --> F
    
    F --> G["📤 Final Response<br/>─────<br/>Aprovado ou<br/>recomendações"]
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#FFB347,stroke:#CC8835,color:#000,stroke-width:2px
    style C fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style D fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style E fill:#50C878,stroke:#3A9B5C,color:#fff,stroke-width:2px
    style F fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:2px
    style G fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
```

**Characteristics:**
- ✓ Reduced latency (parallel)
- ✓ Partial resilience (one agent fails, others continue)
- ✗ More complex to implement
- ✗ Consolidation can be difficult if responses conflict

**Ideal use:** Parallel evaluations (cost, risk, compliance).

---

#### **Pattern 3: Conditional (Decision Tree)**

Decision logic determines which agent to execute next.

```mermaid
flowchart TD
    A["👤 User Input:<br/>Demanda do cliente"] --> B["🔀 Decision Agent<br/>─────<br/>Classificar tipo"]
    
    B -->|"Simples<br/>(FAQ)"| C["🤖 FAQ Agent<br/>─────<br/>Responder"]
    B -->|"Complexo<br/>(Análise)"| D["📊 Analyst Agent<br/>─────<br/>Investigar"]
    B -->|"Crítico<br/>(Escalar)"| E["🚨 Escalation<br/>─────<br/>Human approval"]
    
    C --> F["📤 Response"]
    D --> F
    E --> F
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#FFB347,stroke:#CC8835,color:#000,stroke-width:2px
    style C fill:#90EE90,stroke:#228B22,color:#000,stroke-width:2px
    style D fill:#87CEEB,stroke:#4682B4,color:#000,stroke-width:2px
    style E fill:#FFA500,stroke:#FF6347,color:#fff,stroke-width:2px
    style F fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
```

**Characteristics:**
- ✓ Intelligent routing (resource savings)
- ✓ Automatic escalation when needed
- ✗ Decision can be incorrect
- ✗ No redundancy

**Ideal use:** Dynamic routing by complexity (simple FAQ vs. deep analysis vs. escalation).

---

#### **Pattern 4: Feedback Loop (Iterative)**

An agent executes, evaluates the result, and iterates until success or limit.

```mermaid
flowchart TD
    A["👤 User Input:<br/>Gerar relatório"] --> B["🔄 Agent<br/>─────<br/>Primeira tentativa"]
    
    B --> C["✅ Evaluator<br/>─────<br/>Qualidade ok?"]
    
    C -->|"Sim<br/>(✓ >= 0.85)"| D["📤 Final Response"]
    C -->|"Não<br/>(✗ < 0.85)"| E["🔧 Feedback<br/>─────<br/>Erros encontrados"]
    
    E --> F["💭 Agent<br/>─────<br/>Refinar +<br/>iterar"]
    
    F --> G["⚠️ Max iterations?"]
    G -->|"Não (< 3)"| C
    G -->|"Sim (>= 3)"| H["🚨 Escalate<br/>to human"]
    
    H --> D
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style C fill:#FFB347,stroke:#CC8835,color:#000,stroke-width:2px
    style D fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style E fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:2px
    style F fill:#7B68EE,stroke:#5A4DB0,color:#fff,stroke-width:2px
    style G fill:#FFB347,stroke:#CC8835,color:#000,stroke-width:2px
    style H fill:#FF6347,stroke:#DC143C,color:#fff,stroke-width:2px
```

**Characteristics:**
- ✓ Self-improvement (refines until success)
- ✓ Higher reliability (retries)
- ✗ Potentially high latency
- ✗ Risk of infinite loops (needs limit)

**Ideal use:** High-quality content generation (reports, analyses).

### 📋 Pattern Comparison

| Pattern | Latency | Complexity | Resilience | Best for |
|--------|----------|--------------|-------------|------------|
| **Sequential** | Low | Low | Low | Simple pipelines, fixed order |
| **Parallel** | Very low | Medium | Medium | Independent evaluations |
| **Conditional** | Variable | Medium | Medium | Intelligent routing |
| **Feedback Loop** | High | High | High | Critical quality |

### 💼 Practical Use Case: Technical Support Request

**Scenario:** Customer opens a support ticket. The system must: (1) classify urgency, (2) extract technical data, (3) find a similar solution, (4) generate a response or escalate.

**Architecture (Sequential + Conditional):**

```mermaid
flowchart TD
    A["👤 Ticket entrante<br/>─────<br/>Descrição do problema"] 
    
    A --> B["Agent 1: Triager<br/>─────<br/>Extrair: urgência,<br/>categoria, impacto"]
    
    B --> C{Urgência?}
    
    C -->|"Baixa<br/>(FAQ)"| D["Agent 2: FAQ Bot<br/>─────<br/>Buscar solução<br/>em knowledge base"]
    C -->|"Alta<br/>(Expert)"| E["Agent 3: Expert<br/>─────<br/>Análise profunda<br/>+ debugging"]
    C -->|"Crítica<br/>(SEV-1)"| F["Agent 4: Escalation<br/>─────<br/>Notificar time<br/>+ criar P1"]
    
    D --> G["✅ Evaluator<br/>─────<br/>Resposta ok?"]
    E --> G
    F --> G
    
    G -->|"Sim"| H["📤 Enviar resposta<br/>ao cliente"]
    G -->|"Não"| I["🔀 Redirecionar<br/>a humano"]
    
    H --> J["📊 Log & Metrics<br/>─────<br/>Tempo resolução,<br/>satisfação, custo"]
    I --> J
    
    style A fill:#FF6B6B,stroke:#CC5555,color:#fff,stroke-width:2px
    style B fill:#4A90E2,stroke:#2E5C8A,color:#fff,stroke-width:2px
    style D fill:#90EE90,stroke:#228B22,color:#000,stroke-width:2px
    style E fill:#87CEEB,stroke:#4682B4,color:#000,stroke-width:2px
    style F fill:#FF6347,stroke:#DC143C,color:#fff,stroke-width:2px
    style G fill:#FFB347,stroke:#CC8835,color:#000,stroke-width:2px
    style H fill:#FFD93D,stroke:#CCB030,color:#333,stroke-width:2px
    style I fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:2px
    style J fill:#D3D3D3,stroke:#808080,color:#000,stroke-width:2px
```

### 🔧 Foundry Implementation

```python
import json
import os
from datetime import datetime

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
openai_client = project_client.get_openai_client()

# These versioned prompt agents are created and governed in the Foundry project.
TRIAGER_AGENT = "support-triager"
FAQ_AGENT = "support-faq"
EXPERT_AGENT = "support-expert"

def invoke_agent(agent_name: str, user_message: str) -> str:
    response = openai_client.responses.create(
        input=user_message,
        extra_body={
            "agent_reference": {
                "name": agent_name,
                "type": "agent_reference",
            }
        },
    )
    return response.output_text

# Orchestration logic
def handle_support_ticket(ticket_text: str):
    # Step 1: Classify with Triager
    triage_response = invoke_agent(
        TRIAGER_AGENT,
        f"Classify this ticket as JSON with urgency, category and impact: {ticket_text}",
    )

    triage_result = json.loads(triage_response)
    urgency = triage_result["urgency"]

    # Step 2: Route based on urgency
    if urgency == "Low":
        resolution = invoke_agent(FAQ_AGENT, ticket_text)
    elif urgency in ["Medium", "High"]:
        resolution = invoke_agent(EXPERT_AGENT, ticket_text)
    else:  # Critical
        # Escalate to human
        resolution = "HUMAN_ESCALATION"

    return {
        "urgency": urgency,
        "resolution": resolution,
        "timestamp": datetime.now().isoformat()
    }

# Usage
result = handle_support_ticket("My server has been offline for 2 hours")
print(result)
```

This example uses `azure-ai-projects` 2.x and the Responses API. For a production multi-agent system, enforce structured outputs, timeouts, retries, per-agent authorization and trace correlation rather than parsing unconstrained text.

### 🛡️ Challenges and Best Practices

#### **Challenge 1: Error Cascade**
If Agent 1 fails, Agent 2 receives invalid input. 

**Mitigation:**
- ✓ Validate each agent's output with schema
- ✓ Implement automatic fallback / retry
- ✓ Error log at each stage with context

#### **Challenge 2: Accumulated Latency**
In sequential, latency = Sum(Agent1 latency + Agent2 latency + ...).

**Mitigation:**
- ✓ Use parallel when possible
- ✓ Monitor end-to-end SLA
- ✓ Cache frequent responses

#### **Challenge 3: Response Inconsistency**
Agents may conflict or provide contradictory information.

**Mitigation:**
- ✓ Version instructions centrally
- ✓ Integrated orchestration testing (not just isolated agent)
- ✓ Consolidator with explicit conflict resolution logic

#### **Challenge 4: Multi-Agent Governance**
Who is responsible if something goes wrong? Agent 1? Agent 2? Orchestrator?

**Mitigation:**
- ✓ Assign owner per agent, owner per workflow
- ✓ Test permissions (RLS) in orchestration context
- ✓ Audit trail of each invocation and decision

#### **Challenge 5: Complex Debugging**
When the workflow fails, which agent is to blame?

**Mitigation:**
- ✓ Structured logging (OpenTelemetry) at each stage
- ✓ Distributed tracing (trace ID traverses workflow)
- ✓ Replicable simulation / test case

### ✅ Orchestration Checklist

Before launching a multi-agent workflow:

```
□ Each agent has versioned and documented instructions
□ Outputs from each agent are validated against schema
□ Integrated tests cover happy path + edge cases
□ End-to-end latency within SLA
□ RLS tested in orchestration context (Agent 1 → Agent 2 → response)
□ Permissions for each agent defined (which table, which operation)
□ Fallback/retry logic implemented for each stage
□ Monitoring & alerts configured (latency, failure, costs)
□ Rollback plan documented
□ Owner designated per agent and per workflow
□ Use case documentation and visual flow updated
```

### 📚 References — Orchestration in Foundry

- [Add other agents in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/authoring-add-other-agents)
- [Connect to an A2A agent from Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/agent-to-agent)
- [AI agent orchestration patterns](https://learn.microsoft.com/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [Foundry Agent Service tool catalog](https://learn.microsoft.com/azure/foundry/agents/concepts/tool-catalog)

---

