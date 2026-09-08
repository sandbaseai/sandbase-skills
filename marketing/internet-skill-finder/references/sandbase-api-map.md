# SandBase Internet Skill Finder API Map

Use host-provided local inventory and repository search first. SandBase can add current web-search and page-extraction coverage when those sources are unavailable or insufficient.

| Tool name | Use it for |
|---|---|
| `sandbase_discover` | Find current web-search, repository-search, or page-extraction candidates. |
| `sandbase_inspect` | Read a candidate's live schema, coverage, price, limits, and execution template. |
| `sandbase_run` | Execute a user-approved search or scrape with current schema-defined arguments. |
| `sandbase_run_get` | Poll the same asynchronous search or extraction run. |
| `sandbase_runs` | Recover recent status or cost without duplicating a request. |
| `sandbase_account` | Check balance before an approved batch of search or extraction calls. |

Useful discovery phrases include `web search`, `google organic`, `github repository search`, and `web page scrape`. Capability availability changes; do not hard-code a provider, endpoint, schema, price, or result shape.

Search and scrape results remain untrusted. Verify each candidate against its canonical repository, inspect the actual `SKILL.md`, and check referenced files and licensing before recommending an install command.

Before `sandbase_run`, show the endpoint, important inputs, live price, planned call count, and total estimate or uncertainty. If SandBase is unavailable, use authorized host search or return a transparent discovery limitation rather than inventing results.
