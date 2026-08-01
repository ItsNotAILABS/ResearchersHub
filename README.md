<p align="center">
  <img src="docs/brand/researchershub-wordmark.svg" alt="ResearchersHub" width="540"/>
</p>

<p align="center">
  <strong>Sovereign research desk for scientists — and every coding agent</strong><br/>
  Any model · <b>970+ research skills</b> · Atlas graph · MCP for Claude / Grok / Codex / Cursor<br/>
  Full figures + real Python · Your infra — your data
</p>

<p align="center">
  <a href="https://github.com/ItsNotAILABS/ResearchersHub"><img alt="GitHub" src="https://img.shields.io/badge/ItsNotAILABS%2FResearchersHub-0b6e4f?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://github.com/ItsNotAILABS/ResearchersHub/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/ItsNotAILABS/ResearchersHub?style=for-the-badge&color=1d4ed8"/></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-see%20repo-64748b?style=for-the-badge"/></a>
  <a href="https://github.com/ItsNotAILABS/ResearchersHub/releases"><img alt="Ship" src="https://img.shields.io/badge/ship-1.2.1-10b981?style=for-the-badge"/></a>
</p>

<p align="center">
  <img alt="Skills 970+" src="https://img.shields.io/badge/research%20skills-970%2B-0ea5e9?style=flat-square"/>
  <img alt="MCP" src="https://img.shields.io/badge/MCP-stdio%20%2B%20REST-a855f7?style=flat-square"/>
  <img alt="Models" src="https://img.shields.io/badge/models-Claude%20%7C%20Grok%20%7C%20GPT%20%7C%20DeepSeek%20%7C%20GLM%20%7C%20Kimi%20%7C%20fine--tune-8b5cf6?style=flat-square"/>
  <img alt="Atlas" src="https://img.shields.io/badge/Atlas-shared%20research%20graph-10b981?style=flat-square"/>
  <img alt="No gatekeeping" src="https://img.shields.io/badge/gatekeeping-none-22c55e?style=flat-square"/>
  <img alt="Sovereignty" src="https://img.shields.io/badge/data-on%20your%20infra-f59e0b?style=flat-square"/>
  <img alt="Lineage" src="https://img.shields.io/badge/lineage-POCKET-6366f1?style=flat-square"/>
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white"/>
</p>

<p align="center">
  <img alt="Claude" src="https://img.shields.io/badge/Claude-MCP%20%2B%20CLAUDE.md-d97706?style=flat-square"/>
  <img alt="Grok" src="https://img.shields.io/badge/Grok-skill%20%2B%20tools-06b6d4?style=flat-square"/>
  <img alt="Codex" src="https://img.shields.io/badge/Codex-AGENTS.md%20%2B%20REST-22c55e?style=flat-square"/>
  <img alt="Cursor" src="https://img.shields.io/badge/Cursor-.cursorrules%20%2B%20MCP-0ea5e9?style=flat-square"/>
  <img alt="Copilot" src="https://img.shields.io/badge/Copilot-instructions-6366f1?style=flat-square"/>
  <img alt="Gemini" src="https://img.shields.io/badge/Gemini-GEMINI.md-4285F4?style=flat-square"/>
</p>

---

## What you get

| Pillar | Detail |
|--------|--------|
| **Any model** | Claude · Grok · GPT · Codex · DeepSeek · GLM · Kimi · fine-tune · local — **one flag** (`RH_MODEL`) |
| **970+ skills** | ML · comp bio · cheminformatics · clinical · materials · neuroscience · earth · chemistry · Atlas agents |
| **Editable** | Plain Python catalogs + JSON drops in `skills/` — readable, forkable, extensible |
| **Full figures** | Chats/construct return **complete PNG charts** + **runnable Python**, not placeholders |
| **Native Atlas** | Many agents, **one shared reproducible research graph** on your disk |
| **Coding agents** | MCP stdio + REST tools for Claude, Grok, Codex, Cursor, Copilot, Gemini |
| **No gatekeeping** | No platform throttle deciding what science is okay |
| **Your infra** | Runs where you run it. **Your data stays yours.** |

Built from the **POCKET** multi-agent host lineage (Edge desk, agents, phone, sellable API) — specialized for real research.

<p align="center">
  <img src="docs/brand/researchershub-mark.svg" alt="ResearchersHub mark" width="88"/>
</p>

---

## Ship in 60 seconds

