#!/usr/bin/python
# coding: utf-8

r"""Example distance conversion."""

from ydeos_units.units import cm, inches

# convert 12.0 inches to centimeters
print(f"12 inches is {cm(inches=12.0):.6f} centimetres")

# convert 55 cm to inches
print(f"55 centimetres is {inches(cm=55):.6f} inches")
