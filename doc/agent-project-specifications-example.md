# AI Agent Project Specifications — harafaz.ia

> **Note:** document filled out based on the ADS - harafaz.ia material. Where the source content does not provide a closed value, the field was filled as an **initial recommendation** or **to be validated in discovery/pilot**.

## 1. Business context and agent objective

- **Business unit:** Operations Directorate / harafaz.ia Backoffice, with cross-cutting action across the origination, maintenance and middle journeys.
- **Problem to solve:** fragmented channels, low traceability, absence of a single standardized case, low reuse of data/documents and difficulty measuring SLA, FCR, recurrence and productivity.
- **Main objective (expected outcome):** deploy an AI agent for triage and assisted self-service, integrated with case management, to reduce service/processing time, rework and loss of context, while preserving human escalation in critical cases.
- **Secondary objectives:**
  - standardize the intake of requests across multiple channels;
  - create a single case record with history and audit trail;
  - increase the reuse of data, documents and qualifications already performed;
  - improve operational governance and telemetry;
  - support handoff between journeys.
- **Executive success indicator:** reduction of the average service/processing time, increase in FCR, reduction of rework/recurrence and improvement of the network's internal NPS.

## 2. Functional scope

### 2.1 What the agent does

1. Receives requests through priority channels, classifies topic/product/risk/priority and opens or updates a single case.
2. Performs triage, guides the user, requests missing data, consults a curated knowledge base and triggers flows when eligible.
3. Escalates to a human with full context whenever there is an exception, sensitivity, risk or low confidence.
4. Records evidence, status, times, escalation reason and outcome for analytics.

### 2.2 What the agent does not do

1. Does not make an autonomous final decision in cases of compliance, risk or critical exceptions.
2. Does not replace normative governance, human review of knowledge or formal audit processes.
3. Does not eliminate legacy systems; it orchestrates their use progressively.
4. Must not operate on sources or channels outside the defined data and security policy.

### 2.3 Critical agent decisions

1. Determine whether the request is eligible for self-service/assisted automation or needs human escalation.
2. Determine whether the minimum data is complete and whether the applicable rule/checklist is in effect.
3. Choose the handoff destination based on topic, risk, product and context.
4. Decide when to record a block, pending item, corrective action or closure with evidence.

## 3. User profiles, journeys and channels

### 3.1 User profiles

- **Profile 1:** managers and teams of the business network / internal users.
- **Profile 2:** middle, operations, compliance and centralizing-unit specialists.
- **Profile 3:** product managers and rule-defining areas.
- **Profile 4:** end customer, in future iterations.

### 3.2 Main journeys

- **Journey A:** triage, guidance and case opening for the network's advisory requests.
- **Journey B:** request qualification and guided collection of data/documents for origination.
- **Journey C:** handoff between journeys and areas with context and traceability.
- **Journey D:** tracking of status, resolution, evidence and efficiency measurement.

### 3.3 Interaction channels

- [x] Web
- [x] Teams
- [ ] WhatsApp *(controlled expansion / when applicable)*
- [x] Email
- [x] Other: product-specific pipelines, portal/app, internal network channels

## 4. Non-functional requirements

- **Service SLA:** to be validated per journey and category; measurement recommended from the pilot onward.
- **Maximum acceptable latency:** initial recommendation of up to 5 seconds for the initial response and up to 15 seconds for simple actions with query/orchestration.
- **Target availability:** initial recommendation of 99.5% in the pilot and evolution to 99.9% in expanded production.
- **Expected volume (day/month):** to be validated in the discovery and per-app assessment.
- **Peak window:** commercial peaks, network service hours and campaign/product periods; details to be validated in discovery.
- **Scalability requirements:** expansion in waves, progressive inclusion of channels, products and hubs, maintaining the single case, observability and governance.

## 5. Data and integrations

### 5.1 Data sources

- **Source:** curated internal databases / harafaz.ia Chat / SharePoint / normative databases  
  - **Data type:** normative documents, FAQs, procedures, rules and operational knowledge  
  - **Sensitivity/classification:** internal / operationally confidential

