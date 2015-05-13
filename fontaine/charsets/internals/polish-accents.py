# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Polish Accents'
    native_name = u'Polskie Akcenty'
    key = ord(u'ł')
    polishAccents = u"ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    abbreviation = 'PLKA'
    glyphs = map(ord, polishAccents)