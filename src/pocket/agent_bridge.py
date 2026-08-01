"""ResearchersHub agent bridge — usable by Claude, Grok, Codex, Cursor, and all coding agents.

Provides:
  - Tool catalog (OpenAI / Anthropic / MCP-shaped)
  - HTTP invoke helpers for any agent that can call REST
  - Manifest for skill loaders (Grok skills, Claude Code, Cursor)

Env:
  RH_BASE=http://127.0.0.1:8787
  RH_API_KEY / POCKET_BASIC_AUTH (optional)
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

PRODUCT = "ResearchersHub"
VERSION = "1.2.0"

# Canonical tool list — every coding agent sees the same surface
TOOLS: List[Dict[str, Any]] = [
    {
        "name": "rh_identity",
        "description": "ResearchersHub product identity, doctrine, skill counts, active model.",
        "input_schema": {"type": "object", "properties": {}, "additionalProperties": False},
        "http": {"method": "GET", "path": "/v1/researchers"},
    },
    {
        "name": "rh_skills_list",
        "description": "List 750+ research skills (ML, comp bio, cheminformatics, clinical, …). Optional domain filter.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Filter domain e.g. ml, compbio, cheminformatics, clinical",
                },
                "query": {"type": "string", "description": "Substring match on id/desc"},
                "limit": {"type": "integer", "description": "Max skills to return", "default": 50},
            },
        },
        "http": {"method": "GET", "path": "/v1/researchers/skills"},
    },
    {
        "name": "rh_skill_get",
        "description": "Get one research skill by id.",
        "input_schema": {
            "type": "object",
            "properties": {"skill_id": {"type": "string"}},
            "required": ["skill_id"],
        },
    },
    {
        "name": "rh_models",
        "description": "List model providers and active RH_MODEL flag (glm|kimi|deepseek|claude|gpt|finetune|local).",
        "input_schema": {"type": "object", "properties": {}},
        "http": {"method": "GET", "path": "/v1/researchers/models"},
    },
    {
        "name": "rh_construct",
        "description": (
            "Run a constructive science workflow: returns FULL PNG chart images (base64) "
            "plus a complete runnable Python script. Use for titration, kinetics, dose-response, "
            "regression, Beer-Lambert, stress-strain, or any research chart/workflow."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "What to plot or build"},
                "skill_id": {"type": "string", "description": "Optional skill id"},
                "board": {"type": "boolean", "description": "If true, multi-figure board"},
            },
            "required": ["prompt"],
        },
        "http": {"method": "POST", "path": "/v1/researchers/construct"},
    },
    {
        "name": "rh_chat",
        "description": (
            "Research chat via multi-model router. Figures + Python enrichment when relevant. "
            "model flag: glm|kimi|deepseek|claude|gpt|finetune|local|grok"
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"},
                "messages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "role": {"type": "string"},
                            "content": {"type": "string"},
                        },
                    },
                },
                "model": {"type": "string", "description": "RH_MODEL flag override"},
            },
        },
        "http": {"method": "POST", "path": "/v1/researchers/chat"},
    },
    {
        "name": "rh_atlas_snapshot",
        "description": "Snapshot the shared Atlas research graph (many agents, one graph).",
        "input_schema": {"type": "object", "properties": {}},
        "http": {"method": "GET", "path": "/v1/researchers/atlas"},
    },
    {
        "name": "rh_atlas_export",
        "description": "Export full Atlas graph JSON for reproducibility.",
        "input_schema": {"type": "object", "properties": {}},
        "http": {"method": "GET", "path": "/v1/researchers/atlas/export"},
    },
    {
        "name": "rh_atlas_claim",
        "description": "Any coding agent posts a claim/result into the shared Atlas graph.",
        "input_schema": {
            "type": "object",
            "properties": {
                "agent": {
                    "type": "string",
                    "description": "Agent name e.g. claude, grok, codex, cursor",
                },
                "title": {"type": "string"},
                "body": {"type": "string"},
                "kind": {
                    "type": "string",
                    "description": "claim|paper|dataset|experiment|result|hypothesis|script",
                    "default": "claim",
                },
            },
            "required": ["title"],
        },
        "http": {"method": "POST", "path": "/v1/researchers/atlas/node"},
    },
    {
        "name": "rh_doctrine",
        "description": "ResearchersHub doctrine: any model, 750+ skills, no gatekeeping, Atlas, your infra.",
        "input_schema": {"type": "object", "properties": {}},
        "http": {"method": "GET", "path": "/v1/researchers/doctrine"},
    },
    {
        "name": "rh_coding_help",
        "description": (
            "How coding agents (Claude, Grok, Codex, Cursor, Copilot, Gemini) should use ResearchersHub: "
            "MCP, REST, env flags, skill install paths."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "agent": {
                    "type": "string",
                    "description": "claude|grok|codex|cursor|copilot|gemini|generic",
                }
            },
        },
    },
]


def base_url() -> str:
    return (
        os.environ.get("RH_BASE")
        or os.environ.get("RESEARCHERSHUB_URL")
        or os.environ.get("POCKET_URL")
        or "http://127.0.0.1:8787"
    ).rstrip("/")


def tool_manifest() -> Dict[str, Any]:
    return {
        "ok": True,
        "product": PRODUCT,
        "version": VERSION,
        "base_url": base_url(),
        "tools": TOOLS,
        "tool_count": len(TOOLS),
        "clients": [
            "claude",
            "claude-code",
            "grok",
            "codex",
            "cursor",
            "copilot",
            "gemini",
            "aider",
            "continue",
            "any-http-agent",
        ],
        "mcp": {
            "stdio": "python -m pocket mcp",
            "manifest": "/v1/agents/manifest",
            "tools": "/v1/agents/tools",
            "invoke": "/v1/agents/invoke",
        },
        "openai_tools": openai_tools(),
        "anthropic_tools": anthropic_tools(),
    }


def openai_tools() -> List[Dict[str, Any]]:
    """OpenAI function/tools format (Grok, GPT, Cursor, Codex-style)."""
    out = []
    for t in TOOLS:
        props = (t.get("input_schema") or {}).get("properties") or {}
        required = (t.get("input_schema") or {}).get("required") or []
        out.append(
            {
                "type": "function",
                "function": {
                    "name": t["name"],
                    "description": t["description"],
                    "parameters": {
                        "type": "object",
                        "properties": props,
                        "required": required,
                    },
                },
            }
        )
    return out


def anthropic_tools() -> List[Dict[str, Any]]:
    """Anthropic Claude tool format."""
    return [
        {
            "name": t["name"],
            "description": t["description"],
            "input_schema": t.get("input_schema")
            or {"type": "object", "properties": {}},
        }
        for t in TOOLS
    ]


def coding_help(agent: str = "") -> Dict[str, Any]:
    a = (agent or "generic").lower().strip()
    common = {
        "base_url": base_url(),
        "start_host": "python -m pocket serve --host 0.0.0.0 --port 8787",
        "mcp_stdio": "python -m pocket mcp",
        "env": {
            "RH_BASE": "http://127.0.0.1:8787",
            "RH_MODEL": "claude|grok|gpt|deepseek|glm|kimi|finetune|local",
            "RH_CHAT_VIA_ROUTER": "1",
            "PYTHONPATH": "path/to/ResearchersHub/src",
        },
        "docs": [
            "AGENTS.md",
            "CLAUDE.md",
            ".cursorrules",
            "docs/CODING_AGENTS.md",
            "skills/researchershub/SKILL.md",
        ],
    }
    tips = {
        "claude": {
            "mcp": "Add MCP server: command python, args [-m, pocket], env PYTHONPATH + cwd repo",
            "skill": "CLAUDE.md + skills/researchershub/SKILL.md",
            "tools": "Use anthropic_tools() or MCP tools list",
            "claim_as": "claude",
        },
        "claude-code": {
            "mcp": ".mcp.json or claude mcp add researchershub",
            "skill": "Project CLAUDE.md auto-loaded",
            "claim_as": "claude-code",
        },
        "grok": {
            "skill": "Install skills/researchershub → ~/.grok/skills/researchershub",
            "tools": "OpenAI tools schema + REST invoke",
            "mcp": "python -m pocket mcp",
            "claim_as": "grok",
        },
        "codex": {
            "instructions": "AGENTS.md + .codex/instructions if present",
            "tools": "HTTP invoke /v1/agents/invoke",
            "claim_as": "codex",
        },
        "cursor": {
            "rules": ".cursorrules + .cursor/rules/researchershub.mdc",
            "mcp": "Cursor MCP settings → stdio python -m pocket mcp",
            "claim_as": "cursor",
        },
        "copilot": {
            "instructions": ".github/copilot-instructions.md",
            "tools": "REST /v1/agents/*",
            "claim_as": "copilot",
        },
        "gemini": {
            "instructions": "GEMINI.md / AGENTS.md",
            "tools": "OpenAI-compatible tools or REST",
            "claim_as": "gemini",
        },
    }
    return {
        "ok": True,
        "product": PRODUCT,
        "agent": a,
        "common": common,
        "specific": tips.get(a) or tips.get("claude") and {
            **{"note": "Use generic REST + MCP; see AGENTS.md"},
            "claim_as": a or "agent",
        },
        "all_agents": list(tips.keys()) + ["generic"],
    }


def invoke_local(name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Invoke a tool in-process (no HTTP) — used by MCP stdio and agent host."""
    args = arguments or {}
    name = (name or "").strip()

    if name == "rh_identity":
        from pocket.researchers_hub import identity

        return identity()

    if name == "rh_doctrine":
        from pocket.researchers_hub import doctrine

        return {"ok": True, "doctrine": doctrine()}

    if name == "rh_models":
        from pocket.model_router import doctrine as md, list_providers, resolve_model

        return {
            "ok": True,
            "active": resolve_model(),
            "providers": list_providers(),
            "doctrine": md(),
        }

    if name == "rh_skills_list":
        from pocket.science_skills import all_science_skills, science_catalog_summary

        skills = all_science_skills()
        domain = (args.get("domain") or "").lower().strip()
        query = (args.get("query") or "").lower().strip()
        limit = int(args.get("limit") or 50)
        if domain:
            skills = [
                s
                for s in skills
                if (s.get("domain") or "") == domain or domain in (s.get("tags") or [])
            ]
        if query:
            skills = [
                s
                for s in skills
                if query in (s.get("id") or "") or query in (s.get("desc") or "").lower()
            ]
        return {
            "ok": True,
            "total_catalog": science_catalog_summary().get("total"),
            "returned": len(skills[:limit]),
            "skills": skills[:limit],
            "summary": science_catalog_summary(),
        }

    if name == "rh_skill_get":
        from pocket.science_skills import get_science_skill

        sid = args.get("skill_id") or args.get("id") or ""
        sk = get_science_skill(sid)
        return {"ok": bool(sk), "skill": sk}

    if name == "rh_construct":
        from pocket.science_construct import multi_figure_board, run_construct

        if args.get("board"):
            return {"ok": True, **multi_figure_board(args.get("prompt") or "")}
        r = run_construct(args.get("prompt") or "", skill_id=args.get("skill_id") or "")
        # Cap base64 in tool responses for agent context — keep paths + markdown head
        slim = {
            "ok": True,
            "kind": r.get("kind"),
            "title": r.get("title"),
            "summary": r.get("summary"),
            "script_path": r.get("script_path"),
            "image_paths": r.get("image_paths"),
            "atlas": r.get("atlas"),
            "script": r.get("script"),
            "image_count": len(r.get("images") or []),
            "markdown_preview": (r.get("markdown") or "")[:4000],
            "images": r.get("images") or [],  # full images for agents that can render
        }
        return slim

    if name == "rh_chat":
        from pocket.model_router import chat as rh_chat
        from pocket.science_construct import enrich_chat_text

        msgs = args.get("messages") or []
        prompt = args.get("prompt") or args.get("text") or ""
        if not msgs and prompt:
            msgs = [{"role": "user", "content": prompt}]
        flag = args.get("model") or args.get("flag") or ""
        routed = rh_chat(msgs, flag=flag)
        text = routed.get("content") or routed.get("error") or ""
        last = prompt
        for m in reversed(msgs):
            if (m.get("role") or "").lower() == "user":
                last = m.get("content") or last
                break
        enriched = enrich_chat_text(text, user_prompt=last, force=bool(args.get("force_figures")))
        return {
            "ok": bool(routed.get("ok")),
            "content": enriched.get("text") or text,
            "images": enriched.get("images") or [],
            "construct": enriched.get("construct"),
            "model": routed.get("config"),
            "error": routed.get("error") or "",
        }

    if name == "rh_atlas_snapshot":
        from pocket.atlas_graph import seed_if_empty, snapshot

        seed_if_empty()
        return snapshot()

    if name == "rh_atlas_export":
        from pocket.atlas_graph import export_graph, seed_if_empty

        seed_if_empty()
        return export_graph()

    if name == "rh_atlas_claim":
        from pocket.atlas_graph import agent_claim

        return agent_claim(
            args.get("agent") or "coding-agent",
            args.get("title") or "untitled",
            args.get("body") or args.get("text") or "",
            kind=args.get("kind") or "claim",
            links=args.get("links") or [],
        )

    if name == "rh_coding_help":
        return coding_help(args.get("agent") or "generic")

    return {"ok": False, "error": f"unknown tool: {name}", "tools": [t["name"] for t in TOOLS]}


def invoke_http(name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Invoke via running host HTTP (when agent is remote from Python package)."""
    url = base_url() + "/v1/agents/invoke"
    body = json.dumps({"name": name, "arguments": arguments or {}}).encode("utf-8")
    headers = {"Content-Type": "application/json", "User-Agent": "ResearchersHub-AgentBridge/1.2"}
    key = (os.environ.get("RH_API_KEY") or "").strip()
    if key:
        headers["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception as e:
        return {"ok": False, "error": str(e)[:400], "hint": "Is host up? python -m pocket serve"}


def list_tool_names() -> List[str]:
    return [t["name"] for t in TOOLS]
