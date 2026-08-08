# SandBase Exa API Map

Use these tools through the SandBase gateway. Before each call, use `sandbase_describe_tool` to obtain current parameters, then use `sandbase_call_tool` with the exact tool name.

| Tool name | Use it for | Availability |
|---|---|---|
| `exa_search` | Discover web sources with optional highlights, summaries, or text. | Available |
| `exa_contents` | Extract selected URLs as text, highlights, summaries, or subpages. | Use when available in the current gateway. |

Search before extracting. If `exa_contents` is unavailable, return the selected search results and name the extraction gap. Do not call Exa Answer or Exa Agent; the user's Agent/LLM synthesizes the evidence.
