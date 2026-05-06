---
name: estrategia-adocao-agentes-ia
summary: "Orienta a definicao de arquitetura corporativa para adocao de agentes de IA com Microsoft IQ, Fabric e Foundry, incluindo governanca, seguranca, guard rails e avaliacao continua."
license: MIT
metadata:
  author: Fabio Hara
  version: "1.0.0"
  language: pt-BR
---

# Skill: Estrategia de Adocao de Agentes de IA

## Objetivo

Esta skill ajuda a estruturar recomendacoes praticas para adocao de agentes de IA em ambiente corporativo, com foco em:

- arquitetura de referencia
- dados governados
- seguranca e compliance
- operacao e observabilidade
- evolucao continua com evaluators

## Use Quando

- O usuario pedir estrategia de adocao de agentes de IA.
- O usuario quiser desenhar arquitetura com Work IQ, Foundry IQ e Fabric IQ.
- O usuario precisar conectar IA com governanca de dados e seguranca.
- O usuario solicitar roteiro de implantacao por fases.
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
2. Mapear as fontes de dados e o nivel de governanca atual.
3. Definir separacao de camadas: experiencia (Work IQ), agentes (Foundry IQ), inteligencia de dados (Fabric IQ) e plataforma (Microsoft Fabric).
4. Definir controles transversais: Guard Rails e Evaluators.
5. Propor roadmap em ondas: piloto, expansao e escala.
6. Fechar com metricas de sucesso, riscos e plano de mitigacao.

## Regras de Qualidade da Resposta

- Explicar o "por que" de cada recomendacao.
- Preferir linguagem executiva com detalhes tecnicos objetivos.
- Sempre explicitar trade-offs (custo, risco, velocidade, complexidade).
- Evitar respostas genericas; adaptar ao contexto informado.
- Incluir proximos passos acionaveis.

## Formato de Saida Sugerido

- Visao executiva (curta)
- Arquitetura recomendada (camadas e responsabilidades)
- Governanca e seguranca (controles)
- Plano de implantacao por fases
- KPIs de sucesso
- Riscos e mitigacoes

## Referencia Interna

Base de conteudo principal para aprofundamento:
- Estrategia_Adocao_Agentes_IA_Final_2.md
