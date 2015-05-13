# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansGothic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0304)  #uni0304	COMBINING MACRON
        chars.append(0x0305)  #uni0305	COMBINING OVERLINE
        chars.append(0x0308)  #uni0308	COMBINING DIAERESIS
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0331)  #uni0331	COMBINING MACRON BELOW
        chars.append(0x00B7)  #periodcentered	MIDDLE DOT
        chars.append(0x003A)  #colon	COLON
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0304)  #uni0304	COMBINING MACRON
        chars.append(0x0305)  #uni0305	COMBINING OVERLINE
        chars.append(0x10341)  #glyph00027	GOTHIC LETTER NINETY
        chars.append(0x0308)  #uni0308	COMBINING DIAERESIS
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0331)  #uni0331	COMBINING MACRON BELOW
        chars.append(0x10330)  #glyph00010	GOTHIC LETTER AHSA
        chars.append(0x10331)  #glyph00011	GOTHIC LETTER BAIRKAN
        chars.append(0x10332)  #glyph00012	GOTHIC LETTER GIBA
        chars.append(0x10333)  #glyph00013	GOTHIC LETTER DAGS
        chars.append(0x10334)  #glyph00014	GOTHIC LETTER AIHVUS
        chars.append(0x10335)  #glyph00015	GOTHIC LETTER QAIRTHRA
        chars.append(0x10336)  #glyph00016	GOTHIC LETTER IUJA
        chars.append(0x10337)  #glyph00017	GOTHIC LETTER HAGL
        chars.append(0x10338)  #glyph00018	GOTHIC LETTER THIUTH
        chars.append(0x10339)  #glyph00019	GOTHIC LETTER EIS
        chars.append(0x003A)  #colon	COLON
        chars.append(0x1033B)  #glyph00021	GOTHIC LETTER LAGUS
        chars.append(0x1033C)  #glyph00022	GOTHIC LETTER MANNA
        chars.append(0x1033D)  #glyph00023	GOTHIC LETTER NAUTHS
        chars.append(0x1033E)  #glyph00024	GOTHIC LETTER JER
        chars.append(0x1033F)  #glyph00025	GOTHIC LETTER URUS
        chars.append(0x10340)  #glyph00026	GOTHIC LETTER PAIRTHRA
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10342)  #glyph00028	GOTHIC LETTER RAIDA
        chars.append(0x10343)  #glyph00029	GOTHIC LETTER SAUIL
        chars.append(0x10344)  #glyph00030	GOTHIC LETTER TEIWS
        chars.append(0x10345)  #glyph00031	GOTHIC LETTER WINJA
        chars.append(0x10346)  #glyph00032	GOTHIC LETTER FAIHU
        chars.append(0x10347)  #glyph00033	GOTHIC LETTER IGGWS
        chars.append(0x10348)  #glyph00034	GOTHIC LETTER HWAIR
        chars.append(0x10349)  #glyph00035	GOTHIC LETTER OTHAL
        chars.append(0x1034A)  #glyph00036	GOTHIC LETTER NINE HUNDRED
        chars.append(0x00B7)  #periodcentered	MIDDLE DOT
        chars.append(0x1033A)  #glyph00020	GOTHIC LETTER KUSMA
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


