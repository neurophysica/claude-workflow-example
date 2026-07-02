# Spec: core length conversion

Scope: **code** — create the `unitconv` package with a single conversion function for length
units, plus tests. No CLI yet (that's Step 2).

Disposable: **no**

Commit gate: do not commit — stage changes and surface the diff for review, then wait for
approval.

## 1. Create the `unitconv` package

- `unitconv/__init__.py` — package docstring; re-export `convert` from `core`.
- `unitconv/core.py` — a `convert(value, from_unit, to_unit)` function for **length** units.
  - Represent each supported unit as a factor to a base unit (metres).
  - Support at least: `m, km, cm, mm, mi, ft, in, yd`.
  - Raise `ValueError` for an unrecognized unit.

## 2. Tests

- `tests/test_core.py` — cover a cross-unit conversion (e.g. km→mi), an identity conversion,
  a metric→imperial conversion, and the unknown-unit error path.

## Report

Show the diff and `pytest` output. Propose a commit message and wait for approval.
