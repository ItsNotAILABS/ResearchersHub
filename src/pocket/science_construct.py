"""ResearchersHub constructive science workflows — designed figures + simulations.

Produces REAL runnable Python scripts and FULL chart images (PNG base64)
with a shared publication design system (science_render).
"""

from __future__ import annotations

import base64
import math
import random
import re
import textwrap
import time
import traceback
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from pocket.science_render import (
    PALETTE,
    annotate_hline,
    annotate_vline,
    brand_footer,
    color,
    finish,
    new_axes,
    plot_line,
    script_preamble,
    style_ax,
    try_plt,
)

PRODUCT = "ResearchersHub"


def _home() -> Path:
    p = Path.home() / ".researchershub" / "construct"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _md_image(alt: str, b64: str, mime: str = "image/png") -> str:
    return f"![{alt}](data:{mime};base64,{b64})"


def _pack(
    kind: str,
    title: str,
    summary: str,
    script: str,
    images: List[Dict[str, str]],
    *,
    workflow: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "kind": kind,
        "title": title,
        "summary": summary,
        "script": script,
        "images": images,
        "workflow_steps": workflow
        or [
            "1. Define parameters",
            "2. Simulate / transform data",
            "3. Render publication figure",
            "4. Export script + PNG on disk",
            "5. Link into Atlas research graph",
        ],
        "design": "researchershub.publication.v2",
        "product": PRODUCT,
    }


# ── Charts / simulations ─────────────────────────────────────────────


def chart_titration(n_points: int = 120) -> Dict[str, Any]:
    v_base = [i * 100 / (n_points - 1) for i in range(n_points)]
    v_acid, c_acid, c_base = 50.0, 0.1, 0.1
    ph = []
    for vb in v_base:
        n_h = c_acid * v_acid / 1000
        n_oh = c_base * vb / 1000
        v_tot = (v_acid + vb) / 1000
        if abs(n_oh - n_h) < 1e-12:
            ph.append(7.0)
        elif n_oh < n_h:
            ph.append(-math.log10(max((n_h - n_oh) / v_tot, 1e-14)))
        else:
            ph.append(14 + math.log10(max((n_oh - n_h) / v_tot, 1e-14)))
    plt, fig, ax = new_axes((8.0, 4.8))
    plot_line(ax, v_base, ph, color=PALETTE["primary"], lw=2.6)
    ax.fill_between(v_base, ph, 7, where=[p >= 7 for p in ph], color=PALETTE["secondary"], alpha=0.08)
    ax.fill_between(v_base, ph, 7, where=[p < 7 for p in ph], color=PALETTE["accent"], alpha=0.08)
    annotate_hline(ax, 7.0, "pH 7")
    annotate_vline(ax, 50.0, "equiv. ~50 mL", PALETTE["danger"])
    ax.set_xlabel("Volume NaOH (mL)")
    ax.set_ylabel("pH")
    ax.set_title("Strong acid–base titration · 0.1 M HCl (50 mL) vs 0.1 M NaOH")
    ax.set_ylim(-0.2, 14.2)
    img = finish(fig, plt, alt="Titration curve")
    script = script_preamble() + textwrap.dedent(
        f"""
        v_base = {v_base!r}
        ph = {ph!r}
        fig, ax = plt.subplots(figsize=(8.0, 4.8))
        style_ax(ax)
        ax.plot(v_base, ph, color=PALETTE["primary"], lw=2.6)
        ax.axhline(7, color=PALETTE["muted"], ls="--", lw=1.05)
        ax.axvline(50, color=PALETTE["danger"], ls="--", lw=1.15)
        ax.set_xlabel("Volume NaOH (mL)"); ax.set_ylabel("pH")
        ax.set_title("Strong acid–base titration")
        save(fig, "titration_curve.png"); plt.close()
        """
    )
    return _pack(
        "titration",
        "Acid–base titration curve",
        "Publication titration of 0.1 M HCl (50 mL) with 0.1 M NaOH. Equivalence near 50 mL, pH 7.",
        script,
        [img],
        workflow=[
            "1. Define acid/base volumes and concentrations",
            "2. Compute excess H+/OH− and pH along the curve",
            "3. Mark equivalence and neutrality",
            "4. Export figure + Python workflow",
        ],
    )


def chart_michaelis_menten() -> Dict[str, Any]:
    Km, Vmax = 2.5, 10.0
    s = [i * 0.15 for i in range(0, 121)]
    v = [Vmax * si / (Km + si) for si in s]
    plt, fig, ax = new_axes()
    plot_line(ax, s, v, color=PALETTE["secondary"], lw=2.6, label="v = Vmax·[S]/(Km+[S])")
    annotate_hline(ax, Vmax, f"Vmax={Vmax}")
    annotate_vline(ax, Km, f"Km={Km}", PALETTE["accent"])
    # half-Vmax point
    ax.scatter([Km], [Vmax / 2], s=48, zorder=5, color=PALETTE["accent"], edgecolors="white", lw=0.8)
    ax.set_xlabel("[S] (arb.)")
    ax.set_ylabel("Initial rate v")
    ax.set_title("Michaelis–Menten kinetics")
    ax.legend(loc="lower right")
    img = finish(fig, plt, alt="Michaelis–Menten")
    script = script_preamble() + textwrap.dedent(
        f"""
        Km, Vmax = {Km}, {Vmax}
        s = [i * 0.15 for i in range(0, 121)]
        v = [Vmax * si / (Km + si) for si in s]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(s, v, color=PALETTE["secondary"], lw=2.6)
        ax.axhline(Vmax, ls="--", color=PALETTE["muted"]); ax.axvline(Km, ls="--", color=PALETTE["accent"])
        ax.set_xlabel("[S]"); ax.set_ylabel("v"); ax.set_title("Michaelis–Menten")
        save(fig, "michaelis_menten.png"); plt.close()
        """
    )
    return _pack(
        "enzyme_kinetics",
        "Michaelis–Menten",
        f"Hyperbolic rate law with Km={Km}, Vmax={Vmax}; half-Vmax marked at Km.",
        script,
        [img],
    )


