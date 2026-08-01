# ResearchersHub — coding-agent contract

Optional. For agents and automation that call this host’s tools.

**Product:** ResearchersHub (ItsNotAI Labs)  
**Public docs:** [README.md](README.md) · [docs/REPO_LAYOUT.md](docs/REPO_LAYOUT.md)

## Doctrine

- Any model via one flag — no single-vendor lock-in
- No platform gatekeeping of science
- Data stays on operator infra
- Prefer real scripts + full figures over placeholders
- Write durable claims into Atlas when research finishes

## Start host

```powershell
cd ResearchersHub
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

Base URL: `http://127.0.0.1:8787` (or `$RH_BASE`)

> Import path stays `pocket` for host compatibility; product name is **ResearchersHub**.

## MCP / REST

```powershell
python -m pocket mcp
```

| Call | Path |
|------|------|
| Manifest | `GET /v1/agents/manifest` |
| Tools | `GET /v1/agents/tools` |
| Invoke | `POST /v1/agents/invoke` |

Tools: `rh_identity` · `rh_skills_list` · `rh_skill_get` · `rh_models` · `rh_construct` · `rh_chat` · `rh_atlas_*` · `rh_doctrine` · `rh_coding_help`

## Model flag

```text
RH_MODEL=claude|grok|gpt|deepseek|glm|kimi|codex|finetune|local
RH_CHAT_VIA_ROUTER=1
```

## Repo notes

1. User-facing branding: **ResearchersHub** only.
2. Skills live in `src/pocket/science_skills*.py` and `skills/`.
3. Agent bridge: `agent_bridge.py`, `mcp_server.py`.
4. Optional IDE notes: [docs/developers/](docs/developers/) — not required to run the product.
5. Do not commit secrets or private tool home directories.

Full guide: [docs/CODING_AGENTS.md](docs/CODING_AGENTS.md)
