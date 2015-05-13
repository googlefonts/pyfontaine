# -*- coding: utf-8 -*-
class Charset:
    common_name = "Armenian"
    native_name = u"Հայերեն"
    key = 0x0561  # ARMENIAN SMALL LETTER AYB
    abbreviation = 'ARMN'
    glyphs = \
        list(xrange(0x0531, 0x0556)) + \
        list(xrange(0x0559, 0x055f)) + \
        list(xrange(0x0561, 0x0587)) + \
        [0x589, 0x58a]
