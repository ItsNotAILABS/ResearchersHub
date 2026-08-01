<p align="center">
  <img src="docs/brand/researchershub-wordmark.svg" alt="ResearchersHub" width="520"/>
</p>

<p align="center">
  <strong>Sovereign research desk for scientists</strong><br/>
  Any model · 750+ research skills · Atlas graph · Your infra — your data
</p>

<p align="center">
  <a href="https://github.com/ItsNotAILABS/ResearchersHub"><img alt="GitHub org" src="https://img.shields.io/badge/org-ItsNotAILABS-0b6e4f?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="https://github.com/ItsNotAILABS/ResearchersHub/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/ItsNotAILABS/ResearchersHub?style=for-the-badge&logo=github&color=1d4ed8"/></a>
  <a href="https://github.com/ItsNotAILABS/ResearchersHub/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-see%20repo-64748b?style=for-the-badge"/></a>
</p>

<p align="center">
  <img alt="Skills 750+" src="https://img.shields.io/badge/research%20skills-750%2B-0ea5e9?style=flat-square"/>
  <img alt="Models" src="https://img.shields.io/badge/models-GLM%20%7C%20Kimi%20%7C%20DeepSeek%20%7C%20Claude%20%7C%20GPT%20%7C%20fine--tune-8b5cf6?style=flat-square"/>
  <img alt="Atlas" src="https://img.shields.io/badge/Atlas-shared%20research%20graph-10b981?style=flat-square"/>
  <img alt="No gatekeeping" src="https://img.shields.io/badge/gatekeeping-none-22c55e?style=flat-square"/>
  <img alt="Sovereignty" src="https://img.shields.io/badge/data-stays%20on%20your%20infra-f59e0b?style=flat-square"/>
  <img alt="Lineage" src="https://img.shields.io/badge/lineage-POCKET-6366f1?style=flat-square"/>
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img alt="Version" src="https://img.shields.io/badge/version-1.2.0-0b6e4f?style=flat-square"/>
</p>

---

## Why ResearchersHub

Most AI research tools force you into **one vendor**, **throttled APIs**, and **opaque skills**.  
ResearchersHub is the opposite:

| | |
|--|--|
| **Any model** | GLM · Kimi · DeepSeek · Claude · GPT · your fine-tune — switch with **one flag** |
| **750+ skills** | ML · comp bio · cheminformatics · clinical · materials · neuroscience · earth · more |
| **Editable** | Skills are plain JSON/Python — readable, forkable, extensible |
| **No gatekeeping** | No platform throttle deciding what science is “allowed” |
| **Native Atlas** | Many agents, **one shared reproducible research graph** |
| **Your infra** | Runs where you run it. **Your data stays yours.** |

Built from the **POCKET** multi-agent host lineage — Edge desk, agents, phone, sellable API — re-aimed at real lab and literature work.

<p align="center">
  <img src="docs/brand/researchershub-mark.svg" alt="ResearchersHub mark" width="96"/>
</p>

---

## Quick start

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

---

## Coding agents — Claude, Grok, Codex, Cursor, Copilot, Gemini

ResearchersHub is a **first-class tool host** for coding agents, not only a human desk.

<p align="center">
  <img alt="Claude" src="https://img.shields.io/badge/Claude-MCP%20%2B%20CLAUDE.md-d97706?style=flat-square"/>
  <img alt="Grok" src="https://img.shields.io/badge/Grok-skill%20%2B%20tools-06b6d4?style=flat-square"/>
  <img alt="Codex" src="https://img.shields.io/badge/Codex-AGENTS.md%20%2B%20REST-22c55e?style=flat-square"/>
  <img alt="Cursor" src="https://img.shields.io/badge/Cursor-.cursorrules%20%2B%20MCP-0ea5e9?style=flat-square"/>
  <img alt="Copilot" src="https://img.shields.io/badge/Copilot-instructions-6366f1?style=flat-square"/>
  <img alt="Gemini" src="https://img.shields.io/badge/Gemini-GEMINI.md-4285F4?style=flat-square"/>
</p>

| Agent | How to connect |
|-------|----------------|
| **Claude / Claude Code** | MCP `python -m pocket mcp` + root [`CLAUDE.md`](CLAUDE.md) |
| **Grok** | Skill [`skills/researchershub/SKILL.md`](skills/researchershub/SKILL.md) → `~/.grok/skills/` · or MCP |
| **Codex** | [`AGENTS.md`](AGENTS.md) + `POST /v1/agents/invoke` |
| **Cursor** | [`.cursorrules`](.cursorrules) + MCP (same command) |
| **GitHub Copilot** | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| **Gemini / others** | [`GEMINI.md`](GEMINI.md) + REST tools |

### MCP (one command)

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket mcp
```

Or use repo [`.mcp.json`](.mcp.json). Deep guide: [`docs/CODING_AGENTS.md`](docs/CODING_AGENTS.md)

### REST invoke (any agent)

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: claude" \
  -d "{\"name\":\"rh_construct\",\"arguments\":{\"prompt\":\"titration curve\"}}"
```

**Tools:** `rh_identity` · `rh_skills_list` · `rh_construct` · `rh_chat` · `rh_atlas_claim` · `rh_models` · …

```powershell
# Install Grok + Claude skill mirrors on this machine
powershell -ExecutionPolicy Bypass -File scripts\Install-Coding-Agents.ps1
```

