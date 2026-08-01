"""ResearchersHub — 100+ preloaded science & chemistry skills for real researchers.

Catalog entries are first-class: models can route to these by id/tag.
Execution for constructive skills goes through science_construct (charts, scripts, figures).
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def _s(
    id: str,
    domain: str,
    desc: str,
    *,
    kind: str = "atomic",
    tags: str = "",
    worker: str = "SCRUTATOR",
) -> Dict[str, Any]:
    t = tags.split() if tags else []
    t = list(dict.fromkeys([domain.lower(), "science", "research"] + t))
    return {
        "id": id,
        "worker": worker,
        "desc": desc,
        "kind": kind,
        "tags": t,
        "domain": domain,
        "product": "ResearchersHub",
    }


def _build() -> List[Dict[str, Any]]:
    S: List[Dict[str, Any]] = []

    # ── Advanced Chemistry ──────────────────────────────────────────
    chem = [
        ("chem_stoichiometry", "Balance equations + mole/mass stoichiometry"),
        ("chem_limiting_reagent", "Identify limiting reagent and theoretical yield"),
        ("chem_equilibrium", "Keq, Le Chatelier, ICE tables"),
        ("chem_kinetics_rate", "Rate laws, order, half-life, Arrhenius"),
        ("chem_thermodynamics", "ΔH ΔG ΔS, Hess law, van't Hoff"),
        ("chem_acid_base", "pH, Ka/Kb, buffers, Henderson–Hasselbalch"),
        ("chem_titration_curve", "Generate titration curve chart + script"),
        ("chem_redox_halfcells", "Balance redox half-reactions + E° cell"),
        ("chem_electrochemistry", "Nernst equation, galvanic/electrolytic cells"),
        ("chem_gas_laws", "Ideal/real gas, Dalton, Graham"),
        ("chem_phase_diagram", "Phase diagram sketch data + chart"),
        ("chem_colligative", "Boiling/freezing point, osmotic pressure"),
        ("chem_solubility_product", "Ksp calculations and common-ion effect"),
        ("chem_crystal_field", "Crystal field splitting octahedral/tetrahedral"),
        ("chem_vsepr", "VSEPR geometry and polarity"),
        ("chem_hybridization", "Orbital hybridization and bonding"),
        ("chem_moles_to_molarity", "Concentration conversions"),
        ("chem_dilution", "C1V1=C2V2 dilution planner"),
        ("chem_calorimetry", "q=mcΔT and bomb calorimetry"),
        ("chem_spectroscopy_uvvis", "UV-Vis Beer–Lambert calibration curve"),
        ("chem_ir_peaks", "IR functional group peak guide"),
        ("chem_nmr_h1", "¹H NMR chemical shift interpretation aid"),
        ("chem_nmr_c13", "¹³C NMR interpretation aid"),
        ("chem_ms_fragments", "Mass spectrometry fragmentation patterns"),
        ("chem_xrd_bragg", "Bragg law XRD d-spacing"),
        ("chem_organic_nomenclature", "IUPAC organic naming assist"),
        ("chem_organic_mechanisms", "Common organic mechanisms outline"),
        ("chem_retrosynthesis", "Simple retrosynthesis sketch steps"),
        ("chem_protecting_groups", "Protecting group selection guide"),
        ("chem_green_metrics", "Atom economy, E-factor, PMI"),
        ("chem_process_safety", "Lab safety checklist + SDS thinking"),
        ("chem_hazard_ghs", "GHS pictogram / hazard class map"),
        ("chem_polymer_mw", "Polymer Mn/Mw/PDI basics"),
        ("chem_catalysis", "Homogeneous vs heterogeneous catalysis"),
        ("chem_photochemistry", "Quantum yield and photochemical basics"),
        ("chem_computational_dft", "DFT workflow outline (geometry, energy)"),
        ("chem_rdkit_smiles", "SMILES parse/describe constructive script"),
        ("chem_mol_weight", "Molecular weight from formula"),
        ("chem_element_lookup", "Periodic table properties"),
        ("chem_reaction_yield_plot", "Yield vs condition chart + Python"),
    ]
    for sid, desc in chem:
        S.append(_s(sid, "chemistry", desc, kind="playbook", tags="chemistry advanced", worker="SCRUTATOR"))

    # ── Biochemistry / Biology ──────────────────────────────────────
    bio = [
        ("bio_central_dogma", "DNA→RNA→protein workflow brief"),
        ("bio_pcr_design", "PCR primer design checklist"),
        ("bio_gel_electrophoresis", "Gel band interpretation aid"),
        ("bio_western_blot", "Western blot protocol skeleton"),
        ("bio_elisa", "ELISA standard curve + chart"),
        ("bio_sequence_align", "Pairwise sequence alignment sketch"),
        ("bio_blast_query", "BLAST search planning"),
        ("bio_crispr_guide", "CRISPR guide RNA design checklist"),
        ("bio_cell_culture", "Mammalian cell culture basics"),
        ("bio_pharmacokinetics", "ADME / PK curve chart"),
        ("bio_dose_response", "IC50/EC50 dose–response fit + chart"),
        ("bio_enzyme_kinetics", "Michaelis–Menten Km/Vmax chart"),
        ("bio_protein_structure", "Secondary structure / PDB notes"),
        ("bio_metabolomics_qc", "Metabolomics QC checklist"),
        ("bio_rnaseq_pipeline", "RNA-seq analysis pipeline skeleton"),
        ("bio_microbiome", "16S microbiome analysis outline"),
        ("bio_immuno_assay", "Immunoassay design notes"),
        ("bio_flow_cytometry", "Flow cytometry gating concepts"),
        ("bio_cloning_map", "Plasmid cloning map checklist"),
        ("bio_virology_basics", "Virus structure / assay notes"),
    ]
    for sid, desc in bio:
        S.append(_s(sid, "biology", desc, kind="playbook", tags="biology wetlab", worker="SCRUTATOR"))

    # ── Physics / Materials ─────────────────────────────────────────
    phys = [
        ("phys_kinematics", "1D/2D kinematics solver + plots"),
        ("phys_newton_laws", "Force diagrams + free body notes"),
        ("phys_energy_work", "Work–energy theorem plots"),
        ("phys_oscillator", "Simple harmonic motion chart"),
        ("phys_wave_interference", "Wave interference pattern data"),
        ("phys_optics_snell", "Snell's law ray sketch data"),
        ("phys_thermo_cycles", "Carnot / Otto cycle overview"),
        ("phys_quantum_particle", "Particle in a box energy levels"),
        ("phys_band_structure", "Semiconductor band gap notes"),
        ("mat_stress_strain", "Stress–strain curve chart"),
        ("mat_phase_binary", "Binary phase diagram conceptual"),
        ("mat_diffusion_fick", "Fick's laws diffusion plot"),
        ("mat_hardness", "Hardness test comparison"),
        ("mat_corrosion", "Corrosion rate estimation"),
        ("mat_nanomaterials", "Nanomaterial characterization map"),
    ]
    for sid, desc in phys:
        S.append(_s(sid, "physics", desc, kind="playbook", tags="physics materials", worker="SCRUTATOR"))

    # ── Data science for researchers ────────────────────────────────
    data = [
        ("data_descriptive_stats", "Mean/median/SD/CI table + chart"),
        ("data_hypothesis_ttest", "t-test workflow + Python"),
        ("data_anova", "One-way ANOVA skeleton"),
        ("data_regression_linear", "Linear regression fit + residual chart"),
        ("data_regression_logistic", "Logistic regression outline"),
        ("data_pca", "PCA projection chart"),
        ("data_clustering_kmeans", "K-means clustering chart"),
        ("data_survival_kaplan", "Kaplan–Meier curve chart"),
        ("data_roc_curve", "ROC / AUC chart"),
        ("data_error_bars", "Bar chart with error bars"),
        ("data_heatmap", "Correlation heatmap chart"),
        ("data_timeseries", "Time series trend + seasonality sketch"),
        ("data_power_analysis", "Sample size / power estimate"),
        ("data_outlier_iqr", "Outlier detection IQR"),
        ("data_bootstrap_ci", "Bootstrap confidence interval"),
        ("data_bayes_simple", "Simple Bayesian update sketch"),
        ("data_csv_load_clean", "CSV load/clean constructive script"),
        ("data_figure_publication", "Publication-ready figure settings"),
        ("data_units_convert", "Scientific unit conversion"),
        ("data_significant_figures", "Sig-fig and uncertainty report"),
    ]
    for sid, desc in data:
        S.append(_s(sid, "data", desc, kind="playbook", tags="stats data chart", worker="SCRUTATOR"))

    # ── Literature / lab ops ────────────────────────────────────────
    lit = [
        ("lit_arxiv_search", "arXiv search planning + Edge open", "NAVIGATOR"),
        ("lit_pubmed_search", "PubMed query design", "NAVIGATOR"),
        ("lit_scholar_search", "Google Scholar search plan", "NAVIGATOR"),
        ("lit_doi_resolve", "DOI metadata resolve plan", "SCRUTATOR"),
        ("lit_cite_bibtex", "Generate BibTeX skeleton", "SCRUTATOR"),
        ("lit_related_work", "Related-work matrix template", "SCRUTATOR"),
        ("lit_prism_flow", "PRISMA systematic review flow", "SCRUTATOR"),
        ("lit_paper_outline", "IMRaD paper outline", "SCRUTATOR"),
        ("lit_grant_aims", "Specific aims page skeleton", "SCRUTATOR"),
        ("lit_peer_review", "Peer review checklist", "SCRUTATOR"),
        ("lab_notebook_entry", "ELN / lab notebook entry template", "SCRUTATOR"),
        ("lab_protocol_sop", "SOP protocol template", "SCRUTATOR"),
        ("lab_reagent_calc", "Reagent volume/mass calculator", "SCRUTATOR"),
        ("lab_inventory", "Lab inventory checklist", "SCRUTATOR"),
        ("lab_equipment_log", "Equipment use log template", "SCRUTATOR"),
        ("lab_qc_batch", "Batch QC pass/fail report", "SCRUTATOR"),
        ("lab_lams_sample", "Sample chain-of-custody note", "SCRUTATOR"),
        ("edge_pubchem", "Open PubChem", "NAVIGATOR"),
        ("edge_chembl", "Open ChEMBL", "NAVIGATOR"),
        ("edge_pdb", "Open RCSB PDB", "NAVIGATOR"),
        ("edge_nist_webbook", "Open NIST Chemistry WebBook", "NAVIGATOR"),
        ("edge_materials_project", "Open Materials Project", "NAVIGATOR"),
        ("edge_nature", "Open nature.com", "NAVIGATOR"),
        ("edge_science", "Open science.org", "NAVIGATOR"),
        ("edge_cell", "Open cell.com", "NAVIGATOR"),
    ]
    for sid, desc, worker in lit:
        S.append(
            _s(
                sid,
                "literature" if sid.startswith("lit") else "lab" if sid.startswith("lab") else "web",
                desc,
                kind="playbook" if not sid.startswith("edge_") else "atomic",
                tags="literature lab",
                worker=worker,
            )
        )

    # ── Constructive figure / script meta-skills ────────────────────
    construct = [
        ("construct_python_workflow", "Emit real multi-step Python research workflow script"),
        ("construct_chart_matplotlib", "Run matplotlib chart → full PNG in chat"),
        ("construct_multi_panel_figure", "Multi-panel publication figure"),
        ("construct_lab_report", "Lab report with methods + figure + code"),
        ("construct_notebook_cells", "Jupyter-style cell blocks as .py workflow"),
        ("construct_repro_bundle", "Reproducible script + requirements stub"),
        ("construct_simulation_loop", "Parameter sweep simulation + plots"),
        ("construct_fit_model", "Fit model to data + residual plots"),
        ("construct_export_csv", "Write results CSV next to script"),
        ("construct_image_board", "Return multiple charts as chat images"),
    ]
    for sid, desc in construct:
        S.append(
            _s(
                sid,
                "construct",
                desc,
                kind="playbook",
                tags="construct chart image python",
                worker="SCRIPTOR",
            )
        )

    return S


SCIENCE_SKILLS: List[Dict[str, Any]] = _build()


def all_science_skills() -> List[Dict[str, Any]]:
    return list(SCIENCE_SKILLS)


def science_skill_count() -> int:
    return len(SCIENCE_SKILLS)


def get_science_skill(skill_id: str) -> Optional[Dict[str, Any]]:
    sid = (skill_id or "").lower().replace("-", "_").strip()
    for s in SCIENCE_SKILLS:
        if s["id"] == sid:
            return s
    return None


def skills_by_domain(domain: str = "") -> List[Dict[str, Any]]:
    d = (domain or "").lower().strip()
    if not d:
        return all_science_skills()
    return [s for s in SCIENCE_SKILLS if (s.get("domain") or "").lower() == d or d in (s.get("tags") or [])]


def science_catalog_summary() -> Dict[str, Any]:
    by: Dict[str, int] = {}
    for s in SCIENCE_SKILLS:
        dom = s.get("domain") or "other"
        by[dom] = by.get(dom, 0) + 1
    return {
        "product": "ResearchersHub",
        "total": len(SCIENCE_SKILLS),
        "by_domain": by,
        "tagline": "100+ science skills — chemistry, biology, physics, stats, lab, literature, construct",
    }
