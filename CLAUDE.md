# CLAUDE.md — ResearchersHub

You are Claude working inside **ResearchersHub** (ItsNotAI Labs).

## Product

Sovereign research desk: **any model**, **970+ research skills**, full figures + real Python, **Atlas** shared graph, MCP tools for coding agents. Runs on operator infra.

## Tools

### MCP

```bash
PYTHONPATH=src python -m pocket mcp
```

Tools: `rh_identity`, `rh_skills_list`, `rh_skill_get`, `rh_models`, `rh_construct`, `rh_chat`, `rh_atlas_*`, `rh_doctrine`, `rh_coding_help`.

### REST

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: claude" \
  -d '{"name":"rh_construct","arguments":{"prompt":"titration curve with Python"}}'
```

## Model

```bash
export RH_MODEL=claude
export ANTHROPIC_API_KEY=...
export RH_CHAT_VIA_ROUTER=1
```

## Behaviors

1. Prefer `rh_construct` for charts/kinetics/QSAR — full images + scripts.
2. Search skills with `rh_skills_list` before inventing protocol names.
3. End substantive research with `rh_atlas_claim` (`agent: "claude"`).
4. User-facing name is **ResearchersHub** (package import may still say `pocket`).
5. Data: `~/.researchershub/` for construct + atlas.

See [AGENTS.md](AGENTS.md) and [docs/CODING_AGENTS.md](docs/CODING_AGENTS.md).
