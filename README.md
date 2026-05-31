# HARASKILL

## O que e este projeto

Este repositorio organiza uma base pratica para orientar a adocao corporativa de agentes de IA no ecossistema Microsoft. O foco e apoiar decisoes de arquitetura alvo com integracao entre Work IQ, Foundry IQ e Fabric IQ, conectando estrategia de negocio, dados governados, seguranca, guard rails, evaluators e operacao em escala.

O projeto foi estruturado para servir como referencia executiva e tecnica: ajuda times de negocio, arquitetura, dados e seguranca a alinharem uma visao comum de como planejar, pilotar e expandir iniciativas de IA agentica com menor risco e maior previsibilidade de valor.

## Objetivo

- Definir uma arquitetura de referencia para agentes de IA em contexto corporativo.
- Padronizar recomendacoes com foco em governanca, compliance e observabilidade.
- Apoiar um roadmap em ondas (piloto, expansao e escala) com criterios claros.
- Explicitar trade-offs entre custo, risco, velocidade e complexidade.

## O que voce encontra neste repositorio

- SKILL.md: definicao unica da skill (roteador) que orienta respostas consistentes em contexto de arquitetura de adocao. Aponta para os arquivos de referencia sob demanda (progressive disclosure).
- Estrategia_Adocao_Agentes_IA_Final_2.md: guia principal e documento-base, com visao executiva, indice e ponteiros para os arquivos de referencia.
- referencias/: conteudo tematico fatiado para carregamento sob demanda:
  - referencias/01-fundamentos-llm-rag-agentes.md: LLM x RAG x AI Agent x Agentic AI; espectro de complexidade e guia de decisao.
  - referencias/02-arquitetura-referencia-camadas.md: Work IQ, Foundry IQ, Fabric IQ, Microsoft Fabric e especificacoes tecnicas por camada.
  - referencias/03-roi-ia-vs-homem-hora.md: modelo de ROI/IVA, HITL e multiplicador de escopo.
  - referencias/04-governanca-guardrails-evaluators-hitl.md: Guard Rails, Evaluators e Human-in-the-Loop.
- Guias complementares de dinamicas e setup para facilitar colaboracao e uso no VS Code.

## Estrutura do repositorio (diagrama)

O diagrama abaixo mostra como os arquivos se relacionam. O SKILL.md e o ponto de entrada (roteador); o documento-base concentra o conteudo completo e aponta, sob demanda, para os arquivos tematicos em referencias/.

```mermaid
graph TD
    USER([Usuario / Agente faz uma pergunta]) --> SKILL[SKILL.md<br/>Skill roteadora - ponto de entrada]
    SKILL --> CANON[Estrategia_Adocao_Agentes_IA_Final_2.md<br/>Documento-base - indice + ponteiros]

    SKILL -. progressive disclosure .-> REF{{referencias/}}
    CANON -. ponteiros .-> REF

    REF --> R1[01-fundamentos-llm-rag-agentes.md<br/>LLM x RAG x AI Agent x Agentic AI]
    REF --> R2[02-arquitetura-referencia-camadas.md<br/>Work IQ - Foundry IQ - Fabric IQ - Fabric]
    REF --> R3[03-roi-ia-vs-homem-hora.md<br/>ROI / IVA - HITL - escopo]
    REF --> R4[04-governanca-guardrails-evaluators-hitl.md<br/>Guard Rails - Evaluators - HITL]

    SKILL --> README[README.md<br/>Visao geral do repositorio]

    classDef entry fill:#0078D4,stroke:#004578,color:#fff;
    classDef canon fill:#107C10,stroke:#0B5A0B,color:#fff;
    classDef ref fill:#E6F2FA,stroke:#0078D4,color:#1a1a1a;
    class SKILL entry;
    class CANON canon;
    class R1,R2,R3,R4 ref;
```

## Como navegar (fluxograma de decisao)

Use este fluxo para escolher qual arquivo abrir conforme a sua necessidade.

```mermaid
flowchart TD
    START([Qual e a sua necessidade?]) --> Q1{Quer apenas a<br/>visao geral do repo?}
    Q1 -- Sim --> README[Leia README.md]
    Q1 -- Nao --> Q2{Vai pedir uma<br/>recomendacao a IA?}

    Q2 -- Sim --> SKILL[Use SKILL.md<br/>como contexto/skill]
    Q2 -- Nao --> Q3{Que tema voce<br/>precisa aprofundar?}

    SKILL --> Q3

    Q3 -- Fundamentos<br/>LLM/RAG/Agentes --> R1[referencias/01-fundamentos-llm-rag-agentes.md]
    Q3 -- Arquitetura<br/>por camadas --> R2[referencias/02-arquitetura-referencia-camadas.md]
    Q3 -- Justificativa<br/>financeira / ROI --> R3[referencias/03-roi-ia-vs-homem-hora.md]
    Q3 -- Governanca<br/>e seguranca --> R4[referencias/04-governanca-guardrails-evaluators-hitl.md]
    Q3 -- Visao completa<br/>ou outras secoes --> CANON[Estrategia_Adocao_Agentes_IA_Final_2.md]

    R1 --> END([Aplique no seu caso de uso])
    R2 --> END
    R3 --> END
    R4 --> END
    CANON --> END
    README --> END
```

## Publico-alvo

- Liderancas de tecnologia e negocio.
- Arquitetos corporativos, arquitetos de dados e equipes de plataforma.
- Times de governanca, seguranca e compliance.
- Squads que estao iniciando ou escalando agentes de IA.
