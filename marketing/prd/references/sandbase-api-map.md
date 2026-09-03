# SandBase PRD Research API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Search current product, market, and technical evidence | `tavily_search` |
| Read an authorized product, documentation, or competitor page | `context_dev_scrape_markdown` |

Use external evidence only when it materially informs requirements. Cite sources and mark unresolved product decisions as TBD.
