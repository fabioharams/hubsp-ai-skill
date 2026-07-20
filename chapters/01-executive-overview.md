## 📌 1. Executive Overview

### 🎯 Objective

Define a corporate AI adoption approach that:

- starts with the simplest option that reliably meets the business requirement
- uses governed data and approved domain authorities when grounding is required
- selects Microsoft IQ context workloads and an agent runtime only when justified
- applies guard rails, evaluators and human oversight according to risk
- validates capacity, scale, cost and operational readiness before production

### 🧠 Core Principle

> "AI scales value only when automated decisions are reliable, governed and measurable"

### 🏢 Corporate architecture — what it means in this context

In this guide, corporate architecture is the integrated design of processes, data, identity, security, governance, capacity and user experience for reliable AI-assisted operations. It does not require every scenario to use an agent or Microsoft Fabric. The architecture stops at the first option that meets current requirements: an existing Microsoft or SaaS capability, deterministic automation, a direct LLM call, RAG, a single AI Agent, and only then a multi-agent or mixed solution when independently justified.

When these layers are needed, their roles remain explicit. Microsoft 365 Copilot and business applications provide user experiences. Work IQ, Foundry IQ, Fabric IQ and, when applicable, Web IQ provide complementary context. Microsoft Foundry Agent Service or Copilot Studio provides the selected managed agent platform. Microsoft Agent Framework can implement application-managed orchestration but requires explicit hosting unless deployed as a Foundry hosted agent. Microsoft Fabric provides governed analytical data and business semantics when consolidation or semantic reuse is required. Microsoft Entra ID and Microsoft Purview support identity, authorization, classification and protection, while guard rails and evaluators provide cross-cutting control and measurement.

### ⭐ Why this matters

Corporate architecture transforms isolated experiments into measurable operational capabilities. Without a common decision and control framework, solutions can use conflicting authorities, duplicate integrations and introduce unnecessary technical complexity. With the right design, the organization establishes shared governed authority and business semantics for each domain, while preserving legitimate differences caused by role, region, legal entity, purpose or freshness. This reduces rework and improves traceability without forcing every workload through one physical data store or retrieval path.

Security and quality are validated for each end-to-end path. User identity, workload identity, RLS, CLS, ACLs, sensitivity labels, result filtering and audit coverage must not be assumed to transfer automatically between products. Evaluators can support design-time testing, release gates, continuous evaluation or selected runtime checks; blocking controls must be implemented explicitly as guard rails where the risk requires them.

Before production approval, every selected Microsoft product, SaaS capability, license, SKU and material downstream dependency receives a **Fit**, **Conditional fit** or **Not fit** capacity verdict. The verdict considers peak demand, entitlement, quota, concurrency, regional availability, downstream limits, headroom, load or pilot evidence, monitoring signals and scale triggers. Unknown demand or quota remains a pre-production validation gate.

### 🧩 Practical examples

**Example 1 — Executive support:** an executive asks Microsoft 365 Copilot why the margin dropped in the quarter. Work IQ supplies the user's Microsoft 365 context. When a governed financial metric is required, Fabric IQ, a Fabric data agent or a controlled semantic query can provide the approved calculation. A domain agent is introduced only if the request requires bounded multi-step reasoning or tool use that the simpler retrieval path cannot satisfy. Identity propagation and effective permissions are validated across the complete path.

**Example 2 — Operations workflow:** deterministic rules or an existing monitoring capability first detect and classify an increase in incidents. If users also require conversational investigation and bounded orchestration, a Copilot Studio agent can retrieve approved metrics, apply domain rules and invoke only authorized tools. Guard rails block out-of-scope actions, while audit evidence records the decision path.

**Example 3 — Specialized Foundry agent:** evidence shows that a scenario needs pro-code orchestration, multiple controlled tools or advanced evaluation beyond the simpler options. A Microsoft Foundry Agent Service workload can combine approved enterprise knowledge, governed analytical data and external tools. Entra identities and tool permissions are scoped to the workload, Purview controls are verified for each source, and evaluators measure quality and safety before release and continuously in production. Runtime blocking is added only where an explicit guard rail is required.

**Example 4 — Governance at scale:** departments can deploy a mix of SaaS capabilities, deterministic workflows, RAG solutions and agents for HR, finance and operations. Despite different implementation patterns, all follow common identity, access, data classification, observability, evaluation and capacity standards. New complexity is added only after measurable escalation triggers show that the current pattern is insufficient.

### 📚 Microsoft references

- [Microsoft AI strategy](https://learn.microsoft.com/azure/cloud-adoption-framework/ai/strategy)
- [Microsoft 365 Copilot](https://learn.microsoft.com/microsoft-365-copilot/)
- [Microsoft IQ](https://learn.microsoft.com/microsoft-iq/)
- [Microsoft Foundry Agent Service](https://learn.microsoft.com/azure/foundry/agents/overview)
- [Microsoft Fabric](https://learn.microsoft.com/fabric/)
- [Microsoft Entra managed identities](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview)
- [Microsoft Purview sensitivity labels](https://learn.microsoft.com/purview/sensitivity-labels)

Official references accessed July 20, 2026. Product availability, licensing, quotas and regional support must be revalidated during architecture approval.

---

> Content moved to [AI Architecture Fundamentals](../references/01-llm-rag-ai-agent-fundamentals.md) — LLM vs RAG vs AI Agent vs Agentic AI.

> Content moved to [Reference Architecture Layers](../references/02-reference-architecture-layers.md) — Microsoft IQ context workloads, agent runtimes and Microsoft Fabric.

> Content moved to [PL 2338/2023, Copilot Studio and Microsoft Foundry](../references/06-pl-2338-2023-copilot-studio-foundry.md) — analysis of transparency, governance, risk, audit and data-protection requirements with official sources.

