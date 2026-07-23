# Business Envisioning and Technical Questionnaire for Microsoft AI Architecture Recommendations

## Purpose

Use this questionnaire to turn a business idea into a prioritised, architecture-ready use case without selecting a technology in advance. It consolidates the Microsoft Innovation Hub business-envisioning use-case, value, BXT feasibility, prioritisation and next-step prompts with the technical evidence needed for an architecture recommendation.

The skill evaluates options in order: existing Microsoft/SaaS capability, deterministic automation, direct LLM, RAG, single AI Agent, then multi-agent or mixed architecture. Complete one copy per use case when several use cases need to be compared. Capture less-developed ideas in the parking lot rather than forcing unsupported scores.

Use current facts where possible. Enter **Unknown** instead of guessing, and name an owner who can validate it. Unknowns that affect security, capacity, reliability or feasibility remain pre-production validation gates.

Complete this file directly or copy its questions into another document. The skill also accepts an existing proposal, discovery note, requirements document, workshop summary or technical specification when it contains equivalent business and technical facts. The attached document does not need to preserve this questionnaire's headings or question order.

## Fast Completion Guide

- Use short answers. One or two sentences, values or links to existing evidence are enough.
- Complete Part A first in a business-envisioning workshop. It is enough to compare use cases and produce an initial, conditional recommendation.
- Complete only the Part B answers already known. Do not delay the initial review to research every technical detail.
- Write **Unknown - owner: name or team** when an answer is unavailable. The skill will ask only for missing information that could change the decision.
- Describe the need and current facts. Do not choose an architecture or Microsoft product unless it is an existing constraint.
- Use a 1-5 scale for value and feasibility only after participants agree on the evidence and scoring method.

## Part A: Core Business Intake

Complete these 15 consolidated questions for business-envisioning outputs and an initial architecture recommendation. Each question includes a plain-language explanation and an example. Adapt the examples to your organisation; do not treat them as expected answers.

1. **Use case, problem and idea:** What should we call this use case? What problem or opportunity does it address, how is the work done today and what is the proposed idea?
	- **What this means:** Describe the situation before describing technology. Show where people lose time, repeat work, make errors or wait for another team. Also explain what happens if nothing changes.
	- **Example:** "Supplier Invoice Review. Five analysts manually copy invoice data from email attachments into the finance system. Reviews take three days, duplicate entries occur and late payment fees are increasing. The idea is to extract the information, flag exceptions and prepare entries for analyst approval."

2. **Objective, urgency and strategic fit:** What business outcome should this use case achieve, why is it important now and how does it support the organisation's strategy or roadmap?
	- **What this means:** Connect the use case to an agreed business priority, not only to a local inconvenience. Explain any deadline, market change, customer commitment or regulatory event creating urgency.
	- **Example:** "Reduce invoice-processing time to support the company-wide working-capital programme before the new regional shared-service centre opens in Q2."

3. **Key results and evidence:** Which three to five measurable results will prove that the objective is being achieved?
	- **What this means:** For each result, state how it is calculated, the value today, the desired value, the deadline and who can validate the data. A result should show an outcome, not merely that a solution was launched.
	- **Example:** "Average processing time: 3 days today, 8 hours by 30 June; measured from received timestamp to approved timestamp in the finance system; evidence owner: Accounts Payable Operations."

4. **Business value and time to value:** What financial or operational value will the use case create, and how soon can that value begin?
	- **What this means:** Estimate additional revenue, avoided cost, saved effort, faster service or improved customer and employee outcomes. A useful effort calculation is number of people x minutes per task x number of tasks. Include human-review effort, available budget and the minimum benefit needed to justify continuation.
	- **Example:** "The analyst team processes 4,000 invoices per month at 12 minutes per invoice. That equals 800 hours per month, or 9,600 hours per year. Reducing manual effort by 50% would release about 4,800 hours annually, with benefits expected within six months."

