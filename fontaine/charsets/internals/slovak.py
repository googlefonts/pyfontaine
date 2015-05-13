# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Full Slovak Alphabet'
    native_name = u'Slovenský Abeceda'
    key = ord(u'Č')
    abbreviation = 'SLK'
    slovakAlphabet = u"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÄÉÍÓÔÚÝáäéíóôúýČčĎďĹĺĽľŇňŔŕŠšŤťŽž"
    glyphs = map(ord, slovakAlphabet)
