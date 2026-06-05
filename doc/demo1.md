# Especificações do Projeto de Agente de IA — harafaz.ia

> **Observação:** documento preenchido com base no material de ADS - harafaz.ia. Onde o conteúdo-fonte não traz valor fechado, o campo foi preenchido como **recomendação inicial** ou **a validar no discovery/piloto**.

## 1. Contexto de negócio e objetivo do agente

- **Unidade de negócio:** Diretoria de Operações / Backoffice harafaz.ia, com atuação transversal nas jornadas de originação, manutenção e middle.
- **Problema a resolver:** canais fragmentados, baixa rastreabilidade, ausência de case único padronizado, baixo reuso de dados/documentos e dificuldade para medir SLA, FCR, reincidência e produtividade.
- **Objetivo principal (resultado esperado):** implantar um agente de IA para triagem e autosserviço assistido, integrado a case management, para reduzir tempo de atendimento/processamento, retrabalho e perda de contexto, preservando escalonamento humano em casos críticos.
- **Objetivos secundários:**
  - padronizar a entrada de solicitações em múltiplos canais;
  - criar registro único de caso com histórico e trilha de auditoria;
  - aumentar o reuso de dados, documentos e qualificações já realizadas;
  - melhorar governança operacional e telemetria;
  - apoiar handoff entre jornadas.
- **Indicador executivo de sucesso:** redução do tempo médio de atendimento/processamento, aumento de FCR, redução de retrabalho/reincidência e melhora do NPS interno da rede.

## 2. Escopo funcional

### 2.1 O que o agente faz

1. Recebe demandas por canais prioritários, classifica tema/produto/risco/prioridade e abre ou atualiza um case único.
2. Executa triagem, orienta o usuário, solicita dados faltantes, consulta base de conhecimento curada e aciona fluxos quando elegível.
3. Escala para humano com contexto completo quando houver exceção, sensibilidade, risco ou baixa confiança.
4. Registra evidências, status, tempos, motivo de escalonamento e resultado para analytics.

### 2.2 O que o agente não faz

1. Não toma decisão final autônoma em casos de conformidade, risco ou exceções críticas.
2. Não substitui governança normativa, revisão humana de conhecimento ou processos formais de auditoria.
3. Não elimina sistemas legados; orquestra sua utilização de forma progressiva.
4. Não deve operar sobre fontes ou canais fora da política de dados e segurança definida.

### 2.3 Decisões críticas do agente

1. Determinar se a demanda é elegível para autosserviço/automação assistida ou precisa de escalonamento humano.
2. Determinar se os dados mínimos estão completos e se a regra/checklist aplicável está vigente.
3. Escolher o destino do handoff com base em tema, risco, produto e contexto.
4. Decidir quando registrar bloqueio, pendência, ação corretiva ou encerramento com evidência.

## 3. Perfis de usuários, jornadas e canais

### 3.1 Perfis de usuários

- **Perfil 1:** gerentes e equipes da rede negocial / usuários internos.
- **Perfil 2:** especialistas de middle, operação, conformidade e centralizadoras.
- **Perfil 3:** gestores de produto e áreas definidoras de regra.
- **Perfil 4:** cliente final, em evoluções futuras.

### 3.2 Jornadas principais

- **Jornada A:** triagem, orientação e abertura de case para demandas consultivas da rede.
- **Jornada B:** qualificação de solicitação e coleta guiada de dados/documentos para originação.
- **Jornada C:** handoff entre jornadas e áreas com contexto e rastreabilidade.
- **Jornada D:** acompanhamento de status, resolução, evidências e mensuração de eficiência.

### 3.3 Canais de interação

- [x] Web
- [x] Teams
- [ ] WhatsApp *(expansão controlada / quando aplicável)*
- [x] Email
- [x] Outro: esteiras por produto, portal/app, canais internos da rede

## 4. Requisitos não funcionais

- **SLA de atendimento:** a validar por jornada e categoria; recomendação de medição desde o piloto.
- **Latência máxima aceitável:** recomendação inicial de até 5 segundos para resposta inicial e até 15 segundos para ações simples com consulta/orquestração.
- **Disponibilidade alvo:** recomendação inicial de 99,5% no piloto e evolução para 99,9% em produção ampliada.
- **Volume esperado (dia/mês):** a validar no discovery e assessment por app.
- **Janela de pico:** picos comerciais, horários de atendimento da rede e períodos de campanha/produto; detalhamento a validar no discovery.
- **Requisitos de escalabilidade:** expansão por ondas, inclusão progressiva de canais, produtos e hubs, mantendo case único, observabilidade e governança.

## 5. Dados e integrações

### 5.1 Fontes de dados

