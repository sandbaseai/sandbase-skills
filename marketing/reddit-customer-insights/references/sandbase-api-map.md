# SandBase Reddit API Map

Use the capability identifiers below as discovery hints, not MCP tool names. Find the matching endpoint with `sandbase_discover(q: "<provider and capability>")`; use its returned `name` in `sandbase_inspect(name: "<returned name>")`. Read `inputSchema`, pricing, and `execute_as`, then call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If a `run_id` is returned, poll `sandbase_run_get(run_id: "<returned run_id>")` within the task budget until `completed` or `failed`; report pending or failed runs without resubmitting them automatically.

| Capability identifier | Use it for |
|---|---|
| `reddit_app_search_typeahead` | Discover relevant communities and search queries. |
| `reddit_app_dynamic_search` | Search public posts, comments, and communities. |
| `reddit_app_post_details` | Inspect selected discussion context. |
| `reddit_app_topic_feed` | Collect a public topic feed. |

Use these capabilities only to collect public research evidence. Do not post, vote, message, or alter Reddit accounts.