- **Source:** Dataverse (single case)  
  - **Data type:** cases, status, SLA, history, evidence, classification, handoff, satisfaction  
  - **Sensitivity/classification:** operational and potentially sensitive data

- **Source:** legacy systems (e.g., CXTD, CMTR and others)  
  - **Data type:** processing status, business data, validations and pipeline feedback  
  - **Sensitivity/classification:** high / regulated

- **Source:** forms/survey (e.g., Forms)  
  - **Data type:** internal NPS and service feedback  
  - **Sensitivity/classification:** internal

### 5.2 Integrations

- **System/API:** Dataverse  
  - **Type (read, write, both):** both  
  - **Criticality:** critical

- **System/API:** Power Automate  
  - **Type (read, write, both):** both  
  - **Criticality:** critical

- **System/API:** legacy systems / product-specific pipelines  
  - **Type (read, write, both):** both  
  - **Criticality:** critical

- **System/API:** SharePoint / curated knowledge base / harafaz.ia Chat  
  - **Type (read, write, both):** read  
  - **Criticality:** high

- **System/API:** Teams / Email / Portal / Web channel  
  - **Type (read, write, both):** both  
  - **Criticality:** high

- **System/API:** Power BI / analytics  
  - **Type (read, write, both):** read  
  - **Criticality:** high

### 5.3 Data quality and governance

- **Data owner:** harafaz.ia operational areas per journey, with shared responsibility from product, backoffice and IT; the knowledge base under specialized curation.
- **Retention policies:** to be defined according to corporate policy, regulatory requirements and auditing.
- **Access rules:** least privilege per profile; segregation by environment, hub, topic and journey; Microsoft Entra ID authentication.

## 6. Governance, security and compliance

- **Mandatory guard rails:**
  - authentication via Microsoft Entra ID;
  - RBAC by role and by environment;
  - DLP policies for connectors, tools and channels;
  - audit trail for case creation, transfer, decision and closure;
  - blocking of sources/channels outside the data policy;
  - versioning of normative rules and checklists;
  - human-in-the-loop for critical decisions;
  - periodic review of the knowledge base.

- **Desired evaluators:**
  - groundedness;
  - hallucination detection;
  - classification and routing accuracy;
  - improper escalation rate;
  - context completeness at handoff;
  - quality by topic;
  - sensitive-data exposure detection.

- **Human-in-the-Loop (when and how):** mandatory in exceptions, high risk, low confidence, compliance, incomplete data or sensitive cases; the agent transfers with a summary, applied rules, evidence and history.
- **Applicable regulatory requirements:** LGPD and audit/compliance requirements gathered in discovery; other requirements specific to the journey/product must be confirmed with harafaz.ia.
- **Audit and traceability requirements:** logs of conversation, decision, automatic action, user, date/time, rule/checklist version, human justification and complete handoff trail.

## 7. Success criteria and KPIs

- **KPI 1 (current value -> target):** average service/origination time *(baseline to be measured in the pilot -> reduce within 90 days)*.
- **KPI 2 (current value -> target):** FCR / first-contact resolution rate *(baseline to be measured -> progressive increase for eligible requests)*.
- **KPI 3 (current value -> target):** rework / recurrence rate *(baseline to be measured -> progressive reduction with a curated base and assisted automation)*.
- **KPI 4 (current value -> target):** reuse of data/documents across journeys *(baseline to be measured -> progressive increase)*.
- **KPI 5 (current value -> target):** network internal NPS *(current baseline to be confirmed -> increase after deployment)*.
- **Measurement horizon (30/60/90 days):**
  - **30 days:** channel/pilot adoption, volume handled, classification quality and baseline;
  - **60 days:** FCR, escalation, backlog and SLA;
  - **90 days:** reduction of rework/recurrence, NPS and evidence of value.

## 8. Constraints, risks and assumptions

