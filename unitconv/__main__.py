"""Command-line interface: ``python -m unitconv VALUE FROM TO``."""

from __future__ import annotations

import argparse
import sys

from .core import convert


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, run one conversion, and print the result.

    Args:
        argv: Argument list (defaults to ``sys.argv[1:]``).

    Returns:
        Process exit code (``0`` on success).
    """
    parser = argparse.ArgumentParser(
        prog="unitconv", description="Convert a value between units."
    )
    parser.add_argument("value", type=float, help="numeric value to convert")
    parser.add_argument("from_unit", help="unit to convert from (e.g. km)")
    parser.add_argument("to_unit", help="unit to convert to (e.g. mi)")
    args = parser.parse_args(argv)

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except ValueError as exc:
        parser.error(str(exc))

    print(f"{result:g} {args.to_unit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
