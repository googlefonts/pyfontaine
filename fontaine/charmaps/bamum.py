# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Bamum'
    native_name = u"ꚠꚡꚢꚣ"
    key = 0xA6A0
    glyphs = xrange(0xA6A0, 0xA6F7)


library.register(Charmap)
