# hubsp-ai-skill

## What is this project

This repository organizes a practical knowledge base to guide the corporate adoption of AI in the Microsoft ecosystem. The focus is on selecting the **simplest viable architecture first**, then combining Microsoft IQ context workloads (Work IQ, Foundry IQ, Fabric IQ and Web IQ), explicit agent runtimes, governed data, security, guard rails, evaluators and operations only where the current requirements justify them.

The project was structured to serve as both an executive and technical reference: it helps business, architecture, data and security teams align on a common vision for planning, piloting and expanding AI initiatives with lower risk and greater value predictability. Skill version **1.10.0** accepts either the completed 30-question intake or any equivalent business and technical scenario document, makes low-complexity-first selection mandatory, requires evidence before escalating to agentic, multi-agent or mixed-runtime solutions, and requires a capacity and scale fit verdict before a Microsoft product, SaaS capability, license, SKU or configuration is approved for production. The skill metadata (`name` and `description`) remains compatible with Claude's custom-skill upload requirements.

## Disclaimer

This is an independent community project. It is not an official Microsoft repository and is not endorsed, maintained or supported by Microsoft.

All outputs and recommendations produced by this skill must be reviewed and validated through a Human-in-the-Loop (HITL) process by qualified stakeholders before they are used for business, architecture, security, compliance or production decisions.

## Objective

- Define a reference architecture for AI agents in a corporate context.
- Evaluate existing products, deterministic automation, LLM, RAG, single-agent and multi-agent options in ascending complexity.
- Stop at the first option that reliably satisfies current requirements and require evidence before every escalation.
- Validate product licensing, quotas, throughput, concurrency, data/index size, regional availability, downstream limits and scale headroom against peak requirements.
- Require component-level technical justification and traceable official links for every element in the target architecture, with documented capabilities separated from assumptions, design decisions and measured evidence.
- Standardize recommendations focused on governance, compliance and observability.
- Support a wave-based roadmap (pilot, expansion and scale) with clear criteria.
- Make trade-offs explicit across cost, risk, speed and complexity.

## Low-complexity-first decision policy

The skill evaluates options in this mandatory order:

```mermaid
flowchart LR
   A[Existing product<br/>or SaaS] --> B[Deterministic automation<br/>rules, APIs, Power Automate]
   B --> C[Direct LLM<br/>one-step generation]
   C --> D[RAG<br/>grounded response]
   D --> E[Single AI Agent<br/>bounded tool use]
   E --> F[Multi-agent or mixed<br/>independently justified]

   A -. stop when requirements are met .-> G[Selected baseline]
   B -. stop when requirements are met .-> G
   C -. stop when requirements are met .-> G
   D -. stop when requirements are met .-> G
   E -. stop when requirements are met .-> G
   F -. only with escalation evidence .-> G
```

For every escalation, the recommendation must identify:

1. The current requirement the preceding option cannot satisfy.
2. The test result, pilot evidence or explicit assumption supporting that conclusion.
3. The additional cost, latency, failure modes, operational ownership and governance burden.
4. The measurable trigger that would justify adding deferred complexity later.

When evidence is incomplete, the skill recommends the lower-complexity pilot and turns the uncertainty into a validation objective. Security, compliance, multiple teams or expected growth do not automatically justify multi-agent or mixed architecture. Apply identity, least privilege, isolated tools, data controls, audit, evaluators and HITL to the simpler baseline first.

## Capacity and scale decision policy

Every production recommendation must include a component-level capacity and scale fit matrix. It separates commercial entitlement (licenses, credits, messages or prepaid capacity) from technical throughput (RPM/RPH, TPM, concurrency, CUs, Search Units, replicas/partitions and downstream limits). The lowest sustainable limit in the complete runtime path is treated as the effective capacity.

Each selected component receives a **Fit**, **Conditional fit** or **Not fit** verdict. Unknown peak demand, tenant entitlement, subscription quota, region support or downstream capacity produces a conditional recommendation and a named pre-production validation gate. Daily or monthly volume alone is insufficient; the assessment uses peak demand, p50/p95 work per interaction, explicit headroom and representative end-to-end load testing.

## Who can use the architecture questionnaire

Anyone can use `doc/business-architecture-questionnaire.md` to provide structured inputs for an architecture recommendation. It does not require prior AI, Microsoft cloud or architecture expertise, and respondents should describe the need rather than choose a technology.

Typical users include:

