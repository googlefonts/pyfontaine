# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Basic Cyrillic'
    native_name = u'Кири́ллица'
    glyphs = xrange(0x0410, 0x044f)


library.register(Charmap)
