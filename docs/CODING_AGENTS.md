# Coding agents × ResearchersHub

Optional integration for automation tools. The core product does not require any vendor-specific folders in the public tree.

## Surfaces

| Interface | Path / command |
|-----------|----------------|
| MCP | `python -m pocket mcp` |
| REST | `/v1/agents/*` |
| Example MCP config | [developers/mcp.example.json](developers/mcp.example.json) |
| Shared contract | [../AGENTS.md](../AGENTS.md) |
| Optional IDE notes | [developers/](developers/) |

```http
GET  /v1/agents/manifest
GET  /v1/agents/tools
POST /v1/agents/invoke
```

## Tools

`rh_identity` · `rh_skills_list` · `rh_skill_get` · `rh_models` · `rh_construct` · `rh_chat` · `rh_atlas_*` · `rh_doctrine` · `rh_coding_help`

## CLI

```text
python -m pocket tools
python -m pocket invoke rh_identity
python -m pocket mcp
```

## Security

Prefer localhost. Do not expose unauthenticated agent routes on a public tunnel without Access.
