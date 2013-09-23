===========
py-fontaine
===========

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

If you want to see PNG that represent coverage implementation of font charset, install simpleHilbertCurve and place script somewhere in system wide directory (e.g. /usr/local/bin/) or virtual environment bin directory:

    pyfontaine --coverage font.ttf


.. _libunicodenames: https://bitbucket.org/sortsmill/libunicodenames
.. _freetype-py: http://code.google.com/p/freetype-py/
.. _lxml: http://pypi.python.org/pypi/lxml/
.. _simpleHilbertCurve: https://github.com/dentearl/simpleHilbertCurve
.. _matplotlib: https://pypi.python.org/pypi/matplotlib
