# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansInscriptionalPahlavi-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10B7F)  #glyph00030	INSCRIPTIONAL PAHLAVI NUMBER ONE THOUSAND
        chars.append(0x10B60)  #glyph00004	INSCRIPTIONAL PAHLAVI LETTER ALEPH
        chars.append(0x10B61)  #glyph00005	INSCRIPTIONAL PAHLAVI LETTER BETH
        chars.append(0x10B62)  #glyph00006	INSCRIPTIONAL PAHLAVI LETTER GIMEL
        chars.append(0x10B63)  #glyph00007	INSCRIPTIONAL PAHLAVI LETTER DALETH
        chars.append(0x10B64)  #glyph00008	INSCRIPTIONAL PAHLAVI LETTER HE
        chars.append(0x10B65)  #glyph00009	INSCRIPTIONAL PAHLAVI LETTER WAW-AYIN-RESH
        chars.append(0x10B66)  #glyph00010	INSCRIPTIONAL PAHLAVI LETTER ZAYIN
        chars.append(0x10B67)  #glyph00011	INSCRIPTIONAL PAHLAVI LETTER HETH
        chars.append(0x10B68)  #glyph00012	INSCRIPTIONAL PAHLAVI LETTER TETH
        chars.append(0x10B69)  #glyph00013	INSCRIPTIONAL PAHLAVI LETTER YODH
        chars.append(0x10B6A)  #glyph00014	INSCRIPTIONAL PAHLAVI LETTER KAPH
        chars.append(0x10B6B)  #glyph00015	INSCRIPTIONAL PAHLAVI LETTER LAMEDH
        chars.append(0x10B6C)  #glyph00016	INSCRIPTIONAL PAHLAVI LETTER MEM-QOPH
        chars.append(0x10B6D)  #glyph00017	INSCRIPTIONAL PAHLAVI LETTER NUN
        chars.append(0x10B6E)  #glyph00018	INSCRIPTIONAL PAHLAVI LETTER SAMEKH
        chars.append(0x10B6F)  #glyph00019	INSCRIPTIONAL PAHLAVI LETTER PE
        chars.append(0x10B70)  #glyph00020	INSCRIPTIONAL PAHLAVI LETTER SADHE
        chars.append(0x10B71)  #glyph00021	INSCRIPTIONAL PAHLAVI LETTER SHIN
        chars.append(0x10B72)  #glyph00022	INSCRIPTIONAL PAHLAVI LETTER TAW
        chars.append(0x10B78)  #glyph00023	INSCRIPTIONAL PAHLAVI NUMBER ONE
        chars.append(0x10B79)  #glyph00024	INSCRIPTIONAL PAHLAVI NUMBER TWO
        chars.append(0x10B7A)  #glyph00025	INSCRIPTIONAL PAHLAVI NUMBER THREE
        chars.append(0x10B7B)  #glyph00026	INSCRIPTIONAL PAHLAVI NUMBER FOUR
        chars.append(0x10B7C)  #glyph00027	INSCRIPTIONAL PAHLAVI NUMBER TEN
        chars.append(0x10B7D)  #glyph00028	INSCRIPTIONAL PAHLAVI NUMBER TWENTY
        chars.append(0x10B7E)  #glyph00029	INSCRIPTIONAL PAHLAVI NUMBER ONE HUNDRED
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


