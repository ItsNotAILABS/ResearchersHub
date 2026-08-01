"""ResearchersHub product surface — POCKET forked for scientists & researchers.

Identity, skill merge, and chat enrichment hooks.
"""

from __future__ import annotations

from typing import Any, Dict, List

PRODUCT_NAME = "ResearchersHub"
PRODUCT_FULL = "ResearchersHub — Sovereign research desk for scientists"
TAGLINE = (
    "Chemistry, biology, physics, stats — 100+ science skills. "
    "Chats return whole figures, charts, and real Python constructive workflows."
)
VERSION = "1.0.0"
LINEAGE = "Forked from POCKET host co-pilot; tailored for research labs."
LAB = "ItsNotAI Labs"
COMPANY = "Medina Tech Labs"


def identity() -> Dict[str, Any]:
    from pocket.science_skills import science_catalog_summary

    cat = science_catalog_summary()
    return {
        "ok": True,
        "product": PRODUCT_NAME,
        "full": PRODUCT_FULL,
        "tagline": TAGLINE,
        "version": VERSION,
        "lineage": LINEAGE,
        "lab": LAB,
        "company": COMPANY,
        "science_skills": cat,
        "features": [
            "100+ preloaded science & advanced chemistry skills",
            "Chat returns full PNG charts embedded as images",
            "Real runnable Python constructive workflows saved to disk",
            "Lab / literature / stats / materials skill domains",
            "POCKET host DNA: Edge desk, multi-agent, phone, API",
        ],
        "paths": {
            "desk": "/desk",
            "skills": "/v1/researchers/skills",
            "construct": "/v1/researchers/construct",
            "board": "/v1/researchers/board",
            "chat": "/v1/ai/chat",
        },
    }


def merged_skills() -> List[Dict[str, Any]]:
    """Host skills + science skills (science first-class for researchers)."""
    from pocket.science_skills import all_science_skills

    out: List[Dict[str, Any]] = []
    seen = set()
    for s in all_science_skills():
        sid = s["id"]
        if sid in seen:
            continue
        seen.add(sid)
        out.append(s)
    try:
        from pocket.skill_suite import SUITE

        for s in SUITE:
            sid = s.get("id")
            if not sid or sid in seen:
                continue
            seen.add(sid)
            out.append(s)
    except Exception:
        pass
    return out


def skill_count_total() -> int:
    return len(merged_skills())
