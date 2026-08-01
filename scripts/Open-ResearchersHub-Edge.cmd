@echo off
title ResearchersHub Edge App
set ROOT=C:\Users\Medin\OneDrive\ResearchersHub
set PYTHONPATH=%ROOT%\src
set Path=C:\Users\Medin\.grok\bin;%Path%

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$ErrorActionPreference='Continue'; $env:PYTHONPATH='%ROOT%\src'; " ^
  "try { $r=Invoke-WebRequest 'http://127.0.0.1:8787/health' -UseBasicParsing -TimeoutSec 3 } catch { " ^
  "  Start-Process -FilePath 'C:\Users\Medin\AppData\Local\Programs\Python\Python311-arm64\python.exe' " ^
  "    -ArgumentList '-u','-m','pocket','serve','--host','0.0.0.0','--port','8787' " ^
  "    -WorkingDirectory '%ROOT%' -WindowStyle Hidden; Start-Sleep 5 }"

set EDGE=
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" set EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe
if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" set EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe
if "%EDGE%"=="" (
  start "" "http://127.0.0.1:8787/desk"
  exit /b 0
)
start "" "%EDGE%" --app=http://127.0.0.1:8787/desk --new-window
exit /b 0
