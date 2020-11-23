ydeos_units
===========

.. image:: https://travis-ci.org/ydeos/ydeos_units.svg?branch=main
    :target: https://travis-ci.org/ydeos/ydeos_units

.. image:: https://app.codacy.com/project/badge/Grade/37d381a18b8f419691c9a884e3f8f22b
    :target: https://www.codacy.com/gh/ydeos/ydeos_units/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ydeos/ydeos_units&amp;utm_campaign=Badge_Grade

.. image:: https://coveralls.io/repos/github/ydeos/ydeos_units/badge.svg?branch=main
    :target: https://coveralls.io/github/ydeos/ydeos_units?branch=main


**ydeos_units** is a physical/engineering units conversion library in Python 3.

The following types of units are handled:

- dimension / distance
- area
- force
- mass
- pressure
- speed
- torque
- volume
- geo coordinates
- temperature

The units.py_ module should be self-explanatory regarding the supported units for each type.

Install
-------

.. code-block:: shell

   git clone https://github.com/ydeos/ydeos_units
   cd ydeos_units
   python setup.py install


Examples
--------

See the examples_ folder.

Convert 12 inches to centimeters:

.. code-block:: python

   cm(inches=12.0)

Convert 10'6'' to millimeters:

.. code-block:: python

   convert_imperial(feet=10, inches=6, to_unit='mm')

Convert 10 kilograms to pounds.

.. code-block:: python

   pounds(kg=10.0)



.. _units.py: https://github.com/ydeos/ydeos_units/blob/main/ydeos_units/units.py
.. _examples: https://github.com/ydeos/ydeos_units/tree/main/examples


Contribute
----------

Not every possible unit has been implemented but adding new units is extremely simple thanks to the code generation mechanism that the library is built on.

If you wish to add new units: fork, feature branch and open a pull request. Feel free to contribute!