- Business owners, process owners and subject-matter experts defining a problem or opportunity.
- Product managers, analysts and project managers preparing a discovery, business case or pilot.
- Developers, data teams, security teams and platform teams validating technical feasibility.
- Enterprise and solution architects comparing architecture options.
- Consultants, partners and pre-sales teams running customer workshops or assessments.
- Students, startups and individual practitioners evaluating an idea before implementation.

The questionnaire supports several working modes:

- **Individual intake:** one person completes Part A using available information. The skill produces an initial conditional recommendation and identifies only the missing inputs that could change it.
- **Collaborative workshop:** business participants complete Part A, while technical participants complete Part B during or after the workshop.
- **Interview guide:** a facilitator asks the questions and records concise answers, assumptions and validation owners.
- **Architecture review:** an existing project team uses both parts to challenge a proposed design and expose unsupported product, capacity, security or operational assumptions.
- **Proposal or discovery input:** consultants and partners use the completed questionnaire as a consistent basis for recommendations, estimates and next-step planning.

Part A alone is sufficient for an initial architecture direction. Part B improves product, integration, security, capacity and production-readiness decisions. Enter **Unknown** instead of guessing; an unknown answer does not prevent initial analysis, but material unknowns remain explicit validation gates.

### Tip

To facilitate completion, conduct the questionnaire as an interview recorded in a Microsoft Teams session. With participant consent and the appropriate access permissions, use Work IQ to extract the relevant business and technical answers from the meeting transcript and populate the questionnaire. A facilitator should review the completed questionnaire with participants to confirm the extracted answers, assumptions, unknowns and validation owners before using it as architecture input.

## What you will find in this repository

- SKILL.md: version 1.10.0 skill definition and router. Normalizes a completed questionnaire or equivalent scenario document, enforces the low-complexity-first ladder, evidence-based escalation, capacity and scale validation, and consistent adoption architecture responses while loading reference files on demand.
- AI_Agent_Adoption_Strategy_Final_2.md: lightweight index that routes to thematic references and the 24 individual guide chapters.
- chapters/: complete guide content split for selective, on-demand loading and organized into five groups:
   - Strategy and Adoption: chapters 01-04 (executive overview, adoption strategy, tools and approaches).
   - Data and Agent Consumption: chapters 05-08 (Fabric consumption, agent access and usage examples).
   - Architecture and Operating Model: chapters 09-14 (integration, operating model, Microsoft architecture alignment, instructions and skills).
   - Advanced Agent Capabilities: chapters 15-17 (orchestration, memory and operational implementation).
   - Appendices: chapters 18-24 (code examples, templates, tool decision tree, OpenTelemetry, dataset curation and consolidated references).
- references/: thematically sliced content for on-demand loading:
   - references/01-llm-rag-ai-agent-fundamentals.md: existing/deterministic alternatives, LLM, RAG, AI Agent and Agentic AI; complexity spectrum and escalation decision guide.
   - references/02-reference-architecture-layers.md: conditional Microsoft IQ context capabilities, managed agent platforms, Agent Framework hosting boundaries and the layer overview. The Fabric data-platform specifications are split into on-demand sub-references: 02a (OneLake, Delta Lake, Shortcuts, SQL analytics endpoint), 02b (Medallion architecture) and 02c (Data Products, Purview + Entra governance and the raw-data-to-insight summary).
   - references/03-roi-ai-vs-man-hour.md: dimensionally consistent per-task AAI, period-level ROI, HITL cost and scope/realization multipliers.
   - references/04-governance-guard-rails-evaluators-hitl.md: guard rails, evaluators, Human-in-the-Loop, Agent ID and conditional Agent 365 coverage.
   - references/05-decision-framework-bxt.md: Microsoft AI Decision Framework (Intake Filter, BXT, 9 critical questions, Capability Model, mandatory complexity-escalation gate and technology selection by scenario).
   - references/06-pl-2338-2023-copilot-studio-foundry.md: current legislative-status analysis of PL 2338/2023 and conditional mapping of Microsoft controls to transparency, governance, risk, audit, human oversight and data protection; it does not assert legal compliance.
   - references/07-capacity-and-scale-assessment.md: demand model, product-specific licensing/quota/throughput checks, fit verdict, headroom, load validation and official Microsoft capacity references.