def chart_dose_response() -> Dict[str, Any]:
    log_ic50, hill, top, bottom = 1.0, 1.2, 100.0, 0.0
    xs = [i * 0.05 for i in range(-20, 61)]
    ys = [bottom + (top - bottom) / (1 + 10 ** ((log_ic50 - x) * hill)) for x in xs]
    plt, fig, ax = new_axes()
    plot_line(ax, xs, ys, color="#7c3aed", lw=2.6, label="4-parameter logistic")
    annotate_vline(ax, log_ic50, f"log10 IC50={log_ic50}", PALETTE["danger"])
    annotate_hline(ax, 50, "50% response")
    ax.set_xlabel("log₁₀(dose)")
    ax.set_ylabel("% response")
    ax.set_title("Dose–response (4PL)")
    ax.legend(loc="lower right")
    img = finish(fig, plt, alt="Dose–response")
    script = script_preamble() + textwrap.dedent(
        f"""
        log_ic50, hill, top, bottom = {log_ic50}, {hill}, {top}, {bottom}
        xs = [i * 0.05 for i in range(-20, 61)]
        ys = [bottom + (top - bottom) / (1 + 10 ** ((log_ic50 - x) * hill)) for x in xs]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(xs, ys, color="#7c3aed", lw=2.6)
        ax.axvline(log_ic50, ls="--", color=PALETTE["danger"])
        ax.set_xlabel("log10(dose)"); ax.set_ylabel("% response"); ax.set_title("Dose–response")
        save(fig, "dose_response.png"); plt.close()
        """
    )
    return _pack(
        "dose_response",
        "Dose–response curve",
        f"4PL curve with log10 IC50={log_ic50}, Hill={hill}.",
        script,
        [img],
    )


def chart_arrhenius() -> Dict[str, Any]:
    R, Ea, A = 8.314, 50000, 1e12
    Ts = list(range(280, 361, 4))
    invT = [1 / T for T in Ts]
    lnk = [math.log(A) - Ea / (R * T) for T in Ts]
    plt, fig, ax = new_axes()
    ax.plot(invT, lnk, "o-", color=PALETTE["danger"], lw=1.9, ms=5.5, markerfacecolor="white", markeredgewidth=1.4)
    ax.set_xlabel("1/T (1/K)")
    ax.set_ylabel("ln k")
    ax.set_title(f"Arrhenius plot · Ea = {Ea/1000:.0f} kJ/mol")
    img = finish(fig, plt, alt="Arrhenius plot")
    script = script_preamble() + textwrap.dedent(
        f"""
        R, Ea, A = 8.314, {Ea}, {A}
        Ts = list(range(280, 361, 4))
        invT = [1/T for T in Ts]
        lnk = [math.log(A) - Ea/(R*T) for T in Ts]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(invT, lnk, "o-", color=PALETTE["danger"], lw=1.9, ms=5)
        ax.set_xlabel("1/T"); ax.set_ylabel("ln k"); ax.set_title("Arrhenius")
        save(fig, "arrhenius.png"); plt.close()
        """
    )
    return _pack("arrhenius", "Arrhenius plot", f"ln k vs 1/T with Ea={Ea/1000:.0f} kJ/mol.", script, [img])


def chart_beer_lambert() -> Dict[str, Any]:
    eps, path_cm = 2.0, 1.0
    conc = [i * 0.05 for i in range(0, 21)]
    abs_ = [eps * c * path_cm for c in conc]
    # slight noise for realism
    rng = random.Random(7)
    abs_n = [a + rng.uniform(-0.03, 0.03) for a in abs_]
    plt, fig, ax = new_axes()
    ax.plot(conc, abs_, color=PALETTE["muted"], lw=1.4, ls="--", label="ideal A=εcl")
    ax.scatter(conc, abs_n, s=42, color="#0891b2", zorder=3, edgecolors="white", lw=0.7, label="simulated readings")
    ax.set_xlabel("Concentration (M)")
    ax.set_ylabel("Absorbance")
    ax.set_title("Beer–Lambert calibration · ε=2.0 M⁻¹ cm⁻¹, ℓ=1 cm")
    ax.legend(loc="upper left")
    img = finish(fig, plt, alt="Beer–Lambert")
    script = script_preamble() + textwrap.dedent(
        f"""
        conc = {conc!r}
        A = {abs_!r}
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(conc, A, color=PALETTE["muted"], ls="--")
        ax.scatter(conc, A, color="#0891b2", s=40)
        ax.set_xlabel("Concentration"); ax.set_ylabel("Absorbance")
        ax.set_title("Beer–Lambert")
        save(fig, "beer_lambert.png"); plt.close()
        """
    )
    return _pack("beer_lambert", "Beer–Lambert calibration", "Linear A vs c calibration for UV-Vis.", script, [img])


def chart_linear_regression() -> Dict[str, Any]:
    xs = [1, 2, 3, 4, 5, 6, 7, 8]
    ys = [2.1, 3.9, 6.2, 7.8, 10.1, 11.9, 14.2, 15.8]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    intercept = my - slope * mx
    yhat = [slope * x + intercept for x in xs]
    resid = [y - yh for y, yh in zip(ys, yhat)]
    plt = try_plt()
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(9.4, 4.2), gridspec_kw={"width_ratios": [1.35, 1]})
    style_ax(ax0)
    style_ax(ax1)
    ax0.scatter(xs, ys, s=52, color=PALETTE["primary"], zorder=3, edgecolors="white", lw=0.8, label="data")
    plot_line(ax0, xs, yhat, color=PALETTE["accent"], lw=2.2, label=f"y={slope:.3f}x+{intercept:.3f}")
    ax0.set_xlabel("x")
    ax0.set_ylabel("y")
    ax0.set_title("Linear regression (OLS)")
    ax0.legend(loc="upper left")
    ax1.axhline(0, color=PALETTE["muted"], lw=1)
    ax1.stem(xs, resid, linefmt=PALETTE["secondary"], markerfmt="o", basefmt=" ")
    ax1.set_xlabel("x")
    ax1.set_ylabel("residual")
    ax1.set_title("Residuals")
    img = finish(fig, plt, alt="Linear regression + residuals")
    script = script_preamble() + textwrap.dedent(
        f"""
        xs, ys = {xs!r}, {ys!r}
        n = len(xs); mx, my = sum(xs)/n, sum(ys)/n
        slope = sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / sum((x-mx)**2 for x in xs)
        intercept = my - slope*mx
        yhat = [slope*x+intercept for x in xs]
        resid = [y-yh for y,yh in zip(ys,yhat)]
        fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(9.4, 4.2))
        for a in (ax0, ax1): style_ax(a)
        ax0.scatter(xs, ys); ax0.plot(xs, yhat, color=PALETTE["accent"])
        ax0.set_title("OLS fit"); ax1.stem(xs, resid); ax1.set_title("Residuals")
        save(fig, "linear_regression.png"); plt.close()
        """
    )
    return _pack(
        "linear_regression",
        "Linear regression + residuals",
        f"OLS fit slope={slope:.4f}, intercept={intercept:.4f} with residual panel.",
        script,
        [img],
        workflow=[
            "1. Load x/y assay points",
            "2. Fit OLS slope and intercept",
            "3. Plot fit + residual diagnostics",
            "4. Export dual-panel figure and script",
        ],
    )


