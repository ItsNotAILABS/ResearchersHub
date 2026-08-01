# GitHub Copilot — ResearchersHub

This repository is **ResearchersHub** by ItsNotAI Labs.

## Coding context

- Product name: **ResearchersHub**
- Python package import: `pocket` (host compatibility only)
- Agent tools: `src/pocket/agent_bridge.py`
- MCP: `python -m pocket mcp`
- REST: `POST /v1/agents/invoke` with tool name `rh_*`

## Conventions

- Prefer constructive workflows that emit real Python + matplotlib figures
- Skills: Python catalogs + JSON under `skills/`
- Atlas graph under `~/.researchershub/atlas/`
- Follow `AGENTS.md` for multi-agent doctrine
- Do not reintroduce POCKET marketing copy into user-facing docs (lineage archive only)

## Do not

- Hardcode API keys
- Replace full chart output with ASCII placeholders when construct tools exist
