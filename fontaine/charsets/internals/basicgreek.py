class Charset:
    common_name = "Basic Greek"
    native_name = "Ελληνικό αλφάβητο"
    abbreviation = "GREKb"
    key = 0x03A9
    glyphs = (
        [0x0386, 0x0388, 0x0389, 0x038A, 0x038C, 0x038E, 0x038F, 0x0390]
        + list(range(0x0391, 0x03A1))
        + list(range(0x03A3, 0x03A9))
        + list(range(0x03AA, 0x03B0))
        + list(range(0x03B1, 0x03C9))
        + list(range(0x03CA, 0x03CE))
    )
