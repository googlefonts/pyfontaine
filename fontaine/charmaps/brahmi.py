# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Brahmi'
    native_name = u''
    key = 0x11005
    glyphs = \
        list(xrange(0x11000, 0x1104D)) + \
        list(xrange(0x11052, 0x1106F))


library.register(Charmap)