5. **Personas, appeal and adoption:** Who benefits, how many people will use the solution and why would they prefer it to their current alternative?
	- **What this means:** Name the main user groups and what each one needs. Describe rollout size, likely resistance, accessibility or training needs and how long the change may take. A technically sound solution has little value if users avoid it.
	- **Example:** "The first users are 20 invoice analysts, followed by 150 budget owners. Analysts will adopt it if exception review is faster than entering invoices manually. They need training, keyboard-accessible screens and clear reasons for every flagged item."

6. **Process, rules and judgement:** Which parts of the work follow clear rules, and which parts require context, empathy or human judgement?
	- **What this means:** Separate repeatable decisions from ambiguous or high-consequence decisions. State which exceptions must remain with a person because the answer depends on experience, policy interpretation or the circumstances of an individual case.
	- **Example:** "Matching an invoice to an approved purchase order follows fixed rules. Deciding whether to pay an unusual invoice without a purchase order requires an analyst and manager approval."

7. **Experience and channels:** What is the simplest useful experience, and where should users access it?
	- **What this means:** Choose the experience that best fits the work: form, search, dashboard, notification, workflow or conversation. Clarify whether the user needs a single result, an ongoing dialogue or help completing several steps, and whether this happens in Teams, Microsoft 365 Copilot, web, email, an existing application or an API.
	- **Example:** "Analysts need an exception queue inside the existing finance application, with a Teams notification when an urgent invoice needs approval. They do not need a general-purpose chatbot."

8. **Existing capability and technology fit:** What products, automations, processes, data or tools already support this use case, and what gap remains?
	- **What this means:** Check whether an existing licensed product, configuration or rules-based automation can meet the need before adding AI. Note similar implementations that can be reused and explain the specific extra value expected from generative AI.
	- **Example:** "Power Automate already saves attachments to SharePoint, and the finance platform already detects duplicate invoice numbers. The remaining gap is extracting inconsistent line-item descriptions and explaining exceptions to analysts."

9. **Knowledge, data and permissions:** What trusted information is needed, where is it stored and who is allowed to see it?
	- **What this means:** List the authoritative sources, their format and quality, how often they change and whether outputs must show citations. Identify personal, confidential, regulated or intellectual-property data and explain whether access differs by role, region or legal entity.
	- **Example:** "The solution needs invoices from SharePoint, purchase orders from SAP and the current payment policy from the policy portal. European analysts may view only their legal entity's invoices, and every policy recommendation must cite the relevant policy section."

10. **Answers, actions and approvals:** What may the solution do, and which actions require a person to approve or take over?
	- **What this means:** Distinguish low-risk assistance, such as searching or drafting, from actions that change a business system. Identify read and write actions, irreversible steps and financial, legal or customer-facing decisions that need approval.
	- **Example:** "The solution may read invoices, draft an accounting entry and recommend a payment code. It may not post the entry or release payment until an analyst approves it; payments above $50,000 also require manager approval."

11. **Decision flow and ownership boundaries:** Can one predictable workflow complete the task, or must the solution decide between different tools, processes or specialist responsibilities?
	- **What this means:** Describe how the work moves from start to finish and who owns each decision. Do not assume multiple agents are needed because several teams participate. Separate components are justified only when independent domains, controls or operating owners cannot be handled reliably in one bounded workflow.
	- **Example:** "One Accounts Payable workflow can extract, validate and route standard invoices. Tax disputes are transferred to the Tax team and are outside the pilot; there is no evidence yet that a separate AI agent is required."

12. **Business risk, safeguards and compliance:** What could happen if the solution gives a wrong, unsafe or biased answer or performs the wrong action?
	- **What this means:** Describe the business impact and the responsible AI, security, privacy, legal, regulatory and intellectual-property rules that apply. State what must be blocked, approved, logged, reviewed or capable of being shut down.
	- **Example:** "A wrong bank-account update could cause fraud and financial loss. The solution must never change supplier banking details, must log every recommendation and must allow Finance Security to disable all write actions immediately."

13. **Demand and service expectations:** How much will the solution be used, and what level of service does the business need?
	- **What this means:** Estimate normal and busiest-period volumes, simultaneous users or jobs and growth over the next 12 to 24 months. Include acceptable response time, hours of operation, regions served and what the business does if the solution is unavailable.
	- **Example:** "The service will process about 4,000 invoices per month, peaking at 800 during the final two business days. Up to 30 reviews may run at once. Results should be ready within two minutes; during an outage, analysts use the current manual process."

