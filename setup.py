#!/usr/bin/env python
# coding: utf-8

r"""ydeos_units setup.py."""

from distutils.core import setup

import ydeos_units


setup(name=ydeos_units.__project_name__,
      version=ydeos_units.__version__,
      description=ydeos_units.__description__,
      long_description='Units conversions for area, distance, force, '
                       'geo coordinates, mass, pressure, speed, temperature, '
                       'torque and volume',
      url=ydeos_units.__url__,
      download_url=ydeos_units.__download_url__,
      author=ydeos_units.__author__,
      author_email=ydeos_units.__author_email__,
      license=ydeos_units.__license__,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.7'],
      keywords='units conversion',
      packages=['ydeos_units'])
