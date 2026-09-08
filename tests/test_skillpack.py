import json
import subprocess
import sys
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
        self.assertIn("Validated 182 skill(s).", result.stdout)

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
        self.assertEqual(
            metadata["install"]["cli"],
            "npx skills add sandbaseai/sandbase-skills --skill seo-keyword-insights --agent codex",
        )
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
                / "integrations"
                / "sandbase-registry"
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

    def test_catalog_contains_only_existing_skill_paths(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            self.assertTrue((ROOT / entry["path"] / "SKILL.md").is_file())

    def test_every_catalog_entry_has_a_matching_registry_manifest(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            self.assertTrue((ROOT / entry["registry_path"]).is_file())

    def test_every_catalog_entry_has_a_standard_npx_install_command(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            metadata = json.loads((ROOT / entry["metadata_path"]).read_text(encoding="utf-8"))
            self.assertEqual(
                metadata["install"]["cli"],
                f"npx skills add sandbaseai/sandbase-skills --skill {entry['name']} --agent codex",
            )

    def test_every_installed_skill_documents_its_declared_tools(self):
        catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        for entry in catalog["skills"]:
            skill_dir = ROOT / entry["path"]
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            references_dir = skill_dir / "references"
            for reference in references_dir.rglob("*.md"):
                text += reference.read_text(encoding="utf-8")
            metadata = json.loads((ROOT / entry["metadata_path"]).read_text(encoding="utf-8"))
            for endpoint in metadata["api"]["endpoints"]:
                self.assertIn(endpoint["tool_name"], text)

    def test_video_generator_uses_dynamic_sandbase_media_tools(self):
        skill_dir = ROOT / "marketing" / "video-generator"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
            encoding="utf-8"
        )
        metadata = json.loads(
            (ROOT / "catalog" / "skills" / "video-generator.json").read_text(
                encoding="utf-8"
            )
        )
        tool_names = {endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]}

        self.assertEqual(metadata["api"]["schema_resolution"]["lookup"], "sandbase_inspect")
        self.assertEqual(metadata["api"]["call"]["tool"], "sandbase_run")
        self.assertEqual(
            tool_names,
            {
                "sandbase_discover",
                "sandbase_inspect",
                "sandbase_run",
                "sandbase_run_get",
                "sandbase_runs",
                "sandbase_account",
            },
        )
        self.assertIn("per-call price", skill_text)
        self.assertIn("Never submit a duplicate", skill_text)
        self.assertIn("continue only in **Plan only** mode", skill_text)
        self.assertIn("Do not silently substitute another generation provider", skill_text)
        for legacy_tool in ("`generate_image`", "`generate_image_variation`", "`generate_music`"):
            self.assertNotIn(legacy_tool, skill_text)
            self.assertNotIn(legacy_tool, api_map)

    def test_music_prompter_uses_live_sandbase_music_capabilities(self):
        skill_dir = ROOT / "marketing" / "music-prompter"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
            encoding="utf-8"
        )
        metadata = json.loads(
            (ROOT / "catalog" / "skills" / "music-prompter.json").read_text(
                encoding="utf-8"
            )
        )
        tool_names = {endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]}

        self.assertEqual(
            tool_names,
            {
                "sandbase_discover",
                "sandbase_inspect",
                "sandbase_run",
                "sandbase_run_get",
                "sandbase_runs",
                "sandbase_account",
            },
        )
        self.assertEqual(metadata["api"]["schema_resolution"]["lookup"], "sandbase_inspect")
        self.assertEqual(metadata["api"]["call"]["tool"], "sandbase_run")
        self.assertIn("Do not assume a universal maximum track length", skill_text)
        self.assertIn("Before the first paid call", skill_text)
        self.assertIn("Never create a replacement", skill_text)
        self.assertNotIn("184 seconds", skill_text + api_map)

    def test_listicle_writer_requires_evidence_and_discloses_rankings(self):
        skill_dir = ROOT / "marketing" / "listicle-blog-writer"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
            encoding="utf-8"
        )
        metadata = json.loads(
            (ROOT / "catalog" / "skills" / "listicle-blog-writer.json").read_text(
                encoding="utf-8"
            )
        )
        tool_names = {endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]}

        self.assertEqual(
            tool_names,
            {
                "sandbase_discover",
                "sandbase_inspect",
                "sandbase_run",
                "sandbase_run_get",
                "sandbase_runs",
                "sandbase_account",
            },
        )
        self.assertIn("is not automatically the winner", skill_text)
        self.assertIn("Before any paid research call", skill_text)
        self.assertIn("Official pages support", skill_text + api_map)
        self.assertNotIn("user's product is #1", skill_text.lower())

    def test_manim_animator_keeps_rendering_local_and_media_on_sandbase(self):
        skill_dir = ROOT / "marketing" / "manim-animator"
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
            encoding="utf-8"
        )
        metadata = json.loads(
            (ROOT / "catalog" / "skills" / "manim-animator.json").read_text(
                encoding="utf-8"
            )
        )
        tool_names = {endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]}

        self.assertEqual(
            tool_names,
            {
                "sandbase_discover",
                "sandbase_inspect",
                "sandbase_run",
                "sandbase_run_get",
                "sandbase_runs",
                "sandbase_account",
            },
        )
        self.assertIn("Manim rendering is local and deterministic", api_map)
        self.assertIn("Before any paid call", skill_text)
        self.assertIn("Manim Community or ManimGL and do not mix their APIs", skill_text)
        for legacy_tool in ("`generate_image`", "`generate_speech`", "`generate_music`"):
            self.assertNotIn(legacy_tool, skill_text + api_map)

    def test_new_data_skills_support_current_mcp_and_rest_transports(self):
        expected_tools = {
            "sandbase_discover",
            "sandbase_inspect",
            "sandbase_run",
            "sandbase_run_get",
            "sandbase_runs",
            "sandbase_account",
        }

        for skill_name in ("stock-analysis", "similarweb-analytics"):
            with self.subTest(skill=skill_name):
                skill_dir = ROOT / "marketing" / skill_name
                skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
                api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
                    encoding="utf-8"
                )
                metadata = json.loads(
                    (ROOT / "catalog" / "skills" / f"{skill_name}.json").read_text(
                        encoding="utf-8"
                    )
                )
                tool_names = {
                    endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]
                }

                self.assertEqual(tool_names, expected_tools)
                self.assertEqual(
                    metadata["api"]["schema_resolution"]["lookup"], "sandbase_inspect"
                )
                self.assertIn("SANDBASE_API_KEY", api_map)
                self.assertIn("GET https://api.sandbase.ai/v1/models", api_map)
                self.assertIn("POST https://api.sandbase.ai/v1/run", api_map)
                self.assertIn("do not wrap them in an `input` object", api_map)
                self.assertIn("duplicate", skill_text.lower())
                self.assertNotIn("/opt/.manus", skill_text + api_map)

    def test_latest_imports_preserve_local_work_and_dynamic_sandbase_calls(self):
        expected_tools = {
            "sandbase_discover",
            "sandbase_inspect",
            "sandbase_run",
            "sandbase_run_get",
            "sandbase_runs",
            "sandbase_account",
        }

        for skill_name in ("game-dev", "excel-generator", "internet-skill-finder"):
            with self.subTest(skill=skill_name):
                skill_dir = ROOT / "marketing" / skill_name
                skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
                api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
                    encoding="utf-8"
                )
                metadata = json.loads(
                    (ROOT / "catalog" / "skills" / f"{skill_name}.json").read_text(
                        encoding="utf-8"
                    )
                )
                tool_names = {
                    endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]
                }

                self.assertEqual(tool_names, expected_tools)
                self.assertEqual(
                    metadata["api"]["schema_resolution"]["lookup"], "sandbase_inspect"
                )
                self.assertIn("Before any paid call", skill_text)
                self.assertNotIn("manus.im", skill_text + api_map)
                self.assertNotIn("/home/ubuntu", skill_text + api_map)

        game_text = (ROOT / "marketing" / "game-dev" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        excel_text = (ROOT / "marketing" / "excel-generator" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        finder_text = (
            ROOT / "marketing" / "internet-skill-finder" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Keep the game code", game_text)
        self.assertIn("Workbook generation is local and deterministic", excel_text)
        self.assertIn("Recommendation does not authorize installation", finder_text)
        self.assertIn(
            "npx skills add <owner>/<repository> --skill <skill-id> --agent <agent>",
            finder_text,
        )

    def test_remaining_manus_bundle_has_a_complete_auditable_decision_record(self):
        manifest = json.loads(
            (ROOT / "imports" / "manus-skills-2026-09-02.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            manifest["summary"],
            {"unique_remaining": 161, "imported": 138, "skipped": 23},
        )

        imported = {item["name"]: item for item in manifest["imported"]}
        skipped = {item["name"]: item for item in manifest["skipped"]}
        self.assertEqual(len(imported), 138)
        self.assertEqual(len(skipped), 23)
        self.assertTrue(set(imported).isdisjoint(skipped))

        archive_records = [
            archive
            for item in (*manifest["imported"], *manifest["skipped"])
            for archive in item["source_archives"]
        ]
        self.assertEqual(len(archive_records), 162)
        for archive in archive_records:
            digest = archive["sha256"]
            self.assertEqual(len(digest), 64)
            self.assertTrue(all(character in "0123456789abcdef" for character in digest))

        self.assertEqual(len(imported["turborepo"]["source_archives"]), 2)

        expected_tools = {
            "sandbase_discover",
            "sandbase_inspect",
            "sandbase_run",
            "sandbase_run_get",
            "sandbase_runs",
            "sandbase_account",
        }
        forbidden_source_markers = (
            "/home/ubuntu",
            "/opt/.manus",
            "manus.im",
            "GITHUB_TOKEN",
            "GH_TOKEN",
        )

        for name in imported:
            skill_dir = ROOT / "marketing" / name
            skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            api_map = (skill_dir / "references" / "sandbase-api-map.md").read_text(
                encoding="utf-8"
            )
            metadata = json.loads(
                (ROOT / "catalog" / "skills" / f"{name}.json").read_text(
                    encoding="utf-8"
                )
            )
            registry = json.loads(
                (
                    ROOT
                    / "integrations"
                    / "sandbase-registry"
                    / "data"
                    / "skills"
                    / "sandbase"
                    / name
                    / "plugin.json"
                ).read_text(encoding="utf-8")
            )
            displayed = {
                endpoint["tool_name"] for endpoint in metadata["api"]["endpoints"]
            }

            self.assertEqual(displayed, expected_tools)
            self.assertEqual(
                set(registry["unified_schema"]["required_endpoints"]), expected_tools
            )
            self.assertIn("Before any paid call", skill_text)
            domain_checks = skill_text.split("## Quality gates", 1)[1].split(
                "## SandBase boundary", 1
            )[0]
            self.assertGreaterEqual(
                sum(line.startswith("- ") for line in domain_checks.splitlines()),
                4,
                f"{name} needs at least one capability-specific quality gate",
            )
            for marker in forbidden_source_markers:
                self.assertNotIn(marker, skill_text + api_map)

        for name in skipped:
            self.assertFalse((ROOT / "marketing" / name / "SKILL.md").exists())

    def test_multi_source_search_has_a_no_account_host_tool_path(self):
        skill_text = (ROOT / "research" / "multi-source-search" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        compatibility = next(
            line.removeprefix("compatibility: ")
            for line in skill_text.splitlines()
            if line.startswith("compatibility: ")
        )
        self.assertLessEqual(len(compatibility), 500)
        self.assertIn("Agent Skills-compatible host", compatibility)
        self.assertIn("network access", compatibility)
        self.assertIn("Python 3.9+", compatibility)
        self.assertIn("No SandBase account is required", compatibility)
        self.assertIn("Do not stop merely because SandBase is unavailable", skill_text)
        self.assertIn("host agent's native web search", skill_text)
        self.assertIn("sandbase_describe_tool", skill_text)
        self.assertIn("validate_report.py", skill_text)

    def test_multi_source_search_bounds_tool_loops(self):
        skill_text = (ROOT / "research" / "multi-source-search" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("at most six search calls", skill_text)
        self.assertIn("Never repeat the same query", skill_text)
        self.assertIn("budget is exhausted", skill_text)


if __name__ == "__main__":
    unittest.main()
