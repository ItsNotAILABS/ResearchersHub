# ResearchersHub — product definition

## One sentence

**Local research server:** run it on your machine; get 971 skills, real charts, real Python; drive it from a browser desk **or** from coding agents via tools.

## Who uses it

| User | How they use it | What they see |
|------|-----------------|---------------|
| Scientist | Start host → open desk | Chat UI, figures, scripts |
| Coding agent | MCP or REST tools on host | JSON with PNG + Python |
| GitHub visitor | Read repo | Docs, `skills/` JSON, example graphs |

## What happens (core loop)

1. Host runs on `127.0.0.1:8787`  
2. Human or agent sends a task (construct / skills / atlas)  
3. Host computes on your machine  
4. Writes artifacts under `~/.researchershub/`  
5. Returns full figures + code  

## What it is not

- Not a cloud SaaS that owns your data  
- Not “only a skill list” — skills are **inputs** to a **running host**  
- Not private AI-tool folders on GitHub (no public `.grok` product surface)  

## Details

- Human + agent walkthrough: [docs/HOW_TO_USE.md](docs/HOW_TO_USE.md)  
- Public README: [README.md](README.md)  
