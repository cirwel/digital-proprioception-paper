#!/usr/bin/env python3
"""Offline negative controls for publication routing and metadata consistency."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from check_metadata import check

ROOT = Path(__file__).resolve().parent.parent


class PublicationGuards(unittest.TestCase):
    def setUp(self) -> None:
        (ROOT / ".scratch").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / ".scratch", prefix="publication-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.calls = self.root / "calls.jsonl"
        self.response = self.root / "response.json"
        self.response.write_text(json.dumps({
            "id": 23110718, "conceptrecid": "21930092", "metadata": {"version": "v2.0"},
        }))
        (self.root / ".zenodo.json").write_text('{"version":"v2.0.1"}')
        (self.root / "paper.pdf").write_text("fixture PDF")
        curl = self.bin / "curl"
        curl.write_text('''#!/usr/bin/env python3
import json, os, pathlib, sys
args = sys.argv[1:]
method = args[args.index("-X") + 1] if "-X" in args else "GET"
url = next((arg for arg in args if arg.startswith("https://")), "")
with open(os.environ["PUBLICATION_TEST_CALLS"], "a") as out:
    out.write(json.dumps({"method": method, "url": url}) + "\\n")
# This stub never performs network I/O and refuses every mutation.
if method != "GET" or not url.endswith("/versions/latest"):
    sys.exit(97)
pathlib.Path(args[args.index("-o") + 1]).write_bytes(
    pathlib.Path(os.environ["PUBLICATION_TEST_RESPONSE"]).read_bytes())
print("200", end="")
''')
        curl.chmod(0o755)

    def run_publisher(self, overrides: dict | None = None, tag: str = "paper-v2.0.1"):
        env = {k: v for k, v in os.environ.items() if not k.startswith("ZENODO_")}
        env.update(
            PATH=str(self.bin) + os.pathsep + os.environ["PATH"],
            ZENODO_TOKEN="offline-fixture-token", ZENODO_API_BASE="https://offline.invalid",
            PUBLICATION_TEST_CALLS=str(self.calls), PUBLICATION_TEST_RESPONSE=str(self.response),
            DRY_RUN="0",
        )
        env.update(overrides or {})
        self.calls.unlink(missing_ok=True)
        result = subprocess.run(
            ["bash", str(ROOT / "scripts/publish-to-zenodo.sh"), tag, "paper.pdf"],
            cwd=self.root, env=env, text=True, capture_output=True, timeout=10,
        )
        calls = [json.loads(line) for line in self.calls.read_text().splitlines()] if self.calls.exists() else []
        return result, calls

    def test_default_and_matching_overrides_use_this_concept(self) -> None:
        for overrides in ({}, {"ZENODO_CONCEPT_RECID": "21930092", "ZENODO_VERSION": "v2.0.1"}):
            with self.subTest(overrides=overrides):
                result, calls = self.run_publisher({**overrides, "DRY_RUN": "1"})
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(calls, [{"method": "GET", "url": "https://offline.invalid/api/records/21930092/versions/latest"}])
                self.assertIn("[dry-run] would POST", result.stdout)

    def test_foreign_or_empty_concept_is_rejected_without_network(self) -> None:
        for concept in ("19647159", "", "21930092/../19647159"):
            with self.subTest(concept=concept):
                result, calls = self.run_publisher({"ZENODO_CONCEPT_RECID": concept})
                self.assertEqual(result.returncode, 64)
                self.assertIn("must be 21930092", result.stderr)
                self.assertEqual(calls, [])

    def test_version_override_and_tag_conflicts_are_rejected_without_network(self) -> None:
        for override in ("paper-v2.0.1", "v2.0.2", ""):
            with self.subTest(override=override):
                result, calls = self.run_publisher({"ZENODO_VERSION": override})
                self.assertEqual(result.returncode, 64)
                self.assertIn("ZENODO_VERSION must match", result.stderr)
                self.assertEqual(calls, [])
        for tag in ("paper-v2.0.2", "v2.0.1"):
            with self.subTest(tag=tag):
                result, calls = self.run_publisher(tag=tag)
                self.assertEqual(result.returncode, 64)
                self.assertIn("tag must be paper-v2.0.1", result.stderr)
                self.assertEqual(calls, [])

    def test_bad_metadata_version_is_rejected_without_network(self) -> None:
        for version in (None, "paper-v2.0.1", "v2.0.1-draft", ""):
            with self.subTest(version=version):
                (self.root / ".zenodo.json").write_text(json.dumps({"version": version}))
                result, calls = self.run_publisher()
                self.assertEqual(result.returncode, 64)
                self.assertEqual(calls, [])

    def test_wrong_concept_response_stops_before_mutation(self) -> None:
        self.response.write_text('{"id":123,"conceptrecid":"19647159","metadata":{"version":"v2.0"}}')
        result, calls = self.run_publisher()
        self.assertEqual(result.returncode, 70)
        self.assertIn("no draft created", result.stderr)
        self.assertEqual([call["method"] for call in calls], ["GET"])

    def test_existing_metadata_version_stops_before_mutation(self) -> None:
        self.response.write_text('{"id":23337714,"conceptrecid":"21930092","metadata":{"version":"v2.0.1"}}')
        result, calls = self.run_publisher()
        self.assertEqual(result.returncode, 65)
        self.assertIn("version v2.0.1 already published", result.stderr)
        self.assertEqual([call["method"] for call in calls], ["GET"])


class MetadataGuards(unittest.TestCase):
    def setUp(self) -> None:
        (ROOT / ".scratch").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / ".scratch", prefix="metadata-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.restore()

    def restore(self) -> None:
        for name in ("paper.md", "CITATION.cff", ".zenodo.json"):
            shutil.copyfile(ROOT / name, self.root / name)

    def test_current_metadata_and_presentation_only_changes_match(self) -> None:
        check(self.root)
        cff = self.root / "CITATION.cff"
        cff.write_text(cff.read_text().replace('  A running multi-agent system', '  A running\n  multi-agent system'))
        zenodo = self.root / ".zenodo.json"
        value = json.loads(zenodo.read_text())
        value["description"] = value["description"].replace('"coherence"', '&quot;coherence&quot;')
        zenodo.write_text(json.dumps(value))
        check(self.root)

    def test_drift_in_each_field_and_each_source_is_rejected(self) -> None:
        current_date = json.loads((ROOT / ".zenodo.json").read_text())["publication_date"]
        changed_date = "2000-01-01" if current_date != "2000-01-01" else "2000-01-02"
        replacements = {
            "paper.md": {"title": ("# ", "# DRIFT "), "version": ("**Version:** ", "**Version:** DRIFT"),
                         "date": (current_date, changed_date), "abstract": ("## Abstract\n\n", "## Abstract\n\nDRIFT ")},
            "CITATION.cff": {"title": ('title: "', 'title: "DRIFT '), "version": ('version: "', 'version: "DRIFT'),
                            "date": (current_date, changed_date), "abstract": ("abstract: >\n", "abstract: >\n  DRIFT\n")},
        }
        for source in ("paper.md", "CITATION.cff", ".zenodo.json"):
            for field in ("title", "version", "date", "abstract"):
                with self.subTest(source=source, field=field):
                    self.restore()
                    path = self.root / source
                    if source == ".zenodo.json":
                        value = json.loads(path.read_text())
                        key = {"date": "publication_date", "abstract": "description"}.get(field, field)
                        value[key] = "DRIFT " + value[key]
                        path.write_text(json.dumps(value))
                    else:
                        old, new = replacements[source][field]
                        path.write_text(path.read_text().replace(old, new, 1))
                    with self.assertRaises(ValueError):
                        check(self.root)

    def test_missing_or_unsupported_cff_fields_do_not_skip_validation(self) -> None:
        for old, new in (('title: ', 'unused-title: '), ('abstract: >', 'abstract: |')):
            with self.subTest(field=old):
                self.restore()
                cff = self.root / "CITATION.cff"
                cff.write_text(cff.read_text().replace(old, new, 1))
                with self.assertRaises(ValueError):
                    check(self.root)


if __name__ == "__main__":
    unittest.main()
