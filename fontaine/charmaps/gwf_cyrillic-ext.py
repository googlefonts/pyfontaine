# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF cyrillic-ext'
    native_name = u''

    def glyphs(self):
        # cyrillic-ext subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = (range(0x400, 0x530) +
                   [0x20b4] +
                   range(0x2de0, 0x2e00) +
                   range(0xa640, 0xa6a0))
        return glyphs

library.register(Charmap)
