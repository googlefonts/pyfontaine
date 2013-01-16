# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Catalan'
    native_name = u'Català'
    key = 0x013F
    glyphs = [
        0x00C0,
        0x00E0,
        0x00C7,
        0x00E7,
        0x00C8,
        0x00E8,
        0x00C9,
        0x00E9,
        0x00CD,
        0x00ED,
        0x00CF,
        0x00EF,
        0x013F,
        0x0140,
        0x00D2,
        0x00F2,
        0x00D3,
        0x00F3,
        0x00DA,
        0x00FA,
        0x00DC,
        0x00FC,
        0x00D1,
        0x00F1
    ]


library.register(Charmap)
