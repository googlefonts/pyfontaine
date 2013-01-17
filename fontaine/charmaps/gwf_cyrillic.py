# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF cyrillic'
    native_name = u''

    def glyphs(self):
        # cyrillic subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = range(0x400, 0x460) + [0x490, 0x491, 0x4b0, 0x4b1]
        return glyphs

library.register(Charmap)
