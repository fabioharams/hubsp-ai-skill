# AI Agent Project Specifications

## 1. Business context and agent objective
- Business unit:
- Problem to solve:
- Main objective (expected outcome):
- Secondary objectives:
- Executive success indicator:

## 2. Functional scope
### 2.1 What the agent does
- 
- 

### 2.2 What the agent does not do
- 
- 

### 2.3 Critical agent decisions
- 
- 

### 2.4 Recommended architectural pattern (complexity spectrum)
- [ ] LLM (simple text, single step)
- [ ] RAG (response grounded in data)
- [ ] Single AI Agent (multi-step in one domain)
- [ ] Agentic AI (multi-agent, multiple domains)
- Rationale for the choice (lowest complexity that solves the case):
- Conditions for evolving to a more complex pattern in the roadmap:

## 3. User profiles, journeys and channels
### 3.1 User profiles
- Profile 1:
- Profile 2:

### 3.2 Main journeys
- Journey A:
- Journey B:

### 3.3 Interaction channels
- [ ] Web
- [ ] Teams
- [ ] WhatsApp
- [ ] Email
- [ ] Other:

## 4. Non-functional requirements
- Service SLA:
- Maximum acceptable latency:
- Target availability:
- Expected volume (day/month):
- Peak window:
- Scalability requirements:

## 5. Data and integrations
### 5.1 Data sources
- Source:
- Data type:
- Sensitivity/classification:

### 5.2 Integrations
- System/API:
- Type (read, write, both):
- Criticality:

### 5.3 Data quality and governance
- Data owner:
- Retention policies:
- Access rules:

## 6. Governance, security and compliance
- Mandatory guard rails:
- Desired evaluators:
- Human-in-the-Loop (when and how):
- Applicable regulatory requirements:
- Audit and traceability requirements:

## 7. Success criteria and KPIs
- KPI 1 (current value -> target):
- KPI 2 (current value -> target):
- KPI 3 (current value -> target):
- Measurement horizon (30/60/90 days):

### 7.1 ROI/AAI assumptions
- Loaded man-hour cost (R$/h):
- Task volume (month):
- AI cost per task (tokens + tools):
- HITL time per task (min):
- Amortized setup cost per task:
- Analysis mode:
	- [ ] Efficiency (replacement)
	- [ ] Amplification (copilot)
- Financial evaluation horizon (12-18 months):

## 8. Constraints, risks and assumptions
### 8.1 Constraints
- Budget:
- Timeline:
- Technology:

### 8.2 Risks
- Risk:
- Impact:
- Mitigation:

### 8.3 Assumptions
- 
- 

## 9. Wave-based roadmap
### Wave 1 - Pilot
- Scope:
- Duration:
- Exit criterion:

### Wave 2 - Expansion
- Scope:
- Duration:
- Exit criterion:

### Wave 3 - Scale
- Scope:
- Duration:
- Exit criterion:

## 10. Questions for target-architecture decisions

### 10.1 Intake Filter (Microsoft AI Decision Framework)
- Which business problem needs to be solved now?
- Is there material impact (financial, regulatory, operational or reputational)?
- Which decisions must remain under mandatory human approval?

### 10.2 BXT (Business, Experience, Technology)
- Business: which business KPI will be moved and in how much time?
- Experience: which journey changes for the user, operator and manager?
- Technology: what minimum stack meets the need with security and scale?

### 10.3 9 critical questions (summary for the decision)
- 1) What is the expected business outcome?
- 2) What is the acceptable risk level?
- 3) Which governed data is mandatory?
- 4) Where does Web IQ add real value?
- 5) Which integrations require write/transaction?
- 6) What level of agent autonomy is appropriate?
- 7) Which guard rails and evaluators are mandatory at go-live?
- 8) What scalability criterion is required to exit the pilot?
- 9) What trade-off is accepted between cost, risk, speed and complexity?

## 11. Optional appendices
- Current process diagram (AS-IS):
- Target architecture diagram (TO-BE):
- Relevant internal policies:
- Technical references:

---

## How to use this document with the skill

### VS Code / GitHub Copilot App
Use in the prompt:

> Using #SKILL.md and #doc/agent-project-specifications.md, generate an executive recommendation in the complete format: (1) a medium executive overview (1-2 paragraphs) with at least 1 Mermaid diagram or flowchart to explain the recommended decision, (2) the recommended architectural pattern (LLM/RAG/AI Agent/Agentic AI) with detailed justifications, official Microsoft links and at least 1 Mermaid diagram or flowchart to explain the choice, (3) the target architecture (Work IQ, Foundry IQ, Fabric IQ and Web IQ) with a detailed explanation and 2 mandatory Mermaid diagrams (architecture and decision flowchart), (4) governance and security with guard rails, evaluators, analysis of PL 2338/2023 and an explanation of how the tools and services selected in the architecture address the pillars of transparency, governance, risk, auditing, human oversight and data protection with official sources, and at least 1 Mermaid diagram or flowchart, (5) a phased implementation plan with a breakdown per phase (objective, scope, integrations, entry/exit criteria, target KPI and dominant risk) and at least 1 Mermaid diagram or flowchart, (6) ROI/AAI assumptions with at least 1 Mermaid diagram or flowchart to explain the financial logic, (7) success KPIs with at least 1 Mermaid diagram or flowchart, and (8) risks and mitigations with clarity, official Microsoft links and at least 1 Mermaid diagram or flowchart. The response must be delivered in a new markdown document called doc/resultado.md.

### GitHub Copilot CLI
Use in the prompt:

> Read SKILL.md and doc/agent-project-specifications.md and generate an executive recommendation in an advanced format: a medium executive overview with a Mermaid diagram or flowchart; the architectural pattern with detailed justifications, Microsoft sources and a Mermaid diagram or flowchart; the Work IQ/Foundry IQ/Fabric IQ/Web IQ architecture with a Mermaid diagram and a Mermaid flowchart; governance and security with analysis of PL 2338/2023, an explanation of how the tools and services selected in the architecture address the pillars of transparency, governance, risk, auditing, human oversight and data protection with official sources, and a Mermaid diagram or flowchart; a detailed phased plan with a Mermaid diagram or flowchart; ROI/AAI assumptions with a Mermaid diagram or flowchart; KPIs with a Mermaid diagram or flowchart; risks and mitigations with official Microsoft links and a Mermaid diagram or flowchart. The response must be delivered in a new markdown document called doc/resultado.md.
