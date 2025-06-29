from fontaine.namelist import codepointsInNamelist


class Charset:
    common_name = "Google Fonts: Latin Expert"
    native_name = ""
    abbreviation = "LAT"

    def glyphs(self):
        glyphs = codepointsInNamelist(
            "charsets/internals/google_glyphsets/GF-latin-expert_unique-glyphs.nam"
        )
        return glyphs
