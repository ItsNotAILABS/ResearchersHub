# ResearchersHub Desktop (Electron) — optional shell

Electron shell for the local ResearchersHub host UI.

**Note:** App identifiers may still say `pocket-desktop` in package metadata from host lineage. Product branding is **ResearchersHub**.

## Requirements

- Python with package path: `PYTHONPATH=<repo>/src`
- Host: `python -m pocket serve --host 127.0.0.1 --port 8787`

## Run host first

```powershell
cd <ResearchersHub>
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 127.0.0.1 --port 8787
```

Then start Electron against `http://127.0.0.1:8787/desk` (or use Edge app launcher `scripts/Open-ResearchersHub-Edge.cmd`).

## Env

| Variable | Default | Purpose |
|----------|---------|---------|
| `POCKET_URL` / `RH_BASE` | `http://127.0.0.1:8787/` | URL loaded in the window |
| `POCKET_ROOT` | parent of `desktop-electron` | Repo root |
| `POCKET_PYTHON` | auto | Python executable |

Prefer Edge `--app` for the lightest “installed app” feel unless you need Electron packaging.
