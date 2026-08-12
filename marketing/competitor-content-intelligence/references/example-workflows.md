# Example Workflows

Each example uses SandBase content intelligence capabilities as the evidence source. Inspect the current schema with `sandbase_describe_tool` before calling any listed tool.

## 1. Full competitor content gap analysis

**User request**

```text
Compare content coverage between our-domain.com and three competitors for the "AI agent observability" topic. Find differentiated opportunities.
```

**Use these capabilities**

1. `exa_search` with `include_domains` for each competitor to find their content on this topic.
2. `context_dev_scrape_markdown` for the top 2–3 pages per competitor to analyze depth and angle.
3. `dataforseo_v3_on_page_content_parsing_live` for structured content analysis.
4. `dataforseo_v3_content_analysis_search_live` to check broader market coverage.
5. `exa_search` for buyer questions about this topic that competitors don't answer well.

**Return**: a coverage matrix, 5–7 prioritized content opportunities with differentiation angles, and 3 actionable content briefs.

## 2. Buyer question gap analysis

**User request**

```text
What questions do potential buyers of [product category] ask that no competitor answers well?
```

**Use these capabilities**

1. `exa_search` with question-format queries: "how to choose [category]", "what to look for in [category]", "[category] comparison for [role]".
2. `cloudsway_search` for broader coverage including forums, Q&A sites, and community discussions.
3. `context_dev_scrape_markdown` for the top-ranking content on each question to assess answer quality.
4. `dataforseo_v3_content_analysis_search_live` to validate whether the question truly lacks good coverage.

**Return**: a ranked list of unanswered or poorly-answered buyer questions, with evidence of current coverage quality and recommended content format for each.

## 3. Content freshness opportunity scan

**User request**

```text
Find topics where competitor content is outdated and we could publish something more current.
```

**Use these capabilities**

1. `exa_search` with date filters (e.g., content older than 12 months) for competitor domains on key topics.
2. `dataforseo_v3_on_page_content_parsing_live` to check publication/modification dates.
3. `exa_search` with recent dates to find if newer sources have emerged that competitors haven't incorporated.
4. `context_dev_scrape_markdown` to verify content staleness (outdated examples, deprecated features, old pricing).

**Return**: a freshness opportunity table with topic, competitor page, age, specific outdated elements, and the update angle we could take.

## 4. Format and depth opportunity analysis

**User request**

```text
What content formats are competitors NOT using for [topic]? Where is their content superficial?
```

**Use these capabilities**

1. `exa_search` across competitors for the topic, noting content format (article, comparison, video, tool, template, calculator).
2. `context_dev_scrape_markdown` for representative pages to assess depth (word count, subtopic coverage, examples, data).
3. `cloudsway_search` for format examples from adjacent industries that could be applied.

**Return**: a format matrix showing what each competitor offers, format gaps (e.g., no interactive tools, no comparison tables, no video explanations), and depth analysis showing where content is superficial enough to beat.

## 5. Content brief generation from gaps

**User request**

```text
Give me 5 content briefs for differentiated articles in our space, based on competitor gaps.
```

**Use these capabilities**

1. Run a abbreviated version of Workflow #1 to identify the top 5 gaps.
2. `exa_search` for the best existing content on each topic (from any source) to understand the quality bar.
3. `context_dev_scrape_markdown` for the best-in-class example for each topic.
4. `dataforseo_v3_content_analysis_search_live` to validate audience interest and content volume.

**Return**: 5 structured content briefs, each with: target query, audience, differentiation angle from competitors, required subtopics, recommended format/structure, data or examples to include, word count estimate, and success metrics.
