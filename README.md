# ResearchersHub

**Sovereign research desk** by [ItsNotAI Labs](https://github.com/ItsNotAILABS) — forked from POCKET, built for scientists.

> Any model. 250+ research skills. Full figures in chat. Atlas research graph. **Your infra — your data.**

[![Org](https://img.shields.io/badge/org-ItsNotAILABS-0b6e4f)](https://github.com/ItsNotAILABS/ResearchersHub)
[![Skills](https://img.shields.io/badge/research%20skills-250%2B-1d4ed8)](.)
[![Models](https://img.shields.io/badge/models-GLM%20%7C%20Kimi%20%7C%20DeepSeek%20%7C%20Claude%20%7C%20GPT%20%7C%20fine--tune-7c3aed)](.)

---

## Doctrine

| Pillar | Meaning |
|--------|---------|
| **Any model** | GLM, Kimi, DeepSeek, Claude, GPT, your fine-tune. Switching is **one flag**. |
| **250+ skills** | ML · comp bio · cheminformatics · chemistry · stats · lab. Readable, editable, extensible. |
| **No gatekeeping** | No platform throttling. No vendor deciding what science is okay. |
| **Native Atlas** | Many agents, **one shared reproducible research graph**. |
| **Your infra** | Runs where you run it. **Your data stays yours.** |

---

## One flag — switch models

```powershell
# pick a provider
$env:RH_MODEL = "deepseek"   # glm | kimi | deepseek | claude | gpt | finetune | local

# keys (your keys, your account)
$env:DEEPSEEK_API_KEY = "..."
# or: GLM_API_KEY / KIMI_API_KEY / ANTHROPIC_API_KEY / OPENAI_API_KEY / RH_API_KEY

# optional overrides (fine-tunes, vLLM, Ollama, Azure OpenAI-compatible, …)
$env:RH_BASE_URL = "https://your-endpoint/v1"
$env:RH_MODEL_ID = "your-model-or-ft-id"
$env:RH_API_KEY  = "..."

# force /v1/ai/chat through the router
$env:RH_CHAT_VIA_ROUTER = "1"
```

```http
GET  /v1/researchers/models
POST /v1/researchers/chat   {"messages":[...], "model":"kimi"}
```

---

## 250+ research skills

Domains: **ML**, **computational biology**, **cheminformatics**, chemistry, biology, physics, data, literature, lab, construct, research ops.

```http
GET /v1/researchers/skills
```

### Editable / extensible

Drop JSON (or YAML if PyYAML installed) into:

- `skills/` (repo)
- `~/.researchershub/skills/`
- `$RH_SKILLS_DIR`

```json
{
  "skills": [
    {
      "id": "custom_lab_assay_template",
      "domain": "custom",
      "desc": "Your lab assay — edit freely",
      "tags": "custom editable",
      "kind": "playbook"
    }
  ]
}
```

---

## Atlas — shared research graph

Many agents write **one** graph on your disk (`~/.researchershub/atlas/` or `$RH_ATLAS_DIR`).

Nodes: claim · paper · dataset · experiment · figure · skill · agent · script · hypothesis · molecule · gene · model_run …  
Edges: supports · cites · derives · uses_skill · produced_by · replicates …

```http
GET  /v1/researchers/atlas
GET  /v1/researchers/atlas/export
POST /v1/researchers/atlas/node
     {"agent":"chemist","title":"IC50 claim","kind":"claim","body":"..."}
```

Constructive workflows auto-link **experiment → script → figures** into Atlas.

---

## Chat returns whole figures + real Python

```http
POST /v1/researchers/construct
{"prompt":"Plot a titration curve and give the Python workflow"}
```

Replies include:

1. Full PNG images (`data:image/png;base64,...`)
2. Complete runnable Python scripts  
3. Paths under `~/.researchershub/construct/`

---

## Quick start

```powershell
git clone https://github.com/ItsNotAILABS/ResearchersHub.git
cd ResearchersHub
pip install -r requirements-researchers.txt
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

Desk: http://127.0.0.1:8787/desk  
Identity: http://127.0.0.1:8787/v1/researchers  

---

## API map

| Path | Purpose |
|------|---------|
| `GET /v1/researchers` | Product identity + doctrine |
| `GET /v1/researchers/doctrine` | Pillars only |
| `GET /v1/researchers/models` | Active model + providers |
| `GET /v1/researchers/skills` | Full skill catalog |
| `GET /v1/researchers/atlas` | Graph snapshot |
| `GET /v1/researchers/atlas/export` | Full graph JSON |
| `POST /v1/researchers/atlas/node` | Agent claim into graph |
| `POST /v1/researchers/construct` | Figures + Python workflow |
| `POST /v1/researchers/chat` | Model-routed research chat |
| `POST /v1/ai/chat` | Host chat (router when `RH_CHAT_VIA_ROUTER=1`) |

---

## Org

- **GitHub:** https://github.com/ItsNotAILABS/ResearchersHub  
- **Lab:** ItsNotAI Labs  
- **Lineage:** POCKET multi-agent host  

Python import path remains `pocket` for host compatibility; product name is **ResearchersHub**.

## License

See `LICENSE` and `LICENSE-RESEARCHER.md`.
