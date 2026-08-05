# Scripts

## Use these (product)

| Script | Purpose |
|--------|---------|
| `Start-ResearchersHub.ps1` | Start host on :8787 |
| `Open-ResearchersHub-Edge.cmd` | Open Edge as app → desk |
| `export_skills_catalog.py` | Rebuild public `skills/*.json` |
| `Install-Coding-Agents.ps1` | Optional local skill mirrors for agents |
| `Setup-Cloudflare-Named-Tunnel.ps1` | Optional public URL |
| `Start-Cloudflare-Named.ps1` | Run named tunnel |
| `real-product.ps1` | Real product verification |
| `Install-AlwaysOn.ps1` | Login always-on host (Windows) |

## Ignore unless you know you need them

| Folder | Purpose |
|--------|---------|
| **`legacy/`** | Old **POCKET-named** host scripts from the fork. Not the public product surface. |

```powershell
# Normal start
powershell -ExecutionPolicy Bypass -File scripts\Start-ResearchersHub.ps1
```