- **Fonte:** bases internas curadas / Chat harafaz.ia / SharePoint / bases normativas  
  - **Tipo de dado:** normativos, FAQs, procedimentos, regras e conhecimento operacional  
  - **Sensibilidade/classificação:** interna / sigilosa operacional

- **Fonte:** Dataverse (case único)  
  - **Tipo de dado:** casos, status, SLA, histórico, evidências, classificação, handoff, satisfação  
  - **Sensibilidade/classificação:** dados operacionais e potencialmente sensíveis

- **Fonte:** sistemas legados (ex.: CXTD, CMTR e outros)  
  - **Tipo de dado:** status de processamento, dados de negócio, validações e retorno de esteira  
  - **Sensibilidade/classificação:** alta / regulada

- **Fonte:** formulários/pesquisa (ex.: Forms)  
  - **Tipo de dado:** NPS interno e feedback de atendimento  
  - **Sensibilidade/classificação:** interna

### 5.2 Integrações

- **Sistema/API:** Dataverse  
  - **Tipo (consulta, escrita, ambos):** ambos  
  - **Criticidade:** crítica

- **Sistema/API:** Power Automate  
  - **Tipo (consulta, escrita, ambos):** ambos  
  - **Criticidade:** crítica

- **Sistema/API:** sistemas legados / esteiras por produto  
  - **Tipo (consulta, escrita, ambos):** ambos  
  - **Criticidade:** crítica

- **Sistema/API:** SharePoint / base de conhecimento curada / Chat harafaz.ia  
  - **Tipo (consulta, escrita, ambos):** consulta  
  - **Criticidade:** alta

- **Sistema/API:** Teams / Email / Portal / Web channel  
  - **Tipo (consulta, escrita, ambos):** ambos  
  - **Criticidade:** alta

- **Sistema/API:** Power BI / analytics  
  - **Tipo (consulta, escrita, ambos):** consulta  
  - **Criticidade:** alta

### 5.3 Qualidade e governança de dados

- **Dono do dado:** áreas operacionais da harafaz.ia por jornada, com corresponsabilidade de produto, backoffice e TI; base de conhecimento sob curadoria especializada.
- **Políticas de retenção:** a definir conforme política corporativa, exigências regulatórias e auditoria.
- **Regras de acesso:** menor privilégio por perfil; segregação por ambiente, hub, tema e jornada; autenticação Microsoft Entra ID.

## 6. Governança, segurança e compliance

- **Guard rails obrigatórios:**
  - autenticação via Microsoft Entra ID;
  - RBAC por papel e por ambiente;
  - políticas DLP para conectores, ferramentas e canais;
  - trilha de auditoria para criação, transferência, decisão e fechamento de case;
  - bloqueio de fontes/canais fora da política de dados;
  - versionamento de regras e checklists normativos;
  - human-in-the-loop para decisões críticas;
  - revisão periódica da base de conhecimento.

- **Evaluators desejados:**
  - groundedness;
  - detecção de alucinação;
  - precisão de classificação e roteamento;
  - taxa de escalonamento indevido;
  - completude de contexto no handoff;
  - qualidade por tema;
  - detecção de exposição de dado sensível.

- **Human-in-the-Loop (quando e como):** obrigatório em exceções, risco alto, baixa confiança, conformidade, dados incompletos ou casos sensíveis; o agente transfere com resumo, regras aplicadas, evidências e histórico.
- **Requisitos regulatórios aplicáveis:** LGPD e requisitos de auditoria/compliance levantados no discovery; demais regulações específicas da jornada/produto devem ser confirmadas com a harafaz.ia.
- **Requisitos de auditoria e rastreabilidade:** logs de conversa, decisão, ação automática, usuário, data/hora, versão da regra/checklist, justificativa humana e trilha completa de handoff.

## 7. Critérios de sucesso e KPIs

- **KPI 1 (valor atual -> meta):** tempo médio de atendimento/originação *(baseline a medir no piloto -> reduzir em 90 dias)*.
- **KPI 2 (valor atual -> meta):** FCR / taxa de resolução no primeiro contato *(baseline a medir -> aumento progressivo para demandas elegíveis)*.
- **KPI 3 (valor atual -> meta):** taxa de retrabalho / reincidência *(baseline a medir -> redução progressiva com base curada e automação assistida)*.
- **KPI 4 (valor atual -> meta):** reuso de dados/documentos entre jornadas *(baseline a medir -> aumento progressivo)*.
- **KPI 5 (valor atual -> meta):** NPS interno da rede *(baseline atual a confirmar -> aumento após implantação)*.
- **Horizonte de medição (30/60/90 dias):**
  - **30 dias:** adoção do canal/piloto, volume atendido, qualidade de classificação e baseline;
  - **60 dias:** FCR, escalonamento, backlog e SLA;
  - **90 dias:** redução de retrabalho/reincidência, NPS e evidência de valor.

