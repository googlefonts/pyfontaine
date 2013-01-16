# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Cham'
    native_name = u''
    key = 0xAA00
    glyphs = \
        list(xrange(0xAA00, 0xAA36)) + \
        list(xrange(0xAA40, 0xAA4D)) + \
        list(xrange(0xAA50, 0xAA59)) + \
        list(xrange(0xAA5C, 0xAA5F))


library.register(Charmap)
