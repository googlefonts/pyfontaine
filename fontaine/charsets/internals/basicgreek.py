# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Basic Greek'
    native_name = u"Ελληνικό αλφάβητο"
    abbreviation = 'GREKb'
    key = 0x03a9
    glyphs = [
        0x0386,
        0x0388,
        0x0389,
        0x038a,
        0x038c,
        0x038e,
        0x038f,
        0x0390] + \
        list(xrange(0x0391, 0x03a1)) + \
        list(xrange(0x03a3, 0x03a9)) + \
        list(xrange(0x03aa, 0x03b0)) + \
        list(xrange(0x03b1, 0x03c9)) + \
        list(xrange(0x03ca, 0x03ce))



