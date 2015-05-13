# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Google latin'
    native_name = u''
    abbreviation = 'LAT'

    def glyphs(self):
        # latin subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs  = [0x00AD] # Non Breaking Space, should be present in font
        glyphs += [0x00D0] # Carriage Return control char, should be present in font
        glyphs += [0x2013] # endash
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
        glyphs += [0x0131] # dotlessi
        glyphs += [0x02c6] # circumflex
        glyphs += [0x02da] # ring
        glyphs += [0x02dc] # tilde
        glyphs += [0x2074] # foursuperior
        glyphs += [0x2215] # divison slash
        glyphs += [0x2044] # fraction slash
        # glyphs += [0x2215] # slash division (commented since almost no fonts have this)
        # glyphs += [0xE0FF] # PUA: Font logo
        # glyphs += [0xEFFD] # PUA: Font version number
        # glyphs += [0xF000] # PUA: font ppem size indicator: run `ftview -f 1255 10 Ubuntu-Regular.ttf` to see it in action!
        return glyphs


