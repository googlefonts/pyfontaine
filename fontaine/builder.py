from fontaine.const import SUPPORT_LEVEL_FULL


def yesno(val):
    return 'yes' if val else 'no'


def unicodevalues_asstring(values):
        return map(lambda x: u'U+%04x (%s)' % (x, unichr(x)), values)


class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def construct_tree(self, fonts):
        root = self.builder.add_section('Fonts')
        for font in fonts:

            fs = self.builder.add_section('Font', parent=root)
            self.builder.add_key(fs, 'Common Name', font.common_name)
            self.builder.add_key(fs, 'Sub family', font.sub_family)
            self.builder.add_key(fs, 'Style', font.style_flags)
            self.builder.add_key(fs, 'Weight', font.weight)
            self.builder.add_key(fs, 'Fixed width', yesno(font.is_fixed_width))
            self.builder.add_key(fs, 'Fixed sizes',
                yesno(font.has_fixed_sizes))
            self.builder.add_key(fs, 'Copyright', font.copyright)
            self.builder.add_key(fs, 'License', font.license)
            self.builder.add_key(fs, 'License url', font.license_url)
            self.builder.add_key(fs, 'Version', font.version)
            self.builder.add_key(fs, 'Vendor', font.vendor)
            self.builder.add_key(fs, 'Vendor url', font.vendor_url)
            self.builder.add_key(fs, 'Designer', font.designer)
            self.builder.add_key(fs, 'Designer url', font.designer_url)
            self.builder.add_key(fs, 'Glyph count', font.glyph_num)
            self.builder.add_key(fs, 'Character count', font.character_count)

            orthgraph = None
            for charmap, level, coverage, missing in font.get_orthographies():
                if not orthgraph:
                    orthgraph = fs.add_section('Orthographies')

                o = orthgraph.add_section('Orthography')
                self.builder.add_key(o, 'Common Name',
                    charmap.common_name)
                self.builder.add_key(o, 'Native Name',
                    charmap.native_name)
                self.builder.add_key(o, 'Support Level', level)
                if level != SUPPORT_LEVEL_FULL:
                    self.builder.add_key(o,
                        'Percent coverage', coverage)
                    self.builder.add_key(o, 'Missing values',
                        u', '.join(unicodevalues_asstring(missing)))

    def build(self):
        self.builder.build()


class Builder(object):

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

    def build(self, l=0):
        for k in self.keys:
            for x in xrange(l):
                print '  ',
            print u'%s: %s' % (k['name'], k['value'])
        for section in self.sections:
            for x in xrange(l):
                print '  ',
            print u'%s:' % section.name
            section.build(l + 1)


class Section(Builder):
    keys = {}
    sections = []


class TextBuilder(Builder):
    pass
