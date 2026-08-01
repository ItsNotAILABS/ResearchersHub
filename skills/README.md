# Research skills catalog

**971** skills ship in this folder as readable JSON.

Before this export, skills lived only inside Python modules — so GitHub looked empty.
They are now public and editable here.

| File | Purpose |
|------|---------|
| [CATALOG.json](CATALOG.json) | Counts by domain |
| [INDEX.json](INDEX.json) | All skill ids + one-line descriptions |
| [catalog/](catalog/) | Full skill objects per domain |
| [example_custom.json](example_custom.json) | Template for your own skills |
| [researchershub/SKILL.md](researchershub/SKILL.md) | Optional coding-agent how-to |

## Domains

| Domain | Count | File |
|--------|------:|------|
| `ml` | 203 | [catalog/ml.json](catalog/ml.json) |
| `cheminformatics` | 163 | [catalog/cheminformatics.json](catalog/cheminformatics.json) |
| `compbio` | 146 | [catalog/compbio.json](catalog/compbio.json) |
| `clinical` | 73 | [catalog/clinical.json](catalog/clinical.json) |
| `materials` | 50 | [catalog/materials.json](catalog/materials.json) |
| `chemistry` | 40 | [catalog/chemistry.json](catalog/chemistry.json) |
| `comms` | 30 | [catalog/comms.json](catalog/comms.json) |
| `data_platform` | 30 | [catalog/data_platform.json](catalog/data_platform.json) |
| `research_ops` | 30 | [catalog/research_ops.json](catalog/research_ops.json) |
| `atlas` | 25 | [catalog/atlas.json](catalog/atlas.json) |
| `biology` | 20 | [catalog/biology.json](catalog/biology.json) |
| `data` | 20 | [catalog/data.json](catalog/data.json) |
| `earth` | 20 | [catalog/earth.json](catalog/earth.json) |
| `engineering` | 20 | [catalog/engineering.json](catalog/engineering.json) |
| `neuroscience` | 20 | [catalog/neuroscience.json](catalog/neuroscience.json) |
| `astro` | 15 | [catalog/astro.json](catalog/astro.json) |
| `physics` | 15 | [catalog/physics.json](catalog/physics.json) |
| `theory` | 15 | [catalog/theory.json](catalog/theory.json) |
| `construct` | 10 | [catalog/construct.json](catalog/construct.json) |
| `literature` | 10 | [catalog/literature.json](catalog/literature.json) |
| `web` | 8 | [catalog/web.json](catalog/web.json) |
| `lab` | 7 | [catalog/lab.json](catalog/lab.json) |
| `custom` | 1 | [catalog/custom.json](catalog/custom.json) |

## How skills load at runtime

1. Built-in Python packs: `src/pocket/science_skills.py`, `research_skills_ext.py`, `research_skills_mega.py`
2. JSON in this folder (`catalog/*.json` and extra packs you add)
3. Operator machine: `~/.researchershub/skills/` or `$RH_SKILLS_DIR`

API: `GET /v1/researchers/skills`

Regenerate this export after editing Python packs:

```powershell
python scripts/export_skills_catalog.py
```

