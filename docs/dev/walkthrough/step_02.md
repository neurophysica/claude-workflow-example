# Step 2 — the command-line interface

**Goal:** wrap `convert()` in a `python -m unitconv` CLI, with tests.
**Spec:** [spec_02_cli.md](../specs/spec_02_cli.md) ·
**Tag:** `step_02` ·
**Commit:** [`874e4c6`](https://github.com/neurophysica/claude-workflow-example/commit/874e4c6)

## 1. Design — in Claude Chat 💬

*(You've just re-uploaded the updated `ROADMAP.md` from Step 1, so Chat knows Step 1 is done.)*

> **🧑 → 💬:** Now give it a command line: `unitconv 10 km mi`. Spec it.
>
> **💬:** The CLI should stay a *thin* wrapper — all the logic already lives in `convert()`, so
> `__main__.py` just parses args and prints. Two things to get right: format the number
> cleanly (`%g`), and turn a bad unit into a friendly one-line error via `parser.error(...)`
> instead of a Python traceback. For tests, call `main([...])` directly *and* run it as a
> subprocess so we know `python -m unitconv` actually works.
>
> *(💬 emits `spec_02_cli.md`.)*

> **🧑 Handoff — Chat → repo → Code**
> 1. Download the spec, save it as `docs/dev/specs/spec_02_cli.md`.
> 2. In Claude Code: `implement docs/dev/specs/spec_02_cli.md`

## 2. Execute — in Claude Code ⌨️

> **⌨️:** Added the argparse entry point; it reuses `convert()` unchanged:

```python
# unitconv/__main__.py  (excerpt)
args = parser.parse_args(argv)
try:
    result = convert(args.value, args.from_unit, args.to_unit)
except ValueError as exc:
    parser.error(str(exc))       # clean message, no traceback
print(f"{result:g} {args.to_unit}")
```

> **⌨️:** All green, including the subprocess test that runs the module for real:
>
> ```
> 6 passed in 0.10s
> ```

## 3. Review & commit

**🧑** approves the diff. Commit + tag:

```
Step 2: command-line interface (impl of spec_02)
```

→ See exactly what changed since Step 1:
[`compare/step_01...step_02`](https://github.com/neurophysica/claude-workflow-example/compare/step_01...step_02)

> **🧑 Handoff — repo → Chat**
> Re-upload `docs/ROADMAP.md` (Step 2 ticked) to Chat before designing Step 3.

## What just happened

- **The core didn't change.** The CLI is a thin consumer of `convert()` — a recurring shape in
  this workflow (interfaces and notebooks stay thin; logic lives in the package).
- The spec pinned a **testable contract** (`"6.21371 mi"`), so "done" was unambiguous.

Next: **[Step 3 — mass units & typed errors »](step_03.md)**