```powershell
git clone https://github.com/ItsNotAILABS/ResearchersHub.git
cd ResearchersHub
pip install -r requirements-researchers.txt
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

| Surface | URL |
|---------|-----|
| **Desk** | http://127.0.0.1:8787/desk |
| **Identity** | http://127.0.0.1:8787/v1/researchers |
| **Skills** | http://127.0.0.1:8787/v1/researchers/skills |
| **Models** | http://127.0.0.1:8787/v1/researchers/models |
| **Atlas** | http://127.0.0.1:8787/v1/researchers/atlas |
| **Agent tools** | http://127.0.0.1:8787/v1/agents/manifest |
| **Health** | http://127.0.0.1:8787/health |

```powershell
# Edge app (Windows)
.\scripts\Open-ResearchersHub-Edge.cmd
```

---

## Coding agents (Claude, Grok, and everyone else)

ResearchersHub is a **tool host**, not only a human UI.

| Agent | Connect |
|-------|---------|
| **Claude / Claude Code** | MCP + [`CLAUDE.md`](CLAUDE.md) |
| **Grok** | Skill [`skills/researchershub/SKILL.md`](skills/researchershub/SKILL.md) → `~/.grok/skills/` · MCP/REST |
| **Codex** | [`AGENTS.md`](AGENTS.md) + `POST /v1/agents/invoke` |
| **Cursor** | [`.cursorrules`](.cursorrules) + [`.mcp.json`](.mcp.json) |
| **GitHub Copilot** | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| **Gemini / other** | [`GEMINI.md`](GEMINI.md) + REST |

### MCP (one command)

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket mcp
```

