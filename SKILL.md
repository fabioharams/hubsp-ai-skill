---
name: hubsp-ai-skill
summary: "Guides low-complexity-first corporate AI adoption with Microsoft IQ context workloads, Microsoft Foundry and Fabric, including architecture selection, agent runtimes, ROI, governance, security, guard rails and continuous evaluation."
description: "Use when selecting the simplest viable Microsoft AI architecture or defining agent adoption, runtime, governed data, security, ROI and evidence-based escalation from automation to multi-agent."
license: MIT
metadata:
  author: Fabio
  version: "1.9.0"
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
- The user wants to design architecture with Work IQ, Foundry IQ and Fabric IQ, including external context via Web IQ and an explicit agent runtime when applicable.
- The user needs to understand or compare LLM, RAG, AI Agent and Agentic AI patterns.
- The user wants to decide the minimum level of complexity for a use case.
- The user asks for the simplest viable architecture, a low-complexity baseline or evidence for escalating to an agentic solution.
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

- One attached scenario input document containing the available business and technical facts. The preferred discovery input is a completed `doc/business-architecture-questionnaire.md`, but an equivalent Markdown, text, Word or PDF document is valid.
- The document should cover, when known: business objective and measures; current process and existing capabilities; users and channels; data and actions; risk and compliance; demand and economics; identity and integrations; runtime and network; capacity and reliability; security, operations and delivery.

If critical information is missing, ask only for the minimum necessary before recommending the architecture.
Treat the attached document as the case context and normalize it against `doc/business-architecture-questionnaire.md`; do not require the same headings, question order or filename. Reuse facts already present and do not ask the respondent to re-enter them in the questionnaire. Treat answers as observations and requirements, not a respondent-selected architecture. If only business information is available, provide an initial conditional recommendation and list only the missing technical facts that could change the decision. Unresolved identity, data-access, integration, network, regional, capacity, reliability, security or operational constraints must remain explicit pre-production validation gates.

## Recommended Process

1. Understand the business problem and expected outcome.
2. Evaluate solutions in this mandatory order and stop at the first option that reliably satisfies the current requirements:
  1. Existing Microsoft product, SaaS capability or configuration.
  2. Deterministic workflow, rules, API integration or Power Automate.
  3. Direct LLM call for one-step generative work.
  4. RAG for grounded responses without autonomous tool execution.
  5. Single AI Agent for bounded multi-step reasoning or tool use in one domain.
  6. Multi-agent or mixed architecture only for independently justified specialization or runtime requirements that a single agent cannot reliably satisfy.
2.1. Do not escalate because a technology is strategically attractive, because future growth is possible, or because the scenario has security/compliance requirements. Address security boundaries first with isolated identities, least-privilege tools, permissions, data controls, audit and HITL.
2.2. For every escalation, identify the requirement that the preceding option cannot satisfy, the supporting evidence or explicit assumption, and the incremental cost, latency, operational risk and governance burden. If evidence is missing, recommend the lower-complexity option and label the assumption to validate during the pilot.
2.3. Design for evolution without pre-building future complexity. Define measurable escalation triggers such as orchestration failure rate, tool-count or domain-boundary thresholds, latency limits, ownership separation or evaluation results.
2.4. When the request involves choosing a Microsoft technology/product, apply the Microsoft AI Decision Framework (references/05-decision-framework-bxt.md): Intake Filter, BXT (Business/Experience/Technology), the 9 critical questions and scenario-based selection.
2.5. Before recommending any Microsoft product, SaaS capability, license, SKU or configuration for production, perform a capacity and scale fit assessment (references/07-capacity-and-scale-assessment.md). Translate business demand into peak requests and tokens per minute, concurrent users or jobs, messages/credits, data and vector-index size, ingestion rate, Capacity Units/Search Units and availability requirements as applicable. Check current licensing entitlements, service quotas and hard limits, regional/model/tool availability, downstream connector/API limits and quota-increase lead time. The lowest limit in the end-to-end path is the effective capacity.
2.6. Record a verdict for each selected component: **Fit**, **Conditional fit** or **Not fit**. Include the demand assumption, current limit and scope, required headroom, proposed license/SKU/configuration, load-test or pilot evidence, monitoring signal, scale action and official Microsoft source with an access date. Do not claim that capacity is validated from nominal daily or monthly volume alone. If demand or current quota is unknown, mark the recommendation conditional and define the measurement or administrative check required before production approval.
3. Map data sources and current governance level.
4. Define layer separation: channels and experiences; context workloads (Work IQ, Foundry IQ, Fabric IQ and Web IQ when necessary); agent runtime (Microsoft Foundry Agent Service, Copilot Studio or Microsoft Agent Framework); and data platform (Microsoft Fabric).
4.1. Treat the IQs as complementary context sources, not interchangeable execution layers: Work IQ supplies Microsoft 365 work context; Foundry IQ supplies permission-aware enterprise knowledge through knowledge bases and agentic retrieval; Fabric IQ supplies semantic business context; Web IQ supplies current external web context.
4.2. Recommend a **mixed solution** only when the case simultaneously requires a business experience/channel capability best served by Copilot Studio and advanced pro-code reasoning or orchestration that Copilot Studio cannot reliably satisfy. Compliance, anticipated scale or channel preference alone is not sufficient. Document why a single runtime is inadequate.
5. Define cross-cutting controls: Guard Rails and Evaluators.
5.1. When the request involves regulation, compliance or adherence to legal requirements, map the regulatory axes to Microsoft's technical and governance capabilities, without asserting automatic legal compliance.
6. Validate financial viability with the ROI model (AAI = human cost / AI cost per task), including HITL, amortized setup and scope multiplier; evaluate over a 12-18 month horizon.
7. Propose a wave-based roadmap: pilot, expansion and scale.
8. Close with success metrics, risks and mitigation plan.

