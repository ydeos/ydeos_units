#!/usr/bin/env python
# coding: utf-8

r"""distance.py tests"""

from ydeos_units.units import cm


def test_distances():
    r"""Test expected values"""
    expected_value = 3.3
    atol = 1e-10
    assert expected_value - atol <= cm(mm=33.) <= expected_value + atol
