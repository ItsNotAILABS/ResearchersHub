# Files & folders — what everything is

If the repo felt confusing, start here.  
**Bold** paths are what most people need.

---

## Root (open these first)

| File | Purpose |
|------|---------|
| **[README.md](README.md)** | Product home page |
| **[docs/HOW_TO_USE.md](docs/HOW_TO_USE.md)** | How humans + agents use it, what happens |
| **[PRODUCT.md](PRODUCT.md)** | One-page product definition |
| **[skills/](skills/)** | **971 research skills as JSON** (the catalog you can browse) |
| **[docs/assets/](docs/assets/)** | Example graphs the app generates |
| [SHIP.md](SHIP.md) | Ship checklist |
| [AGENTS.md](AGENTS.md) | Optional coding-agent contract |
| [requirements-researchers.txt](requirements-researchers.txt) | `pip install -r …` |
| [LICENSE](LICENSE) / [LICENSE-RESEARCHER.md](LICENSE-RESEARCHER.md) | License |

---

## Core product code

| Path | Purpose |
|------|---------|
| **`src/pocket/`** | Runtime package you run with `python -m pocket serve` |
| `src/README.md` | Why the folder is named `pocket` (product is still ResearchersHub) |

Important modules inside `src/pocket/`:

| Module | Does |
|--------|------|
| `server.py` | HTTP host (desk + API) |
| `science_construct.py` | Charts / simulations / workflows |
| `science_render.py` | Figure design system |
| `science_skills.py` + `research_skills_*.py` | Skill definitions (also exported to `skills/`) |
| `atlas_graph.py` | Shared research graph on disk |
| `model_router.py` | Multi-model flag `RH_MODEL` |
| `agent_bridge.py` / `mcp_server.py` | Tools for coding agents |
| `cli_main.py` | `python -m pocket serve \| mcp \| tools \| invoke` |

---

## Skills (public, readable)

| Path | Purpose |
|------|---------|
| **`skills/INDEX.json`** | All skill ids + descriptions |
| **`skills/CATALOG.json`** | Counts by domain |
| **`skills/catalog/*.json`** | Full skills per domain (ml, compbio, …) |
| `skills/README.md` | Catalog index |
| `skills/example_custom.json` | Template to add your own |
| `skills/researchershub/SKILL.md` | Optional agent how-to |

---

## Docs

| Path | Purpose |
|------|---------|
| **`docs/HOW_TO_USE.md`** | Start here for “what do I see / what happens” |
| `docs/API_QUICKSTART.md` | HTTP cheat sheet |
| `docs/REPO_LAYOUT.md` | Layout rules |
| `docs/CODING_AGENTS.md` | Agent integration |
| `docs/developers/` | Optional IDE notes (not the product core) |
| `docs/assets/` | Example PNGs |
| `docs/brand/` | Logo / wordmark |
| `docs/archive/` | **Historical host papers only** — not current product |

---

## Scripts (public entrypoints only)

| Path | Purpose |
|------|---------|
| **`scripts/Start-ResearchersHub.ps1`** | Start the host |
| **`scripts/Open-ResearchersHub-Edge.cmd`** | Open Edge app → desk |
| `scripts/export_skills_catalog.py` | Rebuild `skills/*.json` from Python |
| `scripts/Install-Coding-Agents.ps1` | Optional local agent skill mirrors |
| `scripts/Setup-Cloudflare-Named-Tunnel.ps1` | Optional public tunnel |
| `scripts/Start-Cloudflare-Named.ps1` | Run tunnel |
| `scripts/smoke-product.ps1` | Quick smoke check |
| `scripts/legacy/` | **Old host scripts (POCKET names)** — ignore unless you need them |

---

## Optional (not required to understand or run the product)

| Path | Purpose |
|------|---------|
| `optional/desktop-electron/` | Electron shell experiment |
| `optional/vendor/` | Bundled third-party experiments |
| `optional/releases/` | Desktop release metadata |
| `optional/web/` | Extra web scaffold |

See [optional/README.md](optional/README.md).

---

## What is *not* in the public tree

| Local only (gitignored) | Why |
|-------------------------|-----|
| `.grok/`, `.cursor/`, `.claude/` | Private AI-tool config |
| `~/.researchershub/` | Your figures, atlas, custom skills |
| Secrets / `access.env` | Never commit |

---

## Mental model

```text
GitHub (this repo)
  skills/     → browse 971 skills
  docs/       → how to use + examples
  src/pocket/ → run the server
  scripts/    → start host / open desk

Your PC (after you run it)
  host :8787
  ~/.researchershub/construct/  → PNGs + Python
  ~/.researchershub/atlas/      → research graph
```
