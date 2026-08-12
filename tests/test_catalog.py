"""The game guidance catalog is complete, sourced, portable, and internally aligned."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ALLOWED = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_SKILLS = {
    "axmol-patterns",
    "building-isometric-worlds",
    "building-tile-based-worlds",
    "creating-2d-game-art",
    "cpp-patterns",
    "designing-game-cameras-and-controls",
    "designing-game-levels",
    "designing-games",
    "designing-player-experience",
    "engineering-2d-rendering",
    "planning-game-production",
    "playtesting-games",
    "programming-gameplay",
}
FORBIDDEN_FILES = {"README.md", "CHANGELOG.md", "rundesk.json"}


class GameCatalogContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

    def test_manifest_names_the_games_catalog(self):
        self.assertEqual(1, self.manifest["schema"])
        self.assertEqual("rundesk-skills-gamedev", self.manifest["name"])
        self.assertRegex(self.manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertTrue(self.manifest["description"].strip())
        self.assertFalse((ROOT / "catalog.json").exists())

    def test_manifest_declares_the_complete_portfolio_once(self):
        entries = self.manifest["skills"]
        names = [entry["name"] for entry in entries]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(EXPECTED_SKILLS, set(names))
        self.assertEqual(
            EXPECTED_SKILLS,
            {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()},
        )

    def test_readme_lists_exactly_the_manifest_skills(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"(?m)^- `([a-z0-9-]+)`", readme))
        declared = {entry["name"] for entry in self.manifest["skills"]}
        self.assertEqual(declared, listed)

    def test_every_package_is_named_sourced_and_guidance_only(self):
        for entry in self.manifest["skills"]:
            with self.subTest(skill=entry["name"]):
                name = entry["name"]
                self.assertRegex(name, ALLOWED)
                package = ROOT / entry["path"]
                self.assertEqual(name, package.name)
                page = (package / "SKILL.md").read_text(encoding="utf-8")
                sections = page.split("---", 2)
                self.assertEqual(3, len(sections), "SKILL.md needs YAML frontmatter")
                frontmatter = [
                    line for line in sections[1].strip().splitlines() if line.strip()
                ]
                self.assertEqual(["name", "description"], [
                    line.partition(":")[0] for line in frontmatter
                ])
                self.assertEqual(f"name: {name}", frontmatter[0])
                description = frontmatter[1].partition(":")[2].strip()
                self.assertTrue(description)
                self.assertLessEqual(len(description), 1024)
                self.assertNotIn(
                    ": ",
                    description,
                    "an unquoted colon followed by space is invalid YAML plain-scalar content",
                )
                self.assertNotIn(" #", description, "YAML would parse this as a comment")
                self.assertLess(len(page.splitlines()), 500)
                self.assertTrue((package / "references" / "sources.md").is_file())
                for forbidden in FORBIDDEN_FILES:
                    self.assertFalse((package / forbidden).exists())
                self.assertFalse((package / "scripts").exists())
                self.assertFalse((package / "agents").exists())

    def test_local_reference_links_resolve(self):
        link = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+\.md)(?:#[^)]+)?\)")
        for markdown in ROOT.glob("skills/**/*.md"):
            text = markdown.read_text(encoding="utf-8")
            for target in link.findall(text):
                with self.subTest(source=markdown.relative_to(ROOT), target=target):
                    self.assertTrue((markdown.parent / target).resolve().is_file())

    def test_public_files_contain_no_private_workspace_paths(self):
        forbidden = ("/Users/", "Development/Workspace", "Desktop Case Files", "UrbanState")
        for markdown in ROOT.glob("skills/**/*.md"):
            text = markdown.read_text(encoding="utf-8")
            for value in forbidden:
                with self.subTest(source=markdown.relative_to(ROOT), value=value):
                    self.assertNotIn(value, text)

    def test_release_workflow_ties_tags_to_manifest_version(self):
        guide = (ROOT / "RELEASING.md").read_text(encoding="utf-8")
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("manifest.json", guide)
        self.assertIn("tags:", workflow)
        self.assertIn("does not match manifest", workflow)
        self.assertIn("gh release create", workflow)


if __name__ == "__main__":
    unittest.main()
