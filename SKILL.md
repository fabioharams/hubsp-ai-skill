---
name: hubsp-ai-skill
summary: "Guides the definition of corporate architecture for AI agent adoption with Microsoft IQ, Fabric and Foundry, including Work IQ, Foundry IQ, Fabric IQ and Web IQ, architecture fundamentals (LLM, RAG, AI Agent, Agentic AI), ROI model (AI vs. person-hour), governance, security, guard rails and continuous evaluation."
description: "Skill for guiding AI agent adoption strategy in the Microsoft ecosystem, including target architecture, governance, ROI, security and regulatory compliance."
license: MIT
metadata:
  author: Fabio
  version: "1.2.0"
  language: en-US
---

# Skill: AI Agent Adoption Strategy

## Objective

This skill helps structure practical recommendations for adopting AI agents in corporate environments, focusing on:

- AI architecture fundamentals (LLM, RAG, AI Agent, Agentic AI)
- reference architecture
- governed data
- financial justification (ROI: AI vs. person-hour cost)
- security and compliance
- operations and observability
- continuous evolution with evaluators

## Use When

- The user asks for an AI agent adoption strategy.
- The user wants to design architecture with Work IQ, Foundry IQ and Fabric IQ, including external context via Web IQ when applicable.
- The user needs to understand or compare LLM, RAG, AI Agent and Agentic AI patterns.
- The user wants to decide the minimum level of complexity for a use case.
- The user needs to connect AI with data governance and security.
- The user requests a phased deployment roadmap.
- The user asks for financial justification or ROI (AI vs. person-hour, efficiency or expansion mode).
- The user asks for patterns to scale agents across business units.
- The user asks for regulatory analysis, governance or compliance of Microsoft Copilot Studio, Microsoft Foundry and Purview with requirements such as transparency, audit, risk, human oversight and data protection.

## Do Not Use When

- The request is only to fix local code without architectural context.
- The user only wants specific CLI commands without architecture decisions.
- The topic is entirely outside the Microsoft/Fabric/Foundry ecosystem.

## Expected Inputs

- business objective
- impacted area(s)
- data maturity
- security/compliance requirements
- timeline and priority

If critical information is missing, ask only for the minimum necessary before recommending the architecture.

## Recommended Process

1. Understand the business problem and expected outcome.
2. Choose the architectural pattern by the lowest level of complexity that reliably solves it: LLM (text, one step), RAG (data-grounded response), single AI Agent (multi-step task, one domain) or Agentic AI multi-agent (crosses security boundaries, multiple teams or expected growth).
2.1. When the request involves choosing a Microsoft technology/product, apply the Microsoft AI Decision Framework (references/05-decision-framework-bxt.md): Intake Filter, BXT (Business/Experience/Technology), the 9 critical questions and scenario-based selection.
3. Map data sources and current governance level.
4. Define layer separation: experience (Work IQ), agents (Foundry IQ), data intelligence (Fabric IQ), external context (Web IQ, when necessary) and platform (Microsoft Fabric).
4.1. When the case requires it, recommend a **mixed solution**: Copilot Studio for the conversational/business flow layer and Microsoft Foundry for the reasoning/advanced orchestration layer.
5. Define cross-cutting controls: Guard Rails and Evaluators.
5.1. When the request involves regulation, compliance or adherence to legal requirements, map the regulatory axes to Microsoft's technical and governance capabilities, without asserting automatic legal compliance.
6. Validate financial viability with the ROI model (AAI = human cost / AI cost per task), including HITL, amortized setup and scope multiplier; evaluate over a 12-18 month horizon.
7. Propose a wave-based roadmap: pilot, expansion and scale.
8. Close with success metrics, risks and mitigation plan.

## Response Quality Rules

- Explain the "why" behind each recommendation.
- Prefer executive language with objective technical details.
- Always make trade-offs explicit (cost, risk, speed, complexity).
- Avoid generic responses; adapt to the provided context.
- Include actionable next steps.

## Preferred Terms

- Prioritize the terms: guard rails, evaluators, wave-based roadmap, target architecture, governed data.
- For fundamentals, use: complexity spectrum, grounding, RAG, single AI Agent, Agentic AI (multi-agent), HITL, MCP, A2A.
- For ROI, use: loaded person-hour cost, AAI (AI Advantage Index), cost per task, HITL, scope multiplier, realization factor, efficiency mode, expansion mode.
- When synonyms exist, maintain the terms above for consistency across responses.
- In executive responses, use short, decision-oriented sentences.

## Suggested Output Format

- Executive summary (medium)
  - Deliver in 1-2 paragraphs, with context, recommended decision, expected impact and main trade-offs (cost, risk, speed and complexity).
  - Must clearly state the business problem, proposed target architecture and short-term result (pilot) vs. medium-term result (scale).
  - Include at least 1 diagram or simple Mermaid flowchart to visually explain the recommended decision.
  - The visual must summarize the recommendation logic in executive language and be easy to read.
  - Microsoft reference: https://learn.microsoft.com/azure/cloud-adoption-framework/strategy/

- Recommended architectural pattern (LLM, RAG, AI Agent or Agentic AI) with detailed justification
  - Compare options in the context of the case and justify why the recommendation minimizes risk and maximizes value.
  - Explain technical criteria: grounding, orchestration needs, autonomy, data quality, latency, cost per task and HITL requirements.
  - Include justifications with official Microsoft sources to support each choice.
  - Include at least 1 Mermaid flowchart or diagram to explain the chosen architectural pattern and discarded paths.
  - The visual must facilitate understanding of the LLM → RAG → AI Agent → Agentic AI spectrum and the final decision.
  - Microsoft references:
    - Azure OpenAI: https://learn.microsoft.com/azure/ai-services/openai/overview
    - RAG on Azure AI Search: https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview
    - Azure AI Foundry Agent Service: https://learn.microsoft.com/azure/ai-foundry/agents/overview
    - Microsoft AI Decision Framework: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/

