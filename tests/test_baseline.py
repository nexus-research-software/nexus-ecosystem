"""Synthetic regression coverage for source identity and evidence handling."""

import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools import nexus_baseline as baseline


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "example"
        self.source.mkdir()
        (self.source / "module.py").write_text("raise RuntimeError('never import me')\n", encoding="utf-8")
        self.config = {"sources": {"example": self.source}, "artifacts": {}}

    def test_inventory_does_not_execute_source(self):
        snapshot = baseline.snapshot(self.config)
        entry = snapshot["sources"]["example"]["files"]["module.py"]
        self.assertEqual(entry["sha256"], hashlib.sha256((self.source / "module.py").read_bytes()).hexdigest())
        self.assertTrue(snapshot["complete"])

    def test_content_change_detected_even_with_same_size_and_mtime(self):
        item = self.source / "module.py"
        before = baseline.snapshot(self.config)
        previous = item.stat()
        item.write_bytes(item.read_bytes().replace(b"never", b"NEVER"))
        os.utime(item, ns=(previous.st_atime_ns, previous.st_mtime_ns))
        diff = baseline.compare(before, baseline.snapshot(self.config))
        self.assertFalse(diff["equal"])
        self.assertEqual(diff["changes"][0]["status"], "changed")

    def test_added_removed_files_and_sources_are_visible(self):
        before = baseline.snapshot(self.config)
        (self.source / "module.py").unlink()
        (self.source / "replacement.txt").write_text("synthetic", encoding="utf-8")
        after = baseline.snapshot(self.config)
        self.assertEqual({item["status"] for item in baseline.compare(before, after)["changes"]}, {"added", "removed"})
        after["sources"]["additional"] = copy.deepcopy(after["sources"]["example"])
        self.assertTrue(any(item.get("label") == "additional" and item["status"] == "added" for item in baseline.compare(before, after)["changes"]))

    def test_relocated_identical_source_is_equal(self):
        before = baseline.snapshot(self.config)
        after = copy.deepcopy(before)
        after["sources"]["example"]["root"] = "/another/location"
        after["created_utc"] = "a different time"
        self.assertTrue(baseline.compare(before, after)["equal"])

    def test_caches_are_excluded_but_wheels_and_documents_are_hashed(self):
        cache = self.source / "__pycache__"
        cache.mkdir()
        (cache / "cached.pyc").write_bytes(b"cache")
        (self.source / "fixture.docx").write_bytes(b"synthetic placeholder, not a real document")
        (self.source / "package.whl").write_bytes(b"synthetic wheel placeholder")
        result = baseline.tree_identity(self.source)
        self.assertEqual(set(result["files"]), {"module.py", "fixture.docx", "package.whl"})

    def test_archive_identity_changes(self):
        archive = self.root / "example.zip"
        archive.write_bytes(b"first")
        self.config["artifacts"]["example-archive"] = archive
        before = baseline.snapshot(self.config)
        archive.write_bytes(b"other")
        diff = baseline.compare(before, baseline.snapshot(self.config))
        self.assertEqual(diff["changes"], [{"group": "artifacts", "label": "example-archive", "status": "changed"}])

    def test_symlink_is_not_followed_or_reported_as_complete(self):
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "unrelated.txt").write_text("private synthetic sentinel", encoding="utf-8")
        try:
            (self.source / "link").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Host does not allow unprivileged symbolic links")
        result = baseline.snapshot(self.config)
        self.assertFalse(result["complete"])
        self.assertEqual(result["sources"]["example"]["omitted"], [{"path": "link", "reason": "symbolic_link"}])
        self.assertNotIn("link/unrelated.txt", result["sources"]["example"]["files"])
        with self.assertRaises(ValueError):
            baseline.compare(result, result)

    def test_missing_and_empty_sources_fail(self):
        with self.assertRaises(ValueError):
            baseline.tree_identity(self.root / "missing")
        empty = self.root / "empty"
        empty.mkdir()
        with self.assertRaises(ValueError):
            baseline.tree_identity(empty)

    def test_modified_manifest_and_different_policy_cannot_pass(self):
        first = baseline.snapshot(self.config)
        second = copy.deepcopy(first)
        second["sources"]["example"]["files"]["module.py"]["sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            baseline.compare(first, second)
        second = copy.deepcopy(first)
        second["policy"]["excluded_directories"].append("src")
        with self.assertRaises(ValueError):
            baseline.compare(first, second)

    def test_no_output_inside_source_or_over_existing_file(self):
        with self.assertRaises(ValueError):
            baseline.write_report(self.source / "result.json", {}, [self.source])
        output = self.root / "result.json"
        baseline.write_report(output, {"example": 1}, [self.source])
        with self.assertRaises(FileExistsError):
            baseline.write_report(output, {"example": 2}, [self.source])
        self.assertEqual(json.loads(output.read_text()), {"example": 1})

    def test_relative_config_and_both_package_metadata_formats(self):
        config_path = self.root / "config.json"
        config_path.write_text(json.dumps({"schema_version": 1, "sources": {"example": "example"}}))
        config = baseline.load_config(config_path)
        for table in ("project", "tool.poetry"):
            (self.source / "pyproject.toml").write_text(f'[{table}]\nname="synthetic-package"\nversion="0.1.0"\n')
            self.assertEqual(baseline.snapshot(config)["sources"]["example"]["package"], {"name": "synthetic-package", "version": "0.1.0"})

    def test_duplicate_keys_and_unknown_config_fail(self):
        config = self.root / "bad.json"
        config.write_text('{"sources": {}, "sources": {}}')
        with self.assertRaises(ValueError):
            baseline.read_json(config)
        config.write_text('{"schema_version": 1, "source": {}}')
        with self.assertRaises(ValueError):
            baseline.load_config(config)

    def summary(self, body, exit_code=0):
        report = self.root / "report.xml"
        report.write_text(body, encoding="utf-8")
        return baseline.junit_summary(report, exit_code)

    def test_nested_junit_counts_and_no_test_text_export(self):
        report = self.summary('<testsuites><testsuite tests="4" errors="1" failures="1" skipped="1"><testcase name="a"/><testcase name="b"><failure>private synthetic message</failure></testcase><testcase name="c"><skipped/></testcase><testcase name="d"><error/></testcase></testsuite></testsuites>', 1)
        self.assertEqual([report[key] for key in ("testcases", "passed", "failures", "skipped", "errors")], [4, 1, 1, 1, 1])
        self.assertFalse(report["successful"])
        self.assertNotIn("private synthetic message", json.dumps(report))

    def test_failed_process_cannot_pass_from_green_xml(self):
        result = self.summary('<testsuite><testcase/></testsuite>', 2)
        self.assertEqual(result["passed"], 1)
        self.assertFalse(result["successful"])

    def test_empty_or_entirely_skipped_reports_are_not_success(self):
        for xml in ('<testsuite/>', '<testsuite><testcase><skipped/></testcase></testsuite>'):
            self.assertFalse(self.summary(xml)["successful"])

    def test_collection_errors_outside_testcases_fail(self):
        self.assertFalse(self.summary('<testsuite errors="1"><testcase/></testsuite>')["successful"])

    def test_declared_failures_cannot_become_green(self):
        self.assertFalse(self.summary('<testsuite failures="1"><testcase/></testsuite>')["successful"])
        self.assertFalse(self.summary('<testsuites errors="1"><testsuite><testcase/></testsuite></testsuites>')["successful"])

    def test_comparison_cannot_write_into_recorded_source(self):
        before = self.root / "before.json"
        before.write_text(json.dumps(baseline.snapshot(self.config)))
        code = baseline.main(["compare", str(before), str(before), "--output", str(self.source / "comparison.json")])
        self.assertEqual(code, 2)
        self.assertFalse((self.source / "comparison.json").exists())

    def test_malformed_and_entity_xml_are_rejected(self):
        for xml in ('<testsuite>', '<!DOCTYPE x [<!ENTITY a "b">]><testsuite/>', '<other/>'):
            with self.assertRaises((ValueError, baseline.ET.ParseError)):
                self.summary(xml)

    def test_cli_snapshot_compare_and_failed_junit_exit_codes(self):
        config = self.root / "inputs.json"
        config.write_text(json.dumps({"schema_version": 1, "sources": {"example": "example"}}))
        script = Path(baseline.__file__)
        output = self.root / "before.json"
        run = subprocess.run([sys.executable, str(script), "snapshot", "--config", str(config), "--output", str(output)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        compare = subprocess.run([sys.executable, str(script), "compare", str(output), str(output), "--output", str(self.root / "equal.json")], capture_output=True, text=True)
        self.assertEqual(compare.returncode, 0, compare.stderr)
        self.summary('<testsuite><testcase><failure/></testcase></testsuite>', 1)
        summary = subprocess.run([sys.executable, str(script), "junit", str(self.root / "report.xml"), "--exit-code", "1", "--output", str(self.root / "failed.json")], capture_output=True, text=True)
        self.assertEqual(summary.returncode, 1, summary.stderr)
        self.assertFalse(json.loads((self.root / "failed.json").read_text())["successful"])


if __name__ == "__main__":
    unittest.main()
