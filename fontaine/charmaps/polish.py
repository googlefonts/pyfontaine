# -*- coding: utf-8 -*-
class Charmap:
    common_name = u'Full Polish Alphabet'
    native_name = u'Pełny Polski Alfabet'
    key = ord(u'Ł')
    abbreviation = 'PLK'
    polishAlphabet = u"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)

# class names must be unique in each file
class CharmapAccents:
    common_name = u'Polish Accents'
    native_name = u'Polskie Akcenty'
    key = ord(u'ł')
    polishAccents = u"ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    abbreviation = 'PLK'
    glyphs = map(ord, polishAccents)

# Class objects named Charmap are registed automatically.
# Since we have a 2nd Charmap with another name,
# we must register this class manually
from fontaine.cmap import library
library.register(CharmapAccents)