## Response Quality Rules

- Explain the "why" behind each recommendation.
- Prefer executive language with objective technical details.
- Always make trade-offs explicit (cost, risk, speed, complexity).
- Always name the simplest viable baseline, the rejected simpler options and the evidence-based reason for each rejection.
- Never recommend a production product, license, SKU or configuration without a capacity verdict and an explicit peak-demand assumption.
- Separate commercial entitlement from technical throughput: licenses, credits or prepaid capacity do not by themselves guarantee sufficient rate limits, concurrency or downstream capacity.
- Separate capabilities required now from deferred capabilities, and define measurable triggers for adding the deferred complexity.
- Prefer a deterministic or single-agent pilot when uncertainty remains; do not present multi-agent as the default target state.
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
  - Must clearly state the business problem, simplest viable baseline, proposed target architecture and short-term result (pilot) vs. medium-term result (scale).
  - Include at least 1 diagram or simple Mermaid flowchart to visually explain the recommended decision.
  - The visual must summarize the recommendation logic in executive language and be easy to read.
  - Microsoft reference: https://learn.microsoft.com/azure/cloud-adoption-framework/strategy/

- Recommended architectural pattern (LLM, RAG, AI Agent or Agentic AI) with detailed justification
  - Compare existing/SaaS, deterministic automation, LLM, RAG, single-agent and multi-agent options in that order, stopping at the first option that meets current requirements.
  - For every rejected simpler option, state the unmet requirement and evidence or assumption. Include the incremental cost, latency, operational risk and governance burden of the selected escalation.
  - Identify deferred capabilities and measurable triggers for evolving to a more complex pattern.
  - Explain technical criteria: grounding, orchestration needs, autonomy, data quality, latency, cost per task and HITL requirements.
  - Include justifications with official Microsoft sources to support each choice.
  - Include at least 1 Mermaid flowchart or diagram to explain the chosen architectural pattern and discarded paths.
  - The visual must facilitate understanding of the LLM → RAG → AI Agent → Agentic AI spectrum and the final decision.
  - Microsoft references:
    - Azure OpenAI: https://learn.microsoft.com/azure/ai-services/openai/overview
    - RAG on Azure AI Search: https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview
    - Microsoft Foundry Agent Service: https://learn.microsoft.com/azure/foundry/agents/overview
    - Microsoft AI Decision Framework: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/

