# -*- coding: utf8 -*-
class Charset:

    common_name = "Arabic"
    native_name = u"العربية"
    key = 0x0639  # ARABIC LETTER AIN
    abbreviation = 'ARAB'

    glyphs = \
        list(range(0x0621, 0x063a)) + \
        list(range(0x0640, 0x0652)) + \
        list(range(0x0660, 0x0669))



