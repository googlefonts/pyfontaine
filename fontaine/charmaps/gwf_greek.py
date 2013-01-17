# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF greek'
    native_name = u''

    def glyphs(self):
        # greek subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = range(0x370, 0x400)
        return glyphs

library.register(Charmap)
