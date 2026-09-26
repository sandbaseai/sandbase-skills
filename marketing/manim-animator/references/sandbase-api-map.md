# SandBase Media API Map for Manim

Manim rendering is local and deterministic. This Skill uses SandBase's six MCP orchestration tools only when a composition needs generated raster images, narration, music, sound effects, or transcription.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current image, TTS, music, sound-effect, or speech-to-text candidates. |
| `sandbase_inspect` | Read a candidate's current schema, language and format support, timing controls, limits, price, and execution mode. |
| `sandbase_run` | Execute an approved media model using the exact discovered name and schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous media run ID until it completes or fails. |
| `sandbase_runs` | Recover recent result status or reconcile actual cost; it does not generate an asset. |
| `sandbase_account` | Check available balance before an approved multi-call media batch. |

## Selection rules

Search by capability rather than provider name. Useful starting phrases include `text to image`, `text to speech`, `text to music`, `sound effects`, and `speech to text`. Inspect candidates immediately before execution and follow the returned `execute_as` template.

Prefer native Manim vectors for mathematical and diagrammatic content. Use generated media only when it adds information or production value that cannot be expressed precisely with local shapes, text, equations, plots, and transforms.

## Paid-call boundary

Discovery, inspection, and local rendering do not authorize generation. Before `sandbase_run`, show the exact endpoint, important inputs, current price, planned call count, and total estimate or uncertainty. One confirmation may cover a clearly enumerated batch.

Preserve each run ID and poll asynchronous work with `sandbase_run_get`; do not resubmit while it remains pending. Use `sandbase_runs` only for result recovery or cost reconciliation.
