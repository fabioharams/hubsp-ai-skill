# hubsp-ai-skill

## What is this project

This repository organizes a practical knowledge base to guide the corporate adoption of AI agents in the Microsoft ecosystem. The focus is on target architecture decisions that combine Microsoft IQ context workloads (Work IQ, Foundry IQ, Fabric IQ and Web IQ), explicit agent runtimes, governed data, security, guard rails, evaluators and operations at scale.

The project was structured to serve as both an executive and technical reference: it helps business, architecture, data and security teams align on a common vision for planning, piloting and expanding agentic AI initiatives with lower risk and greater value predictability.

## Objective

- Define a reference architecture for AI agents in a corporate context.
- Standardize recommendations focused on governance, compliance and observability.
- Support a wave-based roadmap (pilot, expansion and scale) with clear criteria.
- Make trade-offs explicit across cost, risk, speed and complexity.

## What you will find in this repository

- SKILL.md: single skill definition (router) that guides consistent responses in an adoption architecture context. Points to reference files on demand (progressive disclosure).
- AI_Agent_Adoption_Strategy_Final_2.md: lightweight index that routes to thematic references and the 24 individual guide chapters.
- chapters/: complete guide content split for selective, on-demand loading and organized into five groups:
   - Strategy and Adoption: chapters 01-04 (executive overview, adoption strategy, tools and approaches).
   - Data and Agent Consumption: chapters 05-08 (Fabric consumption, agent access and usage examples).
   - Architecture and Operating Model: chapters 09-14 (integration, operating model, Microsoft architecture alignment, instructions and skills).
   - Advanced Agent Capabilities: chapters 15-17 (orchestration, memory and operational implementation).
   - Appendices: chapters 18-24 (code examples, templates, tool decision tree, OpenTelemetry, dataset curation and consolidated references).
- section_3_2.txt: extracted plain-text section used as a lightweight source for quick copy, review and prompt experiments without markdown formatting overhead.
- references/: thematically sliced content for on-demand loading:
   - references/01-llm-rag-ai-agent-fundamentals.md: LLM vs RAG vs AI Agent vs Agentic AI; complexity spectrum and decision guide.
   - references/02-reference-architecture-layers.md: Microsoft IQ context workloads, agent runtimes, Microsoft Fabric and technical specifications per layer.
   - references/03-roi-ai-vs-man-hour.md: ROI/AAI model, HITL and scope multiplier.
   - references/04-governance-guard-rails-evaluators-hitl.md: Guard Rails, Evaluators and Human-in-the-Loop.
   - references/05-decision-framework-bxt.md: Microsoft AI Decision Framework (Intake Filter, BXT, 9 critical questions, Capability Model and technology selection by scenario).
   - references/06-pl-2338-2023-copilot-studio-foundry.md: analysis of PL 2338/2023 and how Microsoft Copilot Studio, Microsoft Foundry and Purview address the axes of transparency, governance, risk, audit, human oversight and data protection with official sources.
- doc/agent-project-specifications-example.md: starter example of a project specification document to accelerate onboarding before creating or customizing doc/agent-project-specifications.md.
- doc/agent-project-specifications.md: working specification used as primary project input in recommendation prompts.
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

      REF --> R1[01-llm-rag-ai-agent-fundamentals.md<br/>LLM vs RAG vs AI Agent vs Agentic AI]
      REF --> R2[02-reference-architecture-layers.md<br/>Work IQ - Foundry IQ - Fabric IQ - Web IQ - Fabric]
      REF --> R3[03-roi-ai-vs-man-hour.md<br/>ROI / AAI - HITL - scope]
      REF --> R4[04-governance-guard-rails-evaluators-hitl.md<br/>Guard Rails - Evaluators - HITL]
      REF --> R5[05-decision-framework-bxt.md<br/>BXT - 9 questions - Capability Model]
      REF --> R6[06-pl-2338-2023-copilot-studio-foundry.md<br/>PL 2338 - transparency - governance - risk - audit]

    SKILL --> README[README.md<br/>Repository overview]
   README --> DOC[doc/agent-project-specifications.md<br/>Project specifications and requirements]
   README --> DOCEX[doc/agent-project-specifications-example.md<br/>Starter template/example]
   SKILL -. project context .-> DOC
   DOCEX --> DOC
   README --> PROMPT[Default reusable prompt<br/>diagrammed response generation]
   DOC --> PROMPT
   PROMPT --> OUTMD[doc/recommendation-output.md<br/>Markdown output]
   CHAPTERS --> TXT[section_3_2.txt<br/>Plain-text extracted section]

    classDef entry fill:#0078D4,stroke:#004578,color:#fff;
    classDef canon fill:#107C10,stroke:#0B5A0B,color:#fff;
    classDef ref fill:#E6F2FA,stroke:#0078D4,color:#1a1a1a;
   classDef doc fill:#FFF4CE,stroke:#C19C00,color:#1a1a1a;
   classDef prompt fill:#EDE7F6,stroke:#5E35B1,color:#1a1a1a;
   classDef output fill:#E8F5E9,stroke:#2E7D32,color:#1a1a1a;
   classDef artifact fill:#FFF3E0,stroke:#EF6C00,color:#1a1a1a;
    class SKILL entry;
    class CANON canon;
   class R1,R2,R3,R4,R5,R6,CHAPTERS ref;
   class DOC,DOCEX doc;
   class PROMPT prompt;
   class OUTMD output;
   class TXT artifact;
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

   SKILL --> QDOC{Does a document<br/>already exist in doc/?}
   QDOC -- Yes --> DOC[doc/agent-project-specifications.md]
   QDOC -- No --> DOCNEW[Create doc/agent-project-specifications.md]
   DOC --> QOUT{Do you want to save<br/>the response as Markdown?}
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
   C1 --> END
   C2 --> END
   C3 --> END
   C4 --> END
   C5 --> END
    README --> END
