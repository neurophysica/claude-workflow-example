"""Core unit-conversion logic.

Conversions are resolved via a **base unit per dimension** (metres for length, kilograms for
mass): each unit stores a single factor to its dimension's base, and any conversion within a
dimension is ``value * factor[from] / factor[to]``. See docs/dev/DECISIONS.md.
"""

from __future__ import annotations

# Each dimension maps its units to a factor to the dimension's base unit.
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
_MASS_TO_KG = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 1e-6,
    "lb": 0.45359237,
    "oz": 0.028349523125,
}
_DIMENSIONS = {"length": _LENGTH_TO_M, "mass": _MASS_TO_KG}


class UnknownUnitError(ValueError):
    """Raised when a unit is not a recognized unit in any dimension."""


class IncompatibleUnitsError(ValueError):
    """Raised when the two units belong to different dimensions."""


def _resolve(unit: str) -> tuple[str, dict[str, float]]:
    """Return the ``(dimension, factor_table)`` a unit belongs to."""
    for dimension, table in _DIMENSIONS.items():
        if unit in table:
            return dimension, table
    raise UnknownUnitError(f"unknown unit: {unit!r}")


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert ``value`` from ``from_unit`` to ``to_unit``.

    Args:
        value: The numeric magnitude to convert.
        from_unit: The unit ``value`` is expressed in (e.g. ``"km"``).
        to_unit: The unit to convert to (e.g. ``"mi"``).

    Returns:
        The converted magnitude.

    Raises:
        UnknownUnitError: If either unit is not recognized.
        IncompatibleUnitsError: If the units are in different dimensions.
    """
    from_dim, from_table = _resolve(from_unit)
    to_dim, to_table = _resolve(to_unit)
    if from_dim != to_dim:
        raise IncompatibleUnitsError(
            f"cannot convert {from_dim} ({from_unit}) to {to_dim} ({to_unit})"
        )
    return value * from_table[from_unit] / to_table[to_unit]
