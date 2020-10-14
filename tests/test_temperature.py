#!/usr/bin/env python
# coding: utf-8

r"""temperature.py tests."""

import pytest

from ydeos_units.units import celsius, C, fahrenheit, farenheits, F, K, \
    convert_temperature


def test_temperature():
    r"""Test expected values."""
    expected_value = 0.
    atol = 1e-10
    assert expected_value - atol <= celsius(fahrenheit=32.) <= expected_value + atol
    assert expected_value - atol <= C(fahrenheit=32.) <= expected_value + atol
    assert expected_value - atol <= C(kelvin=273.15) <= expected_value + atol

    expected_value = 32.
    atol = 1e-10
    assert expected_value - atol <= fahrenheit(K=273.15) <= expected_value + atol
    assert expected_value - atol <= fahrenheit(C=0.) <= expected_value + atol
    assert expected_value - atol <= farenheits(C=0.) <= expected_value + atol
    assert expected_value - atol <= F(C=0.) <= expected_value + atol

    expected_value = 273.15
    atol = 1e-10
    assert expected_value - atol <= K(celsius=0.) <= expected_value + atol


def test_convert():
    r"""Test the convert function."""
    expected_value = 273.15
    atol = 1e-10
    assert expected_value - atol <= convert_temperature(0., "K", "celsius") <= expected_value + atol


def test_wrong_input():
    r"""Too many kwargs."""
    with pytest.raises(ValueError):
        C(farenheits=32., kelvin=0.)
    with pytest.raises(ValueError):
        K(farenheits=32., C=0.)
    with pytest.raises(ValueError):
        F(K=0., C=0.)


def test_convert_to_same_unit():
    r"""Converting to the same unit"""
    with pytest.raises(KeyError):
        C(celsius=10.)
    with pytest.raises(KeyError):
        farenheits(F=10.)
    with pytest.raises(KeyError):
        K(kelvin=10.)