def chart_stress_strain() -> Dict[str, Any]:
    strain = [i * 0.002 for i in range(0, 90)]
    E = 200e3
    stress = []
    for e in strain:
        if e < 0.02:
            stress.append(E * e / 1000)
        else:
            stress.append(E * 0.02 / 1000 + 90 * (e - 0.02) ** 0.55)
    plt, fig, ax = new_axes()
    plot_line(ax, strain, stress, color="#334155", lw=2.5)
    ax.axvspan(0, 0.02, color=PALETTE["secondary"], alpha=0.06, label="elastic")
    ax.axvspan(0.02, strain[-1], color=PALETTE["accent"], alpha=0.05, label="plastic")
    ax.set_xlabel("Strain")
    ax.set_ylabel("Stress (arb.)")
    ax.set_title("Stress–strain · synthetic ductile response")
    ax.legend(loc="lower right")
    img = finish(fig, plt, alt="Stress–strain")
    script = script_preamble() + textwrap.dedent(
        """
        strain = [i * 0.002 for i in range(0, 90)]
        E = 200e3
        stress = []
        for e in strain:
            stress.append(E*e/1000 if e < 0.02 else E*0.02/1000 + 90*(e-0.02)**0.55)
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(strain, stress, color="#334155", lw=2.5)
        ax.set_xlabel("Strain"); ax.set_ylabel("Stress"); ax.set_title("Stress–strain")
        save(fig, "stress_strain.png"); plt.close()
        """
    )
    return _pack("stress_strain", "Stress–strain curve", "Elastic region then plastic hardening.", script, [img])


def chart_sir_epidemic() -> Dict[str, Any]:
    """SIR compartmental simulation."""
    N, beta, gamma = 10000, 0.28, 0.08
    S, I, R = N - 25, 25.0, 0.0
    dt, days = 0.25, 120
    t, Ss, Is, Rs = [0.0], [S], [I], [R]
    steps = int(days / dt)
    for k in range(steps):
        dS = -beta * S * I / N
        dI = beta * S * I / N - gamma * I
        dR = gamma * I
        S += dS * dt
        I += dI * dt
        R += dR * dt
        t.append((k + 1) * dt)
        Ss.append(S)
        Is.append(I)
        Rs.append(R)
    plt, fig, ax = new_axes((8.2, 4.8))
    plot_line(ax, t, Ss, color=PALETTE["secondary"], label="Susceptible", lw=2.2)
    plot_line(ax, t, Is, color=PALETTE["danger"], label="Infectious", lw=2.4)
    plot_line(ax, t, Rs, color=PALETTE["primary"], label="Recovered", lw=2.2)
    ax.set_xlabel("Day")
    ax.set_ylabel("People")
    ax.set_title(f"SIR epidemic simulation · β={beta}, γ={gamma}, R₀≈{beta/gamma:.2f}")
    ax.legend(loc="center right")
    img = finish(fig, plt, alt="SIR epidemic")
    script = script_preamble() + textwrap.dedent(
        f"""
        # SIR Euler integration
        N, beta, gamma = {N}, {beta}, {gamma}
        S, I, R = N-25, 25.0, 0.0
        dt, days = 0.25, 120
        t, Ss, Is, Rs = [0.0], [S], [I], [R]
        for k in range(int(days/dt)):
            dS = -beta*S*I/N; dI = beta*S*I/N - gamma*I; dR = gamma*I
            S += dS*dt; I += dI*dt; R += dR*dt
            t.append((k+1)*dt); Ss.append(S); Is.append(I); Rs.append(R)
        fig, ax = plt.subplots(figsize=(8.2, 4.8)); style_ax(ax)
        ax.plot(t, Ss, label="S"); ax.plot(t, Is, label="I"); ax.plot(t, Rs, label="R")
        ax.legend(); ax.set_title("SIR"); save(fig, "sir_epidemic.png"); plt.close()
        """
    )
    return _pack(
        "sir_epidemic",
        "SIR epidemic simulation",
        f"Compartmental SIR with R₀≈{beta/gamma:.2f}; full trajectories for S, I, R.",
        script,
        [img],
        workflow=[
            "1. Set population N, β, γ",
            "2. Integrate SIR ODEs (Euler)",
            "3. Plot S/I/R trajectories",
            "4. Export simulation script + figure",
        ],
    )


def chart_lotka_volterra() -> Dict[str, Any]:
    alpha, beta, delta, gamma = 1.1, 0.4, 0.1, 0.4
    x, y = 10.0, 5.0
    dt, n = 0.02, 1800
    t, xs, ys = [0.0], [x], [y]
    for k in range(n):
        dx = alpha * x - beta * x * y
        dy = delta * x * y - gamma * y
        x += dx * dt
        y += dy * dt
        t.append((k + 1) * dt)
        xs.append(x)
        ys.append(y)
    plt = try_plt()
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(9.6, 4.3))
    style_ax(ax0)
    style_ax(ax1)
    plot_line(ax0, t, xs, color=PALETTE["primary"], label="prey", lw=2.1)
    plot_line(ax0, t, ys, color=PALETTE["danger"], label="predator", lw=2.1)
    ax0.set_xlabel("time")
    ax0.set_ylabel("population")
    ax0.set_title("Lotka–Volterra time series")
    ax0.legend()
    ax1.plot(xs, ys, color=PALETTE["secondary"], lw=1.6)
    ax1.set_xlabel("prey")
    ax1.set_ylabel("predator")
    ax1.set_title("Phase portrait")
    img = finish(fig, plt, alt="Lotka–Volterra")
    script = script_preamble() + textwrap.dedent(
        f"""
        alpha, beta, delta, gamma = {alpha}, {beta}, {delta}, {gamma}
        x, y = 10.0, 5.0
        dt, n = 0.02, 1800
        t, xs, ys = [0.0], [x], [y]
        for k in range(n):
            dx = alpha*x - beta*x*y; dy = delta*x*y - gamma*y
            x += dx*dt; y += dy*dt
            t.append((k+1)*dt); xs.append(x); ys.append(y)
        fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(9.6, 4.3))
        for a in (ax0, ax1): style_ax(a)
        ax0.plot(t, xs); ax0.plot(t, ys); ax1.plot(xs, ys)
        ax0.set_title("time"); ax1.set_title("phase")
        save(fig, "lotka_volterra.png"); plt.close()
        """
    )
    return _pack(
        "lotka_volterra",
        "Lotka–Volterra predator–prey",
        "Coupled ODE simulation: time series + phase portrait.",
        script,
        [img],
    )


