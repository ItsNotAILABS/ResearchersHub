"""ResearchersHub multi-model router — one flag to switch providers.

Any model: GLM, Kimi, DeepSeek, Claude, GPT, or your own fine-tune.
No vendor gatekeeping: operator chooses base URL + key + model id.

Flag (first match wins):
  RH_MODEL / RESEARCHERSHUB_MODEL / POCKET_MODEL
  values: glm | kimi | deepseek | claude | gpt | openai | finetune | local | auto

Or full override:
  RH_MODEL_PROVIDER, RH_MODEL_ID, RH_BASE_URL, RH_API_KEY
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

PRODUCT = "ResearchersHub"

# One-flag presets — operator can override URL/key/model anytime
PRESETS: Dict[str, Dict[str, Any]] = {
    "glm": {
        "provider": "glm",
        "label": "Zhipu GLM",
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4-plus",
        "env_key": "GLM_API_KEY",
        "alt_keys": ["ZHIPU_API_KEY", "BIGMODEL_API_KEY"],
    },
    "kimi": {
        "provider": "kimi",
        "label": "Moonshot Kimi",
        "base_url": "https://api.moonshot.cn/v1",
        "model": "moonshot-v1-128k",
        "env_key": "KIMI_API_KEY",
        "alt_keys": ["MOONSHOT_API_KEY"],
    },
    "deepseek": {
        "provider": "deepseek",
        "label": "DeepSeek",
        "base_url": "https://api.deepseek.com/v1",
        "model": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
        "alt_keys": [],
    },
    "claude": {
        "provider": "claude",
        "label": "Anthropic Claude",
        "base_url": "https://api.anthropic.com/v1",
        "model": "claude-sonnet-4-20250514",
        "env_key": "ANTHROPIC_API_KEY",
        "alt_keys": ["CLAUDE_API_KEY"],
        "style": "anthropic",
    },
    "gpt": {
        "provider": "gpt",
        "label": "OpenAI GPT",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4.1",
        "env_key": "OPENAI_API_KEY",
        "alt_keys": [],
    },
    "openai": {
        "provider": "openai",
        "label": "OpenAI-compatible",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4.1",
        "env_key": "OPENAI_API_KEY",
        "alt_keys": [],
    },
    "finetune": {
        "provider": "finetune",
        "label": "Your fine-tune (OpenAI-compatible)",
        "base_url": "",  # must set RH_BASE_URL
        "model": "",  # must set RH_MODEL_ID
        "env_key": "RH_API_KEY",
        "alt_keys": ["FINETUNE_API_KEY", "OPENAI_API_KEY"],
    },
    "local": {
        "provider": "local",
        "label": "Local OpenAI-compatible (Ollama/vLLM/LM Studio)",
        "base_url": "http://127.0.0.1:11434/v1",
        "model": "llama3.1",
        "env_key": "RH_API_KEY",
        "alt_keys": ["OPENAI_API_KEY"],
        "allow_empty_key": True,
    },
}


def _flag() -> str:
    raw = (
        os.environ.get("RH_MODEL")
        or os.environ.get("RESEARCHERSHUB_MODEL")
        or os.environ.get("POCKET_MODEL")
        or "auto"
    ).strip().lower()
    aliases = {
        "chatgpt": "gpt",
        "openai-gpt": "gpt",
        "anthropic": "claude",
        "zhipu": "glm",
        "bigmodel": "glm",
        "moonshot": "kimi",
        "ft": "finetune",
        "fine-tune": "finetune",
        "fine_tune": "finetune",
        "ollama": "local",
        "vllm": "local",
    }
    return aliases.get(raw, raw)


def _first_key(names: List[str]) -> str:
    for n in names:
        v = (os.environ.get(n) or "").strip()
        if v:
            return v
    return ""


def resolve_model(flag: str = "") -> Dict[str, Any]:
    """Resolve active model config from one flag + optional overrides."""
    f = (flag or _flag()).strip().lower()
    if f in ("", "auto"):
        # Prefer explicit RH_* overrides, else first provider with a key
        if os.environ.get("RH_MODEL_ID") or os.environ.get("RH_BASE_URL"):
            f = "finetune"
        else:
            for name in ("deepseek", "glm", "kimi", "claude", "gpt", "local"):
                p = PRESETS[name]
                keys = [p["env_key"]] + list(p.get("alt_keys") or [])
                if _first_key(keys) or p.get("allow_empty_key"):
                    if _first_key(keys) or name == "local":
                        # only pick local if no cloud keys at all
                        if name != "local" or not any(
                            _first_key(
                                [PRESETS[x]["env_key"]] + list(PRESETS[x].get("alt_keys") or [])
                            )
                            for x in ("deepseek", "glm", "kimi", "claude", "gpt")
                        ):
                            f = name
                            if name != "local" or f == "local":
                                break
            if f in ("", "auto"):
                f = "local"

    preset = dict(PRESETS.get(f) or PRESETS["local"])
    provider = (os.environ.get("RH_MODEL_PROVIDER") or preset["provider"]).strip().lower()
    base_url = (
        os.environ.get("RH_BASE_URL")
        or os.environ.get("OPENAI_BASE_URL")
        or preset.get("base_url")
        or ""
    ).rstrip("/")
    model_id = (
        os.environ.get("RH_MODEL_ID")
        or os.environ.get("RH_MODEL_NAME")
        or preset.get("model")
        or ""
    )
    key_names = [preset.get("env_key") or "RH_API_KEY"] + list(preset.get("alt_keys") or [])
    key_names = ["RH_API_KEY"] + key_names
    api_key = _first_key([n for n in key_names if n])
    style = preset.get("style") or "openai"

    return {
        "ok": True,
        "flag": f,
        "provider": provider,
        "label": preset.get("label") or provider,
        "base_url": base_url,
        "model": model_id,
        "api_key_set": bool(api_key),
        "style": style,
        "allow_empty_key": bool(preset.get("allow_empty_key")),
        "product": PRODUCT,
        "switch": "Set RH_MODEL=glm|kimi|deepseek|claude|gpt|finetune|local",
        "sovereign": True,
        "throttling": "none-by-platform",
        "gatekeeping": False,
    }


def list_providers() -> List[Dict[str, Any]]:
    out = []
    for name, p in PRESETS.items():
        keys = [p["env_key"]] + list(p.get("alt_keys") or [])
        out.append(
            {
                "flag": name,
                "label": p.get("label"),
                "default_model": p.get("model"),
                "base_url": p.get("base_url"),
                "key_env": p.get("env_key"),
                "configured": bool(_first_key(keys)) or bool(p.get("allow_empty_key")),
            }
        )
    return out


def _openai_chat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.2,
    max_tokens: int = 4096,
    timeout: int = 120,
) -> Dict[str, Any]:
    url = base_url.rstrip("/") + "/chat/completions"
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    data = json.dumps(body).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "ResearchersHub/1.0",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = json.loads(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:800]
        return {"ok": False, "error": f"HTTP {e.code}: {err_body}", "provider_style": "openai"}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400], "provider_style": "openai"}

    content = ""
    try:
        content = raw["choices"][0]["message"]["content"] or ""
    except Exception:
        content = json.dumps(raw)[:4000]
    return {
        "ok": True,
        "content": content,
        "raw": raw,
        "provider_style": "openai",
        "model": model,
    }


def _anthropic_chat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.2,
    max_tokens: int = 4096,
    timeout: int = 120,
) -> Dict[str, Any]:
    url = base_url.rstrip("/") + "/messages"
    system = ""
    conv: List[Dict[str, Any]] = []
    for m in messages:
        role = (m.get("role") or "user").lower()
        text = m.get("content") or ""
        if role == "system":
            system = (system + "\n" + text).strip()
            continue
        if role not in ("user", "assistant"):
            role = "user"
        conv.append({"role": role, "content": text})
    if not conv:
        conv = [{"role": "user", "content": "Hello"}]
    body: Dict[str, Any] = {
        "model": model,
        "messages": conv,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if system:
        body["system"] = system
    data = json.dumps(body).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key or "",
        "anthropic-version": "2023-06-01",
        "User-Agent": "ResearchersHub/1.0",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = json.loads(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:800]
        return {"ok": False, "error": f"HTTP {e.code}: {err_body}", "provider_style": "anthropic"}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400], "provider_style": "anthropic"}

    content = ""
    try:
        parts = raw.get("content") or []
        content = "".join(p.get("text") or "" for p in parts if isinstance(p, dict))
    except Exception:
        content = json.dumps(raw)[:4000]
    return {
        "ok": True,
        "content": content,
        "raw": raw,
        "provider_style": "anthropic",
        "model": model,
    }


def chat(
    messages: List[Dict[str, str]],
    *,
    flag: str = "",
    temperature: float = 0.2,
    max_tokens: int = 4096,
) -> Dict[str, Any]:
    """Call the active model. No platform throttling or content gatekeeping."""
    cfg = resolve_model(flag)
    if not cfg.get("base_url"):
        return {
            "ok": False,
            "error": "No base_url — set RH_BASE_URL for finetune/custom providers",
            "config": {k: v for k, v in cfg.items() if k != "api_key"},
        }
    if not cfg.get("model"):
        return {
            "ok": False,
            "error": "No model id — set RH_MODEL_ID",
            "config": cfg,
        }
    api_key = _first_key(
        ["RH_API_KEY"]
        + ([PRESETS.get(cfg["flag"], {}).get("env_key") or ""] if cfg.get("flag") in PRESETS else [])
        + list(PRESETS.get(cfg.get("flag") or "", {}).get("alt_keys") or [])
        + ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "DEEPSEEK_API_KEY", "GLM_API_KEY", "KIMI_API_KEY"]
    )
    if not api_key and not cfg.get("allow_empty_key"):
        return {
            "ok": False,
            "error": f"API key not set for provider {cfg.get('provider')}. "
            f"Set RH_API_KEY or provider key env.",
            "config": cfg,
            "hint": "Your infra, your keys — ResearchersHub never proxies vendor accounts.",
        }

    if cfg.get("style") == "anthropic":
        res = _anthropic_chat(
            base_url=cfg["base_url"],
            api_key=api_key,
            model=cfg["model"],
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
    else:
        res = _openai_chat(
            base_url=cfg["base_url"],
            api_key=api_key,
            model=cfg["model"],
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
    res["config"] = {
        "flag": cfg["flag"],
        "provider": cfg["provider"],
        "model": cfg["model"],
        "base_url": cfg["base_url"],
        "label": cfg["label"],
    }
    res["product"] = PRODUCT
    res["doctrine"] = {
        "throttling": "none-by-platform",
        "gatekeeping": False,
        "data_stays": "on_your_infra",
    }
    return res


def doctrine() -> Dict[str, Any]:
    return {
        "product": PRODUCT,
        "any_model": True,
        "providers": list(PRESETS.keys()),
        "one_flag": "RH_MODEL=glm|kimi|deepseek|claude|gpt|finetune|local",
        "overrides": ["RH_MODEL_PROVIDER", "RH_MODEL_ID", "RH_BASE_URL", "RH_API_KEY"],
        "throttling": "none-by-platform",
        "gatekeeping": False,
        "vendor_decides_science": False,
        "runs_on": "your_infra",
        "data_stays": "yours",
    }
