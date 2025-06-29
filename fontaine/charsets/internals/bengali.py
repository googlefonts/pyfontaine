class Charset:
    common_name = "Bengali"
    native_name = "বাংলা"
    abbreviation = "BENG"
    key = 0x0985
    glyphs = (
        list(range(0x0981, 0x0983))
        + list(range(0x0985, 0x098C))
        + list(range(0x098F, 0x0990))
        + list(range(0x0993, 0x09A8))
        + list(range(0x09AA, 0x09B0))
        + [0x09B2]
        + list(range(0x09B6, 0x09B9))
        + [0x09BC]
        + list(range(0x09BE, 0x09C4))
        + list(range(0x09C7, 0x09C8))
        + list(range(0x09CB, 0x09CD))
        + [0x09D7]
        + list(range(0x09DC, 0x09DD))
        + list(range(0x09DF, 0x09E3))
        + list(range(0x09E6, 0x09FA))
    )
