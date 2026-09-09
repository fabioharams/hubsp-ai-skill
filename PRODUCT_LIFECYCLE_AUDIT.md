# Microsoft Product and Technology Lifecycle Audit

> Status date: **2026-09-09**. This register covers the lifecycle-sensitive Microsoft products, services, models, APIs, frameworks and open-source initiatives used by this repository. It uses official Microsoft Learn, release communication, product blog and Microsoft-owned GitHub sources.

## Executive verdict

The repository's target architecture remains directionally current, but the July 2026 lifecycle snapshot was no longer sufficient for production selection. The main corrections are:

- Work IQ must be scoped by surface: the Work IQ API is GA, while Work IQ in Copilot Studio remains preview.
- Microsoft Foundry and Foundry Agent Service have GA core experiences, but Foundry IQ portal access, monitoring, agent guard rails, memory and several integrations remain preview.
- Fabric IQ is still a preview workload containing both GA and preview items. Plan reached GA in July 2026, while Ontology and Graph remain preview.
- The MAI portfolio changed after Build 2026. New coding, image and transcription releases supersede the July model snapshot.
- Microsoft Entra Agent ID has a GA platform foundation, but the broader product documentation and individual security or creation capabilities still carry mixed lifecycle labels.
- ASSERT is open source and versioned; it does not have a Microsoft commercial GA/preview status. ACS is delivered through the Agent Governance Toolkit, which remains public preview.

No preview dependency should be approved for a critical production path solely because its parent platform is GA.

## Current lifecycle register

