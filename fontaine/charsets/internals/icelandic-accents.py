# -*- coding: utf-8 -*-
class Charset:
    common_name = u'Icelandic Accents'
    native_name = u'Íslenska Akcenty'
    key = ord(u'þ')
    icelandicAccents = u"ÁáÐðÉéÍíÓóÚúÝýÞþÆæÖö"
    abbreviation = 'ISLA'
    glyphs = map(ord, icelandicAccents)