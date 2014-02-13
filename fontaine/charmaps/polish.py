# -*- coding: utf-8 -*-
# import library manually so we can have 2 Charmap classes in 1 file
from fontaine.cmap import library

class CharmapFull: # use a class name unique in the file
    common_name = u'Full Polish Alphabet'
    native_name = u'Pełny Polski Alfabet'
    key = ord(u'Ł')
    polishAlphabet = u"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)    
library.register(CharmapFull)
# register the Charmap manually as there are 2 in 1 file

class CharmapAccents:
    common_name = u'Polish Accents'
    native_name = u'Polskie Akcenty'
    key = ord(u'ł')
    polishAccents = u"ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    glyphs = map(ord, polishAccents)
library.register(CharmapAccents)
