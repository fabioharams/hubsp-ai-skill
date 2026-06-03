# PL 2338/2023 e aderencia de Microsoft Copilot Studio e Microsoft Foundry

## Visao executiva

O **PL 2338/2023** estabelece um marco baseado em direitos, classificacao de risco, transparencia, supervisao humana, governanca, rastreabilidade e prestacao de contas para sistemas de inteligencia artificial. A leitura das fontes oficiais indica que **Microsoft Copilot Studio** e **Microsoft Foundry** oferecem os blocos tecnicos e de governanca necessarios para atender grande parte dessas exigencias, especialmente quando combinados com **Microsoft Purview**, **Microsoft Entra**, **Microsoft Sentinel**, **Azure Monitor**, **Defender for Cloud** e **Azure AI Content Safety**.

O ponto central e este: **as ferramentas da Microsoft nao geram conformidade juridica automaticamente**, mas entregam os controles tecnicos, operacionais e de governanca necessarios para implementar guard rails, evaluators, monitoramento, rastreabilidade, protecao de dados, retencao, auditoria e supervisao humana em linha com os eixos do PL.

> Observacao: o **PL 2338/2023 ainda nao foi aprovado em definitivo**. Como a tramitacao legislativa segue em curso, o texto, os artigos de referencia, o escopo regulatorio e as datas de publicacao ainda podem sofrer alteracoes ate a conclusao do processo legislativo e eventual sancao.

## Fontes oficiais consideradas

### Fontes oficiais do PL 2338/2023

- Senado Federal, pagina da materia: https://www25.senado.leg.br/web/atividade/materias/-/materia/157233
- Senado Federal, autografo remetido a Camara: https://legis.senado.leg.br/sdleg-getter/documento?dm=9915448&ts=1774551291270&disposition=inline
- Senado Federal, texto inicial oficial: https://legis.senado.leg.br/sdleg-getter/documento?dm=9347593&ts=1774551274647&disposition=inline
- Senado Federal, consulta publica da materia: https://www12.senado.leg.br/ecidadania/visualizacaomateria?id=157233
- Camara dos Deputados, registro oficial da proposicao: https://dadosabertos.camara.leg.br/api/v2/proposicoes/2487262
- Camara dos Deputados, inteiro teor da proposicao na Camara: https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=2868197

### Fontes oficiais Microsoft

- Copilot Studio, seguranca e governanca: https://learn.microsoft.com/microsoft-copilot-studio/security-and-governance
- Copilot Studio, auditoria em Purview: https://learn.microsoft.com/microsoft-copilot-studio/admin-logging-copilot-studio
- Purview para Copilot Studio: https://learn.microsoft.com/purview/ai-copilot-studio
- Microsoft Foundry, Responsible AI: https://learn.microsoft.com/azure/foundry/responsible-use-of-ai-overview
- Microsoft Foundry, observability: https://learn.microsoft.com/azure/foundry/concepts/observability
- Purview para Microsoft Foundry: https://learn.microsoft.com/purview/ai-azure-foundry
- Prompt Shields em Azure AI Content Safety: https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection
- Gestao de compliance e seguranca no Foundry: https://learn.microsoft.com/azure/foundry/control-plane/how-to-manage-compliance-security
- Governanca regulatoria de apps de IA: https://learn.microsoft.com/security/security-for-ai/govern

## Leitura objetiva do PL

Para esta analise, a referencia juridica principal e o **autografo aprovado no Senado e remetido a Camara**, complementado pelo **texto inicial** para facilitar a identificacao dos artigos e da estrutura original da proposta. Pelas fontes oficiais do Senado, os eixos centrais do PL 2338/2023 incluem:

- **Direito a informacao previa sobre interacao com IA**.
- **Direito a explicacao, contestacao e intervencao humana**.
- **Nao discriminacao e correcao de vieses**.
- **Classificacao de risco e avaliacao de impacto algoritmico para sistemas de alto risco**.
- **Medidas de governanca, seguranca, confiabilidade e monitoramento continuo**.
- **Rastreabilidade, auditabilidade, responsabilizacao e prestacao de contas**.
- **Publicidade de informacoes e mecanismos de supervisao pela autoridade competente**.

Trechos oficiais relevantes, consistentes entre o texto inicial e a versao aprovada no Senado, incluem:

- **Art. 5o**: direito a informacao previa, explicacao, contestacao, participacao humana, nao discriminacao, privacidade e protecao de dados.
- **Art. 7o**: obrigacao de informar carater automatizado, operadores, medidas de governanca, papel de humanos, dados usados, medidas de seguranca, nao discriminacao e confiabilidade.
- **Art. 8o e 9o**: direito a explicacao, revisao, contestacao e solicitacao de intervencao humana.
- **Art. 12**: vedacao a discriminacao direta, indireta, ilegal ou abusiva.
- **Arts. 23 e 24**: avaliacao de impacto algoritmico com independencia funcional, mitigacao, monitoramento e registro de riscos residuais.
- **Art. 30**: codigos de boas praticas e governanca, mecanismos internos de supervisao, resposta a resultados prejudiciais e atualizacao com monitoramento continuo.
- **Art. 32**: fiscalizacao, regulamentacao e exigencia de publicizacao de informacoes.

