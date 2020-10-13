#!/usr/bin/env python
# coding: utf-8

r"""volume.py tests."""

from ydeos_units.units import m3


def test_volume():
    r"""Test expected values."""
    expected_value = 1.
    atol = 1e-10
    assert expected_value - atol <= m3(litre=1000.) <= expected_value + atol