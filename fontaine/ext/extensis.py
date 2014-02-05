from __future__ import print_function

from lxml import etree

import re
import requests


EXTENSIS_LANG_XML = 'http://blog-cache4.webink.com/assets/languages19.txt'


def cmp(val):
    return bool(re.match('0x[0-9A-Fa-f]+\-0x[0-9A-Fa-f]+', val))


class Extensis:

    @staticmethod
    def get_codepoints():
        """ Return all XML <scanning-codepoints> in received XML """
        response = requests.get(EXTENSIS_LANG_XML)
        if response.status_code != 200:
            return []

        content = re.sub('<!--.[^>]*-->', '', response.content)

        doc = etree.fromstring(content.lstrip('`'))
        return doc.findall('.//scanning-codepoints')

    @staticmethod
    def get_unicodes(codepoint):
        """ Return list of unicodes for <scanning-codepoints> """

        result = re.sub('\s', '', codepoint.text)

        # print(codepoint.getparent().attrib['name'], result)
        codes = result.split(',')

        replace = filter(cmp, codes)
        for r in replace:
            start, end = r.split('-')
            rng = range(int(start, 16), int(end, 16) + 1)
            exp = ','.join(map(lambda x: '0x' + str.lower('%04x' % x), rng))
            result = result.replace(r, exp)

        return map(lambda x: int(x, 16),
                   filter(lambda x: x != '', result.split(',')))

    def __init__(self, unichar):
        self.unicodechar = int(unichar, 16)

    def findlanguages(self):
        """ Return string with languages containing passed unicodechar """
        languages = []
        for codepoint in Extensis.get_codepoints():

            if self.unicodechar in Extensis.get_unicodes(codepoint):
                try:
                    languages.append(codepoint.getparent().attrib['name'])
                except (KeyError, ValueError):
                    pass

        return ', '.join(languages)


if __name__ == '__main__':
    assert Extensis('0x0531').findlanguages() == 'Armenian'
