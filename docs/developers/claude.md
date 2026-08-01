# Claude — ResearchersHub

Optional notes for Claude / Claude Code. Product overview: [../../README.md](../../README.md).

## Tools

```bash
PYTHONPATH=src python -m pocket mcp
```

Or REST:

```bash
curl -s http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: claude" \
  -d '{"name":"rh_construct","arguments":{"prompt":"titration curve with Python"}}'
```

## Model env

```bash
export RH_MODEL=claude
export ANTHROPIC_API_KEY=...
export RH_CHAT_VIA_ROUTER=1
```

## Behaviors

1. Prefer `rh_construct` for charts — full images + scripts.
2. Search skills with `rh_skills_list`.
3. Claim results with `rh_atlas_claim` (`agent: "claude"`).
4. User-facing product name is **ResearchersHub**.

Shared contract: [../../AGENTS.md](../../AGENTS.md).
