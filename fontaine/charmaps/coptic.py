# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Coptic'
    native_name = u"Ⲙⲉⲧⲣⲉⲙ̀ⲛⲭⲏⲙⲓ"
    key = 0x03E2
    glyphs = \
        list(xrange(0x03e2, 0x03ef)) + \
        list(xrange(0x2c80, 0x2cb1)) + \
        list(xrange(0x2cb2, 0x2cdb)) + \
        list(xrange(0x2cdc, 0x2ce3)) + \
        list(xrange(0x2ce4, 0x2cea)) + \
        list(xrange(0x2cf9, 0x2cfc)) + \
        [
        0x2cfd,
        0x2cfe,
        0x2cff
        ]


library.register(Charmap)
