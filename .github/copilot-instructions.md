# GitHub Copilot — ResearchersHub

This repository is **ResearchersHub** by ItsNotAI Labs (POCKET lineage).

## Coding context
- Python package import: `pocket`
- Product branding: ResearchersHub
- 750+ research skills; agent tools in `agent_bridge.py`
- MCP: `python -m pocket mcp`
- REST: `POST /v1/agents/invoke` with tool name `rh_*`

## Conventions
- Prefer constructive workflows that emit real Python + matplotlib figures
- Skills are editable JSON under `skills/` and Python catalogs under `src/pocket/research_skills_*.py`
- Atlas graph under `~/.researchershub/atlas/`
- Follow `AGENTS.md` for multi-agent doctrine

## Do not
- Hardcode API keys
- Replace full chart output with ASCII placeholders when construct tools exist
- Assume founder disk paths for market/member seats
