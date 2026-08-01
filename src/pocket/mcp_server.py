"""ResearchersHub MCP server (stdio) — Claude Desktop, Claude Code, Cursor, Grok MCP clients.

Run:
  set PYTHONPATH=src
  python -m pocket mcp

Protocol: JSON-RPC 2.0 over stdin/stdout (MCP subset: initialize, tools/list, tools/call).
"""

from __future__ import annotations

import json
import sys
from typing import Any, Dict, Optional

from pocket.agent_bridge import TOOLS, anthropic_tools, invoke_local, tool_manifest


def _log(msg: str) -> None:
    # MCP: never write non-JSON to stdout
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def _reply(msg_id: Any, result: Any = None, error: Optional[Dict[str, Any]] = None) -> None:
    payload: Dict[str, Any] = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        payload["error"] = error
    else:
        payload["result"] = result
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _tools_list() -> Dict[str, Any]:
    tools = []
    for t in anthropic_tools():
        tools.append(
            {
                "name": t["name"],
                "description": t["description"],
                "inputSchema": t.get("input_schema")
                or {"type": "object", "properties": {}},
            }
        )
    return {"tools": tools}


def _tools_call(params: Dict[str, Any]) -> Dict[str, Any]:
    name = params.get("name") or ""
    arguments = params.get("arguments") or params.get("input") or {}
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except Exception:
            arguments = {"raw": arguments}
    result = invoke_local(name, arguments if isinstance(arguments, dict) else {})
    # MCP content blocks
    text = json.dumps(result, ensure_ascii=False, indent=2, default=str)
    # Keep response bounded for huge base64 boards
    if len(text) > 120_000:
        slim = dict(result) if isinstance(result, dict) else {"result": result}
        if isinstance(slim, dict) and "images" in slim:
            slim["images"] = [
                {
                    "alt": (img or {}).get("alt"),
                    "mime": (img or {}).get("mime"),
                    "base64_len": len((img or {}).get("base64") or ""),
                    "note": "truncated in MCP — use image_paths on disk",
                }
                for img in (slim.get("images") or [])[:8]
            ]
            slim["images_truncated"] = True
        text = json.dumps(slim, ensure_ascii=False, indent=2, default=str)[:100_000]
    return {
        "content": [{"type": "text", "text": text}],
        "isError": not bool(result.get("ok", True)) if isinstance(result, dict) else False,
    }


def handle_message(msg: Dict[str, Any]) -> None:
    method = msg.get("method") or ""
    msg_id = msg.get("id")
    params = msg.get("params") or {}

    # Notifications (no id) — ignore quietly
    if msg_id is None and method.startswith("notifications/"):
        return

    if method == "initialize":
        _reply(
            msg_id,
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "researchershub",
                    "version": "1.2.1",
                },
            },
        )
        return

    if method == "ping":
        _reply(msg_id, {})
        return

    if method == "tools/list":
        _reply(msg_id, _tools_list())
        return

    if method == "tools/call":
        try:
            _reply(msg_id, _tools_call(params if isinstance(params, dict) else {}))
        except Exception as e:
            _reply(msg_id, error={"code": -32000, "message": str(e)[:400]})
        return

    if method in ("resources/list", "prompts/list"):
        _reply(msg_id, {"resources": []} if "resources" in method else {"prompts": []})
        return

    if method == "researchershub/manifest":
        _reply(msg_id, tool_manifest())
        return

    if msg_id is not None:
        _reply(
            msg_id,
            error={"code": -32601, "message": f"Method not found: {method}"},
        )


def main(argv: Optional[list] = None) -> int:
    _log("ResearchersHub MCP server starting (stdio). Tools: " + ", ".join(t["name"] for t in TOOLS))
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as e:
            _log(f"bad json: {e}")
            continue
        if not isinstance(msg, dict):
            continue
        handle_message(msg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
