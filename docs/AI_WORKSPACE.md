# AI workspace (ResearchersHub)

Optional host feature for coding / research agents: a **live workspace** that tracks recent jobs and can be injected into the next prompt so agents waste fewer tokens re-discovering context.

## Location

```text
~/.researchershub/   # ResearchersHub construct, atlas, skills
~/.pocket/           # shared host runtime when co-located with POCKET host
```

## Related

- Infinite Wiki inject on `/v1/ai/chat` (when enabled)
- Atlas graph: `GET /v1/researchers/atlas`
- Construct outputs: `~/.researchershub/construct/`

This is operator-local infrastructure — not a cloud workspace owned by a vendor.
