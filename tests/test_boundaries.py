"""Synthetic boundary checks; never use supplied application source in CI."""
from copy import deepcopy
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools.nexus_baseline import read_json, snapshot
from tools.nexus_boundaries import draft, main, validate_plan


class BoundaryPlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "app.py").write_text("print('synthetic')\n", encoding="utf-8")
        (self.source / "README.md").write_text("Fabricated fixture\n", encoding="utf-8")
        self.baseline = snapshot({"sources": {"demo": self.source}, "artifacts": {}})
        self.plan = draft(self.baseline)

    def reject(self, plan=None, baseline=None):
        with self.assertRaises(ValueError):
            validate_plan(baseline or self.baseline, plan or self.plan)

    def test_draft_covers_every_file_without_authorizing_publication(self):
        result = validate_plan(self.baseline, self.plan)
        self.assertEqual(result["source_files"], 2)
        self.assertEqual(result["dispositions"], {"review_required": 2})
        self.assertFalse(result["publication_authorized"])
        self.assertEqual(result["review_required"], 2)

    def test_reviewed_proposal_has_consistent_public_and_private_targets(self):
        self.plan["targets"] = {
            "app": {"repository": "demo-app", "visibility": "public"},
            "adapter": {"repository": "demo-adapter", "visibility": "private"},
        }
        self.plan["entries"][0].update(disposition="public_candidate", targets=["app"])
        self.plan["entries"][1].update(disposition="split_required", targets=["app", "adapter"])
        result = validate_plan(self.baseline, self.plan)
        self.assertEqual(result["dispositions"], {"public_candidate": 1, "split_required": 1})
        self.assertFalse(result["publication_authorized"])

    def test_omitted_file_rejected(self):
        self.plan["entries"].pop()
        self.reject()

    def test_duplicate_file_rejected_even_with_matching_count(self):
        self.plan["entries"][1] = deepcopy(self.plan["entries"][0])
        self.reject()

    def test_unknown_source_and_file_rejected(self):
        for field in ("source", "path"):
            with self.subTest(field=field):
                plan = deepcopy(self.plan)
                plan["entries"][0][field] = "untracked"
                self.reject(plan)

    def test_stale_file_identity_rejected(self):
        for field, value in (("sha256", "0" * 64), ("bytes", 0), ("bytes", True)):
            with self.subTest(field=field, value=value):
                plan = deepcopy(self.plan)
                plan["entries"][0][field] = value
                self.reject(plan)

    def test_changed_snapshot_policy_cannot_reuse_plan(self):
        changed = deepcopy(self.baseline)
        changed["policy"]["excluded_directories"].append("new-exclusion")
        self.reject(baseline=changed)

    def test_incomplete_or_inconsistent_snapshot_rejected(self):
        changed = deepcopy(self.baseline)
        changed["complete"] = False
        self.reject(baseline=changed)
        changed = deepcopy(self.baseline)
        changed["sources"]["demo"]["files"]["app.py"]["sha256"] = "0" * 64
        self.reject(baseline=changed)

    def test_no_publication_or_review_approval_can_be_recorded(self):
        for field, value in (("visibility", "public"), ("publication_authorized", True)):
            plan = deepcopy(self.plan)
            plan[field] = value
            self.reject(plan)
        self.plan["entries"][0]["review_required"] = False
        self.reject()

    def test_visibility_rules_for_each_disposition(self):
        self.plan["targets"] = {
            "p": {"repository": "public-demo", "visibility": "public"},
            "i": {"repository": "internal-demo", "visibility": "private"},
        }
        invalid = [("public_candidate", []), ("public_candidate", ["i"]),
                   ("private_provider", ["p"]), ("split_required", ["p"]),
                   ("review_required", ["p"]), ("private_evidence", ["i"]),
                   ("generated_exclude", ["p"])]
        for disposition, targets in invalid:
            with self.subTest(disposition=disposition, targets=targets):
                plan = deepcopy(self.plan)
                plan["entries"][0].update(disposition=disposition, targets=targets)
                self.reject(plan)
        self.plan["entries"][0].update(disposition="private_provider", targets=["i"])
        validate_plan(self.baseline, self.plan)

    def test_missing_duplicate_and_unknown_targets_rejected(self):
        for targets in (["missing"], ["p", "p"]):
            plan = deepcopy(self.plan)
            plan["targets"] = {"p": {"repository": "demo", "visibility": "public"}}
            plan["entries"][0].update(disposition="public_candidate", targets=targets)
            self.reject(plan)

    def test_unsafe_paths_rejected(self):
        for path in ("../app.py", "/app.py", "a/../app.py", "./app.py", "a//app.py", "C:/app.py", "a\\app.py"):
            with self.subTest(path=path):
                plan = deepcopy(self.plan)
                plan["entries"][0]["path"] = path
                self.reject(plan)

    def test_invalid_schema_and_reasons_rejected(self):
        for field, value in (("disposition", "export"), ("reasons", []), ("reasons", [""]), ("signals", "scan")):
            plan = deepcopy(self.plan)
            plan["entries"][0][field] = value
            self.reject(plan)
        plan = deepcopy(self.plan)
        plan["approved"] = True
        self.reject(plan)
        plan = deepcopy(self.plan)
        plan["schema_version"] = True
        self.reject(plan)

    def test_empty_source_mapping_cannot_claim_coverage(self):
        artifact = self.root / "archive.txt"
        artifact.write_text("Synthetic archive stand-in", encoding="utf-8")
        baseline = snapshot({"sources": {}, "artifacts": {"archive": artifact}})
        with self.assertRaises(ValueError):
            draft(baseline)

    def test_cli_writes_once_and_protects_inputs(self):
        baseline = self.root / "baseline.private.json"
        baseline.write_text(json.dumps(self.baseline), encoding="utf-8")
        plan = self.root / "plan.private.json"
        report = self.root / "report.private.json"
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            args = ["draft", "--baseline", str(baseline), "--output", str(plan)]
            self.assertEqual(main(args), 0)
            original = plan.read_bytes()
            self.assertEqual(main(args), 2)
            self.assertEqual(plan.read_bytes(), original)
            self.assertEqual(main(["validate", "--baseline", str(baseline), "--plan", str(plan), "--output", str(report)]), 0)
            self.assertEqual(main(["draft", "--baseline", str(baseline), "--output", str(self.source / "report.json")]), 2)
        self.assertTrue(read_json(report)["structure_valid"])
        self.assertFalse((self.source / "report.json").exists())

    def test_cli_rejects_duplicate_json_keys_and_malformed_structure(self):
        baseline = self.root / "baseline.json"
        baseline.write_text(json.dumps(self.baseline), encoding="utf-8")
        plan = self.root / "invalid.json"
        output = self.root / "absent.json"
        for value in ('{"entries": [], "entries": []}', '{"unexpected": null}'):
            plan.write_text(value, encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(["validate", "--baseline", str(baseline), "--plan", str(plan), "--output", str(output)]), 2)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
