"""ResearchersHub product surface — sovereign research desk.

Pillars:
  • Any model (GLM, Kimi, DeepSeek, Claude, GPT, fine-tune) — one flag
  • 250+ research skills (ML, comp bio, cheminformatics, …) — editable
  • No throttling, no gatekeeping, no vendor deciding science
  • Native Atlas — many agents, one shared reproducible research graph
  • Runs on your infra — your data stays yours
"""

from __future__ import annotations

from typing import Any, Dict, List

PRODUCT_NAME = "ResearchersHub"
PRODUCT_FULL = "ResearchersHub — Sovereign research desk for scientists"
TAGLINE = (
    "Any model. 970+ research skills. MCP for coding agents. "
    "Full figures in chat. Atlas graph. Your infra — your data."
)
VERSION = "1.2.1"
LINEAGE = "Forked from POCKET host co-pilot; science-first under ItsNotAI Labs."
LAB = "ItsNotAI Labs"
COMPANY = "Medina Tech Labs"
ORG = "ItsNotAILABS"
GITHUB = "https://github.com/ItsNotAILABS/ResearchersHub"


def doctrine() -> Dict[str, Any]:
    return {
        "any_model": True,
        "models": ["glm", "kimi", "deepseek", "claude", "gpt", "finetune", "local"],
        "one_flag": "RH_MODEL=glm|kimi|deepseek|claude|gpt|finetune|local",
        "skills_750_plus": True,
        "skills_250_plus": True,  # back-compat
        "skills_domains": [
            "ml",
            "compbio",
            "cheminformatics",
            "clinical",
            "materials",
            "neuroscience",
            "earth",
            "astro",
            "engineering",
            "chemistry",
            "biology",
            "physics",
            "data",
            "data_platform",
            "literature",
            "lab",
            "construct",
            "comms",
            "atlas",
            "theory",
            "research_ops",
        ],
        "skills_editable": True,
        "skills_extensible": True,
        "throttling": "none-by-platform",
        "gatekeeping": False,
        "vendor_decides_science": False,
        "atlas": {
            "native": True,
            "many_agents": True,
            "one_shared_graph": True,
            "reproducible": True,
        },
        "runs_on": "your_infra",
        "data_stays": "yours",
    }


def identity() -> Dict[str, Any]:
    from pocket.science_skills import science_catalog_summary

    cat = science_catalog_summary()
    model = {}
    atlas = {}
    try:
        from pocket.model_router import doctrine as model_doctrine, resolve_model

        model = {"doctrine": model_doctrine(), "active": resolve_model()}
    except Exception as e:
        model = {"error": str(e)[:120]}
    try:
        from pocket.atlas_graph import snapshot

        atlas = snapshot()
    except Exception as e:
        atlas = {"error": str(e)[:120]}

    return {
        "ok": True,
        "product": PRODUCT_NAME,
        "full": PRODUCT_FULL,
        "tagline": TAGLINE,
        "version": VERSION,
        "lineage": LINEAGE,
        "lab": LAB,
        "company": COMPANY,
        "org": ORG,
        "github": GITHUB,
        "science_skills": cat,
        "doctrine": doctrine(),
        "model": model,
        "atlas": atlas,
        "features": [
            "Any model: GLM, Kimi, DeepSeek, Claude, GPT, fine-tune — one flag (RH_MODEL)",
            "750+ research skills — ML, comp bio, cheminformatics, clinical, materials, more",
            "Skills readable, editable, extensible (JSON packs + Python catalogs)",
            "No platform throttling, no gatekeeping, no vendor deciding what science is okay",
            "Native Atlas: many agents, one shared reproducible research graph",
            "Runs on your infra — your data stays yours",
            "Chats return whole figures/charts + real Python constructive workflows",
            "Coding agents: Claude, Grok, Codex, Cursor, Copilot, Gemini via MCP + REST tools",
        ],
        "coding_agents": {
            "mcp": "python -m pocket mcp",
            "manifest": "/v1/agents/manifest",
            "invoke": "/v1/agents/invoke",
            "clients": [
                "claude",
                "claude-code",
                "grok",
                "codex",
                "cursor",
                "copilot",
                "gemini",
                "any-http-agent",
            ],
            "docs": [
                "AGENTS.md",
                "CLAUDE.md",
                ".cursorrules",
                "docs/CODING_AGENTS.md",
                "skills/researchershub/SKILL.md",
            ],
        },
        "paths": {
            "desk": "/desk",
            "identity": "/v1/researchers",
            "skills": "/v1/researchers/skills",
            "models": "/v1/researchers/models",
            "atlas": "/v1/researchers/atlas",
            "construct": "/v1/researchers/construct",
            "board": "/v1/researchers/board",
            "chat": "/v1/ai/chat",
            "agents_manifest": "/v1/agents/manifest",
            "agents_invoke": "/v1/agents/invoke",
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
