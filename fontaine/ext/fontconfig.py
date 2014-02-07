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
INCLUDE_REGEX = re.compile('^include ([\w.]+)', re.I | re.U)


def cmp(val):
    return bool(re.match('0x[0-9A-Fa-f]+\-0x[0-9A-Fa-f]+', val))


dirname = os.path.dirname(fontaine.__file__)
ORTH_SOURCE_DIR = os.path.join(dirname, 'charmaps', 'fontconfig', 'fc-lang')


class Fontconfig:

    @staticmethod
    def iterate_orth():
        if not os.path.exists(ORTH_SOURCE_DIR):
            return []

        result = []
        for fileorth in os.listdir(ORTH_SOURCE_DIR):
            if os.path.splitext(fileorth)[1] == '.orth':
                result.append(os.path.join(ORTH_SOURCE_DIR, fileorth))
        return result

    @staticmethod
    def get_string_glyphlist(filename, content):
        glyphs = []

        fn, ext = os.path.splitext(os.path.basename(filename))
        common_name_regex = re.compile(u'#\s+(\w+)\s*\((%s)\)$' % fn, re.I | re.U)

        common_name = ''
        include = ''

        for line in content.split('\n'):
            common_name_match = common_name_regex.match(line)
            if common_name_match:
                common_name = u'fontconfig %s (%s) from %s.orth'
                common_name = common_name % (common_name_match.group(1).decode('utf-8', 'ignore'),
                                             common_name_match.group(2), fn)

            unicode_match = UNICODE_VALUE_REGEX.match(line.strip())
            if unicode_match:
                value = '0x' + unicode_match.group('begr')
                if unicode_match.group('endr'):
                    value = value + '-0x' + unicode_match.group('endr')
                glyphs.append(value)

            regex = INCLUDE_REGEX.match(line)
            if regex:
                include = os.path.join(ORTH_SOURCE_DIR, regex.group(1))

        if include and common_name:
            with open(include) as fp:
                content = fp.read()
            name, ng = Fontconfig.get_string_glyphlist(include, content)
            if name and ng:
                glyphs += ng.split(',')
                common_name += u' + %s' % name

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
