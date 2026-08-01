"""Export built-in research skills to skills/ as public readable JSON."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pocket.science_skills import all_science_skills  # noqa: E402


def main() -> int:
    skills = all_science_skills()
    root = ROOT / "skills"
    root.mkdir(parents=True, exist_ok=True)
    by: dict[str, list] = defaultdict(list)

    for s in skills:
        dom = (s.get("domain") or "other").lower().replace(" ", "_")
        by[dom].append(
            {
                "id": s["id"],
                "domain": s.get("domain"),
                "desc": s.get("desc"),
                "kind": s.get("kind") or "playbook",
                "tags": s.get("tags") or [],
                "worker": s.get("worker") or "SCRUTATOR",
                "product": "ResearchersHub",
                "editable": True,
                "extensible": True,
            }
        )

    catalog = {
        "product": "ResearchersHub",
        "schema": "researchershub.skills.catalog.v1",
        "total": len(skills),
        "by_domain": {k: len(v) for k, v in sorted(by.items())},
        "domains": sorted(by.keys()),
        "note": "Domain packs: skills/catalog/<domain>.json",
    }
    (root / "CATALOG.json").write_text(json.dumps(catalog, indent=2), encoding="utf-8")

    index = {
        "product": "ResearchersHub",
        "total": len(skills),
        "skills": [
            {"id": s["id"], "domain": s.get("domain"), "desc": s.get("desc")} for s in skills
        ],
    }
    (root / "INDEX.json").write_text(json.dumps(index, indent=2), encoding="utf-8")

    cat_dir = root / "catalog"
    cat_dir.mkdir(parents=True, exist_ok=True)
    for dom, items in sorted(by.items()):
        payload = {
            "product": "ResearchersHub",
            "domain": dom,
            "count": len(items),
            "skills": sorted(items, key=lambda x: x["id"]),
        }
        (cat_dir / f"{dom}.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"{dom}: {len(items)}")

    lines = [
        "# Research skills catalog",
        "",
        f"**{len(skills)}** skills ship in this folder as readable JSON.",
        "",
        "Before this export, skills lived only inside Python modules — so GitHub looked empty.",
        "They are now public and editable here.",
        "",
        "| File | Purpose |",
        "|------|---------|",
        "| [CATALOG.json](CATALOG.json) | Counts by domain |",
        "| [INDEX.json](INDEX.json) | All skill ids + one-line descriptions |",
        "| [catalog/](catalog/) | Full skill objects per domain |",
        "| [example_custom.json](example_custom.json) | Template for your own skills |",
        "| [researchershub/SKILL.md](researchershub/SKILL.md) | Optional coding-agent how-to |",
        "",
        "## Domains",
        "",
        "| Domain | Count | File |",
        "|--------|------:|------|",
    ]
    for dom, items in sorted(by.items(), key=lambda x: (-len(x[1]), x[0])):
        lines.append(f"| `{dom}` | {len(items)} | [catalog/{dom}.json](catalog/{dom}.json) |")
    lines += [
        "",
        "## How skills load at runtime",
        "",
        "1. Built-in Python packs: `src/pocket/science_skills.py`, `research_skills_ext.py`, `research_skills_mega.py`",
        "2. JSON in this folder (`catalog/*.json` and extra packs you add)",
        "3. Operator machine: `~/.researchershub/skills/` or `$RH_SKILLS_DIR`",
        "",
        "API: `GET /v1/researchers/skills`",
        "",
        "Regenerate this export after editing Python packs:",
        "",
        "```powershell",
        "python scripts/export_skills_catalog.py",
        "```",
        "",
    ]
    (root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("TOTAL", len(skills))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
