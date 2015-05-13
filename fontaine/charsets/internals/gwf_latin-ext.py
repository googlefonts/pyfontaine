# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Google latin-ext'
    native_name = u''
    abbreviation = 'LAT'

    def glyphs(self):
        # latin-ext subset from http://code.google.com/p/googlefontdirectory/source/browse/tools/subset/subset.py
        glyphs  = ( range(0x0100, 0x0370) +
                    range(0x1d00, 0x1ea0) +
                    range(0x1ef2, 0x1f00) +
                    range(0x2070, 0x20d0) +
                    range(0x2c60, 0x2c80) +
                    range(0xa700, 0xa800))
        glyphs += [0x02BC]
        glyphs += [0x0300]
        glyphs += [0x0301]
        glyphs += [0x0303]
        glyphs += [0x030F]
        glyphs += [0x2070] # zerosuperior
        glyphs += [0x2074] # foursuperior
        glyphs += [0x2075] # fivesuperior
        glyphs += [0x2076] # sixsuperior
        glyphs += [0x2077] # sevensuperior
        glyphs += [0x2078] # eightsuperior
        glyphs += [0x2079] # ninesuperior
        glyphs += [0x207F] # nsuperior
        return glyphs


