# Security — ResearchersHub

## Principles

- **Your infra** — host runs where you run it.
- **Your keys** — model API keys are operator env vars (`ANTHROPIC_API_KEY`, `XAI_API_KEY`, …).
- **No platform gatekeeping** of science content; still apply **your** lab and legal policies.
- **Founder ≠ market disk** — multi-user seats stay isolated from owner personal files.

## Auth

- Desk login: owner / member sessions (`/v1/auth/login`).
- Local desktop auto-session: `/v1/auth/desktop` (localhost only).
- API keys: `sk_pocket_…` Bearer for headless clients.
- Coding agents: prefer localhost MCP/REST; stamp `X-Agent-Name`.

## Secrets

Never commit:

- `access.env`, `ACCESS.txt`, API keys, seat invite raw keys, tunnel credentials.

## Hardening

1. Firewall host port if not intentional LAN service.
2. Tunnel + Access for remote scientists.
3. Rate limits on login endpoints (built-in).
4. Keep Python and OS patched.

## Report issues

Operator: ItsNotAI Labs / Medina Tech Labs (private channel preferred for credentials).
