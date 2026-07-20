# Capacity and Scale Assessment for Microsoft AI Solutions

Use this reference whenever a recommendation selects a Microsoft product, SaaS capability, license, SKU, model deployment or material downstream service. Capacity validation is a production gate, not a product-selection afterthought.

## Decision principle

The effective capacity of an AI solution is the **lowest sustainable limit in its end-to-end runtime path**. Commercial entitlement and technical throughput are separate:

- A license, Copilot credit allocation, prepaid capacity or pay-as-you-go billing permits consumption but does not guarantee the required request rate.
- A model quota does not prove that search, connectors, Power Automate, Dataverse, Fabric or a downstream API can sustain the same peak.
- Nominal daily or monthly volume does not expose bursts, concurrency, long-running requests or retry amplification.

Do not issue an unconditional production recommendation when workload demand, tenant entitlement, subscription quota, regional availability or downstream limits are unknown.

## 1. Build the demand envelope

Capture at least:

| Demand input | Required measure |
|---|---|
| Population and adoption | Eligible users, expected active users, adoption by wave and growth horizon |
| Traffic | Average and peak interactions per minute/hour, burst duration and seasonality |
| Concurrency | Peak concurrent users, jobs, conversations and autonomous runs |
| AI work per interaction | Model calls, tool calls, flow/API calls, input tokens and output tokens at p50/p95 |
| Data | Source size, document count, vector count/dimensions, index growth and ingestion/change rate |
| Service objective | p95/p99 latency, availability, recovery objective and geographic/data-residency needs |
| Safety margin | Explicit headroom percentage and retry/failure assumption |

Use measured p95 values from a representative pilot where possible. For an initial estimate:

$$
\text{Peak model RPM}=\text{Peak interactions/min}\times\text{Model calls/interaction}
$$

$$
\text{Peak TPM}=\text{Peak model RPM}\times(\text{p95 input tokens}+\text{p95 output tokens})
$$

$$
\text{Concurrent work}\approx\text{Requests/second}\times\text{p95 service time in seconds}
$$

Apply the documented headroom to each demand metric. State the chosen margin; do not present a universal percentage as a Microsoft requirement.

## 2. Check every limiting layer

| Product or layer | Capacity checks | Validation evidence |
|---|---|---|
| Microsoft 365 Copilot / SaaS | User eligibility and license coverage, feature/region availability, measured adoption and usage; separately assess any metered agents or connected services | Readiness report, license inventory, usage report and pilot evidence |
| Copilot Studio | Copilot credits/messages and overage model; messages RPM; generative RPM/RPH; autonomous trigger limits; Power Platform requests; Dataverse service protection; Power Automate, connector and downstream API throttles | Tenant/environment entitlement, current quotas, full-path throughput model and load test |
| Foundry Agent Service | Agent artifact limits, selected model/tool support by region and model, project/deployment constraints and model deployment quota | Region compatibility matrix, subscription quota and representative agent test |
| Azure OpenAI / Foundry Models | Deployment type, model/version availability, TPM and RPM quota scope, quota already allocated, context limits, provisioned throughput when justified and quota-increase lead time | Subscription-region-model quota, deployment configuration, token profile and load test |
| Azure AI Search / Foundry IQ retrieval dependency | Tier; index and vector size; partitions for storage/indexing; replicas for query throughput and SLA; Search Units; semantic ranker or serverless throttles; ingestion rate | Built representative index, measured query/index load, SLA topology and scale test |
| Microsoft Fabric / Fabric IQ data dependency | Workload mix, concurrent interactive/background operations, CUs, SKU, bursting/smoothing, throttling, workspace isolation and scale-up/scale-out path | SKU Estimator as initial input, trial or pay-as-you-go pilot, Capacity Metrics app and peak-period evidence |
| Integrations | Connector limits, API gateway policy, Dataverse/Graph/SharePoint limits, database connections, queues, functions and external SaaS/API quotas | Published limit plus owner-confirmed configuration and end-to-end load test |

For products without customer-configurable infrastructure sizing, validate entitlement, published service limits, feature availability and adoption fit. Do not invent a SKU or throughput guarantee.

## 3. Produce the fit matrix

Every selected component must have one row:

| Component | Peak demand + headroom | Entitlement / current limit and scope | Proposed configuration | Region | Bottleneck | Verdict | Evidence and validation | Monitor / scale trigger |
|---|---|---|---|---|---|---|---|---|
| Example | 120 model RPM; 180K TPM | Subscription-region-model quota: tenant check pending | Global Standard deployment | Required region pending | TPM quota | Conditional fit | Confirm quota, then test p95 workload | 429 rate; p95 latency; 70% sustained allocation |

Use these verdicts:

- **Fit**: measured peak plus declared headroom meets SLA within verified entitlement, quota and configuration; downstream dependencies also pass.
- **Conditional fit**: plausible, but a named demand assumption, entitlement/quota check, regional check or representative load test remains open. This cannot pass the production gate.
- **Not fit**: a hard limit, unavailable feature/region, unacceptable SLA/cost or rejected quota/capacity request prevents the requirement from being met.

## 4. Validate before production

1. Confirm licenses, credits and billing model with the tenant administrator.
2. Confirm actual quota and available capacity in the target subscription, region, model and environment. Published defaults are not proof of allocated quota.
3. Build a representative data/index sample and capture p50/p95 token, tool-call and latency profiles.
4. Load test the complete path at expected peak plus declared headroom, including authentication, retrieval, orchestration, flows, connectors and downstream APIs.
5. Test throttling, retries with jitter, back-pressure, queueing, timeout, graceful degradation and failover behavior.
6. Record cost per completed task and peak-period infrastructure/consumption cost.
7. Define monitoring thresholds, owner, lead time and action for optimize, scale up, scale out, quota increase or workload isolation.
8. Reassess after each adoption wave or material model, prompt, tool, data or workload change.

## Official Microsoft sources

Accessed 2026-07-20. Recheck current values before each production decision.

- Copilot Studio throughput planning: https://learn.microsoft.com/microsoft-copilot-studio/guidance/plan-agent-throughput-rate-limits
- Copilot Studio quotas and limits: https://learn.microsoft.com/microsoft-copilot-studio/requirements-quotas
- Copilot Studio licensing and billing: https://learn.microsoft.com/microsoft-copilot-studio/billing-licensing
- Microsoft 365 Copilot readiness report: https://learn.microsoft.com/microsoft-365/admin/activity-reports/microsoft-365-copilot-readiness
- Microsoft 365 Copilot usage report: https://learn.microsoft.com/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage
- Foundry Agent Service limits, quotas and regions: https://learn.microsoft.com/azure/foundry/agents/concepts/limits-quotas-regions
- Azure OpenAI quotas and limits: https://learn.microsoft.com/azure/foundry/openai/quotas-limits
- Azure OpenAI provisioned throughput: https://learn.microsoft.com/azure/foundry/openai/concepts/provisioned-throughput
- Azure AI Search capacity planning: https://learn.microsoft.com/azure/search/search-capacity-planning
- Azure AI Search service limits: https://learn.microsoft.com/azure/search/search-limits-quotas-capacity
- Microsoft Fabric capacity planning: https://learn.microsoft.com/fabric/enterprise/plan-capacity
- Microsoft Fabric capacity planning overview: https://learn.microsoft.com/fabric/enterprise/capacity-planning-overview
- Microsoft Fabric throttling: https://learn.microsoft.com/fabric/enterprise/throttling
- Azure Pricing Calculator: https://azure.microsoft.com/pricing/calculator/