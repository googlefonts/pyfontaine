import re
import requests

from fontaine.ext.base import BaseExt


SOURCE_URL = 'http://www.unicode.org/Public/UNIDATA/Blocks.txt'


class UniBlock(BaseExt):

    @staticmethod
    def __getcharmaps__():
        req = requests.get(SOURCE_URL)

        regex = re.compile('^([\da-f]+)..([\da-f]+);\s*(.*)$', re.I | re.U)
        for line in req.content.split('\n'):
            m = regex.match(line.strip())
            # 100000..10FFFF; Supplementary Private Use Area-B
            if not m:
                continue

            glyphlist = '0x%s-0x%s' % (m.group(1), m.group(2))
            unicodes = UniBlock.convert_to_list_of_unicodes(glyphlist)
            yield type('Charmap', (object,),
                       dict(glyphs=unicodes,
                            common_name=u'Unicode Block: %s' % m.group(3),
                            native_name=''))
