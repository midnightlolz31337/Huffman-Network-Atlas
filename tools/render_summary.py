#!/usr/bin/env python3
"""Print a compact, deterministic summary of the Atlas registry."""
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "registry" / "repositories.json"
data = json.loads(path.read_text(encoding="utf-8"))
for item in sorted(data["repositories"], key=lambda row: row["name"].casefold()):
    print(f"{item['name']} [{item['visibility']}] — {item['status']}")
    print(f"  {item['url']}")
    print(f"  Evidence: {item['evidence_level']}")