## Como Copilot Studio e Microsoft Foundry respondem aos requisitos do PL

| Eixo do PL 2338/2023 | Leitura do requisito na fonte oficial | Como Microsoft Copilot Studio responde | Como Microsoft Foundry responde | Links oficiais Microsoft |
|---|---|---|---|---|
| **Transparencia e informacao previa** | Arts. 5o e 7o exigem informar interacao automatizada, operadores, dados usados, papel humano e medidas de governanca. | Copilot Studio permite governanca por ambiente, autenticacao, controles sobre knowledge sources, actions, connectors, skills, HTTP requests e publication to channels. Com Purview, tambem herda classificacao, trilha de auditoria e exibicao de sensibilidade em cenarios suportados. | Foundry permite documentar projeto, modelo, filtros e metricas; possui control plane, governanca centralizada e integracao com Purview para visibilidade sobre interacoes e classificacoes. | https://learn.microsoft.com/microsoft-copilot-studio/security-and-governance ; https://learn.microsoft.com/purview/ai-copilot-studio ; https://learn.microsoft.com/azure/foundry/control-plane/overview ; https://learn.microsoft.com/security/security-for-ai/govern |
| **Explicabilidade, contestacao e supervisao humana** | Arts. 5o, 8o e 9o tratam de explicacao, revisao, contestacao e intervencao humana. | Copilot Studio ajuda no desenho de workflows com autenticacao, aprovacao administrativa e controle de publicacao. E adequado para processos com humano no loop, especialmente quando o agente apenas recomenda, coleta contexto ou aciona fluxos supervisionados. | Foundry oferece tracing, evaluation e monitoring para entender chamadas, decisoes do agente, tool invocations e cadeias de execucao. Isso facilita explicar comportamento do sistema e implementar revisao humana em cenarios de maior risco. | https://learn.microsoft.com/microsoft-copilot-studio/security-and-governance ; https://learn.microsoft.com/azure/foundry/concepts/observability ; https://learn.microsoft.com/azure/foundry/responsible-use-of-ai-overview |
| **Nao discriminacao, seguranca e confiabilidade** | Art. 12 veda discriminacao; principios do PL incluem nao discriminacao, explicabilidade, auditabilidade, robustez e seguranca da informacao. | Copilot Studio se apoia em DLP, sensitivity labels, auditing, Sentinel e controles de autenticacao. Com Purview, permite monitorar interacoes, detectar comportamentos de risco e aplicar politicas para reduzir exposicao indevida. | Foundry traz built-in evaluators para safety and security, red teaming, prompt attack detection, content filters, Prompt Shields, monitoramento de riscos e integracao com Defender for Cloud. | https://learn.microsoft.com/purview/ai-copilot-studio ; https://learn.microsoft.com/azure/foundry/concepts/observability ; https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection ; https://learn.microsoft.com/azure/foundry/control-plane/how-to-manage-compliance-security |
| **Classificacao de risco e avaliacao de impacto algoritmico** | Arts. 23 e 24 exigem avaliacao de impacto com preparacao, cognicao do risco, mitigacao e monitoramento, especialmente para alto risco. | Copilot Studio ajuda em casos de menor autonomia e maior controle operacional, mas nao substitui o processo formal de avaliacao de impacto. Ele contribui com trilhas de auditoria, telemetria, DLP, governance by environment e logs de alteracoes de configuracao e uso. | Foundry e mais aderente para cenarios que exigem evidence pack tecnico: evaluators, red teaming, tracing, dashboards, content safety filter configurations, monitoramento e documentacao exportavel para fluxos de GRC e auditoria. | https://learn.microsoft.com/microsoft-copilot-studio/admin-logging-copilot-studio ; https://learn.microsoft.com/azure/foundry/concepts/observability ; https://learn.microsoft.com/security/security-for-ai/govern ; https://learn.microsoft.com/azure/foundry/responsible-use-of-ai-overview |
| **Governanca corporativa e monitoramento continuo** | Art. 30 fala em boas praticas, mecanismos internos de supervisao, resposta a resultados prejudiciais e atualizacao por monitoramento continuo. | Copilot Studio oferece data policy controls, bloqueio de publishing, environment routing, CMK, logs em Purview, integracao com Sentinel e administracao central no Power Platform admin center. | Foundry traz governanca em todo o lifecycle: Discover, Protect, Govern; integracao com Azure Monitor, Application Insights, Defender for Cloud, Purview e control plane para operacao em escala. | https://learn.microsoft.com/microsoft-copilot-studio/security-and-governance ; https://learn.microsoft.com/azure/foundry/responsible-use-of-ai-overview ; https://learn.microsoft.com/azure/foundry/control-plane/overview |
| **Rastreabilidade, auditoria e prestacao de contas** | O PL explicita rastreabilidade, auditabilidade, responsabilizacao e prestacao de contas como principios e mecanismos de governanca. | Copilot Studio registra eventos de criacao, alteracao, publicacao, compartilhamento, configuracao e interacao do usuario. Esses eventos podem ser pesquisados no Purview e analisados no DSPM for AI; integracao com Sentinel reforca SOC e resposta a incidentes. | Foundry integra auditoria e classificacao via Purview, activity explorer, retention, eDiscovery e monitoramento operacional por traces, logs e dashboards. Isso suporta trilha de decisao e evidencia para auditoria. | https://learn.microsoft.com/microsoft-copilot-studio/admin-logging-copilot-studio ; https://learn.microsoft.com/purview/ai-copilot-studio ; https://learn.microsoft.com/purview/ai-azure-foundry ; https://learn.microsoft.com/azure/foundry/concepts/observability |
| **Protecao de dados, retencao e investigacao** | O PL dialoga com privacidade, protecao de dados, responsabilizacao e fiscalizacao. | Com Purview, o Copilot Studio suporta auditing, classification, sensitivity labels, DLP, Insider Risk Management, Communication Compliance, eDiscovery, Data Lifecycle Management e Compliance Manager. | O mesmo conjunto e suportado para Foundry, desde que as configuracoes de Purview Data Security e collection policies sejam habilitadas. Isso e especialmente relevante para retencao de prompts, respostas e investigacao regulatoria. | https://learn.microsoft.com/purview/ai-copilot-studio ; https://learn.microsoft.com/purview/ai-azure-foundry |
| **Seguranca contra abuso, prompt injection e uso indevido** | O PL exige mitigacao de riscos, seguranca e monitoramento, sobretudo em cenarios sensiveis ou de alto risco. | Em Copilot Studio, a camada principal de controle esta na politica de conectores, autenticacao, publicacao, DLP, labels, auditoria e restricao de capacidades do agente. | Em Foundry, Azure AI Content Safety e Prompt Shields detectam user prompt attacks e document attacks; Defender for Cloud complementa com deteccao de jailbreak e riscos de workload. | https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection ; https://learn.microsoft.com/azure/foundry/control-plane/how-to-manage-compliance-security |

