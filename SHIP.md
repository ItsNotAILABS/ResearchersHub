# ResearchersHub — ship checklist

**Version:** 1.2.1  
**Org:** https://github.com/ItsNotAILABS/ResearchersHub

## Product surface

- [x] Multi-model `RH_MODEL` (Claude, Grok, GPT, Codex, DeepSeek, GLM, Kimi, fine-tune, local)
- [x] 970+ research skills (editable / extensible)
- [x] Construct: full PNG + real Python
- [x] Atlas shared research graph
- [x] MCP stdio + REST agent tools
- [x] AGENTS.md / CLAUDE.md / .cursorrules / Copilot / Gemini
- [x] Public README with logo + badges
- [x] Docs cleaned (POCKET papers archived under `docs/archive/pocket-lineage/`)
- [x] Install-Coding-Agents.ps1

## Operator commands

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
python -m pocket mcp
python -m pocket tools
python -m pocket identity
```

## Verify

```powershell
curl -s http://127.0.0.1:8787/health
curl -s http://127.0.0.1:8787/v1/researchers
curl -s http://127.0.0.1:8787/v1/agents/manifest
```
