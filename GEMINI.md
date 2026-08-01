# GEMINI.md — ResearchersHub

Use ResearchersHub as the research co-pilot for this workspace.

- Host: `http://127.0.0.1:8787`
- Invoke tools: `POST /v1/agents/invoke`
- MCP: `python -m pocket mcp` (PYTHONPATH=src)
- Models: `RH_MODEL=gemini` is not a built-in preset; use `finetune`/`gpt` with Google OpenAI-compatible endpoint via `RH_BASE_URL` + `RH_MODEL_ID`, or call REST tools directly.
- Claim agent name: `gemini`
- Full contract: `AGENTS.md`
