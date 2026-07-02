# Step 1 — core length conversion

**Goal:** a `convert()` for length units, with tests. No CLI yet.
**Spec:** [spec_01_core_length.md](../specs/spec_01_core_length.md) ·
**Tag:** `step_01` ·
**Commit:** [`0b862c2`](https://github.com/neurophysica/claude-workflow-example/commit/0b862c2)

## 1. Design — in Claude Chat 💬

> **🧑 → 💬:** Let's start the unit converter with the smallest useful core: length
> conversion only, no CLI yet. Draft a spec.
>
> **💬:** Good scope for step one. One design choice worth locking early: instead of storing a
> factor for every *pair* of units, store one factor per unit to a common base (metres) and
> convert *through* it. That's O(1) per unit and trivial to extend to new dimensions later.
> I'll specify `convert(value, from_unit, to_unit)`, a metres table (`m, km, cm, mm, mi, ft,
> in, yd`), and a `ValueError` for unknown units. Tests: a cross-unit case, an identity, a
> metric→imperial case, and the error path.
>
> *(💬 emits `spec_01_core_length.md` as a downloadable file.)*

**🧑 saves it** to `docs/dev/specs/` and tells Claude Code: *"implement
`docs/dev/specs/spec_01_core_length.md`."*

## 2. Execute — in Claude Code ⌨️

> **⌨️:** Created the `unitconv` package with the factors-to-metres model from the spec:

```python
# unitconv/core.py  (excerpt)
_LENGTH_TO_M = {"m": 1.0, "km": 1000.0, "mi": 1609.344, "ft": 0.3048, ...}

def convert(value, from_unit, to_unit):
    for unit in (from_unit, to_unit):
        if unit not in _LENGTH_TO_M:
            raise ValueError(f"unknown unit: {unit!r}")
    return value * _LENGTH_TO_M[from_unit] / _LENGTH_TO_M[to_unit]
```

> **⌨️:** Tests pass — and per the commit gate I stopped for review rather than committing:
>
> ```
> 4 passed in 0.02s
> ```

## 3. Review & commit

**🧑** reads the diff, approves. Code commits with a solo sign-off and tags the point:

```
Step 1: core length conversion (impl of spec_01)
```

→ Browse the repo as of this step: [`tree/step_01`](https://github.com/neurophysica/claude-workflow-example/tree/step_01)

## What just happened

- The **spec was the unit of execution** — a file, not pasted text.
- The **base-unit design idea** came from Chat here; it gets *generalized and logged* as a
  formal decision in [Step 3](step_03.md).
- Code **did not commit on its own** — it surfaced the diff and waited (the gate from
  `CLAUDE.md`).

Next: **[Step 2 — the CLI »](step_02.md)**
