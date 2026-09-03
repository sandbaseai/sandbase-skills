# SandBase Cash-Flow Input API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Extract structured AR, AP, cash, or cost data from an authorized report page | `context_dev_extract_structured_data` |
| Read an authorized report page as Markdown | `context_dev_scrape_markdown` |

Use supplied or authorized data only. Keep forecasts separate from source records and label assumptions, missing opening cash, and confidence limits.
