---
name: reddit-customer-insights
description: Discover evidence-backed customer language, pain points, objections, and buying triggers from relevant Reddit communities. Use when asked for Reddit research, voice-of-customer analysis, audience pain points, product feedback, or community-led content opportunities.
---

# Reddit Customer Insights

Turn Reddit discussions into a concise, source-backed customer-insight brief. Use SandBase Reddit capabilities only for collection; the Agent synthesizes findings from the returned posts and comments. Read [the API map](references/sandbase-api-map.md) before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`. The API map fixes the workflow's tool names; Capability Registry remains authoritative for parameters and available Reddit data.

## Workflow

1. Define the product, audience, market, exclusions, and the decisions the research should inform.
2. Use `reddit_app_search_typeahead` to find relevant communities and queries.
3. Use `reddit_app_dynamic_search` and `reddit_app_topic_feed` to collect a diverse sample of recent discussions.
4. Use `reddit_app_post_details` or batch detail tools only for promising posts; preserve post URLs, dates, score, and community.
5. Separate direct observations from interpretation. Report recurring jobs, pain points, alternatives, objections, language, and unanswered questions.

## Output

Return a source table, recurring themes with post counts, representative paraphrases, content or product implications, and evidence gaps. Do not post, vote, message, or alter Reddit accounts.
