# Example Workflows

Each example uses SandBase Exa capabilities as the evidence source. Inspect the current schema with `sandbase_describe_tool` before calling any listed tool.

## 1. Current landscape scan

**User request**

```text
Find the last 30 days of reliable sources about AI agent observability. Give me a five-source brief with gaps.
```

**Use these capabilities**

1. `exa_search` with `search_depth: "advanced"`, `start_published_date` set to 30 days ago, `include_highlights: true`, `include_summary: true`, `num_results: 10`.
2. Select the top 5 most relevant, authoritative results.
3. Optionally use `exa_contents` with `include_text: true` for the 2–3 sources that need deeper analysis.

**Return**: a source map table, 3–5 key findings with citations, disagreements between sources, and suggested follow-up queries.

## 2. Trusted-source deep research

**User request**

```text
Research how enterprise teams evaluate AI agents. Prefer company and academic sources; exclude vendor blogs.
```

**Use these capabilities**

1. `exa_search` with `search_depth: "advanced"`, `include_domains: ["arxiv.org", "hbr.org", "mckinsey.com", ...]`, `exclude_domains: [known vendor blog domains]`, `include_summary: true`.
2. Run 2–3 refined queries focusing on: evaluation criteria, enterprise deployment challenges, ROI measurement.
3. Use `exa_contents` with `highlights_query: "evaluation criteria"` for the most promising results.

**Return**: findings organized by evaluation dimension, with source quality assessment and gaps where academic/enterprise evidence is thin.

## 3. Competitive argument comparison

**User request**

```text
Compare the public arguments for and against retrieval-augmented generation. Cite each source.
```

**Use these capabilities**

1. `exa_search` with query describing "arguments in favor of RAG for production LLM applications", `search_depth: "advanced"`.
2. `exa_search` with query describing "limitations and criticisms of RAG architecture", `search_depth: "advanced"`.
3. Use `exa_contents` with `include_highlights: true`, `highlights_query` focused on "advantages" then "limitations" for selected URLs.

**Return**: a two-column comparison (for/against), each point citing its source, with a synthesis of where the debate stands and what evidence is missing.

## 4. Recent news monitoring

**User request**

```text
Find recent funding announcements in the AI developer tools space from the last 7 days.
```

**Use these capabilities**

1. `exa_search` with `topic: "news"`, `start_published_date` set to 7 days ago, `num_results: 15`, `include_highlights: true`.
2. Query variations: "AI developer tools startup funding round", "Series A B C AI coding tools".

**Return**: a chronological list with company, amount, round, investors (when available), and source URL. Note which details are confirmed vs. reported by a single source.

## 5. Specific-page extraction

**User request**

```text
Extract the pricing and feature comparison from these three competitor pages: [URL1, URL2, URL3].
```

**Use these capabilities**

1. `exa_contents` with `urls: [URL1, URL2, URL3]`, `include_text: true`, `max_characters: 15000`.
2. If `exa_contents` is unavailable, use `exa_search` with `include_domains` restricted to those domains and include highlights.

**Return**: a structured comparison table extracted from the pages, noting where information was unavailable or behind authentication.
