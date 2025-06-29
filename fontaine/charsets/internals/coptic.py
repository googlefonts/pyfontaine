class Charset:
    common_name = "Coptic"
    native_name = "Ⲙⲉⲧⲣⲉⲙ̀ⲛⲭⲏⲙⲓ"
    key = 0x03E2
    abbreviation = "COPT"
    glyphs = (
        list(range(0x03E2, 0x03EF))
        + list(range(0x2C80, 0x2CB1))
        + list(range(0x2CB2, 0x2CDB))
        + list(range(0x2CDC, 0x2CE3))
        + list(range(0x2CE4, 0x2CEA))
        + list(range(0x2CF9, 0x2CFC))
        + [0x2CFD, 0x2CFE, 0x2CFF]
    )
