# -*- coding: utf-8 -*-
from fontaine.namelist import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Greek Coptic'
    native_name = u''
    abbreviation = 'GREK'

    def glyphs(self):
        glyphs = codepointsInNamelist("charsets/internals/google_glyphsets/Greek/GF-greek-coptic.nam")
        return glyphs


