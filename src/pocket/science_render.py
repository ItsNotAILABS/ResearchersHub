"""ResearchersHub publication rendering — shared design system for all figures."""

from __future__ import annotations

import base64
import io
from typing import Any, Dict, List, Optional, Sequence, Tuple

PRODUCT = "ResearchersHub"

# Brand palette (teal / slate / accent amber)
PALETTE = {
    "primary": "#0b6e4f",
    "primary_dark": "#064e3b",
    "secondary": "#1d4ed8",
    "accent": "#d97706",
    "danger": "#be123c",
    "muted": "#64748b",
    "grid": "#e2e8f0",
    "spine": "#94a3b8",
    "bg": "#ffffff",
    "panel": "#f8fafc",
    "ink": "#0f172a",
    "series": [
        "#0b6e4f",
        "#1d4ed8",
        "#d97706",
        "#7c3aed",
        "#be123c",
        "#0891b2",
        "#ca8a04",
        "#4f46e5",
    ],
}


def try_plt():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import rcParams

    rcParams.update(
        {
            "figure.facecolor": PALETTE["bg"],
            "axes.facecolor": PALETTE["panel"],
            "axes.edgecolor": PALETTE["spine"],
            "axes.labelcolor": PALETTE["ink"],
            "axes.titlecolor": PALETTE["ink"],
            "axes.titlesize": 13,
            "axes.labelsize": 11,
            "axes.titleweight": "bold",
            "axes.linewidth": 0.9,
            "xtick.color": PALETTE["muted"],
            "ytick.color": PALETTE["muted"],
            "xtick.labelsize": 9.5,
            "ytick.labelsize": 9.5,
            "grid.color": PALETTE["grid"],
            "grid.linewidth": 0.7,
            "grid.alpha": 0.95,
            "legend.frameon": True,
            "legend.fancybox": True,
            "legend.framealpha": 0.92,
            "legend.edgecolor": PALETTE["grid"],
            "legend.fontsize": 9,
            "font.family": "DejaVu Sans",
            "figure.dpi": 120,
            "savefig.dpi": 180,
            "savefig.facecolor": PALETTE["bg"],
            "savefig.bbox": "tight",
            "lines.solid_capstyle": "round",
        }
    )
    return plt


def new_axes(figsize: Tuple[float, float] = (7.6, 4.6), nrows: int = 1, ncols: int = 1):
    plt = try_plt()
    if nrows == 1 and ncols == 1:
        fig, ax = plt.subplots(figsize=figsize)
        style_ax(ax)
        return plt, fig, ax
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    flat = axes.ravel() if hasattr(axes, "ravel") else [axes]
    for a in flat:
        style_ax(a)
    return plt, fig, axes


def style_ax(ax, *, grid: bool = True) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(PALETTE["spine"])
    ax.spines["bottom"].set_color(PALETTE["spine"])
    if grid:
        ax.grid(True, which="major", axis="both", linestyle="--", linewidth=0.7, alpha=0.9)
        ax.set_axisbelow(True)
    ax.tick_params(length=3.5, width=0.8)


def brand_footer(fig, text: str = "") -> None:
    label = text or f"{PRODUCT} · constructive simulation"
    fig.text(
        0.99,
        0.01,
        label,
        ha="right",
        va="bottom",
        fontsize=7.5,
        color=PALETTE["muted"],
        alpha=0.9,
    )


def finish(fig, plt, *, alt: str = "figure", footer: bool = True) -> Dict[str, str]:
    if footer:
        brand_footer(fig)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=180, bbox_inches="tight", facecolor=PALETTE["bg"])
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode("ascii")
    plt.close(fig)
    return {"alt": alt, "mime": "image/png", "base64": b64}


def color(i: int = 0) -> str:
    s = PALETTE["series"]
    return s[int(i) % len(s)]


def plot_line(
    ax,
    x: Sequence[float],
    y: Sequence[float],
    *,
    color: Optional[str] = None,
    lw: float = 2.35,
    label: Optional[str] = None,
    alpha: float = 1.0,
    marker: Optional[str] = None,
    ms: float = 4.5,
) -> None:
    kw: Dict[str, Any] = {
        "color": color or PALETTE["primary"],
        "lw": lw,
        "alpha": alpha,
        "solid_capstyle": "round",
    }
    if label:
        kw["label"] = label
    if marker:
        kw["marker"] = marker
        kw["markersize"] = ms
        kw["markevery"] = max(1, len(x) // 12)
    ax.plot(list(x), list(y), **kw)


def annotate_vline(ax, x: float, text: str, color: Optional[str] = None) -> None:
    c = color or PALETTE["accent"]
    ax.axvline(x, color=c, ls="--", lw=1.15, alpha=0.85)
    ymin, ymax = ax.get_ylim()
    ax.text(
        x,
        ymax,
        f" {text}",
        color=c,
        fontsize=8.5,
        va="top",
        ha="left",
        rotation=90,
        clip_on=True,
    )


def annotate_hline(ax, y: float, text: str, color: Optional[str] = None) -> None:
    c = color or PALETTE["muted"]
    ax.axhline(y, color=c, ls="--", lw=1.05, alpha=0.8)
    xmax = ax.get_xlim()[1]
    ax.text(xmax, y, f" {text}", color=c, fontsize=8.5, va="center", ha="right")


def script_preamble() -> str:
    return '''\
# ResearchersHub constructive figure — publication style
import math
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError as e:
    raise SystemExit("pip install matplotlib") from e

PALETTE = {
    "primary": "#0b6e4f",
    "secondary": "#1d4ed8",
    "accent": "#d97706",
    "danger": "#be123c",
    "muted": "#64748b",
    "grid": "#e2e8f0",
    "panel": "#f8fafc",
    "ink": "#0f172a",
    "bg": "#ffffff",
    "series": ["#0b6e4f", "#1d4ed8", "#d97706", "#7c3aed", "#be123c", "#0891b2"],
}

def style_ax(ax):
    ax.set_facecolor(PALETTE["panel"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, ls="--", lw=0.7, color=PALETTE["grid"], alpha=0.95)
    ax.set_axisbelow(True)

def save(fig, path):
    fig.text(0.99, 0.01, "ResearchersHub · constructive simulation",
             ha="right", va="bottom", fontsize=7.5, color=PALETTE["muted"])
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=PALETTE["bg"])
    print("wrote", path)
'''
