# ResearchersHub — instructions for all coding agents

You are working with **ResearchersHub** (ItsNotAI Labs): a sovereign research desk with **970+ skills**, multi-model routing, constructive Python/charts, and a shared **Atlas** research graph.

For **Claude, Grok, Codex, Cursor, Copilot, Gemini**, and any HTTP/MCP agent.

## Doctrine

- Any model via one flag — no single-vendor lock-in
- No platform gatekeeping of science
- Data stays on operator infra
- Prefer real scripts + full figures over prose placeholders
- Write durable claims into Atlas when research work finishes

## Start host

```powershell
cd ResearchersHub
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

Base URL: `http://127.0.0.1:8787` (or `$RH_BASE`)

> Import path stays `pocket` for host compatibility; product name is **ResearchersHub**.

## MCP

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket mcp
```

## REST tools

| Call | Path |
|------|------|
| Manifest | `GET /v1/agents/manifest` |
| Tools | `GET /v1/agents/tools` |
| Help | `GET /v1/agents/help?agent=claude` |
| Invoke | `POST /v1/agents/invoke` |

Tools: `rh_identity` · `rh_skills_list` · `rh_skill_get` · `rh_models` · `rh_construct` · `rh_chat` · `rh_atlas_*` · `rh_doctrine` · `rh_coding_help`

## Model flag

```text
RH_MODEL=claude|grok|gpt|deepseek|glm|kimi|codex|finetune|local
RH_CHAT_VIA_ROUTER=1
```

## When coding on this repo

1. Product branding: **ResearchersHub** (not POCKET) in user-facing text.
2. Skills: `science_skills.py`, `research_skills_ext.py`, `research_skills_mega.py`.
3. Agents: `agent_bridge.py`, `mcp_server.py`.
4. Secrets: never commit keys; use env / operator home.
5. After research: `rh_atlas_claim` with your agent name.

## Docs map

| Doc | Purpose |
|-----|---------|
| [README.md](README.md) | Public product face |
| [PRODUCT.md](PRODUCT.md) | Product definition |
| [SHIP.md](SHIP.md) | Ship checklist |
| [docs/CODING_AGENTS.md](docs/CODING_AGENTS.md) | Per-agent setup |
| [docs/API_QUICKSTART.md](docs/API_QUICKSTART.md) | API |
| [docs/LINEAGE.md](docs/LINEAGE.md) | POCKET heritage (short) |
| [docs/archive/pocket-lineage/](docs/archive/pocket-lineage/) | Historical POCKET papers only |

## Skill install

```powershell
powershell -ExecutionPolicy Bypass -File scripts\Install-Coding-Agents.ps1
```
