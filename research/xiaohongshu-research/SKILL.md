---
name: xiaohongshu-research
description: 通过 SandBase 搜索笔记、分析创作者、追踪话题趋势、研究用户行为。适用于小红书内容研究、种草分析、达人发现、竞品监控、话题追踪等场景。
---

# 小红书研究

小红书内容与创作者研究工具。搜索笔记、分析用户画像、追踪话题热度、研究消费趋势。使用前请阅读 [API 映射表](references/sandbase-api-map.md)。

## 调用 SandBase 能力

每次调用前先使用 `sandbase_describe_tool` 获取当前参数 schema，再使用 `sandbase_call_tool` 传入准确的 `tool_name`。

## 操作原则

- 仅用于公开内容的研究和分析，不发布、点赞或评论。
- 保留归因信息：笔记链接、用户名、互动数据、日期。
- 小红书数据反映消费趋势和种草行为，但不代表购买决策。
- 尊重创作者隐私，不追踪非公开信息。

## 工作流

### 1. 搜索与发现

使用 `xiaohongshu_app_v2_search_notes` 按关键词搜索笔记。
使用 `xiaohongshu_app_v2_search_users` 搜索创作者/品牌账号。
使用 `xiaohongshu_app_v2_topic_feed` 获取话题下的笔记流。
使用 `xiaohongshu_app_v2_topic_info` 获取话题热度信息。

### 2. 创作者分析

使用 `xiaohongshu_app_v2_user_info` 获取用户资料和粉丝数。
使用 `xiaohongshu_app_v2_user_posted_notes` 获取创作者发布的笔记。
使用 `xiaohongshu_app_v2_user_faved_notes` 分析收藏偏好。

### 3. 内容分析

使用 `xiaohongshu_app_v2_image_note_detail` 获取图文笔记详情。
使用 `xiaohongshu_app_v2_video_note_detail` 获取视频笔记详情。
使用 `xiaohongshu_app_v2_note_comments` 分析评论区互动。

### 4. 商品研究

使用 `xiaohongshu_app_v2_search_products` 搜索商品。
使用 `xiaohongshu_app_v2_product_detail` 获取商品详情。
使用 `xiaohongshu_app_v2_product_reviews` 获取商品评价。

## 输出

返回：搜索结果概览、笔记互动数据、创作者分析、话题趋势、消费洞察、竞品内容对比。

## 示例任务

- "搜索小红书上关于 [品牌/产品] 的笔记，分析用户评价。"
- "找出 [品类] 领域粉丝 5 万-50 万的小红书博主。"
- "追踪 #[话题标签] 最近的热度和内容趋势。"
- "分析 @[账号] 的内容策略 — 发布频率、爆款特征、互动率。"
- "[竞品 A] 和 [竞品 B] 在小红书上的种草内容对比。"
