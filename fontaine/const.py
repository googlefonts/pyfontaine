# -*- coding: utf-8 -*-
#
# const.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.
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

COVERAGE_MINIMAL = 80

SUPPORT_LEVEL_FRAGMENTARY = 'fragmentary'
SUPPORT_LEVEL_FULL = 'full'
SUPPORT_LEVEL_PARTIAL = 'partial'
SUPPORT_LEVEL_UNSUPPORTED = 'unsupported'

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
