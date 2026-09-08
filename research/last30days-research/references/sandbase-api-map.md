# SandBase Last 30 Days Research API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `tavily_search` | Web/news search with date filtering (days parameter). |
| `google_news_bulk_articles` | News articles search. |
| `exa_search` | Semantic web search with date filters. |
| `twitter_web_search_timeline` | Twitter/X discussions and mentions. |
| `reddit_app_dynamic_search` | Reddit discussions. |
| `youtube_web_v2_general_search` | YouTube content. |
| `xiaohongshu_app_v2_search_notes` | 小红书 content (Chinese market). |
| `weibo_web_search` | 微博 content (Chinese market). |

Use at least 3-4 platforms for comprehensive recent-history coverage.
