# `src/` — runtime code

## Why is the package named `pocket`?

Historical host package name. Commands are:

```text
python -m pocket serve
python -m pocket mcp
python -m pocket tools
```

**Product name:** ResearchersHub (ItsNotAI Labs).  
Do not rename this folder casually — imports across the host depend on `pocket`.

## What matters for ResearchersHub

| File | Role |
|------|------|
| `pocket/server.py` | HTTP desk + API |
| `pocket/science_construct.py` | Simulations, charts, workflows |
| `pocket/science_render.py` | Publication figure design |
| `pocket/science_skills.py` | Core science skills |
| `pocket/research_skills_ext.py` | ML / comp bio / cheminf packs + JSON load |
| `pocket/research_skills_mega.py` | Expanded domain packs |
| `pocket/atlas_graph.py` | Atlas research graph |
| `pocket/model_router.py` | `RH_MODEL` multi-provider |
| `pocket/agent_bridge.py` | REST tool invoke for agents |
| `pocket/mcp_server.py` | MCP stdio for coding agents |
| `pocket/researchers_hub.py` | Product identity / doctrine |
| `pocket/cli_main.py` | CLI entry |

Other modules are host infrastructure (auth, sessions, jobs, UI) inherited with the runtime.
