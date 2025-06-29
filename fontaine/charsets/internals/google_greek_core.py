from fontaine.namelist import codepointsInNamelist


class Charset:
    common_name = "Google Fonts: Greek Core"
    native_name = ""
    abbreviation = "GREK"

    def glyphs(self):
        glyphs = codepointsInNamelist(
            "charsets/internals/google_glyphsets/Greek/GF-greek-core.nam"
        )
        return glyphs
