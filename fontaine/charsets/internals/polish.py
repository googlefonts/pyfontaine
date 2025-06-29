class Charset:
    common_name = "Full Polish Alphabet"
    native_name = "Pełny Polski Alfabet"
    key = ord("Ł")
    abbreviation = "PLK"
    polishAlphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    glyphs = map(ord, polishAlphabet)