## Sintese executiva

Se a pergunta for se **Microsoft Copilot Studio** e **Microsoft Foundry** conseguem responder aos requisitos do PL 2338/2023, a resposta curta e **sim, em grande parte dos requisitos operacionais e de governanca**.

O racional e simples:

- **Copilot Studio** atende bem o que o PL demanda em **governanca operacional, controle de acesso, trilha de auditoria, DLP, rotulagem de sensibilidade, publicacao controlada e supervisao administrativa**.
- **Microsoft Foundry** atende melhor o que o PL demanda em **avaliacao de risco, evaluators, tracing, monitoramento continuo, evidencia tecnica, guard rails, content safety, red teaming e governanca de agentes em producao**.
- **Microsoft Purview** fecha a lacuna regulatoria em **classificacao, auditoria, retencao, eDiscovery, compliance evidence e controles de dados**.

## Trade-offs importantes

- **Copilot Studio** e mais forte para casos de uso com processo empresarial, canais Microsoft, conectores governados e menor complexidade tecnica.
- **Microsoft Foundry** e mais forte para casos de uso com modelos customizados, multiagente, observability aprofundada, pipeline de avaliacao e maior exigencia de GRC tecnico.
- Para cenarios de **alto risco**, a arquitetura alvo deveria combinar **Work IQ**, **Foundry IQ** e **Fabric IQ** com controles transversais de Purview, Entra, Sentinel e Defender, em vez de depender apenas de um builder de agente.

## Conclusao pratica

Para sustentar a afirmacao de que as ferramentas de IA da Microsoft conseguem atender as demandas do PL 2338/2023, a formulacao mais defensavel e esta:

> A Microsoft oferece, em fontes oficiais, os controles tecnicos e de governanca necessarios para implementar os principais requisitos operacionais associados ao PL 2338/2023, incluindo transparencia, supervisao humana, classificacao de risco, avaliacao e mitigacao de riscos, rastreabilidade, auditoria, protecao de dados, retencao, investigacao e monitoramento continuo. O atendimento juridico-material depende da configuracao correta desses controles, do desenho de processo, da documentacao de risco e da governanca corporativa da organizacao.

## Frase pronta para uso executivo

> Sob a otica de arquitetura e governanca, Microsoft Copilot Studio e Microsoft Foundry, combinados com Microsoft Purview, Entra, Sentinel, Defender for Cloud e Azure AI Content Safety, oferecem capacidade concreta para atender os eixos centrais do PL 2338/2023, com guard rails, evaluators, trilha de auditoria, supervisao humana, protecao de dados e monitoramento continuo em escala corporativa.