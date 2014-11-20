# -*- coding: utf-8 -*-
class Charmap:
    common_name = u'Full Slovak Alphabet'
    native_name = u'Slovenský Abeceda'
    key = ord(u'Č')
    abbreviation = 'SLK'
    polishAlphabet = u"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÄÉÍÓÔÚÝáäéíóôúýČčĎďĹĺĽľŇňŔŕŠšŤťŽž"
    glyphs = map(ord, slovakAlphabet)

# class names must be unique in each file
class CharmapAccents:
    common_name = u'Slovak Accents'
    native_name = u'Slovenský Akcenty'
    key = ord(u'č')
    polishAccents = u"ÁÄÉÍÓÔÚÝáäéíóôúýČčĎďĹĺĽľŇňŔŕŠšŤťŽž"
    abbreviation = 'SLKA'
    glyphs = map(ord, slovakAccents)

# Class objects named Charmap are registed automatically.
# Since we have a 2nd Charmap with another name,
# we must register this class manually
from fontaine.cmap import library
library.register(CharmapAccents)