The Microsoft product, architecture, governance and regulatory sources behind references 01–06 were last rechecked on **2026-07-20**. Product lifecycle, licensing, regional availability, quotas and legal status remain point-in-time facts and must be revalidated for each production recommendation.
- doc/agent-project-specifications-example.md: starter example of a project specification document to accelerate onboarding before creating or customizing doc/agent-project-specifications.md.
- doc/business-architecture-questionnaire.md: business and technical discovery questionnaire that captures outcomes, current process, users, data, actions, risk, demand, economics, identity, integrations, runtime, networking, reliability, security, observability and delivery without asking stakeholders to choose a technology.
- doc/agent-project-specifications.md: implementation-ready scenario input template used when requirements have already been formalized.
- doc/recommendation-output.md: generated output artifact where the executive recommendation is persisted in markdown format.

> Note: AAI (AI Advantage Index) is the ratio between the human cost of the task and the total AI cost per task (AAI = Human Cost / AI Cost). AAI > 1 indicates that AI is financially advantageous (an AAI of 4.0 means the task via AI costs 1/4 of the same task done by a person); AAI = 1 is the break-even point; AAI < 1 indicates keeping human work. Not to be confused with VAT (Value Added Tax).
- Supplementary guides for dynamics and setup to facilitate collaboration and use in VS Code.

## Repository structure (diagram)

The diagram below shows how the files relate to each other. SKILL.md is the entry point (router); the lightweight index points to thematic references and individual chapters that are loaded on demand.

```mermaid
graph TD
    USER([User / Agent asks a question]) --> SKILL[SKILL.md<br/>Routing skill - entry point]
   SKILL --> CANON[AI_Agent_Adoption_Strategy_Final_2.md<br/>Lightweight chapter index]

    SKILL -. progressive disclosure .-> REF{{references/}}
    CANON -. pointers .-> REF
   CANON -. chapter selection .-> CHAPTERS{{chapters/}}

      REF --> R1[01-llm-rag-ai-agent-fundamentals.md<br/>Deterministic - LLM - RAG - Agent - Multi-agent]
      REF --> R2[02-reference-architecture-layers.md<br/>Work IQ - Foundry IQ - Fabric IQ - Web IQ - Fabric]
      REF --> R3[03-roi-ai-vs-man-hour.md<br/>ROI / AAI - HITL - scope]
      REF --> R4[04-governance-guard-rails-evaluators-hitl.md<br/>Guard Rails - Evaluators - HITL]
      REF --> R5[05-decision-framework-bxt.md<br/>BXT - escalation gate - technology selection]
      REF --> R6[06-pl-2338-2023-copilot-studio-foundry.md<br/>PL 2338 - transparency - governance - risk - audit]
      REF --> R7[07-capacity-and-scale-assessment.md<br/>Demand - quotas - throughput - fit verdict]

    SKILL --> README[README.md<br/>Repository overview]
   README --> BQ[doc/business-architecture-questionnaire.md<br/>Preferred scenario input template]
   README --> DOC[Equivalent scenario document<br/>Business and technical facts]
   README --> DOCEX[doc/agent-project-specifications-example.md<br/>Starter template/example]
   SKILL -. discovery context .-> BQ
   SKILL -. project context .-> DOC
   BQ --> DOC
   DOCEX --> DOC
   README --> PROMPT[Universal compact prompt<br/>complete recommendation]
   BQ --> PROMPT
   DOC --> PROMPT
   PROMPT --> OUTMD[doc/recommendation-output.md<br/>Markdown output]

    classDef entry fill:#0078D4,stroke:#004578,color:#fff;
    classDef canon fill:#107C10,stroke:#0B5A0B,color:#fff;
    classDef ref fill:#E6F2FA,stroke:#0078D4,color:#1a1a1a;
   classDef doc fill:#FFF4CE,stroke:#C19C00,color:#1a1a1a;
   classDef prompt fill:#EDE7F6,stroke:#5E35B1,color:#1a1a1a;
   classDef output fill:#E8F5E9,stroke:#2E7D32,color:#1a1a1a;
    class SKILL entry;
    class CANON canon;
   class R1,R2,R3,R4,R5,R6,R7,CHAPTERS ref;
   class BQ,DOC,DOCEX doc;
   class PROMPT prompt;
   class OUTMD output;
```

## How to navigate (decision flowchart)

Use this flow to choose which file to open based on your need.

