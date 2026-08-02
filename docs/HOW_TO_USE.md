# How to use ResearchersHub

Plain language. Three audiences. One product.

---

## 1. What is this?

**ResearchersHub** is software you run **on your own computer** (or lab server).

It is **not** a website you log into on someone else’s cloud as the main product.  
You start a **local host**. Then:

- **You** open a browser desk, **or**
- **Your coding agent** (Claude, Cursor, Codex, etc.) calls tools on that host

It helps with research work: skills catalogs, charts/simulations, real Python scripts, and a shared “Atlas” graph of experiments/figures on **your disk**.

---

## 2. What do people see?

### A. Scientist (human)

| Step | What you do | What you see |
|------|-------------|--------------|
| 1 | Clone repo, install deps, start host | Terminal: server on port **8787** |
| 2 | Open **http://127.0.0.1:8787/desk** | Web desk UI (chat / research surface) |
| 3 | Ask for a chart or workflow | Full **PNG figures** + **Python code** in the reply |
| 4 | Look on disk | Files under `~/.researchershub/construct/` (scripts + PNGs) |
| 5 | Optional | Atlas graph under `~/.researchershub/atlas/` (experiments linked to figures) |

**Browse the repo on GitHub**

| Folder | What a visitor understands |
|--------|----------------------------|
| `README.md` | What the product is |
| `skills/` | **971 research skills** as JSON (catalog by domain) |
| `docs/assets/` | Example graphs the engine already made |
| `docs/` | How-to, API, security |
| `src/pocket/` | Runtime code (folder name is historical; product is ResearchersHub) |
| `scripts/` | Start / export helpers |

### B. Coding agent (Claude, Cursor, Codex, …)

The agent does **not** need the desk UI.

| Step | What happens |
|------|----------------|
| 1 | Host is running on `127.0.0.1:8787` |
| 2 | Agent loads tools via **MCP** (`python -m pocket mcp`) or **REST** (`POST /v1/agents/invoke`) |
| 3 | Agent calls e.g. `rh_construct` with prompt `"titration curve"` |
| 4 | Host returns JSON: markdown, **base64 PNGs**, Python script, paths, workflow steps |
| 5 | Agent shows that to the human, or saves the script |

Optional setup notes (not required to understand the product): [`developers/`](developers/).

### C. You only reading GitHub

You can understand the product **without running anything**:

1. Read this page + [README](../README.md)
2. Open [skills/INDEX.json](../skills/INDEX.json) — list of skills
3. Open [docs/assets/](assets/) — example figures
4. Skim [API_QUICKSTART.md](API_QUICKSTART.md) if you want HTTP details

---

## 3. How do *their agents* use it?

```text
Human's machine
├── ResearchersHub host  (always: python -m pocket serve)
│     listens on http://127.0.0.1:8787
│
├── Optional: MCP bridge  (python -m pocket mcp)
│     exposes tools: rh_construct, rh_skills_list, rh_atlas_claim, …
│
└── Coding agent (Claude / Cursor / Codex / …)
      ├── either: MCP tools
      └── or:     HTTP POST /v1/agents/invoke
```

**Example agent call (REST)**

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: cursor" \
  -d "{\"name\":\"rh_construct\",\"arguments\":{\"prompt\":\"Michaelis-Menten curve\"}}"
```

**What the agent gets back**

- `content` / markdown with embedded full images  
- `images[]` with PNG base64  
- `script` = full Python they can write to a file  
- `workflow_steps` = numbered method steps  
- `atlas` = graph node ids if linking succeeded  

**What the agent should do with it**

1. Show the figure to the user  
2. Offer to save the `.py` script  
3. Optionally `rh_atlas_claim` to record a result for later agents  

Agents do **not** upload your lab data to ResearchersHub cloud — there is no required cloud. Keys for Claude/Grok/etc. stay in **your** environment if you enable chat routing.

---

## 4. What happens? (step-by-step)

### When you ask for a chart

```text
1. Request hits host
   desk chat  OR  POST /v1/researchers/construct  OR  tool rh_construct

2. Construct engine matches intent
   e.g. "titration" → titration simulation
   e.g. "pk_pd_panel" → multi-step workflow (several figures)

3. Simulation runs in Python (on your machine)
   numbers computed → matplotlib draws figure (design v2)

4. Host writes artifacts
   ~/.researchershub/construct/<timestamp>_*.py
   ~/.researchershub/construct/<timestamp>_*.png

5. Host optionally updates Atlas
   experiment node → linked script + figure nodes

6. Response returns to you / agent
   full PNG + full Python + workflow steps (not a blurry stub)
```

### When you list skills

```text
GET /v1/researchers/skills
  → merges:
     - Python packs in src/pocket/
     - JSON in skills/catalog/
     - optional ~/.researchershub/skills/
```

On GitHub you already see the same catalog as files under `skills/`.

### When you set a model flag

```text
RH_MODEL=claude   # or grok, gpt, deepseek, local, …
```

Chat can go through **your** API key to that provider.  
Charts/simulations **do not need** a cloud model — construct runs locally with matplotlib.

---

## 5. Minimal path (copy-paste)

```powershell
git clone https://github.com/ItsNotAILABS/ResearchersHub.git
cd ResearchersHub
pip install -r requirements-researchers.txt
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 127.0.0.1 --port 8787
```

Then open: **http://127.0.0.1:8787/desk**

Or generate one figure without the desk:

```powershell
curl -s -X POST http://127.0.0.1:8787/v1/researchers/construct `
  -H "content-type: application/json" `
  -d "{\"prompt\":\"titration curve\"}"
```

---

## 6. Mental model (one sentence)

**ResearchersHub = your local research server that turns questions into skills + real figures + real Python, and can be driven by humans or coding agents — data stays on your machine.**
