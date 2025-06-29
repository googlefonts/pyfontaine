class Charset:
    common_name = "Basic Cyrillic"
    native_name = "Кири́ллица"
    abbreviation = "CYRL"
    glyphs = list(range(0x0400, 0x045F))
    glyphs += [
        0x0490,
        0x0491,
        0x04B0,
        0x04B1,
        0x2116,
    ]