14. **BXT feasibility and delivery risk:** How feasible is the use case from the Business, eXperience and Technology perspectives?
	- **What this means:** Business viability asks whether sponsorship, funding, value and ownership are credible. Experience viability asks whether users need and will adopt the change. Technical viability asks whether the data, integrations, skills, accuracy and operational support are realistic. Identify dependencies, risks and a credible delivery timeframe.
	- **Example:** "Business feasibility is high because the CFO sponsors the outcome and the baseline is measured. Experience feasibility is medium because analysts need workflow training. Technical feasibility is medium because invoice formats vary and the SAP test interface is available only from September."

15. **Pilot, accountability and next step:** What is the smallest useful pilot, who is accountable and what happens next?
	- **What this means:** Limit the pilot to a scope that can test the main value and risk assumptions quickly. Set an end date and measurable continue, change or stop criteria. Name the stakeholder accountable for the key results and the owners of business process, data, approvals and ongoing operations. Record the first action, its owner and due date.
	- **Example:** "Run an eight-week pilot for PDF invoices from the top 20 suppliers. Continue if extraction accuracy is at least 95%, processing time falls by 40% and no unauthorised posting occurs. The VP of Finance owns the outcome; the Accounts Payable lead owns the next step of supplying 500 test invoices by 15 March."

### Business Measures

| Measure | Current baseline | Target | Deadline | Evidence owner |
|---|---:|---:|---|---|
|  |  |  |  |  |

### Use-Case Prioritisation Summary

Agree the scoring method before assigning scores. Value normally reflects business viability. Feasibility normally reflects the average of experience and technical viability.

| Use case | Value (1-5) | Business viability (1-5) | Experience viability (1-5) | Technical viability (1-5) | Feasibility (1-5) | Evidence or assumptions | Decision (Invest/Quick win/Test and learn/Park) |
|---|---:|---:|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |  |

## Part B: Compact Technical Validation

A solution architect or the relevant platform, security, data and application owners can complete these questions. Each question includes a plain-language explanation and an example. Use exact values and links to evidence when available. If an answer is not yet known, enter **Unknown - owner: name or team** rather than guessing.

16. **Technical scope and standards:** Which parts of the organisation and technology estate are included in this use case?
	- **What this means:** Identify the Microsoft Entra tenants, Azure subscriptions, Power Platform or Fabric tenants, development and production environments, deployment regions and architecture standards that apply. List relevant Microsoft 365, Power Platform, Fabric, Foundry and Azure resources. Clarify what an internal team, Microsoft or a delivery partner will own.
	- **Example:** "The pilot uses the Contoso corporate Entra tenant, the Finance Power Platform environment and the non-production Azure subscription in West Europe. Production must follow the enterprise landing-zone and naming standards. The implementation partner builds the integration, while Contoso owns production operations."

17. **Approved services and reuse:** Which existing, approved services, licences and patterns can the solution reuse?
	- **What this means:** Check what the organisation already owns and permits before proposing new services. Include Microsoft 365, Copilot Studio, Power Platform, Fabric, Foundry, Azure, integration and monitoring capabilities. Record licence limits, approved reference architectures, existing implementations and the team responsible for each service.
	- **Example:** "Power Automate premium connectors, Azure AI Document Intelligence and Application Insights are approved and available. An existing SAP integration pattern can be reused. Copilot Studio licences cover only the 20 pilot users; the Platform team must confirm production licensing."

18. **Identity and access:** Who starts the solution, and whose permissions should it use when accessing another system?
	- **What this means:** State whether a person, scheduled job, event or another application starts the process. For each downstream system, decide whether the solution acts with the signed-in user's permissions or with its own application identity. List Microsoft Entra identities, roles, Conditional Access requirements and any cross-tenant or legal-entity restrictions.
	- **Example:** "An invoice arriving in the shared mailbox starts the process. The extraction service uses a managed identity with read access to the invoice library. Analysts see invoices through their own Entra identity, and SAP updates use a separate application identity limited to creating draft entries for the analyst's legal entity."