```mermaid
flowchart TD
    START([What is your need?]) --> Q1{Do you just want<br/>the repo overview?}
    Q1 -- Yes --> README[Read README.md]
    Q1 -- No --> Q2{Will you ask AI<br/>for a recommendation?}

    Q2 -- Yes --> SKILL[Use SKILL.md<br/>as context/skill]
    Q2 -- No --> Q3{What topic do you<br/>need to explore further?}

   SKILL --> QDOC{What scenario document<br/>is available?}
   QDOC -- Questionnaire --> BQ[Completed business and technical<br/>architecture questionnaire]
   QDOC -- Existing document --> DOC[Proposal, discovery, requirements<br/>or technical specification]
   BQ --> QOUT
   DOC --> QOUT
   BQ -. after direction is approved .-> DOCNEW[Convert into<br/>agent-project-specifications.md]
   QOUT{Do you want to save<br/>the response as Markdown?}
   DOCNEW --> QOUT
   QOUT -- Yes --> PROMPT[Use the default<br/>README prompt]
   PROMPT --> OUTMD[doc/recommendation-output.md]
   QOUT -- No --> Q3
   OUTMD --> Q3

    Q3 -- Fundamentals<br/>LLM/RAG/Agents --> R1[references/01-llm-rag-ai-agent-fundamentals.md]
    Q3 -- Layered<br/>Architecture --> R2[references/02-reference-architecture-layers.md]
    Q3 -- Financial<br/>Justification / ROI --> R3[references/03-roi-ai-vs-man-hour.md]
    Q3 -- Governance<br/>and Security --> R4[references/04-governance-guard-rails-evaluators-hitl.md]
    Q3 -- Microsoft<br/>Technology Selection --> R5[references/05-decision-framework-bxt.md]
   Q3 -- Regulatory Analysis<br/>PL 2338/2023 --> R6[references/06-pl-2338-2023-copilot-studio-foundry.md]
   Q3 -- Capacity and Scale<br/>Fit Assessment --> R7[references/07-capacity-and-scale-assessment.md]
   Q3 -- Other sections --> CANON[Open the lightweight index<br/>and select one chapter group]
   CANON --> C1[Strategy and Adoption<br/>chapters 01-04]
   CANON --> C2[Data and Agent Consumption<br/>chapters 05-08]
   CANON --> C3[Architecture and Operating Model<br/>chapters 09-14]
   CANON --> C4[Advanced Agent Capabilities<br/>chapters 15-17]
   CANON --> C5[Appendices<br/>chapters 18-24]

    R1 --> END([Apply to your use case])
    R2 --> END
    R3 --> END
    R4 --> END
    R5 --> END
   R6 --> END
   R7 --> END
   C1 --> END
   C2 --> END
   C3 --> END
   C4 --> END
   C5 --> END
    README --> END
```

## Target audience

- Anyone who needs structured inputs for an AI architecture recommendation, including people without architecture expertise.
- Technology and business leaders.
- Enterprise architects, data architects and platform teams.
- Governance, security and compliance teams.
- Squads starting or scaling AI agents.

## Universal compact prompt

Attach `SKILL.md` and one scenario input document. The scenario document can be a completed copy of `doc/business-architecture-questionnaire.md` or any proposal, discovery note, requirements document, workshop summary or technical specification containing the available business and technical facts. It does not need to use the questionnaire's headings or order.

Use the same prompt for every supported client:

> Apply hubsp-ai-skill to the attached scenario document. Recommend the simplest viable Microsoft architecture and save the complete recommendation to `doc/recommendation-output.md`. Treat missing decision-critical information as explicit assumptions or validation gates; do not invent facts.

The skill supplies the architecture ladder, evidence-based escalation, target output structure, diagrams, capacity fit, governance, applicable regulation, ROI/AAI, roadmap, KPIs, risks and official-source requirements. Keeping those rules in `SKILL.md` avoids prompt duplication and produces consistent results across clients.



### Exemplo adicional de prompt: análise ilustrada da PL 2338/2023

Use este exemplo quando o cenário envolver uma organização brasileira, uma operação realizada no Brasil ou uma população impactada no Brasil, e quando o entregável precisar explicar visualmente a solução proposta.
Anexe o arquivo `SKILL.md`, o documento do cenário e `references/06-pl-2338-2023-copilot-studio-foundry.md`.

