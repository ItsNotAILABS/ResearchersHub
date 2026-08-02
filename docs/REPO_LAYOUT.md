# Repository layout

**Confused?** Read [HOW_TO_USE.md](HOW_TO_USE.md) and root **[FILES.md](../FILES.md)**.

## Public tree (what you should see on GitHub)

```text
ResearchersHub/
├── README.md                 # Product home
├── FILES.md                  # ← every folder explained
├── PRODUCT.md
├── SHIP.md
├── AGENTS.md                 # optional agent contract
├── LICENSE*
├── requirements-researchers.txt
│
├── docs/                     # How-to + API + example figures
│   ├── HOW_TO_USE.md         # humans + agents + what happens
│   ├── assets/               # example PNGs from construct
│   ├── brand/                # logos
│   ├── developers/           # optional IDE notes
│   └── archive/              # historical host papers only
│
├── skills/                   # 971 skills as public JSON
│   ├── INDEX.json
│   ├── CATALOG.json
│   └── catalog/*.json
│
├── src/                      # runtime
│   ├── README.md             # why package is named pocket
│   └── pocket/               # python -m pocket serve
│
├── scripts/                  # product entry scripts only
│   ├── README.md
│   ├── Start-ResearchersHub.ps1
│   ├── Open-ResearchersHub-Edge.cmd
│   ├── export_skills_catalog.py
│   └── legacy/               # old POCKET-named scripts (ignore)
│
├── optional/                 # NOT required for the product
│   ├── README.md
│   ├── desktop-electron/
│   ├── vendor/
│   ├── releases/
│   └── web/
│
└── .github/                  # GitHub-only metadata
```

## Rules

1. **Product surface** = `docs/`, `skills/`, `src/`, `scripts/` (non-legacy).  
2. **No private AI-tool homes** (`.grok`, etc.) in the public tree.  
3. **Legacy POCKET script names** live only under `scripts/legacy/`.  
4. **Optional** experiments live under `optional/`.  
5. **Archive** = history, not current docs.  
