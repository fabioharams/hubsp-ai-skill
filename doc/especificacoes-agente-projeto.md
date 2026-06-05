# Especificacoes do Projeto de Agente de IA

## 1. Contexto de negocio e objetivo do agente
- Unidade de negocio:
- Problema a resolver:
- Objetivo principal (resultado esperado):
- Objetivos secundarios:
- Indicador executivo de sucesso:

## 2. Escopo funcional
### 2.1 O que o agente faz
- 
- 

### 2.2 O que o agente nao faz
- 
- 

### 2.3 Decisoes criticas do agente
- 
- 

### 2.4 Padrao arquitetural recomendado (espectro de complexidade)
- [ ] LLM (texto simples, um passo)
- [ ] RAG (resposta com grounding em dados)
- [ ] AI Agent unico (multi-etapa em um dominio)
- [ ] Agentic AI (multiagente, multiplos dominios)
- Justificativa da escolha (menor complexidade que resolve o caso):
- Condicoes de evolucao para um padrao mais complexo no roadmap:

## 3. Perfis de usuarios, jornadas e canais
### 3.1 Perfis de usuarios
- Perfil 1:
- Perfil 2:

### 3.2 Jornadas principais
- Jornada A:
- Jornada B:

### 3.3 Canais de interacao
- [ ] Web
- [ ] Teams
- [ ] WhatsApp
- [ ] Email
- [ ] Outro:

## 4. Requisitos nao funcionais
- SLA de atendimento:
- Latencia maxima aceitavel:
- Disponibilidade alvo:
- Volume esperado (dia/mes):
- Janela de pico:
- Requisitos de escalabilidade:

## 5. Dados e integracoes
### 5.1 Fontes de dados
- Fonte:
- Tipo de dado:
- Sensibilidade/classificacao:

### 5.2 Integracoes
- Sistema/API:
- Tipo (consulta, escrita, ambos):
- Criticidade:

### 5.3 Qualidade e governanca de dados
- Dono do dado:
- Politicas de retencao:
- Regras de acesso:

## 6. Governanca, seguranca e compliance
- Guard rails obrigatorios:
- Evaluators desejados:
- Human-in-the-Loop (quando e como):
- Requisitos regulatorios aplicaveis:
- Requisitos de auditoria e rastreabilidade:

## 7. Criterios de sucesso e KPIs
- KPI 1 (valor atual -> meta):
- KPI 2 (valor atual -> meta):
- KPI 3 (valor atual -> meta):
- Horizonte de medicao (30/60/90 dias):

### 7.1 Premissas de ROI/IVA
- Custo de homem-hora carregado (R$/h):
- Volume de tarefas (mes):
- Custo IA por tarefa (tokens + ferramentas):
- Tempo de HITL por tarefa (min):
- Custo de setup amortizado por tarefa:
- Modo de analise:
	- [ ] Eficiencia (substituicao)
	- [ ] Ampliacao (copiloto)
- Horizonte de avaliacao financeira (12-18 meses):

## 8. Restricoes, riscos e premissas
### 8.1 Restricoes
- Orcamento:
- Prazo:
- Tecnologia:

### 8.2 Riscos
- Risco:
- Impacto:
- Mitigacao:

### 8.3 Premissas
- 
- 

## 9. Roadmap em ondas
### Onda 1 - Piloto
- Escopo:
- Duracao:
- Criterio de saida:

### Onda 2 - Expansao
- Escopo:
- Duracao:
- Criterio de saida:

### Onda 3 - Escala
- Escopo:
- Duracao:
- Criterio de saida:

## 10. Perguntas para decisao de arquitetura alvo

### 10.1 Intake Filter (Microsoft AI Decision Framework)
- Qual problema de negocio precisa ser resolvido agora?
- Existe impacto material (financeiro, regulatorio, operacional ou reputacional)?
- Quais decisoes devem permanecer com aprovacao humana obrigatoria?

### 10.2 BXT (Business, Experience, Technology)
- Business: qual KPI de negocio sera movido e em quanto tempo?
- Experience: qual jornada muda para usuario, operador e gestor?
- Technology: qual stack minima atende com seguranca e escala?

### 10.3 9 perguntas criticas (resumo para decisao)
- 1) Qual e o resultado de negocio esperado?
- 2) Qual e o nivel de risco aceitavel?
- 3) Quais dados governados sao obrigatorios?
- 4) Onde Web IQ agrega valor real?
- 5) Quais integracoes exigem escrita/transacao?
- 6) Qual nivel de autonomia do agente e adequado?
- 7) Quais guard rails e evaluators sao obrigatorios no go-live?
- 8) Qual criterio de escalabilidade para sair do piloto?
- 9) Qual trade-off aceito entre custo, risco, velocidade e complexidade?

