"""Core unit-conversion logic (length units)."""

from __future__ import annotations

# Length units expressed as a factor to the base unit (metres).
_LENGTH_TO_M = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "ft": 0.3048,
    "in": 0.0254,
    "yd": 0.9144,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a length ``value`` from ``from_unit`` to ``to_unit``.

    Args:
        value: The numeric magnitude to convert.
        from_unit: The unit ``value`` is expressed in (e.g. ``"km"``).
        to_unit: The unit to convert to (e.g. ``"mi"``).

    Returns:
        The converted magnitude.

    Raises:
        ValueError: If either unit is not a recognized length unit.
    """
    for unit in (from_unit, to_unit):
        if unit not in _LENGTH_TO_M:
            raise ValueError(f"unknown unit: {unit!r}")
    return value * _LENGTH_TO_M[from_unit] / _LENGTH_TO_M[to_unit]
