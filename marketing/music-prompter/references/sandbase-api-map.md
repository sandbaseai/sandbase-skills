# SandBase Music API Map

The installed Skill uses SandBase's six MCP orchestration tools. Music models, schemas, limits, output formats, and prices are discovered at runtime because they can change.

If these tools are unavailable, the Skill can still design prompts and arrangements but cannot generate audio. Connect SandBase using the current instructions in the [SandBase CLI repository](https://github.com/sandbaseai/cli).

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current text-to-music, instrumental, lyric-aware, continuation, or related audio candidates. |
| `sandbase_inspect` | Read a candidate's live input schema, prompt and lyric limits, formats, duration behavior, execution mode, price, and call template. |
| `sandbase_run` | Execute an approved music model using its exact discovered name and schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous music run ID until it completes or fails. |
| `sandbase_runs` | Recover recent run status or reconcile actual cost; it does not create music. |
| `sandbase_account` | Check available balance before an approved multi-call generation batch. |

## Discovery and inspection

Start with capability phrases such as `text to music`, `instrumental music`, `music with lyrics`, or `music continuation`. Inspect every serious candidate immediately before execution. Compare only properties returned by the current schema, including explicit lyric and instrumental controls, output formats, duration behavior, and pricing.

Do not preserve a model-specific parameter snapshot in this repository. Follow the `execute_as` template returned by `sandbase_inspect` and pass only schema-defined arguments to `sandbase_run`.

## Paid-call boundary

Discovery, inspection, and account checks do not authorize generation. Before `sandbase_run`, show the exact endpoint, important arguments, current per-call price, planned call count, and total estimate or uncertainty. One confirmation may cover a clearly enumerated batch.

Preserve every returned run ID. If a call is asynchronous, use `sandbase_run_get` on that ID; never resubmit solely because it remains pending. Use `sandbase_runs` only when a response or run record must be recovered.
