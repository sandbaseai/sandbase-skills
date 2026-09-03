# SandBase Task Source Import API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Read a task source page as Markdown | `context_dev_scrape_markdown` |
| Extract task fields from a structured web page | `context_dev_extract_structured_data` |

Use these capabilities only when the user supplies an authorized source URL. For a local TASKS.md file or pasted text, work directly from that input.
