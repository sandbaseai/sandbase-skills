# SandBase Support Evidence API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Search public status pages, documentation, and known issues | `tavily_search` |
| Read an authorized knowledge-base or incident page | `context_dev_scrape_markdown` |

Use these capabilities for public or user-authorized evidence only. Keep triage read-only unless the user separately authorizes a response, assignment, or escalation.
