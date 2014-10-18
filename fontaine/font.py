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
import os

from fontaine.cmap import library
from fontaine.const import *


def unifyunicode(string):
    if '\000' in string:
        string = unicode(string, 'utf-16-be').encode('utf-8')
    return string.decode('utf8', 'ignore')


def lookup_languages(unichar, _library=library):
    try:
        assert len(unichar) == 1
    except AssertionError:
        return []

    charmaps = []

    for charmap in _library.charmaps:

        glyphs = getattr(charmap, 'glyphs', [])
        if callable(glyphs):
            glyphs = glyphs()
        if ord(unicode(unichar)) in glyphs:
            charmaps.append(charmap)
    return charmaps


class FontFace(object):

    def __init__(self, fontfile):
        import fontTools.ttLib as ttLib
        self.ttf = ttLib.TTFont(fontfile)
        self._flags = 0

    def getCharmap(self):
        tempcmap = self.ttf['cmap'].getcmap(3, 1)
        if tempcmap is not None:
            return map(lambda s: s[0], tempcmap.cmap.items())
        return []

    def getGlyphNames(self):
        return self.ttf.getGlyphNames()

    def getNames(self):
        return self.ttf['name'].names

    def findName(self, nameid):
        names = filter(lambda s: str(s.nameID) == str(nameid), self.getNames())
        if not len(names):
            return
        return names[0]

    @property
    def family_name(self):
        value = self.findName(1)
        if not value:
            return ''
        return unifyunicode(value.string)

    @property
    def num_glyphs(self):
        return int(self.ttf['maxp'].numGlyphs)

    @property
    def style_name(self):
        value = self.findName(17)
        if not value:
            return ''
        return unifyunicode(value.string)

    @property
    def style_flags(self):
        if int(self.ttf['OS/2'].usWeightClass) > 400:
            self._flags = self._flags | FT_STYLE_FLAG_BOLD
        if self.ttf['post'].italicAngle != 0.0:
            self._flags = self._flags | FT_STYLE_FLAG_ITALIC
        return self._flags

    @property
    def is_fixed_width(self):
        return bool(self.ttf['head'].flags & FT_FACE_FLAG_FIXED_WIDTH)

    @property
    def has_fixed_sizes(self):
        return bool(self.ttf['head'].flags & FT_FACE_FLAG_FIXED_SIZES)


class TTXFontFace(FontFace):

    def __init__(self, fontfile):
        import fontTools.ttLib as ttLib
        self.ttf = ttLib.TTFont(None)
        self.ttf.importXML(fontfile, quiet=True)
        self._flags = 0


class FontFactory:

    @staticmethod
    def openfont(fontfile, charmaps=[]):
        if fontfile.lower().endswith('.ttx'):
            return TTXFont(fontfile, charmaps)
        if fontfile.lower().endswith('.ufo') and os.path.isdir(fontfile):
            try:
                import robofab
                return RoboFabFont(fontfile, charmaps)
            except ImportError:
                raise Exception('Install [RoboFab](https://pypi.python.org/pypi/robofab/) before using UFO with Pyfontaine')
        try:
            import freetype
            return FreeTypeFont(fontfile, charmaps)
        except ImportError:
            pass
        return TTFont(fontfile, charmaps)


class CharmapInfo(object):

    def __init__(self, ttfont, charmap):
        self.charmap = charmap
        self.missing = []
        self.ttfont = ttfont
        self.support_level = SUPPORT_LEVEL_UNSUPPORTED
        self.coverage = 0

        if hasattr(charmap, 'glyphnames'):
            self.init_configuration_for_glyphnames()
        else:
            self.init_configuration_for_unicodes()

    def init_configuration_for_glyphnames(self):
        glyphnames = self.charmap.glyphnames
        glyphs = set(glyphnames.pop())
        hits = 0
        while glyphs:
            if set(glyphs) & set(self.ttfont.getGlyphNames()):
                hits += 1
            else:
                self.missing += glyphs

            if glyphnames:
                glyphs = set(glyphnames.pop())
            else:
                glyphs = None

        glyphs_count = len(self.ttfont.getGlyphNames())
        if hits == glyphs_count:
            self.coverage = 100
            self.support_level = SUPPORT_LEVEL_FULL
        else:
            self.coverage = hits * 100 / glyphs_count
            if self.coverage == 0:
                pass
            elif self.coverage < COVERAGE_MINIMAL:
                self.support_level = SUPPORT_LEVEL_FRAGMENTARY
            else:
                self.support_level = SUPPORT_LEVEL_PARTIAL


    def init_configuration_for_unicodes(self):

        glyphs = getattr(self.charmap, 'glyphs', [])
        if callable(glyphs):
            glyphs = glyphs()

        hits = 0
        for char in glyphs:
            if char not in self.ttfont._unicodeValues:
                self.missing.append(char)
            else:
                hits += 1

        glyphs_count = len(glyphs)
        if hits == glyphs_count:
            self.coverage = 100
            self.support_level = SUPPORT_LEVEL_FULL
        else:
            self.coverage = hits * 100 / glyphs_count
            if self.coverage == 0:
                pass
            elif self.coverage < COVERAGE_MINIMAL:
                self.support_level = SUPPORT_LEVEL_FRAGMENTARY
            else:
                self.support_level = SUPPORT_LEVEL_PARTIAL


