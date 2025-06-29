class Charset:
    common_name = "Armenian"
    native_name = "Հայերեն"
    key = 0x0561  # ARMENIAN SMALL LETTER AYB
    abbreviation = "ARMN"
    glyphs = (
        list(range(0x0531, 0x0556))
        + list(range(0x0559, 0x055F))
        + list(range(0x0561, 0x0587))
        + [0x589, 0x58A]
    )
