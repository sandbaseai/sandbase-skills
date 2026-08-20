import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReadmeInventoryTests(unittest.TestCase):
    LOCALIZED_READMES = (
        "README.zh-CN.md",
        "README.ja.md",
        "README.ko.md",
        "README.es.md",
        "README.fr.md",
        "README.de.md",
        "README.pt-BR.md",
    )

    @staticmethod
    def installable_skills() -> set[str]:
        return {
            path.parent.name
            for path in ROOT.rglob("SKILL.md")
            if "node_modules" not in path.parts and ".git" not in path.parts
        }

    def test_readme_catalog_matches_installable_skill_directories(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"^\| `([^`]+)` \|", readme, re.MULTILINE))
        installable = self.installable_skills()

        self.assertEqual(listed, installable)

        heading = re.search(r"^## Skill Catalog \((\d+) Skills\)$", readme, re.MULTILINE)
        self.assertIsNotNone(heading)
        self.assertEqual(int(heading.group(1)), len(installable))

        category_total = sum(
            int(count)
            for count in re.findall(r"^### .+ \((\d+) Skills\)$", readme, re.MULTILINE)
        )
        self.assertEqual(category_total, len(installable))

    def test_skills_sh_groupings_cover_each_installable_skill_once(self) -> None:
        config = json.loads((ROOT / "skills.sh.json").read_text(encoding="utf-8"))
        grouped = [skill for group in config["groupings"] for skill in group["skills"]]

        self.assertEqual(
            config["$schema"], "https://skills.sh/schemas/skills.sh.schema.json"
        )
        self.assertEqual(len(grouped), len(set(grouped)), "skills.sh groups contain duplicates")
        self.assertEqual(set(grouped), self.installable_skills())

    def test_every_readme_has_the_no_install_multi_source_command(self) -> None:
        command = "npx skills use sandbaseai/sandbase-skills@multi-source-search"
        for name in ("README.md", *self.LOCALIZED_READMES):
            with self.subTest(readme=name):
                content = (ROOT / name).read_text(encoding="utf-8")
                self.assertIn(command, content)

    def test_every_readme_documents_deepseek_harness_installation(self) -> None:
        command = "npx --yes github:sandbaseai/sandbase-skills add multi-source-search"
        destination = ".dsh/skills/multi-source-search"
        for name in ("README.md", *self.LOCALIZED_READMES):
            with self.subTest(readme=name):
                content = (ROOT / name).read_text(encoding="utf-8")
                self.assertIn(command, content)
                self.assertIn(destination, content)

    def test_skills_sh_badge_shows_install_count_and_links_to_repository(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "[![skills.sh installs](https://skills.sh/b/sandbaseai/sandbase-skills)]"
            "(https://skills.sh/sandbaseai/sandbase-skills)",
            readme,
        )
        self.assertIn(
            "](https://skills.sh/sandbaseai/sandbase-skills/multi-source-search)",
            readme,
        )

    def test_every_localized_readme_shows_star_and_install_signals(self) -> None:
        stars = "https://img.shields.io/github/stars/sandbaseai/sandbase-skills?style=social"
        installs = "https://skills.sh/b/sandbaseai/sandbase-skills"
        for name in self.LOCALIZED_READMES:
            with self.subTest(readme=name):
                content = (ROOT / name).read_text(encoding="utf-8")
                self.assertIn(stars, content)
                self.assertIn(installs, content)


if __name__ == "__main__":
    unittest.main()