```

## Target audience

- Technology and business leaders.
- Enterprise architects, data architects and platform teams.
- Governance, security and compliance teams.
- Squads starting or scaling AI agents.

## How to use in Visual Studio Code

Prerequisites: VS Code, the GitHub Copilot Chat extension and an active GitHub Copilot subscription.

1. Clone and open the repository:

   ```bash
   git clone https://github.com/<your-org>/hubsp-ai-skill.git
   code hubsp-ai-skill
   ```

2. Open Copilot Chat (chat icon in the sidebar or `Ctrl+Alt+I` / `Cmd+Alt+I`) and use Agent mode.
3. The `.github/copilot-instructions.md` file is automatically loaded as workspace context, ensuring the executive response format is applied consistently.
4. Bring a file into the conversation context in one of these ways:
   - Type `#` and select the file (e.g., `#SKILL.md`).
   - Drag the file from the Explorer into the chat panel.
   - Open the file in the editor and reference it with `#file`.
5. Recommended flow: start with `SKILL.md` and let the agent load one file from `references/` or `chapters/` on demand, based on the topic of the question. Do not attach the complete `chapters/` folder.

For topics beyond the six curated references, open `AI_Agent_Adoption_Strategy_Final_2.md`, choose the relevant chapter group and load only the chapter or chapters required by the request. This progressive-disclosure approach keeps the context focused and avoids loading the full knowledge base.

Example prompt:

> **Applicability disclaimer:** PL 2338/2023 applies only to Brazilian clients and companies. For scenarios outside Brazil, omit the PL 2338/2023 analysis from the prompt or explicitly instruct the agent to state that PL 2338/2023 is not applicable to the scenario being analyzed.

> Using #SKILL.md, recommend the target architecture for a support copilot with governed data in Fabric.

Example with project specifications document:

> **Applicability disclaimer:** PL 2338/2023 applies only to Brazilian clients and companies. For scenarios outside Brazil, omit the PL 2338/2023 analysis from the prompt or explicitly instruct the agent to state that PL 2338/2023 is not applicable to the scenario being analyzed.

> Using #SKILL.md and #doc/agent-project-specifications.md, generate an executive recommendation in full format: (1) medium executive summary (1-2 paragraphs) with at least 1 Mermaid diagram or flowchart to explain the recommended decision, (2) recommended architectural pattern (LLM/RAG/AI Agent/Agentic AI) with detailed justifications, official Microsoft links and at least 1 Mermaid diagram or flowchart to explain the choice, (3) target architecture with Microsoft IQ context workloads (Work IQ, Foundry IQ, Fabric IQ and Web IQ when applicable), an explicit agent runtime and Microsoft Fabric, with detailed explanation and 2 mandatory Mermaid diagrams (architecture and decision flowchart), (4) governance and security with guard rails, evaluators, PL 2338/2023 analysis and explanation of how the tools and services selected in the architecture address the axes of transparency, governance, risk, audit, human oversight and data protection with official sources, and at least 1 Mermaid diagram or flowchart, (5) phased deployment plan with per-phase detail (objective, scope, integrations, entry/exit criteria, target KPI and dominant risk) and at least 1 Mermaid diagram or flowchart, (6) ROI/AAI assumptions with at least 1 Mermaid diagram or flowchart to explain the financial logic, (7) success KPIs with at least 1 Mermaid diagram or flowchart, and (8) risks and mitigations with clarity, official Microsoft links and at least 1 Mermaid diagram or flowchart. The response must be delivered as a new markdown document called doc/recommendation-output.md.

Tip: to use `SKILL.md` as a reusable skill in the official VS Code format, copy it (or create a link) to a folder such as `.github/skills/hubsp-ai-skill/` or `~/.copilot/skills/hubsp-ai-skill/`. In this repository, the file at the root acts as the **canonical source/router** for direct reference in prompts, while the formal skill installation should follow the lowercase folder convention.

