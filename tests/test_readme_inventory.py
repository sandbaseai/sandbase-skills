import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReadmeInventoryTests(unittest.TestCase):
    def test_readme_catalog_matches_installable_skill_directories(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"^\| `([^`]+)` \|", readme, re.MULTILINE))
        installable = {
            path.parent.name
            for path in ROOT.rglob("SKILL.md")
            if "node_modules" not in path.parts and ".git" not in path.parts
        }

        self.assertEqual(listed, installable)

        heading = re.search(r"^## Skill Catalog \((\d+) Skills\)$", readme, re.MULTILINE)
        self.assertIsNotNone(heading)
        self.assertEqual(int(heading.group(1)), len(installable))

        category_total = sum(
            int(count)
            for count in re.findall(r"^### .+ \((\d+) Skills\)$", readme, re.MULTILINE)
        )
        self.assertEqual(category_total, len(installable))


if __name__ == "__main__":
    unittest.main()
