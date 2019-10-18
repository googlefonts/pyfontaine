# -*- coding: utf-8 -*-
from fontaine.namelist import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Greek Ancient Musical Symbols'
    native_name = u''
    abbreviation = 'GREK'

    def glyphs(self):
        glyphs = codepointsInNamelist("charsets/internals/google_glyphsets/Greek/GF-greek-ancient-musical-symbols.nam")
        return glyphs


