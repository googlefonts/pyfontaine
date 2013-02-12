# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF latin'
    native_name = u''

    def glyphs(self):
        # latin subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs  = [0x2013] # endash
        glyphs += [0x2014] # emdash
        glyphs += [0x2018] # quoteleft
        glyphs += [0x2019] # quoteright
        glyphs += [0x201A] # quotesinglbase
        glyphs += [0x201C] # quotedblleft
        glyphs += [0x201D] # quotedblright
        glyphs += [0x201E] # quotedblbase
        glyphs += [0x2022] # bullet
        glyphs += [0x2039] # guilsinglleft
        glyphs += [0x203A] # guilsinglright
        glyphs += range(0x20, 0x7f) # Basic Latin (A-Z, a-z, numbers)
        glyphs += range(0xa0, 0x100) # Western European symbols and diacritics
        glyphs += [0x20ac] # Euro
        glyphs += [0x0152] # OE
        glyphs += [0x0153] # oe
        glyphs += [0x003b] # semicolon
        glyphs += [0x00b7] # periodcentered
        glyphs += [0x0131] # dotlessi
        glyphs += [0x02c6] # circumflex
        glyphs += [0x02da] # ring
        glyphs += [0x02dc] # tilde
        glyphs += [0x2074] # foursuperior
        glyphs += [0x2215] # divison slash
        glyphs += [0x2044] # fraction slash
        return glyphs

library.register(Charmap)
