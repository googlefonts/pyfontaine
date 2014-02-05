import fontaine
import os
import os.path


class Fontconfig:

    @staticmethod
    def iterate_orth():
        dirname = os.path.dirname(fontaine.__file__)
        dirorth = os.path.join(dirname, 'charmaps', 'fontconfig', 'fc-lang')
        for fileorth in os.listdir(dirorth):
            if os.path.splitext(fileorth)[1] == '.orth':
                yield os.path.join(dirorth, fileorth)

    @staticmethod
    def get_orth_charmap(orthfile):
        return [], 'en'
