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
- Qual parte da jornada depende de dados governados?
- Onde o contexto externo (Web IQ) e necessario?
- Quais fluxos exigem aprovacao humana?
- Quais componentes exigem maior observabilidade?

## 11. Anexos opcionais
- Diagrama de processo atual (AS-IS):
- Diagrama de arquitetura alvo (TO-BE):
- Politicas internas relevantes:
- Referencias tecnicas:

---

## Como usar este documento com a skill

### VS Code / GitHub Copilot App
Use no prompt:

> Usando o #SKILL.md e o #doc/especificacoes-agente-projeto.md, recomende a arquitetura alvo (Work IQ, Foundry IQ, Fabric IQ), os guard rails e o roadmap em ondas para este projeto.

### GitHub Copilot CLI
Use no prompt:

> Leia SKILL.md e doc/especificacoes-agente-projeto.md e gere recomendacao executiva com trade-offs entre custo, risco, velocidade e complexidade.
