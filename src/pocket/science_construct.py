"""ResearchersHub constructive science workflows.

Produces REAL runnable Python scripts and FULL chart images (PNG base64)
so chat replies include figures — not placeholders.
"""

from __future__ import annotations

import base64
import io
import json
import math
import re
import textwrap
import time
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

PRODUCT = "ResearchersHub"


def _home() -> Path:
    p = Path.home() / ".researchershub" / "construct"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _md_image(alt: str, b64: str, mime: str = "image/png") -> str:
    return f"![{alt}](data:{mime};base64,{b64})"


def _fig_to_b64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=140, bbox_inches="tight", facecolor="white")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("ascii")


def _try_matplotlib():
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    return plt


def chart_titration(n_points: int = 80) -> Dict[str, Any]:
    """Strong acid / strong base titration curve — real data + figure."""
    plt = _try_matplotlib()
    # 50 mL 0.1 M HCl titrated with 0.1 M NaOH
    v_base = [i * 100 / (n_points - 1) for i in range(n_points)]  # mL
    v_acid, c_acid, c_base = 50.0, 0.1, 0.1
    ph = []
    for vb in v_base:
        n_h = c_acid * v_acid / 1000
        n_oh = c_base * vb / 1000
        v_tot = (v_acid + vb) / 1000
        if abs(n_oh - n_h) < 1e-12:
            ph.append(7.0)
        elif n_oh < n_h:
            h = (n_h - n_oh) / v_tot
            ph.append(-math.log10(max(h, 1e-14)))
        else:
            oh = (n_oh - n_h) / v_tot
            ph.append(14 + math.log10(max(oh, 1e-14)))
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(v_base, ph, color="#0b6e4f", lw=2.2)
    ax.axhline(7, color="#888", ls="--", lw=0.8)
    ax.set_xlabel("Volume NaOH (mL)")
    ax.set_ylabel("pH")
    ax.set_title("Titration curve — 0.1 M HCl vs 0.1 M NaOH")
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        f'''\
        """ResearchersHub — titration curve (constructive workflow)."""
        import math
        import matplotlib.pyplot as plt

        v_base = {v_base!r}
        ph = {ph!r}

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(v_base, ph, color="#0b6e4f", lw=2.2)
        ax.axhline(7, color="#888", ls="--", lw=0.8)
        ax.set_xlabel("Volume NaOH (mL)")
        ax.set_ylabel("pH")
        ax.set_title("Titration curve — 0.1 M HCl vs 0.1 M NaOH")
        ax.grid(True, alpha=0.3)
        fig.savefig("titration_curve.png", dpi=160, bbox_inches="tight")
        print("wrote titration_curve.png")
        plt.show()
        '''
    )
    return {
        "kind": "titration",
        "title": "Acid–base titration curve",
        "script": script,
        "images": [{"alt": "Titration curve", "mime": "image/png", "base64": b64}],
        "summary": "Strong acid/strong base titration (0.1 M HCl, 50 mL) with 0.1 M NaOH. Equivalence near 50 mL, pH 7.",
    }


def chart_michaelis_menten() -> Dict[str, Any]:
    plt = _try_matplotlib()
    Km, Vmax = 2.5, 10.0
    s = [i * 0.2 for i in range(0, 101)]
    v = [Vmax * si / (Km + si) if (Km + si) else 0 for si in s]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(s, v, color="#1d4ed8", lw=2.2)
    ax.axhline(Vmax, color="#94a3b8", ls="--", label=f"Vmax={Vmax}")
    ax.axvline(Km, color="#f59e0b", ls="--", label=f"Km={Km}")
    ax.set_xlabel("[S]")
    ax.set_ylabel("v")
    ax.set_title("Michaelis–Menten kinetics")
    ax.legend()
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        f'''\
        """ResearchersHub — Michaelis–Menten constructive workflow."""
        import matplotlib.pyplot as plt

        Km, Vmax = {Km}, {Vmax}
        s = [i * 0.2 for i in range(0, 101)]
        v = [Vmax * si / (Km + si) for si in s]

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(s, v, lw=2.2)
        ax.axhline(Vmax, ls="--", label=f"Vmax={{Vmax}}")
        ax.axvline(Km, ls="--", label=f"Km={{Km}}")
        ax.set_xlabel("[S]"); ax.set_ylabel("v")
        ax.set_title("Michaelis–Menten kinetics")
        ax.legend(); ax.grid(True, alpha=0.3)
        fig.savefig("michaelis_menten.png", dpi=160, bbox_inches="tight")
        print("wrote michaelis_menten.png")
        plt.show()
        '''
    )
    return {
        "kind": "enzyme_kinetics",
        "title": "Michaelis–Menten",
        "script": script,
        "images": [{"alt": "Michaelis–Menten curve", "mime": "image/png", "base64": b64}],
        "summary": f"Hyperbolic rate curve with Km={Km}, Vmax={Vmax}.",
    }


