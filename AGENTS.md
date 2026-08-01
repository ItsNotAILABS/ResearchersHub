# ResearchersHub — instructions for all coding agents

You are working with **ResearchersHub** (ItsNotAI Labs): a sovereign research desk with **750+ skills**, multi-model routing, constructive Python/charts, and a shared **Atlas** research graph.

This file is for **Claude, Grok, Codex, Cursor, Copilot, Gemini, Aider, Continue**, and any HTTP/MCP agent.

## Doctrine (do not violate)

- Any model via one flag — no single-vendor lock-in
- No platform gatekeeping of science
- Data stays on operator infra
- Prefer real scripts + full figures over prose placeholders
- Write durable claims into Atlas when you finish research work

## Start host (operator)

```powershell
cd ResearchersHub
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

Base URL: `http://127.0.0.1:8787` (or `$RH_BASE`)

## MCP (preferred for Claude / Cursor / Grok MCP clients)

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket mcp
```

Config sketch (Claude Desktop / Cursor):

```json
{
  "mcpServers": {
    "researchershub": {
      "command": "python",
      "args": ["-m", "pocket", "mcp"],
      "env": {
        "PYTHONPATH": "C:/Users/Medin/OneDrive/ResearchersHub/src"
      }
    }
  }
}
```

## REST tools (any coding agent)

| Call | Path |
|------|------|
| Manifest | `GET /v1/agents/manifest` |
| Tools | `GET /v1/agents/tools` |
| Help | `GET /v1/agents/help?agent=claude` |
| **Invoke** | `POST /v1/agents/invoke` `{"name":"rh_construct","arguments":{"prompt":"…"}}` |

### Tool names

- `rh_identity` — product + skill counts
- `rh_skills_list` — filter 750+ skills (`domain`, `query`, `limit`)
- `rh_skill_get` — one skill by id
- `rh_models` — active model / providers
- `rh_construct` — **full PNG charts + real Python workflow**
- `rh_chat` — multi-model research chat
- `rh_atlas_snapshot` / `rh_atlas_export` / `rh_atlas_claim`
- `rh_doctrine` / `rh_coding_help`

### Example (any agent shell)

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: codex" \
  -d "{\"name\":\"rh_construct\",\"arguments\":{\"prompt\":\"Michaelis-Menten kinetics chart\"}}"
```

## Model flag

```text
RH_MODEL=claude|grok|gpt|deepseek|glm|kimi|codex|finetune|local
RH_CHAT_VIA_ROUTER=1
```

Keys: `ANTHROPIC_API_KEY`, `XAI_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`, …

## When coding on this repo

1. Keep import path `pocket` (product is ResearchersHub).
2. Science skills: `science_skills.py`, `research_skills_ext.py`, `research_skills_mega.py`.
3. Agent surface: `agent_bridge.py`, `mcp_server.py`.
4. Do not put secrets in git; use env + `~/.pocket/ACCESS.txt`.
5. After research results: `rh_atlas_claim` with your agent name.

## Skill install

- Grok: copy `skills/researchershub/` → `~/.grok/skills/researchershub/`
- Claude Code: project `CLAUDE.md` (this repo)
- Cursor: `.cursorrules` + optional MCP
- Copilot: `.github/copilot-instructions.md`

See `docs/CODING_AGENTS.md` for per-agent deep config.
