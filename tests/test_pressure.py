#!/usr/bin/env python
# coding: utf-8

r"""pressure.py tests"""

from ydeos_units.units import millibar


def test_pressures():
    r"""Test expected values"""
    expected_value = 1e3
    atol = 1e-10
    assert expected_value - atol <= millibar(bar=1.) <= expected_value + atol