19. **Data-source readiness:** Is each required data source accessible, trustworthy and suitable for the solution?
	- **What this means:** For every source, identify its owner, access method, file or data format, approximate volume, quality and required freshness. Note missing values, duplicates or inconsistent formats. State whether the data may be copied, indexed or retained and where it is legally permitted to reside.
	- **Example:** "SharePoint contains about 1.2 million PDF invoices and receives 4,000 more each month. Accounts Payable owns the library. Most documents are readable, but approximately 8% are scans. Invoices may be processed in the EU but may not be retained in a separate search index after the seven-year finance retention period."

20. **Search, grounding and retrieval:** What trusted information must the solution find and use to support its answers?
	- **What this means:** Grounding means giving the AI relevant, authoritative information instead of relying only on what the model learned previously. Describe what users search for, which sources are authoritative and whether answers need citations. State whether search must respect each user's source permissions and support exact words, meaning-based search, filters, multiple languages, semantic models, Microsoft IQ context capabilities or another governed knowledge base.
	- **Example:** "When explaining a payment exception, the solution must retrieve the current finance policy and cite its section number. It must combine exact supplier-ID matching with meaning-based policy search, filter by legal entity and return only documents the analyst is already permitted to view."

21. **Integrations and action contracts:** Which systems must exchange information with the solution, and exactly what may each integration do?
	- **What this means:** List APIs, connectors, MCP servers, Power Automate flows, events, databases and business applications. For each integration, define whether it can read or write, whether the user waits for an immediate response or the work continues in the background, whether an action can be reversed, who approves sensitive actions and who owns the interface.
	- **Example:** "The SharePoint connector reads invoice files. The SAP API creates draft accounting entries synchronously but cannot post payments. A Service Bus queue sends approved items for background processing. Finance Integration owns the SAP API, and an analyst must approve every draft before posting."

22. **Integration limits and recovery:** What happens when a connected system is busy, slow, unavailable or receives the same request twice?
	- **What this means:** Record how each integration authenticates and its request, concurrency and timeout limits. Define retries, queues and recovery steps. Idempotency means that repeating the same request does not create a second invoice or payment. Include known restrictions in test environments so that testing reflects production behavior.
	- **Example:** "The SAP test API allows 10 requests per second and times out after 30 seconds. Failed draft requests are retried three times and then moved to a review queue. The invoice ID is the idempotency key, so a retry cannot create a duplicate draft. The test environment is unavailable on Sundays."

23. **AI tasks, accuracy and acceptance tests:** Which tasks actually need AI, and how will the team prove they work well enough?
	- **What this means:** Identify tasks such as generating text, extracting fields, classifying documents, retrieving knowledge, planning steps, using tools or processing images and audio. Provide realistic examples for normal cases, unusual cases, malicious inputs and high-risk situations. Define measurable quality thresholds and cases that must always be sent to a person.
	- **Example:** "The solution extracts supplier, invoice number, date, currency and line items from PDFs. Testing uses 500 representative invoices, including scans, handwritten notes, duplicate pages, prompt-injection text and invoices above $50,000. Required field accuracy is at least 95%, and every low-confidence or high-value case goes to an analyst."

24. **State, memory and long-running work:** What information must the solution remember, and for how long?
	- **What this means:** Determine whether the solution needs only the current request or must remember earlier interactions, wait for events, continue work in the background or pause for human approval. For everything retained, state its source, purpose, user or case scope, who can see it, the privacy basis and when it is deleted. Do not treat conversation history as permanent memory by default.
	- **Example:** "The workflow retains the invoice ID, extraction result, validation status and approval history for each case. It waits up to five business days for analyst approval. Analysts can see only cases for their legal entity. Temporary model prompts are deleted after 30 days; the final audit record follows the seven-year finance policy."

