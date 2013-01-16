from fontaine.cmap import library


class Charmap:

    common_name = u'Balinese'
    native_name = u''
    key = 0x1B05

    glyphs = \
        list(xrange(0x1B00, 0x1B4B)) + \
        list(xrange(0x1B50, 0x1B7C))


library.register(Charmap)
