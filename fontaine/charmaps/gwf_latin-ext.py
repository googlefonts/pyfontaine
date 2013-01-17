# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF latin-ext'
    native_name = u''

    def glyphs(self):
        # latin-ext subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = (range(0x100, 0x370) +
                   range(0x1d00, 0x1ea0) +
                   range(0x1ef2, 0x1f00) +
                   range(0x2070, 0x20d0) +
                   range(0x2c60, 0x2c80) +
                   range(0xa700, 0xa800))
        return glyphs

library.register(Charmap)