25. **Hosting, network and environments:** Where will the solution run, and how will it connect securely to required systems?
	- **What this means:** Name the runtime or hosting service explicitly; a development framework alone is not a hosting choice. Describe private endpoints, virtual networks, on-premises connections, controlled internet access, API gateways and data-residency requirements. Define separate development, test and production environments and whether another region is needed for recovery.
	- **Example:** "The API runs in Azure Container Apps in West Europe. It reaches on-premises SAP through ExpressRoute and uses private endpoints for Storage and Azure AI services. Azure API Management controls inbound APIs. Development, test and production are separate, and North Europe is the production recovery region."

26. **Capacity, licences and quotas:** Can the selected services handle the busiest period, and are enough licences and service quotas available?
	- **What this means:** Estimate or measure peak requests, concurrent jobs, tokens and model or tool calls per interaction. Verify licences, credits and quotas rather than assuming availability. Include Fabric Capacity Units, Azure AI Search Units, model throughput and downstream-system limits by tenant, subscription, region and model when relevant.
	- **Example:** "Month-end demand is 800 invoices over two days, with 30 concurrent jobs. Each invoice is expected to make one extraction call, two model calls and one SAP call. The Azure subscription has sufficient Document Intelligence quota, but the Foundry model deployment quota in West Europe is still unknown; owner: AI Platform team."

27. **Reliability and reduced service:** How available must the solution be, how much data or time may be lost and what happens during a failure?
	- **What this means:** Availability is the percentage of time the service must work. RTO is the maximum acceptable time to restore the service. RPO is the maximum acceptable amount of recent data loss. Define peak-load testing, spare capacity, timeouts, fallback behavior, manual recovery and the evidence required before production.
	- **Example:** "The service target is 99.5% during finance operating hours. RTO is four hours and RPO is 15 minutes. If AI extraction is unavailable, invoices remain in the queue and analysts can use the manual process. Production approval requires a test at 1.5 times expected month-end load."

28. **Security and guard rails:** What controls will prevent unauthorised access, unsafe instructions, excessive actions or data leakage?
	- **What this means:** Apply least privilege so every person and service has only the access it needs. Describe secret storage, encryption, content controls, prompt and tool-input validation, log redaction, human approvals and audit records. Define how operations can quickly disable a model, tool or all write actions during an incident.
	- **Example:** "Managed identities replace stored passwords, and secrets are held in Key Vault. Invoice text is treated as untrusted input and cannot change system instructions. Logs mask bank and tax identifiers. SAP posting always requires human approval, and Finance Security can disable the SAP tool through a central configuration switch."

29. **Observability, evaluators and operations:** How will the team know whether the solution is useful, accurate, safe, healthy and affordable?
	- **What this means:** Observability includes logs, metrics and traces that show what happened across models and tools. Evaluators are repeatable tests or measures for answer quality and safety. Define business key results, quality and safety thresholds, model and tool traces, cost and capacity alerts, support owners, operational runbooks and incident-response procedures.
	- **Example:** "The dashboard tracks processing time, extraction accuracy, analyst override rate, unauthorised-action attempts, failed SAP calls and cost per invoice. Alerts fire if field accuracy falls below 95%, the failure rate exceeds 2% or daily cost exceeds the agreed threshold. Finance Technology owns support and the month-end incident runbook."

30. **Delivery lifecycle, rollback and handoff:** How will every solution component be tested, approved, released, operated and reversed if necessary?
	- **What this means:** Cover code, prompts, models, tools, knowledge sources, policies and infrastructure. Explain version control, development-to-production promotion, automated and human tests, release approval and rollback. Name the ongoing operator and ensure each next-step owner accepts the action and due date in writing.
	- **Example:** "Code, prompts and infrastructure are versioned in Git. Changes deploy to development, then test, where the 500-invoice evaluation set and security tests must pass before Finance and Security approve production. The previous application and prompt versions remain deployable for rollback. Finance Technology accepts production support, and each handoff action is confirmed by email."

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

### Parking Lot

Use this for ideas that lack enough evidence for scoring or dedicated analysis.

| Use case | Description | Evidence of value | Evidence of feasibility | Missing information | Owner to advance |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Agreed Next Steps

An action is agreed only when its owner confirms the scope and due date.

| Use case | Next step | Owner | Due date | Acceptance evidence | Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

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