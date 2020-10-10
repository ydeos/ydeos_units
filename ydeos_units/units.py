# coding: utf-8

r"""Units conversions system"""

from typing import Union, Tuple
from fractions import Fraction

code = """def %s(**kwargs):
    if len(kwargs.items()) != 1:
        raise ValueError("Too many keywords")
    try:
        # wrapping in list of keys and values if for Python 3 compatibility
        result = list(kwargs.values())[0] * %s[list(kwargs.keys())[0]] / %s['%s']
    except KeyError:
        raise KeyError("Unknown input unit")
    return result
"""


def create_code(dict_name: str, key_name: str) -> str:
    r"""Create the code to be compiled on the fly by the conversion modules

    dict_name : The name of the dictionary that defines the units in the conversion module
    key_name : The key name in the dictionary that defines the units in the conversion module

    Returns the Python code as a string

    """
    return code % (key_name, dict_name, dict_name, key_name)


areas = {"m2": 1., "square_meter": 1., "square_meters": 1.,
         "cm2": 1e-4, "square_centimeter": 1e-4, "square_centimeters": 1e-4,
         "mm2": 1e-6, "square_millimeter": 1e-6, "square_millimeters": 1e-6}

for k in areas.keys():
    exec(create_code("areas", k), globals())


distances = {"mm": 1e-3, "millimeter": 1e-3, "millimeters": 1e-3, "millimetre": 1e-3, "millimetres": 1e-3,
             "cm": 1e-2, "centimeter": 1e-2, "centimeters": 1e-2, "centimetre": 1e-2, "centimetres": 1e-2,
             "m": 1., "meter": 1., "meters": 1., "metre": 1., "metres": 1.,
             "km": 1000., "kilometer": 1000., "kilometers": 1000., "kilometre": 1000., "kilometres": 1000.,
             # "in": 0.0254,  # in is a reserved keyword in Python
             "inch": 0.0254, "inches": 0.0254,
             "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
             "yd": 0.9144, "yard": 0.9144, "yards": 0.9144,
             "mi": 1609.344, "mile": 1609.344, "miles": 1609.344,
             "ftm": 1.8288, "fathom": 1.8288, "fathoms": 1.8288,
             "nm": 1852., "nautical_mile": 1852., "nautical_miles": 1852.}

for k in distances.keys():
    # code = fs_units.base.create_code("distances", k)
    # exec code in module.__dict__
    # g = globals()
    exec(create_code("distances", k), globals())


forces = {"N": 1., "newton": 1., "newtons": 1.,
          "kgf": 9.81, "kilogram_force": 9.81, "kilograms_force": 9.81}

for k in forces.keys():
    exec(create_code("forces", k), globals())


masses = {"kg": 1., "kilogram": 1., "kilograms": 1.,
          "g": 1e-3, "gram": 1e-3, "grams": 1e-3,
          "t": 1000., "ton": 1000., "tons": 1000.,
          "oz": 28.349523125 * 1e-3, "ounce": 28.349523125 * 1e-3, "ounces": 28.349523125 * 1e-3,
          "lb": 0.45359237, "pound": 0.45359237, "pounds": 0.45359237,
          "st": 6.35029318, "stone": 6.35029318, "stones": 6.35029318}

for k in masses.keys():
    exec(create_code("masses", k), globals())


pressures = {"Pa": 1., "pascal": 1., "pascals": 1.,
             "hPa": 100., "hectopascal": 100., "hectopascals": 100.,
             "bar": 1e5, "bars": 1e5,
             "millibar": 100., "millibars": 100.,
             "mmHg": 133.322387415, "millimeter_of_mercury": 133.322387415, "millimeters_of_mercury": 133.322387415}

for k in pressures.keys():
    exec(create_code("pressures", k), globals())


speeds = {"ms": 1., "mps": 1., "meter_per_second": 1., "meters_per_second": 1.,
          "kmh": 1000./3600., "kilometer_per_hour": 1000./3600., "kilometers_per_hour": 1000./3600.,
          "kt": 1852./3600., "knt": 1852./3600., "knts": 1852./3600., "knot": 1852./3600., "knots": 1852./3600.}