def chart_radioactive_decay() -> Dict[str, Any]:
    half = 8.0  # days
    lam = math.log(2) / half
    t = [i * 0.25 for i in range(0, 161)]
    n0 = 1000.0
    n = [n0 * math.exp(-lam * ti) for ti in t]
    plt, fig, ax = new_axes()
    plot_line(ax, t, n, color="#7c3aed", lw=2.5, label="N(t)=N₀ e^(−λt)")
    annotate_vline(ax, half, f"t½={half} d", PALETTE["accent"])
    annotate_hline(ax, n0 / 2, "N₀/2")
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Nuclei (arb.)")
    ax.set_title("Radioactive decay simulation")
    ax.legend()
    img = finish(fig, plt, alt="Radioactive decay")
    script = script_preamble() + textwrap.dedent(
        f"""
        half, n0 = {half}, {n0}
        lam = math.log(2)/half
        t = [i*0.25 for i in range(0, 161)]
        n = [n0*math.exp(-lam*ti) for ti in t]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(t, n, color="#7c3aed", lw=2.5)
        ax.axvline(half, ls="--"); ax.set_title("Decay")
        save(fig, "radioactive_decay.png"); plt.close()
        """
    )
    return _pack("radioactive_decay", "Radioactive decay", f"Exponential decay with t½={half} days.", script, [img])


def chart_binding_isotherm() -> Dict[str, Any]:
    Kd, Bmax = 3.0, 100.0
    L = [i * 0.25 for i in range(0, 81)]
    B = [Bmax * li / (Kd + li) for li in L]
    plt, fig, ax = new_axes()
    plot_line(ax, L, B, color=PALETTE["primary"], lw=2.5, label="Langmuir / single-site")
    annotate_vline(ax, Kd, f"Kd={Kd}", PALETTE["accent"])
    annotate_hline(ax, Bmax / 2, "Bmax/2")
    ax.set_xlabel("[Ligand]")
    ax.set_ylabel("Bound")
    ax.set_title("Binding isotherm (single-site)")
    ax.legend(loc="lower right")
    img = finish(fig, plt, alt="Binding isotherm")
    script = script_preamble() + textwrap.dedent(
        f"""
        Kd, Bmax = {Kd}, {Bmax}
        L = [i*0.25 for i in range(0, 81)]
        B = [Bmax*li/(Kd+li) for li in L]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(L, B, color=PALETTE["primary"], lw=2.5)
        ax.set_title("Binding isotherm"); save(fig, "binding_isotherm.png"); plt.close()
        """
    )
    return _pack("binding_isotherm", "Binding isotherm", f"Single-site binding with Kd={Kd}, Bmax={Bmax}.", script, [img])


def chart_volcano() -> Dict[str, Any]:
    rng = random.Random(11)
    n = 400
    logfc = [rng.gauss(0, 1.1) for _ in range(n)]
    p = [min(1.0, max(1e-12, abs(rng.gauss(0.2, 0.35)))) for _ in range(n)]
    # enrich some hits
    for i in range(18):
        logfc[i] = rng.choice([-1, 1]) * rng.uniform(1.2, 3.5)
        p[i] = 10 ** (-rng.uniform(3, 8))
    neglogp = [-math.log10(pi) for pi in p]
    plt, fig, ax = new_axes((7.8, 5.0))
    cols = []
    for fc, nlp in zip(logfc, neglogp):
        if nlp > 1.3 and abs(fc) > 1:
            cols.append(PALETTE["danger"] if fc > 0 else PALETTE["secondary"])
        else:
            cols.append("#94a3b8")
    ax.scatter(logfc, neglogp, c=cols, s=18, alpha=0.75, edgecolors="none")
    ax.axhline(1.3, color=PALETTE["muted"], ls="--", lw=1)
    ax.axvline(-1, color=PALETTE["muted"], ls=":", lw=1)
    ax.axvline(1, color=PALETTE["muted"], ls=":", lw=1)
    ax.set_xlabel("log₂ fold-change")
    ax.set_ylabel("−log₁₀ p")
    ax.set_title("Volcano plot · differential abundance (simulated)")
    img = finish(fig, plt, alt="Volcano plot")
    script = script_preamble() + textwrap.dedent(
        """
        import random
        rng = random.Random(11)
        logfc = [rng.gauss(0, 1.1) for _ in range(400)]
        p = [min(1.0, max(1e-12, abs(rng.gauss(0.2, 0.35)))) for _ in range(400)]
        neglogp = [-math.log10(pi) for pi in p]
        fig, ax = plt.subplots(figsize=(7.8, 5.0)); style_ax(ax)
        ax.scatter(logfc, neglogp, s=16, alpha=0.75)
        ax.axhline(1.3, ls="--"); ax.set_title("Volcano")
        save(fig, "volcano.png"); plt.close()
        """
    )
    return _pack("volcano", "Volcano plot", "Simulated differential abundance volcano with significance cut lines.", script, [img])


