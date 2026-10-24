"""Draft and validate PRIVATE repository boundary plans against frozen inputs.

This is a coverage checker, not a content scanner, exporter, or publication gate.
It never imports application code and cannot authorize publication.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Any

try:
    from .nexus_baseline import read_json, validate_snapshot, write_report
except ImportError:  # Direct execution from tools/.
    from nexus_baseline import read_json, validate_snapshot, write_report

DISPOSITIONS = frozenset({
    "public_candidate", "private_provider", "split_required",
    "private_evidence", "generated_exclude", "review_required",
})
HELD = frozenset({"private_evidence", "generated_exclude", "review_required"})
NAME = re.compile(r"[a-z0-9][a-z0-9_.-]*\Z")


def snapshot_digest(snapshot: dict[str, Any]) -> str:
    """Bind the plan to the complete snapshot, including its exclusion policy."""
    payload = json.dumps(snapshot, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _path(value: Any) -> None:
    if (not isinstance(value, str) or not value or "\\" in value or ":" in value
            or any(ord(char) < 32 for char in value)
            or PurePosixPath(value).is_absolute()
            or any(part in {"", ".", ".."} for part in value.split("/"))):
        raise ValueError("Expected a normalized relative file path")


def _strings(value: Any, *, nonempty: bool = False) -> bool:
    return (isinstance(value, list) and (bool(value) or not nonempty)
            and all(isinstance(item, str) and item.strip() for item in value))


def draft(snapshot: dict[str, Any]) -> dict[str, Any]:
    """Create an unreviewed entry for every included source file; classify none."""
    validate_snapshot(snapshot)
    entries = []
    for source, tree in sorted(snapshot["sources"].items()):
        for path, identity in sorted(tree["files"].items()):
            entries.append({
                "source": source, "path": path, **identity,
                "disposition": "review_required", "targets": [],
                "reasons": ["Review content, ownership, provenance, and licensing before assigning a destination."],
                "review_required": True,
            })
    plan = {
        "schema_version": 1, "kind": "boundary_plan", "visibility": "private",
        "snapshot_sha256": snapshot_digest(snapshot),
        "publication_authorized": False, "targets": {}, "entries": entries,
        "notes": ["Original archives are preserved privately; this plan covers included source files only."],
    }
    validate_plan(snapshot, plan)
    return plan


def validate_plan(snapshot: dict[str, Any], plan: dict[str, Any]) -> dict[str, Any]:
    """Require exact identity/coverage and consistent proposed destinations."""
    validate_snapshot(snapshot)
    fields = {"schema_version", "kind", "visibility", "snapshot_sha256",
              "publication_authorized", "targets", "entries", "notes"}
    if not isinstance(plan, dict) or set(plan) != fields:
        raise ValueError("Unsupported boundary plan fields")
    if type(plan["schema_version"]) is not int or plan["schema_version"] != 1 or plan["kind"] != "boundary_plan":
        raise ValueError("Unsupported boundary plan schema")
    if plan["visibility"] != "private" or plan["publication_authorized"] is not False:
        raise ValueError("Boundary plans must remain private and cannot authorize publication")
    if plan["snapshot_sha256"] != snapshot_digest(snapshot):
        raise ValueError("Plan is bound to a different snapshot")
    if not _strings(plan["notes"]):
        raise ValueError("Plan notes must be a list of nonempty strings")
    targets = plan["targets"]
    if not isinstance(targets, dict):
        raise ValueError("Targets must be an object")
    for label, target in targets.items():
        if (not isinstance(label, str) or not NAME.fullmatch(label)
                or not isinstance(target, dict) or set(target) != {"repository", "visibility"}
                or not isinstance(target["repository"], str) or not NAME.fullmatch(target["repository"])
                or target["visibility"] not in ("public", "private")):
            raise ValueError("Invalid logical repository target")
    expected = {}
    for source, tree in snapshot["sources"].items():
        if not isinstance(source, str) or not source.strip():
            raise ValueError("Invalid source label")
        for path, identity in tree["files"].items():
            _path(path)
            expected[(source, path)] = identity
    if not expected:
        raise ValueError("A boundary plan requires at least one source file")
    if not isinstance(plan["entries"], list):
        raise ValueError("Entries must be a list")
    seen = set()
    counts: Counter[str] = Counter()
    per_source: dict[str, Counter[str]] = {}
    required = {"source", "path", "sha256", "bytes", "disposition", "targets", "reasons", "review_required"}
    for entry in plan["entries"]:
        if not isinstance(entry, dict) or not required <= set(entry) or set(entry) - required - {"signals"}:
            raise ValueError("Invalid entry fields")
        _path(entry["path"])
        if not isinstance(entry["source"], str):
            raise ValueError("Invalid entry source")
        key = (entry["source"], entry["path"])
        if key in seen:
            raise ValueError(f"Duplicate file entry: {key}")
        if key not in expected:
            raise ValueError(f"Unknown source file: {key}")
        seen.add(key)
        if (type(entry["bytes"]) is not int
                or {"bytes": entry["bytes"], "sha256": entry["sha256"]} != expected[key]):
            raise ValueError(f"Source identity mismatch: {key}")
        if entry["review_required"] is not True:
            raise ValueError("Planning entries must retain review_required=true")
        if not _strings(entry["reasons"], nonempty=True) or not _strings(entry.get("signals", [])):
            raise ValueError("Each entry needs reasons and valid optional signals")
        disposition = entry["disposition"]
        if not isinstance(disposition, str) or disposition not in DISPOSITIONS:
            raise ValueError("Unknown disposition")
        selected = entry["targets"]
        if not _strings(selected) or len(selected) != len(set(selected)) or any(label not in targets for label in selected):
            raise ValueError("Entry targets must be unique declared repository labels")
        visibility = {targets[label]["visibility"] for label in selected}
        if ((disposition == "public_candidate" and visibility != {"public"})
                or (disposition == "private_provider" and visibility != {"private"})
                or (disposition == "split_required" and visibility != {"public", "private"})
                or (disposition in HELD and selected)):
            raise ValueError("Disposition and target visibility disagree")
        counts[disposition] += 1
        per_source.setdefault(key[0], Counter())[disposition] += 1
    if seen != set(expected):
        raise ValueError(f"Missing {len(set(expected) - seen)} source file entries")
    return {
        "schema_version": 1, "kind": "boundary_validation", "visibility": "private",
        "snapshot_sha256": snapshot_digest(snapshot), "structure_valid": True,
        "source_files": len(seen), "dispositions": dict(sorted(counts.items())),
        "per_source": {key: dict(sorted(value.items())) for key, value in sorted(per_source.items())},
        "publication_authorized": False, "review_required": len(seen),
        "scope": "Exact inventory coverage and plan consistency only; no content, secret, license, dependency, or behavioral approval.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("draft", "validate"):
        command = sub.add_parser(name)
        command.add_argument("--baseline", type=Path, required=True)
        if name == "validate":
            command.add_argument("--plan", type=Path, required=True)
        command.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        snapshot = read_json(args.baseline)
        result = draft(snapshot) if args.command == "draft" else validate_plan(snapshot, read_json(args.plan))
        protected = [args.baseline]
        if args.command == "validate":
            protected.append(args.plan)
        protected += [Path(item["root"]) for item in snapshot["sources"].values()]
        protected += [Path(item["path"]) for item in snapshot["artifacts"].values()]
        write_report(args.output, result, protected)
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        print(f"Boundary plan rejected: {exc}", file=sys.stderr)
        return 2
    print(f"Private {args.command} report written. Publication is not authorized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
