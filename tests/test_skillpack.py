import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "skillpack.py"


class SkillpackTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_catalog_and_skills_validate(self):
        result = self.run_cli("validate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validated 5 skill(s).", result.stdout)

    def test_seo_skill_declares_sandbase_tool_map(self):
        skill_dir = ROOT / "marketing" / "seo-keyword-insights"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(encoding="utf-8")
        self.assertIn("sandbase_call_tool", skill_text)
        self.assertIn("sandbase_describe_tool", skill_text)
        self.assertIn("dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live", api_map)
        self.assertIn("dataforseo_v3_serp_google_autocomplete_live_advanced", api_map)
        self.assertTrue((skill_dir / "references" / "example-workflows.md").is_file())

    def test_seo_web_metadata_is_display_ready(self):
        metadata_path = ROOT / "catalog" / "skills" / "seo-keyword-insights.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        self.assertEqual(metadata["id"], "seo-keyword-insights")
        self.assertIn("prompt", metadata["install"])
        self.assertEqual(metadata["api"]["pricing_model"], "usage-based/call")
        self.assertGreaterEqual(len(metadata["api"]["endpoints"]), 10)
        for endpoint in metadata["api"]["endpoints"]:
            self.assertEqual(endpoint["method"], "POST")
            self.assertTrue(endpoint["operation"])
            self.assertTrue(endpoint["tool_name"])

    def test_keyword_suggestions_uses_dynamic_schema(self):
        metadata = json.loads(
            (ROOT / "catalog" / "skills" / "seo-keyword-insights.json").read_text(encoding="utf-8")
        )
        endpoint = next(
            item
            for item in metadata["api"]["endpoints"]
            if item["tool_name"] == "dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live"
        )
        self.assertEqual(endpoint["capability_id"], "7899ddd4-f405-4fb0-a073-35ac83042d97")
        self.assertEqual(endpoint["schema"]["source"], "sandbase-capability-registry")
        self.assertEqual(metadata["api"]["schema_resolution"]["strategy"], "dynamic")

    def test_registry_example_matches_the_public_endpoint_catalog(self):
        plugin = json.loads(
            (
                ROOT
                / "registry"
                / "data"
                / "skills"
                / "sandbase"
                / "seo-keyword-insights"
                / "plugin.json"
            ).read_text(encoding="utf-8")
        )
        catalog = json.loads(
            (ROOT / "catalog" / "skills" / "seo-keyword-insights.json").read_text(encoding="utf-8")
        )
        self.assertEqual(plugin["name"], "sandbase/seo-keyword-insights")
        self.assertEqual(plugin["type"], "skill")
        required = set(plugin["unified_schema"]["required_endpoints"])
        displayed = {item["tool_name"] for item in catalog["api"]["endpoints"]}
        self.assertEqual(required, displayed)
        self.assertEqual(plugin["metadata"]["endpoint_count"], len(displayed))

    def test_dry_run_does_not_write_and_real_install_copies_skill(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            project = Path(temp_dir) / "sample-project"
            project.mkdir()
            dry_run = self.run_cli(
                "install", "--target", "codex", "--dest", str(project), "--dry-run"
            )
            installed = project / ".codex" / "skills" / "seo-keyword-insights"
            self.assertEqual(dry_run.returncode, 0, dry_run.stderr)
            self.assertFalse(installed.exists())
            install = self.run_cli("install", "--target", "codex", "--dest", str(project))
            self.assertEqual(install.returncode, 0, install.stderr)
            self.assertTrue((installed / "SKILL.md").is_file())

    def test_catalog_contains_only_existing_skill_paths(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            self.assertTrue((ROOT / entry["path"] / "SKILL.md").is_file())

    def test_every_catalog_entry_has_a_matching_registry_manifest(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            self.assertTrue((ROOT / entry["registry_path"]).is_file())

    def test_every_skill_has_agent_metadata(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            self.assertTrue((ROOT / entry["path"] / "agents" / "openai.yaml").is_file())


if __name__ == "__main__":
    unittest.main()
