# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Chess Symbols'
    native_name = u'Chess Symbols'
    key = 0x2659
    glyphs = xrange(0x2654, 0x265F)


library.register(Charmap)
