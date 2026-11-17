## 🔗 11. Full Integration (Final Architecture)

### 🎯 How the layers connect

This is a full-stack reference for cases in which every shown capability has been independently justified. It is not the default starting architecture. Simpler scenarios can stop at an existing SaaS capability, deterministic automation, direct LLM or RAG and omit any unnecessary IQ capability, agent platform or Fabric dependency.

1. **Copilot, Teams and business apps** receive user intent through familiar channels.
2. **Work IQ**, when required, supplies Microsoft 365 work context such as emails, chats, files, meetings and workflows.
3. **Foundry IQ**, when required, supplies permission-aware enterprise knowledge through knowledge bases and agentic retrieval.
4. **Fabric IQ**, when required, supplies corporate semantic context such as metrics, entities and business rules.
5. **Web IQ**, when available and required, supplements grounding with current external evidence.
6. **Microsoft Foundry Agent Service or Copilot Studio** provides the managed agent platform. An application built with **Microsoft Agent Framework** requires explicit hosting unless deployed as a Foundry hosted agent.
7. **Microsoft Fabric**, when analytical consolidation or semantic reuse is required, delivers governed analytical data.
8. **Guard Rails** and **Evaluators** act cross-cuttingly: one controls risk and access, the other measures quality and feeds continuous improvement.

### 🧩 Consolidated diagram (Mermaid)

```mermaid
flowchart TD
    U[Usuario\nCopilot Teams Apps] --> S{Opcao mais simples\natende agora}
    S -->|SaaS automacao LLM ou RAG| R[Resposta ao usuario]
    S -->|Agente necessario| A[Plataforma gerenciada\nou app hospedado]
    Q[Work IQ\nse necessario] -.-> A
    K[Foundry IQ\nse necessario] -.-> A
    B[Fabric IQ\nse necessario] -.-> A
    W[Web IQ\nendpoint aprovado se necessario] -.-> A
    B -.-> C[Microsoft Fabric\nse consolidacao analitica exigida]
    C -.-> B
    A --> R

    G[Guard Rails\nidentidade acesso seguranca] --> A
    G --> B
    G --> C
    G --> W

    E[Evaluators\nqualidade seguranca drift] --> A
    E --> M[Feedback de melhoria\nprompt tools dados policies]
    M --> A
```

### 📌 Executive reading of the integration

- **Value**: AI-assisted decisions based on reliable corporate data and up-to-date external context.
- **Control**: security and compliance applied throughout the entire response cycle.
- **Evolution**: evaluators and observability convert usage into operational learning.

### 📣 Context update — Foundry and Foundry IQ

- **Foundry platform:** the new Microsoft Foundry portal is GA for defined core scenarios. Core agents, models, tools, toolboxes, evaluations and quota are GA, while monitoring, agent guard rails, memory and parts of Operate remain preview. Do not infer blanket GA from the platform milestone.
- **Foundry Agent Service:** core and hosted agents are GA. The initial hosted-agent preview backend reached end of support on **August 20, 2026** and requires redeployment to the current hosting model.
- **Foundry IQ mixed lifecycle:** Azure AI Search API `2026-04-01` is GA but provides a narrower retrieval contract. The current `2026-08-01-preview` API is required for answer synthesis, non-minimal reasoning and multi-turn messages; portal access remains preview.
- **MAI lifecycle, checked November 17:** MAI-Thinking-1 and Foundry MAI-Image-2.6 variants remain preview; MAI Image 2.7 launched as an editing preview. Azure Speech now documents MAI-Voice-2.1 variants in preview. Batch MAI-Transcribe-2 lacks explicit GA confirmation in its current guide; the Streaming variant is explicitly preview. See the [model-level evidence and conflicts](../PRODUCT_LIFECYCLE_AUDIT.md#models-cited-by-the-guide).
- **Workflow retirement:** Foundry Workflows remains preview and is scheduled for retirement on **December 1, 2026**. Use Microsoft Agent Framework for new workflow orchestration.
- **Critical distinction for target architecture:** the Foundry and Azure portals still expose agentic retrieval capabilities with components in preview; therefore, production decisions must explicitly separate GA dependencies from preview dependencies.
- **Executive implication:** use GA APIs in production where their contract meets the requirement. Treat preview dependencies as exception-based pilots; governance controls do not change preview support or SLA status.
- **Fabric boundary:** Fabric data agent core and the Power BI-focused Fabric IQ MCP server are GA. The separate Foundry Fabric IQ (OneLake Catalog) integration remains preview; the [legacy data-agent tool](https://learn.microsoft.com/fabric/data-science/data-agent-foundry) became unsupported on **November 6, 2026**.
- **Governance transition:** [Purview Data Governance](https://learn.microsoft.com/purview/data-governance-overview) is retiring, with support ending **November 12, 2027**. Purview Data Security and Compliance continue; assess OneLake catalog for new Fabric governance requirements.

### 🧪 Context update — Microsoft Build 2026 (ASSERT and ACS)

- **ASSERT (open-source evaluation):** Microsoft Responsible AI released ASSERT on **June 2, 2026** as an MIT-licensed framework for converting natural-language behavior requirements into executable evaluations and repeatable regression tests. It uses tagged open-source releases rather than a commercial GA/preview lifecycle. Teams can integrate it into CI/CD, but it is not a managed continuous-monitoring service.
- **Agent Control Specification (ACS):** the upstream policy runtime has prerelease packages, currently documented as `0.4.0-beta.1`. ACS returns policy decisions; the host enforces them. The separate Agent Governance Toolkit is versioned MIT open source; its current changelog removes the commercial **public preview** label as inapplicable. This does not constitute a managed-service GA announcement.
- **Direct architectural value:** ASSERT reinforces the evaluators layer (continuous measurement and validation) and ACS reinforces guard rails (runtime enforcement), increasing auditability and operational consistency.
- **Recommended use in this guide:** treat ASSERT as a policy-driven evaluation mechanism in the continuous improvement cycle and ACS as the technical contract for controls in the agent runtime.
- **Acronym note:** in this document, **ACS** stands for **Agent Control Specification**. Not to be confused with **Azure ACS (Access Control Services)**, a legacy technology already retired in the SharePoint Online context.

**Sources:**
- [What is Microsoft Foundry?](https://learn.microsoft.com/azure/foundry/what-is-foundry)
- [Microsoft Foundry portal general availability overview](https://learn.microsoft.com/azure/foundry/concepts/general-availability)
- [What is Foundry IQ?](https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq)
- [Agentic retrieval overview](https://learn.microsoft.com/azure/search/agentic-retrieval-overview)
- [Migrate agentic retrieval code to the latest version](https://learn.microsoft.com/azure/search/agentic-retrieval-how-to-migrate)
- [Migrate hosted agents to the latest version](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate-hosted-agent-preview)
- [ASSERT announcement](https://commandline.microsoft.com/assert-written-intent-executable-evals/) and [official repository](https://github.com/responsibleai/ASSERT)
- [Agent Control Specification announcement](https://commandline.microsoft.com/agent-control-specification-runtime-governance/) and [official toolkit](https://github.com/microsoft/agent-governance-toolkit)
- [Current ACS runtime and contract](https://github.com/responsibleai/agent-control-spec)
- [Toolkit lifecycle-label correction](https://github.com/microsoft/agent-governance-toolkit/blob/main/CHANGELOG.md)
- [Preview Foundry Fabric IQ integration](https://learn.microsoft.com/fabric/data-science/data-agent-foundry-fabric-iq) and [GA Fabric IQ MCP server](https://learn.microsoft.com/fabric/iq/connectors/fabric-iq-mcp)

---

