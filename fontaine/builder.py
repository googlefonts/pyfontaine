# -*- coding: utf-8 -*-
#
# builder.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

from __future__ import print_function
import csv
import os
import StringIO
import sys
import unicodedata

from collections import OrderedDict


from fontaine.const import SUPPORT_LEVEL_FULL, SUPPORT_LEVEL_UNSUPPORTED
from fontaine.cmap import library
from fontaine.font import Font
from fontaine.structures.dict2xml import dict2xml, dict2txt


def yesno(val):
    return 'yes' if val else 'no'


db = os.environ.get('UNAMES_DB') or os.path.join(os.path.dirname(__file__),
                                                 'charmaps', 'names.db',
                                                 'en.names-db')


def format(x):
    return u'U+%04x\x20\x20%s\x20\x20%s' % \
        (x, unichr(x), unicodedata.name(unichr(x), ''))


def unicodevalues_asstring(values):
    """ Return string with unicodenames (unless that is disabled) """
    if not os.environ.get('DISABLE_UNAMES'):
        return map(lambda x: '%s' % format(x).strip(), values)
    return map(lambda x: u'U+%04x %s' % (x, unichr(x)), values)


extract_firstline = lambda text: \
    (text or '').replace('\r', '\n').split('\n')[0]


class Director(object):

    def __init__(self, generate_coverage=None, charmaps=[]):
        self.generate_coverage = generate_coverage
        self.charmaps = charmaps

    def represent_coverage_png(self, font):
        cmaps = filter(lambda x: hasattr(x, 'key'), library.charmaps)

        if not os.path.exists('coverage_pngs'):
            os.makedirs('coverage_pngs')

        for cmap in cmaps:
            if self.charmaps:
                cn = getattr(cmap, 'common_name', False)
                nn = getattr(cmap, 'native_name', False)
                if cn and cn not in self._charmaps:
                    continue
                if nn and nn not in self._charmaps:
                    continue

            if cmap.key not in font._unicodeValues:
                continue

            filename = u'coverage_pngs/%s - %s' % (font.common_name,
                                                   cmap.common_name)

            txtFilename = filename + '.txt'
            fp = open(txtFilename, 'w+')

            glyphs = cmap.glyphs
            if callable(glyphs):
                glyphs = glyphs()
            for i, char in enumerate(sorted(glyphs)):
                flag = str(0)
                if char in font._unicodeValues:
                    flag = str(1)
                fp.write(str(i + 1) + ' ' + flag + '\n')

            fp.close()
            hilbertScript = ('simpleHilbertCurve'
                             ' --outFormat=png'
                             ' --level=3'
                             ' --out="%s" "%s"') % (filename, txtFilename)
            os.system(hilbertScript)

    def construct_tree(self, fonts):

        tree = OrderedDict({'fonts': []})

        for font_filename in fonts:
            font = Font(font_filename, charmaps=self.charmaps)

            F = OrderedDict()
            desc = OrderedDict()
            desc['commonName'] = font.common_name
            desc['subFamily'] = font.sub_family
            desc['style'] = font.style_flags
            desc['weight'] = font.weight
            desc['fixedWidth'] = yesno(font.is_fixed_width)
            desc['fixedSizes'] = yesno(font.has_fixed_sizes)
            desc['copyright'] = extract_firstline(font.copyright or '')
            desc['license'] = extract_firstline(font.license or '')
            desc['licenseUrl'] = font.license_url
            desc['version'] = font.version
            desc['vendor'] = extract_firstline(font.vendor or '')
            desc['vendorUrl'] = font.vendor_url
            desc['designer'] = font.designer
            desc['designerUrl'] = font.designer_url
            desc['glyphCount'] = font.glyph_num
            desc['characterCount'] = font.character_count
            for charmap, support_level, coverage, missing \
                    in font.get_orthographies():
                if support_level == SUPPORT_LEVEL_UNSUPPORTED:
                    continue
                if 'orthographies' not in desc:
                    desc['orthographies'] = []

                orth = OrderedDict({'orthography': OrderedDict()})
                orth['orthography']['commonName'] = charmap.common_name
                orth['orthography']['nativeName'] = charmap.native_name
                orth['orthography']['supportLevel'] = support_level

                if support_level != SUPPORT_LEVEL_FULL:
                    values = u'\n%s' % u'\n'.join(unicodevalues_asstring(missing))
                    orth['orthography']['percentCoverage'] = coverage
                    orth['orthography']['missingValues'] = values

                desc['orthographies'].append(orth)

            if self.generate_coverage:
                self.represent_coverage_png(font)

            F['font'] = desc
            tree['fonts'].append(F)

        return tree


