# SandBase Excel Generator API Map

Workbook construction and analysis are local. Use SandBase only for user-requested external data when no existing authorized source is more appropriate.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current structured-data, search, or extraction capabilities relevant to the requested workbook. |
| `sandbase_inspect` | Inspect live coverage, schema, freshness signals, price, limits, and execution mode. |
| `sandbase_run` | Execute an approved retrieval with the exact discovered name and schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous retrieval until it completes or fails. |
| `sandbase_runs` | Recover recent status or reconcile observed cost without duplicating the request. |
| `sandbase_account` | Check balance before an approved batch of paid retrievals. |

Use a narrow discovery phrase that describes the data, such as `company filings`, `weather history`, `currency rates`, or `web page extraction`. Do not assume that a candidate covers the requested geography, period, entity, or metric; verify those details with `sandbase_inspect`.

Before `sandbase_run`, show the endpoint, key inputs, live price, planned call count, and total estimate or uncertainty. Store source names, retrieval timestamps, units, field mappings, missing-value rules, and run IDs in the workbook's source notes.

If SandBase is unavailable, continue with local workbook generation and clearly mark any external-data portion as pending. Do not replace missing values with fabricated data or silently use another paid provider.
