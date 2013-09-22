===========
py-fontaine
===========

Dependencies
------------

* freetype-py_
* lxml_

Related:

* libunicodenames_

Usage
---------

To output plain text:

    python fontaine/main.py font.ttf

To output XML:

    python fontaine/main.py --xml font.ttf

To output JSON:

    python fontaine/main.py --json font.ttf

To output percent coveraging in CSV:

    python fontaine/main.py --csv font.ttf

If you want to see PNG that represent coverage implementation of font charset:

    python fontaine/main.py --coverage font.ttf


.. _libunicodenames: https://bitbucket.org/sortsmill/libunicodenames
.. _freetype-py: http://code.google.com/p/freetype-py/
.. _lxml: http://pypi.python.org/pypi/lxml/
.. _simpleHilbertCurve: https://github.com/dentearl/simpleHilbertCurve
