#!/usr/bin/env python
#
# fontaine.py
#
# Copyright (c) 2013, 
# Виталий Волков <hash.3g@gmail.com> 
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

import freetype
import logging

from fontTools.unicode import Unicode


log = logging.getLogger(__name__)


FT_STYLE_FLAG_ITALIC = (1 << 0)
FT_STYLE_FLAG_BOLD = (1 << 1)
FT_FACE_FLAG_SFNT = (1L << 3)

FT_STYLE_ITALIC = 'italic'
FT_STYLE_BOLD = 'bold'
FT_STYLE_NORMAL = 'normal'

NID_COPYRIGHT = 0
NID_FONT_FAMILY = 1
NID_FONT_SUBFAM = 2
NID_UNIQUE_ID = 3
NID_FULL_NAME = 4
NID_VERSION = 5
NID_POSTSCRIPT = 6
NID_TRADEMARK = 7
NID_VENDOR = 8
NID_DESIGNER = 9
NID_DESCRIPTION = 10
NID_URL_VENDOR = 11
NID_URL_DESIGNER = 12
NID_LICENSE = 13
NID_URL_LICENSE = 14
NID_RESERVED = 15
NID_PREF_NAME = 16
NID_PREF_SUBFAM = 17
NID_MAC_FULLNAME = 18
NID_SAMPLETEXT = 19
NID_FINDFONT_NM = 20


NAME_ID_FONTPROPMAP = {
    NID_COPYRIGHT: 'copyright',
    NID_FONT_FAMILY: 'common_name',
    NID_FONT_SUBFAM: 'sub_family',
    NID_UNIQUE_ID: 'unique_id',
    NID_FULL_NAME: 'full_name',
    NID_VERSION: 'version',
    NID_POSTSCRIPT: 'postscript',
    NID_TRADEMARK: 'trademark',
    NID_VENDOR: 'vendor',
    NID_DESIGNER: 'designer',
    NID_DESCRIPTION: 'description',
    NID_URL_VENDOR: 'vendor_url',
    NID_URL_DESIGNER: 'designer_url',
    NID_LICENSE: 'license',
    NID_URL_LICENSE: 'license_url',
    NID_RESERVED: 'reserved',
    NID_PREF_NAME: 'pref_name',
    NID_PREF_SUBFAM: 'sub_family',
    NID_MAC_FULLNAME: 'mac_fullname',
    NID_SAMPLETEXT: 'sample_text',
    NID_FINDFONT_NM: 'findfont_nm',
}


class Font:

    def __init__(self, fontfile):
        self._fontFace = freetype.Face(fontfile)

        self.refresh_sfnt_properties()

        self.codes = set()
        self.complete = set(Unicode.codes.keys())

        charcode, agindex = self._fontFace.get_first_char()
        while agindex != 0:
            self.codes.add(charcode)
            charcode, agindex = self._fontFace.get_next_char(charcode, agindex)
            self._character_count += 1

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

    def find_missing(self):
        return map(hex, sorted(self.complete.difference(self.codes)))

    @property
    def character_count(self):
        return self._character_count
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
            print

    def print_xml(self):
        raise NotImplementedError
