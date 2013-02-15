# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF extras'
    native_name = u''

    def glyphs(self):
        glyphs  = [0xe0ff] # PUA: Font logo
        glyphs += [0xeffd] # PUA: Font version number
        glyphs += [0xf000] # PUA: font ppem size indicator: run `ftview -f 1255 10 Ubuntu-Regular.ttf` to see it in action!
        return glyphs

library.register(Charmap)
