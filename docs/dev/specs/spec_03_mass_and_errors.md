# Spec: mass units, typed errors, incompatibility check

Scope: **code + one decision** — generalize `convert()` beyond length, introduce typed
exceptions, and reject conversions across dimensions. Log the design decision in
`DECISIONS.md`.

Disposable: **no**

Commit gate: do not commit — stage changes and surface the diff for review, then wait for
approval.

## 1. Generalize the conversion model

- Refactor `core.py` to hold one factor table **per dimension** (length → metres,
  mass → kilograms), keyed in a `_DIMENSIONS` registry.
- Add mass units: `kg, g, mg, lb, oz`.
- `convert()` resolves each unit's dimension, then converts via the dimension's base unit.

## 2. Typed exceptions + incompatibility

- Add `UnknownUnitError(ValueError)` and `IncompatibleUnitsError(ValueError)` (both subclass
  `ValueError` so existing callers/tests keep working).
- Raise `UnknownUnitError` for an unrecognized unit.
- Raise `IncompatibleUnitsError` when the two units belong to different dimensions
  (e.g. `kg` → `m`).
- Re-export both exception types from `unitconv/__init__.py`.

## 3. Log the decision

Add a dated entry to `DECISIONS.md` (newest-at-top, above the workflow baseline):
convert via a base unit per dimension.
- **Rationale:** O(1) storage per unit and trivial extension to new dimensions, versus an
  N×N table of pairwise factors that grows quadratically and duplicates information.

## 4. Tests

Extend `tests/test_core.py`: a mass conversion (e.g. kg→lb), and that `kg`→`m` raises
`IncompatibleUnitsError`.

## Report

Show the diff and `pytest` output. Propose a commit message and wait for approval.
