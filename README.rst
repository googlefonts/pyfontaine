===========
pyfontaine
===========

pyfontaine is a python reimplementation of [Fontaine](http://fontaine.sf.net) (by Ed Trager) which analyses fonts for language support. It has a simple character set definition format ([Polish example](https://github.com/davelab6/pyfontaine/blob/master/fontaine/charmaps/polish.py) and autodetects new definition files that appear in the [charmaps](https://github.com/davelab6/pyfontaine/tree/master/fontaine/charmaps) directory. 

It has a command line tool. Given a font, it returns the font's metadata found directly in the font (family name, style name, copyrights, etc) and then infers some useful metadata about its language support (coverage as 4-stars, as percentage, and a list of missing characters needed to get to 100%). 

It has a python module. [Example script](https://github.com/xen/fontbakery/blob/master/scripts/famchar.py) from the Font Bakery project.

pyfontaine has been made so far by @hash3g and @davelab6 and @xen, and your contributions are welcome!

Dependencies
------------

* freetype-py_
* lxml_
* simpleHilbertCurve_
* matplotlib_

Related:

* libunicodenames_

Usage
---------

To output plain text:

    pyfontaine font.ttf

To output XML:

    pyfontaine --xml font.ttf

To output JSON:

    pyfontaine --json font.ttf

To output percent coveraging in CSV:

    pyfontaine --csv font.ttf

If you want to see PNG that represent coverage implementation of font charset:

    pyfontaine --coverage font.ttf

To specify only set of charmaps:
	
	pyfontaine --set African,'Basic Latin','GWF vietnamese' font.ttf


.. _libunicodenames: https://bitbucket.org/sortsmill/libunicodenames
.. _freetype-py: http://code.google.com/p/freetype-py/
.. _lxml: http://pypi.python.org/pypi/lxml/
.. _simpleHilbertCurve: https://github.com/dentearl/simpleHilbertCurve
.. _matplotlib: https://pypi.python.org/pypi/matplotlib
