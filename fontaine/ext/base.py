import re


def cmp(val):
    return bool(re.match('0x[0-9A-Fa-f]+\-0x[0-9A-Fa-f]+', val))


class BaseExt(object):

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
    def get_charmaps(cls):
        return cls.__getcharmaps__()
