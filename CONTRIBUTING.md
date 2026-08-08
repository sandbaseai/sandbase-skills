# Contributing

Thank you for improving SandBase Skills.

## Change an existing Skill

1. Update `marketing/<skill-id>/SKILL.md`. Keep the workflow concise and do not add API keys, endpoint parameter snapshots, or provider-specific credentials.
2. If its display or endpoint bindings change, update `catalog/skills/<skill-id>.json`.
3. If its registered endpoint bindings change, update `registry/data/skills/sandbase/<skill-id>/plugin.json` with the same endpoint set.
4. Run the validation commands below.

## Add a new Skill

1. Create `marketing/<skill-id>/SKILL.md` with `name` and `description` YAML frontmatter.
2. Add `marketing/<skill-id>/agents/openai.yaml` with display metadata and a default prompt that names `$<skill-id>`.
3. Add one entry to `skills.json`.
4. Add one display record under `catalog/skills/` and one registry manifest under `registry/data/skills/sandbase/`.
5. Declare the same `tool_name` values in the catalog and the registry manifest.

## Validate before opening a pull request

```bash
python3 scripts/skillpack.py validate
python3 -m unittest discover -s tests -v
```

Keep changes focused. Do not commit secrets, generated endpoint schemas, copied provider documentation, or unrelated files.
