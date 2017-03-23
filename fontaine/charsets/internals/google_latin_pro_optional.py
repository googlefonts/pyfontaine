# -*- coding: utf-8 -*-
from gfonts_utils import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Latin Pro (Optional Glyphs)'
    native_name = u''
    abbreviation = 'LAT'

    def glyphs(self):
        glyphs = codepointsInNamelist("google_glyphsets/GF-latin-pro_optional-glyphs.nam")
        return glyphs


