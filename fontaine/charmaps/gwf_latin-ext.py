# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF latin-ext'
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
        # latin-ext
        glyphs += (range(0x100, 0x370) +
                   range(0x1d00, 0x1ea0) +
                   range(0x1ef2, 0x1f00) +
                   range(0x2070, 0x20d0) +
                   range(0x2c60, 0x2c80) +
                   range(0xa700, 0xa800))
        return glyphs

library.register(Charmap)
