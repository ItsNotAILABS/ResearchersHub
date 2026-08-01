# CLAUDE.md — ResearchersHub

You are Claude working inside **ResearchersHub** (ItsNotAI Labs / POCKET lineage).

## What this product is

Sovereign research desk: **any model**, **750+ research skills**, full figures + real Python, **Atlas** shared graph, runs on operator infra.

## How you call tools

### Preferred: MCP

```bash
PYTHONPATH=src python -m pocket mcp
```

Tools: `rh_identity`, `rh_skills_list`, `rh_skill_get`, `rh_models`, `rh_construct`, `rh_chat`, `rh_atlas_*`, `rh_doctrine`, `rh_coding_help`.

### REST fallback

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: claude" \
  -d '{"name":"rh_construct","arguments":{"prompt":"titration curve with Python"}}'
```

## Model routing

```bash
export RH_MODEL=claude
export ANTHROPIC_API_KEY=...
export RH_CHAT_VIA_ROUTER=1
```

## Behaviors

1. Prefer `rh_construct` when user wants charts, kinetics, QSAR plots, dose–response, lab figures — return **full images + scripts**, not ASCII art.
2. Search skills with `rh_skills_list` before inventing a protocol name.
3. End substantive research turns with `rh_atlas_claim` (`agent: "claude"`).
4. Never claim vendor-only science restrictions; doctrine is no gatekeeping.
5. Local data: `~/.researchershub/` for construct + atlas.

## Repo map

| Path | Role |
|------|------|
| `src/pocket/agent_bridge.py` | Tool catalog + invoke |
| `src/pocket/mcp_server.py` | MCP stdio |
| `src/pocket/science_skills.py` | Skill merge |
| `src/pocket/science_construct.py` | Charts + Python |
| `src/pocket/atlas_graph.py` | Shared research graph |
| `src/pocket/model_router.py` | RH_MODEL multi-provider |

Read `AGENTS.md` for the shared multi-agent contract.
