# -*- coding: utf8 -*-
from fontaine.cmap import library


class Charmap:

    common_name = "Arabic"
    native_name = u"العربية"
    key = 0x0639  # ARABIC LETTER AIN

    glyphs = \
        list(xrange(0x0621, 0x063a)) + \
        list(xrange(0x0640, 0x0652)) + \
        list(xrange(0x0660, 0x0669))


library.register(Charmap)
