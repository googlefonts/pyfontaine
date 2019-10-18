# -*- coding: utf-8 -*-
from fontaine.namelist import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Latin Pro'
    native_name = u''
    abbreviation = 'LAT'

    def glyphs(self):
        glyphs = codepointsInNamelist("charsets/internals/google_glyphsets/GF-latin-pro_unique-glyphs.nam")
        return glyphs


