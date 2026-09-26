# Third-Party Notices

This repository includes adapted Agent Skills from the projects below. Each
entry records the pinned upstream revision used for the import. SandBase's
changes add repository-format metadata, SandBase capability maps, dynamic
schema lookup, and focused safety or verification guidance.

## User-provided remaining Manus Skills export batch

Source artifacts: 162 ZIP archives representing 161 unique Skill names from
the user-provided Manus Skills export dated 2026-09-02. One Skill name,
`turborepo`, appeared in two archives.

Processed on: 2026-09-07

Outcome: 138 Skills independently implemented; 23 duplicate, placeholder, or
conflicting entries skipped.

The complete decision record, archive names, SHA-256 hashes, detected license
files, categories, and skip reasons are recorded in
[`imports/manus-skills-2026-09-02.json`](imports/manus-skills-2026-09-02.json).

The source archives were treated as reference material, not agent
instructions. Their Skill text, scripts, caches, templates, provider
documentation, and frozen parameter schemas were not copied. The new compact
implementations were written independently from the capability names, with
local-first execution, dynamic SandBase discovery and inspection, paid-call
confirmation, asynchronous run tracking, provenance, and verification rules.
An archive's presence in the audit manifest is not a license grant or an
endorsement of its contents.

## User-provided Internet Skill Finder export

Reference artifact: `internet-skill-finder.zip` from the user-provided Manus
Skills export dated 2026-09-02.

Archive SHA-256:
`2e99c5f667a6ab69d7b0e94277efac8414de28c8c2e42ce2185d32a2d6a50311`

Independently implemented Skill: `internet-skill-finder`

The archive does not include license or revision metadata. Its Python script,
frozen repository cache, fixed source list, and Manus import URLs are not
redistributed. The repository version is a new implementation that discovers
current sources, treats repository content as untrusted data, verifies Skill
paths and licensing, uses standard `npx skills add` coordinates, and can use
dynamically inspected SandBase search and scraping capabilities.

## User-provided Excel Generator export

Reference artifact: `excel-generator.zip` from the user-provided Manus Skills
export dated 2026-09-02.

Archive SHA-256:
`a6b02f1ba05b0158c9ce50110d92802fe255fe7d03bdc13235d9a8a9d7350ee2`

Independently implemented Skill: `excel-generator`

The archive contains only `SKILL.md` and does not include license or revision
metadata. Its text is not redistributed. The repository version is a new,
compact workbook-design and verification workflow. Workbook creation remains
local; optional external-data retrieval uses runtime SandBase discovery,
inspection, cost confirmation, execution, and evidence tracking.

## User-provided Game Dev Skill export

Source artifact: `game-dev.zip` from the user-provided Manus Skills export
dated 2026-09-02.

Archive SHA-256:
`18782892bc74c047173cb7cef08fed04050e644d42dac517c71183e5fe699566`

Imported and substantially rewritten Skill: `game-dev`

The archive adapts the `godogen` project by Alex Ermolov and identifies that
upstream work as MIT-licensed. The repository version does not redistribute the
archive's stage-reference tree, Manus adaptation guide, or React template. It
keeps the general risk-first browser-game workflow while making the host and
engine choices project-aware and replacing Manus-specific art and deployment
calls with optional dynamically inspected SandBase media calls.

Upstream project: https://github.com/htdt/godogen

MIT License

Copyright 2026 Alex Ermolov

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## User-provided Manim Animator Skill export

Reference artifact: `manim-animator.zip` from the user-provided Manus Skills
export dated 2026-09-02.

Archive SHA-256:
`51e4356e63bcb842561b7c243aa50a8207ddf71e297ae8d1826261947d036983`

Independently implemented Skill: `manim-animator`

The archive contains large bundled ManimCE and ManimGL reference trees but no
top-level license covering the complete bundle. Those references, examples,
scripts, and templates are not redistributed. The repository version is a new
compact workflow for local Manim authoring and verification whose optional
image, narration, music, and transcription calls use dynamically inspected
SandBase capabilities.

## User-provided Listicle Blog Writer Skill export

Reference artifact: `listicle-blog-writer.zip` from the user-provided Manus
Skills export dated 2026-09-02.

