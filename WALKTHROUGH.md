# Walkthrough: building `unitconv` with the CC↔CCh workflow

This is the narrated build of the toy project in this repo. It shows one full turn of the loop
per step: **design in Claude Chat → save a spec → execute in Claude Code → review → commit**.

> ⚠️ The **Claude Chat** turns below are *illustrative reconstructions* — written to be
> didactic, not a verbatim log. The **Claude Code** side (diffs, tests, commits, tags) is
> **real**: every step is a git tag you can check out or diff.

## The cast

- **🧑 Human** — the hands: sets direction, and does the manual glue — **uploads files to
  Chat, saves specs into the repo, points Code at them**, reviews diffs, approves commits.
- **💬 Claude Chat (CC)** — designs, writes specs, reviews. *No filesystem access — you upload
  files to it.*
- **⌨️ Claude Code (CCh)** — executes specs, runs tests, commits. *Has the repo — no uploads
  needed.*
- **📁 The repo** — the shared memory. Specs and results live here, not in either chat.

## The loop, in one line

`design (CC)` → `spec file in docs/dev/specs/` → `"implement it" (CCh)` → `diff + tests` →
`human approves` → `commit + tag` → repeat.

The 🧑 actions between surfaces — **which files you upload, when you save a spec, how you point
Code at it, and re-uploading changed files to keep Chat current** — are the workflow's plumbing.
**[Step 0](docs/dev/walkthrough/step_00_setup.md)** lays them out, and every step below marks
them with **🧑 Handoff** callouts.

## The steps

| Step | Goal | Spec | Tag | Commit |
|---|---|---|---|---|
| 0 | Set up the two surfaces | — | — | — |
| 1 | Core length conversion | [spec_01](docs/dev/specs/spec_01_core_length.md) | `step_01` | [`196658b`](https://github.com/neurophysica/claude-workflow-example/commit/196658b) |
| 2 | Command-line interface | [spec_02](docs/dev/specs/spec_02_cli.md) | `step_02` | [`e14429d`](https://github.com/neurophysica/claude-workflow-example/commit/e14429d) |
| 3 | Mass units + typed errors | [spec_03](docs/dev/specs/spec_03_mass_and_errors.md) | `step_03` | [`05080e9`](https://github.com/neurophysica/claude-workflow-example/commit/05080e9) |

Read them in order:

0. **[Step 0 — set up the two surfaces](docs/dev/walkthrough/step_00_setup.md)** (uploads, opening the repo in Code)
1. **[Step 1 — core length conversion](docs/dev/walkthrough/step_01.md)**
2. **[Step 2 — the CLI](docs/dev/walkthrough/step_02.md)**
3. **[Step 3 — mass units & typed errors](docs/dev/walkthrough/step_03.md)**

## What to notice as you read

- The **spec is the unit of work** — the human points Code at a *file*, never pastes the task.
- Every spec is **kept** in `docs/dev/specs/` as provenance (see the spec-persistence decision
  in [DECISIONS.md](docs/dev/DECISIONS.md)).
- Code **stops before committing** and waits for approval — the human-in-the-loop gate from
  [CLAUDE.md](CLAUDE.md).
- Design decisions born in Chat get **promoted to `DECISIONS.md`** so they survive the session.

## Try it yourself

```bash
python -m unitconv 10 km mi                 # -> 6.21371 mi
uv run --with pytest python -m pytest       # -> 8 passed
git checkout step_01                         # rewind to the end of Step 1
```
