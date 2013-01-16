# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Cherokee'
    native_name = u'ᏣᎳᎩ'
    key = 0x13E3
    glyphs = xrange(0x13A0, 0x13F4)


library.register(Charmap)
