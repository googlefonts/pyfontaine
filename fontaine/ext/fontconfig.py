import fontaine
import os
import os.path
import re


# include gez.orth
# 1238-123f  # xe-xWa
# 1268-126e  # ve-vo
# 1278-127f  # ce-cWa
# 1298-129f  # Ne-NWa
# 12a8       # ea
# 12e0-12e8  # Ze-ZWa
# 1300-1307  # je-jWa
# 1328-132f  # Ce-CWa

UNICODE_VALUE_REGEX = re.compile('^(?P<bx>0x)?(?P<begr>[0-9a-f]+)(\-(?!0x)(?P<endr>[0-9a-f]+))?', re.I)


def cmp(val):
    return bool(re.match('0x[0-9A-Fa-f]+\-0x[0-9A-Fa-f]+', val))


class Fontconfig:

    @staticmethod
    def iterate_orth():
        dirname = os.path.dirname(fontaine.__file__)
        dirorth = os.path.join(dirname, 'charmaps', 'fontconfig', 'fc-lang')
        for fileorth in os.listdir(dirorth):
            if os.path.splitext(fileorth)[1] == '.orth':
                yield os.path.join(dirorth, fileorth)

    @classmethod
    def get_string_glyphlist(cls, filename, content):
        glyphs = []

        fn, ext = os.path.splitext(os.path.basename(filename))
        common_name_regex = re.compile(u'#\s+(\w+)\s*\(%s\)$' % fn, re.I | re.U)

        common_name = ''

        for line in content.split('\n'):
            common_name_match = common_name_regex.match(line)
            if common_name_match:
                common_name = u'Fontconfig %s' % common_name_match.group(1).decode('utf-8', 'ignore')

            unicode_match = UNICODE_VALUE_REGEX.match(line.strip())
            if unicode_match:
                value = '0x' + unicode_match.group('begr')
                if unicode_match.group('endr'):
                    value = value + '-0x' + unicode_match.group('endr')
                glyphs.append(value)
        return common_name, ','.join(glyphs)

    @staticmethod
    def get_orth_charmap(orthfile):
        with open(orthfile) as fp:
            content = fp.read()

        name, glyphlist = Fontconfig.get_string_glyphlist(orthfile, content)

        if not name:
            return [], ''

        codes = glyphlist.split(',')

        replace = filter(cmp, codes)
        for r in replace:
            start, end = r.split('-')
            rng = range(int(start, 16), int(end, 16) + 1)
            exp = ','.join(map(lambda x: '0x' + str.lower('%04x' % x), rng))
            glyphlist = glyphlist.replace(r, exp)

        return map(lambda x: int(x, 16),
                   filter(lambda x: x != '', glyphlist.split(','))), name
