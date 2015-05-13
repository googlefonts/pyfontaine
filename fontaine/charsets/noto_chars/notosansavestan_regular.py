# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansAvestan-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10B01)  #glyph00007	AVESTAN LETTER AA
        chars.append(0x10B02)  #glyph00008	AVESTAN LETTER AO
        chars.append(0x10B03)  #glyph00009	AVESTAN LETTER AAO
        chars.append(0x10B04)  #glyph00010	AVESTAN LETTER AN
        chars.append(0x10B05)  #glyph00011	AVESTAN LETTER AAN
        chars.append(0x10B06)  #glyph00012	AVESTAN LETTER AE
        chars.append(0x10B07)  #glyph00013	AVESTAN LETTER AEE
        chars.append(0x10B08)  #glyph00014	AVESTAN LETTER E
        chars.append(0x10B09)  #glyph00015	AVESTAN LETTER EE
        chars.append(0x10B0A)  #glyph00016	AVESTAN LETTER O
        chars.append(0x10B0B)  #glyph00017	AVESTAN LETTER OO
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x10B0E)  #glyph00020	AVESTAN LETTER U
        chars.append(0x10B0F)  #glyph00021	AVESTAN LETTER UU
        chars.append(0x10B10)  #glyph00022	AVESTAN LETTER KE
        chars.append(0x10B11)  #glyph00023	AVESTAN LETTER XE
        chars.append(0x10B12)  #glyph00024	AVESTAN LETTER XYE
        chars.append(0x10B13)  #glyph00025	AVESTAN LETTER XVE
        chars.append(0x10B14)  #glyph00026	AVESTAN LETTER GE
        chars.append(0x10B15)  #glyph00027	AVESTAN LETTER GGE
        chars.append(0x10B16)  #glyph00028	AVESTAN LETTER GHE
        chars.append(0x10B17)  #glyph00029	AVESTAN LETTER CE
        chars.append(0x10B18)  #glyph00030	AVESTAN LETTER JE
        chars.append(0x10B19)  #glyph00031	AVESTAN LETTER TE
        chars.append(0x10B1A)  #glyph00032	AVESTAN LETTER THE
        chars.append(0x10B1B)  #glyph00033	AVESTAN LETTER DE
        chars.append(0x10B1C)  #glyph00034	AVESTAN LETTER DHE
        chars.append(0x10B1D)  #glyph00035	AVESTAN LETTER TTE
        chars.append(0x10B1E)  #glyph00036	AVESTAN LETTER PE
        chars.append(0x10B1F)  #glyph00037	AVESTAN LETTER FE
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10B21)  #glyph00039	AVESTAN LETTER BHE
        chars.append(0x10B22)  #glyph00040	AVESTAN LETTER NGE
        chars.append(0x10B23)  #glyph00041	AVESTAN LETTER NGYE
        chars.append(0x10B24)  #glyph00042	AVESTAN LETTER NGVE
        chars.append(0x10B25)  #glyph00043	AVESTAN LETTER NE
        chars.append(0x10B26)  #glyph00044	AVESTAN LETTER NYE
        chars.append(0x10B27)  #glyph00045	AVESTAN LETTER NNE
        chars.append(0x10B28)  #glyph00046	AVESTAN LETTER ME
        chars.append(0x10B29)  #glyph00047	AVESTAN LETTER HME
        chars.append(0x10B2A)  #glyph00048	AVESTAN LETTER YYE
        chars.append(0x10B2B)  #glyph00049	AVESTAN LETTER YE
        chars.append(0x10B2C)  #glyph00050	AVESTAN LETTER VE
        chars.append(0x10B2D)  #glyph00051	AVESTAN LETTER RE
        chars.append(0x10B2E)  #glyph00052	AVESTAN LETTER LE
        chars.append(0x10B2F)  #glyph00053	AVESTAN LETTER SE
        chars.append(0x10B30)  #glyph00054	AVESTAN LETTER ZE
        chars.append(0x10B31)  #glyph00055	AVESTAN LETTER SHE
        chars.append(0x10B32)  #glyph00056	AVESTAN LETTER ZHE
        chars.append(0x10B33)  #glyph00057	AVESTAN LETTER SHYE
        chars.append(0x10B34)  #glyph00058	AVESTAN LETTER SSHE
        chars.append(0x10B35)  #glyph00059	AVESTAN LETTER HE
        chars.append(0x10B39)  #glyph00060	AVESTAN ABBREVIATION MARK
        chars.append(0x10B3A)  #glyph00061	TINY TWO DOTS OVER ONE DOT PUNCTUATION
        chars.append(0x10B3B)  #glyph00062	SMALL TWO DOTS OVER ONE DOT PUNCTUATION
        chars.append(0x10B3C)  #glyph00063	LARGE TWO DOTS OVER ONE DOT PUNCTUATION
        chars.append(0x10B3D)  #glyph00064	LARGE ONE DOT OVER TWO DOTS PUNCTUATION
        chars.append(0x10B3E)  #glyph00065	LARGE TWO RINGS OVER ONE RING PUNCTUATION
        chars.append(0x10B3F)  #glyph00066	LARGE ONE RING OVER TWO RINGS PUNCTUATION
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10B0C)  #glyph00018	AVESTAN LETTER I
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x10B20)  #glyph00038	AVESTAN LETTER BE
        chars.append(0x10B00)  #glyph00006	AVESTAN LETTER A
        chars.append(0x10B0D)  #glyph00019	AVESTAN LETTER II
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


