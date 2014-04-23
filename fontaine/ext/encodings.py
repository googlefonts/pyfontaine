import os
import re

from fontaine.ext.base import BaseExt


class Extension(BaseExt):

    extension_name = 'encodings'

    @staticmethod
    def __getcharmaps__():
        path = os.path.join(BaseExt.CHARACTER_SET_PATH, 'unicode')

        for filepath in os.listdir(path):
            common_name = os.path.basename(filepath)
            common_name = common_name.replace('unicodes-', '')
            common_name = os.path.splitext(os.path.basename(filepath))[0]

            with open(os.path.join(path, filepath)) as fp:
                contents = fp.read()

            lines = contents.split('\n')
            unicodes = []
            for ch in lines:
                if not ch:
                    continue
                unicodes.append(int(ch.lstrip('U+'), 16))
            yield type('Charmap', (object,),
                       dict(glyphs=unicodes,
                            common_name=u'Encodings %s' % common_name,
                            native_name=''))
