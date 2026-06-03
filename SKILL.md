---
name: estrategia-adocao-agentes-ia
summary: "Orienta a definicao de arquitetura corporativa para adocao de agentes de IA com Microsoft IQ, Fabric e Foundry, incluindo Work IQ, Foundry IQ, Fabric IQ e Web IQ, fundamentos de arquitetura (LLM, RAG, AI Agent, Agentic AI), modelo de ROI (IA vs. homem-hora), governanca, seguranca, guard rails e avaliacao continua."
license: MIT
metadata:
  author: Fabio
  version: "1.1.0"
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
5. Definir controles transversais: Guard Rails e Evaluators.
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

- Visao executiva (curta)
- Padrao arquitetural recomendado (LLM, RAG, AI Agent ou Agentic AI) e por que
- Arquitetura recomendada (camadas e responsabilidades)
- Governanca e seguranca (controles)
- Plano de implantacao por fases
- Justificativa financeira (ROI/IVA, quando aplicavel)
- KPIs de sucesso
- Riscos e mitigacoes

## Referencia Interna

Carregue apenas o arquivo de referencia necessario para a pergunta (progressive disclosure):

- referencias/01-fundamentos-llm-rag-agentes.md — LLM x RAG x AI Agent x Agentic AI; espectro de complexidade e guia de decisao.
- referencias/02-arquitetura-referencia-camadas.md — Microsoft IQ (Work IQ, Foundry IQ, Fabric IQ, Web IQ) e Microsoft Fabric; especificacoes tecnicas por camada.
- referencias/03-roi-ia-vs-homem-hora.md — modelo de ROI/IVA, HITL, multiplicador de escopo.
- referencias/04-governanca-guardrails-evaluators-hitl.md — Guard Rails, Evaluators e Human-in-the-Loop.
- referencias/05-decision-framework-bxt.md — Microsoft AI Decision Framework: Intake Filter, BXT, 9 perguntas criticas, Capability Model e selecao de tecnologia por cenario.

Indice completo e demais secoes: Estrategia_Adocao_Agentes_IA_Final_2.md (fonte canonica, com ponteiros para os arquivos acima).
