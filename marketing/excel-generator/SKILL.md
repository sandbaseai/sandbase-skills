---
name: excel-generator
description: "Create, edit, analyze, and verify professional Excel workbooks for general business and operational use. Use when the deliverable is an .xlsx file; use a finance-specific modeling workflow for valuation or regulated financial models."
---

# Excel Generator

Create a workbook that is useful immediately on open: accurate, navigable, editable where appropriate, and visually clear. Workbook generation is local and deterministic. SandBase is optional only when the user asks for current external data and no authorized dedicated source is already available.

Read [the SandBase API map](references/sandbase-api-map.md) only when external data retrieval is required.

## Define the workbook contract

Infer reasonable defaults from the request, but resolve missing choices that change the result:

- intended decisions and audience;
- input data, source, freshness, units, and missing-value meaning;
- required sheets, calculations, filters, charts, and editable inputs;
- locale, currency, date system, time zone, and decimal conventions;
- delivery path, Excel compatibility, print or PDF requirements, and whether macros are allowed.

Never introduce macros, external workbook links, hidden tracking, or network-refresh behavior unless the user explicitly requests them and understands the implications.

## Design before styling

Choose a structure that matches the task rather than a fixed template. For a multi-sheet analytical workbook, a useful default is:

- an Overview sheet with purpose, freshness, headline metrics, and navigation;
- one or more clean input or source-data sheets;
- calculation or analysis sheets when formulas should remain inspectable;
- notes or definitions when methodology needs explanation.

Keep raw/source data distinct from calculated output. Use Excel tables or well-bounded ranges for data users will filter or extend. Freeze headers on long sheets and add navigation when the workbook has several sheets.

## Preserve data meaning

- Keep identifiers as text when leading zeros matter.
- Use true date, time, Boolean, and numeric cell types rather than formatted strings.
- Distinguish blank, zero, not applicable, and unavailable values.
- State units in headers and apply consistent precision within a field.
- Use formulas when users should be able to change inputs and see results update.
- Avoid volatile or version-specific formulas unless they provide clear value and the target Excel version supports them.
- Record source URLs, retrieval dates, time ranges, transformations, and assumptions near the affected data or in a notes sheet.

For finance, valuation, tax, audit, or regulated reporting, preserve the user's domain template and standards. Do not apply decorative styling that obscures model inputs, formula lineage, review controls, or required conventions.

## Use restrained visual hierarchy

Use one coherent theme and let formatting communicate structure:

- descriptive title and subtitle;
- clear table headers and section boundaries;
- consistent number formats for both values and formula results;
- meaningful conditional formatting tied to defined thresholds;
- charts only when they make a comparison, distribution, composition, or trend easier to see;
- accessible contrast and readable sizing.

Avoid merged cells inside data tables, rainbow palettes, unexplained icons, 3D charts, clipped labels, and decorative elements that compete with the data. Ensure charts do not overlap tables or each other.

## Optional external data through SandBase

Prefer user-provided files, existing authorized connectors, and dedicated APIs the user already has. Do not use SandBase for purely local workbook creation or for data already present in the workspace.

When SandBase is the appropriate source:

1. Call `sandbase_discover` with a narrow capability query for the required data.
2. Call `sandbase_inspect` for viable candidates and compare coverage, freshness, schema, price, limits, and execution mode.
3. Explain what source is being queried and how its fields will map into the workbook.
4. Before any paid call, show the endpoint, important arguments, current price, call count, and total estimate or uncertainty, then obtain confirmation.
5. Use `sandbase_account` before an approved multi-call batch and call `sandbase_run` only with live schema-defined arguments.
6. Poll asynchronous work with `sandbase_run_get` using the same run ID; do not resubmit a pending request.
7. Use `sandbase_runs` only to recover status or reconcile observed cost.

Treat retrieved values as evidence, not truth. Preserve provider attribution and timestamps, flag estimates, and never silently convert missing data to zero.

## Verify the file

After writing the workbook:

1. reopen it with an independent reader when available;
2. verify sheet names, dimensions, tables, filters, panes, validations, named ranges, formulas, links, and charts;
3. scan formulas for broken references and error values;
4. confirm numeric and date formats on both input and formula cells;
5. render or preview representative sheets and inspect clipping, overlaps, unreadable text, excess blank space, and print boundaries;
6. confirm the final file exists at the promised path and opens without a repair warning.

Formula-writing libraries often do not calculate formulas. If no calculation engine is available, say that formula results will calculate when opened in Excel and do not invent cached results.

Return the workbook, a short sheet map, key assumptions, source and freshness notes, validation performed, and any limitations.