- Recommended architecture (layers and responsibilities) with detailed explanation
  - Describe roles and boundaries of Work IQ, Foundry IQ, Fabric IQ and Web IQ, including how they connect to governed data and cross-cutting controls.
  - Explain responsibilities per layer (experience/channels, agent orchestration, data/analytics, external context).
  - Required to include:
    - 1 Mermaid architecture diagram (layers and main flows).
    - 1 Mermaid flowchart (routing decision: self-service, escalation, HITL).
  - Diagrams must be simple, readable and decision-oriented for executive audiences.
  - Microsoft references:
    - Microsoft 365 Copilot: https://learn.microsoft.com/microsoft-365-copilot/
    - Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry/
    - Microsoft Fabric: https://learn.microsoft.com/fabric/

- Governance and security (controls)
  - Detail technical and operational guard rails: Entra ID, RBAC, DLP, audit trail, rules/checklist versioning, evaluators and HITL.
  - Relate each control to the risk it mitigates (e.g., hallucination, unauthorized access, critical decision without oversight).
  - Include explicit analysis of PL 2338/2023, connecting the recommended architecture to the axes of transparency, governance, risk, audit, human oversight and data protection.
  - Explain how the tools and services selected in the architecture address each regulatory axis, indicating limits, dependencies and any implementation gaps.
  - Prioritize official Microsoft sources and, when relevant, mention the repository's regulatory reference file to support the analysis.
  - Include at least 1 Mermaid diagram or flowchart showing the sequence of controls, validations and blocking/approval points.
  - Microsoft references:
    - Microsoft Entra: https://learn.microsoft.com/entra/identity/
    - Microsoft Purview: https://learn.microsoft.com/purview/governance-solutions-overview
    - Responsible AI in Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry/responsible-ai/overview
    - Microsoft Security: https://learn.microsoft.com/security/
    - Well-Architected Framework - Security: https://learn.microsoft.com/azure/well-architected/security/

- Phased deployment plan (detailed)
  - Describe at least 3 phases: Pilot, Expansion and Scale.
  - For each phase, specify: objective, functional scope, integrations, minimum guard rails, entry criteria, exit criteria, target KPI and dominant risk.
  - Include critical dependencies (data, integrations, executive sponsorship, change management).
  - Include at least 1 Mermaid diagram or flowchart to explain the progression between phases, dependencies and decision gates.
  - Microsoft reference: https://learn.microsoft.com/azure/cloud-adoption-framework/plan/

- Financial justification (ROI/AAI, when applicable)
  - Explain assumptions, baseline, calculation method and value capture horizon.
  - Include loaded person-hour cost, AI cost per task, HITL, amortized setup and sensitivity (conservative/base/aggressive).
  - Include at least 1 Mermaid diagram or flowchart to explain the calculation logic, cost drivers and financial decision criteria.
  - Microsoft references:
    - Azure Pricing Calculator: https://azure.microsoft.com/pricing/calculator/
    - Azure TCO Calculator: https://azure.microsoft.com/pricing/tco/calculator/

- Success KPIs
  - Cover efficiency, quality, risk and adoption KPIs (e.g., SLA, FCR, rework, latency, improper escalation rate, cost per case, internal NPS).
  - Suggest measurement windows (30/60/90 days) and adjustment triggers.
  - Include at least 1 Mermaid diagram or flowchart to organize KPIs by category, measurement horizon or causal relationship with business value.
  - Microsoft references:
    - Azure Monitor: https://learn.microsoft.com/azure/azure-monitor/
    - Application Insights: https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview

- Risks and mitigations (clear, with official justification)
  - Clearly explain the main risks: data, security, compliance, operations, adoption and integration dependency.
  - For each risk, include impact, probability, warning signal and technical/procedural mitigation.
  - Always justify mitigations with official Microsoft links.
  - Include at least 1 Mermaid diagram or flowchart showing the relationship between risk, control, mitigation and response owner.
  - Microsoft references:
    - Microsoft Security: https://learn.microsoft.com/security/
    - Well-Architected Framework (Security): https://learn.microsoft.com/azure/well-architected/security/
    - Well-Architected Framework (Operational Excellence): https://learn.microsoft.com/azure/well-architected/operational-excellence/

## Internal Reference

Load only the reference file needed for the question (progressive disclosure):

- references/01-llm-rag-ai-agent-fundamentals.md — LLM vs RAG vs AI Agent vs Agentic AI; complexity spectrum and decision guide.
- references/02-reference-architecture-layers.md — Microsoft IQ (Work IQ, Foundry IQ, Fabric IQ, Web IQ) and Microsoft Fabric; technical specifications per layer.
- references/03-roi-ai-vs-man-hour.md — ROI/AAI model, HITL, scope multiplier.
- references/04-governance-guard-rails-evaluators-hitl.md — Guard Rails, Evaluators and Human-in-the-Loop.
- references/05-decision-framework-bxt.md — Microsoft AI Decision Framework: Intake Filter, BXT, 9 critical questions, Capability Model and technology selection by scenario.
- references/06-pl-2338-2023-copilot-studio-foundry.md — analysis of PL 2338/2023, focusing on transparency, governance, risk, audit, human oversight and data protection with official sources.

For topics not covered by these curated references, read only the lightweight index in AI_Agent_Adoption_Strategy_Final_2.md, select the relevant file from `chapters/`, and load that chapter only. Do not load all chapter files by default.
