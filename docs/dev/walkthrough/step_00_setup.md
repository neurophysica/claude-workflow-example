# Step 0 — set up the two surfaces

Before any code, wire the two Claude surfaces around the repo. You do this **once**, up front.
Everything below is a real manual action *you* (🧑) take — this is the plumbing the rest of the
walkthrough leans on.

## 1. Create the repo and open it in Claude Code ⌨️

- Create a repo from the template — **"Use this template"** on GitHub, or
  `gh repo create <owner>/<name> --template neurophysica/claude-workflow-template` — then clone it.
- **Open the repo directory in Claude Code** (run the `claude` CLI from inside the repo folder,
  or point the IDE / desktop app at it).
- **No uploads to Code.** It has the filesystem and reads [`CLAUDE.md`](../../../CLAUDE.md) on its
  first turn, so it already knows the conventions, layout, and git rules. That's the whole reason
  `CLAUDE.md` lives at the repo root.

## 2. Start Claude Chat and hand it the context 💬

Claude Chat has **no filesystem**, so you give it the durable context by **uploading these files**
at the start of the conversation (a Chat *Project* is a good home for them):

- [`CLAUDE.md`](../../../CLAUDE.md)
- [`docs/dev/WORKFLOW.md`](../WORKFLOW.md)
- [`docs/dev/DECISIONS.md`](../DECISIONS.md)
- [`docs/ROADMAP.md`](../../ROADMAP.md)
- [`docs/dev/specs/SPEC_TEMPLATE.md`](../specs/SPEC_TEMPLATE.md)

Then state its role, e.g.: *"You're the Claude Chat surface for this project — you own design,
specs, and review; Claude Code executes. Emit specs as downloadable files following
SPEC_TEMPLATE.md; I'll save them under `docs/dev/specs/` and run them in Claude Code."*

## The handoff cheatsheet (used at every step below)

Each step of the loop is joined by three manual 🧑 actions. Watch for the **🧑 Handoff** callouts:

- **Chat → repo:** download the spec Chat produced, save it as `docs/dev/specs/<name>.md`.
- **repo → Code:** in Claude Code, say `implement docs/dev/specs/<name>.md`.
- **repo → Chat:** after a commit, **re-upload** any changed durable files (e.g. `DECISIONS.md`,
  `ROADMAP.md`) so Chat's context matches the repo — *Chat only sees the version you last uploaded.*

Next: **[Step 1 — core length conversion »](step_01.md)**