## Note on project documents (`doc` folder)

To standardize skill usage across any channel (VS Code, GitHub Copilot App and CLI), create a `doc/` folder at the repository root and add to it a document with the project's specifications and requirements to be analyzed.

Recommended path example:

`doc/agent-project-specifications.md`

Ready-to-use template:

`doc/agent-project-specifications.md` (fill in and attach this file to the chat alongside `SKILL.md`).

Recommended minimum document structure (suggested order):

1. Business context and agent objective.
2. Functional scope (what the agent does and does not do).
3. User profiles, journeys and channels.
4. Non-functional requirements (SLA, latency, availability, scale).
5. Data and integrations (sources, APIs, systems, data classification).
6. Governance and security (guard rails, compliance, audit, HITL).
7. Success criteria and KPIs.
8. Constraints, risks and assumptions.
9. Wave-based roadmap (pilot, expansion, scale).

Supported file extensions (recommended practice):

- `.md`: best performance and highest reading predictability by the agent (recommended).
- `.txt`: high performance, without formatting features.
- `.pdf`: supported, but may lose structure in tables/diagrams and vary depending on text extraction.
- `.docx`: supported, good for executive authoring, with possible interpretation variation in complex layouts.

Best overall performance for skill analysis: **`.md`** (plain text, clear sections and objective headings).

## Default reusable prompt (generate a diagrammed Markdown file)

Use this prompt in any project with a document at `doc/agent-project-specifications.md`:

> **Applicability disclaimer:** PL 2338/2023 applies only to Brazilian clients and companies. For scenarios outside Brazil, omit the PL 2338/2023 analysis from the prompt or explicitly instruct the agent to state that PL 2338/2023 is not applicable to the scenario being analyzed.

> Using #SKILL.md and #doc/agent-project-specifications.md, generate an executive recommendation in full format: (1) medium executive summary (1-2 paragraphs) with at least 1 Mermaid diagram or flowchart to explain the recommended decision, (2) recommended architectural pattern (LLM/RAG/AI Agent/Agentic AI) with detailed justifications, official Microsoft links and at least 1 Mermaid diagram or flowchart to explain the choice, (3) target architecture with Microsoft IQ context workloads (Work IQ, Foundry IQ, Fabric IQ and Web IQ when applicable), an explicit agent runtime and Microsoft Fabric, with detailed explanation and 2 mandatory Mermaid diagrams (architecture and decision flowchart), (4) governance and security with guard rails, evaluators, PL 2338/2023 analysis and explanation of how the tools and services selected in the architecture address the axes of transparency, governance, risk, audit, human oversight and data protection with official sources, and at least 1 Mermaid diagram or flowchart, (5) phased deployment plan with per-phase detail (objective, scope, integrations, entry/exit criteria, target KPI and dominant risk) and at least 1 Mermaid diagram or flowchart, (6) ROI/AAI assumptions with at least 1 Mermaid diagram or flowchart to explain the financial logic, (7) success KPIs with at least 1 Mermaid diagram or flowchart, and (8) risks and mitigations with clarity, official Microsoft links and at least 1 Mermaid diagram or flowchart. The response must be delivered as a new markdown document called doc/recommendation-output.md.

Variation for GitHub Copilot CLI:

> **Applicability disclaimer:** PL 2338/2023 applies only to Brazilian clients and companies. For scenarios outside Brazil, omit the PL 2338/2023 analysis from the prompt or explicitly instruct the agent to state that PL 2338/2023 is not applicable to the scenario being analyzed.

> Read SKILL.md and doc/agent-project-specifications.md and generate an executive recommendation in advanced format: medium executive summary with Mermaid diagram or flowchart; architectural pattern with detailed justifications, Microsoft sources and Mermaid diagram or flowchart; Microsoft IQ context workloads plus an explicit agent runtime and Microsoft Fabric, with a Mermaid architecture diagram and Mermaid decision flowchart; governance and security with PL 2338/2023 analysis, explanation of how the tools and services selected in the architecture address the axes of transparency, governance, risk, audit, human oversight and data protection with official sources, and Mermaid diagram or flowchart; detailed phased plan with Mermaid diagram or flowchart; ROI/AAI assumptions with Mermaid diagram or flowchart; KPIs with Mermaid diagram or flowchart; risks and mitigations with official Microsoft links and Mermaid diagram or flowchart. The response must be delivered as a new markdown document called doc/recommendation-output.md.

## How to use in the GitHub Copilot App

Prerequisites: GitHub Copilot app with repository access and an active GitHub Copilot subscription.

1. Open this repository in the app as a workspace/project.
2. Start a chat in Agent mode.
3. Attach `SKILL.md` to the context (or use `#SKILL.md`) to apply the response format rules.
4. When depth is needed, also attach the relevant file from `references/` or one selected file from `chapters/` based on the topic. Avoid attaching all chapters at once.
5. Ask the question with business context and decision objective.
