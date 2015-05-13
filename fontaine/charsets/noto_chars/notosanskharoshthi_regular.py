# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansKharoshthi-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10A01)  #glyph00005	KHAROSHTHI VOWEL SIGN I
        chars.append(0x10A02)  #glyph00006	KHAROSHTHI VOWEL SIGN U
        chars.append(0x10A03)  #glyph00007	KHAROSHTHI VOWEL SIGN VOCALIC R
        chars.append(0x10A05)  #glyph00008	KHAROSHTHI VOWEL SIGN E
        chars.append(0x10A06)  #glyph00009	KHAROSHTHI VOWEL SIGN O
        chars.append(0x10A41)  #glyph00053	KHAROSHTHI DIGIT TWO
        chars.append(0x10A0C)  #glyph00010	KHAROSHTHI VOWEL LENGTH MARK
        chars.append(0x000D)  #uni000D	????
        chars.append(0x10A0E)  #glyph00012	KHAROSHTHI SIGN ANUSVARA
        chars.append(0x10A0F)  #glyph00013	KHAROSHTHI SIGN VISARGA
        chars.append(0x10A10)  #glyph00014	KHAROSHTHI LETTER KA
        chars.append(0x10A11)  #glyph00015	KHAROSHTHI LETTER KHA
        chars.append(0x10A12)  #glyph00016	KHAROSHTHI LETTER GA
        chars.append(0x10A13)  #glyph00017	KHAROSHTHI LETTER GHA
        chars.append(0x10A15)  #glyph00018	KHAROSHTHI LETTER CA
        chars.append(0x10A16)  #glyph00019	KHAROSHTHI LETTER CHA
        chars.append(0x10A17)  #glyph00020	KHAROSHTHI LETTER JA
        chars.append(0x10A19)  #glyph00021	KHAROSHTHI LETTER NYA
        chars.append(0x10A1A)  #glyph00022	KHAROSHTHI LETTER TTA
        chars.append(0x10A1B)  #glyph00023	KHAROSHTHI LETTER TTHA
        chars.append(0x10A1C)  #glyph00024	KHAROSHTHI LETTER DDA
        chars.append(0x10A1D)  #glyph00025	KHAROSHTHI LETTER DDHA
        chars.append(0x10A1E)  #glyph00026	KHAROSHTHI LETTER NNA
        chars.append(0x10A1F)  #glyph00027	KHAROSHTHI LETTER TA
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10A21)  #glyph00029	KHAROSHTHI LETTER DA
        chars.append(0x10A22)  #glyph00030	KHAROSHTHI LETTER DHA
        chars.append(0x10A23)  #glyph00031	KHAROSHTHI LETTER NA
        chars.append(0x10A24)  #glyph00032	KHAROSHTHI LETTER PA
        chars.append(0x10A25)  #glyph00033	KHAROSHTHI LETTER PHA
        chars.append(0x10A26)  #glyph00034	KHAROSHTHI LETTER BA
        chars.append(0x10A27)  #glyph00035	KHAROSHTHI LETTER BHA
        chars.append(0x10A28)  #glyph00036	KHAROSHTHI LETTER MA
        chars.append(0x10A29)  #glyph00037	KHAROSHTHI LETTER YA
        chars.append(0x10A2A)  #glyph00038	KHAROSHTHI LETTER RA
        chars.append(0x10A2B)  #glyph00039	KHAROSHTHI LETTER LA
        chars.append(0x10A2C)  #glyph00040	KHAROSHTHI LETTER VA
        chars.append(0x10A2D)  #glyph00041	KHAROSHTHI LETTER SHA
        chars.append(0x10A2E)  #glyph00042	KHAROSHTHI LETTER SSA
        chars.append(0x10A2F)  #glyph00043	KHAROSHTHI LETTER SA
        chars.append(0x10A30)  #glyph00044	KHAROSHTHI LETTER ZA
        chars.append(0x10A31)  #glyph00045	KHAROSHTHI LETTER HA
        chars.append(0x10A32)  #glyph00046	KHAROSHTHI LETTER KKA
        chars.append(0x10A33)  #glyph00047	KHAROSHTHI LETTER TTTHA
        chars.append(0x10A20)  #glyph00028	KHAROSHTHI LETTER THA
        chars.append(0x10A38)  #glyph00048	KHAROSHTHI SIGN BAR ABOVE
        chars.append(0x10A39)  #glyph00049	KHAROSHTHI SIGN CAUDA
        chars.append(0x10A3A)  #glyph00050	KHAROSHTHI SIGN DOT BELOW
        chars.append(0x10A3F)  #glyph00051	KHAROSHTHI VIRAMA
        chars.append(0x10A40)  #glyph00052	KHAROSHTHI DIGIT ONE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10A42)  #glyph00054	KHAROSHTHI DIGIT THREE
        chars.append(0x10A43)  #glyph00055	KHAROSHTHI DIGIT FOUR
        chars.append(0x10A44)  #glyph00056	KHAROSHTHI NUMBER TEN
        chars.append(0x10A45)  #glyph00057	KHAROSHTHI NUMBER TWENTY
        chars.append(0x10A46)  #glyph00058	KHAROSHTHI NUMBER ONE HUNDRED
        chars.append(0x10A47)  #glyph00059	KHAROSHTHI NUMBER ONE THOUSAND
        chars.append(0x10A0D)  #glyph00011	KHAROSHTHI SIGN DOUBLE RING BELOW
        chars.append(0x10A50)  #glyph00060	KHAROSHTHI PUNCTUATION DOT
        chars.append(0x10A51)  #glyph00061	KHAROSHTHI PUNCTUATION SMALL CIRCLE
        chars.append(0x10A52)  #glyph00062	KHAROSHTHI PUNCTUATION CIRCLE
        chars.append(0x10A53)  #glyph00063	KHAROSHTHI PUNCTUATION CRESCENT BAR
        chars.append(0x10A54)  #glyph00064	KHAROSHTHI PUNCTUATION MANGALAM
        chars.append(0x10A55)  #glyph00065	KHAROSHTHI PUNCTUATION LOTUS
        chars.append(0x10A00)  #glyph00004	KHAROSHTHI LETTER A
        chars.append(0x10A57)  #glyph00067	KHAROSHTHI PUNCTUATION DOUBLE DANDA
        chars.append(0x10A58)  #glyph00068	KHAROSHTHI PUNCTUATION LINES
        chars.append(0x10A56)  #glyph00066	KHAROSHTHI PUNCTUATION DANDA
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


