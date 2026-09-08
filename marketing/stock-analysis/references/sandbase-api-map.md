# SandBase Stock Analysis API Map

Use one SandBase transport for a coherent retrieval batch. Capability names, schemas, availability, and pricing are resolved at runtime; this Skill intentionally does not preserve the original Manus/Yahoo parameter snapshot.

## MCP transport

Use this mode when the host exposes the current SandBase MCP bridge:

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current company-profile, market-history, ownership, insider, filing, valuation, or analyst-data capabilities. |
| `sandbase_inspect` | Read a candidate's live schema, output shape, price, limits, execution mode, and call template. |
| `sandbase_run` | Execute an approved capability with the exact discovered name and schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous run ID until it completes, fails, or times out. |
| `sandbase_runs` | Reconcile recent run status or cost when a response or run ID must be recovered. |
| `sandbase_account` | Check account balance before an approved multi-call batch. |

Start with focused queries such as `public company profile`, `historical stock prices`, `insider transactions`, or `SEC filings`. Inspect every serious candidate before execution. Do not assume that a capability is backed by Yahoo or that a name observed in another runtime exists in SandBase.

## REST transport with an API key

Use this mode only when the host can make HTTPS requests and `SANDBASE_API_KEY` is already configured in its environment. Never ask the user to paste the key into chat, a prompt, a generated report, or a command argument that will be logged.

The official REST equivalents are:

| Operation | Request |
|---|---|
| Discover | `GET https://api.sandbase.ai/v1/models?q=<capability>&type=` |
| Inspect | `GET https://api.sandbase.ai/v1/models/<full-logical-name>` |
| Account check | `GET https://api.sandbase.ai/v1/account/balance` |
| Execute | `POST https://api.sandbase.ai/v1/run` |
| Poll | `GET https://api.sandbase.ai/v1/run/<opaque-id>` |

Authenticate each request with the environment value as an HTTP Bearer token. For execution, send `model` plus capability-specific fields at the top level of the JSON body; do not wrap them in an `input` object. Resolve those fields from the live model detail response. An explicitly empty `type` query removes the model-list default of `llm`, which is necessary when discovering API capabilities.

Treat HTTP 200 as a synchronous result and HTTP 202 as an asynchronous acceptance. For 202, preserve the returned opaque `id` and poll only that ID every 5–10 seconds until `completed`, `failed`, or `timeout`. Stop and report 401, 402, or 403 responses; never expose the credential or retry a paid request blindly.

## Evidence and cost boundary

Discovery and inspection do not authorize a paid data call. Before a batch, disclose the selected logical capability names, important arguments, current price when available, and number of calls. Reuse a completed response within the same analysis instead of paying for the same data twice.