> Aplique o hubsp-ai-skill ao cenário anexado e analise a aplicabilidade e as implicações arquiteturais do PL 2338/2023. Recomende a arquitetura Microsoft mais simples viável e salve a análise completa em `doc/recommendation-output.md`. No documento:
>
> 1. Revalide a situação legislativa atual utilizando fontes oficiais brasileiras e informe a data da verificação. Não descreva o projeto de lei como lei em vigor, a menos que uma fonte oficial confirme isso.
> 2. Separe a interpretação jurídica, as capacidades documentadas da Microsoft, as premissas do cenário, as decisões de arquitetura e as evidências que ainda requerem validação. Não afirme que um produto da Microsoft garante automaticamente conformidade legal.
> 3. Compare produto/SaaS existente, automação determinística, LLM direto, RAG, Agente de IA único e arquitetura multiagente ou híbrida, nessa ordem. Pare na primeira opção que atenda de forma confiável aos requisitos do cenário.
> 4. Inclua um diagrama Mermaid legível da arquitetura-alvo mostrando usuários, canais, o runtime selecionado, dados governados, integrações, identidade, guard rails, avaliadores, monitoramento, auditoria e HITL (Human-in-the-Loop). Mostre separadamente os componentes adiados para além do escopo do piloto.
> 5. Inclua fluxogramas Mermaid para o fluxo de solicitação e decisão, o fluxo de controle e aprovação, e o roadmap por ondas (waves). Marque explicitamente os caminhos de bloqueio, escalonamento, revisão humana e incidentes.
> 6. Mapeie os eixos relevantes do PL 2338/2023, incluindo transparência, avaliação de risco, supervisão humana, não discriminação, rastreabilidade, auditabilidade, proteção de dados e responsabilização, para controles de arquitetura, responsáveis, evidências, limitações e lacunas de implementação.
> 7. Forneça matrizes de justificativa técnica dos componentes e aderência de capacidade (capacity fit), ondas de implementação, KPIs, riscos e mitigações, além de um gate de validação jurídica antes da entrada em produção.
> 8. Cite a fonte jurídica oficial e a fonte oficial da Microsoft ao lado de cada afirmação material, incluindo título da fonte, URL e data de acesso. Trate informações críticas para decisão que estejam ausentes como premissas explícitas ou gates de validação; não invente fatos.


Why the prompt is structured this way:

| Prompt element | Purpose |
| --- | --- |
| Scenario and PL 2338/2023 applicability | Prevents a generic regulatory summary and ties the analysis to the affected organization, people, decisions, data and risk level. |
| Legislative-status revalidation | PL 2338/2023 is still subject to legislative change; the output must present a dated, point-in-time assessment. |
| Evidence separation | Distinguishes legal interpretation from product documentation, design choices, assumptions and measured results. |
| Low-complexity-first comparison | Prevents regulation from being used as an unsupported reason to adopt agents, multiple runtimes or a larger Microsoft product stack. |
| Target-architecture diagram | Shows component boundaries and how the selected runtime connects to governed data and cross-cutting controls. |
| Decision and control flowcharts | Make normal, blocked, escalated, HITL and incident paths understandable to executive, legal, security and engineering reviewers. |
| Regulatory control mapping | Converts broad legal axes into implementable controls, named owners, required evidence and visible gaps. |
| Legal-review gate | Makes clear that technical controls support compliance work but do not replace counsel or the organization's accountability. |
| Sources beside claims | Enables reviewers to verify legal status, product capability and design dependencies without relying only on a final bibliography. |

The resulting document should use diagrams to clarify decisions, not to decorate the output. Every architecture component must have a matching technical-justification row, and every regulatory control shown in a flowchart must identify an owner, evidence source and failure or escalation path.

Questionnaire-based architecture flow:

1. Any individual or team can start by completing the 15 questions in Part A of `doc/business-architecture-questionnaire.md`. When technical participants are available, use the 15 questions in Part B to strengthen feasibility and production-readiness inputs. Respondents may answer **Unknown** and name a validation owner instead of guessing.
2. Attach the completed questionnaire with `SKILL.md`, or attach another document containing equivalent business and technical facts.
3. Convert the approved recommendation and unresolved technical items into `doc/agent-project-specifications.md` before implementation planning.

Tip: to use `SKILL.md` as a reusable skill in the official VS Code format, copy it (or create a link) to a folder such as `.github/skills/hubsp-ai-skill/` or `~/.copilot/skills/hubsp-ai-skill/`. In this repository, the file at the root acts as the **canonical source/router** for direct reference in prompts, while the formal skill installation should follow the lowercase folder convention.

