## 📝 A. Executable Code Examples

### A.1 Python — Microsoft Agent Framework Using a Foundry Model

> This example constructs an Agent Framework application that calls a model through Foundry. Agent Framework does not supply managed hosting; the application remains responsible for hosting, scaling, identity, state and operations unless it is separately deployed as a Foundry hosted agent.

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
            model=os.getenv("FOUNDRY_MODEL", "gpt-4.1-mini"),
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

> Executive note: **Microsoft Agent Framework** supports Python and .NET, with Go in public preview as of July 20, 2026. This Node.js example uses a channel-specific SDK and integrates with governed corporate services or separately hosted agents.

```javascript
const { ConversationBot } = require("@microsoft/teams-ai");

const config = {
    // Exemplo simplificado: carregue credenciais/config do ambiente.
};

const AGENT_INSTRUCTIONS = `
You are a Sales Analysis Agent.

SCOPE:
- Answer questions about sales pipeline, segments, forecasts
- Provide data-driven recommendations
- Escalate sensitive requests

BOUNDARIES:
- Cannot approve discounts
- Cannot access PII (RLS enforced)
- Can see aggregated segments and regions

TONE:
- Professional, concise, data-focused
- Always cite source
- Transparency: "Confidence: High/Medium/Low"
`;

const bot = new ConversationBot({
  adapterConfig: config,
    requestHandler: async (context) => {
    const userMessage = context.activity.text;
    console.log(`User: ${userMessage}`);
        // In production, delegate to a governed agent endpoint.
        await context.sendActivity("Processing your request with policy controls...");
  }
});

module.exports = bot;
```

---

