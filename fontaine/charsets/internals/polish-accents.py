class Charset:
    common_name = "Polish Accents"
    native_name = "Polskie Akcenty"
    key = ord("ł")
    polishAccents = "ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    abbreviation = "PLKA"
    glyphs = map(ord, polishAccents)
