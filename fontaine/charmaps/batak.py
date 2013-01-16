# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Surat Batak'
    native_name = u''
    key = 0x1BC0
    glyphs = \
        list(xrange(0x1BC0, 0x1BF3)) + \
        list(xrange(0x1BFC, 0x1BFF))


library.register(Charmap)