## 8. Restrições, riscos e premissas

### 8.1 Restrições

- **Orçamento:** não explicitado no material; recomendada abordagem incremental por ondas.
- **Prazo:** roadmap sugerido entre 0 e 28 semanas, com piloto inicial em até 8 semanas e gestão de mudança estimada em 4–6 meses.
- **Tecnologia:** uso prioritário de Copilot Studio, Dataverse, Power Automate, canais Microsoft e integração progressiva com legados existentes.

### 8.2 Riscos

- **Risco:** manutenção do comportamento atual de contato direto na pessoa / duplicação de canais.  
  - **Impacto:** baixa adoção e pouca rastreabilidade.  
  - **Mitigação:** canal único mais simples, SLA visível, privacidade por caso e melhor experiência.

- **Risco:** qualidade e governança da base de conhecimento / normativos.  
  - **Impacto:** respostas imprecisas e risco operacional.  
  - **Mitigação:** curadoria contínua, versionamento e revisão periódica.

- **Risco:** integração com múltiplas esteiras e sistemas legados.  
  - **Impacto:** atraso no rollout e aumento de complexidade.  
  - **Mitigação:** piloto em 1–2 hubs/produtos prioritários e expansão por ondas.

- **Risco:** privacidade e sensibilidade de atendimento.  
  - **Impacto:** exposição indevida de dados e não conformidade.  
  - **Mitigação:** RBAC, segregação por caso/hub, DLP, auditoria e HITL.

- **Risco:** automação excessiva em decisões críticas.  
  - **Impacto:** erro operacional e risco regulatório.  
  - **Mitigação:** limites claros de autonomia e revisão humana obrigatória.

### 8.3 Premissas

1. A harafaz.ia manterá uma base de conhecimento curada e atualizada.
2. Haverá patrocínio operacional para impor registro único de case e reduzir uso de canais paralelos.
3. Os sistemas legados prioritários terão integração viável por etapas.
4. Haverá definição de donos de dados, SLAs e critérios de escalonamento por jornada.

## 9. Roadmap em ondas

### Onda 1 - Piloto

- **Escopo:** case único no Dataverse; agente no Copilot Studio para triagem e FAQ/coleta guiada; 1 jornada piloto e 1–2 canais prioritários; checklist/regras versionadas; dashboard inicial.
- **Duração:** 0–8 semanas.
- **Critério de saída:** piloto estabilizado, baseline medido, handoff funcional, telemetria ativa e evidência inicial de redução de esforço/retrabalho.

### Onda 2 - Expansão

- **Escopo:** ampliação de canais; integração das principais esteiras/legados; handoff estruturado entre jornadas; automações para temas recorrentes; expansão para 2–3 produtos/hubs prioritários.
- **Duração:** 9–16 semanas.
- **Critério de saída:** ganho comprovado em FCR/SLA, redução de escalonamento indevido, adoção ampliada e governança operacional funcionando.

### Onda 3 - Escala

- **Escopo:** omnicanalidade ampliada; mais automações assistidas com guardrails; analytics avançado; consolidação de governança, conectores, observabilidade e rollout amplo.
- **Duração:** 17–28 semanas.
- **Critério de saída:** operação escalável com observabilidade, segurança e governança consolidadas, além de roadmap contínuo de melhoria.

## 10. Perguntas para decisão de arquitetura alvo

- **Qual parte da jornada depende de dados governados?** classificação de demanda, consulta a normativos e regras vigentes, dados/documentos de clientes e operações, status de case, SLA, histórico, evidências e decisões.
- **Onde o contexto externo (Web IQ) é necessário?** em geral, baixo para o núcleo operacional; útil apenas para referências públicas regulatórias ou conteúdo externo controlado e aprovado.
- **Quais fluxos exigem aprovação humana?** conformidade, exceções, alto risco, baixa confiança do modelo e decisões que impactem cliente, crédito, elegibilidade ou tratativas sensíveis.
- **Quais componentes exigem maior observabilidade?** classificação/roteamento, handoff entre jornadas, integrações com legados, uso da base de conhecimento, latência/falhas de fluxo e auditoria de decisões.

## 11. Anexos opcionais

- **Diagrama de processo atual (AS-IS):** derivar do material de discovery e das entrevistas por jornada.
- **Diagrama de arquitetura alvo (TO-BE):** usar como base as arquiteturas de referência de Originação e Middle em Copilot Studio.
- **Políticas internas relevantes:** política de dados, identidade e acesso, LGPD, auditoria, governança de conectores, retenção e curadoria de conhecimento.
- **Referências técnicas:** Copilot Studio, Dataverse, Power Automate, analytics, handoff e políticas DLP / segurança Power Platform.
