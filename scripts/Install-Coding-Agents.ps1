# Optional: copy ResearchersHub skill pack into local agent skill directories.
# Does not change the public repo layout — only writes under the user profile.
$ErrorActionPreference = "Continue"
$Root = Split-Path $PSScriptRoot -Parent
if (-not (Test-Path "$Root\src\pocket")) {
  $Root = "C:\Users\Medin\OneDrive\ResearchersHub"
}

Write-Host "ResearchersHub — optional local skill install" -ForegroundColor Cyan
Write-Host "Root: $Root"

$src = Join-Path $Root "skills\researchershub"
if (-not (Test-Path $src)) {
  Write-Host "Missing skills\researchershub" -ForegroundColor Red
  exit 1
}

# Common local skill roots used by various coding agents (all under user home)
$targets = @(
  (Join-Path $env:USERPROFILE ".researchershub\skills\researchershub"),
  (Join-Path $env:USERPROFILE ".agents\skills\researchershub")
)
# Also mirror if those tool dirs already exist on this machine
foreach ($extra in @(
  (Join-Path $env:USERPROFILE ".grok\skills\researchershub"),
  (Join-Path $env:USERPROFILE ".claude\skills\researchershub")
)) {
  $parent = Split-Path (Split-Path $extra)
  if (Test-Path $parent) { $targets += $extra }
}

foreach ($t in $targets) {
  New-Item -ItemType Directory -Force -Path (Split-Path $t) | Out-Null
  Copy-Item -Recurse -Force $src $t
  Write-Host "  + $t" -ForegroundColor Green
}

$hint = Join-Path $env:USERPROFILE ".researchershub\CODING_AGENTS_HINT.txt"
New-Item -ItemType Directory -Force -Path (Split-Path $hint) | Out-Null
@"
ResearchersHub tools
====================
Repo: $Root
Host: set PYTHONPATH=$Root\src ; python -m pocket serve
MCP:  set PYTHONPATH=$Root\src ; python -m pocket mcp
Docs: $Root\AGENTS.md , $Root\docs\developers\
Invoke: POST http://127.0.0.1:8787/v1/agents/invoke
"@ | Set-Content $hint -Encoding UTF8
Write-Host "  + $hint" -ForegroundColor Green
Write-Host "DONE." -ForegroundColor Cyan