class Builder(object):

    @staticmethod
    def text_(tree):
        return dict2txt(tree, names=NAMES)

    @staticmethod
    def xml_(tree):
        return dict2xml({'report': tree})

    @staticmethod
    def json_(tree):
        items_length = 0
        pprint(tree, indent='', items_length=items_length)

    @staticmethod
    def csv_(fonts):
        data = StringIO.StringIO()
        doc = csv.writer(data, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        headers = ['Family', 'Style']
        for subset in library.charmaps:
            headers.append(subset.common_name)
        doc.writerow(headers)

        for font in fonts:
            row = [font.common_name.encode('ascii', 'ignore')] + [font.sub_family.encode('ascii', 'ignore')]
            for subset in library.charmaps:
                charmap, support_level, coverage, missing = font.get_othography_info(subset)
                row.append(str(coverage))
            doc.writerow(row)

        data.seek(0)
        return data.read()


NAMES = {
    'fonts': 'Fonts',
    'font': 'Font',
    'commonName': 'Common name',
    'nativeName': 'Native name',
    'subFamily': 'Sub family',
    'style': 'Style',
    'weight': 'Weight',
    'fixedWidth': 'Fixed width',
    'fixedSizes': 'Fixed sizes',
    'copyright': 'Copyright',
    'license': 'License',
    'licenseUrl': 'License url',
    'version': 'Version',
    'vendor': 'Vendor',
    'vendorUrl': 'Vendor url',
    'designer': 'Designer',
    'designerUrl': 'Designer url',
    'glyphCount': 'Glyph count',
    'characterCount': 'Character count',
    'orthographies': 'Orthographies',
    'orthography': 'Orthography',
    'supportLevel': 'Support level',
    'percentCoverage': 'Percent coverage',
    'missingValues': 'Missing values'
}


def pprint_dict(obj, indent, length):
    for i, key in enumerate(obj.keys()):
        comma = ', '
        if i + 1 == length:
            comma = ''
        if type(obj[key]) in [str, int, unicode]:
            value = unicode(obj[key]).replace('\n', ', ').strip(', ')
            value = value.replace('"', '\"').replace('\\', '\\\\')
            value = value.replace('\r', '')
            sys.stdout.write((u"%s  %r: \"%s\"%s" % (indent, key, value, comma)))
        else:
            sys.stdout.write((u"%s  %r:" % (indent, key)))
            pprint(obj[key], indent + '  ')


def pprint(obj, indent='', items_length=0):
    comma = ''
    if isinstance(obj, OrderedDict):
        length = len(obj.keys())
        if length == 1:
            pprint(obj[obj.keys()[0]], indent, items_length=items_length)
            return

        sys.stdout.write((u"%s{" % indent))
        pprint_dict(obj, indent, length)
        if items_length > 0:
            comma = ', '
        sys.stdout.write((u"%s}%s" % (indent, comma)))
    elif isinstance(obj, list):
        sys.stdout.write((u"%s[" % indent))
        length = len(obj)
        for i, o in enumerate(obj):
            length -= 1
            pprint(o, indent + '  ', items_length=length)
        sys.stdout.write((u"%s]%s" % (indent, comma)))
