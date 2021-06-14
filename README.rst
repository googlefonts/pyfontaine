pyfontaine
==========================================================

|Latest PyPI Version| |Python| |Travis Build Status| |License: GPL v3|

pyfontaine analyses fonts for their language and character/glyph-set support.

It has a straightforward pythonic set definition format:

- `simple example <https://github.com/googlefonts/pyfontaine/blob/master/fontaine/charsets/internals/africaan.py>`__
- `medium example <https://github.com/googlefonts/pyfontaine/blob/master/fontaine/charsets/internals/armenian.py>`__
- `complex example <https://github.com/googlefonts/pyfontaine/blob/master/fontaine/charsets/internals/polish.py>`__

Additional definitions are downloaded from the Extensis, font-config and Unicode websites during installation, and can be updated without reinstalling.

Adding your own definitions is easy.
All files in the `internals <https://github.com/googlefonts/pyfontaine/tree/master/fontaine/charsets/internals>`__ directory are auto-detected, so just add definition files there.

Installation
------------

macOS:

First, install Python and the `pip <http://www.pip-installer.org>`__ python package manager. This is installed by default with `homebrew <http://brew.sh/>`__ python, so, install homebrew, then install the neccessary depedencies (`PyICU <https://pypi.org/project/PyICU/>`__) as follows::

    brew install python icu4c pkg-config;
    export PATH="/usr/local/opt/icu4c/bin:/usr/local/opt/icu4c/sbin:$PATH";
    export PKG_CONFIG_PATH="$PKG_CONFIG_PATH:/usr/local/opt/icu4c/lib/pkgconfig";
    export CC="$(which gcc)" CXX="$(which g++)";
    pip3 install --no-binary=:pyicu: pyicu;

Debian:

    apt-get install libicu-dev

Install the latest release easily with pip::

    pip3 install fontaine --user;

To install the latest development version::

    pip3 install git+https://github.com/googlefonts/pyfontaine.git#egg=fontaine --user;


Usage
-----

Given a list of space separated font filenames, it returns a report with some general metadata and a language support analysis::

    pyfontaine font.ttf;

Given a list of space separated unicode characters, or unicode values, it returns a list of character sets that include that character::

    pyfontaine 0x0061;
    pyfontaine ğ ø ∂;

Similarly you can find out if a font supports specific characters by also giving the filename::

    pyfontaine U+C480 U+C481 font.ttf;

To output font reports in various formats::

    pyfontaine --xml font.ttf;
    pyfontaine --json font.ttf;
    pyfontaine --csv font.ttf;
    pyfontaine --wiki font.ttf;

The `--wiki` format produces a MediaWiki table
(`example <https://en.wikipedia.org/wiki/DejaVu_fonts#Unicode_coverage>`__)

To only show character sets from different collections::

    pyfontaine --collections all font.ttf; # default
    pyfontaine --collections pyfontaine font.ttf;
    pyfontaine --collections uniblocks font.ttf;
    pyfontaine --collections extensis font.ttf;
    pyfontaine --collections fontconfig font.ttf;
    pyfontaine --collections cldr font.ttf;
    pyfontaine --collections subsets font.ttf;

To only show specific character sets::

    pyfontaine --set africaan,adobe_latin_3 font.ttf;

To print a list of all the missing unicode values from each set::

    pyfontaine --missing --set adobe_latin_3 font.ttf;

 To output visualisations of the coverage using `Hilbert curves <http://en.wikipedia.org/wiki/Hilbert_curve>`__ (thanks for the idea, `Øyvind 'pippin' Kolås <http://github.com/hodefoting>`__!):

    pyfontaine --show_hilbert font.ttf; ls -l coverage_pngs/;

 The PNG files are stored in a new directory, ``coverage_pngs``, under the current directory.

Update collection data
~~~~~~~~~~~~~~~~~~~~~~

You can update remote collections data when you are online::

    pyfontaine --update-data 1;

Python Module
~~~~~~~~~~~~~

It has a python module called ``fontaine``

Making a release on PyPI
~~~~~~~~~~~~~~~~~~~~~~~~

To release a new version on PyPI, create and push a new git tag with a version number following the [semver](https://www.semver.org) versioning scheme.

Then set up a ``~/.pypirc`` file::

    [distutils]
    index-servers=pypi
    
    [pypi]
    repository = https://pypi.python.org/pypi
		
		[server-login]
    username = user
    password = password

Then run::

    python setup.py build;
    python setup.py sdist upload;

Contributing
------------

Your contributions under `the GPLv3 <LICENSE.txt>`__ are welcome!

pyfontaine is a python reimplementation of
`Fontaine <http://fontaine.sf.net>`__ by Ed Trager, and has been made by
`Vitaly Volkov <http://github.com/hash3g>`__,
`Dave Crossland <http://github.com/davelab6>`__,
`Mikhail Kashkin <http://github.com/xen>`__ and
`Felipe Sanches <http://github.com/felipesanches>`__.

Thanks
------

We would like to thank some upstream projects that make pyfontaine even
more useful:

* `Thomas Phinney <http://www.thomasphinney.com/>`__ for the `WebINK Character
  Sets <http://web.archive.org/web/20150222004543/http://blog.webink.com/custom-font-subsetting-for-faster-websites/>`__

* `Behdad Esfabod <http://behdad.org>`__ for the `font-config languages
  definitions <http://cgit.freedesktop.org/fontconfig/tree/fc-lang>`__

* Unicode Consortium for the `Unicode Blocks
  <http://www.unicode.org/Public/UNIDATA/Blocks.txt>`__

Dependencies
------------

- Mac OS X requires the XCode Command Line Tools to be installed
- `fonttools <https://github.com/behdad/fonttools>`__ (common) *or*
  `freetype-py <http://code.google.com/p/freetype-py>`__ (fast)
- `lxml <http://pypi.python.org/pypi/lxml>`__
- `PyICU <http://pyicu.osafoundation.org/>`__
- `simpleHilbertCurve <https://github.com/dentearl/simpleHilbertCurve>`__
- `matplotlib <https://pypi.python.org/pypi/matplotlib>`__
- `tabulate <https://pypi.python.org/pypi/tabulate>`__
- `requests <https://pypi.python.org/pypi/requests>`__

Related Projects
----------------

-  `fontaine <http://fontaine.sf.net>`__
-  `fontbakery <https://github.com/googlefonts/fontbakery>`__
-  `libunicodenames <https://bitbucket.org/sortsmill/libunicodenames>`__


.. |Latest PyPI Version| image:: https://img.shields.io/pypi/v/fontaine.svg?style=flat
   :target: https://pypi.python.org/pypi/fontaine
.. |Python| image:: https://img.shields.io/pypi/pyversions/fontaine.svg?style=flat
   :target: https://pypi.python.org/pypi/fontaine
.. |Travis Build Status| image:: https://travis-ci.org/googlefonts/pyfontaine.svg
   :target: https://travis-ci.org/googlefonts/pyfontaine
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
