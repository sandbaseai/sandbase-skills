---
name: exa-deep-search
description: Search, extract, and compare high-quality public sources with Exa through SandBase. Use when asked for deep web research, source discovery, current evidence, topic investigation, company research, or citation-ready findings.
---

# Exa Deep Search

Turn Exa search into a focused, source-backed research brief. The current Skill uses the SandBase `exa_search` capability, which can return highlights, summaries, or full page text in the same call.

## Workflow

1. Confirm the research question, time window, geography, exclusions, and required deliverable.
2. Use `exa_search` with `search_depth: advanced` for difficult research and `basic` for quick validation.
3. Refine queries by company, product, user problem, competitor, event, or time period until the evidence is sufficient.
4. Send selected URLs to `exa_contents` for batch extraction; choose text, highlights, or summary according to the research need.
5. Use `max_age_hours: 0` only when freshness requires a live crawl; use `subpages` only for an explicit documentation, pricing, or API crawl.
6. Preserve URLs, dates, and source relevance; separate observations, quotes, and inferences.

## Query patterns

- **Current landscape**: set `topic: news`, a bounded date range, and `include_highlights: true`.
- **Deep evidence**: use `search_depth: advanced`, `include_summary: true`, and request full text only for the few sources selected for closer review.
- **Selected-source extraction**: pass selected URLs to `exa_contents`; use `highlights_query` or `summary_query` to focus extraction.
- **Trusted-source research**: use `include_domains` for first-party, academic, or approved publisher domains.
- **Competitive research**: use `exclude_domains` for the target's own site and search separately for each competitor or category query.

## Evidence rules

- Cite a result URL for every externally verifiable claim.
- Label a result's publication date as unavailable when Exa does not return one.
- Do not treat an Exa summary as a source quote; use it as an aid to select evidence.
- Do not call Exa Answer or Exa Agent. The user's Agent/LLM synthesizes the evidence.
- If `exa_contents` is not yet available in the current Gateway, return the Search results and state that extraction is awaiting capability publication.

## Example tasks

- “Find the last 30 days of reliable sources about AI agent observability. Give me a five-source brief with gaps.”
- “Research how enterprise teams evaluate AI agents. Prefer company and academic sources; exclude vendor blogs.”
- “Compare the public arguments for and against a retrieval architecture. Use advanced search and cite each source.”

## Output

Return a source map, concise findings, disagreements or evidence gaps, and next research queries. Do not invent citations or copy long source passages.
