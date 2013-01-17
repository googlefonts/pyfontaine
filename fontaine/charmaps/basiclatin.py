# -*- coding: utf8 -*-
from fontaine.cmap import library


class Charmap:

    common_name = 'Basic Latin'
    native_name = 'Basic Latin'

    def glyphs(self):
        return range(0x0041, 0x005A)

    key = 0x0041


library.register(Charmap)
