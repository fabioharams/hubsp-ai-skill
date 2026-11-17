# Setup Guide: Using hubsp-ai-skill Across Platforms

This guide covers how to set up and use the hubsp-ai-skill across different platforms and tools. Select the platform that matches your environment and workflow.

Microsoft product lifecycle claims were checked on **2026-11-17**; see the [lifecycle register](../PRODUCT_LIFECYCLE_AUDIT.md). Third-party client setup and plan entitlements are outside that verification.

## How to use in Visual Studio Code

Prerequisites:

- VS Code, the GitHub Copilot Chat extension and an active GitHub Copilot subscription.
- The [Microsoft Learn MCP Server](https://learn.microsoft.com/training/support/mcp-get-started) configured in VS Code. This skill requires the server to retrieve current, authoritative Microsoft documentation and validate product capabilities, limits and recommendations.

1. Clone and open the repository:

   ```bash
   git clone https://github.com/<your-org>/hubsp-ai-skill.git
   code hubsp-ai-skill
   ```

2. Open Copilot Chat (chat icon in the sidebar or `Ctrl+Alt+I` / `Cmd+Alt+I`) and use Agent mode.
3. The `.github/copilot-instructions.md` file is automatically loaded as workspace context, ensuring the executive response format is applied consistently.
4. Bring a file into the conversation context in one of these ways:
   - Type `#` and select the file (e.g., `#SKILL.md`).
   - Drag the file from the Explorer into the chat panel.
   - Open the file in the editor and reference it with `#file`.
5. Recommended flow: start with `SKILL.md` and let the agent load one file from `references/` or `chapters/` on demand, based on the topic of the question. Do not attach the complete `chapters/` folder.

For topics beyond the seven curated references, open `AI_Agent_Adoption_Strategy_Final_2.md`, choose the relevant chapter group and load only the chapter or chapters required by the request. This progressive-disclosure approach keeps the context focused and avoids loading the full knowledge base.

## How to use in Claude Desktop

Claude custom skills use progressive disclosure and are uploaded as a ZIP package. Skills are available on Free, Pro, Max, Team and Enterprise plans, but **Code execution and file creation** must be enabled.

1. From the parent directory of this repository, create a ZIP whose root is the `hubsp-ai-skill/` folder:

   ```bash
   cd ..
   zip -r hubsp-ai-skill.zip hubsp-ai-skill \
     -x "hubsp-ai-skill/.git/*"
   ```

2. In Claude Desktop, enable the required capability:
   - Free, Pro or Max: open **Settings > Capabilities** and enable **Code execution and file creation**.
   - Team or Enterprise: an owner must enable **Code execution and file creation** and **Skills** under **Organization settings > Skills**.
3. Open **Customize > Skills**.
4. Select **+ > Create skill > Upload a skill** and upload `hubsp-ai-skill.zip`.
5. Confirm that the skill appears in the list and toggle it on.
6. Start a new chat, attach the completed questionnaire or another scenario document, and apply the universal compact prompt:

   > Apply hubsp-ai-skill to the attached scenario document. Recommend the simplest viable Microsoft architecture and save the complete recommendation to `doc/recommendation-output.md`. Treat missing decision-critical information as explicit assumptions or validation gates; do not invent facts.

7. Claude loads the skill instructions dynamically, maps the attached document to the questionnaire fields and uses it as case context. The document can use any clear structure.
8. After changing this repository, rebuild the ZIP and replace the uploaded skill so Claude uses the latest version.

Review the ZIP contents before uploading, especially if scripts or external dependencies are added later. Custom skills can execute code, so do not include credentials or secrets.

Official Anthropic references:

- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)

## How to use in Microsoft Scout

> **Preview notice (checked 2026-11-17):** the [current Microsoft Scout overview](https://learn.microsoft.com/microsoft-scout/overview) still identifies the desktop application as **Frontier preview**. Availability and behavior can change; preview features might not reach GA.

Current prerequisites include Windows 11 or macOS 12+, a Microsoft 365 work or school account, Microsoft 365 Copilot access, a GitHub Copilot Business or Enterprise license, local installation permission and administrator enablement for the Frontier preview.

1. Join the [Microsoft Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/) and confirm that your administrator has enabled Microsoft Scout access.
2. [Download Microsoft Scout](https://aka.ms/msscout), install it and sign in to both Microsoft 365 and GitHub when prompted.
3. Set this repository, or the project directory containing the scenario input document, as the Scout workspace.
4. From this repository root, install the complete skill in Scout's global skills directory so its references and chapters remain available:

   ```bash
   mkdir -p ~/.copilot/skills/hubsp-ai-skill
   rsync -a --exclude '.git' ./ ~/.copilot/skills/hubsp-ai-skill/
   ```

5. Start a new conversation. Scout discovers custom skills at the beginning of future conversations; loaded skills appear in the conversation context.
6. Attach the completed questionnaire or another scenario document and ask Scout to apply the skill:

   > Apply hubsp-ai-skill to the attached scenario document. Recommend the simplest viable Microsoft architecture and save the complete recommendation to `doc/recommendation-output.md`. Treat missing decision-critical information as explicit assumptions or validation gates; do not invent facts.

7. Keep **Auto-approve** disabled while validating the skill. Review requests to run shell commands, write files, use the browser or act on Microsoft 365 data before approving them.
8. To update the installed skill after repository changes, rerun the `rsync` command and begin a new conversation.

Scout operates within the configured workspace and your existing permissions. Custom skills are not validated by Microsoft, so review generated recommendations and all sensitive actions before approval. Microsoft 365 data processed through GitHub Copilot can be subject to different protection and data-processing terms than data processed entirely within Microsoft 365.

Official Microsoft references:

- [Microsoft Scout overview](https://learn.microsoft.com/microsoft-scout/overview)
- [Get started with Microsoft Scout](https://learn.microsoft.com/microsoft-scout/get-started)
- [Use Microsoft Scout](https://learn.microsoft.com/microsoft-scout/use-microsoft-scout)
- [Microsoft Scout common questions](https://learn.microsoft.com/microsoft-scout/faq)

## How to use in the GitHub Copilot App

Prerequisites: GitHub Copilot app with repository access and an active GitHub Copilot subscription.

1. Open this repository in the app as a workspace/project.
2. Start a chat in Agent mode.
3. Attach `SKILL.md` and one completed questionnaire or equivalent scenario document.
4. Use the universal compact prompt. The skill loads only the relevant files from `references/` or `chapters/` when additional depth is required.
