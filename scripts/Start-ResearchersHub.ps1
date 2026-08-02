# Start ResearchersHub host (local research server)
# Usage: powershell -ExecutionPolicy Bypass -File scripts\Start-ResearchersHub.ps1

$ErrorActionPreference = "Continue"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
if (-not (Test-Path (Join-Path $Root "src\pocket"))) {
  $Root = "C:\Users\Medin\OneDrive\ResearchersHub"
}
$Src = Join-Path $Root "src"

$py = "C:\Users\Medin\AppData\Local\Programs\Python\Python311-arm64\python.exe"
if (-not (Test-Path $py)) {
  $c = Get-Command python -ErrorAction SilentlyContinue
  if ($c) { $py = $c.Source } else { throw "Python not found — install Python 3.11+" }
}

$env:PYTHONPATH = $Src
$env:Path = "C:\Users\Medin\.grok\bin;" + $env:Path

# Optional secrets (never commit these files)
foreach ($f in @(
  (Join-Path $env:USERPROFILE ".researchershub\access.env"),
  (Join-Path $env:USERPROFILE ".pocket\access.env")
)) {
  if (Test-Path $f) {
    Get-Content $f | ForEach-Object {
      if ($_ -match '^\s*([A-Z0-9_]+)=(.*)$') {
        Set-Item -Path ("env:" + $matches[1]) -Value $matches[2].Trim()
      }
    }
  }
}

function HealthOk {
  try {
    $r = Invoke-WebRequest "http://127.0.0.1:8787/health" -UseBasicParsing -TimeoutSec 3
    return ($r.StatusCode -eq 200)
  } catch { return $false }
}

if (HealthOk) {
  Write-Host "ResearchersHub already up → http://127.0.0.1:8787/desk" -ForegroundColor Green
  exit 0
}

$logDir = Join-Path $env:USERPROFILE ".researchershub"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$out = Join-Path $logDir "serve.out.log"
$err = Join-Path $logDir "serve.err.log"

Write-Host "Starting ResearchersHub host on :8787 ..." -ForegroundColor Cyan
Start-Process -FilePath $py -ArgumentList "-u","-m","pocket","serve","--host","127.0.0.1","--port","8787" `
  -WorkingDirectory $Root -WindowStyle Hidden `
  -RedirectStandardOutput $out -RedirectStandardError $err | Out-Null

Start-Sleep -Seconds 5
if (HealthOk) {
  Write-Host "UP  desk  http://127.0.0.1:8787/desk" -ForegroundColor Green
  Write-Host "    health http://127.0.0.1:8787/health"
  Write-Host "    skills http://127.0.0.1:8787/v1/researchers/skills"
  exit 0
}

Write-Host "Host did not become healthy. Check:" -ForegroundColor Yellow
Write-Host "  $err"
exit 1
