# SandBase Business Model API Map

Core Business Model work remains local. SandBase is optional and is used only for current external evidence, search, scraping, enrichment, or model inference that is not already available through the user's authorized tools.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current capabilities by task rather than assuming a provider or endpoint. |
| `sandbase_inspect` | Read the live input schema, coverage, limits, output shape, price, and execution template. |
| `sandbase_run` | Execute a user-approved capability with the exact discovered name and schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous run until it completes or fails. |
| `sandbase_runs` | Recover recent run status or reconcile observed cost without submitting a duplicate. |
| `sandbase_account` | Check balance before an approved multi-call batch. |

Before `sandbase_run`, present the selected endpoint, important inputs, current pricing, planned call count, and total estimate or uncertainty. Discovery and inspection are not permission to execute a paid call.

Capability availability changes. Do not hard-code model names, provider parameters, prices, output URLs, or result schemas. Prefer an existing dedicated integration or user-provided API access when it already covers the request.
