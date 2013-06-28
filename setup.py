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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import Extension, setup
from setuptools.command.test import test as TestCommand

with open("README.rst", 'r') as readme_file:
    readme = readme_file.read()

with open("LICENSE.txt", 'r') as license_file:
    license = license_file.read()

setup(name='fontaine',
    version='1.0.3',
    description='Fontaine font tool',
    license=license,
    long_description=readme,
    author='Dave Crossland, Виталий Волков',
    author_email='dave@lab6.com',
    url='https://github.com/davelab6/pyfontaine',
    # more examples here http://docs.python.org/distutils/examples.html#pure-python-distribution-by-package
    packages=['fontaine', 'fontaine.charmaps', 'fontaine.structures',],
    install_requires=[
      'freetype',
      'lxml'
    ],
    package_data = {
        'fontaine': [
            'charmaps/names.db/*.*',
        ]
    }
)