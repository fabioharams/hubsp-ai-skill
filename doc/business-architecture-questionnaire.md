# Business and Technical Questionnaire for Microsoft AI Architecture Recommendations

## Purpose

Use this questionnaire to describe the need without selecting a technology in advance. The skill evaluates options in order: existing Microsoft/SaaS capability, deterministic automation, direct LLM, RAG, single AI Agent, then multi-agent or mixed architecture.

Use current facts where possible. Enter **Unknown** instead of guessing, and name an owner who can validate it. Unknowns that affect security, capacity, reliability or feasibility remain pre-production validation gates.

Complete this file directly or copy its questions into another document. The skill also accepts an existing proposal, discovery note, requirements document, workshop summary or technical specification when it contains equivalent business and technical facts. The attached document does not need to preserve this questionnaire's headings or question order.

## Fast Completion Guide

- Use short answers. One or two sentences, values or links to existing evidence are enough.
- Complete Part A first. It is enough for an initial, conditional recommendation.
- Complete only the Part B answers already known. Do not delay the initial review to research every technical detail.
- Write **Unknown - owner: name or team** when an answer is unavailable. The skill will ask only for missing information that could change the decision.
- Describe the need and current facts. Do not choose an architecture or Microsoft product unless it is an existing constraint.

## Part A: Core Business Intake

Complete these 15 questions for an initial architecture recommendation.

1. **Problem and urgency:** What problem needs to be solved? Who is affected, and why does it matter now?
2. **Expected results:** What one to three measurable results should improve? Give the current value, target value and target date when known.
3. **Current process:** How is the work done today? Identify the main delays, errors, repeated work or failed handoffs.
4. **Existing tools:** Which Microsoft or other software products and automations are already licensed or used? Explain what they cannot do today.
5. **Rules and judgment:** Which steps follow clear, stable rules? Which steps need human judgment or exception handling?
6. **Users and channels:** Who will use the solution, and how many users are expected at each rollout stage? State where they should use it, such as Microsoft 365 Copilot, Teams, web, a business application, email or API.
7. **User experience:** What is the simplest useful experience: a form, search, dashboard, notification, workflow or conversation? State whether users need one answer, a dialogue or a multi-step task.
8. **Knowledge and data:** Which trusted information sources are needed, and where are they stored? State how often they change and whether answers must cite their sources.
9. **Sensitive data:** What personal, confidential or regulated data is involved? State whether access changes by user, role, region or legal entity.
10. **Answers and actions:** Should the solution only answer or draft content, or should it also read or update systems? Identify actions that are high impact, cannot be reversed or require human approval.
11. **Decision flow:** Can fixed rules define every step, or must the solution choose a tool or decide what to do next? Explain whether one workflow and one owner can reliably cover the full task.
12. **Risk and compliance:** What could happen if an answer or action is wrong? List applicable policies or regulations and anything that must be logged, reviewed or blocked.
13. **Demand and service:** How much usage is expected on an average day and during the busiest period? Include simultaneous users or jobs, required response time and availability, operating regions and expected growth over 12 to 24 months.
14. **Costs and value:** How many tasks occur each month, and how long does each take today? Include the full hourly labor cost, expected percentage needing human review, available budget and minimum benefit required to continue.
15. **Pilot and ownership:** What is the smallest useful pilot, when must it finish and what results would make it successful? Name the owners for the business outcome, data, approvals and ongoing operation.

### Business Measures

| Measure | Current baseline | Target | Deadline | Evidence owner |
|---|---:|---:|---|---|
|  |  |  |  |  |

## Part B: Compact Technical Validation

A solution architect or the relevant platform, security, data and application owners can complete these questions. Plain-language answers are acceptable. Use exact values and links to evidence when available; otherwise enter **Unknown** for an initial conditional recommendation.