### REST invoke (any agent)

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: claude" \
  -d "{\"name\":\"rh_construct\",\"arguments\":{\"prompt\":\"titration curve with full Python\"}}"
```

**Tools:** `rh_identity` · `rh_skills_list` · `rh_skill_get` · `rh_models` · `rh_construct` · `rh_chat` · `rh_atlas_snapshot` · `rh_atlas_export` · `rh_atlas_claim` · `rh_doctrine` · `rh_coding_help`

### CLI

```text
python -m pocket serve
python -m pocket mcp
python -m pocket tools
python -m pocket invoke rh_identity
python -m pocket invoke rh_construct --args "{\"prompt\":\"Michaelis-Menten\"}"
python -m pocket identity
```

### Install local skill mirrors

```powershell
powershell -ExecutionPolicy Bypass -File scripts\Install-Coding-Agents.ps1
```

Deep guide: **[`docs/CODING_AGENTS.md`](docs/CODING_AGENTS.md)** · Shared contract: **[`AGENTS.md`](AGENTS.md)**

---

## One flag — any model

```powershell
$env:RH_MODEL = "claude"     # grok | gpt | codex | deepseek | glm | kimi | finetune | local
$env:ANTHROPIC_API_KEY = "..."   # or XAI_API_KEY / OPENAI_API_KEY / DEEPSEEK_API_KEY / ...

# Fine-tune or private OpenAI-compatible endpoint
$env:RH_MODEL = "finetune"
$env:RH_BASE_URL = "https://your-endpoint/v1"
$env:RH_MODEL_ID = "your-model-id"
$env:RH_API_KEY  = "..."
$env:RH_CHAT_VIA_ROUTER = "1"
```

```http
GET  /v1/researchers/models
POST /v1/researchers/chat
```

---

## 970+ research skills

| Domain | What lives here |
|--------|-----------------|
| **ML / deep learning** | Transformers, RLHF/DPO, RAG, HPO, drift, fairness, deploy |
| **Computational biology** | scRNA, spatial, CRISPR, GWAS, multi-omics |
| **Cheminformatics** | SMILES, QSAR, docking, ADMET, generative molecules |
| **Clinical & stats** | Estimands, survival, adaptive trials, CDISC, KM/forest plots |
| **Materials & physics** | DFT, phonons, battery materials, metrology |
| **Neuroscience · earth · astro** | EEG/fMRI, GIS/climate, photometry |
| **Lab · chemistry · construct** | Kinetics, titration, SOPs, full PNG + Python |
| **Atlas agents** | Shared graph claims, handoffs, repro bundles |

```http
GET /v1/researchers/skills
```

### Editable · extensible

Drop JSON into `skills/`, `~/.researchershub/skills/`, or `$RH_SKILLS_DIR`:

```json
{
  "skills": [
    {
      "id": "custom_lab_assay_template",
      "domain": "custom",
      "desc": "Your assay — edit freely",
      "tags": "custom editable",
      "kind": "playbook"
    }
  ]
}
```

---

## Atlas — many agents, one graph

Shared reproducible research graph on your disk (`~/.researchershub/atlas/` or `$RH_ATLAS_DIR`).

**Nodes:** claim · paper · dataset · experiment · figure · skill · script · hypothesis · molecule · gene · model_run  
**Edges:** supports · refutes · cites · derives · uses_skill · produced_by · replicates

```http
GET  /v1/researchers/atlas
GET  /v1/researchers/atlas/export
POST /v1/researchers/atlas/node
POST /v1/agents/invoke   {"name":"rh_atlas_claim","arguments":{"agent":"grok","title":"…"}}
```

Constructive workflows auto-link **experiment → script → figures**.

---

## Full figures + real Python

```http
POST /v1/researchers/construct
{"prompt":"Plot a dose–response IC50 curve and give the full Python workflow"}
```

You get:

1. **Complete PNG images** (`data:image/png;base64,...`)
2. **Runnable multi-step Python** (simulate → CSV → figure)
3. Files under `~/.researchershub/construct/`
4. Atlas nodes for reproducibility

---

## Doctrine

```text
✓ Any model — one flag (Claude, Grok, GPT, DeepSeek, GLM, Kimi, fine-tune, local)
✓ 970+ research skills — readable, editable, extensible
✓ No throttling · no gatekeeping · no vendor deciding science
✓ Native Atlas — many agents, one shared research graph
✓ MCP + REST — Claude, Grok, Codex, Cursor, Copilot, Gemini
✓ Runs on your infra — your data stays yours
```

`GET /v1/researchers/doctrine`

---

## API map

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/health` | Liveness |
| GET | `/v1/researchers` | Product identity |
| GET | `/v1/researchers/doctrine` | Pillars |
| GET | `/v1/researchers/models` | Active model + providers |
| GET | `/v1/researchers/skills` | Full skill catalog |
| GET | `/v1/researchers/atlas` | Graph snapshot |
| GET | `/v1/researchers/atlas/export` | Full graph JSON |
| POST | `/v1/researchers/atlas/node` | Agent claim |
| POST | `/v1/researchers/construct` | Figures + Python |
| POST | `/v1/researchers/chat` | Model-routed research chat |
| GET | `/v1/agents/manifest` | Coding-agent tool manifest |
| GET | `/v1/agents/tools` | OpenAI + Anthropic schemas |
| POST | `/v1/agents/invoke` | Invoke tool by name |
| GET | `/v1/agents/help?agent=claude` | Per-agent setup |
| POST | `/v1/ai/chat` | Host chat (router optional) |

---

## Architecture

```text
┌──────────────────────────────────────────────────────────────────┐
│                        ResearchersHub                            │
│         Edge desk · agents · phone · API  (POCKET DNA)           │
├────────────────┬─────────────────────┬───────────────────────────┤
│  model_router  │  970+ research      │  Atlas research graph     │
│  RH_MODEL=*    │  skills (editable)  │  many agents → one graph  │
├────────────────┴─────────────────────┴───────────────────────────┤
│  science_construct → full PNG figures + real Python workflows    │
│  agent_bridge + mcp_server → Claude · Grok · Codex · Cursor …    │
│  your keys · your disk · your infra                              │
└──────────────────────────────────────────────────────────────────┘
```

---

## Repo map

| Path | Role |
|------|------|
| `src/pocket/agent_bridge.py` | Tool catalog + invoke |
| `src/pocket/mcp_server.py` | MCP stdio |
| `src/pocket/model_router.py` | Multi-model one flag |
| `src/pocket/science_skills.py` | Skill merge |
| `src/pocket/research_skills_*.py` | Skill packs |
| `src/pocket/science_construct.py` | Charts + Python |
| `src/pocket/atlas_graph.py` | Shared research graph |
| `skills/researchershub/` | Grok/Claude agent skill |
| `AGENTS.md` · `CLAUDE.md` · `.cursorrules` | Coding-agent contracts |
| `docs/CODING_AGENTS.md` | Per-agent setup |
| `docs/brand/` | Logo + wordmark |

---

## Docs (clean set)

| Doc | Purpose |
|-----|---------|
| [PRODUCT.md](PRODUCT.md) | Product definition |
| [SHIP.md](SHIP.md) | Ship checklist |
| [AGENTS.md](AGENTS.md) | All coding agents |
| [docs/CODING_AGENTS.md](docs/CODING_AGENTS.md) | Claude / Grok / Codex / Cursor |
| [docs/API_QUICKSTART.md](docs/API_QUICKSTART.md) | API quickstart |
| [docs/AI_API.md](docs/AI_API.md) | Sellable AI API |
| [docs/SECURITY.md](docs/SECURITY.md) | Security |
| [docs/PRODUCTION.md](docs/PRODUCTION.md) | Production |
| [docs/LINEAGE.md](docs/LINEAGE.md) | Short heritage note |
| [docs/archive/pocket-lineage/](docs/archive/pocket-lineage/) | Historical POCKET papers only |

---

## Brand

| Asset | Path |
|-------|------|
| Mark | [`docs/brand/researchershub-mark.svg`](docs/brand/researchershub-mark.svg) |
| Wordmark | [`docs/brand/researchershub-wordmark.svg`](docs/brand/researchershub-wordmark.svg) |

---

## Project

| | |
|--|--|
| **Org** | [ItsNotAILABS](https://github.com/ItsNotAILABS) |
| **Repo** | [ItsNotAILABS/ResearchersHub](https://github.com/ItsNotAILABS/ResearchersHub) |
| **Lab** | ItsNotAI Labs |
| **Company** | Medina Tech Labs |
| **Version** | **1.2.1** |
| **Lineage** | Host DNA from POCKET — product is ResearchersHub ([docs/LINEAGE.md](docs/LINEAGE.md)) |

Python import path remains `pocket` for host compatibility; the product name is **ResearchersHub**.

---

## License

See [`LICENSE`](LICENSE) and [`LICENSE-RESEARCHER.md`](LICENSE-RESEARCHER.md).

---

<p align="center">
  <sub>Built for scientists who refuse vendor lock-in — and agents that ship real work.</sub><br/>
  <b>ResearchersHub</b> · ItsNotAI Labs · <a href="https://github.com/ItsNotAILABS/ResearchersHub">Ship it</a>
</p>
