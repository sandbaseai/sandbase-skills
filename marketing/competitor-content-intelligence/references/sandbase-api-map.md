# SandBase Content Intelligence API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `exa_search` | Discover relevant competitor and source pages. |
| `cloudsway_search` | Find complementary public web sources. |
| `context_dev_scrape_markdown` | Extract a selected public page as clean Markdown. |
| `dataforseo_v3_on_page_content_parsing_live` | Parse a selected page into structured content. |
| `dataforseo_v3_content_analysis_search_live` | Validate broader topical coverage and content patterns. |

Use only the sources needed for the decision. Cite page URLs and do not reproduce long competitor passages.
