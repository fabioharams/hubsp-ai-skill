# AI Solution Project Specification - Example

This fictional example demonstrates the expected evidence level. It is not a product recommendation.

## 1. Business Outcome

- Problem and baseline: Support specialists spend 12 minutes locating approved return policies for each escalated case.
- Target: Reduce median research time by 30% without increasing incorrect-policy use.
- Owner: Customer Support Director.
- Users and channel: 40 specialists in the existing support application.
- Existing capability: The support platform has keyword search, but ranking and citations do not meet the measured baseline.

## 2. Functional Scope

- In scope: Retrieve approved policy passages and cite the source.
- Out of scope: Approving refunds, changing orders or contacting customers.
- Human accountability: The specialist remains responsible for the case decision.

## 3. Architecture Decision

| Option | Fit | Evidence |
|---|---|---|
| Existing SaaS search | Not fit | Representative test set misses the approved passage in 24% of cases. |
| Deterministic automation | Not fit | Policy questions are unstructured and cannot be represented by stable rules alone. |
| Direct LLM application | Not fit | The response must cite current approved policy. |
| RAG or built-in retrieval | Conditional fit | Meets the bounded read-only requirement; ranking, permissions and capacity require pilot validation. |
| Single AI Agent | Deferred | No multi-step reasoning or tool action is currently required. |
| Multi-agent or mixed architecture | Deferred | No independent runtime or specialist requirement exists. |

- Simplest viable baseline: Managed grounded retrieval embedded in the existing support experience.
- Escalation trigger: Consider a single agent only if a future requirement needs bounded multi-step tool use that retrieval cannot satisfy.

## 4. Data, Security and Controls

- Authority: Approved policy repository owned by Legal Operations.
- Identity: Signed-in specialist; effective source permissions must be tested end to end.
- Guard rails: Read-only scope, approved-domain allow-list and citation requirement.
- Evaluators: Retrieval relevance, groundedness, citation correctness and policy-version freshness.
- HITL: Specialist validates the cited policy before taking action.

## 5. Capacity and Reliability

| Component | Peak demand | Headroom | Verdict | Required validation |
|---|---|---|---|---|
| Retrieval service | Unknown concurrent queries during shift change | 30% | Conditional fit | Measure peak concurrency and run a representative load test. |
| Policy source | 15-minute freshness target | N/A | Conditional fit | Verify indexing schedule and deletion propagation. |
| Support application integration | 40 pilot users | 30% | Conditional fit | Validate authentication, timeout and fallback behavior. |

## 6. Evidence-Gated Roadmap

- Pilot: 10 specialists, read-only retrieval, representative policy set and predefined quality thresholds.
- Expansion: Add users only after permissions, quality, support load and capacity headroom are proven.
- Scale: Operate as a managed capability with monitoring, release gates, cost attribution and retirement criteria.

This internal roadmap maps to Microsoft's applicable planning, governance, security, build and management activities; it is not Microsoft's named lifecycle.
