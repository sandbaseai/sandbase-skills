# SandBase Sales Evidence API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Read an authorized product, pricing, proof, or competitor page | `context_dev_scrape_markdown` |
| Search for current public market and competitor evidence | `tavily_search` |

Use evidence to support claims, not invent them. Do not send collateral, publish pages, or contact prospects without explicit authorization.
