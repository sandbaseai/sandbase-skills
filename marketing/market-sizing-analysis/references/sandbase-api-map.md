# SandBase Market Sizing Research API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Search for current market, company, and industry evidence | `tavily_search` |
| Find semantically relevant primary and high-quality secondary sources | `exa_search` |

Record source URLs, publication dates, geography, units, and assumptions. Never convert unavailable data into a fabricated estimate.
