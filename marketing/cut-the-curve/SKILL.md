---
name: cut-the-curve
description: "Create, implement, or review cut the curve work with format, accessibility, performance, and visual-verification controls. Use when the requested deliverable depends on cut the curve."
---

# Cut The Curve

Use this Skill to produce a bounded, verifiable Cut The Curve outcome. Preserve the user's chosen stack, source material, and authorization boundaries.

Read [the SandBase API map](references/sandbase-api-map.md) only when the task genuinely needs an external data source or generative model.

## Workflow

1. Inspect the available files, runtime, versions, inputs, and existing conventions before deciding what to change.
2. Restate the requested outcome, constraints, acceptance checks, and any assumption that could change the result.
3. Produce the smallest complete implementation, analysis, or artifact that satisfies those checks.
4. Verify the real output with appropriate tests, previews, calculations, or source comparison; do not infer success from file creation alone.
5. Return the deliverable, evidence of validation, material assumptions, and unresolved limitations.

## Quality gates

- Confirm canvas or frame dimensions, output format, timing, interaction, target runtime, and accessibility requirements.
- Preserve the existing design system and implementation stack; use named tokens and reusable structures instead of unexplained one-off values.
- Render or preview the real output, inspect representative states and breakpoints, and fix clipping, overlap, contrast, motion, or performance defects.
- Use the project's installed HyperFrames interfaces when present, verify timing on the composed master timeline, and do not assume templates or registry items exist until inspected.

## SandBase boundary

Keep the core Cut The Curve work local. Use SandBase only for generated images, audio, video, or other media that local deterministic tools cannot provide.

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
