# SandBase Tavily API Map

Use these tools through the SandBase gateway. Before each call, use `sandbase_describe_tool` to obtain current parameters, then use `sandbase_call_tool` with the exact tool name.

| Tool name | Use it for |
|---|---|
| `tavily_search` | AI-optimized web search with depth control, topic filtering, and domain filtering. |
| `tavily_extract` | Extract clean, readable content from one or more URLs. |
| `tavily_map` | Discover site structure and list all pages on a website. |

Use appropriate search depth for the task. Cite all sources with URLs.
