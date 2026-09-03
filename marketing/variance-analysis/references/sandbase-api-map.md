# SandBase Variance Input API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Extract tabular or structured values from an authorized report page | `context_dev_extract_structured_data` |
| Read an authorized report page as Markdown | `context_dev_scrape_markdown` |

Treat extracted values as inputs to verify, not posted accounting records. Do not alter source reports or publish financial commentary without authorization.
