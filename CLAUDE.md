# CLAUDE.md

Guidance for Claude Code (and humans) working in this repo. Read this first each session.

## What this project is

A **worked example** of the Claude Chat ↔ Claude Code workflow (see
[docs/dev/WORKFLOW.md](docs/dev/WORKFLOW.md)). The toy project is `unitconv`, a tiny
command-line **unit converter** — deliberately trivial so the focus stays on the *workflow*,
not the code. The project was built one spec at a time; the narrated journey is in
[WALKTHROUGH.md](WALKTHROUGH.md).

## Layout

```
unitconv/            # the package
  __init__.py
  core.py            # convert(): the conversion logic
  __main__.py        # `python -m unitconv` CLI
tests/               # pytest tests
docs/
  ROADMAP.md         # progress tracker
  dev/
    WORKFLOW.md      # how the two Claude surfaces coordinate
    DECISIONS.md     # locked decisions (workflow baseline + project decisions)
    specs/           # the specs this project was built from
    walkthrough/     # per-step annotated Chat/Code transcripts
WALKTHROUGH.md       # start here: the narrated build
```

## Conventions

- Python ≥ 3.10, standard library only (no runtime dependencies).
- Tests are **pytest**; `testpaths = ["tests"]`.
- Every spec that built this repo is kept under `docs/dev/specs/` as provenance.

## Environment

```bash
# Run the tests with an ephemeral pytest (no project install needed):
uv run --with pytest python -m pytest

# Run the CLI:
python -m unitconv 10 km mi
```

## Living documents (keep in sync as we work)

| Document | Purpose | Update when… |
|---|---|---|
| `CLAUDE.md` (this file) | Stable overview, layout, conventions, env | Architecture, conventions, deps, or layout change |
| `docs/ROADMAP.md` | Live progress tracker | A milestone starts or lands; focus or plan changes |
| `docs/dev/DECISIONS.md` | Dated log of locked decisions | A decision is made, changed, or superseded |
| `docs/dev/WORKFLOW.md` | How Claude Chat + Claude Code coordinate via the repo | The two-surface process or division of labor changes |
| `README.md` | Public-facing summary + setup | User-facing setup or scope changes |

## Git conventions

- **Wait for the human before committing.** Do not run `git commit` or push until explicitly
  asked — the human reviews the diff first. Prepare/stage and surface the change, then wait.
- **Commit sign-off is solo — do NOT add `Co-Authored-By` or any co-author trailer.**
  Use exactly: `Signed-off-by: Wisam Reid <wisam@g.harvard.edu>`
- Default branch is `main`.