- Recommended architecture (layers and responsibilities) with detailed explanation
  - Distinguish the minimum viable architecture for the first wave from optional future-state components. Do not include future components in the initial implementation unless an evidence-based escalation gate requires them.
  - Describe roles and boundaries of Work IQ, Foundry IQ, Fabric IQ and Web IQ, including how they connect to governed data, the selected agent runtime and cross-cutting controls.
  - Explain responsibilities per layer (experience/channels, context sources, agent runtime/orchestration, data platform and cross-cutting controls).
  - Include a **capacity and scale fit matrix** for every recommended Microsoft product, SaaS capability and material downstream dependency. At minimum show: demand metric and peak assumption; current entitlement/quota/limit and scope; required headroom; selected license/SKU/configuration; region availability; bottleneck; Fit/Conditional fit/Not fit verdict; validation method; monitoring and scale trigger; official source and access date.
  - For SaaS, distinguish user/license eligibility, metered consumption and rate provisioning. For Foundry models, assess TPM/RPM, quota scope, deployment type and regional capacity. For Copilot Studio, assess credits/messages separately from RPM/RPH and downstream Power Platform/connectors. For Fabric, estimate and measure CUs by workload and concurrency. For Azure AI Search, assess index/vector storage, replicas, partitions, Search Units, query/indexing throughput and SLA topology.
  - Show the capacity calculation or state why it cannot yet be completed. Treat missing production demand, tenant entitlement or subscription quota as a conditional recommendation with a pre-production validation gate.
  - Do not describe Foundry IQ as the agent runtime. Foundry IQ is the managed enterprise knowledge layer; Microsoft Foundry Agent Service, Copilot Studio or Microsoft Agent Framework performs orchestration and execution.
  - Required to include:
    - 1 Mermaid architecture diagram (layers and main flows).
    - 1 Mermaid flowchart (routing decision: self-service, escalation, HITL).
  - Diagrams must be simple, readable and decision-oriented for executive audiences.
  - Microsoft references:
    - Microsoft 365 Copilot: https://learn.microsoft.com/microsoft-365-copilot/
    - Microsoft Foundry: https://learn.microsoft.com/azure/foundry/
    - Microsoft Foundry Agent Service: https://learn.microsoft.com/azure/foundry/agents/overview
    - Microsoft IQ: https://learn.microsoft.com/microsoft-iq/
    - Foundry IQ: https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq
    - Fabric IQ: https://learn.microsoft.com/fabric/iq/overview
    - Microsoft Fabric: https://learn.microsoft.com/fabric/

- Governance and security (controls)
  - Detail technical and operational guard rails: Entra ID, RBAC, DLP, audit trail, rules/checklist versioning, evaluators and HITL.
  - Relate each control to the risk it mitigates (e.g., hallucination, unauthorized access, critical decision without oversight).
  - Include explicit analysis of PL 2338/2023 only when the scenario involves Brazilian clients, operations or companies, connecting the recommended architecture to the axes of transparency, governance, risk, audit, human oversight and data protection. Otherwise state that it is outside the scenario scope and assess only the applicable regulations identified in the input.
  - Explain how the tools and services selected in the architecture address each regulatory axis, indicating limits, dependencies and any implementation gaps.
  - Prioritize official Microsoft sources and, when relevant, mention the repository's regulatory reference file to support the analysis.
  - Include at least 1 Mermaid diagram or flowchart showing the sequence of controls, validations and blocking/approval points.
  - Microsoft references:
    - Microsoft Entra: https://learn.microsoft.com/entra/identity/
    - Microsoft Purview: https://learn.microsoft.com/purview/governance-solutions-overview
    - Responsible AI in Microsoft Foundry: https://learn.microsoft.com/azure/foundry/responsible-use-of-ai-overview
    - Microsoft Agent 365: https://learn.microsoft.com/microsoft-agent-365/overview
    - Microsoft Entra Agent ID: https://learn.microsoft.com/entra/agent-id/what-is-microsoft-entra-agent-id
    - Microsoft Security: https://learn.microsoft.com/security/
    - Well-Architected Framework - Security: https://learn.microsoft.com/azure/well-architected/security/

- Phased deployment plan (detailed)
  - Describe at least 3 phases: Pilot, Expansion and Scale.
  - Start the pilot with the simplest viable baseline and add architectural complexity only when defined exit metrics or escalation triggers justify it.
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
- references/02-reference-architecture-layers.md — Microsoft IQ context workloads (Work IQ, Foundry IQ, Fabric IQ and Web IQ), agent runtimes and Microsoft Fabric; technical specifications per layer.
- references/03-roi-ai-vs-man-hour.md — ROI/AAI model, HITL, scope multiplier.
- references/04-governance-guard-rails-evaluators-hitl.md — Guard Rails, Evaluators and Human-in-the-Loop.
- references/05-decision-framework-bxt.md — Microsoft AI Decision Framework: Intake Filter, BXT, 9 critical questions, Capability Model and technology selection by scenario.
- references/06-pl-2338-2023-copilot-studio-foundry.md — analysis of PL 2338/2023, focusing on transparency, governance, risk, audit, human oversight and data protection with official sources.
- references/07-capacity-and-scale-assessment.md — demand model, product-specific capacity checks, fit verdict, headroom, pilot/load validation and official Microsoft capacity references.

For a new use case, use the attached scenario input document as the case context and load `doc/business-architecture-questionnaire.md` only as the normalization checklist. A completed copy of the questionnaire is preferred but not mandatory. Use `doc/agent-project-specifications.md` when implementation requirements are already formalized or after discovery converts the available scenario into an approved implementation specification.

For topics not covered by these curated references, read only the lightweight index in AI_Agent_Adoption_Strategy_Final_2.md, select the relevant file from `chapters/`, and load that chapter only. Do not load all chapter files by default.
