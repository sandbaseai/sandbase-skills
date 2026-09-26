# SandBase Game Dev API Map

Game code, builds, tests, browser automation, and deterministic asset processing remain local. SandBase is optional and is used only for user-approved generated media.

The installed Skill uses SandBase's six orchestration tools. Capability availability, schemas, inputs, limits, pricing, and execution modes are discovered at runtime.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current text-to-image, image-editing, reference-image, transparency, or other required media candidates. |
| `sandbase_inspect` | Read a candidate's live schema, supported formats and ratios, limits, price, and execution template. |
| `sandbase_run` | Execute a user-approved asset-generation call with the exact discovered name and current arguments. |
| `sandbase_run_get` | Poll the same asynchronous asset run until completion or failure. |
| `sandbase_runs` | Recover recent run status or reconcile observed cost without submitting another generation. |
| `sandbase_account` | Check balance before an approved multi-asset batch. |

Search by capability rather than provider name. Useful starting queries include `text to image`, `image edit with reference`, `game texture`, `sprite sheet`, and `transparent background image`. Search results do not guarantee that a model can produce a mechanically correct sprite sheet or seamless texture; confirm the live schema and verify the returned asset in the game.

Before `sandbase_run`, present the exact endpoint, important inputs, current price, call count, and total estimate or uncertainty. Discovery and inspection are not permission to generate.

If SandBase is unavailable, continue with local code and user-supplied or procedural assets. Do not silently switch to another paid generation provider or claim that an asset was generated.
