# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Full Polish Alphabet'
    native_name = u'Pełny Polski Alfabet'
    key = ord(u'Ł')
    abbreviation = 'PLK'
    polishAlphabet = u"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)
