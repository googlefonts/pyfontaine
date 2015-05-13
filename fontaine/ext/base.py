import os.path as op
import re


def cmp(val):
    return bool(re.match('0x[0-9A-Fa-f]+\-0x[0-9A-Fa-f]+', val))


class PackageRequiredException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


class BaseExt(object):

    CHARACTER_SET_PATH = op.realpath(op.join(op.dirname(__file__), '..', 'charsets'))

    @staticmethod
    def convert_to_list_of_unicodes(string):
        codes = string.split(',')

        replace = filter(cmp, codes)
        for r in replace:
            start, end = r.split('-')
            rng = range(int(start, 16), int(end, 16) + 1)
            exp = ','.join(map(lambda x: '0x' + str.lower('%04x' % x), rng))
            string = string.replace(r, exp)

        return map(lambda x: int(x, 16),
                   filter(lambda x: x != '', string.split(',')))

    @classmethod
    def get_charsets(cls):
        return cls.__getcharsets__()
