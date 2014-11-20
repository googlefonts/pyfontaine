# -*- coding: utf-8 -*-
class Charmap:
    common_name = u'Full Danish Alphabet'
    native_name = u'Fuld Dansk Alfabet'
    key = ord(u'Å')
    abbreviation = 'DAN'
    danishAlphabet = u"abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    glyphs = map(ord, danishAlphabet)
