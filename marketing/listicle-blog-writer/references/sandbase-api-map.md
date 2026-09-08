# SandBase Listicle Research API Map

This Skill uses SandBase's six MCP orchestration tools for optional live research. The available SERP, keyword, scraping, review, and screenshot capabilities are discovered at runtime so the installed Skill does not depend on a frozen provider schema.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current organic SERP, related-query, page extraction, public review, and webpage screenshot candidates. |
| `sandbase_inspect` | Read a candidate's current schema, market controls, result limits, output shape, price, and execution mode. |
| `sandbase_run` | Execute an approved research or screenshot capability with exact schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous research run ID until completion or failure. |
| `sandbase_runs` | Recover recent result status or reconcile actual cost; it does not start research. |
| `sandbase_account` | Check available balance before an approved multi-call research batch. |

## Capability selection

Search separately for the evidence needed. Useful starting phrases include `google organic serp`, `related keywords`, `scrape markdown`, `page screenshot`, and the name of a public review source. Inspect serious candidates immediately before execution and follow the returned `execute_as` template.

Prefer one reusable SERP response over repeated category searches. Fetch or screenshot individual product pages only when that evidence is part of the requested deliverable. Official pages support first-party feature and pricing claims but must not be presented as independent reviews.

## Paid-call boundary

Discovery and inspection do not authorize paid research. Before `sandbase_run`, show the endpoint names, important inputs, current prices, expected call count, and total estimate or uncertainty. One confirmation may cover a clearly enumerated batch.

Preserve returned run IDs and poll asynchronous work with `sandbase_run_get`. Do not create replacement calls while a run is pending. Use `sandbase_runs` only for recovery or cost reconciliation.
