# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'GWF vietnamese'
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
        # vietnamese
        glyphs += [0x00c0, 0x00c1, 0x00c2, 0x00c3, 0x00C8, 0x00C9,
                   0x00CA, 0x00CC, 0x00CD, 0x00D2, 0x00D3, 0x00D4,
                   0x00D5, 0x00D9, 0x00DA, 0x00DD, 0x00E0, 0x00E1,
                   0x00E2, 0x00E3, 0x00E8, 0x00E9, 0x00EA, 0x00EC,
                   0x00ED, 0x00F2, 0x00F3, 0x00F4, 0x00F5, 0x00F9,
                   0x00FA, 0x00FD, 0x0102, 0x0103, 0x0110, 0x0111,
                   0x0128, 0x0129, 0x0168, 0x0169, 0x01A0, 0x01A1,
                   0x01AF, 0x01B0, 0x20AB] + range(0x1EA0, 0x1EFA)
        return glyphs

library.register(Charmap)
