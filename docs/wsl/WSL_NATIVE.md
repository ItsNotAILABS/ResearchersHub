# WSL native (optional)

ResearchersHub can use the host’s WSL integration when the underlying host runtime has WSL agent support enabled.

## Typical use

- Linux toolchains for bioinformatics / ML
- Shell skills that prefer bash over PowerShell

## Setup

1. Install WSL2 + distro.
2. Ensure host process can reach `wsl.exe`.
3. Use desk modes or agent tools that target WSL when available.

This is optional. Core construct (Python charts) runs on Windows Python without WSL.
