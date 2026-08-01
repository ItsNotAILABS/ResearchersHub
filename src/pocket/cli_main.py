"""ResearchersHub CLI entry — serve | mcp | agent-tools | identity."""

from __future__ import annotations

import argparse
import json
import sys


def main(argv: list | None = None) -> int:
    argv = list(argv if argv is not None else sys.argv[1:])
    if not argv:
        argv = ["serve"]

    cmd = argv[0].lower().strip()

    if cmd in ("mcp", "mcp-server", "agent-mcp"):
        from pocket.mcp_server import main as mcp_main

        return mcp_main(argv[1:])

    if cmd in ("tools", "agent-tools", "manifest"):
        from pocket.agent_bridge import tool_manifest

        print(json.dumps(tool_manifest(), indent=2, ensure_ascii=False))
        return 0

    if cmd in ("invoke", "tool"):
        from pocket.agent_bridge import invoke_local

        p = argparse.ArgumentParser(prog="pocket invoke")
        p.add_argument("name")
        p.add_argument("--args", default="{}", help="JSON arguments")
        ns = p.parse_args(argv[1:])
        try:
            args = json.loads(ns.args)
        except json.JSONDecodeError:
            args = {}
        print(json.dumps(invoke_local(ns.name, args), indent=2, ensure_ascii=False, default=str))
        return 0

    if cmd in ("identity", "whoami"):
        from pocket.researchers_hub import identity

        print(json.dumps(identity(), indent=2, ensure_ascii=False, default=str))
        return 0

    if cmd in ("skills-count", "skills"):
        from pocket.science_skills import science_catalog_summary

        print(json.dumps(science_catalog_summary(), indent=2))
        return 0

    if cmd in ("help", "-h", "--help"):
        print(
            """ResearchersHub CLI
  python -m pocket serve [--host 0.0.0.0] [--port 8787]
  python -m pocket mcp              # MCP stdio for Claude / Cursor / Grok
  python -m pocket tools            # print agent tool manifest
  python -m pocket invoke NAME --args '{}'
  python -m pocket identity
  python -m pocket skills-count
"""
        )
        return 0

    # Default: host server (POCKET serve)
    if cmd == "serve":
        from pocket.server import main as serve_main

        return serve_main(argv) or 0

    # Unknown first arg: pass through to server CLI (worker, doctor, …)
    from pocket.server import main as serve_main

    return serve_main(argv) or 0


if __name__ == "__main__":
    raise SystemExit(main())
