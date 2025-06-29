class Charset:
    common_name = "Full Finnish Alphabet"
    native_name = "Koko Suomi Alphabet"
    key = ord("Ä")
    abbreviation = "FIN"
    finnishAlphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZzÅåÄäÖö"
    glyphs = map(ord, finnishAlphabet)
