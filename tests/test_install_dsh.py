import tempfile
import unittest
from pathlib import Path

from scripts.install_dsh import available_skills, install_skill


class InstallDshTests(unittest.TestCase):
    def test_catalog_contains_public_skills(self):
        skills = available_skills()
        self.assertIn("exa-deep-search", skills)
        self.assertIn("reddit-customer-insights", skills)

    def test_installs_bundle_in_dsh_discovery_root(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = install_skill("exa-deep-search", Path(directory))
            self.assertEqual(
                destination,
                Path(directory).resolve() / ".dsh" / "skills" / "exa-deep-search",
            )
            self.assertTrue((destination / "SKILL.md").is_file())
            self.assertTrue((destination / "references" / "sandbase-api-map.md").is_file())

    def test_refuses_to_replace_without_force(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            install_skill("exa-deep-search", project)
            with self.assertRaises(FileExistsError):
                install_skill("exa-deep-search", project)

            destination = install_skill("exa-deep-search", project, force=True)
            self.assertTrue((destination / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
