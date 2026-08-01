"""ResearchersHub extended research skills — ML, computational biology, cheminformatics.

Readable · editable · extensible:
  - Built-in pack below
  - Drop JSON/YAML skill files in skills/ or ~/.researchershub/skills/
  - Each file: { "id", "domain", "desc", "tags"?, "kind"?, "worker"? }
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # optional


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
        "editable": True,
        "extensible": True,
    }


def _pairs(domain: str, items: List[tuple], tags: str = "", worker: str = "SCRUTATOR") -> List[Dict[str, Any]]:
    return [_s(i, domain, d, kind="playbook", tags=tags, worker=worker) for i, d in items]


def _ml_skills() -> List[Dict[str, Any]]:
    items = [
        ("ml_train_test_split", "Stratified train/val/test split workflow"),
        ("ml_cross_validation", "K-fold CV plan + metrics aggregate"),
        ("ml_baseline_models", "Baseline classifier/regressor suite"),
        ("ml_feature_engineering", "Feature transforms + leakage checklist"),
        ("ml_feature_selection", "Filter/wrapper/embedded selection"),
        ("ml_imbalance_handling", "Class imbalance: weights, SMOTE notes"),
        ("ml_hyperparam_grid", "Grid/random search skeleton"),
        ("ml_hyperparam_bayes", "Bayesian optimization outline"),
        ("ml_early_stopping", "Early stopping + checkpoint policy"),
        ("ml_metrics_classif", "Accuracy/F1/ROC-AUC/PR-AUC report"),
        ("ml_metrics_regress", "MAE/RMSE/R² residual analysis"),
        ("ml_confusion_matrix", "Confusion matrix chart + script"),
        ("ml_learning_curve", "Learning curve plot workflow"),
        ("ml_calibration_curve", "Probability calibration chart"),
        ("ml_shap_explain", "SHAP / feature importance workflow"),
        ("ml_lime_explain", "LIME local explanation outline"),
        ("ml_pipeline_sklearn", "sklearn Pipeline constructive script"),
        ("ml_xgboost_train", "XGBoost train + eval workflow"),
        ("ml_lightgbm_train", "LightGBM train + eval workflow"),
        ("ml_random_forest", "Random forest baseline workflow"),
        ("ml_svm_kernel", "SVM kernel selection notes"),
        ("ml_knn_baseline", "k-NN baseline + distance metrics"),
        ("ml_clustering_eval", "Silhouette / ARI clustering eval"),
        ("ml_dbscan", "DBSCAN density clustering"),
        ("ml_umap_embed", "UMAP embedding visualization"),
        ("ml_tsne_embed", "t-SNE embedding visualization"),
        ("ml_autoencoder", "Autoencoder recon + latent chart"),
        ("ml_vae_outline", "VAE generative outline"),
        ("ml_gan_outline", "GAN training pitfalls checklist"),
        ("ml_contrastive", "Contrastive learning skeleton"),
        ("ml_transfer_learning", "Transfer / fine-tune strategy"),
        ("ml_lora_finetune", "LoRA / PEFT fine-tune checklist"),
        ("ml_prompt_eval", "LLM prompt evaluation harness"),
        ("ml_rag_pipeline", "RAG retrieve-then-generate pipeline"),
        ("ml_embedding_index", "Vector index build/query notes"),
        ("ml_token_budget", "Context token budget planner"),
        ("ml_dataset_card", "Dataset card template"),
        ("ml_model_card", "Model card template"),
        ("ml_experiment_track", "Experiment tracking (MLflow-style)"),
        ("ml_repro_seed", "Full reproducibility seed policy"),
        ("ml_data_version", "Dataset versioning checklist"),
        ("ml_dvc_outline", "DVC pipeline outline"),
        ("ml_onnx_export", "ONNX export + validate"),
        ("ml_batch_infer", "Batch inference job skeleton"),
        ("ml_online_infer", "Online inference latency budget"),
        ("ml_drift_detect", "Data/concept drift detection"),
        ("ml_active_learning", "Active learning loop"),
        ("ml_semi_supervised", "Semi-supervised pseudo-label plan"),
        ("ml_time_series_cv", "Time-series CV (no leakage)"),
        ("ml_forecast_baseline", "Forecast baseline + residual plot"),
        ("ml_anomaly_detect", "Anomaly detection workflow"),
        ("ml_nlp_classify", "Text classification pipeline"),
        ("ml_nlp_ner", "NER pipeline outline"),
        ("ml_cv_classify", "Image classification pipeline"),
        ("ml_cv_segment", "Segmentation metrics (IoU/Dice)"),
        ("ml_audio_features", "Audio feature extraction notes"),
        ("ml_multimodal_fuse", "Multimodal fusion patterns"),
        ("ml_rl_outline", "RL problem formulation checklist"),
        ("ml_causal_inference", "Causal DAG / ATE outline"),
        ("ml_ab_test", "A/B test design + power"),
        ("ml_fairness_audit", "Fairness metrics audit"),
        ("ml_privacy_dp", "Differential privacy notes"),
        ("ml_secure_agg", "Federated / secure agg outline"),
        ("ml_gpu_profile", "GPU memory/throughput profiling"),
        ("ml_distributed_train", "DDP / multi-GPU checklist"),
        ("ml_unit_test_model", "Model unit tests + golden set"),
        ("ml_ci_ml", "CI for training + eval gates"),
        ("ml_error_analysis", "Slice-based error analysis"),
        ("ml_label_quality", "Label noise audit"),
        ("ml_weak_supervision", "Weak supervision labeling"),
        ("ml_synthetic_data", "Synthetic data generation plan"),
        ("ml_curriculum", "Curriculum learning schedule"),
        ("ml_knowledge_distill", "Knowledge distillation outline"),
        ("ml_quantization", "INT8/FP16 quantization checklist"),
        ("ml_pruning", "Pruning / sparsity outline"),
        ("ml_serving_fastapi", "FastAPI model serve skeleton"),
        ("ml_monitor_prod", "Production monitoring dashboard plan"),
    ]
    return _pairs("ml", items, tags="ml machine-learning")


def _compbio_skills() -> List[Dict[str, Any]]:
    items = [
        ("cbi_genome_assembly", "Genome assembly QC metrics"),
        ("cbi_variant_call", "Variant calling pipeline outline"),
        ("cbi_vep_annotate", "Variant effect prediction notes"),
        ("cbi_gwas_outline", "GWAS design + Manhattan plot plan"),
        ("cbi_eqtl", "eQTL analysis outline"),
        ("cbi_rna_quant", "RNA quantification (counts/TPM)"),
        ("cbi_de_genes", "Differential expression workflow"),
        ("cbi_gsea", "Gene set enrichment analysis"),
        ("cbi_pathway_ora", "Over-representation pathway analysis"),
        ("cbi_single_cell", "scRNA-seq QC + clustering outline"),
        ("cbi_spatial_tx", "Spatial transcriptomics outline"),
        ("cbi_atac", "ATAC-seq peak workflow"),
        ("cbi_chipseq", "ChIP-seq peak calling outline"),
        ("cbi_methylation", "Bisulfite / methylation analysis"),
        ("cbi_hic", "Hi-C contact map notes"),
        ("cbi_proteomics_lfq", "LFQ proteomics pipeline"),
        ("cbi_phospho", "Phosphoproteomics outline"),
        ("cbi_metabolomics_ms", "MS metabolomics peak table workflow"),
        ("cbi_lipidomics", "Lipidomics analysis outline"),
        ("cbi_multiomics_integrate", "Multi-omics integration patterns"),
        ("cbi_phylogeny", "Phylogenetic tree workflow"),
        ("cbi_msa", "Multiple sequence alignment"),
        ("cbi_hmm_profile", "HMM profile search outline"),
        ("cbi_structure_predict", "Protein structure prediction notes"),
        ("cbi_docking_protein", "Protein–ligand docking outline"),
        ("cbi_md_sim", "Molecular dynamics setup checklist"),
        ("cbi_alphafold_use", "AlphaFold result interpretation"),
        ("cbi_antibody_design", "Antibody CDR design notes"),
        ("cbi_vaccine_epitope", "Epitope prediction checklist"),
        ("cbi_microbiome_diversity", "Alpha/beta diversity analysis"),
        ("cbi_metagenome", "Metagenome assembly/binning outline"),
        ("cbi_viral_assembly", "Viral genome assembly notes"),
        ("cbi_crispr_screens", "CRISPR screen analysis"),
        ("cbi_drug_response_omics", "Omics–drug response modeling"),
        ("cbi_clinical_biomarker", "Biomarker discovery pipeline"),
        ("cbi_survival_omics", "Survival analysis with omics features"),
        ("cbi_batch_correct", "Batch correction (ComBat-style)"),
        ("cbi_qc_fastqc", "FastQC / MultiQC report review"),
        ("cbi_alignment_bwa", "Read alignment (BWA/STAR) notes"),
        ("cbi_count_matrix", "Build gene count matrix"),
        ("cbi_pseudobulk", "Pseudobulk DE for single-cell"),
        ("cbi_celltype_annotate", "Cell type annotation strategies"),
        ("cbi_trajectory", "Trajectory / pseudotime outline"),
        ("cbi_network_grn", "Gene regulatory network inference"),
        ("cbi_ppi_network", "Protein–protein interaction network"),
        ("cbi_gwas_fine_map", "Fine-mapping outline"),
        ("cbi_prs", "Polygenic risk score outline"),
        ("cbi_mendelian_random", "Mendelian randomization checklist"),
        ("cbi_fair_omics", "FAIR omics data packaging"),
        ("cbi_repro_nfcore", "nf-core pipeline reuse notes"),
    ]
    return _pairs("compbio", items, tags="compbio bioinformatics genomics")


def _cheminf_skills() -> List[Dict[str, Any]]:
    items = [
        ("cheminf_smiles_parse", "Parse/validate SMILES"),
        ("cheminf_inchi_key", "InChI / InChIKey conversion"),
        ("cheminf_canonical_smiles", "Canonicalize SMILES"),
        ("cheminf_descriptors_2d", "2D molecular descriptors"),
        ("cheminf_descriptors_3d", "3D descriptors + conformers"),
        ("cheminf_fingerprints_ecfp", "ECFP/Morgan fingerprints"),
        ("cheminf_fingerprints_maccs", "MACCS keys"),
        ("cheminf_tanimoto", "Tanimoto similarity matrix"),
        ("cheminf_mcs", "Maximum common substructure"),
        ("cheminf_substructure_search", "Substructure filter"),
        ("cheminf_scaffold_bemis", "Bemis–Murcko scaffolds"),
        ("cheminf_scaffold_hop", "Scaffold hopping ideas"),
        ("cheminf_lipinski", "Lipinski Ro5 filter"),
        ("cheminf_veber", "Veber oral bioavailability rules"),
        ("cheminf_pains", "PAINS filter"),
        ("cheminf_brenk", "Brenk unwanted groups"),
        ("cheminf_qed", "QED drug-likeness score"),
        ("cheminf_sa_score", "Synthetic accessibility score"),
        ("cheminf_logp", "logP / logD estimation notes"),
        ("cheminf_pka", "pKa estimation outline"),
        ("cheminf_tautomer", "Tautomer enumeration"),
        ("cheminf_stereo", "Stereochemistry perception"),
        ("cheminf_conformer_gen", "Conformer generation workflow"),
        ("cheminf_minimize", "Energy minimization outline"),
        ("cheminf_docking_ligand", "Ligand docking prep (PDBQT)"),
        ("cheminf_virtual_screen", "Virtual screening cascade"),
        ("cheminf_qsar_build", "QSAR model build + validate"),
        ("cheminf_qsar_ad", "Applicability domain"),
        ("cheminf_admet_predict", "ADMET property prediction plan"),
        ("cheminf_toxicity_alert", "Toxicity structural alerts"),
        ("cheminf_metabolite", "Metabolite prediction outline"),
        ("cheminf_reaction_smarts", "Reaction SMARTS encoding"),
        ("cheminf_retrosyn_template", "Template retrosynthesis"),
        ("cheminf_library_enum", "Combinatorial library enum"),
        ("cheminf_diversity_select", "Diverse subset selection"),
        ("cheminf_clustering_mol", "Molecular clustering"),
        ("cheminf_mcp_map", "Matched molecular pairs"),
        ("cheminf_rgroup", "R-group decomposition"),
        ("cheminf_ph4", "Pharmacophore modeling outline"),
        ("cheminf_shape_sim", "Shape similarity screening"),
        ("cheminf_dock_rescore", "Docking rescoring strategies"),
        ("cheminf_md_ligand", "Ligand MD stability notes"),
        ("cheminf_free_energy", "Free energy perturbation outline"),
        ("cheminf_crystal_packing", "Crystal packing / polymorph notes"),
        ("cheminf_spectrum_predict", "NMR/MS spectrum prediction notes"),
        ("cheminf_pubchem_assay", "PubChem bioassay mining plan"),
        ("cheminf_chembl_query", "ChEMBL activity query design"),
        ("cheminf_pdb_ligand", "PDB ligand extraction"),
        ("cheminf_sdf_io", "SDF read/write workflow"),
        ("cheminf_parquet_mol", "Large moltable → parquet plan"),
        ("cheminf_active_learning_qsar", "Active learning for QSAR"),
        ("cheminf_multiobj_opt", "Multi-objective molecule opt"),
        ("cheminf_generative_smiles", "SMILES generative model outline"),
        ("cheminf_graph_nn", "Molecular GNN training outline"),
        ("cheminf_contrastive_mol", "Molecular contrastive learning"),
        ("cheminf_reagents_db", "Reagent database hygiene"),
        ("cheminf_eln_chem", "Chemistry ELN reaction table"),
        ("cheminf_green_chem_score", "Green chemistry scoring"),
        ("cheminf_patent_markush", "Markush structure notes"),
        ("cheminf_fair_chem", "FAIR chemical data packaging"),
    ]
    return _pairs("cheminformatics", items, tags="cheminformatics chemistry qsar")


def _extra_research() -> List[Dict[str, Any]]:
    """Additional cross-cutting research ops to push past 250 with core pack."""
    items = [
        ("res_preregister", "Study pre-registration template"),
        ("res_power_calc", "Statistical power calculation"),
        ("res_sample_size", "Sample size justification"),
        ("res_blind_design", "Blinding / randomization design"),
        ("res_irreproducible", "Irreproducibility risk checklist"),
        ("res_open_data", "Open data release checklist"),
        ("res_code_ocean", "Compute capsule packaging"),
        ("res_container_repro", "Docker/Singularity repro env"),
        ("res_citation_graph", "Citation graph exploration"),
        ("res_evidence_grade", "Evidence grading (study design)"),
        ("res_conflict_interest", "COI disclosure checklist"),
        ("res_ethics_irb", "IRB/ethics protocol notes"),
        ("res_biosafety", "Biosafety level checklist"),
        ("res_chemical_safety", "Chemical hygiene plan notes"),
        ("res_data_dictionary", "Data dictionary template"),
        ("res_crd_protocol", "CRD / factorial experiment design"),
        ("res_doe_response", "Design of experiments (DoE)"),
        ("res_bayes_ab", "Bayesian A/B analysis outline"),
        ("res_meta_analysis", "Meta-analysis workflow"),
        ("res_forest_plot", "Forest plot constructive chart"),
        ("res_funnel_plot", "Publication bias funnel plot"),
        ("res_prisma_update", "PRISMA 2020 checklist"),
        ("res_arrive", "ARRIVE animal research checklist"),
        ("res_strobe", "STROBE observational checklist"),
        ("res_consort", "CONSORT trial checklist"),
        ("res_spirit", "SPIRIT protocol checklist"),
        ("res_tripod", "TRIPOD prediction model checklist"),
        ("res_claim_graph", "Link claim → evidence in Atlas"),
        ("res_agent_handoff", "Multi-agent handoff protocol"),
        ("res_atlas_export", "Export Atlas graph JSON"),
    ]
    return _pairs("research_ops", items, tags="reproducibility methods atlas")


def builtin_extended() -> List[Dict[str, Any]]:
    return _ml_skills() + _compbio_skills() + _cheminf_skills() + _extra_research()


def _skill_dirs() -> List[Path]:
    dirs: List[Path] = []
    env = (os.environ.get("RH_SKILLS_DIR") or "").strip()
    if env:
        dirs.append(Path(env))
    # repo-relative skills pack
    here = Path(__file__).resolve()
    repo = here.parents[2] if len(here.parents) >= 3 else here.parent
    dirs.append(repo / "skills")
    dirs.append(Path.home() / ".researchershub" / "skills")
    return dirs


def _load_file(path: Path) -> List[Dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return []
    data: Any = None
    if path.suffix.lower() in (".yaml", ".yml") and yaml is not None:
        try:
            data = yaml.safe_load(text)
        except Exception:
            data = None
    if data is None:
        try:
            data = json.loads(text)
        except Exception:
            return []
    items: List[Any]
    if isinstance(data, dict) and "skills" in data:
        items = data["skills"]
    elif isinstance(data, list):
        items = data
    elif isinstance(data, dict) and data.get("id"):
        items = [data]
    else:
        return []
    out: List[Dict[str, Any]] = []
    for it in items:
        if not isinstance(it, dict) or not it.get("id"):
            continue
        out.append(
            _s(
                str(it["id"]),
                str(it.get("domain") or "custom"),
                str(it.get("desc") or it.get("description") or it["id"]),
                kind=str(it.get("kind") or "atomic"),
                tags=str(it.get("tags") or "custom editable"),
                worker=str(it.get("worker") or "SCRUTATOR"),
            )
        )
        out[-1]["source"] = str(path)
        out[-1]["editable"] = True
    return out


def load_external_skills() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for d in _skill_dirs():
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*")):
            if p.suffix.lower() not in (".json", ".yaml", ".yml"):
                continue
            out.extend(_load_file(p))
    return out


def all_extended_skills() -> List[Dict[str, Any]]:
    seen = set()
    out: List[Dict[str, Any]] = []
    for s in builtin_extended() + load_external_skills():
        sid = s["id"]
        if sid in seen:
            continue
        seen.add(sid)
        out.append(s)
    return out


def write_example_skill_pack(path: Optional[Path] = None) -> str:
    """Write an example editable skill file for operators."""
    p = path or (Path.home() / ".researchershub" / "skills" / "example_custom.json")
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "skills": [
            {
                "id": "custom_lab_assay_template",
                "domain": "custom",
                "desc": "Example editable skill — replace with your lab assay",
                "tags": "custom editable",
                "kind": "playbook",
            }
        ]
    }
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return str(p)
