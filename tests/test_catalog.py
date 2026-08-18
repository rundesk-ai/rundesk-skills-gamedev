"""The game guidance catalog is complete, sourced, portable, and internally aligned."""

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ALLOWED = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_GUIDE_URL = "https://github.com/rundesk-ai/rundesk-cli/blob/main/docs/catalogs.md"
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
    "designing-systemic-management-games",
    "engineering-2d-rendering",
    "engineering-game-animation",
    "engineering-world-simulations",
    "generating-game-worlds",
    "planning-game-production",
    "playtesting-games",
    "programming-gameplay",
}
FORBIDDEN_FILES = {"README.md", "CHANGELOG.md", "rundesk.json"}
ALLOWED_PACKAGE_ROOTS = {"SKILL.md", "LICENSE.txt", "references", "assets"}
AGENT_HEADINGS = (
    "# AGENTS",
    "## Purpose",
    "## Before you work",
    "## Repository layout",
    "## Package and artifact contract",
    "## Safety and approval gates",
    "## Delegation",
    "## Architecture and conventions",
    "## Documentation duties",
    "## Build, test, and run",
    "## Pull requests and releases",
    "## Definition of done",
)
PR_HEADINGS = (
    "## Summary",
    "## Scope and compatibility",
    "## Critical risk",
    "## Validation",
    "## Repository gates",
    "## Release",
    "## Manual user path",
)
PR_CHECKLIST_ANCHORS = (
    "- Packages changed:",
    "- [ ] `python3 -m unittest discover -s tests -v`",
    "- [ ] A substantial new or changed skill was forward-tested against a realistic raw game task, or no forward-test was required.",
    "- [ ] Required GitHub checks pass for the exact head commit.",
    "- [ ] The diff contains no secret, customer identifier, private-project language, owner-specific path, private evidence, or unrelated artifact.",
    "- [ ] `README.md`, `manifest.json`, `tests/test_catalog.py`, and `skills/` agree.",
)
README_HEADINGS = (
    "## Skills",
    "## Install",
    "## Requirements",
    "## Repository layout",
    "## Development",
    "## Creating a skill catalog",
    "## Contributing",
    "## Releases",
    "## License",
)
ISSUE_HEADINGS = {
    "bug-report.md": (
        "## Problem",
        "## Reproduction",
        "## Expected behavior",
        "## Evidence",
        "## Environment",
        "## Scope and privacy",
    ),
    "change-proposal.md": (
        "## Problem",
        "## Desired outcome",
        "## Users and value",
        "## Scope and compatibility",
        "## Alternatives",
        "## Validation",
    ),
}
ISSUE_DIGESTS = {
    "bug-report.md": "747da5c0682a73adc61c35407327fb174c648630e80278c275af4a4542da6caf",
    "change-proposal.md": "2fe6a1d651ce91af2c3d19e98eea150ca26f41ad9a1ed95a6466a692b73eb4d7",
}


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
        self.assertEqual(
            README_HEADINGS,
            tuple(re.findall(r"^## .+$", readme, re.MULTILINE)),
        )
        for required in (
            CATALOG_GUIDE_URL,
            ".github/ISSUE_TEMPLATE/bug-report.md",
            ".github/ISSUE_TEMPLATE/change-proposal.md",
            ".github/pull_request_template.md",
            "rundesk skills install https://github.com/rundesk-ai/rundesk-skills-gamedev --confirm",
            "rundesk skills grant ava rundesk-skills-gamedev/designing-games",
        ):
            with self.subTest(readme_contract=required):
                self.assertIn(required, readme)
        self.assertNotIn("<agent>", readme)

    def test_every_package_is_named_sourced_and_guidance_only(self):
        for entry in self.manifest["skills"]:
            with self.subTest(skill=entry["name"]):
                name = entry["name"]
                self.assertRegex(name, ALLOWED)
                package = ROOT / entry["path"]
                self.assertEqual(name, package.name)
                self.assertEqual(Path("skills") / name, Path(entry["path"]))
                self.assertLessEqual(
                    {path.name for path in package.iterdir()},
                    ALLOWED_PACKAGE_ROOTS,
                )
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
                for artifact in package.rglob("*"):
                    if artifact.is_file():
                        self.assertEqual(
                            0,
                            artifact.stat().st_mode & 0o111,
                            f"{artifact.relative_to(ROOT)} must not be executable",
                        )

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

    def test_repository_guides_and_templates_follow_the_shared_contract(self):
        agents = (ROOT / "AGENTS.md").read_bytes()
        self.assertEqual(agents, (ROOT / "CLAUDE.md").read_bytes())
        self.assertIn(
            CATALOG_GUIDE_URL.encode(),
            agents,
        )
        self.assertEqual(
            AGENT_HEADINGS,
            tuple(re.findall(r"^#{1,2} .+$", agents.decode("utf-8"), re.MULTILINE)),
        )

        pull_request = ROOT / ".github" / "pull_request_template.md"
        self.assertTrue(pull_request.is_file())
        pull_request_text = pull_request.read_text(encoding="utf-8")
        self.assertEqual(
            PR_HEADINGS,
            tuple(re.findall(r"^## .+$", pull_request_text, re.MULTILINE)),
        )
        for anchor in PR_CHECKLIST_ANCHORS:
            with self.subTest(pull_request_anchor=anchor):
                self.assertIn(anchor, pull_request_text)

        issue_root = ROOT / ".github" / "ISSUE_TEMPLATE"
        self.assertEqual(
            {"bug-report.md", "change-proposal.md", "config.yml"},
            {path.name for path in issue_root.iterdir() if path.is_file()},
        )
        self.assertEqual(
            b"blank_issues_enabled: false\n",
            (issue_root / "config.yml").read_bytes(),
        )
        for filename, expected in ISSUE_HEADINGS.items():
            with self.subTest(issue_template=filename):
                issue = issue_root / filename
                self.assertTrue(issue.is_file())
                issue_bytes = issue.read_bytes()
                self.assertEqual(
                    ISSUE_DIGESTS[filename],
                    hashlib.sha256(issue_bytes).hexdigest(),
                )
                self.assertEqual(
                    expected,
                    tuple(re.findall(r"^## .+$", issue_bytes.decode("utf-8"), re.MULTILINE)),
                )

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
