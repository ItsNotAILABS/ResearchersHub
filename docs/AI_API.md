# ResearchersHub AI API

Sellable / headless research API on your host.

## Auth

```http
Authorization: Bearer sk_pocket_…
# or
X-API-Key: sk_pocket_…
```

Keys are minted on the operator host (desk or admin API). Metering uses host credits when enabled.

## Core routes

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/health` | Liveness |
| GET | `/v1/researchers` | Product identity |
| GET | `/v1/researchers/skills` | 970+ research skills |
| GET | `/v1/researchers/models` | Active model (`RH_MODEL`) |
| POST | `/v1/researchers/construct` | Full charts + Python workflows |
| POST | `/v1/researchers/chat` | Multi-model research chat |
| GET | `/v1/agents/manifest` | Coding-agent tool catalog |
| POST | `/v1/agents/invoke` | Invoke `rh_*` tools |
| POST | `/v1/ai/chat` | OpenAI-shaped chat (wiki + construct enrich) |
| POST | `/v1/ai/agents/{id}/run` | Headless agent run |

## Coding agents

Prefer tools over raw curl when using Claude / Grok / Cursor:

```text
python -m pocket mcp
POST /v1/agents/invoke  {"name":"rh_construct","arguments":{"prompt":"…"}}
```

See [CODING_AGENTS.md](CODING_AGENTS.md).

## Deploy notes

1. Run host on your infra (`python -m pocket serve`).
2. Optional: Cloudflare named tunnel for public URL.
3. Put Access / auth in front of any public exposure.
4. Keys stay on operator machine — no vendor gatekeeping of science.