for k in speeds.keys():
    exec(create_code("speeds", k), globals())


torques = {"Nm": 1., "newton_metre": 1., "newton_metres": 1., "newton_meter": 1., "newton_meters": 1.}

for k in torques.keys():
    exec(create_code("torques", k), globals())


volumes = {"m3": 1., "cubic_meter": 1., "cubic_meters": 1.,
           "l": 0.001, "litre": 0.001, "liter": 0.001, "litres": 0.001, "liters": 0.001,
           "cm3": 1e-6, "centimeter_cube": 1e-6, "centimeters_cube": 1e-6,
           "ml": 1e-6, "millilitre": 1e-6, "millilitres": 1e-6, "milliliter": 1e-6, "milliliters": 1e-6,
           "mm3": 1e-9, "millimeter_cube": 1e-9, "millimeters_cube": 1e-9,
           "pt": 568.26125 * 1e-6, "pint": 568.26125 * 1e-6, "pints": 568.26125 * 1e-6,
           "qt": 1136.5225 * 1e-6, "quart": 1136.5225 * 1e-6, "quarts": 1136.5225 * 1e-6,
           "gal": 4546.09 * 1e-6, "gallon": 4546.09 * 1e-6, "gallons": 4546.09 * 1e-6}

for k in volumes.keys():
    exec(create_code("volumes", k), globals())


def convert(value: Union[int, float], to_unit: str, from_unit: str) -> float:
    r"""Convenience function for cases where the to_unit and the from_unit are in string form

    to_unit : The desired unit
    from_unit : The input unit

    """
    return globals()[to_unit](**{from_unit: value})


# Conversion between geo coordinates


def decimal_degrees(degrees: Union[int, float] = 0,
                    minutes: Union[int, float] = 0,
                    seconds: Union[int, float] = 0) -> float:
    r"""Convert degrees and decimal minutes or degrees minutes seconds to decimal degrees

    Returns decimal degrees

    Notes
    -----
    The intentional use of this function is to have all parameters with the same sign
    >>> decimal_degrees(20, 30, 45)
    However it can be use to substract 20 seconds to 30 degrees in the following way:
    >>> decimal_degrees(degrees=30, seconds=-20.)

    """
    if minutes >= 60 or seconds >= 60:
        raise ValueError("Minutes and seconds should be lesser than 60")
    if degrees > 180 or degrees < -180:
        raise ValueError("Degrees must lie in the -180 to 180 range")
    return degrees + minutes / 60. + seconds / 3600.


def degrees_minutes_seconds(decimal_degree: float = 0.) -> Tuple[int, int, float, float]:
    r"""Convert decimal degrees to degrees and decimal minutes and degrees minutes seconds

    Returns a tuple (int, int, float, float): degrees, minutes, decimal_minutes (e.g. 30.99), seconds

    """
    if decimal_degree > 180 or decimal_degree < -180:
        raise ValueError("Degrees must lie in the -180 to 180 range")

    sign = decimal_degree / abs(decimal_degree) if decimal_degree != 0. else 1

    decimal_degree = abs(decimal_degree)
    degree = decimal_degree // 1  # Truncate degree to be an integer
    # Calculate the decimal minutes
    decimal_minute = (decimal_degree - degree) * 60.
    minute = decimal_minute // 1  # Truncate minute to be an integer
    second = (decimal_minute - minute) * 60.  # Calculate the decimal seconds
    # Finally, re-impose the appropriate sign
    degree *= sign
    minute *= sign
    decimal_minute *= sign
    second *= sign
    return int(degree), int(minute), decimal_minute, second


# Parse and convert imperial distance units


