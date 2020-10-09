# -*- coding utf-8 -*-
from fontaine.ext.base import BaseExt, PackageRequiredException

try:
    import hyperglot.languages
except ImportError:
    package = ("hyperglot <https://github.com/rosettatype/hyperglot> to "
               "enable hyperglot, perhaps with: pip install "
               "git+https://github.com/rosettatype/hyperglot")
    raise PackageRequiredException('Please install %s' % package)


class Extension(BaseExt):

    extension_name = 'hyperglot'
    description = 'Rosetta Type collection'

    from hyperglot.languages import Languages
    db = Languages()

    @staticmethod
    def to_charset(orthography):
        glyphs = orthography.get("base", [])
        glyphs.extend(orthography.get("numerals", []))
        glyphs.extend([g.upper() for g in glyphs
            if g.upper() != g and len(g.upper()) == 1 ])
            # Length check is necessary because Unicode ß casing wrong
        return [ord(g) for g in set(glyphs)]

    @staticmethod
    def make_locale(key,locale, orth_ix):
        orthography = locale["orthographies"][orth_ix]
        return type('Charset', (object,),
               dict(glyphs=Extension.to_charset(orthography),
                    common_name='Hyperglot ' + locale.get("name"),
                    native_name=orthography.get("autonym",""),
                    abbreviation=key,
                    short_name='hyperglot-{}'.format(key)))

    @staticmethod
    def __getcharsets__():
        for key, locale in Extension.db.items():
            if len(locale["orthographies"]) == 1:
                yield Extension.make_locale(key, locale, 0)
            else:
                for ix in range(0,len(locale["orthographies"])):
                    yield Extension.make_locale(key+"-"+str(1+ix), locale, ix)