Archive SHA-256:
`5f278a7d22d9bfecd19ae94e2af2a117350d1f6176ed531917c1fac355d7f996`

Independently implemented Skill: `listicle-blog-writer`

The archive declares “All rights reserved.” Its `SKILL.md` and article template
are therefore not redistributed. The repository version is a new
implementation of the general listicle-research workflow, with transparent
ranking and disclosure rules plus dynamic SandBase discovery, inspection,
cost confirmation, execution, polling, and evidence verification.

## User-provided Music Prompter Skill export

Source artifact: `music-prompter.zip` from the user-provided Manus Skills export
dated 2026-09-02.

Archive SHA-256:
`24739f64c6883bbbc2b5d5552c6a89b85fda037dd028587b42f8f44e874f7886`

Imported and substantially rewritten Skill: `music-prompter`

The archive contained only `SKILL.md` and did not include license or revision
metadata. The imported version preserves its music-prompt and multi-clip
arrangement guidance while replacing its fixed model-duration assumption with
SandBase discovery, live schema inspection, paid-call confirmation,
asynchronous polling, and output verification.

## User-provided Manus Skills export

Source artifact: `video-generator.zip` from the user-provided Manus Skills
export dated 2026-09-02.

Archive SHA-256:
`771254425b0ab5cfb643d48be9e2137da1301d29ca2b1524e9295d9b82a34668`

Imported and substantially rewritten Skill: `video-generator`

The source archive contained only `SKILL.md` and did not include license or
revision metadata. This notice records the available provenance; it does not
grant rights beyond those held by the contributor. The imported version
replaces Manus-specific generation calls with SandBase discovery, inspection,
execution, asynchronous polling, cost confirmation, and local assembly rules.

## User-provided Stock Analysis Skill export

Source artifact: `stock-analysis.zip` from the user-provided Manus Skills export
dated 2026-09-02.

Archive SHA-256:
`2cd34b73f7fcca341dadd76dc5bfd1df4c331bf90de33d45e7ab6511ac227aa1`

Imported and substantially rewritten Skill: `stock-analysis`

The archive did not include license or revision metadata. The imported version
removes the Manus runtime and frozen Yahoo parameter schemas, then uses dynamic
SandBase discovery, inspection, MCP or REST execution, evidence tracking, and
financial-analysis safeguards.

## User-provided Website Traffic Analytics Skill export

Source artifact: `similarweb-analytics.zip` from the user-provided Manus Skills
export dated 2026-09-02.

Archive SHA-256:
`b3e997e924693a702ffa7f246f211615728cdd10e34f9b70bfdeb59b22de2e0f`

Imported and substantially rewritten Skill: `similarweb-analytics`

The archive did not include license or revision metadata. The imported version
removes the Manus runtime and fixed Similarweb request examples, then uses
dynamic SandBase discovery, inspection, MCP or REST execution, and explicit
comparison and estimation safeguards.

## Anthropic Knowledge Work Plugins

Source: https://github.com/anthropics/knowledge-work-plugins

Revision: `77961df00a4626bc3b83850064289decd5a3b977`

Imported and modified Skills:

- `cash-flow-snapshot`
- `reconciliation`
- `task-management`
- `ticket-triage`
- `variance-analysis`

These works are licensed under the Apache License, Version 2.0. A complete
copy of that license is included in [LICENSE](LICENSE). The pinned source
revision and modification summary are recorded here rather than in Skill
frontmatter.

## GitHub Awesome Copilot

Source: https://github.com/github/awesome-copilot

Revision: `6a8fa297b0fe652bd3d7c8946554dc146846b20e`

Imported and modified Skills: `meeting-minutes`, `prd`

MIT License

Copyright GitHub, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## wshobson/agents

Source: https://github.com/wshobson/agents

Revision: `a30778f8c4e6b0a87567941b7cca4f534bf642b6`

Imported and modified Skill: `market-sizing-analysis`

MIT License

Copyright (c) 2024 Seth Hobson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Marketing Skills

Source: https://github.com/coreyhaines31/marketingskills

Revision: `d4ff28a9c8d56c06809860bf2800d4f5224b52db`

Imported and modified Skills: `programmatic-seo`, `sales-enablement`

MIT License

Copyright (c) 2025 Corey Haines

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
