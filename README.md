<p align="center">
  <img src="docs/brand/researchershub-wordmark.svg" alt="ResearchersHub" width="540"/>
</p>

<p align="center">
  <strong>Your local research server</strong> — skills, real charts, real Python, on your machine.<br/>
  Humans use a desk in the browser. Coding agents call the same host with tools.
</p>

<p align="center">
  <a href="https://github.com/ItsNotAILABS/ResearchersHub"><img alt="GitHub" src="https://img.shields.io/badge/ItsNotAILABS%2FResearchersHub-0b6e4f?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="docs/HOW_TO_USE.md"><img alt="How to use" src="https://img.shields.io/badge/start-HOW%20TO%20USE-1d4ed8?style=for-the-badge"/></a>
  <a href="skills/"><img alt="Skills" src="https://img.shields.io/badge/skills-971%20JSON-0ea5e9?style=for-the-badge"/></a>
</p>

<p align="center">
  <img alt="Local" src="https://img.shields.io/badge/runs-on%20your%20infra-f59e0b?style=flat-square"/>
  <img alt="Figures" src="https://img.shields.io/badge/figures-full%20PNG%20%2B%20Python-10b981?style=flat-square"/>
  <img alt="Agents" src="https://img.shields.io/badge/agents-MCP%20%2B%20REST-a855f7?style=flat-square"/>
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white"/>
</p>

---

## Read this first (so the repo makes sense)

| Question | Answer |
|----------|--------|
| **What is it?** | A **program you run locally** — not a SaaS you only visit |
| **Who is it for?** | Scientists **and** people whose coding agents help with research |
| **What do I see on GitHub?** | Product docs, **971 skills as JSON**, example graphs, source code |
| **What do I see when running?** | Browser desk at `http://127.0.0.1:8787/desk` + files under `~/.researchershub/` |
| **How do agents use it?** | They call **tools** on that same host (MCP or HTTP) — same charts/skills |
| **What happens when I ask for a plot?** | Host simulates → draws PNG → writes Python → returns both (design v2) |

**Full plain-language guide:** **[docs/HOW_TO_USE.md](docs/HOW_TO_USE.md)**

```mermaid
flowchart TB
  subgraph GitHub["What you see on GitHub"]
    R[README + docs]
    S[skills/ 971 JSON files]
    A[docs/assets example graphs]
    C[src runtime code]
  end
  subgraph Run["What you run on your PC"]
    H[Host on port 8787]
    D[Browser desk]
    T[Agent tools MCP/REST]
    Disk["~/.researchershub figures + atlas"]
  end
  GitHub -->|clone + start| H
  H --> D
  H --> T
  H --> Disk
  D -->|ask for chart| H
  T -->|rh_construct| H
```

---

## 60-second start (human)

```powershell
git clone https://github.com/ItsNotAILABS/ResearchersHub.git
cd ResearchersHub
pip install -r requirements-researchers.txt
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 127.0.0.1 --port 8787
```

Open: **http://127.0.0.1:8787/desk**

> Note: commands say `python -m pocket` because the **package folder** is `src/pocket` (legacy name).  
> The **product name** is always **ResearchersHub**.

One figure with no UI:

```powershell
curl -s -X POST http://127.0.0.1:8787/v1/researchers/construct `
  -H "content-type: application/json" `
  -d "{\"prompt\":\"titration curve\"}"
```

---

## What happens when you ask for a graph

```mermaid
sequenceDiagram
  participant You as You or coding agent
  participant Host as ResearchersHub host
  participant Sim as Simulation + design v2
  participant Disk as Your disk

  You->>Host: "titration curve" / rh_construct
  Host->>Sim: match workflow + compute series
  Sim->>Sim: draw publication PNG
  Sim->>Disk: save .py + .png
  Host->>Disk: optional Atlas link
  Host-->>You: full image + full Python + steps
```

| Step | Result |
|------|--------|
| 1 | Intent matched (titration, IC50, SIR, workflow name, …) |
| 2 | Numbers simulated on **your** machine |
| 3 | Figure drawn with **design system v2** (branded, annotated) |
| 4 | Script + PNG written under `~/.researchershub/construct/` |
| 5 | Reply includes **whole PNG** + **runnable Python** (not a stub) |

---

## How coding agents use it

Agents talk to the **same host** you started. They never need a special “Grok folder” in the public repo.

