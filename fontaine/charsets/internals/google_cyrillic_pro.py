# -*- coding: utf-8 -*-
from gfonts_utils import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Cyrillic Pro'
    native_name = u''
    abbreviation = 'CYRL'

    def glyphs(self):
        glyphs = codepointsInNamelist("google_glyphsets/Cyrillic/GF-cyrillic-pro_unique-glyphs.nam")
        return glyphs


