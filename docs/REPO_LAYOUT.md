# Public repository layout

This repo is **public**. Folders are named for the product, not for private AI tools.

**Confused what this product is?** Read [HOW_TO_USE.md](HOW_TO_USE.md) first (what people see, how agents call it, what happens).

```text
ResearchersHub/
├── README.md                 # Product face
├── PRODUCT.md                # Definition
├── SHIP.md                   # Ship checklist
├── AGENTS.md                 # Shared coding-agent contract (industry-standard name)
├── LICENSE*
├── requirements-researchers.txt
├── docs/                     # Product documentation
│   ├── developers/           # Optional IDE/agent setup (claude, cursor, mcp examples)
│   ├── brand/                # Logos
│   ├── archive/              # Historical host papers only
│   └── …
├── src/pocket/               # Runtime package (import name historical; product = ResearchersHub)
├── skills/                   # 971 research skills as public JSON (catalog/ + INDEX)
│   ├── CATALOG.json
│   ├── INDEX.json
│   ├── catalog/*.json        # per-domain full skill objects
│   └── researchershub/       # optional agent how-to
├── scripts/                  # Installers & launchers
├── desktop-electron/         # Optional desktop shell
├── releases/                 # Release artifacts metadata
├── vendor/                   # Bundled libraries
└── .github/                  # GitHub Actions / Copilot instructions only
```

## What is *not* in the public tree

These stay **local / gitignored** (private tool config):

| Path | Why |
|------|-----|
| `.grok/` | Private Grok Build config — not a public product surface |
| `.agents/`, `.codex/`, `.cursor/`, `.claude/` | Editor/agent private state |
| `.pocket/`, `.researchershub/` | Secrets, sessions, local data |

## Package name `src/pocket`

Python still runs as `python -m pocket …` for host compatibility.  
**User-facing name is always ResearchersHub.**
