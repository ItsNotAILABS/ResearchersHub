# ResearchersHub

**Sovereign research desk for scientists** — forked from [POCKET](https://github.com/FreddyCreates/pocket), tailored for real lab and literature work.

> Chemistry · biology · physics · materials · stats · ELN · literature  
> **100+ preloaded science skills** · chats return **whole images & charts** · **real Python constructive workflows**

[![Product](https://img.shields.io/badge/product-ResearchersHub-0b6e4f)](.)
[![Skills](https://img.shields.io/badge/science%20skills-100%2B-1d4ed8)](.)
[![Lineage](https://img.shields.io/badge/lineage-POCKET-7c3aed)](.)

---

## Why ResearchersHub

POCKET is a general multi-agent host co-pilot. **ResearchersHub** keeps that DNA (Edge desk, agents, phone, sellable API) and re-aims it at **scientists and researchers**:

| Capability | What you get |
|------------|----------------|
| **Science skills** | 100+ preloaded skills — advanced chemistry, wet lab, kinetics, spectroscopy, stats, arXiv/PubMed planning, lab SOPs |
| **Full figures in chat** | Matplotlib charts returned as **complete PNG images** embedded in the reply (not placeholders) |
| **Constructive Python** | Real multi-step scripts: simulate → CSV → figure; saved under `~/.researchershub/construct/` |
| **Host power** | Local desk, agents, Infinite Wiki, swarm lineage from POCKET |

---

## Quick start

```powershell
cd ResearchersHub
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

Open: [http://127.0.0.1:8787/desk](http://127.0.0.1:8787/desk)

### Science API (no heavy auth for catalog/health)

```http
GET  /health
GET  /v1/researchers
GET  /v1/researchers/skills
GET  /v1/researchers/board          # multi-figure PNG board
POST /v1/researchers/construct      # {"prompt":"titration curve"}
POST /v1/ai/chat                    # science-enriched completions
```

### Chat with full chart + script

```bash
curl -s http://127.0.0.1:8787/v1/ai/chat ^
  -H "Content-Type: application/json" ^
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"Plot a titration curve and give me the Python workflow\"}],\"agent\":\"researcher\"}"
```

Reply includes:

1. **Full markdown images** (`![](data:image/png;base64,...)`)
2. **Complete Python script** in a fenced block
3. Script path on disk under `~/.researchershub/construct/`

---

## Skill domains (100+)

- **Chemistry** — stoichiometry, equilibrium, kinetics, thermo, acid–base, titration charts, redox, spectroscopy (UV-Vis, IR, NMR, MS, XRD), organic mechanisms, green metrics, DFT outline, SMILES…
- **Biology** — PCR, gels, Western, ELISA curves, enzyme kinetics, dose–response / IC50, RNA-seq pipeline skeleton, CRISPR checklist…
- **Physics / materials** — kinematics plots, Arrhenius, stress–strain, diffusion, band gap notes…
- **Data** — t-tests, ANOVA, regression, PCA, ROC, Kaplan–Meier, heatmaps, publication figure settings…
- **Literature / lab** — arXiv, PubMed, PRISMA, BibTeX, ELN entries, SOPs, reagent calc, PubChem/ChEMBL/PDB/NIST openers…
- **Construct** — matplotlib charts, multi-panel figures, repro bundles, simulation loops…

List live: `GET /v1/researchers/skills`

---

## Product identity

```text
Name:     ResearchersHub
Version:  1.0.0
Lineage:  POCKET multi-agent host
Lab:      ItsNotAI Labs
Company:  Medina Tech Labs
```

Python package import path remains `pocket` for compatibility with the host stack; product branding is **ResearchersHub**.

---

## License

See `LICENSE` and `LICENSE-RESEARCHER.md` (researcher license lineage from POCKET).

---

## Relation to POCKET

ResearchersHub is a **whole-product copy** of the POCKET host, specialized for research:

- New modules: `science_skills.py`, `science_construct.py`, `researchers_hub.py`
- Chat path (`/v1/ai/chat`) enriches science prompts with **full figures + scripts**
- Skill suite merges science pack **before** general host skills

Upstream POCKET: https://github.com/FreddyCreates/pocket