1. **Technical scope:** Which tenants, subscriptions, environments, regions and architecture standards are in scope? List relevant Power Platform, Fabric, Foundry and Azure resources.
2. **Services already available:** Which approved Microsoft 365, Copilot Studio, Power Platform, Fabric, Foundry, Azure, integration and monitoring services can be reused?
3. **Identity and access:** Who or what starts the solution? State whether downstream systems must act as the user, and list the required Entra identities, permissions, Conditional Access or cross-tenant rules.
4. **Data sources:** For each source, provide its owner, interface, format, approximate size and required freshness. Include access rules and any restrictions on copying or indexing the data.
5. **Search and retrieval:** What must the solution find and cite? State whether it must preserve source permissions or support vector or hybrid search, filters, multiple languages, semantic models or knowledge bases.
6. **Integrations:** Which APIs, connectors, MCP servers, flows, events, databases or applications must be used? For each, state whether access is read or write, immediate or asynchronous, and who owns it.
7. **Integration limits:** How do integrations authenticate and handle high traffic, timeouts, failures and duplicate requests? Include known rate or concurrency limits, retry or queueing rules, recovery steps and test-environment constraints.
8. **AI tasks and tests:** Which tasks need generation, extraction, classification, retrieval, planning, tool use, structured output or images and audio? Provide representative examples that can be used as tests.
9. **State and long-running work:** Must the solution remember information, wait for events, run in the background or request human approval? State what must be retained, for whom and for how long.
10. **Network and environments:** Which network or hosting controls are required? Include private endpoints, VNet or on-premises connectivity, controlled internet access, API gateway, data residency, separate environments and multi-region recovery.
11. **Capacity and limits:** What are the estimated or measured busiest-period requests, simultaneous work, tokens and model or tool calls per interaction? List verified licenses, credits, quotas, Fabric Capacity Units, Search Units and downstream limits by tenant, subscription, region and model.
12. **Reliability:** What availability and recovery targets are required, including RTO and RPO when known? Define the peak-load test, safety margin and reduced-service behavior required before production.
13. **Security controls:** How will the solution protect secrets and data from unsafe prompts, tool inputs or leakage? Include encryption, log redaction and emergency shutdown.
14. **Monitoring and evaluation:** What must be measured, logged and alerted on? Include business KPIs, traces, quality and safety evaluators, cost and capacity thresholds, support owners and runbooks.
15. **Delivery and rollback:** How will code, prompts, models, tools, knowledge, policies and infrastructure move through development, test and production? Explain versioning, approval, testing and rollback.

### Technical Decision Summary

| Area | Requirement or current state | Evidence | Owner | Status (Known/Unknown/Blocked) |
|---|---|---|---|---|
| Identity and access |  |  |  |  |
| Data and retrieval |  |  |  |  |
| Integrations and actions |  |  |  |  |
| Runtime and network |  |  |  |  |
| Capacity and reliability |  |  |  |  |
| Security and operations |  |  |  |  |
| Delivery lifecycle |  |  |  |  |

## Universal Architecture Recommendation Prompt

Attach the completed questionnaire or any document that describes the business and technical scenario, then use:

> Apply hubsp-ai-skill to the attached scenario document. Recommend the simplest viable Microsoft architecture and save the complete recommendation to `doc/recommendation-output.md`. Treat missing decision-critical information as explicit assumptions or validation gates; do not invent facts.

When the skill is referenced as a file instead of installed, attach `SKILL.md` as well. The skill contains the architecture ladder, output structure, capacity assessment, governance, ROI/AAI, roadmap, KPI, risk and Microsoft-source requirements, so these rules do not need to be repeated in the prompt.

## Interpretation Guide

| Observed requirement | Lowest option evaluated first |
|---|---|
| Existing product satisfies the journey with configuration | Existing Microsoft/SaaS capability |
| Stable rules, structured inputs and predictable actions | Deterministic workflow or Power Automate |
| One-step generation without proprietary grounding | Direct LLM |
| Authoritative changing knowledge and citations, without autonomous action | RAG |
| Bounded multi-step tool use or actions in one domain | Single AI Agent |
| Evidence proves independent domain/runtime responsibilities cannot be met by one agent | Multi-agent or mixed architecture |

This guide is not an automatic score. Risk, capacity, data readiness, cost and missing evidence can keep the recommendation at a simpler pilot or make it conditional.