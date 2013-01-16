# -*- coding: utf-8 -*-
#
# flinfo.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

import freetype

from fontaine.cmap import library
from fontaine.const import *


class Font:

    def __init__(self, fontfile):
        self._fontFace = freetype.Face(fontfile)
        self.refresh_sfnt_properties()

        self._unicodeValues = []
        charcode, agindex = self._fontFace.get_first_char()
        while agindex != 0:
            charcode, agindex = self._fontFace.get_next_char(charcode, agindex)
            self._unicodeValues.append(charcode)

    def refresh_sfnt_properties(self):
        sfnt_count = self._fontFace.sfnt_name_count
        if not isinstance(sfnt_count, int):
            return
        for i in xrange(sfnt_count):
            try:
                sfnt_record = self._fontFace.get_sfnt_name(i)
            except freetype.FT_Exception:
                continue
            propname = NAME_ID_FONTPROPMAP.get(sfnt_record.name_id)
            setattr(self, '_%s' % propname, sfnt_record.string)

    @staticmethod
    def unicodevalues_asstring(values):
        return map(lambda x: u'U+%04x (%s)' % (x, unichr(x)), values)

    def get_orthographies(self):
        orths = []
        missing = []
        for cmap in library.charmaps:

            if cmap.key not in self._unicodeValues:
                continue

            tries = 0
            hits = 0

            for char in cmap.glyphs:
                tries += 1
                if char not in self._unicodeValues:
                    missing.append(char)
                else:
                    hits += 1

            if hits == tries:
                orths.append((cmap, SUPPORT_LEVEL_FULL, 100, []))
            else:
                coverage = hits * 100 / tries
                if coverage < COVERAGE_MINIMAL:
                    support_level = SUPPORT_LEVEL_FRAGMENTARY
                else:
                    support_level = SUPPORT_LEVEL_PARTIAL
                orths.append((cmap, support_level, coverage, missing))

        return orths

    _supported_orthographies = []

    @property
    def orthographies(self):
        if not self._supported_orthographies:
            self._supported_orthographies = self.get_orthographies()
        return self._supported_orthographies

    @property
    def character_count(self):
        return len(self._unicodeValues)
    _character_count = 0

    @property
    def common_name(self):
        default = self._fontFace.family_name
        return self._common_name or default

    @property
    def copyright(self):
        return self._copyright
    _copyright = ''

    @property
    def designer(self):
        return self._designer
    _designer = ''

    @property
    def designer_url(self):
        return self._designer_url
    _designer_url = ''

    @property
    def license(self):
        return self._license
    _license = ''

    @property
    def license_url(self):
        return self._license_url
    _license_url = ''

    @property
    def glyph_num(self):
        return self._fontFace.num_glyphs

    @property
    def style_flags(self):
        return FT_STYLE_ITALIC \
            if self._fontFace.style_flags & FT_STYLE_FLAG_ITALIC \
                else ''

    @property
    def sub_family(self):
        default = self._fontFace.style_name
        return self._sub_family or default

    @property
    def vendor(self):
        return self._vendor
    _vendor = ''

    @property
    def vendor_url(self):
        return self._vendor_url
    _vendor_url = ''

    @property
    def version(self):
        return self._version
    _version = ''

    @property
    def weight(self):
        return FT_STYLE_BOLD \
            if self._fontFace.style_flags & FT_STYLE_FLAG_BOLD \
                else FT_STYLE_NORMAL

    @property
    def is_fixed_width(self):
        return self._fontFace.is_fixed_width

    @property
    def has_fixed_sizes(self):
        return self._fontFace.has_fixed_sizes


class Fonts:

    _fonts = []

    def add_font(self, fontfile):
        font = Font(fontfile)
        self._fonts.append(font)

    def print_plain_text(self):
        print 'Fonts'
        print
        for font in self._fonts:
            print '  Font'
            print
            print '    Common name:', font.common_name
            print '    Sub family:', font.sub_family
            print '    Style:', font.style_flags
            print '    Weight:', font.weight
            print '    Fixed width:', 'yes' if font.is_fixed_width else 'no'
            print '    Fixed sizes:', 'yes' if font.has_fixed_sizes else 'no'
            print '    Copyright:', font.copyright
            print '    License:', font.license
            print '    License url:', font.license_url
            print '    Version:', font.version
            print '    Vendor:', font.vendor
            print '    Vendor url:', font.vendor_url
            print '    Designer:', font.designer
            print '    Designer url:', font.designer_url
            print '    Glyph count:', font.glyph_num
            print '    Character count:', font.character_count
            print '    Orthographies:'
            for orth, level, coverage, missing in font.get_orthographies():
                print '      Orthography:'
                print '         Common Name:', orth.common_name
                print '         Native Name:', orth.native_name
                print '         Support Level:', level
                if level == SUPPORT_LEVEL_FRAGMENTARY:
                    print '         Percent coverage:', coverage
                    print u'         Missing values:',
                    print u', '.join(Font.unicodevalues_asstring(missing))
                print

    def print_xml(self):
        raise NotImplementedError
