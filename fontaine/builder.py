import csv
import os
import StringIO

try:
    from unicodenames import unicodenames
    os.environ['UNAMES_INSTALLED'] = 'uname-installed'
except ImportError:
    pass


from fontaine.const import SUPPORT_LEVEL_FULL, SUPPORT_LEVEL_UNSUPPORTED
from fontaine.cmap import library
from fontaine.structures.dict2xml import dict2xml, dict2txt


def yesno(val):
    return 'yes' if val else 'no'


db = os.environ.get('UNAMES_DB') or os.path.join(
        os.path.dirname(__file__), 'charmaps', 'names.db', 'en.names-db')


def format(x):
    return u'U+%04x\x20\x20%s\x20\x20%s' % \
        (x, unichr(x), unicodenames(db).name(x) or '')


def unicodevalues_asstring(values):
    """ Return string with unicodenames if db defined """
    if os.environ.get('UNAMES_INSTALLED') and not os.environ.get('DISABLE_UNAMES'):
        return map(lambda x: '%s' % format(x).strip(), values)
    return map(lambda x: u'U+%04x %s' % (x, unichr(x)), values)


class Director(object):

    def construct_tree(self, fonts):

        tree = {'fonts': []}

        for font in fonts:
            F = {}
            desc = {
                'commonName': font.common_name,
                'subFamily': font.sub_family,
                'style': font.style_flags,
                'weight': font.weight,
                'fixedWidth': yesno(font.is_fixed_width),
                'fixedSizes': yesno(font.has_fixed_sizes),
                'copyright': font.copyright,
                'license': font.license.replace('\r', ' '),
                'licenseUrl': font.license_url,
                'Version': font.version,
                'Vendor': font.vendor,
                'vendorUrl': font.vendor_url,
                'designer': font.designer,
                'designerUrl': font.designer_url,
                'glyphCount': font.glyph_num,
                'characterCount': font.character_count
            }
            orthgraph = None
            for charmap, support_level, coverage, missing in font.get_orthographies():
                if support_level == SUPPORT_LEVEL_UNSUPPORTED:
                    continue
                if not orthgraph:
                    desc['orthographies'] = []

                orth = {'orthography': {}}
                orth['orthography']['commonName'] = charmap.common_name
                orth['orthography']['nativeName'] = charmap.native_name
                orth['orthography']['supportLevel'] = support_level

                if support_level != SUPPORT_LEVEL_FULL:
                    values = u'\n%s' % u'\n'.join(unicodevalues_asstring(missing))
                    orth['orthography']['percentCoverage'] = coverage
                    orth['orthography']['missingValues'] = values

                desc['orthographies'].append(orth)

            F['font'] = desc
            tree['fonts'].append(F)

        return tree


class Builder(object):

    @staticmethod
    def text_(tree):
        return dict2txt(tree)

    @staticmethod
    def xml_(tree):
        return dict2xml({'report': tree})

    @staticmethod
    def csv_(fonts):
        data = StringIO.StringIO()
        doc = csv.writer(data, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        headers = ['Common Name']
        for subset in library.charmaps:
            headers.append(subset.common_name)
        doc.writerow(headers)

        for font in fonts:
            row = [font.common_name]
            for subset in library.charmaps:
                charmap, support_level, coverage, missing = font.get_othography_info(subset)
                row.append(str(coverage))
            doc.writerow(row)

        data.seek(0)
        return data.read()

letterlower = lambda s: s[:1].lower() + s[1:] if s else ''
