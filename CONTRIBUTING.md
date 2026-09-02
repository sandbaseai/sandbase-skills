# Contributing

Thank you for improving SandBase Skills.

## Submit a contribution

External contributors should use GitHub's standard fork-and-pull-request workflow:

1. Fork `sandbaseai/sandbase-skills` on GitHub.
2. Clone your fork and create a focused branch, for example `add/reddit-insight-skill` or `fix/exa-install-instructions`.
3. Make the change, then run the validation commands below.
4. Commit clear, English commit messages and push the branch to your fork.
5. Open a pull request from your fork to `sandbaseai/sandbase-skills:main`. Explain the user problem, the changed Skill, and how you validated it.

Do not push directly to the upstream repository. Keep one pull request focused on one user-facing change.

## Change an existing Skill

1. Update `marketing/<skill-id>/SKILL.md`. Keep the workflow concise and do not add API keys, endpoint parameter snapshots, or provider-specific credentials.
2. If its display or endpoint bindings change, update `catalog/skills/<skill-id>.json`.
3. If its SandBase Registry endpoint bindings change, update `integrations/sandbase-registry/data/skills/sandbase/<skill-id>/plugin.json` with the same endpoint set.
4. Run the validation commands below.

## Add a new Skill

Every installable Skill needs a `research/<skill-id>/SKILL.md` or
`marketing/<skill-id>/SKILL.md` with matching `name` and a discriminating
`description` in YAML frontmatter. Add it to the English README catalog and to
exactly one group in `skills.sh.json`, then rebuild the Claude marketplace.

Choose one of these integration tracks:

### Host-only Skill

Use this track when the workflow operates on user-provided files or uses
capabilities supplied by the host agent and has no required SandBase endpoint.

1. Keep tool selection host-neutral and document optional dependencies in the Skill.
2. Do not add the Skill to `skills.json`, `catalog/skills/`, or the SandBase Registry.
3. Do not invent a placeholder endpoint merely to enroll the Skill in the API catalog.

### SandBase-backed Skill

Use this track when the installed workflow calls one or more SandBase capabilities.

1. Add `references/sandbase-api-map.md` documenting every available capability.
2. Add one entry to `skills.json`.
3. Add one display record under `catalog/skills/` and one manifest under
   `integrations/sandbase-registry/data/skills/sandbase/`.
4. Set the catalog `install.cli` to
   `npx skills add sandbaseai/sandbase-skills --skill <skill-id> --agent codex`.
5. Declare the same `tool_name` values in the catalog, installed API map, and
   registry manifest.

For adapted third-party work, record the upstream URL, pinned revision,
original license, and modifications in `THIRD_PARTY_NOTICES.md` and preserve
any notices required by the upstream license.

## Validate before opening a pull request

```bash
python3 scripts/skillpack.py validate
python3 -m unittest discover -s tests -v
npm test
npm run marketplace:build
npm run marketplace:check
```

Changes to the DeepSeek Harness installer must also preserve the native DSH
layout `.dsh/skills/<skill-id>/SKILL.md`; `tests/test_install_dsh.py` covers the
copy and overwrite-safety contract.

Keep changes focused. Do not commit secrets, generated endpoint schemas, copied provider documentation, or unrelated files.
