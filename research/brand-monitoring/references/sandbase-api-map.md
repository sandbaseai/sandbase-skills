# SandBase Brand Monitoring API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `twitter_web_search_timeline` | Search brand mentions on Twitter/X. |
| `twitter_web_trending` | Check if brand is trending. |
| `reddit_app_dynamic_search` | Search brand discussions on Reddit. |
| `tavily_search` | Search news and web for brand mentions. |
| `google_news_bulk_articles` | Search news articles about the brand. |
| `xiaohongshu_app_v2_search_notes` | Search brand mentions on 小红书. |
| `weibo_web_search` | Search brand mentions on 微博. |

Monitor across multiple platforms for comprehensive coverage.
