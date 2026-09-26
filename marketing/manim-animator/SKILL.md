---
name: manim-animator
description: "Create code-driven explanatory animations and precise vector graphics with Manim, optionally using SandBase for generated images, narration, music, or transcription. Use for mathematical, scientific, algorithmic, or diagrammatic animation; use a video-generation workflow for photoreal footage."
---

# Manim Animator

Turn an explanation into reproducible Manim source code and a verified video. Draw equations, diagrams, charts, and transitions locally; use SandBase only for generative media that Manim cannot produce itself.

Read [the SandBase API map](references/sandbase-api-map.md) before generating any image or audio asset.

## Route the request

Use Manim when the value comes from exact geometry, mathematical notation, deterministic timing, reproducible diagrams, or a step-by-step conceptual explanation. Prefer another workflow when the main deliverable is:

- photoreal or cinematic generated footage;
- conventional timeline editing of supplied footage;
- a static chart or diagram with no meaningful animation;
- an avatar or talking-head presentation.

Translate named stylistic references into concrete traits such as dark background, minimal palette, hand-drawn-feeling curves, spatial transformations, or deliberate pacing. Do not promise an exact imitation of a creator's identity.

## Preflight

Inspect the current project before creating files:

- determine whether it already uses Manim Community or ManimGL and do not mix their APIs;
- check the installed Python and Manim versions, renderer, FFmpeg, and LaTeX availability;
- preserve the project's existing environment and dependency manager;
- identify output resolution, frame rate, aspect ratio, duration, codec, and caption requirements.

Default to Manim Community for a new project unless the request specifically depends on ManimGL behavior. Do not install system packages, change global environments, or add optional plugins without user authorization. If required tooling is unavailable, return the source and an exact dependency plan instead of claiming a render succeeded.

## Plan scenes

For more than one short idea, create a compact scene plan before coding:

| Field | Record |
|---|---|
| Purpose | Question or idea the scene resolves |
| Duration | Target seconds, or measured narration duration |
| Objects | Equations, labels, shapes, axes, graphs, images, and camera elements |
| State changes | What appears, transforms, moves, highlights, or disappears |
| Explanation | Narration or on-screen text associated with each beat |
| Continuity | Objects and visual state carried into the next scene |
| Technical needs | 2D/3D scene type, LaTeX, updater, plugin, raster asset, or audio |

Keep each scene focused on one conceptual transition. Reuse object instances when continuity matters, and design equations so corresponding terms can transform cleanly.

## Generate optional media through SandBase

Manim code and vector graphics are local work and do not require SandBase. For raster images, narration, music, sound effects, or transcription:

1. Call `sandbase_discover` separately for the needed capability, such as `text to image`, `text to speech`, `text to music`, or `speech to text`.
2. Call `sandbase_inspect` for serious candidates. Confirm language, timing controls, formats, reference-input rules, limits, price, and execution mode.
3. Prefer vector construction over generated raster media when Manim can express the visual precisely.
4. Before any paid call, show the selected endpoint, important arguments, call count, per-call price, and total estimate or uncertainty. Obtain confirmation for the exact call or batch.
5. Use `sandbase_account` before an approved multi-call batch.
6. Call `sandbase_run` with the exact discovered name and only current schema-defined arguments.
7. Poll an asynchronous result with `sandbase_run_get` using the same run ID. Never submit a replacement merely because it is pending.
8. Use `sandbase_runs` only to recover a result or reconcile actual cost.

Generate and save every asset before writing code that references its path. Keep an asset ledger with purpose, file path, SandBase endpoint, run ID, license or provenance, and actual cost when available.

### Narration-first timing

When narration controls the pace:

1. Finalize the narration text per scene.
2. Generate one approved audio clip per scene rather than one monolithic file.
3. Measure each clip with an available local media inspector.
4. Use the measured duration as the scene timing budget.
5. Make the sum of animation `run_time` and waits match that budget through meaningful pacing, not black-frame padding.

Use an inspected transcription capability only when captions or word-level timing are required and the selected schema provides suitable timestamps. Otherwise use scene-level caption timing derived from the narration plan.

## Write maintainable Manim code

- Keep configuration outside scene bodies when the installed Manim version supports project configuration.
- Use named constants for palette, typography, margins, timing, and repeated coordinates.
- Group related objects and use relative placement methods instead of unexplained pixel-like offsets.
- Create axes, labels, and equations with explicit ranges and semantic names.
- Prefer transforms between related states over delete-and-recreate sequences.
- Keep updaters bounded, remove them when no longer needed, and avoid frame-dependent side effects.
- Use camera movement only when it clarifies spatial relationships.
- Ensure text contrast, minimum readable size, safe margins, and enough dwell time.
- Avoid runtime network requests. Resolve external assets before rendering.

For multi-scene output, keep scenes independently renderable and maintain a deterministic source order for final assembly.

## Render and iterate

1. Render every scene at low quality first with caching disabled when stale output is possible.
2. Capture the exit status and a concise error tail per scene.
3. Fix import, API-version, LaTeX, missing-asset, geometry, and timing errors before visual review.
4. Inspect representative frames at the beginning, key transformations, dense layouts, scene boundaries, and ending.
5. Revise overlaps, clipping, illegible text, jerky transforms, excessive motion, and continuity breaks.
6. Stop after three unsuccessful revision loops and return the source, logs, and remaining blocker.
7. After all scenes pass, render at the requested final quality and concatenate or mix audio with local deterministic tooling.

Do not start a costly final render until a low-quality preview has passed technical and visual checks. Do not edit encoded frames by hand to hide a source-level defect.

## Final verification

Check the final container, video and audio codecs, duration, dimensions, frame rate, decodability, audio presence, caption presence, and representative frames. Watch the complete render when the host supports playback. For narrated work, compare each scene's visual duration with its measured clip and check that speech is not cut off.

Return the Manim source, dependency or run command, final video, scene plan, generated-asset ledger with SandBase run IDs and costs, and any known rendering or timing compromises. Do not claim completion if a scene failed, a required asset is missing, or the final file was not checked.
