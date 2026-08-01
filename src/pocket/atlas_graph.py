"""ResearchersHub native Atlas integration — many agents, one shared research graph.

Atlas = reproducible research graph stored on operator infra:
  nodes: claims, papers, datasets, experiments, figures, skills, agents, scripts
  edges: supports | cites | derives | uses_skill | produced_by | replicates

All agents read/write the same graph under ~/.researchershub/atlas/ (or RH_ATLAS_DIR).
"""

from __future__ import annotations

import json
import os
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

PRODUCT = "ResearchersHub"
SCHEMA = "researchershub.atlas.v1"

NODE_TYPES = (
    "claim",
    "paper",
    "dataset",
    "experiment",
    "figure",
    "skill",
    "agent",
    "script",
    "protocol",
    "result",
    "hypothesis",
    "molecule",
    "gene",
    "model_run",
)

EDGE_TYPES = (
    "supports",
    "refutes",
    "cites",
    "derives",
    "uses_skill",
    "produced_by",
    "replicates",
    "depends_on",
    "measures",
    "trains_on",
    "evaluates",
)


def atlas_dir() -> Path:
    raw = (os.environ.get("RH_ATLAS_DIR") or "").strip()
    if raw:
        p = Path(raw)
    else:
        p = Path.home() / ".researchershub" / "atlas"
    p.mkdir(parents=True, exist_ok=True)
    (p / "nodes").mkdir(exist_ok=True)
    (p / "edges").mkdir(exist_ok=True)
    return p


def _id(prefix: str = "n") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def _read_json(path: Path) -> Optional[dict]:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def add_node(
    kind: str,
    title: str,
    *,
    body: str = "",
    meta: Optional[Dict[str, Any]] = None,
    agent: str = "",
    node_id: str = "",
) -> Dict[str, Any]:
    kind = (kind or "claim").lower().strip()
    if kind not in NODE_TYPES:
        kind = "claim"
    nid = node_id or _id("n")
    node = {
        "id": nid,
        "kind": kind,
        "title": (title or "").strip() or nid,
        "body": body or "",
        "meta": meta or {},
        "agent": agent or "",
        "created_at": time.time(),
        "updated_at": time.time(),
        "product": PRODUCT,
        "schema": SCHEMA,
    }
    _write_json(atlas_dir() / "nodes" / f"{nid}.json", node)
    _append_event({"op": "add_node", "id": nid, "kind": kind, "agent": agent})
    return node


def add_edge(
    src: str,
    dst: str,
    relation: str,
    *,
    meta: Optional[Dict[str, Any]] = None,
    agent: str = "",
    edge_id: str = "",
) -> Dict[str, Any]:
    rel = (relation or "derives").lower().strip()
    if rel not in EDGE_TYPES:
        rel = "derives"
    eid = edge_id or _id("e")
    edge = {
        "id": eid,
        "src": src,
        "dst": dst,
        "relation": rel,
        "meta": meta or {},
        "agent": agent or "",
        "created_at": time.time(),
        "product": PRODUCT,
        "schema": SCHEMA,
    }
    _write_json(atlas_dir() / "edges" / f"{eid}.json", edge)
    _append_event({"op": "add_edge", "id": eid, "src": src, "dst": dst, "relation": rel, "agent": agent})
    return edge


def _append_event(ev: dict) -> None:
    log = atlas_dir() / "events.jsonl"
    ev = {**ev, "ts": time.time()}
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ev, ensure_ascii=False) + "\n")


def get_node(node_id: str) -> Optional[Dict[str, Any]]:
    return _read_json(atlas_dir() / "nodes" / f"{node_id}.json")


