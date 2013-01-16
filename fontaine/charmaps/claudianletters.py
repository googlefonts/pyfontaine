# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Claudian Letters'
    native_name = u'Claudian Letters'
    key = 0x2183
    glyphs = [
        0x2132,
        0x214E,
        0x2183,
        0x2184,
        0x2C75,
        0x2C76
    ]


library.register(Charmap)
