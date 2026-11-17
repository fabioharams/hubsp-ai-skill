## 📝 A. Executable Code Examples

### A.1 Python — Microsoft Agent Framework Using a Foundry Model

> This example constructs an Agent Framework application that calls a model through Foundry. Agent Framework does not supply managed hosting; the application remains responsible for hosting, scaling, identity, state and operations unless it is separately deployed as a Foundry hosted agent.

Lifecycle checked **2026-11-17**: .NET/Python core is GA; integrations can remain prerelease. Agent Framework Python 1.25 requires **Python 3.11+**. The `gpt-5.4-mini` fallback is an illustrative deployment name, not an automatically provisioned model; use an existing approved deployment. See [package requirements](https://learn.microsoft.com/agent-framework/support/upgrade/python-2026-significant-changes) and the [model lifecycle schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule).

```python
# agent_framework_foundry_example.py
import asyncio
import os

from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

load_dotenv()


@tool(approval_mode="always_require")
def get_top_product_by_margin(quarter: str, region: str) -> str:
    """Skill de exemplo: em producao, conecte ao seu data product governado."""
    return f"Top produto por margem em {quarter} na regiao {region}: Contoso Analytics Suite (32.4%)."


async def main() -> None:
    credential = AzureCliCredential()
    try:
        client = FoundryChatClient(
            project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
            model=os.getenv("FOUNDRY_MODEL", "gpt-5.4-mini"),
            credential=credential,
        )

        agent = Agent(
            client=client,
            name="SalesAnalysisAgent",
            instructions=(
                "Voce e um agente de analise comercial. "
                "Responda com dados objetivos, cite fonte e nao aprove descontos."
            ),
            tools=[get_top_product_by_margin],
        )

        # Explicit session for multi-turn conversation with controlled state.
        session = agent.create_session()

        result_1 = await agent.run(
            "Qual foi o produto com maior margem no Q3 2026 em LATAM?",
            session=session,
        )
        print("Turn 1:", result_1.text)

        result_2 = await agent.run(
            "Now explain in 3 bullets the reason and include an upsell recommendation.",
            session=session,
        )
        print("Turn 2:", result_2.text)
    finally:
        await credential.close()


if __name__ == "__main__":
    asyncio.run(main())
```

### A.2 C# — Microsoft Agent Framework (.NET)

```csharp
using Azure.AI.OpenAI;
using Azure.Identity;
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;
using OpenAI.Chat;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deploymentName = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME")
    ?? "gpt-5.4-mini";

// Em producao, prefira ManagedIdentityCredential quando aplicavel.
AIAgent agent = new AzureOpenAIClient(new Uri(endpoint), new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        name: "SalesAnalysisAgent",
        instructions: "You are a sales analysis agent. Cite data sources and never approve discounts.",
        tools: [AIFunctionFactory.Create(GetTopProductByMargin)]);

AgentSession session = await agent.CreateSessionAsync();

var response1 = await agent.RunAsync("What is the top product by margin in Q3 2026 for LATAM?", session);
Console.WriteLine($"Turn 1: {response1}");

var response2 = await agent.RunAsync("Summarize in 3 bullets and propose one upsell action.", session);
Console.WriteLine($"Turn 2: {response2}");

static string GetTopProductByMargin(string quarter, string region)
    => $"Top product by margin in {quarter} for {region}: Contoso Analytics Suite (32.4%).";
```

### A.3 Node.js — Channel integration (outside the MAF core)

> Lifecycle checked **2026-11-17**: Agent Framework .NET/Python core is GA; Go remains public preview. Go can invoke existing server-side Foundry agents but lacks the documented hosted-deployment helpers. Hosting adapters remain prerelease. See [Agent Framework](https://learn.microsoft.com/agent-framework/overview/) and [hosting support](https://learn.microsoft.com/agent-framework/hosting/foundry-hosted-agent).

Use the current **Teams SDK**, which has stable released tracks. The old Teams AI Library example used an unsupported SDK; see [Microsoft's migration guidance](https://learn.microsoft.com/microsoftteams/platform/legacy-tools-sdks). Save this JavaScript module as `teams-channel.mjs` in a configured Teams SDK project with authentication and channel registration. It only acknowledges a message; connect the approved agent endpoint before enabling business actions. The [official runtime example](https://learn.microsoft.com/microsoftteams/platform/agents-in-teams/port-slack-bolt-javascript-app#initialize-the-runtime) uses `App` from `@microsoft/teams.apps`.

```javascript
import { App } from "@microsoft/teams.apps";

const app = new App();

app.on("message", async ({ send }) => {
    await send("Request received. This channel sample does not execute business actions.");
});

app.start().catch((error) => {
    console.error("Teams application startup failed:", error);
    process.exitCode = 1;
});

export default app;
```

---

