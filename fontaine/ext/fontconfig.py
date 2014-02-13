import fontaine
import os
import os.path
import re

from fontaine.ext.base import BaseExt


UNICODE_VALUE_REGEX = re.compile('^(?P<bx>0x)?(?P<begr>[0-9a-f]+)(\-(?!0x)(?P<endr>[0-9a-f]+))?', re.I)
INCLUDE_REGEX = re.compile('include ([\w]+.orth)', re.I | re.U | re.S)


dirname = os.path.dirname(fontaine.__file__)
ORTH_SOURCE_DIR = os.path.join(dirname, 'charmaps', 'fontconfig', 'fc-lang')


class Extension(BaseExt):

    extension_name = 'fontconfig'

    @staticmethod
    def __getcharmaps__():
        for ext in Extension.iterate_orth():
            unicodes, common_name, abbr = Extension.get_orth_charmap(ext)

            if not common_name:
                continue

            yield type('Charmap', (object,),
                       dict(glyphs=unicodes, common_name=common_name,
                            native_name='', abbreviation=abbr))

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
        common_name_regex = re.compile(u'#\s+(\w+)\s*\((%s)\)' % fn, re.I | re.U | re.S)

        common_name_match = common_name_regex.search(content)
        if common_name_match:
            common_name = u'fontconfig %s (%s) from %s.orth'
            common_name = common_name % (common_name_match.group(1).decode('utf-8', 'ignore'),
                                         common_name_match.group(2), fn)
        else:
            return [], '', ''

        for line in content.split('\n'):
            unicode_match = UNICODE_VALUE_REGEX.match(line.strip())
            if not unicode_match:
                continue

            value = '0x' + unicode_match.group('begr')
            if unicode_match.group('endr'):
                value = value + '-0x' + unicode_match.group('endr')
            glyphs.append(value)

        regex = INCLUDE_REGEX.search(content)
        if regex:
            include = os.path.join(ORTH_SOURCE_DIR, regex.group(1))

            with open(include) as fp:
                content = fp.read()
            name, abbr, ng = Extension.get_string_glyphlist(include, content)
            if name and ng:
                glyphs += ng.split(',')
                common_name += u' + %s' % name

        return common_name, common_name_match.group(2), ','.join(glyphs)

    @staticmethod
    def get_orth_charmap(orthfile):
        with open(orthfile) as fp:
            content = fp.read()

        name, abbr, glyphlist = Extension.get_string_glyphlist(orthfile, content)

        if not name:
            return [], '', ''

        return Extension.convert_to_list_of_unicodes(glyphlist), name, abbr