def chart_pca_scatter() -> Dict[str, Any]:
    rng = random.Random(3)
    def cloud(cx, cy, n=80, s=0.55):
        return (
            [cx + rng.gauss(0, s) for _ in range(n)],
            [cy + rng.gauss(0, s) for _ in range(n)],
        )
    g1 = cloud(-1.2, 0.4)
    g2 = cloud(1.5, -0.2)
    g3 = cloud(0.1, 1.6, s=0.45)
    plt, fig, ax = new_axes((7.6, 5.0))
    ax.scatter(g1[0], g1[1], s=28, c=PALETTE["primary"], alpha=0.8, label="cluster A", edgecolors="white", lw=0.4)
    ax.scatter(g2[0], g2[1], s=28, c=PALETTE["secondary"], alpha=0.8, label="cluster B", edgecolors="white", lw=0.4)
    ax.scatter(g3[0], g3[1], s=28, c=PALETTE["accent"], alpha=0.8, label="cluster C", edgecolors="white", lw=0.4)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_title("PCA-style embedding (simulated clusters)")
    ax.legend()
    img = finish(fig, plt, alt="PCA scatter")
    script = script_preamble() + textwrap.dedent(
        """
        import random
        rng = random.Random(3)
        def cloud(cx, cy, n=80, s=0.55):
            return [cx+rng.gauss(0,s) for _ in range(n)], [cy+rng.gauss(0,s) for _ in range(n)]
        g1, g2, g3 = cloud(-1.2,0.4), cloud(1.5,-0.2), cloud(0.1,1.6,s=0.45)
        fig, ax = plt.subplots(figsize=(7.6, 5.0)); style_ax(ax)
        ax.scatter(*g1, label="A"); ax.scatter(*g2, label="B"); ax.scatter(*g3, label="C")
        ax.legend(); ax.set_title("PCA-style"); save(fig, "pca_scatter.png"); plt.close()
        """
    )
    return _pack("pca_scatter", "PCA-style clusters", "Three Gaussian clouds in PC space for exploratory viz.", script, [img])


def chart_random_walk() -> Dict[str, Any]:
    rng = random.Random(21)
    n = 500
    paths = []
    for seed in range(6):
        r = random.Random(21 + seed)
        y, series = 0.0, [0.0]
        for _ in range(n):
            y += r.choice([-1, 1]) * r.uniform(0.4, 1.2)
            series.append(y)
        paths.append(series)
    t = list(range(n + 1))
    plt, fig, ax = new_axes((8.2, 4.6))
    for i, p in enumerate(paths):
        plot_line(ax, t, p, color=color(i), lw=1.35, alpha=0.85, label=f"path {i+1}" if i < 3 else None)
    ax.set_xlabel("step")
    ax.set_ylabel("position")
    ax.set_title("Stochastic random-walk ensemble")
    ax.legend(loc="upper left", ncol=3)
    img = finish(fig, plt, alt="Random walk")
    script = script_preamble() + textwrap.dedent(
        """
        import random
        fig, ax = plt.subplots(figsize=(8.2, 4.6)); style_ax(ax)
        for seed in range(6):
            r = random.Random(21+seed); y, series = 0.0, [0.0]
            for _ in range(500):
                y += r.choice([-1,1])*r.uniform(0.4,1.2); series.append(y)
            ax.plot(series, lw=1.3)
        ax.set_title("Random walks"); save(fig, "random_walk.png"); plt.close()
        """
    )
    return _pack("random_walk", "Random-walk ensemble", "Six stochastic paths for Monte-Carlo style illustration.", script, [img])


def chart_diffusion_1d() -> Dict[str, Any]:
    """1D diffusion heat-map over time (Gaussian spreading)."""
    D = 0.08
    xs = [i * 0.1 - 5 for i in range(101)]
    times = [0.2, 0.8, 2.0, 5.0]
    plt, fig, ax = new_axes((8.0, 4.8))
    for i, t in enumerate(times):
        ys = [math.exp(-(x * x) / (4 * D * t)) / math.sqrt(4 * math.pi * D * t) for x in xs]
        plot_line(ax, xs, ys, color=color(i), lw=2.2, label=f"t={t}")
    ax.set_xlabel("x")
    ax.set_ylabel("concentration")
    ax.set_title(f"1D diffusion · D={D}")
    ax.legend()
    img = finish(fig, plt, alt="1D diffusion")
    script = script_preamble() + textwrap.dedent(
        f"""
        D = {D}
        xs = [i*0.1 - 5 for i in range(101)]
        times = [0.2, 0.8, 2.0, 5.0]
        fig, ax = plt.subplots(figsize=(8.0, 4.8)); style_ax(ax)
        for t in times:
            ys = [math.exp(-(x*x)/(4*D*t))/math.sqrt(4*math.pi*D*t) for x in xs]
            ax.plot(xs, ys, label=f"t={{t}}")
        ax.legend(); ax.set_title("Diffusion"); save(fig, "diffusion_1d.png"); plt.close()
        """
    )
    return _pack("diffusion_1d", "1D diffusion profiles", "Gaussian solutions of the diffusion equation at several times.", script, [img])


def chart_spectrum_nmr_style() -> Dict[str, Any]:
    """Synthetic multi-peak spectrum (NMR-like)."""
    xs = [i * 0.01 for i in range(0, 1201)]  # 0..12 ppm-like
    peaks = [(1.2, 1.0, 0.04), (2.1, 0.55, 0.05), (3.6, 0.8, 0.035), (7.2, 0.45, 0.03), (7.35, 0.4, 0.03)]
    ys = []
    for x in xs:
        y = 0.02
        for mu, amp, sig in peaks:
            y += amp * math.exp(-((x - mu) ** 2) / (2 * sig * sig))
        ys.append(y)
    plt, fig, ax = new_axes((9.0, 3.8))
    ax.fill_between(xs, ys, color=PALETTE["secondary"], alpha=0.15)
    plot_line(ax, xs, ys, color=PALETTE["ink"], lw=1.4)
    ax.invert_xaxis()
    ax.set_xlabel("Chemical shift (arb. ppm)")
    ax.set_ylabel("Intensity")
    ax.set_title("Synthetic multi-peak spectrum (NMR-style)")
    img = finish(fig, plt, alt="NMR-style spectrum")
    script = script_preamble() + textwrap.dedent(
        f"""
        xs = [i*0.01 for i in range(0, 1201)]
        peaks = {peaks!r}
        ys = []
        for x in xs:
            y = 0.02
            for mu, amp, sig in peaks:
                y += amp * math.exp(-((x-mu)**2)/(2*sig*sig))
            ys.append(y)
        fig, ax = plt.subplots(figsize=(9.0, 3.8)); style_ax(ax)
        ax.plot(xs, ys); ax.invert_xaxis(); ax.set_title("Spectrum")
        save(fig, "spectrum.png"); plt.close()
        """
    )
    return _pack("spectrum_nmr", "NMR-style spectrum", "Synthetic multiplet spectrum for teaching/demo rendering.", script, [img])


