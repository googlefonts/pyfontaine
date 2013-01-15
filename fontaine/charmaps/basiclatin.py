# -*- coding: utf8 -*-
from fontaine.cmap import library


class Charmap:

    name = 'Basic Latin'

    glyphs = \
        xrange(0x0041, 0x005A)


library.register(Charmap)
