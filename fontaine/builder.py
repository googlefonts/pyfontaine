import csv
import os
import re
import StringIO

try:
    from unicodenames import unicodenames
    os.environ['UNAMES_INSTALLED'] = 'uname-installed'
except ImportError:
    pass

from lxml import etree

from fontaine.const import SUPPORT_LEVEL_FULL, SUPPORT_LEVEL_UNSUPPORTED
from fontaine.cmap import library


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
        tree = Section()
        root = tree.add_section('Fonts')
        for font in fonts:

            fs = root.add_section('Font')
            root.add_key(fs, 'Common Name', font.common_name)
            root.add_key(fs, 'Sub family', font.sub_family)
            root.add_key(fs, 'Style', font.style_flags)
            root.add_key(fs, 'Weight', font.weight)
            root.add_key(fs, 'Fixed width', yesno(font.is_fixed_width))
            root.add_key(fs, 'Fixed sizes',
                yesno(font.has_fixed_sizes))
            root.add_key(fs, 'Copyright', font.copyright)
            root.add_key(fs, 'License', font.license)
            root.add_key(fs, 'License url', font.license_url)
            root.add_key(fs, 'Version', font.version)
            root.add_key(fs, 'Vendor', font.vendor)
            root.add_key(fs, 'Vendor url', font.vendor_url)
            root.add_key(fs, 'Designer', font.designer)
            root.add_key(fs, 'Designer url', font.designer_url)
            root.add_key(fs, 'Glyph count', font.glyph_num)
            root.add_key(fs, 'Character count', font.character_count)

            orthgraph = None
            for charmap, level, coverage, missing in font.get_orthographies():
                if level == SUPPORT_LEVEL_UNSUPPORTED:
                    continue
                if not orthgraph:
                    orthgraph = fs.add_section('Orthographies')

                o = orthgraph.add_section('Orthography')
                root.add_key(o, 'Common Name',
                    charmap.common_name)
                root.add_key(o, 'Native Name',
                    charmap.native_name)
                root.add_key(o, 'Support Level', level)
                if level != SUPPORT_LEVEL_FULL:
                    values = u'\n%s' % u'\n'.join(unicodevalues_asstring(missing))
                    root.add_key(o,
                        'Percent coverage', coverage)
                    root.add_key(o, 'Missing values', values)

        return root


class Section(object):

    name = ''

    def __init__(self):
        self.keys = []
        self.sections = []

    def add_section(self, name, parent=None):
        section = Section()
        section.name = name
        if parent:
            parent.sections.append(section)
        else:
            self.sections.append(section)
        return section

    def add_key(self, section, name, value):
        section.keys.append({'name': name, 'value': value})


class Builder(object):

    @staticmethod
    def build_plaintext(section, level=0):
        for x in xrange(level):
            print ' ',
        print u'%s:' % section.name

        def ljust(s):
            return str.rjust(str(s.group(0)), len(s.group(0)) + level + 13)

        for k in section.keys:
            for x in xrange(level):
                print ' ',
            value = k['value']
            if k['name'] == 'Missing values':
                p = re.compile(r'U\+', re.M | re.U)
                value = p.sub(ljust, value)
            print u'  %s: %s' % (k['name'], value)
        for section in section.sections:
            Builder.build_plaintext(section, level + 1)

    @staticmethod
    def build_xml_report(section):
        root = etree.Element("report")
        print etree.tostring(Builder.build_xml(section, root),
            encoding="UTF-8", pretty_print=True)

    @staticmethod
    def build_csv_report(fonts):
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
        print data.read()

    @staticmethod
    def build_xml(section, element=None):
        if element is not None:
            el = etree.SubElement(element, letterlower(section.name))
        else:
            el = etree.Element(letterlower(section.name))

        for k in section.keys:
            keyel = etree.SubElement(el,
                letterlower(k['name']).replace(' ', ''))
            if isinstance(k['value'], int):
                k['value'] = str(k['value'])
            try:
                keyel.text = k['value']
            except Exception:
                pass

        for section in section.sections:
            Builder.build_xml(section, el)
        return element

letterlower = lambda s: s[:1].lower() + s[1:] if s else ''
