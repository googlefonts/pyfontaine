# -*- coding: utf-8 -*-
from gfonts_utils import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Latin Plus'
    native_name = u''
    abbreviation = 'LAT'

    def glyphs(self):
        glyphs = codepointsInNamelist("google_glyphsets/GF-latin-plus_unique-glyphs.nam")
        return glyphs


