# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'Polish'
    native_name = u'Polski'
    key = ord(u'Ł')
    polishAlphabet = u"AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)    

library.register(Charmap)
