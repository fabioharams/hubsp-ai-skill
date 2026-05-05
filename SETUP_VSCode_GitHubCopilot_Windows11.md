# Setup no Windows 11 para usar esta Skill no VS Code + GitHub Copilot

Este guia padroniza o ambiente para usar a skill deste projeto em qualquer maquina com Windows 11.

## 1. Pre-requisitos

- Windows 11 atualizado
- VS Code instalado (versao estavel ou Insiders)
- Conta GitHub com licenca ativa do GitHub Copilot
- Acesso a internet para login e sincronizacao

## 2. Estrutura de arquivos (neste projeto)

Arquivo de skill padronizado:

- `SKILL.md`

Observacao: o arquivo foi renomeado para `SKILL.md` para seguir o padrao de skills e reduzir ambiguidades entre ambientes.

## 3. Instalar extensoes no VS Code

No VS Code, abra Extensions e instale:

- GitHub Copilot
- GitHub Copilot Chat

## 4. Autenticacao no GitHub Copilot

1. Abra o VS Code.
2. Clique no icone de conta (canto inferior esquerdo ou superior direito).
3. Faca Sign in with GitHub.
4. Autorize o VS Code no navegador.
5. Confirme que o Copilot esta ativo (icone/status do Copilot no editor).

## 5. Abrir o workspace correto

1. Abra a pasta do projeto no VS Code:
   - `c:\Users\fabioh\OneDrive - Microsoft\AGENT\HARASKILL`
2. Confirme que o arquivo `SKILL.md` esta na raiz da pasta.

## 6. Como usar a skill na pratica (modo seguro e portavel)

Como forma mais confiavel entre maquinas, use a skill como contexto explicito no chat.

### Fluxo recomendado

1. Abra o Chat do Copilot no VS Code.
2. Use Add Context e selecione `SKILL.md`.
3. Faça seu pedido de arquitetura/estrategia.

Exemplo de prompt:

```text
Use o SKILL.md como base e proponha uma arquitetura de adocao de agentes de IA para a area financeira, com foco em governanca, seguranca e rollout em 90 dias.
```

## 7. Opcional: instrucoes persistentes no repositorio

Se quiser orientar o Copilot automaticamente neste projeto, crie o arquivo `.github/copilot-instructions.md` com algo como:

```md
Sempre considerar o contexto e as regras definidas em SKILL.md para respostas sobre estrategia de adocao de agentes de IA.
Priorizar recomendacoes em pt-BR com foco em arquitetura corporativa, governanca, seguranca e roadmap por fases.
```

Isso melhora consistencia, mas ainda e recomendado anexar `SKILL.md` no chat para garantir grounding.

## 8. Checklist de validacao

- Copilot e Copilot Chat instalados
- Login GitHub concluido no VS Code
- Projeto aberto na pasta correta
- `SKILL.md` presente e legivel
- `SKILL.md` anexado no contexto do chat
- Respostas alinhadas com o formato esperado (visao executiva, arquitetura, governanca, fases, KPIs e riscos)

## 9. Troubleshooting rapido

### Copilot nao responde ou aparece offline

- Verifique internet e proxy corporativo
- Refaca o Sign out/Sign in do GitHub no VS Code
- Atualize VS Code e extensoes do Copilot

### Resposta muito generica

- Anexe novamente `SKILL.md` no Add Context
- Torne o prompt mais especifico (area, prazo, restricoes, KPIs)

### Comportamento diferente em outra maquina

- Verifique versao do VS Code e extensoes
- Confirme se a conta GitHub e a mesma
- Confirme que o arquivo `SKILL.md` e o mesmo (sincronizado)

## 10. Recomendacao de operacao para equipe

- Versionar `SKILL.md` e este guia no repositorio
- Usar prompts com estrutura fixa (contexto, objetivo, restricoes, formato de saida)
- Revisar o `SKILL.md` a cada ciclo de aprendizado (mensal ou bimestral)
