## 🤖 6. Consumption Examples

### ✅ Example 1 — Copilot
- queries Fabric data
- generates insights
- authentication via Microsoft Graph API with Entra ID
- SharePoint and OneLake data consumed via Purview Sensitivity Label

### ✅ Example 2 — Claude via Foundry
- uses Fabric as context
- executes advanced reasoning
- accesses data via OneLake SQL Analytics Endpoint with Entra ID authentication
- 1M token context window (Opus 4.6) — processes long documents, contracts, full financial reports in a single call
- Constitutional AI — safe, auditable responses aligned with corporate policies by design

#### 🔧 Technical flow for Example 2
`User → Copilot Studio (front) → Microsoft Foundry Agent Service → Claude Opus 4.6 (reasoning) → SQL Analytics Endpoint (Fabric OneLake) → Gold Data (Delta Parquet) → Grounded + evaluated response`

### ✅ Example 3 — Multi-step Agent with Tool Calls (medium term)
- user requests: "analyze the impact of the margin drop in Q3 and suggest actions"
- Agent (Microsoft Foundry) makes tool call 1: fetches financial data from Fabric via SQL Endpoint
- Agent makes tool call 2: fetches industry benchmarks via MCP (web search)
- Claude reasons over both contexts → generates structured analysis + recommendations
- Evaluator validates groundedness and task adherence → response delivered to user via Copilot Studio
- ASSERT can be used in the development cycle to transform corporate policies into executable tests before rollout
- Agent Control Specification (ACS) can be used at runtime to apply deterministic controls at critical checkpoints such as input, tool execution and output

📌 Claude can operate via Foundry and integrate with systems and data

**Architectural reading:** in this pattern, **ASSERT** reinforces evaluation discipline before and after changes; **ACS** reinforces the consistent application of guard rails during execution.

---

