# -*- coding utf-8 -*-
import re

from fontaine.ext.base import BaseExt
from fontaine.ext.update import get_from_cache


URL = 'https://raw.githubusercontent.com/pauldhunt/source-devanagari-sans/master/GlyphOrderAndAliasDB'


class Extension(BaseExt):

    extension_name = 'unencoded'
    description = 'Unencoded Glyphs'

    @staticmethod
    def __getcharsets__():
        f = open(get_from_cache('AdobeSourceSansDevanagariGlyphOrderAndAliasDB.txt', URL), 'r')

        glyphnames = []
        for line in f:
            glyphnames += [re.sub(r'\s+', ' ', line).split()]

        return [type('Charset', (object,),
                     dict(glyphnames=glyphnames,
                          common_name='Unencoded Glyphs',
                          short_name='unencoded-glyphs',
                          native_name=''))]
