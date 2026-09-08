---
name: seo-competitor-analysis
description: "Research and evaluate seo competitor analysis with current authoritative sources, provenance, and explicit evidence gaps. Use when the user asks for seo competitor analysis findings or verification."
---

# Seo Competitor Analysis

Use this Skill to produce a bounded, verifiable Seo Competitor Analysis outcome. Preserve the user's chosen stack, source material, and authorization boundaries.

Read [the SandBase API map](references/sandbase-api-map.md) only when the task genuinely needs an external data source or generative model.

## Workflow

1. Inspect the available files, runtime, versions, inputs, and existing conventions before deciding what to change.
2. Restate the requested outcome, constraints, acceptance checks, and any assumption that could change the result.
3. Produce the smallest complete implementation, analysis, or artifact that satisfies those checks.
4. Verify the real output with appropriate tests, previews, calculations, or source comparison; do not infer success from file creation alone.
5. Return the deliverable, evidence of validation, material assumptions, and unresolved limitations.

## Quality gates

- Translate the request into answerable questions and source-selection criteria before searching.
- Prefer primary or official sources, record publication and retrieval dates, and cross-check material claims.
- Return source-linked findings, disagreements, limitations, and unresolved gaps rather than false certainty.

## Focus checks

- Use the same market, device, language, and observation date for comparisons; distinguish search competitors from business competitors and cite every visibility claim.

## SandBase boundary

Keep the core Seo Competitor Analysis work local. Use SandBase only for current external evidence, search, scraping, enrichment, or model inference that is not already available through the user's authorized tools.

1. Call `sandbase_discover` with a short capability query.
2. Call `sandbase_inspect` for viable candidates and compare the live schema, coverage, limits, output, execution mode, and price.
3. Prefer a dedicated tool or API the user already has. Send only the minimum necessary data.
4. Before any paid call, show the endpoint, important arguments, current unit price, call count, and total estimate or uncertainty, then obtain confirmation.
5. Use `sandbase_account` before an approved multi-call batch and call `sandbase_run` only with current schema-defined arguments.
6. Poll asynchronous work with `sandbase_run_get` using the same run ID; never resubmit merely because it is pending.
7. Use `sandbase_runs` only to recover status or reconcile observed cost.

If SandBase is unavailable, continue with local work and authorized sources when possible. Do not silently switch providers, fabricate external results, or claim a generation or retrieval succeeded.

## Handoff

Provide the completed artifact or findings, concise reproduction steps, checks actually run, source or asset provenance, SandBase endpoint and run IDs when used, observed cost when available, and any follow-up that still requires user action.
