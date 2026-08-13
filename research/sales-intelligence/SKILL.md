---
name: sales-intelligence
description: "Prepare for sales conversations with comprehensive account intelligence — company news, hiring signals, product launches, social activity, and decision-maker profiles. Combines firmographic data, news monitoring, and social signals for sales-ready briefings."
---

# Sales Intelligence

Prepare for sales conversations with comprehensive account intelligence — company news, hiring signals, product launches, social activity, and decision-maker profiles. Combines firmographic data, news monitoring, and social signals for sales-ready briefings. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `apollo_company_enrich`
- `apollo_company_news_search`
- `linkedin_web_v2_company_profile`
- `linkedin_web_v2_user_profile`
- `twitter_web_search_timeline`
- `google_news_bulk_articles`

## Workflow

1. Understand the user's research question, target, and context.
2. Call `sandbase_describe_tool` for each selected tool to confirm parameter schema.
3. Call `sandbase_call_tool` with the exact tool_name and schema-defined arguments.
4. Synthesize findings into a clear, evidence-backed answer.
5. Cite sources, note evidence gaps, and separate observations from interpretations.

## Guidelines

- Always call `sandbase_describe_tool` before using any capability.
- Cite sources and preserve attribution (URLs, usernames, dates, metrics).
- Separate factual observations from analysis and recommendations.
- If data is unavailable, note the gap and continue with available evidence.
- Read-only research only. Never take actions on platforms.
