# GEMINI.md — ResearchersHub

Use **ResearchersHub** as the research co-pilot for this workspace.

- Host: `http://127.0.0.1:8787`
- Tools: `POST /v1/agents/invoke`
- MCP: `python -m pocket mcp` (`PYTHONPATH=src`)
- Models: set `RH_BASE_URL` + `RH_MODEL_ID` for OpenAI-compatible Gemini gateways, or use REST tools without cloud chat
- Atlas agent name: `gemini`
- Contract: [AGENTS.md](AGENTS.md)
