"""Tests for unitconv.core.convert (length and mass units)."""

import pytest

from unitconv.core import IncompatibleUnitsError, convert


def test_km_to_mi():
    assert convert(10, "km", "mi") == pytest.approx(6.2137119, rel=1e-6)


def test_kg_to_lb():
    assert convert(1, "kg", "lb") == pytest.approx(2.2046226, rel=1e-6)


def test_incompatible_dimensions():
    with pytest.raises(IncompatibleUnitsError):
        convert(1, "kg", "m")


def test_identity():
    assert convert(5, "m", "m") == 5


def test_m_to_ft():
    assert convert(1, "m", "ft") == pytest.approx(3.28084, rel=1e-5)


def test_unknown_unit():
    with pytest.raises(ValueError):
        convert(1, "m", "furlong")
