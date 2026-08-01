---
name: researchershub
description: >
  ResearchersHub — sovereign research desk for Claude, Grok, Codex, Cursor, and all coding agents.
  970+ research skills (ML, comp bio, cheminformatics, clinical). Full PNG charts + real Python.
  Atlas shared research graph. MCP + REST tools. Triggers: /researchershub, research skills,
  titration chart, QSAR, Atlas claim, RH_MODEL, science construct, coding agent research.
---

# ResearchersHub skill

## Product

Local research platform by **ItsNotAI Labs**:

- Any model via `RH_MODEL` (claude · grok · gpt · deepseek · glm · kimi · finetune · local)
- 970+ editable research skills
- Construct: full figures + runnable Python
- Atlas: many agents → one reproducible graph
- Your infra — data stays yours

**Base:** `http://127.0.0.1:8787`  
**Env:** `RH_BASE`, `PYTHONPATH=<repo>/src`

## Start

```powershell
$env:PYTHONPATH = "<path-to-ResearchersHub>\src"
python -m pocket serve --host 0.0.0.0 --port 8787
python -m pocket mcp
```

## Tools

| Tool | Purpose |
|------|---------|
| `rh_identity` | Product + skill counts |
| `rh_skills_list` | Search skills |
| `rh_skill_get` | One skill |
| `rh_models` | Providers / active flag |
| `rh_construct` | Charts + full Python |
| `rh_chat` | Multi-model research chat |
| `rh_atlas_snapshot` / `export` / `claim` | Research graph |
| `rh_coding_help` | Per-agent setup |
| `rh_doctrine` | Pillars |

```bash
curl -s "$RH_BASE/v1/agents/invoke" \
  -H "content-type: application/json" \
  -H "X-Agent-Name: grok" \
  -d '{"name":"rh_construct","arguments":{"prompt":"dose-response IC50 curve"}}'
```

## Workflow

1. Host up → `rh_identity`
2. Figures → `rh_construct`
3. Protocols → `rh_skills_list` (domain: ml, compbio, cheminformatics, …)
4. Results → `rh_atlas_claim` with your agent name

## Install for Grok

```powershell
Copy-Item -Recurse -Force <repo>\skills\researchershub $env:USERPROFILE\.grok\skills\researchershub
```

## Repo

https://github.com/ItsNotAILABS/ResearchersHub
