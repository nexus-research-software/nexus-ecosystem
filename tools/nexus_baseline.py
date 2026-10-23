"""Capture source identity and compare baselines without importing source code.

Reports are PRIVATE by default: filenames and test evidence can be sensitive.
Python 3.11+; standard library only. This tool does not execute application tests.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import stat
import sys
import tomllib
from typing import Any
import xml.etree.ElementTree as ET

SCHEMA_VERSION = 1
EXCLUDED_DIRECTORIES = frozenset({
    ".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".hypothesis",
})
EXCLUDED_SUFFIXES = (".pyc", ".pyo")


def read_json(path: Path) -> dict[str, Any]:
    """Read a JSON object, rejecting duplicate keys instead of losing evidence."""
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    result = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)
    if not isinstance(result, dict):
        raise ValueError("Expected a JSON object")
    return result


def file_identity(path: Path) -> dict[str, Any]:
    """Hash a regular file; reject observed replacement or mutation during read."""
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise ValueError(f"Not a regular file: {path}")
    digest = hashlib.sha256()
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    with os.fdopen(os.open(path, flags), "rb") as stream:
        opened = os.fstat(stream.fileno())
        if not os.path.samestat(before, opened):
            raise ValueError(f"File replaced before read: {path}")
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
        after = os.fstat(stream.fileno())
    current = path.lstat()
    if (not os.path.samestat(before, current)
            or not stat.S_ISREG(current.st_mode)
            or (before.st_size, before.st_mtime_ns, before.st_ctime_ns)
            != (after.st_size, after.st_mtime_ns, after.st_ctime_ns)
            or (after.st_size, after.st_mtime_ns, after.st_ctime_ns)
            != (current.st_size, current.st_mtime_ns, current.st_ctime_ns)):
        raise ValueError(f"File changed during read: {path}")
    return {"bytes": after.st_size, "sha256": digest.hexdigest()}


def tree_identity(root: Path) -> dict[str, Any]:
    """Hash a quiescent source tree; record unsupported entries as incomplete."""
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Source must be a real directory: {root}")
    entries: dict[str, Any] = {}
    omitted: list[dict[str, str]] = []

    def visit(directory: Path) -> None:
        for path in sorted(directory.iterdir(), key=lambda item: item.name):
            relative = path.relative_to(root).as_posix()
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                omitted.append({"path": relative, "reason": "symbolic_link"})
            elif stat.S_ISDIR(mode):
                if path.name not in EXCLUDED_DIRECTORIES:
                    visit(path)
            elif stat.S_ISREG(mode):
                if not path.name.endswith(EXCLUDED_SUFFIXES):
                    entries[relative] = file_identity(path)
            else:
                omitted.append({"path": relative, "reason": "non_regular_file"})

    visit(root)
    if not entries:
        raise ValueError(f"No included files in source: {root}")
    canonical = json.dumps(entries, sort_keys=True, separators=(",", ":"))
    result: dict[str, Any] = {
        "root": str(root.resolve()), "complete": not omitted,
        "files": entries, "omitted": omitted,
        "tree_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    }
    metadata = root / "pyproject.toml"
    if "pyproject.toml" in entries:
        parsed = tomllib.loads(metadata.read_text(encoding="utf-8"))
        project = parsed.get("project", parsed.get("tool", {}).get("poetry", {}))
        result["package"] = {key: project[key] for key in ("name", "version") if key in project}
    return result


def load_config(path: Path) -> dict[str, dict[str, Path]]:
    """Resolve explicit input mappings relative to the config file."""
    data = read_json(path)
    if data.get("schema_version") != SCHEMA_VERSION or set(data) - {
        "schema_version", "sources", "artifacts"
    }:
        raise ValueError("Unsupported config schema or unknown fields")
    result: dict[str, dict[str, Path]] = {}
    for group in ("sources", "artifacts"):
        mapping = data.get(group, {})
        if not isinstance(mapping, dict):
            raise ValueError(f"{group} must be an object")
        result[group] = {}
        for label, location in mapping.items():
            if not isinstance(label, str) or not label.strip() or not isinstance(location, str) or not location.strip():
                raise ValueError("Input labels and paths must be nonempty strings")
            candidate = Path(location).expanduser()
            if not candidate.is_absolute():
                candidate = path.resolve().parent / candidate
            # Keep the final component intact so a linked root/file is rejected.
            result[group][label] = candidate
    if not any(result.values()):
        raise ValueError("At least one source or artifact is required")
    return result


def snapshot(config: dict[str, dict[str, Path]]) -> dict[str, Any]:
    """Capture identities only; never import, extract, or execute supplied files."""
    sources = {name: tree_identity(root) for name, root in sorted(config["sources"].items())}
    artifacts = {
        name: {"path": str(path.absolute()), **file_identity(path)}
        for name, path in sorted(config["artifacts"].items())
    }
    return {
        "schema_version": SCHEMA_VERSION, "kind": "source_snapshot", "visibility": "private",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {"python": platform.python_version(), "system": platform.system(), "machine": platform.machine()},
        "policy": {"excluded_directories": sorted(EXCLUDED_DIRECTORIES), "excluded_suffixes": list(EXCLUDED_SUFFIXES)},
        "complete": all(item["complete"] for item in sources.values()),
        "sources": sources, "artifacts": artifacts,
    }


def validate_snapshot(data: dict[str, Any]) -> None:
    """Reject malformed or incomplete evidence before comparison."""
    if data.get("schema_version") != SCHEMA_VERSION or data.get("kind") != "source_snapshot":
        raise ValueError("Unsupported snapshot schema")
    if data.get("complete") is not True:
        raise ValueError("Cannot establish equality from an incomplete snapshot")
    if not isinstance(data.get("sources"), dict) or not isinstance(data.get("artifacts"), dict):
        raise ValueError("Missing source/artifact mappings")
    if not data["sources"] and not data["artifacts"]:
        raise ValueError("Empty snapshot")
    if not isinstance(data.get("policy"), dict):
        raise ValueError("Missing exclusion policy")
    for item in data["sources"].values():
        if item.get("complete") is not True or item.get("omitted") or not isinstance(item.get("files"), dict) or not item["files"]:
            raise ValueError("Incomplete source identity")
        canonical = json.dumps(item["files"], sort_keys=True, separators=(",", ":"))
        if hashlib.sha256(canonical.encode("utf-8")).hexdigest() != item.get("tree_sha256"):
            raise ValueError("Source identity digest is inconsistent")
    identities = list(data["artifacts"].values())
    for item in data["sources"].values():
        identities.extend(item["files"].values())
    for identity in identities:
        digest = identity.get("sha256", "")
        if (type(identity.get("bytes")) is not int or identity["bytes"] < 0
                or not isinstance(digest, str) or len(digest) != 64
                or any(c not in "0123456789abcdef" for c in digest)):
            raise ValueError("Invalid file identity")


def compare(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    """Report additions, removals, and changed bytes; relocated roots are allowed."""
    validate_snapshot(before)
    validate_snapshot(after)
    if before["policy"] != after["policy"]:
        raise ValueError("Exclusion policies differ; baselines are not comparable")
    changes = []
    for group in ("sources", "artifacts"):
        for label in sorted(set(before[group]) | set(after[group])):
            old, new = before[group].get(label), after[group].get(label)
            if old is None or new is None:
                changes.append({"group": group, "label": label, "status": "added" if old is None else "removed"})
                continue
            if group == "artifacts":
                if any(old[key] != new[key] for key in ("sha256", "bytes")):
                    changes.append({"group": group, "label": label, "status": "changed"})
                continue
            for name in sorted(set(old["files"]) | set(new["files"])):
                old_file, new_file = old["files"].get(name), new["files"].get(name)
                if old_file != new_file:
                    changes.append({"group": group, "label": label, "path": name,
                                    "status": "added" if old_file is None else "removed" if new_file is None else "changed"})
    return {"schema_version": SCHEMA_VERSION, "kind": "source_comparison", "visibility": "private",
            "equal": not changes, "changes": changes}


def junit_summary(path: Path, exit_code: int) -> dict[str, Any]:
    """Summarize observed cases and process status without exporting test text."""
    if path.stat().st_size > 32 * 1024 * 1024:
        raise ValueError("JUnit report exceeds 32 MiB")
    raw = path.read_bytes()
    if b"<!DOCTYPE" in raw.upper() or b"<!ENTITY" in raw.upper() or b"\x00" in raw:
        raise ValueError("DTD, entities, and non-UTF-8 XML are unsupported")
    root = ET.fromstring(raw)
    if root.tag not in {"testsuite", "testsuites"}:
        raise ValueError("Expected a JUnit testsuite/testsuites document")
    counts = dict(passed=0, failures=0, errors=0, skipped=0)
    for case in root.iter("testcase"):
        key = "errors" if case.find("error") is not None else "failures" if case.find("failure") is not None else "skipped" if case.find("skipped") is not None else "passed"
        counts[key] += 1
    total = sum(counts.values())
    # A collection/runner error can exist outside a testcase. Never turn it green.
    leaves = [suite for suite in root.iter("testsuite") if suite.find("testsuite") is None]
    for key in ("failures", "errors"):
        declared = [int(suite.get(key, "0")) for suite in leaves]
        if any(value < 0 for value in declared):
            raise ValueError("Negative JUnit counts")
        counts[key] = max(counts[key], sum(declared), int(root.get(key, "0")))
    return {"schema_version": SCHEMA_VERSION, "kind": "test_summary", "visibility": "private",
            "report_sha256": file_identity(path)["sha256"], "exit_code": exit_code,
            "testcases": total, **counts,
            "successful": exit_code == 0 and counts["passed"] > 0 and not counts["failures"] and not counts["errors"]}


def write_report(path: Path, data: dict[str, Any], protected: list[Path]) -> None:
    """Write once, outside source roots; never replace an input or old baseline."""
    destination = path.resolve()
    for item in protected:
        item = item.resolve()
        if destination == item or (item.is_dir() and destination.is_relative_to(item)):
            raise ValueError("Output must be outside all input paths")
    payload = json.dumps(data, indent=2, sort_keys=True) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    with os.fdopen(os.open(path, flags, 0o600), "w", encoding="utf-8", newline="\n") as stream:
        stream.write(payload)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    capture = sub.add_parser("snapshot", help="Capture private source/archive identities")
    capture.add_argument("--config", type=Path, required=True)
    comparison = sub.add_parser("compare", help="Compare two complete source snapshots")
    comparison.add_argument("before", type=Path)
    comparison.add_argument("after", type=Path)
    junit = sub.add_parser("junit", help="Summarize a test report with its actual process exit code")
    junit.add_argument("report", type=Path)
    junit.add_argument("--exit-code", type=int, required=True)
    for command in (capture, comparison, junit):
        command.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "snapshot":
            config = load_config(args.config)
            protected = [args.config, *(p for group in config.values() for p in group.values())]
            data = snapshot(config)
            success = data["complete"]
        elif args.command == "compare":
            before, after = read_json(args.before), read_json(args.after)
            data = compare(before, after)
            protected = [args.before, args.after]
            protected += [Path(item["root"]) for report in (before, after) for item in report["sources"].values() if "root" in item]
            success = data["equal"]
        else:
            data = junit_summary(args.report, args.exit_code)
            protected = [args.report]
            success = data["successful"]
        write_report(args.output, data, protected)
        print(f"{data['kind']}: {'ok' if success else 'attention required'}; report is private")
        return 0 if success else 1
    except (OSError, ValueError, TypeError, KeyError, AttributeError, ET.ParseError) as exc:
        print(f"Baseline could not be established: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
