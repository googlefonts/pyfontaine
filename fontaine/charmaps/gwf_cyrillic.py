# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF cyrillic'
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
        glyphs += [0xe0ff] # PUA: Font logo
        glyphs += [0xeffd] # PUA: Font version number
        glyphs += [0xf000] # PUA: font ppem size indicator: run `ftview -f 1255 10 Ubuntu-Regular.ttf` to see it in action!
        # cyrillic
        glyphs += range(0x400, 0x460) + [0x490, 0x491, 0x4b0, 0x4b1]
        return glyphs

library.register(Charmap)
