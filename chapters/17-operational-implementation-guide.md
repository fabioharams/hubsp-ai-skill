## 🧪 19. Operational Implementation Guide (90 days)

### 🎯 Objective

Transform the architectural framework into practical execution, with delivery cadence, quality criteria, operational governance and continuous improvement process.

### 📆 90-day plan (executable)

| Window | Focus | Minimum deliverables |
|---|---|---|
| **Days 0-30** | Technical foundation and governance | 1) prioritized backlog of 2-3 agents, 2) baseline instructions per agent, 3) initial skills catalogue, 4) evaluation dataset (normal + edge cases), 5) telemetry enabled |
| **Days 31-60** | Controlled validation | 1) pilot with real users, 2) batch quality and security evaluators, 3) active guardrails by risk, 4) incident runbook tested in tabletop |
| **Days 61-90** | Production with gates | 1) deploy with go-live checklist, 2) continuous monitoring, 3) biweekly instructions/skills tuning routine, 4) cost and reliability baseline |

### 🚦 Quality gates for production

Use objective gates to reduce approval subjectivity. Values below are initial references and should be calibrated by domain:

| Dimension | Suggested metric | Recommended initial gate |
|---|---|---|
| **Task adherence** | Task adherence | **>= 0.85** |
| **Grounding** | Groundedness (responses with evidence) | **>= 0.85** |
| **Semantic quality** | Coherence/Relevance | **>= 0.80** |
| **Action execution** | Tool call accuracy | **>= 0.90** for critical skills |
| **Security** | Safety/policy violations | **0 critical incidents** in validation batch |
| **Operation** | Safe fallback rate | Stable and explainable trend by scenario |

### ✅ Go-live checklist (production)

1. Instructions reviewed by business, security and operations.
2. Skills classified by risk: read, write, critical integration.
3. Human approval enabled for critical/irreversible actions.
4. Guardrails active for prompt injection, content and exfiltration.
5. Evaluators configured in pre-production and post-production.
6. Logs and tracing enabled (input, decision, tool call, output).
7. Agent owner defined and operational SLA agreed.
8. Rollback plan documented and tested.

### 🚨 Minimum incident runbook

| Severity | Example | Immediate action | Target time |
|---|---|---|---|
| **SEV-1** | Unintended action with financial/compliance impact | Disable skill/agent, block route, notify security and business | within 15 min |
| **SEV-2** | Recurring incorrect response without critical damage | Force fallback, reduce agent scope, open instructions correction | within 4 h |
| **SEV-3** | Point-in-time quality drop | Monitor, record, correct in next release cycle | within 2 days |

Standard steps for any incident:
1. Contain: interrupt the highest-risk capability.
2. Preserve evidence: logs, prompts, tool calls, context.
3. Diagnose cause: instructions, skill, data, policy or model.
4. Correct and revalidate: run evaluation suite before reopening.
5. Record lessons learned and update controls.

### 🔁 Versioning pattern (Instructions + Skills)

Adopt explicit versioning per agent:
- **Instructions**: `major.minor.patch` (e.g., policy change = major).
- **Skills**: version input/output contract and permissions.
- **Risk catalogue**: maintain skill -> risk -> control -> owner map.

Change criteria:
1. **Patch**: textual adjustment without expected behavior change.
2. **Minor**: addition of a non-critical new skill or new scenario covered.
3. **Major**: change of policy, scope or critical actions.

### ⚙️ CI/CD pattern for agents

Recommended pipeline:
1. **PR check**: instruction lint + skills schema validation.
2. **Eval batch**: automatic suite (quality, groundedness, security).
3. **Policy gate**: block merge if critical violation found.
4. **Progressive deploy**: canary by user group.
5. **Post-deploy eval**: monitor degradation and automatic rollback by trigger.

### 📌 Suggested operational cadence

1. **Daily**: monitor incidents, fallback and cost per agent.
2. **Weekly**: review top failures and adjust instructions/skills.
3. **Biweekly**: review quality metrics by domain.
4. **Monthly**: governance committee for risk, ROI and prioritization.

### ✅ Expected outcome after 90 days

1. Agents in production with risk control and measured quality.
2. Repeatable evolution process (not dependent on ad hoc effort).
3. Less response variability and higher operational confidence.
4. Foundation ready to scale new agents with consistent governance.

---