---

## One flag — any model

```powershell
$env:RH_MODEL = "deepseek"   # glm | kimi | deepseek | claude | gpt | finetune | local
$env:DEEPSEEK_API_KEY = "sk-..."

# Your fine-tune / vLLM / Ollama / private gateway
$env:RH_MODEL = "finetune"
$env:RH_BASE_URL = "https://your-endpoint/v1"
$env:RH_MODEL_ID = "your-model-id"
$env:RH_API_KEY  = "..."

# Force host chat through the router
$env:RH_CHAT_VIA_ROUTER = "1"
```

```http
GET  /v1/researchers/models
POST /v1/researchers/chat
Content-Type: application/json

{"messages":[{"role":"user","content":"Design a QSAR workflow with full Python"}],"model":"kimi"}
```

---

## 750+ research skills

Skills span the real research stack — not a toy checklist.

| Domain | Examples |
|--------|----------|
| **ML / deep learning** | Transformers, RLHF/DPO, RAG eval, HPO, drift, fairness, deploy |
| **Computational biology** | scRNA, spatial, CRISPR, GWAS, multi-omics, FAIR genomics |
| **Cheminformatics** | SMILES, QSAR, docking, ADMET, retrosynthesis, generative mol |
| **Clinical & stats** | Estimands, survival, adaptive trials, CDISC, forest/KM plots |
| **Materials & physics** | DFT, phonons, battery materials, FEA, metrology |
| **Neuroscience** | EEG/fMRI, BIDS, connectivity, BCI |
| **Earth & climate** | GIS, NDVI, extremes, carbon budgets |
| **Lab · chemistry · construct** | Kinetics, titration charts, SOPs, full PNG figures + Python |
| **Atlas agents** | Shared graph claims, handoffs, repro bundles |

```http
GET /v1/researchers/skills
```

### Editable · extensible

Drop skills into:

- `skills/` (this repo)
- `~/.researchershub/skills/`
- `$RH_SKILLS_DIR`

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

All agents write a **shared reproducible research graph** on your disk  
(`~/.researchershub/atlas/` or `$RH_ATLAS_DIR`).

**Nodes:** claim · paper · dataset · experiment · figure · skill · script · hypothesis · molecule · gene · model_run …  
**Edges:** supports · refutes · cites · derives · uses_skill · produced_by · replicates …

```http
GET  /v1/researchers/atlas
GET  /v1/researchers/atlas/export
POST /v1/researchers/atlas/node
```

Constructive workflows auto-link **experiment → script → figures**.

---

## Full figures + real Python in chat

Ask for a titration curve, dose–response, enzyme kinetics, regression…  
Replies include:

1. **Complete PNG charts** (embedded `data:image/png;base64,...`)
2. **Runnable Python** multi-step workflows  
3. Files under `~/.researchershub/construct/`

```http
POST /v1/researchers/construct
{"prompt":"Plot a Michaelis–Menten curve and give the full Python workflow"}
```

---

## Doctrine

```text
✓ Any model — one flag
✓ 750+ research skills — readable, editable, extensible
✓ No throttling · no gatekeeping · no vendor deciding science
✓ Native Atlas — many agents, one shared research graph
✓ Runs on your infra — your data stays yours
```

`GET /v1/researchers/doctrine`

---

## API map

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/v1/researchers` | Product identity |
| GET | `/v1/researchers/doctrine` | Pillars |
| GET | `/v1/researchers/models` | Active model + providers |
| GET | `/v1/researchers/skills` | Full skill catalog |
| GET | `/v1/researchers/atlas` | Graph snapshot |
| GET | `/v1/researchers/atlas/export` | Full graph JSON |
| POST | `/v1/researchers/atlas/node` | Agent claim |
| POST | `/v1/researchers/construct` | Figures + Python |
| POST | `/v1/researchers/chat` | Model-routed chat |
| GET | `/v1/agents/manifest` | **Coding-agent tool manifest** |
| GET | `/v1/agents/tools` | OpenAI + Anthropic tool schemas |
| POST | `/v1/agents/invoke` | **Invoke tool by name** |
| GET | `/v1/agents/help?agent=claude` | Per-agent setup |
| POST | `/v1/ai/chat` | Host chat (router optional) |
| GET | `/health` | Liveness |

---

## Architecture (simple)

```text
┌─────────────────────────────────────────────────────────┐
│                     ResearchersHub                      │
│  Edge desk · agents · phone · sellable API (POCKET DNA) │
├──────────────┬──────────────────┬───────────────────────┤
│ model_router │  750+ skills     │  Atlas research graph │
│ RH_MODEL=*   │  ML·bio·chem…    │  nodes + edges        │
├──────────────┴──────────────────┴───────────────────────┤
│ science_construct → full PNG figures + real Python      │
│ your keys · your disk · your infra                      │
└─────────────────────────────────────────────────────────┘
```

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
| **Version** | 1.2.0 |
| **Lineage** | POCKET multi-agent host |

Python import path remains `pocket` for host compatibility; the product name is **ResearchersHub**.

---

## License

See [`LICENSE`](LICENSE) and [`LICENSE-RESEARCHER.md`](LICENSE-RESEARCHER.md).

---

<p align="center">
  <sub>Built for scientists who refuse vendor lock-in.</sub><br/>
  <b>ResearchersHub</b> · ItsNotAI Labs
</p>