def convert_imperial_str(value: str, to_unit: str):
    r"""Convert a distance expressed in the imperial system (feet, inches, fraction of an inch) into the specified unit

    value : String representation of the imperial distance
    to_unit : The desired (metric based) unit

    """
    if "''" in value:
        split_on_inches = value.strip().split("''")
        split_on_inches = list(filter(lambda x: x != '', split_on_inches))
        # print("split_on_inches : %s" % str(split_on_inches))
        # print("split_on_inches[0].split(''') : %s" % str(split_on_inches[0].split("'")))
        if len(split_on_inches[0].split("'")) == 2:
            feet = float(split_on_inches[0].split("'")[0])
        elif len(split_on_inches[0].split("'")) == 1:
            feet = 0.
        else:
            raise ValueError

        # print("feet : %f" % feet)
        if "'" in split_on_inches[0]:
            inches_int = int(split_on_inches[0].split("'")[1])
        else:
            inches_int = int(split_on_inches[0])
        # print("inches_int : %s" % str(inches_int))
        if len(split_on_inches) == 2 and split_on_inches[1] != "":
            inches_frac = float(Fraction(split_on_inches[1]))
        else:
            inches_frac = 0.
        # print("inches_frac : %s" % str(inches_frac))
        inches_float = inches_int + inches_frac
    else:
        feet = float(value[0:-1])
        inches_float = 0.

    return convert_imperial(feet=feet, inches=inches_float, to_unit=to_unit)


def convert_imperial(feet: float = 0., inches: float = 0., to_unit: str = "mm") -> float:
    r"""Convert a distance expressed in the imperial system
    (feet, inches, fraction of an inch) into the specified unit

    to_unit : The desired (metric based) unit

    """
    return convert(feet, from_unit="feet", to_unit=to_unit) + convert(inches, from_unit="inches", to_unit=to_unit)


# Temperature conversions


def farenheit(**kwargs):
    r"""Conversion to farenheit degrees"""
    if len(kwargs.items()) != 1:
        raise ValueError("Too many keywords")

    if list(kwargs.keys())[0] in ["celsius", "C"]:
        return (list(kwargs.values())[0] * 9./5) + 32.
    elif list(kwargs.keys())[0] in ["kelvin", "kelvins", "K"]:
        return (list(kwargs.values())[0] - 273.15) * 9./5 + 32
    else:
        raise KeyError("Unknown input unit")


def F(**kwargs):
    r"""Conversion to farenheit degrees"""
    return farenheit(**kwargs)


def farenheits(**kwargs):
    r"""Conversion to farenheit degrees"""
    return farenheit(**kwargs)


def celsius(**kwargs):
    r"""Conversion to celsius degrees"""
    if len(kwargs.items()) != 1:
        raise ValueError("Too many keywords")

    if list(kwargs.keys())[0] in ["farenheit", "F"]:
        return (list(kwargs.values())[0] - 32.) * 5./9
    elif list(kwargs.keys())[0] in ["kelvin", "kelvins", "K"]:
        return list(kwargs.values())[0] - 273.15
    else:
        raise KeyError("Unknown input unit")


def C(**kwargs):
    r"""Conversion to celsius degrees"""
    return celsius(**kwargs)


def kelvin(**kwargs):
    r"""Conversion to kelvin degrees"""
    if len(kwargs.items()) != 1:
            raise ValueError("Too many keywords")

    if list(kwargs.keys())[0] in ["farenheit", "F"]:
        return (list(kwargs.values())[0] - 32.) * 5./9 + 273.15
    elif list(kwargs.keys())[0] in ["celsius", "C"]:
        return list(kwargs.values())[0] + 273.15
    else:
        raise KeyError("Unknown input unit")


def K(**kwargs):
    r"""Conversion to Kelvin degrees"""
    return kelvin(**kwargs)


def kelvins(**kwargs):
    r"""Conversion to kelvin degrees"""
    return kelvin(**kwargs)


def convert_temperature(value: float, to_unit: str, from_unit: str) -> float:
    r"""Convenience function for cases where the to_unit and the from_unit are in string form

    to_unit : The desired unit
    from_unit : The input unit

    """
    return globals()[to_unit](**{from_unit: value})
