# Install ResearchersHub skill packs for local coding agents (Grok, optional Claude skill dir)
$ErrorActionPreference = "Continue"
$Root = Split-Path $PSScriptRoot -Parent
if (-not (Test-Path "$Root\src\pocket")) {
  $Root = "C:\Users\Medin\OneDrive\ResearchersHub"
}

Write-Host "ResearchersHub coding-agent install" -ForegroundColor Cyan
Write-Host "Root: $Root"

# Grok skill
$grokSkills = Join-Path $env:USERPROFILE ".grok\skills\researchershub"
New-Item -ItemType Directory -Force -Path (Split-Path $grokSkills) | Out-Null
Copy-Item -Recurse -Force (Join-Path $Root "skills\researchershub") $grokSkills
Write-Host "  + Grok skill -> $grokSkills" -ForegroundColor Green

# Claude-style project skill mirror under user home (optional)
$claudeSkills = Join-Path $env:USERPROFILE ".claude\skills\researchershub"
New-Item -ItemType Directory -Force -Path (Split-Path $claudeSkills) | Out-Null
Copy-Item -Recurse -Force (Join-Path $Root "skills\researchershub") $claudeSkills
Write-Host "  + Claude skill dir -> $claudeSkills" -ForegroundColor Green

# Codex / agents note
$agentsHint = Join-Path $env:USERPROFILE ".researchershub\CODING_AGENTS_HINT.txt"
New-Item -ItemType Directory -Force -Path (Split-Path $agentsHint) | Out-Null
@"
ResearchersHub coding agents
============================
Repo: $Root
MCP:  set PYTHONPATH=$Root\src ; python -m pocket mcp
Host: set PYTHONPATH=$Root\src ; python -m pocket serve
Docs: $Root\AGENTS.md , $Root\docs\CODING_AGENTS.md
Invoke: POST http://127.0.0.1:8787/v1/agents/invoke
"@ | Set-Content $agentsHint -Encoding UTF8
Write-Host "  + Hint -> $agentsHint" -ForegroundColor Green

# Smoke tools
$env:PYTHONPATH = Join-Path $Root "src"
python -m pocket tools 2>$null | Select-Object -First 5
Write-Host "DONE. Point Claude/Cursor MCP at: python -m pocket mcp (PYTHONPATH=src)" -ForegroundColor Cyan
