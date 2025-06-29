class Charset:
    common_name = "Google Fonts: Extras"
    native_name = ""

    def glyphs(self):
        glyphs = [0xE0FF]  # PUA: Font logo
        glyphs += [0xEFFD]  # PUA: Font version number
        glyphs += [
            0xF000
        ]  # PUA: font ppem size indicator: run `ftview -f 1255 10 Ubuntu-Regular.ttf` to see it in action!
        return glyphs
