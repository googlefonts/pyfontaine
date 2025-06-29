class Charset:
    common_name = "Cham"
    native_name = ""
    key = 0xAA00
    glyphs = (
        list(range(0xAA00, 0xAA36))
        + list(range(0xAA40, 0xAA4D))
        + list(range(0xAA50, 0xAA59))
        + list(range(0xAA5C, 0xAA5F))
    )
