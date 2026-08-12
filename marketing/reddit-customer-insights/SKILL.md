---
name: reddit-customer-insights
description: Discover evidence-backed customer language, pain points, objections, and buying triggers from relevant Reddit communities. Use when asked for Reddit research, voice-of-customer analysis, audience pain points, product feedback, or community-led content opportunities.
---

# Reddit Customer Insights

Turn Reddit discussions into a concise, source-backed customer-insight brief. This Skill calls the named Reddit capabilities in [the SandBase API map](references/sandbase-api-map.md) through the SandBase MCP gateway. In a SandBase Agent, run the capabilities directly. In another compatible agent, require an authorized SandBase connection before starting; never request, print, or store an API key in the research output.

Read [example workflows](references/example-workflows.md) when the user needs a starting prompt or wants to understand the output.

## Operating principles

- Research public discussions only; never post, vote, message, or alter Reddit accounts.
- Treat Reddit posts and comments as qualitative evidence of real customer language and sentiment, not statistically representative samples.
- Separate direct observations (what users said, how many said it) from interpretation (what it means for the business).
- Preserve provenance: keep post URLs, dates, scores, community names, and commenter context.
- Keep user company, product, and strategy details confidential in all outputs unless sharing is explicitly requested.
- Respect that Reddit users are real people. Do not mock, target, or re-identify individuals.

## Workflow

### 1. Frame the research question

Collect or infer: the product or market category, target audience segment, competitor landscape, research objective (pain points, buying triggers, objections, language, content ideas), and any exclusions (communities, time ranges, competitor names to avoid).

Classify the request as one or more of:
- **Pain point discovery**: what frustrates potential buyers
- **Buying trigger research**: what events or needs prompt purchase decisions
- **Objection mining**: what stops people from buying or adopting
- **Language extraction**: exact words and phrases customers use
- **Content opportunity finding**: unanswered questions worth creating content for
- **Product feedback**: what existing users praise or criticize

### 2. Select and call SandBase capabilities

Read [the SandBase API map](references/sandbase-api-map.md) before selecting tools. Use the listed `tool_name` through the SandBase gateway:

1. Call `sandbase_describe_tool` for the selected `tool_name` and read its current input schema.
2. Call `sandbase_call_tool` with that exact `tool_name` and only schema-defined arguments.
3. Keep the tool name, query parameters, and result metadata with the returned data.

### 3. Discover relevant communities

Use `reddit_app_search_typeahead` to find:
- Subreddits where the target audience discusses the category
- Related search queries that reveal community terminology
- Adjacent communities (e.g., industry-specific, role-specific, tool-comparison subs)

Tips:
- Search for the product category, not the product name, to find broader discussions.
- Try role-based terms (e.g., "marketing manager", "DevOps engineer") alongside category terms.
- Note community sizes and activity levels to prioritize collection.

### 4. Collect discussions

Use `reddit_app_dynamic_search` and `reddit_app_topic_feed` to build a diverse sample:

| Strategy | When to use |
|---|---|
| Problem-focused queries | "frustrated with [category]", "looking for alternative to [competitor]" |
| Decision-stage queries | "recommendation for [category]", "which [product type] should I use" |
| Experience queries | "switched from [competitor]", "after using [product] for 6 months" |
| Topic feed | When you need volume from a specific community over time |

Tips:
- Collect from multiple communities to avoid single-community bias.
- Include both recent posts (current sentiment) and older high-score posts (established patterns).
- Search for competitor names to find comparison and switching discussions.
- Use negative terms ("hate", "frustrated", "switched away") for pain points and positive terms ("love", "finally", "game changer") for satisfaction signals.

### 5. Inspect selected posts

Use `reddit_app_post_details` only for the most promising discussions:
- Posts with high engagement (many comments, high score)
- Posts that contain decision-making language
- Posts where the title suggests detailed experience sharing

Read comment threads for:
- Recurring recommendations (what gets upvoted as answers)
- Disagreements (signals of market segmentation)
- Specific feature mentions and workflow descriptions
- Price sensitivity signals
- Integration or ecosystem requirements

### 6. Synthesize findings

Organize findings by research theme, not by source post. For each theme:
- Count how many distinct posts/comments express the pattern
- Quote representative language (paraphrased, with source link)
- Note the community context (what role or situation the commenter is in)
- Distinguish one-time complaints from recurring patterns

## Output

Return a structured insight brief:

### Research scope

- Category and audience studied
- Communities and queries searched
- Time range and sample size
- Limitations and blind spots

### Source table

| # | Community | Post title (abbreviated) | URL | Date | Score | Comments |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... |

### Recurring themes

| Theme | Post count | Representative language | Business implication |
|---|---|---|---|
| ... | ... | ... | ... |

### Pain points (ranked by frequency)

1. **[Pain point]** — observed in N posts across M communities. Example language: "..."
   - Implication: ...

### Buying triggers

Events or needs that prompt purchase decisions, with evidence.

### Objections and barriers

What stops people from buying/adopting, with evidence.

### Customer language

Exact phrases and framings customers use (for messaging, SEO, ad copy).

### Content and product opportunities

Unanswered questions, underserved needs, and positioning gaps.

### Evidence gaps

What this research cannot answer and what additional research would help.

## Tips for better results

- **Cast a wide net first**: Start with 3–5 community searches and 5–10 diverse queries before narrowing.
- **Look for "switching" posts**: "I switched from X to Y because..." contains the richest insight.
- **Check "what do you use" threads**: These aggregate many data points in one post.
- **Note the non-obvious communities**: Industry-specific subs often have more candid discussions than product-category subs.
- **Time-bound for relevance**: Weight recent posts more heavily for fast-moving categories; include older posts for established patterns.
- **Triangulate**: If a pain point appears in only one community, it may be community-specific rather than market-wide.

## Failure handling

- If SandBase is unavailable or unauthorized, report the failed capability and ask the user to connect or authorize SandBase; do not silently substitute a direct API.
- If searches return few results, try: broader category terms, different community targets, or adjacent problem spaces. Report if the topic genuinely lacks Reddit coverage.
- If a community is private or restricted, note the gap and search for alternative communities.
- If results are predominantly spam or self-promotion, filter them out and note the signal quality issue.

## Quality gate

Before delivering, verify that:

- Every theme cites at least 2 distinct source posts (avoid single-post conclusions).
- Observations are separated from business interpretations.
- Community and time context is preserved for each finding.
- The sample includes multiple communities (avoid single-community bias).
- Sensitive user information (usernames in sensitive contexts) is handled respectfully.
- The research answers the original question, not just adjacent topics.
