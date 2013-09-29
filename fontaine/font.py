# -*- coding: utf-8 -*-
#
# font.py
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

    def __init__(self, fontfile, charmaps=[]):
        self._fontFace = freetype.Face(fontfile)
        self._charmaps = charmaps
        self.refresh_sfnt_properties()

        self._unicodeValues = []
        charcode, agindex = self._fontFace.get_first_char()
        while agindex != 0:
            self._unicodeValues.append(charcode)
            charcode, agindex = self._fontFace.get_next_char(charcode, agindex)

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
            setattr(self, '_%s' % propname,
                    sfnt_record.string.replace('\x00', '').decode('utf8',
                                                                  'ignore'))

    def get_othography_info(self, charmap, hits=0):
        ''' Return 4-tuple list with short orthographies information
            * selected supported character map by py-fontaine
            * support level with current font instance
            * percent of coverage filled glyphs
            * array of missing unicode characters codes
        '''
        missing = []

        glyphs = getattr(charmap, 'glyphs', [])
        if callable(glyphs):
            glyphs = glyphs()

        for char in glyphs:
            if char not in self._unicodeValues:
                missing.append(char)
            else:
                hits += 1
        glyphs_count = len(glyphs)
        if hits == glyphs_count:
            return (charmap, SUPPORT_LEVEL_FULL, 100, [])

        coverage = hits * 100 / glyphs_count
        if coverage == 0:
            return (charmap, SUPPORT_LEVEL_UNSUPPORTED, 0, [])
        elif coverage < COVERAGE_MINIMAL:
            support_level = SUPPORT_LEVEL_FRAGMENTARY
        else:
            support_level = SUPPORT_LEVEL_PARTIAL
        return (charmap, support_level, coverage, missing)

    def get_orthographies(self):
        ''' Return array of 4-tuples lists about supported orthographies
        for current font instance'''
        for charmap in library.charmaps:
            if self._charmaps:
                cn = getattr(charmap, 'common_name', False)
                nn = getattr(charmap, 'native_name', False)
                if cn and cn not in self._charmaps:
                    continue
                if nn and nn not in self._charmaps:
                    continue
            yield self.get_othography_info(charmap)

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
        try:
            return self._license.split('\n')[0]
        except IndexError:
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
