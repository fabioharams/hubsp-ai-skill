---
name: hubsp-ai-skill
summary: "Orienta a definicao de arquitetura corporativa para adocao de agentes de IA com Microsoft IQ, Fabric e Foundry, incluindo Work IQ, Foundry IQ, Fabric IQ e Web IQ, fundamentos de arquitetura (LLM, RAG, AI Agent, Agentic AI), modelo de ROI (IA vs. homem-hora), governanca, seguranca, guard rails e avaliacao continua."
description: "Skill para orientar estrategia de adocao de agentes de IA no ecossistema Microsoft, incluindo arquitetura alvo, governanca, ROI, seguranca e aderencia regulatoria."
license: MIT
metadata:
  author: Fabio
  version: "1.2.0"
  language: pt-BR
---

# Skill: Estrategia de Adocao de Agentes de IA

## Objetivo

Esta skill ajuda a estruturar recomendacoes praticas para adocao de agentes de IA em ambiente corporativo, com foco em:

- fundamentos de arquitetura de IA (LLM, RAG, AI Agent, Agentic AI)
- arquitetura de referencia
- dados governados
- justificativa financeira (ROI: IA vs. custo de homem-hora)
- seguranca e compliance
- operacao e observabilidade
- evolucao continua com evaluators

## Use Quando

- O usuario pedir estrategia de adocao de agentes de IA.
- O usuario quiser desenhar arquitetura com Work IQ, Foundry IQ e Fabric IQ, incluindo contexto externo via Web IQ quando aplicavel.
- O usuario precisar entender ou comparar os padroes LLM, RAG, AI Agent e Agentic AI.
- O usuario quiser decidir o nivel minimo de complexidade para um caso de uso.
- O usuario precisar conectar IA com governanca de dados e seguranca.
- O usuario solicitar roteiro de implantacao por fases.
- O usuario pedir justificativa financeira ou ROI (IA vs. homem-hora, modo eficiencia ou ampliacao).
- O usuario pedir padroes para escalar agentes entre areas de negocio.
- O usuario pedir analise regulatoria, governanca ou aderencia de Microsoft Copilot Studio, Microsoft Foundry e Purview a requisitos como transparencia, auditoria, risco, supervisao humana e protecao de dados.

## Nao Use Quando

- O pedido for apenas para corrigir codigo local sem contexto arquitetural.
- O usuario quiser somente comandos CLI pontuais sem decisao de arquitetura.
- O tema for totalmente fora do ecossistema Microsoft/Fabric/Foundry.

## Entradas Esperadas

- objetivo de negocio
- area(s) impactada(s)
- maturidade de dados
- requisitos de seguranca/compliance
- prazo e prioridade

Se faltar informacao critica, solicitar apenas o minimo necessario antes de recomendar a arquitetura.

## Processo Recomendado

1. Entender o problema de negocio e o resultado esperado.
2. Escolher o padrao arquitetural pelo menor nivel de complexidade que resolve de forma confiavel: LLM (texto, um passo), RAG (resposta fundamentada em dados), AI Agent unico (tarefa multi-etapa, um dominio) ou Agentic AI multiagente (cruza seguranca, multiplos times ou crescimento previsto).
2.1. Quando o pedido envolver escolha de tecnologia/produto Microsoft, aplicar o Microsoft AI Decision Framework (referencias/05-decision-framework-bxt.md): Intake Filter, BXT (Business/Experience/Technology), as 9 perguntas criticas e a selecao por cenario.
3. Mapear as fontes de dados e o nivel de governanca atual.
4. Definir separacao de camadas: experiencia (Work IQ), agentes (Foundry IQ), inteligencia de dados (Fabric IQ), contexto externo (Web IQ, quando necessario) e plataforma (Microsoft Fabric).
4.1. Quando o caso exigir, recomendar **solucao mista**: Copilot Studio na camada conversacional/fluxo de negocio e Microsoft Foundry na camada de reasoning/orquestracao avancada.
5. Definir controles transversais: Guard Rails e Evaluators.
5.1. Quando o pedido envolver regulacao, compliance ou aderencia a requisitos legais, mapear os eixos regulatorios para capacidades tecnicas e de governanca da Microsoft, sem afirmar conformidade juridica automatica.
6. Validar a viabilidade financeira com o modelo de ROI (IVA = custo humano / custo IA por tarefa), incluindo HITL, setup amortizado e multiplicador de escopo; avaliar no horizonte de 12-18 meses.
7. Propor roadmap em ondas: piloto, expansao e escala.
8. Fechar com metricas de sucesso, riscos e plano de mitigacao.

