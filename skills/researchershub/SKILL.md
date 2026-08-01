---
name: researchershub
description: >
  ResearchersHub — sovereign research desk for Claude, Grok, Codex, Cursor, and all coding agents.
  750+ research skills (ML, comp bio, cheminformatics, clinical). Full PNG charts + real Python.
  Atlas shared research graph. MCP + REST tools. Triggers: /researchershub, research skills,
  titration chart, QSAR, Atlas claim, RH_MODEL, science construct, coding agent research.
---

# ResearchersHub skill (all coding agents)

## What it is

Local research platform (ItsNotAI Labs):

- **Any model** via `RH_MODEL` (claude · grok · gpt · deepseek · glm · kimi · finetune · local)
- **750+** editable research skills
- **Construct**: full figures + runnable Python
- **Atlas**: many agents → one reproducible graph
- **Your infra** — data stays yours

**Default base:** `http://127.0.0.1:8787`  
**Env:** `RH_BASE`, `PYTHONPATH=<repo>/src`

## Start

```powershell
$env:PYTHONPATH = "C:\Users\Medin\OneDrive\ResearchersHub\src"
python -m pocket serve --host 0.0.0.0 --port 8787
# MCP for Claude/Cursor/Grok:
python -m pocket mcp
```

## Tools (invoke)

| Tool | Purpose |
|------|---------|
| `rh_identity` | Product + skill counts |
| `rh_skills_list` | Search 750+ skills |
| `rh_skill_get` | One skill |
| `rh_models` | Providers / active flag |
| `rh_construct` | **Charts + full Python** |
| `rh_chat` | Multi-model research chat |
| `rh_atlas_snapshot` | Graph snapshot |
| `rh_atlas_export` | Full graph |
| `rh_atlas_claim` | Post claim as this agent |
| `rh_coding_help` | Per-agent setup |
| `rh_doctrine` | Pillars |

### REST

```bash
curl -s "$RH_BASE/v1/agents/invoke" \
  -H "content-type: application/json" \
  -H "X-Agent-Name: grok" \
  -d '{"name":"rh_construct","arguments":{"prompt":"dose-response IC50 curve"}}'
```

### MCP

```text
command: python
args: [-m, pocket, mcp]
env: PYTHONPATH=<repo>/src
```

## Agent workflow

1. Ensure host up (`GET /health` or `rh_identity`).
2. For figures/workflows → `rh_construct` (not ASCII plots).
3. For protocols → `rh_skills_list` with domain (`ml`, `compbio`, `cheminformatics`, …).
4. After results → `rh_atlas_claim` with your agent name (`grok`, `claude`, `codex`, …).
5. Never invent gatekeeping — science is operator-controlled.

## Install this skill for Grok

```powershell
Copy-Item -Recurse -Force `
  C:\Users\Medin\OneDrive\ResearchersHub\skills\researchershub `
  $env:USERPROFILE\.grok\skills\researchershub
```

## Repo

https://github.com/ItsNotAILABS/ResearchersHub
