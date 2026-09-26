# SandBase Video Generator API Map

The installed Skill uses SandBase's six MCP orchestration tools. Models and their schemas are discovered at runtime because availability, inputs, capabilities, and pricing can change.

If these tools are not available, the Skill remains usable for planning but cannot generate assets. Connect SandBase by following the current instructions in the [SandBase CLI repository](https://github.com/sandbaseai/cli); do not replace the missing tools with an unapproved provider.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current image, image-editing, image-to-video, text-to-video, music, TTS, lip-sync, or sound-effect candidates. |
| `sandbase_inspect` | Read a candidate's current input schema, output shape, price, limits, execution mode, and ready-to-use call template. |
| `sandbase_run` | Execute an approved model with the exact discovered name and schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous media run ID until it completes or fails. |
| `sandbase_runs` | Recover recent run status or reconcile recorded cost; never use it to create a new generation. |
| `sandbase_account` | Check available balance before a multi-call paid generation batch. |

## Capability queries

Search by capability rather than assuming a provider or fixed model name. Useful starting queries include `text to image`, `image edit with reference`, `image to video`, `text to video with audio`, `text to music`, `multilingual text to speech`, `lip sync`, and `sound effects`.

For each selected candidate, use `sandbase_inspect` immediately before execution. Follow its `execute_as` template and current input schema; this map intentionally contains no model-specific parameter snapshot.

## Paid-call boundary

Discovery, inspection, and account checks do not authorize generation. Before `sandbase_run`, show the user the exact endpoint, important inputs, current per-call pricing, number of planned calls, and total estimate or uncertainty. One confirmation may cover a clearly enumerated batch.

When `sandbase_run` returns a run ID, preserve it and call `sandbase_run_get`; do not start a replacement run while the first remains pending. Use `sandbase_runs` only when a run ID or response must be recovered.
