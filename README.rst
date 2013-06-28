===========
py-fontaine
===========

Dependencies
------------

* [freetype-py](http://code.google.com/p/freetype-py/)
* [lxml](http://pypi.python.org/pypi/lxml/)
* [libunicodenames](https://bitbucket.org/sortsmill/libunicodenames)

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
