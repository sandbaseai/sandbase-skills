---
name: listicle-blog-writer
description: "Research and write evidence-backed listicles, product roundups, and best-of comparisons with optional SandBase SERP, page, review, and screenshot evidence. Use for ‘best tools’, ‘top products’, roundup, SEO, GEO, or answer-engine content; do not use for an unresearched promotional ranking presented as independent advice."
---

# Listicle Blog Writer

Create useful, scannable comparison articles whose rankings follow disclosed criteria and current evidence. Drafting can use user-provided material alone; live research and screenshots use SandBase.

Read [the SandBase API map](references/sandbase-api-map.md) before retrieving external evidence.

## Define the assignment

Resolve or state reasonable defaults for:

- topic, audience, market, language, and publication date;
- intended number of entries and any must-include or excluded products;
- publisher or client relationship to a featured product;
- evaluation criteria and their relative importance;
- hands-on testing performed by the user versus third-party evidence;
- primary query, related questions, and supplied keyword or analytics exports;
- article length, tone, house style, output path, and whether screenshots are required.

A must-include product is not automatically the winner. If the publisher owns, sponsors, or affiliates with an entry, disclose that relationship and rank it by the same stated criteria. Do not claim hands-on testing, independent review, or measured performance unless the evidence supports it.

## Choose the evidence mode

- **User-supplied evidence**: use product notes, exports, tests, screenshots, and source links supplied by the user. No SandBase call is required.
- **Live research**: discover and inspect current SandBase capabilities for organic SERPs, related queries, page extraction, screenshots, and public review evidence.
- **Outline or draft without live research**: write a clearly labeled preliminary draft, mark unverified price and feature fields, and omit screenshots or review claims that have not been collected.

If SandBase is unavailable, continue with supplied sources or a labeled research plan. Do not request provider-specific API keys or invent current facts.

## SandBase execution contract

For live research:

1. Call `sandbase_discover` separately for the required evidence classes, such as `google organic serp`, `related keywords`, `scrape markdown`, `page screenshot`, or a named public review platform.
2. Call `sandbase_inspect` for each serious candidate. Confirm the live schema, geography and language controls, result limits, output type, price, and sync or async behavior.
3. Build the smallest call plan that can support the article. Reuse one SERP response across entries and avoid screenshot or scrape calls that do not affect the deliverable.
4. Before any paid research call, show the selected endpoints, important arguments, call count, per-call prices, and total estimate or uncertainty. Obtain confirmation for the exact call or batch.
5. Use `sandbase_account` before an approved multi-call batch.
6. Call `sandbase_run` with exact discovered names and only current schema-defined arguments.
7. Poll each asynchronous result with `sandbase_run_get` using the same run ID. Never resubmit merely because a run remains pending.
8. Use `sandbase_runs` only to recover a lost result or reconcile actual cost.

Model and API availability changes. Do not hard-code a provider endpoint, parameter snapshot, price, or output URL in the Skill or article.

## Research the category

Start with the search landscape rather than a predetermined ordering:

1. Inspect the primary query and related questions for the requested market and language.
2. Identify the recurring products, page formats, search intent, comparison criteria, and freshness expectations.
3. Build a candidate set broad enough to cover distinct user needs. Exclude entries that cannot be verified or do not belong to the category.
4. Record source URL, publisher, observation date, what the source supports, and whether it is primary, independent, or user supplied.
5. Define a short scoring rubric before ranking. Typical dimensions include fit for the stated use case, core capability, usability, integration, price, support, and material limitations.

Official pages may support current features, documentation, and prices. They are not independent reviews. Use public third-party sources for experience claims, and preserve both praise and criticism when relevant.

For each entry, verify only what the article needs:

- canonical homepage and product name;
- current plan or price relevant to the target reader, including billing basis and observation date;
- a few differentiating features tied to the evaluation criteria;
- important constraints, exclusions, or tradeoffs;
- independent experience evidence when the article promises reviews;
- a current homepage screenshot when the deliverable includes imagery.

## Plan the article

Use a structure that is easy for readers and answer engines to parse:

1. **Title and opening** — identify the category, audience, year or as-of date, and the decision the article helps make.
2. **Quick recommendations** — give a few self-contained “best for” answers with one-sentence reasons. Do not force a fixed number when the evidence supports fewer.
3. **Method** — disclose research dates, source types, testing status, ranking criteria, and commercial relationships.
4. **Comparison table** — use consistent columns and units. Include only fields that were verified for every entry or mark missing values explicitly.
5. **Ranked entries** — explain fit, evidence, differentiators, tradeoffs, and price in a consistent but natural format.
6. **Decision guidance** — explain how the top choices differ by need rather than repeating the ranking.
7. **FAQ** — answer real related questions found in research or supplied by the user.
8. **Sources and disclosures** — link claims to sources and state the evidence window.

Avoid treating a rigid template as a ranking signal. Match section depth to the decision complexity and publication style.

## Write each entry

For every product or item:

- link to the canonical page at its first useful mention;
- state who it is best for and why before listing features;
- connect each differentiator to a reader need rather than repeating marketing copy;
- include concrete drawbacks and boundary conditions;
- normalize prices to the same billing period and currency when possible, without converting plans that are not equivalent;
- attribute public experience claims to their actual source;
- keep screenshots in a stable article-relative folder and use descriptive alt text.

Do not reproduce long passages from competitors or review sites. Quote only the minimum necessary, prefer paraphrase, and retain source links.

## SEO and answer-engine quality gate

Before delivery, verify that:

- the title and opening match the actual query intent;
- quick recommendations and the comparison table are understandable outside surrounding prose;
- headings describe distinct needs rather than keyword variants;
- every current feature, price, and experience claim has an evidence record and as-of date;
- missing or conflicting evidence is visible rather than averaged away;
- the FAQ reflects genuine questions and gives direct, self-contained answers;
- no entry is ranked first solely because it belongs to the publisher;
- screenshots exist at the referenced paths and were checked visually;
- links resolve and affiliate or sponsorship disclosures are present where required;
- prose is specific, varied, and free of unsupported superlatives.

## Handoff

Return the article, image folder when requested, a compact evidence ledger, the ranking rubric, SandBase endpoint names and run IDs used, estimated and observed cost, unresolved facts, and the latest verification date. If research is incomplete, label the output as a draft and list the calls or user inputs still needed.