def chart_dose_response() -> Dict[str, Any]:
    plt = _try_matplotlib()
    # logistic: response = bottom + (top-bottom)/(1+10**((logIC50-x)*hill))
    log_ic50, hill, top, bottom = 1.0, 1.2, 100.0, 0.0
    xs = [i * 0.05 for i in range(-20, 61)]  # log10 dose
    ys = [bottom + (top - bottom) / (1 + 10 ** ((log_ic50 - x) * hill)) for x in xs]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(xs, ys, color="#7c3aed", lw=2.2)
    ax.axvline(log_ic50, color="#f43f5e", ls="--", label=f"log10 IC50={log_ic50}")
    ax.set_xlabel("log10(dose)")
    ax.set_ylabel("% response")
    ax.set_title("Dose–response (4-parameter logistic)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        f'''\
        """ResearchersHub — dose–response constructive workflow."""
        import matplotlib.pyplot as plt

        log_ic50, hill, top, bottom = {log_ic50}, {hill}, {top}, {bottom}
        xs = [i * 0.05 for i in range(-20, 61)]
        ys = [bottom + (top - bottom) / (1 + 10 ** ((log_ic50 - x) * hill)) for x in xs]

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(xs, ys, color="#7c3aed", lw=2.2)
        ax.axvline(log_ic50, ls="--", label=f"log10 IC50={{log_ic50}}")
        ax.set_xlabel("log10(dose)"); ax.set_ylabel("% response")
        ax.set_title("Dose–response (4-parameter logistic)")
        ax.legend(); ax.grid(True, alpha=0.3)
        fig.savefig("dose_response.png", dpi=160, bbox_inches="tight")
        print("wrote dose_response.png")
        plt.show()
        '''
    )
    return {
        "kind": "dose_response",
        "title": "Dose–response curve",
        "script": script,
        "images": [{"alt": "Dose–response", "mime": "image/png", "base64": b64}],
        "summary": f"4PL curve with log10 IC50={log_ic50}, Hill={hill}.",
    }


def chart_arrhenius() -> Dict[str, Any]:
    plt = _try_matplotlib()
    # ln k vs 1/T
    R = 8.314
    Ea = 50000  # J/mol
    A = 1e12
    Ts = list(range(280, 361, 5))
    invT = [1 / T for T in Ts]
    lnk = [math.log(A) - Ea / (R * T) for T in Ts]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(invT, lnk, "o-", color="#dc2626", lw=1.8, ms=4)
    ax.set_xlabel("1/T (1/K)")
    ax.set_ylabel("ln k")
    ax.set_title(f"Arrhenius plot (Ea={Ea/1000:.0f} kJ/mol)")
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        f'''\
        """ResearchersHub — Arrhenius plot constructive workflow."""
        import math
        import matplotlib.pyplot as plt

        R, Ea, A = 8.314, {Ea}, {A}
        Ts = list(range(280, 361, 5))
        invT = [1/T for T in Ts]
        lnk = [math.log(A) - Ea/(R*T) for T in Ts]

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(invT, lnk, "o-", lw=1.8, ms=4)
        ax.set_xlabel("1/T (1/K)"); ax.set_ylabel("ln k")
        ax.set_title("Arrhenius plot (Ea={Ea/1000:.0f} kJ/mol)")
        ax.grid(True, alpha=0.3)
        fig.savefig("arrhenius.png", dpi=160, bbox_inches="tight")
        print("wrote arrhenius.png")
        plt.show()
        '''
    )
    return {
        "kind": "arrhenius",
        "title": "Arrhenius plot",
        "script": script,
        "images": [{"alt": "Arrhenius plot", "mime": "image/png", "base64": b64}],
        "summary": f"ln k vs 1/T with Ea={Ea/1000:.0f} kJ/mol.",
    }


def chart_beer_lambert() -> Dict[str, Any]:
    plt = _try_matplotlib()
    # A = ε c l  (ε=2.0, l=1 cm)
    eps, path = 2.0, 1.0
    conc = [i * 0.05 for i in range(0, 21)]
    abs_ = [eps * c * path for c in conc]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(conc, abs_, "s-", color="#0891b2", lw=2, ms=5)
    ax.set_xlabel("Concentration (M)")
    ax.set_ylabel("Absorbance")
    ax.set_title("Beer–Lambert calibration (ε=2.0 M⁻¹ cm⁻¹, l=1 cm)")
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        f'''\
        """ResearchersHub — Beer–Lambert calibration constructive workflow."""
        import matplotlib.pyplot as plt

        eps, path_cm = {eps}, {path}
        conc = [i * 0.05 for i in range(0, 21)]
        A = [eps * c * path_cm for c in conc]

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(conc, A, "s-", lw=2, ms=5)
        ax.set_xlabel("Concentration (M)"); ax.set_ylabel("Absorbance")
        ax.set_title("Beer–Lambert calibration")
        ax.grid(True, alpha=0.3)
        fig.savefig("beer_lambert.png", dpi=160, bbox_inches="tight")
        print("wrote beer_lambert.png")
        plt.show()
        '''
    )
    return {
        "kind": "beer_lambert",
        "title": "Beer–Lambert calibration",
        "script": script,
        "images": [{"alt": "Beer–Lambert", "mime": "image/png", "base64": b64}],
        "summary": "Linear A vs c calibration for UV-Vis.",
    }


def chart_linear_regression() -> Dict[str, Any]:
    plt = _try_matplotlib()
    xs = [1, 2, 3, 4, 5, 6, 7, 8]
    ys = [2.1, 3.9, 6.2, 7.8, 10.1, 11.9, 14.2, 15.8]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs) or 1.0
    slope = num / den
    intercept = my - slope * mx
    yhat = [slope * x + intercept for x in xs]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.scatter(xs, ys, color="#0f766e", s=40, label="data", zorder=3)
    ax.plot(xs, yhat, color="#b45309", lw=2, label=f"y={slope:.3f}x+{intercept:.3f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Linear regression (OLS)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        f'''\
        """ResearchersHub — linear regression constructive workflow."""
        import matplotlib.pyplot as plt

        xs = {xs!r}
        ys = {ys!r}
        n = len(xs)
        mx, my = sum(xs)/n, sum(ys)/n
        slope = sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / sum((x-mx)**2 for x in xs)
        intercept = my - slope*mx
        yhat = [slope*x + intercept for x in xs]

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.scatter(xs, ys, s=40, label="data", zorder=3)
        ax.plot(xs, yhat, lw=2, label=f"y={{slope:.3f}}x+{{intercept:.3f}}")
        ax.set_xlabel("x"); ax.set_ylabel("y")
        ax.set_title("Linear regression (OLS)")
        ax.legend(); ax.grid(True, alpha=0.3)
        fig.savefig("linear_regression.png", dpi=160, bbox_inches="tight")
        print("wrote linear_regression.png", "slope", slope, "intercept", intercept)
        plt.show()
        '''
    )
    return {
        "kind": "linear_regression",
        "title": "Linear regression",
        "script": script,
        "images": [{"alt": "Linear regression fit", "mime": "image/png", "base64": b64}],
        "summary": f"OLS fit slope={slope:.4f}, intercept={intercept:.4f}.",
    }


def chart_stress_strain() -> Dict[str, Any]:
    plt = _try_matplotlib()
    strain = [i * 0.002 for i in range(0, 80)]
    E = 200e3  # MPa-ish synthetic
    stress = []
    for e in strain:
        if e < 0.02:
            stress.append(E * e / 1000)  # elastic scaled for plot
        else:
            # plastic plateau + work hardening
            stress.append(E * 0.02 / 1000 + 80 * (e - 0.02) ** 0.5)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(strain, stress, color="#334155", lw=2.2)
    ax.set_xlabel("Strain")
    ax.set_ylabel("Stress (arb.)")
    ax.set_title("Stress–strain (synthetic ductile)")
    ax.grid(True, alpha=0.3)
    b64 = _fig_to_b64(fig)
    plt.close(fig)
    script = textwrap.dedent(
        '''\
        """ResearchersHub — stress–strain constructive workflow."""
        import matplotlib.pyplot as plt

        strain = [i * 0.002 for i in range(0, 80)]
        E = 200e3
        stress = []
        for e in strain:
            if e < 0.02:
                stress.append(E * e / 1000)
            else:
                stress.append(E * 0.02 / 1000 + 80 * (e - 0.02) ** 0.5)

        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(strain, stress, lw=2.2)
        ax.set_xlabel("Strain"); ax.set_ylabel("Stress (arb.)")
        ax.set_title("Stress–strain (synthetic ductile)")
        ax.grid(True, alpha=0.3)
        fig.savefig("stress_strain.png", dpi=160, bbox_inches="tight")
        print("wrote stress_strain.png")
        plt.show()
        '''
    )
    return {
        "kind": "stress_strain",
        "title": "Stress–strain curve",
        "script": script,
        "images": [{"alt": "Stress–strain", "mime": "image/png", "base64": b64}],
        "summary": "Synthetic ductile metal: elastic region then plastic hardening.",
    }


def generic_science_script(topic: str) -> Dict[str, Any]:
    """Always-available constructive Python workflow for any research topic."""
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", (topic or "experiment")[:48]).strip("_") or "experiment"
    script = textwrap.dedent(
        f'''\
        #!/usr/bin/env python3
        """ResearchersHub constructive workflow: {topic}

        Steps:
          1) define parameters
          2) simulate / transform data
          3) write CSV results
          4) plot publication-style figure
        """
        from __future__ import annotations

        import csv
        import math
        from pathlib import Path

        try:
            import matplotlib.pyplot as plt
        except ImportError as e:
            raise SystemExit("pip install matplotlib") from e

        OUT = Path(__file__).resolve().parent
        TOPIC = {topic!r}

        def simulate(n: int = 100):
            xs, ys = [], []
            for i in range(n):
                x = i / (n - 1) * 10.0
                # constructive demo signal: damped sinusoid + mild trend
                y = math.exp(-0.15 * x) * math.sin(1.3 * x) + 0.05 * x
                xs.append(x)
                ys.append(y)
            return xs, ys

        def write_csv(path: Path, xs, ys):
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["x", "y", "topic"])
                for x, y in zip(xs, ys):
                    w.writerow([f"{{x:.6f}}", f"{{y:.6f}}", TOPIC])

        def plot(xs, ys, path: Path):
            fig, ax = plt.subplots(figsize=(7.2, 4.4))
            ax.plot(xs, ys, color="#0b6e4f", lw=2.0)
            ax.set_title(f"ResearchersHub — {{TOPIC}}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True, alpha=0.3)
            fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
            plt.close(fig)

        def main():
            xs, ys = simulate()
            csv_path = OUT / f"{safe}_results.csv"
            png_path = OUT / f"{safe}_figure.png"
            write_csv(csv_path, xs, ys)
            plot(xs, ys, png_path)
            print("OK")
            print("csv:", csv_path)
            print("figure:", png_path)

        if __name__ == "__main__":
            main()
        '''
    )
    # Also produce a live figure for chat
    images: List[Dict[str, str]] = []
    try:
        plt = _try_matplotlib()
        xs = [i / 99 * 10.0 for i in range(100)]
        ys = [math.exp(-0.15 * x) * math.sin(1.3 * x) + 0.05 * x for x in xs]
        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        ax.plot(xs, ys, color="#0b6e4f", lw=2.0)
        ax.set_title(f"ResearchersHub — {topic[:60]}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True, alpha=0.3)
        b64 = _fig_to_b64(fig)
        plt.close(fig)
        images.append({"alt": f"Figure: {topic[:40]}", "mime": "image/png", "base64": b64})
    except Exception:
        pass
    return {
        "kind": "generic_workflow",
        "title": f"Constructive workflow: {topic[:80]}",
        "script": script,
        "images": images,
        "summary": "Runnable multi-step Python workflow: simulate → CSV → figure.",
    }


_ROUTES: List[Tuple[re.Pattern, Any]] = [
    (re.compile(r"titrat|ph\s*curve|acid.?base", re.I), chart_titration),
    (re.compile(r"michaelis|enzyme\s*kinet|mm\s*kinet|km\b|vmax", re.I), chart_michaelis_menten),
    (re.compile(r"dose.?response|ic50|ec50|hill\s*slope", re.I), chart_dose_response),
    (re.compile(r"arrhenius|activation\s*energy|ln\s*k", re.I), chart_arrhenius),
    (re.compile(r"beer|lambert|absorbance|uv.?vis|calibration\s*curve", re.I), chart_beer_lambert),
    (re.compile(r"regress|linear\s*fit|least\s*squares|ols", re.I), chart_linear_regression),
    (re.compile(r"stress.?strain|tensile|young.?s?\s*modulus", re.I), chart_stress_strain),
]


def detect_construct(prompt: str) -> Optional[str]:
    p = prompt or ""
    for rx, fn in _ROUTES:
        if rx.search(p):
            return fn.__name__
    # broad science / chart intent
    if re.search(
        r"\b(chart|plot|figure|graph|image|matplotlib|python\s+script|workflow|"
        r"chemistry|chem|spectrum|kinetics|thermodynamics|research|"
        r"scientist|lab\s*report|construct)\b",
        p,
        re.I,
    ):
        return "generic_science_script"
    return None


def run_construct(prompt: str, skill_id: str = "") -> Dict[str, Any]:
    """Build constructive payload: scripts + full images + markdown for chat."""
    p = (prompt or "").strip()
    sid = (skill_id or "").lower()
    result: Dict[str, Any]
    try:
        if "titrat" in sid or re.search(r"titrat|acid.?base", p, re.I):
            result = chart_titration()
        elif "enzyme" in sid or "michaelis" in sid or re.search(r"michaelis|enzyme", p, re.I):
            result = chart_michaelis_menten()
        elif "dose" in sid or re.search(r"dose.?response|ic50", p, re.I):
            result = chart_dose_response()
        elif "arrhenius" in sid or re.search(r"arrhenius", p, re.I):
            result = chart_arrhenius()
        elif "beer" in sid or "uvvis" in sid or re.search(r"beer|lambert|absorbance", p, re.I):
            result = chart_beer_lambert()
        elif "regress" in sid or re.search(r"regress|linear\s*fit", p, re.I):
            result = chart_linear_regression()
        elif "stress" in sid or re.search(r"stress.?strain", p, re.I):
            result = chart_stress_strain()
        else:
            topic = p[:120] if p else "research experiment"
            result = generic_science_script(topic)
    except Exception as e:
        result = {
            "kind": "error",
            "title": "Construct failed",
            "script": f"# error\n# {e}\n",
            "images": [],
            "summary": f"Could not build figure: {e}",
            "traceback": traceback.format_exc()[-800:],
        }

    # Persist script to disk for researcher reuse
    home = _home()
    stamp = time.strftime("%Y%m%d_%H%M%S")
    kind = re.sub(r"[^a-z0-9_]+", "_", (result.get("kind") or "workflow").lower())
    script_path = home / f"{stamp}_{kind}.py"
    try:
        script_path.write_text(result.get("script") or "", encoding="utf-8")
        result["script_path"] = str(script_path)
    except Exception:
        result["script_path"] = ""

    # Also save PNGs
    saved_imgs = []
    for i, img in enumerate(result.get("images") or []):
        try:
            raw = base64.b64decode(img["base64"])
            ip = home / f"{stamp}_{kind}_{i}.png"
            ip.write_bytes(raw)
            saved_imgs.append(str(ip))
        except Exception:
            pass
    result["image_paths"] = saved_imgs
    result["product"] = PRODUCT
    result["markdown"] = format_construct_markdown(result)
    return result


def format_construct_markdown(result: Dict[str, Any]) -> str:
    """Full chat body: prose + WHOLE images + complete Python script."""
    lines: List[str] = []
    lines.append(f"### {result.get('title') or 'ResearchersHub constructive result'}")
    if result.get("summary"):
        lines.append("")
        lines.append(result["summary"])
    lines.append("")
    lines.append("#### Figures (full images)")
    imgs = result.get("images") or []
    if not imgs:
        lines.append("_No figure generated (matplotlib may be missing)._")
    for img in imgs:
        lines.append("")
        lines.append(_md_image(img.get("alt") or "figure", img.get("base64") or "", img.get("mime") or "image/png"))
    lines.append("")
    lines.append("#### Real Python script (constructive workflow)")
    if result.get("script_path"):
        lines.append(f"Saved on disk: `{result['script_path']}`")
    lines.append("")
    lines.append("```python")
    lines.append((result.get("script") or "").rstrip())
    lines.append("```")
    lines.append("")
    lines.append(
        "_ResearchersHub returns complete charts as embedded images and runnable scripts — "
        "not truncated placeholders._"
    )
    return "\n".join(lines)


def enrich_chat_text(text: str, user_prompt: str = "", force: bool = False) -> Dict[str, Any]:
    """Append constructive science block when the prompt warrants it."""
    want = force or bool(detect_construct(user_prompt or text or ""))
    if not want:
        return {"text": text, "construct": None, "images": []}
    c = run_construct(user_prompt or text)
    md = c.get("markdown") or ""
    # Prefer construct figures first, then agent text
    merged = md
    if text and text.strip() and text.strip() not in md:
        merged = md + "\n\n---\n\n#### Model notes\n\n" + text.strip()
    return {
        "text": merged,
        "construct": {
            "kind": c.get("kind"),
            "script_path": c.get("script_path"),
            "image_paths": c.get("image_paths"),
            "summary": c.get("summary"),
        },
        "images": c.get("images") or [],
    }


def multi_figure_board(prompt: str = "") -> Dict[str, Any]:
    """Return several science charts at once for rich chat."""
    builders = [
        chart_titration,
        chart_michaelis_menten,
        chart_dose_response,
        chart_beer_lambert,
        chart_linear_regression,
    ]
    images: List[Dict[str, str]] = []
    scripts: List[str] = []
    for fn in builders:
        try:
            r = fn()
            images.extend(r.get("images") or [])
            scripts.append(f"# --- {r.get('title')} ---\n{r.get('script')}")
        except Exception as e:
            scripts.append(f"# {fn.__name__} failed: {e}")
    bundle_script = "\n\n".join(scripts)
    home = _home()
    path = home / f"board_{int(time.time())}.py"
    path.write_text(bundle_script, encoding="utf-8")
    result = {
        "kind": "image_board",
        "title": "ResearchersHub multi-figure board",
        "script": bundle_script,
        "script_path": str(path),
        "images": images,
        "summary": f"{len(images)} full charts for science chat: titration, enzyme, dose–response, Beer–Lambert, regression.",
        "product": PRODUCT,
    }
    result["markdown"] = format_construct_markdown(result)
    return result
