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
        self.assertIn("Validated 1 skill(s).", result.stdout)

    def test_seo_skill_declares_sandbase_tool_map(self):
        skill_dir = ROOT / "marketing" / "seo-keyword-research"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(encoding="utf-8")
        self.assertIn("sandbase_call_tool", skill_text)
        self.assertIn("sandbase_describe_tool", skill_text)
        self.assertIn("dataforseo_v3_dataforseo_labs_google_keyword_suggestions_live", api_map)
        self.assertNotIn("AISA_API_KEY", skill_text + api_map)
        self.assertNotIn("api.aisa", skill_text + api_map)

    def test_dry_run_does_not_write_and_real_install_copies_skill(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            project = Path(temp_dir) / "sample-project"
            project.mkdir()
            dry_run = self.run_cli(
                "install", "--target", "codex", "--dest", str(project), "--dry-run"
            )
            installed = project / ".codex" / "skills" / "seo-keyword-research"
            self.assertEqual(dry_run.returncode, 0, dry_run.stderr)
            self.assertFalse(installed.exists())
            install = self.run_cli("install", "--target", "codex", "--dest", str(project))
            self.assertEqual(install.returncode, 0, install.stderr)
            self.assertTrue((installed / "SKILL.md").is_file())

    def test_catalog_contains_only_existing_skill_paths(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            self.assertTrue((ROOT / entry["path"] / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
