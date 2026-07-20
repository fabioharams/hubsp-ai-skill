# AI Solution Project Specification

Use this template after discovery or when requirements are already formalized. Record facts and constraints without selecting technology in advance. Use **Unknown** for unresolved items and assign a validation owner.

## 1. Business Outcome

- Problem and current baseline:
- Target outcome and KPI:
- Business owner and decision owner:
- Users, channels and rollout scope:
- Current process and existing Microsoft/SaaS capabilities:

## 2. Functional Scope

- In scope:
- Out of scope:
- Required inputs and outputs:
- Required actions and autonomy:
- Human approval and escalation points:
- Deterministic rules or workflows already available:

## 3. Architecture Decision

Evaluate in order and stop at the first option that reliably meets current requirements.

| Option | Fit | Unmet requirement or rejection evidence |
|---|---|---|
| Existing Microsoft/SaaS capability | Unknown | |
| Deterministic automation or API workflow | Unknown | |
| Direct LLM application | Unknown | |
| RAG or built-in grounded retrieval | Unknown | |
| Single AI Agent | Unknown | |
| Multi-agent or mixed architecture | Unknown | |

- Simplest viable baseline:
- Selected target architecture:
- Deferred capabilities:
- Measurable escalation triggers:
- Cost, latency, risk and complexity trade-offs:

## 4. Experience, Context and Runtime

- Experience or channel:
- Required context capabilities: Work IQ / Foundry IQ / Fabric IQ / Web IQ / other:
- Managed agent platform, if required: Foundry Agent Service / Copilot Studio / none:
- Microsoft Agent Framework, if required:
- Hosting, scaling and operations choice for framework applications:
- Model and deployment type:
- Data platform and authoritative sources:

## 5. Data and Integrations

| Domain or integration | Authority | Access path | Identity | Freshness | Classification | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

- Data residency and movement constraints:
- RLS, CLS, ACL or result-filtering requirements:
- Tool/API contracts, retries, idempotency and rollback:

## 6. Security, Governance and Responsible AI

- Applicable regulations and policies:
- Entra identities, RBAC and least privilege:
- Purview classification, DLP, retention and audit:
- Guard rails and blocked actions:
- Evaluators and release thresholds:
- HITL rules and accountable decision owners:
- Incident response and rollback:

## 7. Capacity, Reliability and Cost

| Component or dependency | Peak demand | Limit and scope | Headroom | License/SKU/configuration | Region | Bottleneck | Verdict | Validation and scale action | Official source and access date |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | Conditional fit | | |

Use only **Fit**, **Conditional fit** or **Not fit**. Unknown demand, entitlement, quota, regional availability or downstream capacity remains a pre-production gate.

- Availability and recovery objectives:
- Degraded behavior and fallback:
- Cost per successful task and budget owner:
- Production-like load-test plan:

## 8. Delivery and Operations

| Wave | Objective | Entry criteria | Exit criteria | KPI | Dominant risk | Owner |
|---|---|---|---|---|---|---|
| Pilot | | | | | | |
| Expansion | | | | | | |
| Scale | | | | | | |

Map these internal waves to the applicable Microsoft AI or agent-adoption lifecycle. Governance and security apply throughout every wave.

- Observability, traces, metrics and alerts:
- Change and release process:
- Support model and service ownership:
- Open assumptions and validation owners:
