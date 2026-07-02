# Step 3 — mass units & typed errors

**Goal:** generalize beyond length, add typed exceptions, reject cross-dimension conversions,
and log the design decision.
**Spec:** [spec_03_mass_and_errors.md](../specs/spec_03_mass_and_errors.md) ·
**Tag:** `step_03` ·
**Commit:** [`05080e9`](https://github.com/neurophysica/claude-workflow-example/commit/05080e9)

## 1. Design — in Claude Chat 💬

> **🧑 → 💬:** Add mass units too. And `kg → m` should fail cleanly, not silently.
>
> **💬:** This is where the Step 1 base-unit idea pays off: keep one factor table *per
> dimension* (metres for length, kilograms for mass) in a small registry, and have `convert()`
> resolve each unit's dimension first. Add `UnknownUnitError` and `IncompatibleUnitsError` —
> I'd subclass both from `ValueError` so nothing that already catches `ValueError` breaks.
> Cross-dimension conversions raise `IncompatibleUnitsError`. This design is now load-bearing,
> so let's **log it in `DECISIONS.md`**.
>
> *(💬 emits `spec_03_mass_and_errors.md`, including a "log the decision" step.)*

> **🧑 Handoff — Chat → repo → Code**
> 1. Download the spec, save it as `docs/dev/specs/spec_03_mass_and_errors.md`.
> 2. In Claude Code: `implement docs/dev/specs/spec_03_mass_and_errors.md`

## 2. Execute — in Claude Code ⌨️

> **⌨️:** Refactored to a per-dimension registry and added the typed exceptions:

```python
# unitconv/core.py  (excerpt)
_DIMENSIONS = {"length": _LENGTH_TO_M, "mass": _MASS_TO_KG}

class UnknownUnitError(ValueError): ...
class IncompatibleUnitsError(ValueError): ...

def convert(value, from_unit, to_unit):
    from_dim, from_table = _resolve(from_unit)
    to_dim, to_table = _resolve(to_unit)
    if from_dim != to_dim:
        raise IncompatibleUnitsError(...)
    return value * from_table[from_unit] / to_table[to_unit]
```

> **⌨️:** Logged the decision in `DECISIONS.md`, extended the tests, and confirmed the CLI:
>
> ```
> 8 passed in 0.10s
> $ python -m unitconv 1 kg lb   ->  2.20462 lb
> ```

## 3. Review & commit

**🧑** approves. Commit + tag:

```
Step 3: mass units, typed errors, incompatibility check (impl of spec_03)
```

→ Diff since Step 2:
[`compare/step_02...step_03`](https://github.com/neurophysica/claude-workflow-example/compare/step_02...step_03) ·
→ The logged decision:
[`DECISIONS.md`](../DECISIONS.md)

> **🧑 Handoff — repo → Chat**
> This step changed **two** durable files — re-upload both `docs/dev/DECISIONS.md` and
> `docs/ROADMAP.md` so Chat's context reflects the new decision and the completed roadmap.

## What just happened

- A **decision from Chat became durable**: the base-unit model is now an entry in
  `DECISIONS.md`, so a future session won't re-litigate it.
- The refactor was **backward-compatible** — subclassing `ValueError` meant Step 1's error
  test still passed untouched.
- `ROADMAP.md` shows all three steps `[x]` — the tracker and reality agree.

← Back to the **[walkthrough index](../../../WALKTHROUGH.md)**
