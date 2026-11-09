#!/usr/bin/env python3
"""Validate the Atlas repository registry using only the Python standard library."""
from __future__ import annotations
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "repositories.json"
REQUIRED = {"id", "url", "owner", "name", "visibility", "description", "status", "evidence_level"}

def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    records = data.get("repositories")
    if not isinstance(records, list):
        return errors + ["repositories must be an array"]
    seen: set[str] = set()
    for index, record in enumerate(records):
        prefix = f"repositories[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED - record.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(sorted(missing))}")
        rid = record.get("id")
        if isinstance(rid, str):
            if rid in seen:
                errors.append(f"duplicate repository id: {rid}")
            seen.add(rid)
        url = record.get("url")
        parsed = urlparse(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme != "https" or parsed.netloc != "github.com":
            errors.append(f"{prefix}.url must be an https://github.com URL")
        if record.get("visibility") not in {"public", "private", "internal", "unknown"}:
            errors.append(f"{prefix}.visibility is invalid")
        if not isinstance(record.get("description"), str) or not record["description"].strip():
            errors.append(f"{prefix}.description must be non-empty")
    return errors

def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1
    print(f"OK: {len(data['repositories'])} repository records validated")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
