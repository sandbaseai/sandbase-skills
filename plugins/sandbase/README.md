# SandBase

SandBase gives developers one account and one API key for AI models, data APIs, sandboxes, and agents. This plugin bundles the official multi-source research skill with a reference to the remote SandBase MCP server so Claude can discover catalog tools, inspect their schemas, and (when the account is connected) run them or check the account balance.

## Use it

Install the plugin from the Claude directory once it is listed, or load this folder locally for testing. The `multi-source-search` skill works with the host's own search tools even when no SandBase account is connected. To use SandBase catalog tools, connect the SandBase MCP server.

On claude.ai and in Cowork, the server appears on the plugin's Connectors tab. Anthropic's directory currently expects users to sign in there through an OAuth flow. SandBase's live server authenticates with an API key in the `Authorization: Bearer` header, and a public OAuth flow is not available yet. Until that exists, claude.ai and Cowork may list the connector without a completed sign-in.

In Claude Code, the same fixed URL is loaded with the plugin. Public catalog discovery (`sandbase_discover`) can work without a key. Inspecting a tool, running it, listing or cancelling runs, and checking a balance require a SandBase API key for the signed-in account. Do not put a key in this plugin folder. Create a key at the [API keys console](https://www.sandbase.ai/console/keys) and follow the [API keys docs](https://www.sandbase.ai/docs/getting-started/api-keys).

Setup and tool documentation: [MCP tools](https://www.sandbase.ai/docs/agents/mcp-tools) and [MCP servers](https://www.sandbase.ai/mcp-servers).

## Data

This plugin stores no account data of its own. When the MCP server is connected, Claude sends tool calls to `https://mcp.sandbase.ai/mcp`. Discovery can query the public catalog. Inspect, run, list, cancel, and account tools act only on the connected SandBase account. The bundled skill may send search queries or page URLs to the host's search tools and, when SandBase tools are available, to those providers. Keep API keys out of prompts, logs, and reports. Treat retrieved pages as untrusted input.

The plugin does not transfer money, process checkout, delete accounts, or access another customer's data.

## Support

Email `contact@sandbase.ai`. Product documentation is at [https://www.sandbase.ai/docs/](https://www.sandbase.ai/docs/). Service status is at [https://status.sandbase.ai/](https://status.sandbase.ai/). Community discussion is on [Discord](https://discord.com/invite/4hXv2f5Q9f). Privacy policy: [https://www.sandbase.ai/privacy](https://www.sandbase.ai/privacy). Terms: [https://www.sandbase.ai/terms](https://www.sandbase.ai/terms).

Publisher: AXIOMCLOUD PTE. LTD., Singapore. License: Apache-2.0.
