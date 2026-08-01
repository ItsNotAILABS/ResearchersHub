# Cursor rules (optional)

Copy into your local Cursor project settings if you use Cursor with this repo.  
This file is **documentation** in the public repo — not a hidden vendor folder.

## Product

- Name: **ResearchersHub** (ItsNotAI Labs)
- 970+ research skills, multi-model (`RH_MODEL`), Atlas graph, constructive charts/Python
- Package import: `pocket` (runtime compatibility only)

## Tools

```text
GET  http://127.0.0.1:8787/v1/agents/manifest
POST http://127.0.0.1:8787/v1/agents/invoke
Header: X-Agent-Name: cursor
```

MCP: `python -m pocket mcp` with `PYTHONPATH=src`.

## Rules

1. Use `rh_construct` for science figures (full PNG + real Python).
2. Use `rh_skills_list` before inventing skills.
3. Claim results via `rh_atlas_claim` with `agent=cursor`.
4. No secrets in commits.
5. Do not reintroduce archived host-marketing copy into public docs.
