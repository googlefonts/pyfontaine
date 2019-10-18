# -*- coding: utf-8 -*-
from fontaine.namelist import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Cyrillic Historical'
    native_name = u''
    abbreviation = 'CYRL'

    def glyphs(self):
        glyphs = codepointsInNamelist("charsets/internals/google_glyphsets/Cyrillic/GF-cyrillic-historical_unique-glyphs.nam")
        return glyphs


