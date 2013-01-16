# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Buginese'
    native_name = u''
    key = 0x1A00
    glyphs = \
        list(xrange(0x1A00, 0x1A1B)) + \
        list(xrange(0x1A1E, 0x1A1F))


library.register(Charmap)
