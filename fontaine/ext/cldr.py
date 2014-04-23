# -*- coding utf-8 -*-
from fontaine.ext.base import BaseExt, PackageRequiredException

try:
    import icu
except ImportError:
    package = "[PyICU](https://pypi.python.org/pypi/PyICU)"
    raise PackageRequiredException('Please install %s' % package)


class Extension(BaseExt):

    extension_name = 'cldr'

    @staticmethod
    def to_charmap(locale):
        glyphs = []

        try:
            unicodeset = icu.LocaleData(locale.getName()).getExemplarSet()
        except AttributeError:
            return []
        iter = icu.UnicodeSetIterator(unicodeset)
        for char in iter:
            try:
                glyphs.append(ord(char))
            except TypeError:  # , ex:
                # print char, '=', char[0], char[1], ex
                pass
        return glyphs

    @staticmethod
    def __getcharmaps__():
        for key, locale in icu.Locale.getAvailableLocales().items():
            yield type('Charmap', (object,),
                       dict(glyphs=Extension.to_charmap(locale),
                            common_name='CLDR ' + locale.getDisplayName(),
                            native_name='', abbreviation=locale))
