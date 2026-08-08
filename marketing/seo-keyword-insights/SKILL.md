---
name: seo-keyword-insights
description: Build evidence-backed SEO keyword insights and strategy using SandBase-managed search, keyword, site-analysis, and SERP capabilities. Use when asked to discover or prioritize keywords, assess search demand or ranking feasibility, map intent and topics, find competitor gaps, plan organic-search landing pages or content, or analyze a website's SEO opportunities.
---

# SEO Keyword Insights

Build a decision-ready organic-search strategy from a site, product, seed topic, or competitor set. This Skill is a SandBase API workflow: it calls the named SEO capabilities in [the SandBase API map](references/sandbase-api-map.md) through the SandBase MCP gateway. In a SandBase Agent, run the capabilities directly. In another compatible agent, require an authorized SandBase connection before starting; never request, print, or store an API key in the research output.

The primary capability is **DataForSEO keyword search through SandBase**: discover candidates, validate demand and difficulty, compare site visibility, and inspect live SERPs. Read [example workflows](references/example-workflows.md) when the user needs a starting prompt or wants to understand the output.

## Operating principles

- Start from the business and audience, not a brand-name keyword list.
- Treat tool-returned metrics and SERP results as evidence; treat model-generated keywords, intent labels, and recommendations as hypotheses or judgment.
- Select the country, language, device, and search engine deliberately. State any default rather than silently assuming a market.
- Optimize for qualified organic traffic and the site's conversion model, not volume alone.
- Inspect live SERPs before recommending a page type or claiming a ranking opportunity.
- Keep user domains, competitor lists, raw exports, and strategy confidential. Return a summarized report unless raw data is requested.

## Workflow

### 1. Frame the decision

Collect or infer the target site or product, target market, language, conversion goal, audience, content scope, and competitors. Classify the request as one or more of: discovery, site opportunity, competitor gap, content roadmap, or page keyword map.

If a site is supplied, form a compact site brief before researching: category, offer, ICP, jobs-to-be-done, differentiators, conversion action, current content themes, and exclusions. Inspect the homepage and a small set of representative product, use-case, pricing, docs, and content pages. Use a SandBase site/content capability when available; use SandBase web search only as a fallback. Record inaccessible or JavaScript-heavy pages as evidence gaps.

When market details are missing, choose a defensible default only if the site or request makes one clear; otherwise ask for the market. Never merge metrics from different markets or engines without labels.

### 2. Select and call SandBase capabilities

Read [the SandBase API map](references/sandbase-api-map.md) before selecting tools. Use the listed `tool_name` through the SandBase gateway:

1. Call `sandbase_describe_tool` for the selected `tool_name` and read its current input schema.
2. Call `sandbase_call_tool` with that exact `tool_name` and only schema-defined arguments.
3. Keep the tool name, market, language, device, and timestamp with the returned data.

Use `sandbase_find_tools` only when the API map does not cover a needed capability or SandBase has added a relevant one. Do not replace a mapped SEO capability with an unverified guessed name.

Prefer this evidence ladder:

1. Site/content parsing for the supplied site.
2. Keyword discovery from site-derived, product, problem, use-case, and integration seeds.
3. Demand, difficulty, trend, and clickstream metrics for the shortlisted candidates.
4. Ranked-keyword, competitor, and intersection data when a domain comparison is useful.
5. Live organic SERPs for the leading candidates and each priority cluster.

The API map intentionally fixes the product-facing capability names, while `sandbase_describe_tool` remains authoritative for payload shape, supported locations, and optional parameters. If an expected capability is unavailable, identify the evidence gap and continue only with evidence that is available.

### 3. Build and validate the keyword universe

Create 3–10 justified seed themes from the site brief or product description: category, capability, use case, pain point, buyer role, integration, comparison, and transactional or informational modifiers. Keep brand terms separate unless brand SEO is explicitly in scope.

Expand a small number of diverse seeds first, then deduplicate and remove clearly irrelevant, unsafe, navigational, or off-market terms. Preserve the provenance of each candidate: `site`, `seed`, `suggestion`, `related`, `competitor`, `SERP`, or `hypothesis`.

