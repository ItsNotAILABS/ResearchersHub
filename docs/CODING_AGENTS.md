# Coding agents × ResearchersHub

Make **Claude, Grok, Codex, Cursor, Copilot, Gemini**, and any HTTP agent first-class clients.

## One surface, every agent

| Interface | Best for |
|-----------|----------|
| **MCP stdio** `python -m pocket mcp` | Claude Desktop, Claude Code, Cursor, Grok MCP |
| **REST** `/v1/agents/*` | Codex, Copilot, shell agents, CI, custom bots |
| **OpenAI tools JSON** | Grok, GPT, Cursor tool calling |
| **Anthropic tools JSON** | Claude tool use |
| **Skill files** | Grok `~/.grok/skills`, Claude project skills |

```http
GET  /v1/agents/manifest
GET  /v1/agents/tools
GET  /v1/agents/help?agent=grok
POST /v1/agents/invoke
```

## Claude

1. Project instructions: root `CLAUDE.md` + `AGENTS.md`
2. MCP server:

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

3. Model flag: `RH_MODEL=claude` + `ANTHROPIC_API_KEY`
4. Atlas agent id: `claude` / `claude-code`

## Grok

1. Install skill:

```powershell
Copy-Item -Recurse skills\researchershub $env:USERPROFILE\.grok\skills\researchershub
```

2. Or MCP / REST as above
3. Model: `RH_MODEL=grok` + `XAI_API_KEY`
4. Atlas agent id: `grok`

OpenAI-style tools: `GET /v1/agents/tools` → `.openai`

## Codex / OpenAI coding agents

```bash
export PYTHONPATH=src
python -m pocket serve &
curl -s $RH_BASE/v1/agents/invoke -H 'content-type: application/json' \
  -H 'X-Agent-Name: codex' \
  -d '{"name":"rh_skills_list","arguments":{"domain":"ml","limit":20}}'
```

Also reads `AGENTS.md`. Model: `RH_MODEL=codex` or `gpt`.

## Cursor

- `.cursorrules` loaded automatically
- Add MCP server (same as Claude)
- Header `X-Agent-Name: cursor`

## GitHub Copilot

- `.github/copilot-instructions.md`
- Use REST invoke from agent mode / chat with host running

## Gemini / others

- `GEMINI.md` + `AGENTS.md`
- Point `RH_BASE_URL` at any OpenAI-compatible endpoint for chat routing
- Always can use tools without a cloud model (construct, skills, atlas are local)

## CLI for agents

```text
python -m pocket tools              # print full manifest
python -m pocket invoke rh_identity
python -m pocket invoke rh_construct --args "{\"prompt\":\"titration\"}"
python -m pocket mcp                # stdio MCP
```

## Security note

Agent prefixes (`/v1/agents/`, `/v1/researchers/`) are open on the local host for ergonomics.  
Do **not** expose an unauthenticated public tunnel without Access / auth in front.