def chart_oscillator() -> Dict[str, Any]:
    t = [i * 0.04 for i in range(0, 250)]
    y = [math.exp(-0.12 * ti) * math.cos(3.2 * ti) for ti in t]
    env = [math.exp(-0.12 * ti) for ti in t]
    plt, fig, ax = new_axes()
    plot_line(ax, t, y, color=PALETTE["secondary"], lw=2.2, label="damped cos")
    plot_line(ax, t, env, color=PALETTE["accent"], lw=1.3, label="+envelope")
    plot_line(ax, t, [-e for e in env], color=PALETTE["accent"], lw=1.3, label="-envelope")
    ax.set_xlabel("t")
    ax.set_ylabel("x(t)")
    ax.set_title("Damped harmonic oscillator")
    ax.legend()
    img = finish(fig, plt, alt="Damped oscillator")
    script = script_preamble() + textwrap.dedent(
        """
        t = [i*0.04 for i in range(0, 250)]
        y = [math.exp(-0.12*ti)*math.cos(3.2*ti) for ti in t]
        env = [math.exp(-0.12*ti) for ti in t]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(t, y); ax.plot(t, env, ls="--"); ax.plot(t, [-e for e in env], ls="--")
        ax.set_title("Damped oscillator"); save(fig, "oscillator.png"); plt.close()
        """
    )
    return _pack("oscillator", "Damped oscillator", "Underdamped harmonic motion with exponential envelope.", script, [img])


def chart_histogram_kde() -> Dict[str, Any]:
    rng = random.Random(5)
    data = [rng.gauss(0, 1) for _ in range(400)] + [rng.gauss(2.2, 0.55) for _ in range(180)]
    plt, fig, ax = new_axes()
    ax.hist(data, bins=28, color=PALETTE["primary"], alpha=0.55, edgecolor="white", density=True, label="histogram")
    # simple KDE
    xs = [i * 0.08 - 4 for i in range(120)]
    h = 0.35
    dens = []
    for x in xs:
        dens.append(sum(math.exp(-((x - d) ** 2) / (2 * h * h)) for d in data) / (len(data) * h * math.sqrt(2 * math.pi)))
    plot_line(ax, xs, dens, color=PALETTE["danger"], lw=2.3, label="KDE")
    ax.set_xlabel("value")
    ax.set_ylabel("density")
    ax.set_title("Distribution · histogram + KDE")
    ax.legend()
    img = finish(fig, plt, alt="Histogram + KDE")
    script = script_preamble() + textwrap.dedent(
        """
        import random
        rng = random.Random(5)
        data = [rng.gauss(0,1) for _ in range(400)] + [rng.gauss(2.2,0.55) for _ in range(180)]
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.hist(data, bins=28, density=True, alpha=0.55)
        ax.set_title("Histogram"); save(fig, "histogram_kde.png"); plt.close()
        """
    )
    return _pack("histogram_kde", "Histogram + KDE", "Bimodal sample with density estimate overlay.", script, [img])


