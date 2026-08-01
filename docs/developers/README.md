# Developer & coding-agent notes

Optional setup for people who use **coding agents** against this host.  
These files are **not** required to run ResearchersHub as a research product.

| File | For |
|------|-----|
| [claude.md](claude.md) | Claude / Claude Code |
| [gemini.md](gemini.md) | Gemini-style agents |
| [cursor-rules.md](cursor-rules.md) | Cursor rules (copy into your editor if you want) |
| [mcp.example.json](mcp.example.json) | Example MCP client config |
| [../CODING_AGENTS.md](../CODING_AGENTS.md) | Full multi-agent guide |
| [../../AGENTS.md](../../AGENTS.md) | Shared contract for all agents |

## Public product (everyone)

Start here instead:

- [../../README.md](../../README.md)
- [../../PRODUCT.md](../../PRODUCT.md)
- [../API_QUICKSTART.md](../API_QUICKSTART.md)

## Run host + tools

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
python -m pocket mcp    # optional: tool bridge for coding agents
```
