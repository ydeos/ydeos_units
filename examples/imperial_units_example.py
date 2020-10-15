#!/usr/bin/env python
# coding: utf-8

r"""Imperial conversions."""

from ydeos_units.units import convert_imperial, convert_imperial_str


def print_convert_imperial(feet, to_unit, inches=0):
    print(f"{feet}'{inches}'' is {convert_imperial(feet=feet, inches=inches, to_unit='mm')} {to_unit}")


def print_convert_imperial_str(value, to_unit):
    v_mm = convert_imperial_str(value=value, to_unit=to_unit)
    print(f"{value} is {v_mm} mm")


if __name__ == "__main__":
    print_convert_imperial(feet=1., inches=2.5, to_unit='mm')
    print_convert_imperial_str(value="1'2''1/2", to_unit='mm')

    print_convert_imperial(feet=1., inches=2, to_unit="mm")
    print_convert_imperial_str(value="1'2''", to_unit="mm")

    print_convert_imperial(feet=1., inches=2.625, to_unit="mm")
    print_convert_imperial_str(value="1'2''5/8", to_unit="mm")

    print_convert_imperial(feet=0., inches=1., to_unit="mm")
    print_convert_imperial_str(value="1''", to_unit="mm")

    print_convert_imperial(feet=0., inches=1.5, to_unit="mm")
    print_convert_imperial_str(value="1''1/2", to_unit="mm")

    print_convert_imperial(feet=8., to_unit="mm")
    print_convert_imperial_str(value="8'", to_unit="mm")

    print_convert_imperial(feet=8.5, to_unit="mm")
    print_convert_imperial_str(value="8.5'", to_unit="mm")
