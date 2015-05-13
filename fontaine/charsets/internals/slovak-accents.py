# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Slovak Accents'
    native_name = u'Slovenský Akcenty'
    key = ord(u'č')
    slovakAccents = u"ÁÄÉÍÓÔÚÝáäéíóôúýČčĎďĹĺĽľŇňŔŕŠšŤťŽž"
    abbreviation = 'SLKA'
    glyphs = map(ord, slovakAccents)