## Setup

To get started with hubsp-ai-skill, select the platform or tool that matches your workflow. Detailed setup instructions for each platform are available in [doc/setup-guide.md](doc/setup-guide.md):

- **[Visual Studio Code](doc/setup-guide.md#how-to-use-in-visual-studio-code)**: Integrate with GitHub Copilot Chat and the Microsoft Learn MCP Server for real-time documentation access.
- **[Claude Desktop](doc/setup-guide.md#how-to-use-in-claude-desktop)**: Upload the skill as a custom ZIP package for use in Claude's skill library.
- **[Microsoft Scout](doc/setup-guide.md#how-to-use-in-microsoft-scout)**: Install the skill in Scout's global skills directory for local workspace integration.
- **[GitHub Copilot App](doc/setup-guide.md#how-to-use-in-the-github-copilot-app)**: Open the repository directly in the GitHub Copilot App and attach scenario documents.

Each setup option includes prerequisites, step-by-step installation, and recommended workflows for getting the most out of the skill.

## Note on project documents (`doc` folder)

To standardize skill usage across any channel, provide one scenario input document containing the available business and technical facts. Use a completed `doc/business-architecture-questionnaire.md`, or reuse an existing proposal, discovery note, requirements document, workshop summary or technical specification. Do not rewrite a useful document only to match the questionnaire structure.

Recommended path example:

`doc/agent-project-specifications.md`

Preferred discovery template:

`doc/business-architecture-questionnaire.md` (complete the known answers and attach it alongside `SKILL.md`).

Implementation-ready template:

`doc/agent-project-specifications.md` (use when requirements have already been formalized).

Recommended minimum document structure (suggested order):

1. Business context and agent objective.
2. Current process, existing products/SaaS capabilities and deterministic automation already available.
3. Functional scope (what the AI solution does and does not do).
4. User profiles, journeys and channels.
5. Non-functional requirements (SLA, latency, availability, scale).
6. Data, integrations, required actions and autonomy (sources, APIs, systems, data classification).
7. Governance and security (guard rails, compliance, audit, HITL).
8. Success criteria and KPIs.
9. Constraints, risks and assumptions.
10. Wave-based roadmap and measurable escalation triggers (pilot, expansion, scale).

Supported file extensions (recommended practice):

- `.md`: best performance and highest reading predictability by the agent (recommended).
- `.txt`: high performance, without formatting features.
- `.pdf`: supported, but may lose structure in tables/diagrams and vary depending on text extraction.
- `.docx`: supported, good for executive authoring, with possible interpretation variation in complex layouts.

Best overall performance for skill analysis: **`.md`** (plain text, clear sections and objective headings).

## Default reusable prompt

After attaching `SKILL.md` and one scenario input document, use:

> Apply hubsp-ai-skill to the attached scenario document. Recommend the simplest viable Microsoft architecture and save the complete recommendation to `doc/recommendation-output.md`. Treat missing decision-critical information as explicit assumptions or validation gates; do not invent facts.

Variation for GitHub Copilot CLI:

> Read `SKILL.md` and the supplied scenario document. Apply hubsp-ai-skill, recommend the simplest viable Microsoft architecture, and save the complete recommendation to `doc/recommendation-output.md`. Treat missing decision-critical information as explicit assumptions or validation gates; do not invent facts.

## Knowledge base roadmap with Obsidian

In the next releases, this project will use [Obsidian](https://obsidian.md/) to manage the knowledge base layer that supports these skills. Obsidian is a knowledge-management application that organizes notes as local Markdown files inside a folder called a **vault**. Because the content remains in standard `.md` files, it can continue to be versioned with Git, reviewed in VS Code and loaded by AI tools without requiring a proprietary storage format.

Obsidian connects notes through internal links, tags and metadata. These relationships can be explored through backlinks and a visual graph, making it easier to navigate related architecture guidance, references, chapters and reusable skill instructions. In practical terms, contributors edit the same repository content while Obsidian provides an additional interface for discovering relationships, maintaining structure and identifying knowledge gaps.

The planned integration will make Obsidian the authoring and knowledge-management layer, not a runtime dependency for using the skills. The existing Markdown files and progressive-disclosure model will remain the portable source of knowledge consumed by GitHub Copilot, Claude and other supported clients. Adoption details, vault conventions and migration guidance will be documented as this capability is introduced in future releases.
