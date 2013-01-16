from lxml import etree

from fontaine.const import SUPPORT_LEVEL_FULL


def yesno(val):
    return 'yes' if val else 'no'


def unicodevalues_asstring(values):
        return map(lambda x: u'U+%04x (%s)' % (x, unichr(x)), values)


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
                if not orthgraph:
                    orthgraph = fs.add_section('Orthographies')

                o = orthgraph.add_section('Orthography')
                root.add_key(o, 'Common Name',
                    charmap.common_name)
                root.add_key(o, 'Native Name',
                    charmap.native_name)
                root.add_key(o, 'Support Level', level)
                if level != SUPPORT_LEVEL_FULL:
                    root.add_key(o,
                        'Percent coverage', coverage)
                    root.add_key(o, 'Missing values',
                        u', '.join(unicodevalues_asstring(missing)))

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

        for k in section.keys:
            for x in xrange(level):
                print ' ',
            print u'  %s: %s' % (k['name'], k['value'])
        for section in section.sections:
            Builder.build_plaintext(section, level + 1)

    @staticmethod
    def build_xml(section, element=None):
        if element is not None:
            el = etree.SubElement(element, section.name)
        else:
            el = etree.XML("<report></report>")
            el = etree.SubElement(el, section.name)

        for k in section.keys:
            keyel = etree.SubElement(element, k['name'].replace(' ', ''))
            if isinstance(k['value'], int):
                k['value'] = str(k['value'])
            try:
                keyel.text = k['value']
            except Exception, ex:
                print ex
                print k['value']

        for section in section.sections:
            Builder.build_xml(section, el)
        return el