def list_nodes(kind: str = "", limit: int = 200) -> List[Dict[str, Any]]:
    root = atlas_dir() / "nodes"
    out: List[Dict[str, Any]] = []
    for p in sorted(root.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        n = _read_json(p)
        if not n:
            continue
        if kind and n.get("kind") != kind:
            continue
        out.append(n)
        if len(out) >= limit:
            break
    return out


def list_edges(limit: int = 500) -> List[Dict[str, Any]]:
    root = atlas_dir() / "edges"
    out: List[Dict[str, Any]] = []
    for p in sorted(root.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        e = _read_json(p)
        if e:
            out.append(e)
        if len(out) >= limit:
            break
    return out


def neighbors(node_id: str) -> Dict[str, Any]:
    edges = [e for e in list_edges(limit=2000) if e.get("src") == node_id or e.get("dst") == node_id]
    ids = set()
    for e in edges:
        ids.add(e.get("src"))
        ids.add(e.get("dst"))
    ids.discard(node_id)
    nodes = [get_node(i) for i in ids if i]
    return {
        "ok": True,
        "node": get_node(node_id),
        "edges": edges,
        "neighbors": [n for n in nodes if n],
    }


def agent_claim(
    agent: str,
    title: str,
    body: str = "",
    *,
    kind: str = "claim",
    links: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, Any]:
    """Any agent posts a node and optional edges into the shared graph."""
    node = add_node(kind, title, body=body, agent=agent)
    made_edges = []
    for link in links or []:
        dst = link.get("dst") or link.get("to") or ""
        rel = link.get("relation") or link.get("rel") or "derives"
        if dst:
            made_edges.append(add_edge(node["id"], dst, rel, agent=agent))
    return {"ok": True, "node": node, "edges": made_edges}


def record_construct(
    *,
    title: str,
    script_path: str = "",
    image_paths: Optional[List[str]] = None,
    summary: str = "",
    agent: str = "construct",
    skill_id: str = "",
) -> Dict[str, Any]:
    """Link constructive workflow outputs into Atlas for reproducibility."""
    exp = add_node(
        "experiment",
        title,
        body=summary,
        agent=agent,
        meta={"skill_id": skill_id},
    )
    nodes = [exp]
    if script_path:
        sc = add_node(
            "script",
            Path(script_path).name,
            body=script_path,
            agent=agent,
            meta={"path": script_path},
        )
        add_edge(exp["id"], sc["id"], "produced_by", agent=agent)
        nodes.append(sc)
    for ip in image_paths or []:
        fig = add_node(
            "figure",
            Path(ip).name,
            body=ip,
            agent=agent,
            meta={"path": ip},
        )
        add_edge(exp["id"], fig["id"], "produced_by", agent=agent)
        nodes.append(fig)
    if skill_id:
        sk = add_node("skill", skill_id, body=skill_id, agent=agent, meta={"skill_id": skill_id})
        add_edge(exp["id"], sk["id"], "uses_skill", agent=agent)
        nodes.append(sk)
    return {"ok": True, "experiment": exp, "nodes": nodes}


def export_graph(limit_nodes: int = 500, limit_edges: int = 2000) -> Dict[str, Any]:
    nodes = list_nodes(limit=limit_nodes)
    edges = list_edges(limit=limit_edges)
    return {
        "ok": True,
        "schema": SCHEMA,
        "product": PRODUCT,
        "dir": str(atlas_dir()),
        "counts": {"nodes": len(nodes), "edges": len(edges)},
        "nodes": nodes,
        "edges": edges,
        "reproducible": True,
        "shared_by": "all_agents",
    }


def snapshot() -> Dict[str, Any]:
    nodes = list_nodes(limit=5000)
    edges = list_edges(limit=10000)
    by_kind: Dict[str, int] = {}
    for n in nodes:
        k = n.get("kind") or "?"
        by_kind[k] = by_kind.get(k, 0) + 1
    return {
        "ok": True,
        "product": PRODUCT,
        "schema": SCHEMA,
        "dir": str(atlas_dir()),
        "nodes": len(nodes),
        "edges": len(edges),
        "by_kind": by_kind,
        "doctrine": {
            "many_agents": True,
            "one_shared_graph": True,
            "reproducible": True,
            "data_on": "your_infra",
        },
    }


def seed_if_empty() -> Dict[str, Any]:
    """Bootstrap a minimal research graph once."""
    if list_nodes(limit=1):
        return {"ok": True, "seeded": False}
    root = add_node(
        "hypothesis",
        "ResearchersHub Atlas root",
        body="Shared reproducible research graph for all agents.",
        agent="atlas",
    )
    doctrine = add_node(
        "claim",
        "Science without vendor gatekeeping",
        body="Any model, 250+ skills, data stays on operator infra.",
        agent="atlas",
    )
    add_edge(root["id"], doctrine["id"], "supports", agent="atlas")
    return {"ok": True, "seeded": True, "root": root["id"]}
