---
name: competitor-content-intelligence
description: Analyze competitor content coverage and uncover differentiated content opportunities using web search, page extraction, and DataForSEO content analysis. Use when asked for competitor content research, editorial gap analysis, content brief inputs, or topic whitespace.
---

# Competitor Content Intelligence

Compare public content evidence to identify differentiated editorial and landing-page opportunities. This Skill calls the named search, extraction, and analysis capabilities in [the SandBase API map](references/sandbase-api-map.md) through the SandBase MCP gateway. In a SandBase Agent, run the capabilities directly. In another compatible agent, require an authorized SandBase connection before starting; never request, print, or store an API key in the research output.

Read [example workflows](references/example-workflows.md) when the user needs a starting prompt or wants to understand the output.

## Operating principles

- Focus on content strategy differentiation, not content copying. The goal is to find what's missing, underserved, or poorly served.
- Treat web data and content analysis as evidence; treat gap identification, angle suggestions, and content briefs as judgment clearly separated from observations.
- Respect intellectual property: do not reproduce competitor text beyond short necessary excerpts for analysis.
- Select geography, language, and audience deliberately. A gap in one market may be saturated in another.
- Optimize for content that serves the target's audience and conversion goals, not content volume alone.
- Keep user strategy, positioning, and competitor lists confidential unless sharing is explicitly requested.

## Workflow

### 1. Frame the analysis

Collect or infer: the target audience and their problems, the topic or category, 2–5 competitor domains or brands, the target's positioning and differentiation, content types in scope (blog, landing page, documentation, comparison, tool), and the intended use of findings (content calendar, brief backlog, editorial strategy).

Classify the request as one or more of:
- **Coverage mapping**: what topics do competitors cover vs. not?
- **Depth analysis**: where is competitor content superficial or outdated?
- **Angle discovery**: what perspectives, formats, or audiences are underserved?
- **Question gap**: what buyer questions remain unanswered across competitors?
- **Format opportunity**: what content types are missing (interactive, data, video, tool)?

### 2. Select and call SandBase capabilities

Read [the SandBase API map](references/sandbase-api-map.md) before selecting tools. Use the listed `tool_name` through the SandBase gateway:

1. Call `sandbase_describe_tool` for the selected `tool_name` and read its current input schema.
2. Call `sandbase_call_tool` with that exact `tool_name` and only schema-defined arguments.
3. Keep the tool name, query parameters, and result metadata with the returned data.

### 3. Discover competitor content

Use `exa_search` and `cloudsway_search` to map the competitor content landscape:

| Strategy | Approach |
|---|---|
| Topic coverage | Search for the category + each competitor's domain to find their published content |
| Question targeting | Search for buyer questions in the category and see which competitors answer them |
| Format variety | Search for comparisons, guides, tools, calculators, templates in the category |
| Freshness gaps | Search with date filters to find where competitor content is outdated |

Tips:
- Use `include_domains` to search within a specific competitor's site.
- Use semantic queries that describe the ideal content (Exa responds well to this).
- Search for the same topic across multiple competitors to build a coverage matrix.
- Search for "[category] + [buyer question]" to find question-gap opportunities.
- Use `cloudsway_search` for broader web coverage that may surface sources Exa doesn't index.

### 4. Extract and analyze selected pages

Use `context_dev_scrape_markdown` and `dataforseo_v3_on_page_content_parsing_live` for deeper analysis:

**When to extract full pages:**
- Competitor's top-ranking content for a target topic (to understand depth and angle)
- Pages that rank for queries you want to target (to understand what Google rewards)
- Content that gets high engagement or links (to understand format patterns)

**What to analyze in extracted content:**
| Dimension | Questions to answer |
|---|---|
| Depth | How thorough is the coverage? What subtopics are included/excluded? |
| Freshness | When was it last updated? Are examples and data current? |
| Audience | Who is it written for? (beginner/advanced, role, industry) |
| Angle | What perspective or opinion does it take? |
| Format | How is information structured? (listicle, guide, comparison, tutorial) |
| Conversion | What CTA or next step does it offer? |
| Gaps | What questions does a reader still have after reading? |

### 5. Validate topic patterns

Use `dataforseo_v3_content_analysis_search_live` to validate broader patterns:

- Confirm whether a content gap is real (no one covers it) vs. just missed by your competitor sample.
- Check content volume and freshness for a topic to assess saturation.
- Identify emerging subtopics with growing coverage.

### 6. Synthesize opportunities

For each identified opportunity, document:
- **The gap**: what's missing, superficial, or underserved
- **The evidence**: which competitors were checked, what they cover vs. don't
- **The audience**: who would benefit from this content
- **The differentiation**: why the target can serve this better than competitors
- **The format**: recommended content type and structure
- **The priority**: based on audience value, competitive vacuum, and feasibility

## Output

Return a structured content intelligence brief:

### Coverage matrix

| Topic / Question | Competitor 1 | Competitor 2 | Competitor 3 | Target | Gap type |
|---|---|---|---|---|---|
| ... | ✅ deep | ⚠️ shallow | ❌ absent | ❌ absent | Full gap |
| ... | ✅ deep | ✅ deep | ✅ deep | ⚠️ outdated | Freshness gap |
| ... | ❌ absent | ❌ absent | ❌ absent | ❌ absent | Market gap |

### Priority opportunities

| # | Opportunity | Gap type | Evidence | Audience value | Differentiation angle | Recommended format | Priority |
|---|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... | ... |

### Content brief backlog

For the top 3–5 opportunities, provide actionable briefs:

**Brief: [Topic]**
- Target query/question: ...
- Audience: ...
- Angle that differentiates from competitors: ...
- Key subtopics to cover: ...
- Format and structure: ...
- Evidence/data to include: ...
- Conversion path: ...
- Success metric: ...

### Competitive patterns

Observations about competitor content strategy (publishing cadence, preferred formats, topic clusters, content quality trends).

### Evidence gaps

What couldn't be verified, what additional research would help, and confidence levels.

## Tips for better results

- **Compare, don't copy**: The goal is finding whitespace, not replicating what works for competitors.
- **Think in questions**: Frame gaps as buyer questions that lack good answers.
- **Check the SERP, not just competitor sites**: Sometimes the gap exists because no one ranks well for a query (use with SEO Keyword Insights skill).
- **Look for format gaps**: Sometimes the information exists but the format is wrong (text wall when a comparison table would serve better).
- **Consider the full journey**: Map content to funnel stages; gaps at one stage may be more valuable than gaps at another.
- **Freshness is a strategy**: Outdated competitor content is an opportunity even if the topic is "covered".
- **Non-obvious competitors**: Include content publishers (blogs, media sites) not just product competitors.

## Failure handling

- If SandBase is unavailable or unauthorized, report the failed capability and ask the user to connect or authorize SandBase; do not silently substitute a direct provider API.
- If scraping is blocked (authentication, paywall, JavaScript-heavy), note the gap and work with available metadata and search results.
- If competitors have minimal public content, note the early-market signal and suggest alternative research approaches (Reddit, community forums, sales conversations).
- If the topic is highly saturated, shift focus from "topic gaps" to "angle gaps", "depth gaps", or "format gaps".

## Quality gate

Before delivering, verify that:

- The coverage matrix is based on actual page analysis, not assumptions about competitor content.
- Each opportunity has specific evidence of the gap (not just "they don't cover X").
- Differentiation angles are tied to the target's actual capabilities or positioning.
- Content briefs are specific enough for a writer to execute without additional research.
- The priority considers audience value and business impact, not just ease of creation.
- Competitive analysis is fair — acknowledge where competitors do well, not just where they're weak.
