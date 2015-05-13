# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Google greek'
    native_name = u''
    abbreviation = 'GREK'

    def glyphs(self):
        # greek subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs = range(0x370, 0x400)
        return glyphs


