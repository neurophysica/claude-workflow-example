# claude-workflow-example

A **worked example** of the Claude Chat ↔ Claude Code workflow, built from
[claude-workflow-template](https://github.com/neurophysica/claude-workflow-template).

The toy project is `unitconv`, a tiny command-line unit converter. It's deliberately trivial
— the point isn't the code, it's watching the **two-surface loop** in action: design a spec in
Claude Chat, execute it in Claude Code, review the diff, commit.

## 👉 Start here: [WALKTHROUGH.md](WALKTHROUGH.md)

The walkthrough narrates the whole build step by step, with the (illustrative) Claude Chat
exchanges, the real Claude Code diffs, and links to the specs, files, and commits that
resulted. Each step is also a git tag (`step_01`, `step_02`, `step_03`) so you can check out or
diff any point in the story.

> **Note:** the Claude Chat turns in the walkthrough are illustrative reconstructions written
> to be didactic — not a verbatim log. The Claude Code side (code, diffs, commits, tags) is
> real.

## Try the toy

```bash
# Run the CLI
python -m unitconv 10 km mi        # -> 6.21371 mi

# Run the tests (ephemeral pytest via uv; no install needed)
uv run --with pytest python -m pytest
```

## How it's organized

| Path | What it is |
|---|---|
| [`WALKTHROUGH.md`](WALKTHROUGH.md) | The narrated build — read this first |
| [`docs/dev/specs/`](docs/dev/specs/) | The specs the project was built from |
| [`docs/dev/walkthrough/`](docs/dev/walkthrough/) | Per-step annotated Chat/Code transcripts |
| [`docs/dev/DECISIONS.md`](docs/dev/DECISIONS.md) | Decisions locked during the build |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Progress tracker |
| [`unitconv/`](unitconv/) · [`tests/`](tests/) | The toy code and its tests |
