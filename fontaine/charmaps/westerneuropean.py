# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Western European'
    native_name = u'Western European'

    def glyphs(self):
        glyphs  = range(0x00C0, 0x00CF)
        glyphs += range(0x00D0, 0x00D6)
        glyphs += range(0x00D8, 0x00DF)
        glyphs += range(0x00E0, 0x00EF)
        glyphs += range(0x00F0, 0x00F6)
        glyphs += range(0x00F8, 0x00FF)
        return glyphs


library.register(Charmap)