| Product or capability | Status on 2026-09-09 | Release or transition reflected | Decision note | Official evidence |
| --- | --- | --- | --- | --- |
| Microsoft 365 Copilot | GA product; individual app, model and agent features vary | Commercial release began in November 2023 | Validate the exact feature, tenant, cloud and license rather than relying on the product-level status | [Microsoft 365 Copilot release notes archive](https://learn.microsoft.com/microsoft-365/copilot/release-notes-archive#november-2023) |
| Microsoft Copilot Studio | GA platform with a mixed feature lifecycle | Feature dates are maintained individually | Work IQ, computer use and other named capabilities can remain preview even when the platform is production-supported | [What's new in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/whats-new) |
| Microsoft Fabric | GA platform with feature-level GA and preview states | Platform GA in November 2023; current features continue to graduate independently | OneLake, Lakehouse, Warehouse and each connector or workload must be checked separately | [What's new in Microsoft Fabric](https://learn.microsoft.com/fabric/fundamentals/whats-new) |
| Microsoft Foundry portal | GA for defined core scenarios; mixed feature lifecycle | Current GA scope documented in 2026 | Core agents, models, tools, toolboxes, evaluations and quota are GA; monitoring, agent guard rails, memory and parts of Operate remain preview | [Foundry portal GA overview](https://learn.microsoft.com/azure/foundry/concepts/general-availability) |
| Microsoft Foundry Agent Service | Core service and hosted agents GA; individual tools and integrations vary | Agent Service GA in May 2025; old hosted-agent preview backend support ended **August 20, 2026** | Do not reuse the initial preview hosting packages or assume every integration is GA | [Agent Service what's new](https://learn.microsoft.com/azure/foundry-classic/agents/whats-new#may-2025), [hosted-agent migration](https://learn.microsoft.com/azure/foundry/agents/how-to/migrate-hosted-agent-preview) |
| Work IQ | Mixed by surface | Work IQ API GA on **June 16, 2026** | The Copilot Studio integration is still preview; confirm billing, permissions and the exact API or MCP surface | [June 2026 announcement](https://learn.microsoft.com/partner-center/announcements/2026-june#work-iq-api-and-consumptive-pricing-update), [Work IQ in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/add-work-iq) |
| Foundry IQ / Azure AI Search agentic retrieval | Partial GA | Stable REST API `2026-04-01`; latest documented preview REST API `2026-08-01-preview` | The stable API supports a narrower contract. Answer synthesis, non-minimal reasoning, multi-turn messages and portal access remain preview | [Foundry IQ overview](https://learn.microsoft.com/azure/foundry/agents/concepts/what-is-foundry-iq), [migration matrix](https://learn.microsoft.com/azure/search/agentic-retrieval-how-to-migrate) |
| Fabric IQ | Preview workload with mixed item status | Introduced in November 2025; Plan GA in **July 2026**; Operations agent GA in **June 2026** | Ontology and Graph remain preview. Semantic models and some data-agent integrations are GA. Check the selected item and region | [Fabric IQ overview](https://learn.microsoft.com/fabric/iq/overview), [Fabric What's new](https://learn.microsoft.com/fabric/fundamentals/whats-new) |
| Web IQ | Announced and access-controlled; no GA label in the launch source | Launched **June 2, 2026** | The official announcement still directs customers to express interest. Treat it as a conditional dependency with a fallback | [Announcing Microsoft Web IQ](https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ) |
| Microsoft Agent Framework | Released Python core; .NET supported; Go public preview; integrations vary | Python `1.0.0` released **April 2, 2026** | Go does not yet support all framework features, Foundry managed-agent integration or Foundry hosted agents. Some .NET/Python integration packages are prerelease | [Agent Framework overview](https://learn.microsoft.com/agent-framework/overview/), [Python 1.0 changes](https://learn.microsoft.com/agent-framework/support/upgrade/python-2026-significant-changes#python-100-april-2-2026), [Foundry hosted agents](https://learn.microsoft.com/agent-framework/hosting/foundry-hosted-agent) |
| Microsoft Entra Agent ID | GA platform foundation; mixed product and feature lifecycle | Agent ID platform GA in **April 2026** | Microsoft release notes say the platform is GA, while a broader Agent ID page still labels the product preview and some identity creation flows remain preview. Validate each required capability | [Entra April 2026 releases](https://learn.microsoft.com/entra/fundamentals/whats-new#april-2026), [Agent ID what's new](https://learn.microsoft.com/entra/agent-id/whats-new-agent-id), [Agent ID overview](https://learn.microsoft.com/entra/agent-id/identity-professional/microsoft-entra-agent-identities-for-ai-agents) |
| Microsoft Agent 365 | GA for the Commercial segment, per user | GA on **May 1, 2026**; new-purchase prerequisites effective **June 1, 2026**; covered security capability cutover on **July 1, 2026** | License and prerequisite checks are mandatory; coverage varies by agent type and connected security service | [Agent 365 overview](https://learn.microsoft.com/microsoft-agent-365/overview), [July licensing announcement](https://learn.microsoft.com/partner-center/announcements/2026-july#new-licensing-prerequisite-for-agent-365), [security transition](https://learn.microsoft.com/defender-xdr/security-for-ai/transition-agent-security-to-agent-365) |
| Microsoft Scout | Frontier preview | Introduced **June 2, 2026** | Not a GA production dependency; availability is controlled by Frontier enrollment and the tenant administrator | [Scout overview](https://learn.microsoft.com/microsoft-scout/overview), [June announcement](https://learn.microsoft.com/partner-center/announcements/2026-june#copilot-cowork-and-microsoft-scout-what-partners-need-to-know) |
| ASSERT | Available open-source project; no commercial GA/preview label | Released **June 2, 2026** | Track tagged releases and validate the framework in CI. It is not a managed monitoring service or compliance certification | [ASSERT announcement](https://commandline.microsoft.com/assert-written-intent-executable-evals/), [official repository](https://github.com/responsibleai/ASSERT) |
| Agent Control Specification and Agent Governance Toolkit | Public preview | Introduced **June 2, 2026** | Breaking changes can occur before GA. Validate adapters, fail-closed behavior and conformance before production reliance | [ACS announcement](https://commandline.microsoft.com/agent-control-specification-runtime-governance/), [official toolkit](https://github.com/microsoft/agent-governance-toolkit) |
| MCP and A2A | Open protocols, not Microsoft commercial products | Versioned by their respective specifications and implementations | GA/preview labels apply to each Microsoft product integration, not to the protocol name by itself | [MCP in Foundry](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/model-context-protocol), [A2A in Foundry](https://learn.microsoft.com/azure/foundry/agents/how-to/tools/agent-to-agent) |

## MAI model status changes since the July snapshot

| Model or family | Current documented status | Dated change |
| --- | --- | --- |
| MAI-Thinking-1 | Public preview in Microsoft Foundry, Global Standard, model version `2026-06-01` | The repository's previous "private preview at announcement" wording was stale |
| MAI-Code-1.1-Flash | In production in GitHub Copilot; not documented as a generally selectable Foundry catalog model | Released **August 11, 2026**, superseding the June MAI-Code-1-Flash production rollout |
| MAI-Image-2.6 and 2.6-Flash | Public preview in Microsoft Foundry, model version `2026-07-31` | Public availability announced **September 4, 2026** |
| MAI-Transcribe-2 | Public preview through Azure Speech / Microsoft Foundry | Announced **September 3, 2026**; MAI-Transcribe-1 was deprecated **August 20, 2026** |
| MAI-Voice-2 and 2-Flash | Public preview through Azure Speech; instant voice cloning remains gated | MAI-Voice-2-Flash is now available and is no longer only "coming soon" |

Official model evidence: [MAI-Thinking-1](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai-thinking), [MAI-Code-1.1-Flash](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/), [MAI image models](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai-image), [MAI-Transcribe](https://learn.microsoft.com/azure/ai-services/speech-service/mai-transcribe), and [MAI-Voice](https://learn.microsoft.com/azure/ai-services/speech-service/mai-voices).

## Date interpretation rules

- A model version date is not necessarily its public announcement or GA date. This register preserves both when Microsoft publishes both.
- A roadmap target is not proof of release. A capability is marked released only when a current official page or release record confirms it.
- A parent platform's GA status does not promote preview child features to GA.
- Region, cloud, model, SKU, quota, license and tenant rollout remain production validation gates after a feature reaches GA.
- Recheck this file before each production architecture approval and update both the status and access date when a source changes.