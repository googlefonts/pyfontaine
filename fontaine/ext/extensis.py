from __future__ import print_function

from lxml import etree

import re
import requests


EXTENSIS_LANG_XML = 'http://blog-cache4.webink.com/assets/Languages.txt'


class Extensis:

    def __init__(self, unichar):
        self.unicodechar = int(unichar, 16)

    def findlanguages(self):
        response = requests.get(EXTENSIS_LANG_XML)
        if response.status_code != 200:
            return ''

        def cmp(val):
            return bool(re.match('0x[0-9A-Fa-f]+\-0x[0-9A-Fa-f]+', val))

        doc = etree.fromstring(response.content)
        codepoints = doc.findall('.//scanning-codepoints')
        languages = []
        for codepoint in codepoints:
            result = ''.join(map(str.strip, codepoint.text.lower().split('\n')))
            codes = result.split(',')

            replace = filter(cmp, codes)
            for r in replace:
                start, end = r.split('-')
                rng = range(int(start, 16), int(end, 16) + 1)
                result = result.replace(r, ','.join(map(lambda x: '0x' + str.lower('%04x' % x), rng)))

            unicodes = map(lambda x: int(x, 16),
                           filter(lambda x: x != '', result.split(',')))

            if self.unicodechar in unicodes:
                try:
                    languages.append(codepoint.getparent().attrib['name'])
                except (KeyError, ValueError):
                    pass

        return ', '.join(languages)


if __name__ == '__main__':

    # assert Extensis(0x0531).findlanguages() == 'Armenian'
    assert Extensis('0x0531').findlanguages() == 'Armenian'
