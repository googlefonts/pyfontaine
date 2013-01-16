# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Western European'
    native_name = u'Western European'
    key = 0x00C0
    glyphs = \
        list(xrange(0x00C0, 0x00CF)) + \
        list(xrange(0x00D0, 0x00D6)) + \
        list(xrange(0x00D8, 0x00DF)) + \
        list(xrange(0x00E0, 0x00EF)) + \
        list(xrange(0x00F0, 0x00F6)) + \
        list(xrange(0x00F8, 0x00FF))


library.register(Charmap)
