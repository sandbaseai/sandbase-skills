# SandBase Meeting Source API Map

Use these exact SandBase `tool_name` values through `sandbase_call_tool`. Before each call, use `sandbase_describe_tool` to obtain the current input schema and pass only schema-defined arguments.

| Purpose | tool_name |
|---|---|
| Read an authorized transcript or notes page | `context_dev_scrape_markdown` |
| Retrieve captions from a published YouTube recording | `youtube_web_v2_video_captions` |

Use only sources the user is authorized to access. Do not publish minutes or create external tasks without explicit authorization.
