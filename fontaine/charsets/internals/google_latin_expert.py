# -*- coding: utf-8 -*-
from fontaine.namelist import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Latin Expert'
    native_name = u''
    abbreviation = 'LAT'

    def glyphs(self):
        glyphs = codepointsInNamelist("charsets/internals/google_glyphsets/GF-latin-expert_unique-glyphs.nam")
        return glyphs


