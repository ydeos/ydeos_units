#!/usr/bin/env python
# coding: utf-8

r"""distance.py tests."""

from ydeos_units.units import cm, convert_imperial_str, convert_imperial


def test_distances():
    r"""Test expected values."""
    expected_value = 3.3
    atol = 1e-10
    assert expected_value - atol <= cm(mm=33.) <= expected_value + atol


def test_convert_imperial_str():
    r"""Test the conversion of an imperial measure as a string"""
    measure = "2'0''1/8''"
    assert convert_imperial_str(measure, "m") == convert_imperial(2, 1/8, "m")

    measure = "2'1''1/8''"
    assert convert_imperial_str(measure, "m") == convert_imperial(2, 1+1/8, "m")


def test_convert_imperial():
    r"""From imperial to metric"""
    measure = convert_imperial(feet=0., inches=1, to_unit="mm")
    assert measure == 25.4
