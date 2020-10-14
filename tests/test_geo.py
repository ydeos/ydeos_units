#!/usr/bin/env python
# coding: utf-8

r"""Tests for the geo.py module."""

import pytest

from ydeos_units.units import degrees_minutes_seconds, decimal_degrees


def test_decimal_degrees_wrong_input():
    r"""Asking for impossible things."""
    with pytest.raises(ValueError):
        decimal_degrees(0, 60, 0)
    with pytest.raises(ValueError):
        decimal_degrees(0, 0, 60)
    with pytest.raises(ValueError):
        decimal_degrees(-180.1, 0, 0)
    with pytest.raises(ValueError):
        decimal_degrees(180.1, 0, 0)


def test_degrees_minutes_seconds_wrong_input():
    r"""Asking for impossible things."""
    with pytest.raises(ValueError):
        degrees_minutes_seconds(-180.1)
    with pytest.raises(ValueError):
        degrees_minutes_seconds(180.1)


def test_decimaldegrees_to_ddmmss():
    r"""Test conversion from decimal degrees to degrees, minutes, seconds."""
    assert degrees_minutes_seconds(decimal_degree=0.) == (0, 0, 0., 0.)
    assert degrees_minutes_seconds(decimal_degree=-0.) == (0, 0, 0., 0.)

    assert degrees_minutes_seconds(decimal_degree=45.) == (45, 0, 0., 0.)
    assert degrees_minutes_seconds(decimal_degree=-45.) == (-45, 0, 0., 0.)

    assert degrees_minutes_seconds(decimal_degree=45.5) == (45, 30, 30., 0.)
    assert degrees_minutes_seconds(decimal_degree=-45.5) == (-45, -30, -30., 0.)

    assert degrees_minutes_seconds(decimal_degree=45.51) == (45,
                                                             30,
                                                             30.59999999999988,
                                                             35.99999999999284)
    assert degrees_minutes_seconds(decimal_degree=-45.51) == (-45,
                                                              -30,
                                                              -30.59999999999988,
                                                              -35.99999999999284)


def test_ddmm_to_decimaldegrees():
    r"""Test conversion from degrees and decimal minutes to decimal degrees."""
    assert decimal_degrees(degrees=0, minutes=0.) == 0.

    assert decimal_degrees(degrees=45, minutes=30.59999999999988) == 45.51
    assert decimal_degrees(degrees=-45, minutes=-30.59999999999988) == -45.51


def test_ddmmss_to_decimaldegrees():
    r"""Test conversion from degrees minutes seconds to decimal degrees."""
    assert decimal_degrees(degrees=0, minutes=0., seconds=0.) == 0.

    error = 1e-6
    assert .01 - error <= decimal_degrees(degrees=0, minutes=0., seconds=35.99999999999284) <= .01 + error

    assert decimal_degrees(degrees=45, minutes=30., seconds=35.99999999999284) == 45.51
    assert decimal_degrees(degrees=-45, minutes=-30., seconds=-35.99999999999284) == -45.51


def test_degrees_decimalminutes_to_ddmmss():
    r"""Test combining functions to convert 45°30.5' to 45° 30' 30'' ."""
    # convert to decimal degrees
    dd = decimal_degrees(degrees=45, minutes=30.5)
    # convert decimal degrees to dd mm ss
    d, m, dm, s = degrees_minutes_seconds(decimal_degree=dd)
    error = 1e-6
    assert d == 45
    assert m == 30
    assert 30.5 - error <= dm <= 30.5 + error
    assert 30 - error <= s <= 30. + error
