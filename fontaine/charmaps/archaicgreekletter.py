# -*- coding: utf8 -*-
from fontaine.cmap import library


class Charmap:

    common_name = "Archaic Greek Letters"
    native_name = "Archaic Greek Letters"
    key = 0x03e0  # Greek letter SAMPI

    glyphs = [
        0x0370,
        0x0371,
        0x0372,
        0x0373,
        0x0376,
        0x0377
    ]
    glyphs += list(xrange(0x03d8, 0x03e1))
    glyphs += [
        0x03f7,
        0x03f8,
        0x03fa,
        0x03fb
    ]


library.register(Charmap)