def generic_science_script(topic: str) -> Dict[str, Any]:
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", (topic or "experiment")[:48]).strip("_") or "experiment"
    xs = [i / 99 * 10.0 for i in range(100)]
    ys = [math.exp(-0.15 * x) * math.sin(1.3 * x) + 0.05 * x for x in xs]
    plt, fig, ax = new_axes()
    ax.fill_between(xs, ys, color=PALETTE["primary"], alpha=0.12)
    plot_line(ax, xs, ys, color=PALETTE["primary"], lw=2.4)
    ax.set_title(f"ResearchersHub · {topic[:56]}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    img = finish(fig, plt, alt=f"Figure: {topic[:40]}")
    script = script_preamble() + textwrap.dedent(
        f"""
        import csv
        OUT = Path(__file__).resolve().parent
        TOPIC = {topic!r}
        def simulate(n=100):
            xs, ys = [], []
            for i in range(n):
                x = i/(n-1)*10.0
                y = math.exp(-0.15*x)*math.sin(1.3*x)+0.05*x
                xs.append(x); ys.append(y)
            return xs, ys
        xs, ys = simulate()
        with (OUT / f"{safe}_results.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["x","y","topic"])
            for x,y in zip(xs,ys): w.writerow([f"{{x:.6f}}", f"{{y:.6f}}", TOPIC])
        fig, ax = plt.subplots(figsize=(7.6, 4.6)); style_ax(ax)
        ax.plot(xs, ys, color=PALETTE["primary"], lw=2.4)
        ax.set_title(f"ResearchersHub — {{TOPIC[:56]}}")
        save(fig, str(OUT / f"{safe}_figure.png")); plt.close()
        print("csv+figure written")
        """
    )
    return _pack(
        "generic_workflow",
        f"Constructive workflow: {topic[:80]}",
        "Multi-step workflow: simulate → CSV → publication figure.",
        script,
        [img],
        workflow=[
            "1. Parameterize the research question",
            "2. Simulate / generate series",
            "3. Write CSV results",
            "4. Render branded figure",
            "5. Persist script + PNG + Atlas nodes",
        ],
    )


# ── Multi-step named workflows ───────────────────────────────────────

WORKFLOWS: Dict[str, Dict[str, Any]] = {
    "assay_standard_curve": {
        "title": "Assay standard-curve workflow",
        "steps": [
            "Prepare concentration ladder",
            "Simulate absorbance readings (Beer–Lambert + noise)",
            "Fit linear calibration",
            "Export dual-panel figure (fit + residuals)",
            "Write reproducible Python + CSV",
        ],
        "charts": ["beer_lambert", "linear_regression"],
    },
    "pk_pd_panel": {
        "title": "PK/PD exploratory panel",
        "steps": [
            "Simulate dose–response (4PL)",
            "Simulate enzyme kinetics (MM)",
            "Compare potency vs capacity visuals",
            "Bundle scripts for lab notebook",
        ],
        "charts": ["dose_response", "enzyme_kinetics"],
    },
    "epidemic_scenario": {
        "title": "Epidemic scenario workflow",
        "steps": [
            "Set population and transmission parameters",
            "Integrate SIR compartments",
            "Plot outbreak curves",
            "Archive figure in Atlas",
        ],
        "charts": ["sir_epidemic"],
    },
    "ecology_dynamics": {
        "title": "Predator–prey ecology workflow",
        "steps": [
            "Choose Lotka–Volterra rates",
            "Integrate populations",
            "Render time series + phase portrait",
            "Export for report",
        ],
        "charts": ["lotka_volterra"],
    },
    "omics_hits": {
        "title": "Omics hit-calling visual workflow",
        "steps": [
            "Simulate logFC and p-values",
            "Render volcano with cut lines",
            "Optional PCA-style sample map",
            "Export panels",
        ],
        "charts": ["volcano", "pca_scatter"],
    },
    "materials_tensile": {
        "title": "Tensile response workflow",
        "steps": [
            "Define elastic modulus region",
            "Simulate plastic hardening",
            "Plot stress–strain with regions",
            "Export figure",
        ],
        "charts": ["stress_strain"],
    },
    "physical_chemistry_lab": {
        "title": "Physical chemistry lab pack",
        "steps": [
            "Titration curve",
            "Arrhenius temperature dependence",
            "Decay / first-order process",
            "Bundle lab report figures",
        ],
        "charts": ["titration", "arrhenius", "radioactive_decay"],
    },
    "binding_and_kinetics": {
        "title": "Binding + kinetics pack",
        "steps": [
            "Binding isotherm (Kd)",
            "Michaelis–Menten kinetics",
            "Side-by-side interpretation",
        ],
        "charts": ["binding_isotherm", "enzyme_kinetics"],
    },
    "stochastic_lab": {
        "title": "Stochastic simulation lab",
        "steps": [
            "Random-walk ensemble",
            "Distribution histogram + KDE",
            "Discuss noise vs signal",
        ],
        "charts": ["random_walk", "histogram_kde"],
    },
    "diffusion_and_waves": {
        "title": "Diffusion & oscillator pack",
        "steps": [
            "1D diffusion profiles",
            "Damped oscillator trajectory",
            "Export teaching figures",
        ],
        "charts": ["diffusion_1d", "oscillator"],
    },
    "spectroscopy_demo": {
        "title": "Spectroscopy demo workflow",
        "steps": [
            "Synthetic multiplet spectrum",
            "Beer–Lambert calibration",
            "Lab teaching bundle",
        ],
        "charts": ["spectrum_nmr", "beer_lambert"],
    },
    "full_methods_bundle": {
        "title": "Full methods figure bundle",
        "steps": [
            "Core chem/bio curves",
            "Stats diagnostics",
            "Systems simulation",
            "Ship multi-figure board",
        ],
        "charts": [
            "titration",
            "enzyme_kinetics",
            "dose_response",
            "linear_regression",
            "sir_epidemic",
            "volcano",
        ],
    },
}


CHART_BUILDERS: Dict[str, Callable[[], Dict[str, Any]]] = {
    "titration": chart_titration,
    "enzyme_kinetics": chart_michaelis_menten,
    "michaelis_menten": chart_michaelis_menten,
    "dose_response": chart_dose_response,
    "arrhenius": chart_arrhenius,
    "beer_lambert": chart_beer_lambert,
    "linear_regression": chart_linear_regression,
    "stress_strain": chart_stress_strain,
    "sir_epidemic": chart_sir_epidemic,
    "lotka_volterra": chart_lotka_volterra,
    "radioactive_decay": chart_radioactive_decay,
    "binding_isotherm": chart_binding_isotherm,
    "volcano": chart_volcano,
    "pca_scatter": chart_pca_scatter,
    "random_walk": chart_random_walk,
    "diffusion_1d": chart_diffusion_1d,
    "spectrum_nmr": chart_spectrum_nmr_style,
    "oscillator": chart_oscillator,
    "histogram_kde": chart_histogram_kde,
}


_ROUTES: List[Tuple[re.Pattern, str]] = [
    (re.compile(r"titrat|ph\s*curve|acid.?base", re.I), "titration"),
    (re.compile(r"michaelis|enzyme\s*kinet|\bkm\b|vmax", re.I), "enzyme_kinetics"),
    (re.compile(r"dose.?response|ic50|ec50|hill\s*slope", re.I), "dose_response"),
    (re.compile(r"arrhenius|activation\s*energy|ln\s*k", re.I), "arrhenius"),
    (re.compile(r"beer|lambert|absorbance|uv.?vis|calibration", re.I), "beer_lambert"),
    (re.compile(r"regress|linear\s*fit|least\s*squares|\bols\b|residual", re.I), "linear_regression"),
    (re.compile(r"stress.?strain|tensile|young", re.I), "stress_strain"),
    (re.compile(r"\bsir\b|epidemic|outbreak|compartmental", re.I), "sir_epidemic"),
    (re.compile(r"lotka|volterra|predator|prey", re.I), "lotka_volterra"),
    (re.compile(r"decay|half.?life|radioactive", re.I), "radioactive_decay"),
    (re.compile(r"binding|isotherm|\bkd\b|langmuir", re.I), "binding_isotherm"),
    (re.compile(r"volcano|logfc|differential\s*express", re.I), "volcano"),
    (re.compile(r"\bpca\b|embedding|cluster\s*plot", re.I), "pca_scatter"),
    (re.compile(r"random\s*walk|brownian|stochastic\s*path", re.I), "random_walk"),
    (re.compile(r"diffusion|fick", re.I), "diffusion_1d"),
    (re.compile(r"nmr|spectrum|multiplet|chemical\s*shift", re.I), "spectrum_nmr"),
    (re.compile(r"oscillator|damped\s*harmonic|hooke", re.I), "oscillator"),
    (re.compile(r"histogram|kde|distribution\s*plot", re.I), "histogram_kde"),
]


def list_workflows() -> List[Dict[str, Any]]:
    out = []
    for wid, w in WORKFLOWS.items():
        out.append(
            {
                "id": wid,
                "title": w["title"],
                "steps": w["steps"],
                "charts": w["charts"],
                "product": PRODUCT,
            }
        )
    return out


def list_chart_kinds() -> List[str]:
    return sorted(CHART_BUILDERS.keys())


def detect_construct(prompt: str) -> Optional[str]:
    p = prompt or ""
    for wid in WORKFLOWS:
        if wid.replace("_", " ") in p.lower() or wid in p.lower():
            return f"workflow:{wid}"
    for rx, kind in _ROUTES:
        if rx.search(p):
            return kind
    if re.search(
        r"\b(chart|plot|figure|graph|simulat|matplotlib|python\s+script|workflow|"
        r"chemistry|chem|kinetics|thermodynamics|research|scientist|construct)\b",
        p,
        re.I,
    ):
        return "generic_workflow"
    return None


def run_workflow(workflow_id: str) -> Dict[str, Any]:
    w = WORKFLOWS.get(workflow_id)
    if not w:
        return generic_science_script(f"workflow {workflow_id}")
    images: List[Dict[str, str]] = []
    scripts: List[str] = [f"# Workflow: {w['title']}\n"]
    kinds_run = []
    for kind in w["charts"]:
        fn = CHART_BUILDERS.get(kind)
        if not fn:
            continue
        try:
            r = fn()
            images.extend(r.get("images") or [])
            scripts.append(f"\n# --- {r.get('title')} ---\n{r.get('script') or ''}")
            kinds_run.append(kind)
        except Exception as e:
            scripts.append(f"\n# {kind} failed: {e}\n")
    result = _pack(
        f"workflow_{workflow_id}",
        w["title"],
        f"Multi-step workflow with {len(images)} figure(s): " + ", ".join(kinds_run),
        "\n".join(scripts),
        images,
        workflow=list(w["steps"]),
    )
    result["workflow_id"] = workflow_id
    result["charts"] = kinds_run
    return result


def run_construct(prompt: str, skill_id: str = "") -> Dict[str, Any]:
    """Build constructive payload: scripts + full images + markdown for chat."""
    p = (prompt or "").strip()
    sid = (skill_id or "").lower().replace("-", "_")
    result: Dict[str, Any]
    try:
        # Named workflow by skill or prompt
        if sid in WORKFLOWS or sid.startswith("workflow_"):
            wid = sid.replace("workflow_", "") if sid.startswith("workflow_") else sid
            result = run_workflow(wid)
        elif (det := detect_construct(p)) and str(det).startswith("workflow:"):
            result = run_workflow(str(det).split(":", 1)[1])
        else:
            kind = None
            for rx, k in _ROUTES:
                if rx.search(p) or k in sid or k.replace("_", "") in sid.replace("_", ""):
                    kind = k
                    break
            if kind and kind in CHART_BUILDERS:
                result = CHART_BUILDERS[kind]()
            elif "board" in sid or re.search(r"multi.?figure|figure\s*board|all\s*charts", p, re.I):
                result = multi_figure_board(p)
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
            "workflow_steps": [],
            "design": "researchershub.publication.v2",
        }

    home = _home()
    stamp = time.strftime("%Y%m%d_%H%M%S")
    kind = re.sub(r"[^a-z0-9_]+", "_", (result.get("kind") or "workflow").lower())
    script_path = home / f"{stamp}_{kind}.py"
    try:
        script_path.write_text(result.get("script") or "", encoding="utf-8")
        result["script_path"] = str(script_path)
    except Exception:
        result["script_path"] = ""

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
    try:
        from pocket.atlas_graph import record_construct

        result["atlas"] = record_construct(
            title=result.get("title") or "constructive workflow",
            script_path=result.get("script_path") or "",
            image_paths=result.get("image_paths") or [],
            summary=result.get("summary") or "",
            agent="construct",
            skill_id=skill_id or result.get("kind") or "",
        )
    except Exception as e:
        result["atlas"] = {"ok": False, "error": str(e)[:160]}
    return result


