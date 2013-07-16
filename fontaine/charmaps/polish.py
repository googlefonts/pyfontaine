# -*- coding: utf-8 -*-
from fontaine.cmap import library

class CharmapFull:
    common_name = u'Full Polish Alphabet'
    native_name = u'Pełny Polski Alfabet'
    key = ord(u'Ł')
    polishAlphabet = u"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)    

class CharmapAccents:
    common_name = u'Polish Accents'
    native_name = u'Polskie Akcenty'
    key = ord(u'ł')
    polishAccents = u"ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    glyphs = map(ord, polishAccents)

library.register(CharmapFull)
library.register(CharmapAccents)