Validate the promising candidates with the available SandBase capabilities. Keep search volume, difficulty, CPC, trend, clickstream, rank, and SERP features in their original market and source context. Mark unavailable metrics as unavailable; never estimate them.

For competitor work, distinguish:

- **coverage gap**: a competitor ranks and the target does not;
- **performance gap**: both rank, but the target is materially weaker;
- **strategic gap**: the query fits the target's offer but no adequate target page exists.

Do not call every available provider merely because it exists. Stop expanding once clusters have enough evidence to make a decision; expand again only for thin or ambiguous clusters.

Use the keyword capabilities deliberately:

- Start with `keyword_suggestions`, `keyword_ideas`, `related_keywords`, or Google Ads seed expansion.
- Use `search_volume`, historical volume, Google Trends, and bulk difficulty only after shortlisting candidates.
- Use `keywords_for_site` and `ranked_keywords` to distinguish existing coverage from true gaps.
- Use `competitors_domain`, `domain_intersection`, and `serp_competitors` only for a justified competitor comparison.
- Use Google organic SERP and related/autocomplete queries to validate intent and the recommended page type.

### 4. Interpret intent, competition, and opportunity

Cluster validated candidates by user problem and shared ranking intent, then label each cluster with funnel stage and the best page purpose. Use live SERPs to verify whether the query rewards a product page, feature page, comparison, integration page, programmatic template, documentation, category page, or editorial content.

Score at cluster level before scoring individual keywords. Use a transparent qualitative scorecard:

| Dimension | Question |
|---|---|
| Qualified demand | Is the audience and demand meaningful for the business? |
| Commercial fit | Can the offer or a conversion path serve this query well? |
| Feasibility | Do difficulty, incumbent quality, topical authority, and SERP shape make entry plausible? |
| Strategic leverage | Does winning support positioning, product adoption, or a reusable page family? |
| Evidence confidence | Are the market, metrics, and SERP evidence sufficiently complete? |

Explain the reasoning behind each priority. Do not use a universal volume or difficulty cutoff: an opportunity's threshold depends on the market, query intent, business value, and the target's authority. If the user supplies a threshold, honor it and show which candidates meet it.

### 5. Produce an execution plan

Return a concise report using [the report template](references/report-template.md) for full deliverables. Separate observed data, calculated prioritization, and strategic judgment. Include assumptions, market labels, sources/capabilities used, data gaps, and next validation actions.

For every recommended page, specify its target cluster, primary query, supporting queries, intent, proposed page type, angle, conversion path, and SERP evidence. Recommend updates to an existing page when that is stronger than creating a new URL. Flag potential cannibalization between pages targeting the same intent.

## Example tasks

- “Find non-brand keyword opportunities for `example.com` in the United States. Prioritize commercial intent and show the evidence behind every recommendation.”
- “Expand `AI agent observability` into keyword clusters, then validate volume, difficulty, trends, and the Google SERP for the top cluster.”
- “Compare `our-domain.com` with `competitor-a.com` and `competitor-b.com`. Separate coverage gaps from performance gaps and recommend the next three pages.”
- “Audit the keywords this domain already ranks for. Identify which existing pages should be improved before creating new content.”
- “Research keyword opportunities for `CRM software` in Germany. Keep Germany/German metrics separate from any English-language research.”

## Quality gate

Before delivering, verify that:

- The site brief supports the selected seeds, or a no-site scope is explicit.
- Every metric is source-backed and labeled with its market or marked unavailable.
- Intent and page-type claims for priority clusters have live-SERP evidence.
- Competitor claims distinguish observation from inference.
- Priorities favor qualified outcomes and feasibility, not a single vanity metric.
- Recommendations are specific enough to hand to content, product marketing, or SEO owners.

## Failure handling

- If SandBase is unavailable or unauthorized, report the failed capability and ask the user to connect or authorize SandBase; do not silently substitute a direct provider API.
- If a capability returns incomplete data, keep partial findings, downgrade confidence, and name the missing evidence.
- If crawling is blocked, analyze accessible pages and clarify that the site brief may be incomplete.
- If no feasible priority emerges, report that finding and recommend a validation, authority-building, or paid-discovery path rather than inventing an opportunity.
