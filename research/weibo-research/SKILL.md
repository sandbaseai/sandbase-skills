---
name: weibo-research
description: 通过 SandBase 搜索微博、追踪热搜、分析用户和话题趋势。适用于微博舆情监控、热点追踪、用户分析、品牌口碑研究等场景。
---

# 微博研究

微博热点与舆情研究工具。搜索内容、追踪热搜趋势、分析用户画像和话题传播。使用前请阅读 [API 映射表](references/sandbase-api-map.md)。

## 调用 SandBase 能力

每次调用前先使用 `sandbase_describe_tool` 获取当前参数 schema，再使用 `sandbase_call_tool` 传入准确的 `tool_name`。

## 操作原则

- 仅用于公开内容的研究和分析，不发布或互动。
- 保留归因：微博链接、用户名、互动数据、时间。
- 热搜数据时效性强，注意标注观察时间。
- 微博内容反映中国社交舆论趋势，但不代表全民观点。

## 工作流

### 1. 热搜与趋势

使用 `weibo_web_hot_search` 获取实时热搜榜。
使用 `weibo_web_trend_top` 获取趋势排行。
使用 `weibo_web_search_topics` 搜索话题。

### 2. 内容搜索

使用 `weibo_web_search` 按关键词搜索微博。
使用 `weibo_web_channel_feed` 获取频道内容。

### 3. 用户分析

使用 `weibo_web_user_info` 获取用户资料和统计。
使用 `weibo_web_user_posts` 获取用户发布的微博。

### 4. 内容详情

使用 `weibo_web_post_detail` 获取微博详情。
使用 `weibo_web_post_comments` 获取评论区内容。
使用 `weibo_web_comment_replies` 获取评论回复。

## 输出

返回：热搜榜单、搜索结果、用户画像、话题热度趋势、评论区舆情分析。

## 示例任务

- "现在微博热搜榜上有哪些热点话题？"
- "搜索微博上关于 [品牌/事件] 的讨论，分析舆情走向。"
- "分析 @[账号] 的微博运营数据 — 发博频率、互动率、内容主题。"
- "追踪 #[话题标签]# 的热度变化和讨论内容。"
- "[品牌] 最近在微博上的口碑如何？正负面舆情对比。"
