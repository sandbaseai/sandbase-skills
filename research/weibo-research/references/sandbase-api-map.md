# SandBase 微博 API Map

通过 SandBase gateway 调用。每次调用前先用 `sandbase_describe_tool` 获取参数，再用 `sandbase_call_tool` 传入准确的 tool name。

| Tool name | 用途 |
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
