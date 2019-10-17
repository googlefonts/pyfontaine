#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# fontaine.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

from setuptools import setup
from io import open

with open("README.rst", 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(name='fontaine',
      use_scm_version={"write_to": "fontaine/_version.py"},
      description='Font analysis tool for determining character/glyph support',
      license="GNU GPLv3",
      long_description=readme,
      author='Dave Crossland, Виталий Волков, Felipe Sanches',
      author_email='dave@lab6.com',
      url='https://github.com/googlefonts/pyfontaine',
      # more examples here http://docs.python.org/distutils/examples.html#pure-python-distribution-by-package
      packages=['fontaine', 'fontaine.charsets', 'fontaine.charsets.internals', 'fontaine.structures', 'fontaine.ext'],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3 :: Only',
      ],
      python_requires='>=3.6',
      setup_requires=['setuptools_scm'],
      install_requires=[
          'fonttools',
          'lxml',
          'PyICU',
          'requests',
          'tabulate'
      ],
      package_data={
          'fontaine': [
              'charsets/names.db/*.*',
              'charsets/fontconfig/fc-lang/*.orth',
              'charsets/subsets/*.txt',
              'charsets/internals/google_glyphsets/GF-latin*.nam',
              'charsets/internals/google_glyphsets/Cyrillic/*.nam',
              'charsets/internals/google_glyphsets/Greek/*.nam',
              'ext/data/*.*',
              'glyphlists/*.txt'
          ]
      },
      scripts=['bin/simpleHilbertCurve',
               'bin/pyfontaine'])
