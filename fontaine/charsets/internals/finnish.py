# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Full Finnish Alphabet'
    native_name = u'Koko Suomi Alphabet'
    key = ord(u'Ä')
    abbreviation = 'FIN'
    finnishAlphabet = u"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZzÅåÄäÖö"
    glyphs = map(ord, finnishAlphabet)
