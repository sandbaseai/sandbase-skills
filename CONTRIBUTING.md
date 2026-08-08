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

1. Create `marketing/<skill-id>/SKILL.md` with `name` and `description` YAML frontmatter.
2. Add a `references/sandbase-api-map.md` file that documents every tool available to the installed Skill.
3. Add one entry to `skills.json`.
4. Add one display record under `catalog/skills/` and, when SandBase Registry import is needed, one manifest under `integrations/sandbase-registry/data/skills/sandbase/`.
5. Set the catalog `install.cli` to `npx skills add sandbaseai/sandbase-skills --skill <skill-id> --agent codex`.
6. Declare the same `tool_name` values in the catalog, installed API map, and registry manifest.

## Validate before opening a pull request

```bash
python3 scripts/skillpack.py validate
python3 -m unittest discover -s tests -v
```

Keep changes focused. Do not commit secrets, generated endpoint schemas, copied provider documentation, or unrelated files.
