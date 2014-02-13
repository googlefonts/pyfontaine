# -*- coding: utf-8 -*-
class CharmapAccents:

    common_name = u'Polish Accents'
    native_name = u'Polskie Akcenty'
    key = ord(u'ł')
    polishAccents = u"ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    abbreviation = 'PLK'
    glyphs = map(ord, polishAccents)


class CharmapFull:
    # use a class name unique in the file
    common_name = u'Full Polish Alphabet'
    native_name = u'Pełny Polski Alfabet'
    key = ord(u'Ł')
    abbreviation = 'PLK'
    polishAlphabet = u"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)


# Register of custom charmap class. By default it should contain class
# named `Charmap`. If this class does not contain that we have to register
# our class manually. Make sure you import library
#
# from fontaine.cmap import library

from fontaine.cmap import library

library.register(CharmapFull)
library.register(CharmapAccents)
