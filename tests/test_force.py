#!/usr/bin/env python
# coding: utf-8

r"""force.py tests."""

from ydeos_units.units import newton


def test_forces():
    r"""Test expected values."""
    expected_value = 9.81
    atol = 1e-10
    assert expected_value - atol <= newton(kgf=1.) <= expected_value + atol
