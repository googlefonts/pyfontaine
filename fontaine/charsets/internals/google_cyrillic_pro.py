from fontaine.namelist import codepointsInNamelist


class Charset:
    common_name = "Google Fonts: Cyrillic Pro"
    native_name = ""
    abbreviation = "CYRL"

    def glyphs(self):
        glyphs = codepointsInNamelist(
            "charsets/internals/google_glyphsets/Cyrillic/GF-cyrillic-pro_unique-glyphs.nam"
        )
        return glyphs
