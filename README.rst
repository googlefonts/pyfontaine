pyfontaine
==========================================================

|Build Status| |Health| |Coverage Status|

pyfontaine analyses fonts for their language and character/glyph-set support.

It has a straightforward pythonic set definition format:

- `simple example <https://github.com/davelab6/pyfontaine/blob/master/fontaine/charsets/internals/africaan.py>`__
- `medium example <https://github.com/davelab6/pyfontaine/blob/master/fontaine/charsets/internals/armenian.py>`__
- `complex example <https://github.com/davelab6/pyfontaine/blob/master/fontaine/charsets/internals/polish.py>`__

Additional definitions are downloaded from the Extensis, font-config and Unicode websites during installation, and can be updated without reinstalling. 

Adding your own definitions is easy. 
All files in the `internals <https://github.com/davelab6/pyfontaine/tree/master/fontaine/charsets/internals>`__ directory are auto-detected, so just add definition files there.

Installation
------------

First, install Python and the `pip <http://www.pip-installer.org>`__ python package manager. This is installed by default with `homebrew <http://brew.sh/>`__, so, try to run pip and if it isn't available then install homebrew, or install pip directly as follows::

    curl -O https://bootstrap.pypa.io/get-pip.py;
    sudo python get-pip.py;
    rm get-pip.py;

On Mac OS X, install the pyicu dependency as follows::

    CFLAGS=-I/usr/local/opt/icu4c/include LDFLAGS=-L/usr/local/opt/icu4c/lib pip install pyicu;

Install the latest release easily with pip::

    sudo pip install fontaine

To install the latest development version::

    sudo pip install https://github.com/davelab6/pyfontaine/archive/master.zip;

Usage
-----

Given a list of space separated font filenames, it returns a report with some general metadata and a language support analysis::

    pyfontaine font.ttf;

Given a list of space separated unicode characters, or unicode values, it returns a list of character sets that include that character::

    pyfontaine 0x0061;
    pyfontaine ğ ø ∂;

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

.. To output visualisations of the coverage using `Hilbert curves <http://en.wikipedia.org/wiki/Hilbert_curve>`__ (thanks for the idea, `Øyvind 'pippin' Kolås <http://github.com/hodefoting>`__!): 
.. 
..    pyfontaine --coverage font.ttf; ls -l coverage_pngs/;
..
.. The PNG files are stored in a new directory, ``coverage_pngs``, under the current directory.

Update collection data
~~~~~~~~~~~~~~~~~~~~~~

You can update remote collections data when you are online:

    pyfontaine --update-data 1;

Python Module
~~~~~~~~~~~~~

It has a python module, ``fontaine``

Contributing
------------

Your contributions under `the GPLv3 <LICENSE.txt>`__ are welcome!

pyfontaine is a python reimplementation of
`Fontaine <http://fontaine.sf.net>`__ by Ed Trager, and has been made by
by `Vitaly Volkov <http://github.com/hash3g>`__, `Dave
Crossland <http://github.com/davelab6>`__ and `Mikhail
Kashkin <http://github.com/xen>`__.

Thanks
------

We would like to thank some upstream projects that make pyfontaine even
more useful: 

* `Thomas Phinney <http://www.thomasphinney.com/>`__ for the `WebINK Character
  Sets <http://blog.webink.com/custom-font-subsetting-for-faster-websites/>`__

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

Related Projects
----------------

-  `fontaine <http://fontaine.sf.net>`__
-  `fontbakery <https://github.com/xen/fontbakery>`__
-  `libunicodenames <https://bitbucket.org/sortsmill/libunicodenames>`__

.. |Build Status| image:: https://travis-ci.org/davelab6/pyfontaine.svg
   :target: https://travis-ci.org/davelab6/pyfontaine
.. |Health| image:: https://landscape.io/github/davelab6/pyfontaine/master/landscape.svg?style=flat
   :target: https://landscape.io/github/davelab6/pyfontaine/master
.. |Coverage Status| image:: https://img.shields.io/coveralls/davelab6/pyfontaine.svg
   :target: https://coveralls.io/r/davelab6/pyfontaine
