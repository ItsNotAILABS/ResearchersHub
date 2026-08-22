<p align="center">
  <img src="docs/brand/researchershub-wordmark.svg" alt="ResearchersHub" width="540"/>
</p>

# ResearchersHub

**Local research compute, scientific workflow and artifact server for humans and agents.**

ResearchersHub gives a researcher and a coding agent the same local runtime: searchable skills, structured research construction, Python-backed computation, publication figures, evidence packs and exported artifacts.

The repository includes **971 JSON research skills**, browser desk surfaces and an MCP/REST-compatible host.

```text
Research question
      │
      ▼
ResearchersHub
      │
      ├── skill discovery
      ├── research construction
      ├── Python / numerical compute
      ├── chart / figure generation
      ├── source/provenance metadata
      └── artifact export
      │
      ▼
PNG / Python / data / evidence pack / NEXUS artifact
```

## Quick start

```bash
git clone https://github.com/ItsNotAILABS/ResearchersHub.git
cd ResearchersHub
pip install -r requirements-researchers.txt
export PYTHONPATH="$PWD/src"
python -m pocket serve --host 127.0.0.1 --port 8787
```

Windows PowerShell:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pocket serve --host 127.0.0.1 --port 8787
```

Open:

```text
http://127.0.0.1:8787/desk
```

The Python package still uses the historical `src/pocket` module name; the product is ResearchersHub.

## Agent/API use

A local agent can call the same research host through MCP/HTTP tools rather than maintaining a second research implementation.

Example construction request:

```bash
curl -X POST http://127.0.0.1:8787/v1/researchers/construct \
  -H 'content-type: application/json' \
  -d '{"prompt":"titration curve"}'
```

A figure workflow can produce both a rendered artifact and the Python/source used to construct it.

## Research skills

The `skills/` directory contains the machine-readable skill library used to select domain workflows. Skills should describe inputs, computation/research steps, expected outputs and artifact form rather than acting as opaque prompts.

## NEXUS federation

Declaration: [`ecosystem.surface.json`](ecosystem.surface.json).

Primary federation actions:

```text
research.skill_search
research.construct
research.compute
research.figure
research.export
research.evidence_pack
```

Typical outputs:

```text
nexus.artifact.v1
nexus.execution-receipt.v1
nexus.context-pack.v1
nexus.release-evidence.v1
nexus.handoff.v1
```

ResearchersHub is the research/artifact plane; POCKET owns user/team/policy and NEXUS owns cross-repo routing.

## Production research flow

```text
question
 -> select workflow/skill
 -> identify required data/assumptions
 -> compute or analyze
 -> create figure/data/report artifact
 -> hash artifact
 -> record provenance
 -> produce evidence pack
 -> hand off to POCKET/NEXUS/publishing lane
```

## Artifact discipline

For research that will be used in a paper, release or external claim, preserve:

```text
input data/source references
code used for computation
parameters/assumptions
figure/data artifact
sha256
software/runtime version
request ID
research timestamp
```

That makes a result reproducible by the next agent instead of becoming a screenshot with no lineage.

## Verify

Run the repository's test/figure workflows for the research lane being changed. For ecosystem compatibility:

```bash
# from ItsNotAILABS/nexus
python tools/validate_ecosystem_protocols.py
python tools/validate_ecosystem_registry.py
python tools/production_gate.py
```

## Storage

Running ResearchersHub maintains user artifacts under the local ResearchersHub state directory, including generated figures and research atlas/state. Keep generated research artifacts separate from source-controlled templates unless they are intentional release evidence.

## Documentation

Start with [`docs/HOW_TO_USE.md`](docs/HOW_TO_USE.md) for the human/agent workflow and the repository docs for specific research lanes.

## Ecosystem

- [NEXUS](https://github.com/ItsNotAILABS/nexus) — research task routing and evidence contracts
- [POCKET](https://github.com/ItsNotAILABS/pocket) — user/team/product host
- [POCKET Agent](https://github.com/ItsNotAILABS/pocket-agent) — long-running research execution
- [MatDaemon](https://github.com/ItsNotAILABS/MatDaemon) — bounded numerical compute
- [Medina Memory](https://github.com/ItsNotAILABS/MedinaMemorySystems) — durable findings/context

ResearchersHub turns research into **reusable computation plus artifacts**, not one-off prose.