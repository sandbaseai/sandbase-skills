---
name: exa-deep-search
description: Search, extract, and compare high-quality public sources with Exa through SandBase. Use when asked for deep web research, source discovery, current evidence, topic investigation, company research, or citation-ready findings.
---

# Exa Deep Search

Turn Exa search into a focused, source-backed research brief. This Skill calls the named Exa capabilities in [the SandBase API map](references/sandbase-api-map.md) through the SandBase MCP gateway. Use an authorized SandBase MCP connection and the discover → inspect → run workflow below; never request, print, or store an API key in the research output.

Read [example workflows](references/example-workflows.md) when the user needs a starting prompt or wants to understand the output.

## Operating principles

- Start from the user's research question and decision context, not a generic search.
- Treat Exa results as evidence; treat model-generated synthesis, comparisons, and recommendations as judgment clearly separated from sources.
- Select search depth, time window, domains, and geography deliberately. State any assumption rather than silently defaulting.
- Optimize for source quality, recency, and relevance — not quantity.
- Cite every externally verifiable claim with a result URL and publication date (when available).
- Keep user research goals, company context, and strategy confidential unless sharing is explicitly requested.

## Workflow

### 1. Frame the research question

Collect or infer: the topic or entity, time window, geography, trusted or excluded domains, audience for the deliverable, and how findings will be used. Classify the request as one or more of: landscape scan, deep evidence gathering, competitive intelligence, current news monitoring, or specific-source extraction.

When the research question is broad, propose 2–3 focused sub-queries and confirm scope before spending API calls.

### 2. Select and call SandBase capabilities

Read [the SandBase API map](references/sandbase-api-map.md) before selecting tools. Treat each listed `tool_name` as a capability identifier to resolve through the SandBase gateway:

1. Use `sandbase_discover` with the provider and capability to find the current endpoint name.
2. Pass the returned `name` to `sandbase_inspect`; read `inputSchema`, pricing, and `execute_as`.
3. Follow `execute_as` to call `sandbase_run` using `execute_as.arguments.name` and schema-defined `arguments`. If it returns a `run_id`, poll `sandbase_run_get` within the task budget until `completed` or `failed`; report pending or failed runs without automatically resubmitting them.
4. Keep the returned endpoint name, query, search parameters, and result metadata with the returned data.

### 3. Search with Exa

Resolve `exa_search` with `sandbase_discover`, then map these research needs to the current `inputSchema` from `sandbase_inspect`. Use the discovered endpoint name and its `execute_as` template for execution:

| Research need | Search intent |
|---|---|
| Current landscape | News results within a bounded publication window, with relevant highlights |
| Deep evidence | A supported deep search mode with summaries; request full text only for selected sources |
| Trusted sources only | Restrict results to first-party, academic, or approved publisher domains |
| Competitive research | Exclude the target's own domain; use separate queries per competitor |
| Validation or quick check | A supported fast search mode with 3–5 results |

Tips:
- Write queries as natural-language statements of what a good result page would say, not short keyword strings. Exa responds best to semantic queries.
- Use the inspected schema’s supported categories to narrow result types.
- Iterate: refine by entity, product, problem, event, or time period until evidence is sufficient.
- Request relevant highlights using the inspected schema’s content options, without extracting full text for every result.

### 4. Extract selected sources

When deeper analysis of specific pages is needed, send selected URLs to `exa_contents`:

- Request full page content when analyzing structure or extracting data.
- Request focused highlights when the inspected extraction schema supports them.
- Request concise summaries when reviewing many pages, if supported.
- Include subpages only for explicit documentation, pricing, or API crawl tasks and only when supported.
- Request a live crawl only when freshness requires it and the inspected schema supports it.

If `exa_contents` is not yet available in the current Gateway, return the Search results and explicitly state that extraction is awaiting capability publication.

### 5. Synthesize findings

- Separate direct observations from interpretation.
- Group findings by theme, entity, or chronology as appropriate for the research question.
- Note disagreements between sources and evidence gaps.
- Propose follow-up queries for unresolved questions.

## Query crafting tips

Good Exa queries describe the content of the ideal result page:

| Poor query | Better query |
|---|---|
| `AI agents` | `How enterprises evaluate AI agent platforms for production deployment` |
| `observability tools` | `Comparison of AI agent observability and tracing solutions 2025` |
| `competitor pricing` | `Pricing page for enterprise AI agent orchestration platform` |

- Add temporal context: "in 2025", "since January", "latest announcement".
- Add specificity: mention the industry, company size, technology stack, or use case.
- Use the inspected schema’s domain exclusion option to avoid results you already know about.

## Output

Return a structured research brief:

### Source map

| # | Title | URL | Published | Relevance |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |

### Key findings

Numbered findings, each citing source(s) by number.

### Disagreements and evidence gaps

What sources disagree on, and what questions remain unanswered.

### Suggested next queries

Follow-up Exa queries or alternative research paths.

## Evidence rules

- Cite a result URL for every externally verifiable claim.
- Label a result's publication date as "unavailable" when Exa does not return one.
- Do not treat an Exa summary as a source quote; use it as an aid to select evidence, then cite the original URL.
- Do not call Exa Answer or Exa Agent endpoints. The user's Agent/LLM synthesizes the evidence.
- Do not copy long source passages; paraphrase and cite.
- Mark clearly when a finding is inferred from multiple sources vs. directly stated in one.

## Failure handling

- If SandBase is unavailable or unauthorized, report the failed capability and ask the user to connect or authorize SandBase; do not silently substitute a direct provider API.
- If `exa_search` returns few or no results, try: broader query, a different supported search mode, removed domain filters, or a wider date range. Report if the topic genuinely lacks public coverage.
- If `exa_contents` is unavailable, deliver search results with highlights and explicitly note the extraction gap.
- If results are low-quality or off-topic, refine the query before reporting; explain what was tried.

## Example tasks

- "Find the last 30 days of reliable sources about AI agent observability. Give me a five-source brief with gaps."
- "Research how enterprise teams evaluate AI agents. Prefer company and academic sources; exclude vendor blogs."
- "Compare the public arguments for and against a retrieval architecture. Use advanced search and cite each source."
- "Find recent funding announcements in the AI developer tools space. Only include sources from the last 7 days."
- "Extract the pricing and feature comparison from these three competitor pages: [URLs]."

## Quality gate

Before delivering, verify that:

- Every finding cites at least one source URL.
- Observations are separated from model-generated interpretations.
- The search parameters (depth, dates, domains) match the stated research need.
- Evidence gaps and low-confidence findings are explicitly labeled.
- The deliverable format matches what the user requested.
