---
name: programmatic-seo
description: "Design and generate useful SEO page families from structured data and templates, including opportunity validation, page manifests, internal linking, indexation controls, sample pages, and quality checks."
license: MIT
metadata:
  source: "https://github.com/coreyhaines31/marketingskills/tree/d4ff28a9c8d56c06809860bf2800d4f5224b52db/skills/programmatic-seo"
  modified: "Condensed, aligned with existing SEO research Skills, and added safe host-neutral batch generation controls."
---

# Programmatic SEO

Build page families that satisfy recurring search intents with genuinely useful, entity-specific data. A template plus swapped keywords is not sufficient. Use this Skill for opportunity design, page manifests, templates, sample generation, and quality review—not for ordinary single-page copywriting or a general technical SEO audit.

## Intake

Establish:

- site, offer, audience, conversion goal, market, and language;
- repeating query pattern and the intent behind it;
- entities or variables, page count, and available structured data;
- data rights, provenance, update frequency, and unique value per entity;
- current site architecture, rendering stack, CMS, and indexation controls.

Use existing keyword, SERP, content-brief, and site-audit capabilities when available and authorized. Treat search volume, difficulty, competitor coverage, and live SERP observations as evidence; mark model-generated query patterns as hypotheses.

## Select a defensible page family

Common patterns include templates, examples, locations, personas, integrations, comparisons, conversions, glossaries, directories, profiles, curation, and localized content. Choose a pattern because the user's data and product can satisfy the intent, not merely because many URL combinations exist.

Reject or narrow the plan when pages would be doorway pages, near-duplicates, unsupported profiles, unlicensed copies, or combinations with no distinct user value.

## Workflow

### 1. Validate the opportunity

- Define the pattern and variables.
- Check representative head, middle, and long-tail queries.
- Inspect the live SERP shape and incumbent page quality when tools are available.
- Estimate useful page coverage from validated entities, not the Cartesian product of every field.
- State evidence gaps when reliable keyword or SERP data is unavailable.

### 2. Audit the data

Create a data dictionary with field, type, source, rights, freshness, null policy, and page use. Identify which fields create unique value and which are merely boilerplate. Define update and deletion behavior before generation.

### 3. Design the page contract

For each page type specify:

- canonical URL and slug rules;
- title, description, H1, and intent-specific sections;
- data-driven insights, useful tool or action, and conversion path;
- structured data only when the visible content supports it;
- canonical, `index`/`noindex`, sitemap, breadcrumb, and pagination behavior;
- hub, spoke, sibling, and related-entity links.

### 4. Build a manifest and samples

Produce a page manifest before bulk generation:

```text
page_id, entity_id, url, primary_query, intent, template,
data_completeness, unique_value_fields, indexation, canonical_url, updated_at
```

Generate three representative samples—strong, typical, and sparse-data—then review them before a large batch. If the user asked for file generation, write only within the agreed destination and do not overwrite existing pages without authorization.

### 5. Quality and launch plan

Define automated and editorial checks, rollout batches, monitoring, refresh cadence, and removal rules. Prioritize high-value, high-completeness pages. Publishing, deployment, sitemap submission, and Search Console actions require explicit user authorization.

## Output

```markdown
## Opportunity and evidence
## Page-family decision
## Data dictionary and rights
## URL and page contract
## Template with conditional sections
## Page manifest
## Three representative samples
## Internal-linking and indexation plan
## Validation, rollout, monitoring, and refresh plan
## Risks, assumptions, and open questions
```

## Quality gate

- Each indexable page satisfies a distinct intent with entity-specific value.
- URLs, canonicals, sitemap entries, and internal links are deterministic.
- Sparse pages have a merge, `noindex`, or omission rule.
- Titles and copy do not make unsupported claims.
- Data provenance, rights, freshness, and deletion handling are documented.
- Sample pages pass content, accessibility, structured-data, and duplicate checks before batching.
- The plan avoids keyword cannibalization with existing pages.

## Failure handling

- If keyword evidence is unavailable, deliver a hypothesis and validation plan rather than a traffic forecast.
- If data is incomplete or unlicensed, reduce page coverage or stop generation.
- If generated pages are near-duplicates, improve conditional value or consolidate the entities.
- If a batch partially fails, preserve the manifest and failure log, retry only failed pages, and never overwrite verified output silently.