class TTFont(object):

    def __init__(self, fontfile, charmaps=[]):
        self._fontFace = FontFace(fontfile)
        self._unicodeValues = self._fontFace.getCharmap()

        self._charmaps = [str.lower(x) for x in charmaps]
        self.refresh_sfnt_properties()

    def getGlyphNames(self):
        return self._fontFace.getGlyphNames()

    def refresh_sfnt_properties(self):
        for record in self._fontFace.getNames():
            propname = NAME_ID_FONTPROPMAP.get(record.nameID)
            value = unifyunicode(record.string)
            setattr(self, '_%s' % propname, value)

    def get_orthographies(self, _library=library):
        ''' Returns list of CharmapInfo about supported orthographies '''
        results = []
        for charmap in _library.charmaps:
            if self._charmaps:
                cn = getattr(charmap, 'common_name', False)
                abbr = getattr(charmap, 'abbreviation', False)
                nn = getattr(charmap, 'short_name', False)

                if cn and cn.lower() in self._charmaps:
                    results.append(charmap)

                elif nn and nn.lower() in self._charmaps:
                    results.append(charmap)

                elif abbr and abbr.lower() in self._charmaps:
                    results.append(charmap)
            else:
                results.append(charmap)

        for result in results:
            yield CharmapInfo(self, result)

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
    _common_name = ''

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
    _sub_family = ''

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


class TTXFont(TTFont):

    def __init__(self, fontfile, charmaps=[]):
        self._fontFace = TTXFontFace(fontfile)
        self._unicodeValues = self._fontFace.getCharmap()

        self._charmaps = map(str.lower, charmaps)
        self.refresh_sfnt_properties()


class FreeTypeFont(TTFont):

    def __init__(self, fontfile, charmaps=[]):
        import freetype
        self._unicodeValues = []
        self._fontFace = freetype.Face(fontfile)
        charcode, agindex = self._fontFace.get_first_char()
        while agindex != 0:
            self._unicodeValues.append(charcode)
            charcode, agindex = self._fontFace.get_next_char(charcode, agindex)
        self._charmaps = [charmap.lower() for charmap in charmaps]
        self.refresh_sfnt_properties()

    def refresh_sfnt_properties(self):
        import freetype
        sfnt_count = self._fontFace.sfnt_name_count
        if not isinstance(sfnt_count, int):
            return
        for i in xrange(sfnt_count):
            try:
                sfnt_record = self._fontFace.get_sfnt_name(i)
            except freetype.FT_Exception:
                continue
            propname = NAME_ID_FONTPROPMAP.get(sfnt_record.name_id)
            value = unifyunicode(sfnt_record.string)
            setattr(self, '_%s' % propname, value)

    def getGlyphNames(self):
        raise NotImplementedError(('Get glyph names is not implemented'
                                   ' with FreeType library'))


class RoboFabFont(TTFont):

    def __init__(self, fontfile, charmaps=[]):
        import robofab.world
        self._fontFace = robofab.world.OpenFont(fontfile)
        self.info = self._fontFace.info.__dict__
        self._unicodeValues = map(lambda x: x.unicode, self._fontFace)
        self._charmaps = map(str.lower, charmaps)

    def getGlyphNames(self):
        return [t.name for t in self._fontFace]

    @property
    def common_name(self):
        return self.info.get('familyName', '')

    @property
    def copyright(self):
        return self.info.get('copyright', '')

    @property
    def designer(self):
        return self.info.get('openTypeNameDesigner', '')

    @property
    def designer_url(self):
        return self.info.get('openTypeNameManufacturerURL', '')

    @property
    def license(self):
        return self.info.get('openTypeNameLicense', '')

    @property
    def license_url(self):
        return self.info.get('openTypeNameLicenseURL', '')

    @property
    def glyph_num(self):
        return len(self._unicodeValues)

    @property
    def style_flags(self):
        return FT_STYLE_ITALIC \
            if self.info.get('italicAngle') else ''

    @property
    def sub_family(self):
        return self.info.get('styleName', '')

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
        return self.info.get('openTypeNameVersion', '')

    @property
    def weight(self):
        return FT_STYLE_BOLD \
            if self.info.get('openTypeOS2WeightClass', 0) >= 600 \
            else FT_STYLE_NORMAL

    @property
    def is_fixed_width(self):
        return bool(self.info.get('postscriptIsFixedPitch'))

    @property
    def has_fixed_sizes(self):
        # always False
        return False
