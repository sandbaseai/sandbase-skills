# SandBase 微博 API Map

下列能力标识仅用于检索，不是直接调用的 MCP 工具名。先用 `sandbase_discover(q: "<供应商和能力>")` 查找匹配端点，再将返回的 `name` 传给 `sandbase_inspect`，读取当前 `inputSchema`、价格和 `execute_as`。按模板调用 `sandbase_run`，将 `execute_as.arguments.name` 作为 `name`，并传入符合 schema 的 `arguments`。若返回 `run_id`，在任务预算内通过 `sandbase_run_get(run_id: "<返回的 run_id>")` 查询至 `completed` 或 `failed`；超出预算时报告待完成状态，失败时报告错误，不自动重复提交。

| Capability identifier | 用途 |
|---|---|
| `weibo_web_hot_search` | 获取实时热搜榜。 |
| `weibo_web_trend_top` | 获取趋势排行。 |
| `weibo_web_search` | 按关键词搜索微博。 |
| `weibo_web_search_topics` | 搜索话题。 |
| `weibo_web_channel_feed` | 获取频道内容流。 |
| `weibo_web_user_info` | 获取用户资料和统计。 |
| `weibo_web_user_posts` | 获取用户发布的微博。 |
| `weibo_web_post_detail` | 获取微博详情和互动数据。 |
| `weibo_web_post_comments` | 获取评论区内容。 |
| `weibo_web_comment_replies` | 获取评论回复。 |
| `weibo_web_config_list` | 获取微博配置信息。 |

仅用于公开内容研究。不发布、转发或评论。