## Regras de Qualidade da Resposta

- Explicar o "por que" de cada recomendacao.
- Preferir linguagem executiva com detalhes tecnicos objetivos.
- Sempre explicitar trade-offs (custo, risco, velocidade, complexidade).
- Evitar respostas genericas; adaptar ao contexto informado.
- Incluir proximos passos acionaveis.

## Termos Preferenciais

- Priorizar os termos: guard rails, evaluators, roadmap em ondas, arquitetura alvo, dados governados.
- Para fundamentos, usar: espectro de complexidade, grounding, RAG, AI Agent unico, Agentic AI (multiagente), HITL, MCP, A2A.
- Para ROI, usar: custo de homem-hora carregado, IVA (Indice de Vantagem da IA), custo por tarefa, HITL, multiplicador de escopo, fator de realizacao, modo eficiencia, modo ampliacao.
- Quando houver sinonimos, manter os termos acima para consistencia entre respostas.
- Em respostas executivas, usar frases curtas e orientadas a decisao.

## Formato de Saida Sugerido

- Visao executiva (media)
  - Entregar em 1-2 paragrafos, com contexto, decisao recomendada, impacto esperado e principais trade-offs (custo, risco, velocidade e complexidade).
  - Deve deixar claro o problema de negocio, a arquitetura alvo proposta e o resultado de curto prazo (piloto) vs. medio prazo (escala).
  - Incluir pelo menos 1 diagrama ou fluxograma simples em Mermaid para explicar visualmente a decisao recomendada.
  - O visual deve resumir a logica da recomendacao em linguagem executiva e ser de facil leitura.
  - Referencia Microsoft: https://learn.microsoft.com/azure/cloud-adoption-framework/strategy/

- Padrao arquitetural recomendado (LLM, RAG, AI Agent ou Agentic AI) com justificativa detalhada
  - Comparar as opcoes no contexto do caso e justificar por que a recomendacao minimiza risco e maximiza valor.
  - Explicar criterios tecnicos: grounding, necessidade de orquestracao, autonomia, qualidade de dados, latencia, custo por tarefa e necessidade de HITL.
  - Incluir justificativas com fontes oficiais Microsoft para sustentar cada escolha.
  - Incluir pelo menos 1 fluxograma ou diagrama em Mermaid para explicar o padrao arquitetural escolhido e os caminhos descartados.
  - O visual deve facilitar a compreensao do espectro LLM → RAG → AI Agent → Agentic AI e a decisao final.
  - Referencias Microsoft:
    - Azure OpenAI: https://learn.microsoft.com/azure/ai-services/openai/overview
    - RAG no Azure AI Search: https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview
    - Azure AI Foundry Agent Service: https://learn.microsoft.com/azure/ai-foundry/agents/overview
    - Microsoft AI Decision Framework: https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/

- Arquitetura recomendada (camadas e responsabilidades) com explicacao detalhada
  - Descrever papeis e limites de Work IQ, Foundry IQ, Fabric IQ e Web IQ, incluindo como se conectam a dados governados e controles transversais.
  - Explicar responsabilidades por camada (experiencia/canais, orquestracao de agentes, dados/analytics, contexto externo).
  - Obrigatorio incluir:
    - 1 diagrama de arquitetura em Mermaid (camadas e fluxos principais).
    - 1 fluxograma em Mermaid (decisao de roteamento: autosservico, escalonamento, HITL).
  - Os diagramas devem ser simples, legiveis e orientados a decisao executiva.
  - Referencias Microsoft:
    - Microsoft 365 Copilot: https://learn.microsoft.com/microsoft-365-copilot/
    - Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry/
    - Microsoft Fabric: https://learn.microsoft.com/fabric/

- Governanca e seguranca (controles)
  - Detalhar guard rails tecnicos e operacionais: Entra ID, RBAC, DLP, trilha de auditoria, versionamento de regras/checklists, evaluators e HITL.
  - Relacionar cada controle ao risco que ele mitiga (ex.: alucinacao, acesso indevido, decisao critica sem supervisao).
  - Incluir analise explicita do PL 2338/2023, conectando a arquitetura recomendada aos eixos de transparencia, governanca, risco, auditoria, supervisao humana e protecao de dados.
  - Explicar como as ferramentas e servicos selecionados na arquitetura respondem a cada eixo regulatorio, indicando limites, dependencias e eventuais lacunas de implementacao.
  - Priorizar o uso de fontes oficiais Microsoft e, quando relevante, mencionar o arquivo de referencia regulatoria do repositorio para sustentar a analise.
  - Incluir pelo menos 1 diagrama ou fluxograma em Mermaid mostrando a sequencia de controles, validacoes e pontos de bloqueio/aprovacao.
  - Referencias Microsoft:
    - Microsoft Entra: https://learn.microsoft.com/entra/identity/
    - Microsoft Purview: https://learn.microsoft.com/purview/governance-solutions-overview
    - Responsible AI no Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry/responsible-ai/overview
    - Microsoft Security: https://learn.microsoft.com/security/
    - Well-Architected Framework - Security: https://learn.microsoft.com/azure/well-architected/security/

