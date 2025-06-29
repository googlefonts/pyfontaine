class Charset:
    common_name = "Full Danish Alphabet"
    native_name = "Fuld Dansk Alfabet"
    key = ord("Å")
    abbreviation = "DAN"
    danishAlphabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    glyphs = map(ord, danishAlphabet)
