# Coding agents × ResearchersHub

First-class clients: **Claude, Grok, Codex, Cursor, Copilot, Gemini**, and any HTTP agent.

## Surfaces

| Interface | Best for |
|-----------|----------|
| **MCP** `python -m pocket mcp` | Claude Desktop, Claude Code, Cursor, Grok MCP |
| **REST** `/v1/agents/*` | Codex, Copilot, CI, custom bots |
| **OpenAI tools JSON** | Grok, GPT tool calling |
| **Anthropic tools JSON** | Claude tool use |
| **Skill file** | `skills/researchershub/SKILL.md` |

```http
GET  /v1/agents/manifest
GET  /v1/agents/tools
GET  /v1/agents/help?agent=grok
POST /v1/agents/invoke
```

## Claude

1. [`CLAUDE.md`](../CLAUDE.md) + [`AGENTS.md`](../AGENTS.md)
2. MCP:

```json
{
  "mcpServers": {
    "researchershub": {
      "command": "python",
      "args": ["-m", "pocket", "mcp"],
      "env": { "PYTHONPATH": "/absolute/path/to/ResearchersHub/src" }
    }
  }
}
```

3. `RH_MODEL=claude` + `ANTHROPIC_API_KEY`
4. Atlas agent id: `claude`

## Grok

```powershell
Copy-Item -Recurse skills\researchershub $env:USERPROFILE\.grok\skills\researchershub
```

Or MCP / REST. `RH_MODEL=grok` + `XAI_API_KEY`. Atlas id: `grok`.

## Codex

```bash
export PYTHONPATH=src
python -m pocket serve &
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H 'content-type: application/json' \
  -H 'X-Agent-Name: codex' \
  -d '{"name":"rh_skills_list","arguments":{"domain":"ml","limit":20}}'
```

## Cursor / Copilot / Gemini

- Cursor: [`.cursorrules`](../.cursorrules) + [`.mcp.json`](../.mcp.json)
- Copilot: [`.github/copilot-instructions.md`](../.github/copilot-instructions.md)
- Gemini: [`GEMINI.md`](../GEMINI.md)

## Tools

`rh_identity` · `rh_skills_list` · `rh_skill_get` · `rh_models` · `rh_construct` · `rh_chat` · `rh_atlas_*` · `rh_doctrine` · `rh_coding_help`

## CLI

```text
python -m pocket tools
python -m pocket invoke rh_identity
python -m pocket mcp
```

## Security

Agent routes are convenient on localhost. Do not expose unauthenticated public tunnels without Access.
