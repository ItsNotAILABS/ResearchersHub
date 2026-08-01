# Cloudflare named tunnel (optional)

Expose your **ResearchersHub** host for phone / remote without opening inbound ports.

## Outline

1. Install `cloudflared`.
2. Login / create named tunnel.
3. Route hostname → `http://127.0.0.1:8787`.
4. Keep PC awake; host process must stay up.

## Scripts

Repo may include helpers under `scripts/` (`Start-Cloudflare-Named.ps1`, etc.) inherited from host tooling. Prefer reading script headers before run.

## Security

Public URL exposes your multi-agent research desk. Prefer **Cloudflare Access** and never post owner passwords.

## Local-first

Most scientists should use:

```text
http://127.0.0.1:8787/desk
```

Tunnel is optional for remote access.
