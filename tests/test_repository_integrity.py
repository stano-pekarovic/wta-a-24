from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

# Curated sample files that must stay present and healthy. The repo also holds
# free-form workshop artifacts (some intentionally with unresolved merge
# conflicts); those are out of scope so the smoke suite stays green.
SAMPLE_FILES = [
    "about-me.md",
    "notes.md",
    "dano.txt",
    "eli.txt",
    "erik.txt",
    "stano-p.txt",
    "monika-drajnova.txt",
    "test-data/current/bratislava.json",
    "test-data/current/kosice.json",
    "test-data/current/poprad.json",
    "test-data/test-data-A-1.txt",
    "test-data/test-data-A-2.txt",
    "test-data/README.md",
]


class RepositoryIntegrityTests(unittest.TestCase):
    def test_readme_has_project_heading_and_description(self):
        readme = ROOT / "README.md"

        self.assertTrue(readme.is_file(), "README.md should exist")
        content = readme.read_text(encoding="utf-8").strip()
        lines = content.splitlines()

        self.assertTrue(lines, "README.md should not be empty")
        self.assertRegex(lines[0], r"^#\s+\S+", "README.md should start with an H1 heading")
        self.assertIn("git workshop", content.lower())

    def test_sample_files_are_present_and_non_empty(self):
        for file_name in SAMPLE_FILES:
            with self.subTest(file=file_name):
                path = ROOT / file_name
                content = path.read_text(encoding="utf-8").strip() if path.exists() else ""

                self.assertTrue(path.is_file(), f"{file_name} should exist")
                self.assertGreater(len(content), 0, f"{file_name} should not be empty")

    def test_sample_files_do_not_contain_merge_conflict_markers(self):
        conflict_markers = ("<<<<<<<", "=======", ">>>>>>>")

        for file_name in SAMPLE_FILES:
            with self.subTest(file=file_name):
                path = ROOT / file_name
                content = path.read_text(encoding="utf-8")

                for marker in conflict_markers:
                    self.assertNotIn(marker, content, f"{file_name} contains merge conflict marker {marker}")


if __name__ == "__main__":
    unittest.main()
