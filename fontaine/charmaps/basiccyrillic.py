# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Basic Cyrillic'
    native_name = u'Кири́ллица'
    glyphs  = range(0x0400, 0x045f)
    glyphs += [0x0490,
               0x0491,
               0x04B0,
               0x04B1,
               0x2116,
              ]

library.register(Charmap)