## 11. Anexos opcionais
- Diagrama de processo atual (AS-IS):
- Diagrama de arquitetura alvo (TO-BE):
- Politicas internas relevantes:
- Referencias tecnicas:

---

## Como usar este documento com a skill

### VS Code / GitHub Copilot App
Use no prompt:

> Usando o #SKILL.md e o #doc/especificacoes-agente-projeto.md, gere uma recomendacao executiva no formato completo: (1) visao executiva media (1-2 paragrafos) com pelo menos 1 diagrama ou fluxograma Mermaid para explicar a decisao recomendada, (2) padrao arquitetural recomendado (LLM/RAG/AI Agent/Agentic AI) com justificativas detalhadas, links oficiais da Microsoft e pelo menos 1 diagrama ou fluxograma Mermaid para explicar a escolha, (3) arquitetura alvo (Work IQ, Foundry IQ, Fabric IQ e Web IQ) com explicacao detalhada e 2 diagramas Mermaid obrigatorios (arquitetura e fluxograma de decisao), (4) governanca e seguranca com guard rails e evaluators e pelo menos 1 diagrama ou fluxograma Mermaid, (5) plano de implantacao por fases com detalhamento por fase (objetivo, escopo, integracoes, criterios de entrada/saida, KPI alvo e risco dominante) e pelo menos 1 diagrama ou fluxograma Mermaid, (6) premissas de ROI/IVA com pelo menos 1 diagrama ou fluxograma Mermaid para explicar a logica financeira, (7) KPIs de sucesso com pelo menos 1 diagrama ou fluxograma Mermaid, e (8) riscos e mitigacoes com clareza, links oficiais Microsoft e pelo menos 1 diagrama ou fluxograma Mermaid. A resposta devera ser entregue em um novo documento em markdown chamado doc/resultado.md.
> Usando o #SKILL.md e o #doc/especificacoes-agente-projeto.md, gere uma recomendacao executiva no formato completo: (1) visao executiva media (1-2 paragrafos) com pelo menos 1 diagrama ou fluxograma Mermaid para explicar a decisao recomendada, (2) padrao arquitetural recomendado (LLM/RAG/AI Agent/Agentic AI) com justificativas detalhadas, links oficiais da Microsoft e pelo menos 1 diagrama ou fluxograma Mermaid para explicar a escolha, (3) arquitetura alvo (Work IQ, Foundry IQ, Fabric IQ e Web IQ) com explicacao detalhada e 2 diagramas Mermaid obrigatorios (arquitetura e fluxograma de decisao), (4) governanca e seguranca com guard rails, evaluators, analise do PL 2338/2023 e explicacao de como as ferramentas e servicos selecionados na arquitetura respondem aos eixos de transparencia, governanca, risco, auditoria, supervisao humana e protecao de dados com fontes oficiais, e pelo menos 1 diagrama ou fluxograma Mermaid, (5) plano de implantacao por fases com detalhamento por fase (objetivo, escopo, integracoes, criterios de entrada/saida, KPI alvo e risco dominante) e pelo menos 1 diagrama ou fluxograma Mermaid, (6) premissas de ROI/IVA com pelo menos 1 diagrama ou fluxograma Mermaid para explicar a logica financeira, (7) KPIs de sucesso com pelo menos 1 diagrama ou fluxograma Mermaid, e (8) riscos e mitigacoes com clareza, links oficiais Microsoft e pelo menos 1 diagrama ou fluxograma Mermaid. A resposta devera ser entregue em um novo documento em markdown chamado doc/resultado.md.

### GitHub Copilot CLI
Use no prompt:

> Leia SKILL.md e doc/especificacoes-agente-projeto.md e gere recomendacao executiva em formato avancado: visao executiva media com diagrama ou fluxograma Mermaid; padrao arquitetural com justificativas detalhadas, fontes Microsoft e diagrama ou fluxograma Mermaid; arquitetura Work IQ/Foundry IQ/Fabric IQ/Web IQ com diagrama Mermaid e fluxograma Mermaid; governanca e seguranca com analise do PL 2338/2023, explicacao de como as ferramentas e servicos selecionados na arquitetura respondem aos eixos de transparencia, governanca, risco, auditoria, supervisao humana e protecao de dados com fontes oficiais, e diagrama ou fluxograma Mermaid; plano em fases detalhado com diagrama ou fluxograma Mermaid; premissas de ROI/IVA com diagrama ou fluxograma Mermaid; KPIs com diagrama ou fluxograma Mermaid; riscos e mitigacoes com links oficiais da Microsoft e diagrama ou fluxograma Mermaid. A resposta devera ser entregue em um novo documento em markdown chamado doc/resultado.md.
