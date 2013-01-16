# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Unified Canadian Aboriginal Syllabics'
    native_name = u'Unified Canadian Aboriginal Syllabics'
    key = 0x1433  # CANADIAN SYLLABICS PO
    glyphs = xrange(0x1401, 0x1676)


library.register(Charmap)