### 8.1 Constraints

- **Budget:** not stated in the material; an incremental, wave-based approach is recommended.
- **Timeline:** suggested roadmap between 0 and 28 weeks, with an initial pilot within up to 8 weeks and change management estimated at 4–6 months.
- **Technology:** priority use of Copilot Studio, Dataverse, Power Automate, Microsoft channels and progressive integration with existing legacy systems.

### 8.2 Risks

- **Risk:** maintaining the current behavior of direct person-to-person contact / channel duplication.  
  - **Impact:** low adoption and little traceability.  
  - **Mitigation:** a simpler single channel, visible SLA, per-case privacy and a better experience.

- **Risk:** quality and governance of the knowledge base / normative documents.  
  - **Impact:** inaccurate responses and operational risk.  
  - **Mitigation:** continuous curation, versioning and periodic review.

- **Risk:** integration with multiple pipelines and legacy systems.  
  - **Impact:** rollout delay and increased complexity.  
  - **Mitigation:** pilot in 1–2 priority hubs/products and expansion in waves.

- **Risk:** privacy and sensitivity of service interactions.  
  - **Impact:** improper data exposure and non-compliance.  
  - **Mitigation:** RBAC, per-case/hub segregation, DLP, auditing and HITL.

- **Risk:** excessive automation in critical decisions.  
  - **Impact:** operational error and regulatory risk.  
  - **Mitigation:** clear autonomy limits and mandatory human review.

### 8.3 Assumptions

1. harafaz.ia will maintain a curated and up-to-date knowledge base.
2. There will be operational sponsorship to enforce the single case record and reduce the use of parallel channels.
3. The priority legacy systems will have feasible integration in stages.
4. There will be a definition of data owners, SLAs and escalation criteria per journey.

## 9. Wave-based roadmap

### Wave 1 - Pilot

- **Scope:** single case in Dataverse; agent in Copilot Studio for triage and FAQ/guided collection; 1 pilot journey and 1–2 priority channels; versioned checklist/rules; initial dashboard.
- **Duration:** 0–8 weeks.
- **Exit criterion:** stabilized pilot, measured baseline, functional handoff, active telemetry and initial evidence of reduced effort/rework.

### Wave 2 - Expansion

- **Scope:** channel expansion; integration of the main pipelines/legacy systems; structured handoff between journeys; automations for recurring topics; expansion to 2–3 priority products/hubs.
- **Duration:** 9–16 weeks.
- **Exit criterion:** proven gain in FCR/SLA, reduction of improper escalation, broader adoption and operational governance in place.

### Wave 3 - Scale

- **Scope:** expanded omnichannel; more assisted automations with guardrails; advanced analytics; consolidation of governance, connectors, observability and broad rollout.
- **Duration:** 17–28 weeks.
- **Exit criterion:** scalable operation with consolidated observability, security and governance, plus a continuous improvement roadmap.

## 10. Questions for target-architecture decisions

- **Which part of the journey depends on governed data?** request classification, consultation of normative documents and current rules, customer and operations data/documents, case status, SLA, history, evidence and decisions.
- **Where is external context (Web IQ) needed?** in general, low for the operational core; useful only for public regulatory references or controlled and approved external content.
- **Which flows require human approval?** compliance, exceptions, high risk, low model confidence and decisions that impact the customer, credit, eligibility or sensitive dealings.
- **Which components require greater observability?** classification/routing, handoff between journeys, integrations with legacy systems, knowledge base usage, flow latency/failures and decision auditing.

## 11. Optional appendices

- **Current process diagram (AS-IS):** derive from the discovery material and the per-journey interviews.
- **Target architecture diagram (TO-BE):** use the Origination and Middle reference architectures in Copilot Studio as a basis.
- **Relevant internal policies:** data policy, identity and access, LGPD, auditing, connector governance, retention and knowledge curation.
- **Technical references:** Copilot Studio, Dataverse, Power Automate, analytics, handoff and DLP policies / Power Platform security.