| Method | How |
|--------|-----|
| **REST** | `POST http://127.0.0.1:8787/v1/agents/invoke` with `{"name":"rh_construct","arguments":{"prompt":"…"}}` |
| **MCP** | `python -m pocket mcp` then use tools `rh_*` |
| **List skills** | tool `rh_skills_list` or `GET /v1/researchers/skills` |
| **Record result** | tool `rh_atlas_claim` |

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: my-agent" \
  -d "{\"name\":\"rh_construct\",\"arguments\":{\"prompt\":\"dose-response IC50\"}}"
```

**Agent gets back:** markdown + base64 PNGs + full Python + workflow steps.  
**Human sees:** whatever the agent UI shows (chat with image + code).

Optional IDE notes only: [docs/developers/](docs/developers/) · contract: [AGENTS.md](AGENTS.md)

---

## What’s in this repository (files that make sense)

**Full map:** **[FILES.md](FILES.md)**

| Path | Purpose |
|------|---------|
| **[FILES.md](FILES.md)** | **Every folder explained** |
| **[docs/HOW_TO_USE.md](docs/HOW_TO_USE.md)** | What you see / what agents do / what happens |
| **[skills/](skills/)** | **971 research skills as JSON** |
| **[docs/assets/](docs/assets/)** | Example graphs from the engine |
| **[src/](src/)** | Runtime (`python -m pocket serve`) — see `src/README.md` |
| **[scripts/](scripts/)** | Start host / open desk / export skills |
| **[scripts/legacy/](scripts/legacy/)** | Old host scripts — **ignore** |
| **[optional/](optional/)** | Electron / vendor extras — **not required** |
| **[docs/archive/](docs/archive/)** | Historical papers — **not current product** |

There is **no** public `.grok` folder. Private AI-tool config stays on your machine only.

---

## Skills (yes — they are here)

| File | What you open on GitHub |
|------|-------------------------|
| [skills/CATALOG.json](skills/CATALOG.json) | Counts by domain |
| [skills/INDEX.json](skills/INDEX.json) | Every skill id + description |
| [skills/catalog/](skills/catalog/) | Full domain packs (ml, compbio, cheminformatics, …) |

```http
GET /v1/researchers/skills
```

---

## Use cases

| Who | They do this | They get |
|-----|--------------|----------|
| Chemist | Ask titration / Arrhenius / spectrum | Full curve + Python |
| Biochem / pharma | IC50, Michaelis–Menten, binding | Annotated plots + scripts |
| Comp bio / omics | Volcano, PCA-style map, skill checklists | Figures + skill JSON |
| ML / stats | Regression residuals, distributions | Dual-panel diagnostics |
| Lab lead | Multi-step workflows (`pk_pd_panel`, …) | Bundled figure sets |
| Coding agent | `rh_construct` / `rh_skills_list` | Same artifacts via tools |

Named workflows: `GET /v1/researchers/workflows`  
Examples: `assay_standard_curve`, `pk_pd_panel`, `epidemic_scenario`, `omics_hits`, `full_methods_bundle`, …

---

## Example figures (from the live engine)

<p align="center">
  <img src="docs/assets/titration_curve.png" alt="Titration" width="400"/>
  <img src="docs/assets/michaelis_menten.png" alt="Michaelis–Menten" width="400"/>
</p>
<p align="center">
  <img src="docs/assets/dose_response.png" alt="Dose–response" width="400"/>
  <img src="docs/assets/sir_epidemic.png" alt="SIR" width="400"/>
</p>
<p align="center">
  <img src="docs/assets/volcano.png" alt="Volcano" width="400"/>
  <img src="docs/assets/lotka_volterra.png" alt="Lotka–Volterra" width="400"/>
</p>

---

## Architecture (runtime)

```mermaid
flowchart LR
  Human[Human desk] --> Host[Host :8787]
  Agent[Coding agent] --> Host
  Host --> Skills[skills JSON + Python]
  Host --> Construct[Construct design v2]
  Host --> Atlas[Atlas graph]
  Construct --> Disk[(~/.researchershub)]
  Atlas --> Disk
  Host --> Models[Optional RH_MODEL cloud/local LLM]
```

Optional models (`RH_MODEL=claude|grok|gpt|…`) need **your** API keys.  
Charts and simulations work **without** any cloud model.

---

## API cheat sheet

| Call | Purpose |
|------|---------|
| `GET /health` | Is host up? |
| `GET /v1/researchers` | Product identity |
| `GET /v1/researchers/skills` | Skill catalog |
| `GET /v1/researchers/workflows` | Named multi-step workflows |
| `POST /v1/researchers/construct` | Figures + Python |
| `GET /v1/agents/manifest` | Tool list for agents |
| `POST /v1/agents/invoke` | Run a tool by name |

More: [docs/API_QUICKSTART.md](docs/API_QUICKSTART.md)

---

## Docs map

| Doc | For |
|-----|-----|
| **[FILES.md](FILES.md)** | **File/folder map** |
| **[docs/HOW_TO_USE.md](docs/HOW_TO_USE.md)** | What you see & what happens |
| [PRODUCT.md](PRODUCT.md) | Product definition |
| [docs/REPO_LAYOUT.md](docs/REPO_LAYOUT.md) | Layout rules |
| [docs/CODING_AGENTS.md](docs/CODING_AGENTS.md) | Agent integration |
| [docs/SECURITY.md](docs/SECURITY.md) | Security |
| [SHIP.md](SHIP.md) | Ship checklist |

---

## Project

| | |
|--|--|
| **Org** | [ItsNotAILABS](https://github.com/ItsNotAILABS) |
| **Repo** | [ItsNotAILABS/ResearchersHub](https://github.com/ItsNotAILABS/ResearchersHub) |
| **Lab** | ItsNotAI Labs |
| **Version** | 1.2.1 |

<p align="center">
  <sub>ResearchersHub · your infra · your data · real figures</sub>
</p>
