#!/usr/bin/env python
#
# fontaine.py
#
# Copyright (c) 2019, the pyfontaine authors:
#
# - Dave Crossland <dave@understandinglimited.com>
# - Felipe Sanches <juca@members.fsf.org>
# - Vitaly Volkov <hash.3g@gmail.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

from setuptools import setup

with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="fontaine",
    use_scm_version={"write_to": "fontaine/_version.py"},
    description="Font analysis tool for determining character/glyph support",
    license="GNU GPLv3",
    long_description=readme,
    author="Dave Crossland, Felipe Sanches, Vitaly Volkov",
    author_email="dave@lab6.com",
    url="https://github.com/googlefonts/pyfontaine",
    packages=[
        "fontaine",
        "fontaine.charsets",
        "fontaine.charsets.internals",
        "fontaine.structures",
        "fontaine.ext",
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6",
    setup_requires=["setuptools_scm"],
    install_requires=["fonttools", "lxml", "PyICU", "requests", "tabulate"],
    package_data={
        "fontaine": [
            "charsets/names.db/*.*",
            "charsets/fontconfig/fc-lang/*.orth",
            "charsets/subsets/*.txt",
            "charsets/internals/google_glyphsets/GF-latin*.nam",
            "charsets/internals/google_glyphsets/Cyrillic/*.nam",
            "charsets/internals/google_glyphsets/Greek/*.nam",
            "ext/data/*.*",
            "glyphlists/*.txt",
        ]
    },
    scripts=["bin/simpleHilbertCurve", "bin/pyfontaine"],
)
