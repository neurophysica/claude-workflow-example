# Spec: command-line interface

Scope: **code** — add a `python -m unitconv` CLI wrapping `convert()`, plus tests. No new
units (that's Step 3).

Disposable: **no**

Commit gate: do not commit — stage changes and surface the diff for review, then wait for
approval.

## 1. Add the CLI

- `unitconv/__main__.py` with a `main(argv=None)` entry point using `argparse`.
  - Positional args: `value` (float), `from_unit`, `to_unit`.
  - Print the result as `"<value:g> <to_unit>"`.
  - On a bad unit (`ValueError` from `convert`), exit with a clean error via
    `parser.error(...)` rather than a traceback.
  - `main` returns an exit code; `if __name__ == "__main__": sys.exit(main())`.

## 2. Tests

- `tests/test_cli.py`:
  - call `main([...])` directly and capture stdout (e.g. `10 km mi -> "6.21371 mi"`).
  - run the module as a subprocess (`python -m unitconv 1 m cm`) and assert the output.

## Report

Show the diff and `pytest` output. Propose a commit message and wait for approval.