def format_construct_markdown(result: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append(f"### {result.get('title') or 'ResearchersHub constructive result'}")
    if result.get("summary"):
        lines.append("")
        lines.append(result["summary"])
    steps = result.get("workflow_steps") or []
    if steps:
        lines.append("")
        lines.append("#### Workflow")
        for s in steps:
            lines.append(f"- {s}")
    lines.append("")
    lines.append(f"#### Figures · design `{result.get('design') or 'v2'}`")
    imgs = result.get("images") or []
    if not imgs:
        lines.append("_No figure generated (matplotlib may be missing)._")
    for img in imgs:
        lines.append("")
        lines.append(_md_image(img.get("alt") or "figure", img.get("base64") or "", img.get("mime") or "image/png"))
    lines.append("")
    lines.append("#### Real Python script")
    if result.get("script_path"):
        lines.append(f"Saved: `{result['script_path']}`")
    lines.append("")
    lines.append("```python")
    lines.append((result.get("script") or "").rstrip())
    lines.append("```")
    lines.append("")
    lines.append(
        f"_{PRODUCT} returns complete charts as embedded images and runnable scripts — "
        "publication styling v2, not placeholders._"
    )
    return "\n".join(lines)


def enrich_chat_text(text: str, user_prompt: str = "", force: bool = False) -> Dict[str, Any]:
    want = force or bool(detect_construct(user_prompt or text or ""))
    if not want:
        return {"text": text, "construct": None, "images": []}
    c = run_construct(user_prompt or text)
    md = c.get("markdown") or ""
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
            "workflow_steps": c.get("workflow_steps"),
            "design": c.get("design"),
        },
        "images": c.get("images") or [],
    }


def multi_figure_board(prompt: str = "") -> Dict[str, Any]:
    builders = [
        chart_titration,
        chart_michaelis_menten,
        chart_dose_response,
        chart_beer_lambert,
        chart_linear_regression,
        chart_sir_epidemic,
        chart_volcano,
        chart_lotka_volterra,
    ]
    images: List[Dict[str, str]] = []
    scripts: List[str] = [script_preamble(), "\n# Multi-figure board\n"]
    for fn in builders:
        try:
            r = fn()
            images.extend(r.get("images") or [])
            scripts.append(f"\n# --- {r.get('title')} ---\n")
        except Exception as e:
            scripts.append(f"# {fn.__name__} failed: {e}\n")
    result = _pack(
        "image_board",
        "ResearchersHub multi-figure board",
        f"{len(images)} publication figures: titration, enzyme, dose–response, Beer–Lambert, regression, SIR, volcano, Lotka–Volterra.",
        "".join(scripts),
        images,
        workflow=[
            "1. Select core teaching/research figures",
            "2. Render each with design system v2",
            "3. Bundle into multi-figure board",
            "4. Export paths + Atlas experiment",
        ],
    )
    home = _home()
    path = home / f"board_{int(time.time())}.py"
    path.write_text(result["script"], encoding="utf-8")
    result["script_path"] = str(path)
    return result