- Plano de implantacao por fases (detalhado)
  - Descrever no minimo 3 fases: Piloto, Expansao e Escala.
  - Para cada fase, explicitar: objetivo, escopo funcional, integracoes, guard rails minimos, criterios de entrada, criterios de saida, KPI alvo e risco dominante.
  - Informar dependencias criticas (dados, integracoes, patrocino executivo, change management).
  - Incluir pelo menos 1 diagrama ou fluxograma em Mermaid para explicar a progressao entre fases, dependencias e gates de decisao.
  - Referencia Microsoft: https://learn.microsoft.com/azure/cloud-adoption-framework/plan/

- Justificativa financeira (ROI/IVA, quando aplicavel)
  - Explicar premissas, baseline, metodo de calculo e horizonte de captura de valor.
  - Incluir custo de homem-hora carregado, custo IA por tarefa, HITL, setup amortizado e sensibilidade (conservador/base/agressivo).
  - Incluir pelo menos 1 diagrama ou fluxograma em Mermaid para explicar a logica de calculo, os drivers de custo e o criterio de decisao financeira.
  - Referencias Microsoft:
    - Azure Pricing Calculator: https://azure.microsoft.com/pricing/calculator/
    - Azure TCO Calculator: https://azure.microsoft.com/pricing/tco/calculator/

- KPIs de sucesso
  - Cobrir KPIs de eficiencia, qualidade, risco e adocao (ex.: SLA, FCR, retrabalho, latencia, taxa de escalonamento indevido, custo por caso, NPS interno).
  - Sugerir janelas de afericao (30/60/90 dias) e gatilhos de ajuste.
  - Incluir pelo menos 1 diagrama ou fluxograma em Mermaid para organizar KPIs por categoria, horizonte de medicao ou relacao causal com valor de negocio.
  - Referencias Microsoft:
    - Azure Monitor: https://learn.microsoft.com/azure/azure-monitor/
    - Application Insights: https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview

- Riscos e mitigacoes (claros, com justificativa oficial)
  - Explicar com clareza os principais riscos: dados, seguranca, compliance, operacao, adocao e dependencia de integracao.
  - Para cada risco, incluir impacto, probabilidade, sinal de alerta e mitigacao tecnica/processual.
  - Sempre justificar as mitigacoes com links oficiais Microsoft.
  - Incluir pelo menos 1 diagrama ou fluxograma em Mermaid para mostrar relacao entre risco, controle, mitigacao e responsavel de resposta.
  - Referencias Microsoft:
    - Microsoft Security: https://learn.microsoft.com/security/
    - Well-Architected Framework (Security): https://learn.microsoft.com/azure/well-architected/security/
    - Well-Architected Framework (Operational Excellence): https://learn.microsoft.com/azure/well-architected/operational-excellence/

## Referencia Interna

Carregue apenas o arquivo de referencia necessario para a pergunta (progressive disclosure):

- referencias/01-fundamentos-llm-rag-agentes.md — LLM x RAG x AI Agent x Agentic AI; espectro de complexidade e guia de decisao.
- referencias/02-arquitetura-referencia-camadas.md — Microsoft IQ (Work IQ, Foundry IQ, Fabric IQ, Web IQ) e Microsoft Fabric; especificacoes tecnicas por camada.
- referencias/03-roi-ia-vs-homem-hora.md — modelo de ROI/IVA, HITL, multiplicador de escopo.
- referencias/04-governanca-guardrails-evaluators-hitl.md — Guard Rails, Evaluators e Human-in-the-Loop.
- referencias/05-decision-framework-bxt.md — Microsoft AI Decision Framework: Intake Filter, BXT, 9 perguntas criticas, Capability Model e selecao de tecnologia por cenario.
- referencias/07-pl-2338-2023-copilot-studio-foundry.md — analise do PL 2338/2023, com foco em transparencia, governanca, risco, auditoria, supervisao humana e protecao de dados com fontes oficiais.

Indice completo e demais secoes: Estrategia_Adocao_Agentes_IA_Final_2.md (fonte canonica, com ponteiros para os arquivos acima).
