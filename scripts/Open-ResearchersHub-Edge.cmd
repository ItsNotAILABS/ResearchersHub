@echo off
title ResearchersHub
set ROOT=%~dp0..
set PYTHONPATH=%ROOT%\src

REM Ensure host is up
powershell -NoProfile -ExecutionPolicy Bypass -File "%ROOT%\scripts\Start-ResearchersHub.ps1"

set EDGE=
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" set EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe
if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" set EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe

if "%EDGE%"=="" (
  start "" "http://127.0.0.1:8787/desk"
  exit /b 0
)

start "" "%EDGE%" --app=http://127.0.0.1:8787/desk --new-window
exit /b 0
