# Production — ResearchersHub

## Minimum production

1. Host process always on (`python -m pocket serve` or Windows always-on scripts).
2. `matplotlib` installed for full chart construct (`requirements-researchers.txt`).
3. Secrets only in env / `~/.pocket/access.env` — never in git.
4. Optional Cloudflare named tunnel for phone / remote.
5. MCP only on trusted machines (`python -m pocket mcp`).

## Health

```text
GET /health
GET /v1/researchers
```

## Data directories

| Path | Contents |
|------|----------|
| `~/.researchershub/construct/` | Scripts + PNG figures |
| `~/.researchershub/atlas/` | Shared research graph |
| `~/.researchershub/skills/` | Editable skill JSON packs |
| `~/.pocket/` | Host auth, users, jobs (when co-hosted) |

## Public exposure

If you publish a URL:

- Prefer Cloudflare Access or equivalent.
- Do not leave `/v1/agents/*` open to the internet without auth.
- Rotate owner password after any leak.

## Ship checklist

See root [`SHIP.md`](../SHIP.md).
