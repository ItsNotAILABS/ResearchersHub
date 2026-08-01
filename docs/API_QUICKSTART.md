# API quickstart — ResearchersHub

## 1. Start host

```powershell
cd ResearchersHub
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 0.0.0.0 --port 8787
```

## 2. Health

```bash
curl -s http://127.0.0.1:8787/health
curl -s http://127.0.0.1:8787/v1/researchers
```

## 3. Skills + construct

```bash
curl -s http://127.0.0.1:8787/v1/researchers/skills | head
curl -s -X POST http://127.0.0.1:8787/v1/researchers/construct \
  -H "content-type: application/json" \
  -d "{\"prompt\":\"titration curve with full Python\"}"
```

## 4. Coding-agent invoke

```bash
curl -s -X POST http://127.0.0.1:8787/v1/agents/invoke \
  -H "content-type: application/json" \
  -H "X-Agent-Name: codex" \
  -d "{\"name\":\"rh_identity\",\"arguments\":{}}"
```

## 5. Model flag

```powershell
$env:RH_MODEL = "deepseek"   # claude | grok | gpt | codex | glm | kimi | finetune | local
$env:RH_CHAT_VIA_ROUTER = "1"
```

## 6. MCP

```powershell
python -m pocket mcp
```

Full agent guide: [CODING_AGENTS.md](CODING_AGENTS.md).
