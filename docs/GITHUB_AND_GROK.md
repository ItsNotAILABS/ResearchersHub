# What GitHub and Grok are doing with ResearchersHub

## GitHub (what you see on the site)

| Thing | Meaning |
|-------|---------|
| **Repo URL** | https://github.com/ItsNotAILABS/ResearchersHub |
| **Owner** | **ItsNotAILABS** (org) — this is the product home |
| **Commit author “FreddyCreates”** | Your personal GitHub account that **pushed** the commits (git `user.name` / signed-in `gh`). Org owns the repo; the person who ran `git push` is still listed on each commit. |
| **Folders like `.github`, `src/pocket`, `skills`** | Normal product code + agent instructions — not “another product” |

So: **company face = ItsNotAILABS/ResearchersHub**.  
**“FreddyCreates” on commits** = who authored/pushed, not a second product.

To make future commits show org identity (optional):

```powershell
# only if you want commit attribution under org bot / company email
git config user.name "ItsNotAI Labs"
git config user.email "your-company@email"
```

(You still push with an account that has write access to the org repo.)

---

## Grok (what `.grok/` is)

`.grok/` is **Grok Build / Grok CLI project config** that was copied when we forked the host tree.

| Path | Role |
|------|------|
| `.grok/personas/*.toml` | Short system personas Grok can load when coding **in this repo** (engine vs UI). They are **not** the ResearchersHub science skill pack. |
| `skills/researchershub/SKILL.md` | The **product skill** for coding agents (also installed under `~/.grok/skills/researchershub`) |
| `python -m pocket mcp` | MCP server so Grok/Claude/Cursor call `rh_*` tools |

**Personas ≠ science skills.**  
- **Personas** = how Grok behaves while editing this codebase.  
- **Skills (970+)** = research capabilities inside the running host (`/v1/researchers/skills`).  
- **Agent skill** `researchershub` = how Grok/Claude *call* that host.

Stale `pocket_engine.toml` / `pocket_ui.toml` were leftover from POCKET and are replaced by:

- `researchershub_engine.toml`
- `researchershub_ui.toml`

---

## Why the tree still says `src/pocket`

Python package import remains `pocket` so the host runtime (`python -m pocket serve`) keeps working.  
**Product name** everywhere user-facing is **ResearchersHub**.

---

## Quick map

```text
GitHub ItsNotAILABS/ResearchersHub
  ├── README / docs     → public product
  ├── src/pocket        → runtime (import name historical)
  ├── skills/researchershub → Grok/Claude agent skill
  ├── .grok/personas    → Grok Build coding personas for this repo
  └── docs/archive/…    → old POCKET papers only
```
