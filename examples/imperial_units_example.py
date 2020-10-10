#!/usr/bin/env python
# coding: utf-8

r"""Imperial conversions"""

from ydeos_units.units import convert_imperial, convert_imperial_str

if __name__ == "__main__":
    print(convert_imperial(feet=1., inches=2.5, to_unit="mm"))
    print(convert_imperial_str(value="1'2''1/2", to_unit="mm"))

    print(convert_imperial(feet=1., inches=2, to_unit="mm"))
    print(convert_imperial_str(value="1'2''", to_unit="mm"))

    print(convert_imperial(feet=1., inches=2.625, to_unit="mm"))
    print(convert_imperial_str(value="1'2''5/8", to_unit="mm"))

    print(convert_imperial(feet=0., inches=1., to_unit="mm"))
    print(convert_imperial_str(value="1''", to_unit="mm"))

    print(convert_imperial(feet=0., inches=1.5, to_unit="mm"))
    print(convert_imperial_str(value="1''1/2", to_unit="mm"))

    print(convert_imperial(feet=8., to_unit="mm"))
    print(convert_imperial_str(value="8'", to_unit="mm"))

    print(convert_imperial(feet=8.5, to_unit="mm"))
    print(convert_imperial_str(value="8.5'", to_unit="mm"))
