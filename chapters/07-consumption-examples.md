## 🤖 6. Consumption Examples

These examples illustrate different points on the complexity ladder. They are alternatives, not mandatory stages or one universal product chain.

### ✅ Example 1 — Existing Microsoft Capability

**Need:** A user summarizes meetings, files and messages already available in Microsoft 365.

**Pattern:** `User → Microsoft 365 Copilot + Work IQ → Permission-trimmed response`

Use the existing SaaS capability when it meets the business requirement. Validate licensing, eligible users, source permissions, sensitivity behavior and service limits before production rollout.

### ✅ Example 2 — Deterministic Governed Metric

**Need:** Finance asks for an approved quarterly margin calculation.

**Pattern:** `User experience → Controlled semantic or API query → Certified metric`

Use Fabric IQ, a Fabric data agent, a DAX/SQL query or a governed API according to the authoritative serving layer. Allow-list operations, validate parameters, propagate the intended identity, shape results and test RLS, CLS or ACL behavior for that path. An agent is unnecessary when the query contract is predictable.

### ✅ Example 3 — Grounded Knowledge with Citations

**Need:** An employee asks how an internal policy applies and needs supporting citations.

**Pattern:** `User experience → Foundry IQ or supported connector → Approved knowledge + citations`

Prefer built-in retrieval before custom RAG. Move to Azure AI Search or custom retrieval only when ranking, lifecycle, schema, networking or regulatory requirements cannot be met by the managed capability.

### ✅ Example 4 — Single Agent with Controlled Tools

**Need:** A user asks to analyze a margin change, retrieve an approved benchmark and draft recommended actions.

**Pattern:** `User → Selected agent runtime → Governed metric tool + approved knowledge tool → Draft → HITL when required`

Use Microsoft Foundry Agent Service, Copilot Studio or an explicitly hosted Microsoft Agent Framework application only after retrieval or deterministic automation proves insufficient for the bounded multi-step requirement. Tool identities, scopes, inputs, outputs, retries, audit and rollback behavior must be tested independently. Model selection, including Microsoft or partner models available in Foundry, follows quality, availability, latency, cost and compliance evidence.

### ✅ Example 5 — Mixed or Multi-Agent Exception

Use Copilot Studio with Foundry, or multiple specialized agents, only when one runtime cannot reliably satisfy independently owned channel, orchestration or domain requirements. Record the failed single-runtime baseline and the incremental latency, cost, operational boundary and governance burden.

### Cross-Cutting Validation

- Evaluators measure groundedness, task success, safety and regression before release and continuously where appropriate; they do not automatically block every response.
- Guard rails enforce deterministic controls at required input, tool and output checkpoints.
- ASSERT and Agent Control Specification can support evaluation and portable control contracts where their maturity and product support fit the workload.
- Every selected product and downstream dependency requires a **Fit**, **Conditional fit** or **Not fit** capacity verdict based on peak demand and measured evidence.

---

