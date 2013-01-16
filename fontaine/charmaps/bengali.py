# -*- coding: utf-8 -*-
from fontaine.cmap import library


class Charmap:
    common_name = u'Bengali'
    native_name = u'বাংলা'
    key = 0x0985
    glyphs = \
        list(xrange(0x0981, 0x0983)) + \
        list(xrange(0x0985, 0x098c)) + \
        list(xrange(0x098f, 0x0990)) + \
        list(xrange(0x0993, 0x09a8)) + \
        list(xrange(0x09aa, 0x09b0)) + \
        [0x09b2] + \
        list(xrange(0x09b6, 0x09b9)) + \
        [0x09bc] + \
        list(xrange(0x09be, 0x09c4)) + \
        list(xrange(0x09c7, 0x09c8)) + \
        list(xrange(0x09cb, 0x09cd)) + \
        [0x09d7] + \
        list(xrange(0x09dc, 0x09dd)) + \
        list(xrange(0x09df, 0x09e3)) + \
        list(xrange(0x09e6, 0x09fa))


library.register(Charmap)
