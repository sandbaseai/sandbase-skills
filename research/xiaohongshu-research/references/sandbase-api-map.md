# SandBase 小红书 API Map

下列能力标识仅用于检索，不是直接调用的 MCP 工具名。先用 `sandbase_discover(q: "<供应商和能力>")` 查找匹配端点，再将返回的 `name` 传给 `sandbase_inspect`，读取当前 `inputSchema`、价格和 `execute_as`。按模板调用 `sandbase_run`，将 `execute_as.arguments.name` 作为 `name`，并传入符合 schema 的 `arguments`。若返回 `run_id`，在任务预算内通过 `sandbase_run_get(run_id: "<返回的 run_id>")` 查询至 `completed` 或 `failed`；超出预算时报告待完成状态，失败时报告错误，不自动重复提交。

| Capability identifier | 用途 |
|---|---|
| `xiaohongshu_app_v2_search_notes` | 按关键词搜索笔记。 |
| `xiaohongshu_app_v2_search_users` | 搜索用户/创作者。 |
| `xiaohongshu_app_v2_search_products` | 搜索商品。 |
| `xiaohongshu_app_v2_search_groups` | 搜索群组。 |
| `xiaohongshu_app_v2_topic_feed` | 获取话题下的笔记流。 |
| `xiaohongshu_app_v2_topic_info` | 获取话题热度和信息。 |
| `xiaohongshu_app_v2_user_info` | 获取用户资料和统计。 |
| `xiaohongshu_app_v2_user_posted_notes` | 获取用户发布的笔记。 |
| `xiaohongshu_app_v2_user_faved_notes` | 获取用户收藏的笔记。 |
| `xiaohongshu_app_v2_image_note_detail` | 获取图文笔记详情。 |
| `xiaohongshu_app_v2_video_note_detail` | 获取视频笔记详情。 |
| `xiaohongshu_app_v2_note_comments` | 获取笔记评论。 |
| `xiaohongshu_app_v2_note_sub_comments` | 获取评论回复。 |
| `xiaohongshu_app_v2_product_detail` | 获取商品详情。 |
| `xiaohongshu_app_v2_product_reviews` | 获取商品评价。 |
| `xiaohongshu_app_v2_product_recommendations` | 获取推荐商品。 |

仅用于公开内容研究。不发布、点赞或评论。
