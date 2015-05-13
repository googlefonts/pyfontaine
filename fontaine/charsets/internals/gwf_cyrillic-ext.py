# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Google cyrillic-ext'
    native_name = u''
    abbreviation = 'CYRL'

    def glyphs(self):
        # cyrillic-ext subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = (range(0x400, 0x530) +
                   [0x20b4] +
                   range(0x2de0, 0x2e00) +
                   range(0xa640, 0xa6a0))
        return glyphs


