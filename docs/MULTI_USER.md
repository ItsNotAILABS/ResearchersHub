# Multi-user seats (ResearchersHub)

## Mental model

| Role | Who | Sign-in |
|------|-----|---------|
| **Owner** | Operator of this host | ACCESS / owner username + password |
| **Member** | Invited researcher | **Their** username + password from seat register |

Register **never** puts someone on the owner account.  
A seat invite key only proves “owner allowed a new seat.”

## Seat invites

- Format: `pk_seat_<random>`
- Mint (admin): `POST /v1/admin/invites` `{ "label": "alice", "max_uses": 1 }`
- Member: desk → **Create my seat** → invite key → choose username/password

## Isolation

- Members get separate tokens and sandboxes.
- Market seats must not receive founder personal disk paths.
- Owner stays owner when minting invites.

## Local coding agents

Coding agents (Claude, Grok, Codex) use `/v1/agents/*` on localhost. Do not expose unauthenticated agent routes on a public tunnel without Access.
