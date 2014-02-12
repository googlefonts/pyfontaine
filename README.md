===========
pyfontaine
===========

pyfontaine analyses fonts for their language and character set support. 





It has a simple character set definition format ([Polish example](https://github.com/davelab6/pyfontaine/blob/master/fontaine/charmaps/polish.py) and autodetects new definition files that appear in the [charmaps](https://github.com/davelab6/pyfontaine/tree/master/fontaine/charmaps) directory.

Usage
-----

It has a command line tool. 

Given a font, it returns a report with some general metadata and th language support analysis. 

```sh
pyfontaine font.ttf;
```

Given a unicode character value, it returns a list of character sets that include that character.

```sh
pyfontaine 0x0061;
```

To output font reports in various formats:

```sh
pyfontaine --xml font.ttf;
pyfontaine --json font.ttf;
pyfontaine --csv font.ttf;
pyfontaine --wiki font.ttf; # MediaWiki Table:
```

To only show character sets from different collections:

```sh
pyfontaine --collections all font.ttf; # default
pyfontaine --collections pyfontaine font.ttf;
pyfontaine --collections uniblocks font.ttf;
pyfontaine --collections extensis font.ttf;
pyfontaine --collections fontconfig font.ttf;
```

To only show specific character sets:

```sh
pyfontaine --set African,'Basic Latin','GWF vietnamese' font.ttf;
```

To print a list of all the missing unicode values from each set:

```sh
pyfontaine --missing font.ttf;
```

To output visualisations of the coverage using [Hilbert curves](http://en.wikipedia.org/wiki/Hilbert_curve) (thanks for the idea, @hodefoting!):

```sh
pyfontaine --coverage font.ttf;
ls -l coverage_pngs/;
```

(The PNG files are stored in a new directory, `coverage_pngs` in the current directory.)

Python Module
--------------

It has a python module. Here is an [example script](https://github.com/xen/fontbakery/blob/master/scripts/famchar.py) from the Font Bakery project by @xen.

Contributing
----------------

pyfontaine is a python reimplementation of [Fontaine](http://fontaine.sf.net) by Ed Trager, and has been made by by @hash3g, @davelab6 and @xen. Your contributions under the GPLv3 or compatible licenses such as Apache v2 are welcome!

Dependencies
------------

* fontTools_ _or_ * freetype-py_
* lxml_
* simpleHilbertCurve_
* matplotlib_

Related Projects
------------

* fontaine_
* fontbakery_
* libunicodenames_

.. _fontTools: https://github.com/behdad/fonttools
.. _fontaine: http://fontaine.sf.net
.. _fontbakery: https://github.com/xen/fontbakery
.. _libunicodenames: https://bitbucket.org/sortsmill/libunicodenames
.. _freetype-py: http://code.google.com/p/freetype-py
.. _lxml: http://pypi.python.org/pypi/lxml
.. _simpleHilbertCurve: https://github.com/dentearl/simpleHilbertCurve
.. _matplotlib: https://pypi.python.org/pypi/matplotlib
