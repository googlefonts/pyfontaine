# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansInscriptionalParthian-Regular'
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
        chars.append(0x10B4B)  #glyph00015	INSCRIPTIONAL PARTHIAN LETTER LAMEDH
        chars.append(0x10B40)  #glyph00004	INSCRIPTIONAL PARTHIAN LETTER ALEPH
        chars.append(0x10B41)  #glyph00005	INSCRIPTIONAL PARTHIAN LETTER BETH
        chars.append(0x10B42)  #glyph00006	INSCRIPTIONAL PARTHIAN LETTER GIMEL
        chars.append(0x10B43)  #glyph00007	INSCRIPTIONAL PARTHIAN LETTER DALETH
        chars.append(0x10B44)  #glyph00008	INSCRIPTIONAL PARTHIAN LETTER HE
        chars.append(0x10B45)  #glyph00009	INSCRIPTIONAL PARTHIAN LETTER WAW
        chars.append(0x10B46)  #glyph00010	INSCRIPTIONAL PARTHIAN LETTER ZAYIN
        chars.append(0x10B47)  #glyph00011	INSCRIPTIONAL PARTHIAN LETTER HETH
        chars.append(0x10B48)  #glyph00012	INSCRIPTIONAL PARTHIAN LETTER TETH
        chars.append(0x10B49)  #glyph00013	INSCRIPTIONAL PARTHIAN LETTER YODH
        chars.append(0x10B4A)  #glyph00014	INSCRIPTIONAL PARTHIAN LETTER KAPH
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10B4C)  #glyph00016	INSCRIPTIONAL PARTHIAN LETTER MEM
        chars.append(0x10B4D)  #glyph00017	INSCRIPTIONAL PARTHIAN LETTER NUN
        chars.append(0x10B4E)  #glyph00018	INSCRIPTIONAL PARTHIAN LETTER SAMEKH
        chars.append(0x10B4F)  #glyph00019	INSCRIPTIONAL PARTHIAN LETTER AYIN
        chars.append(0x10B50)  #glyph00020	INSCRIPTIONAL PARTHIAN LETTER PE
        chars.append(0x10B51)  #glyph00021	INSCRIPTIONAL PARTHIAN LETTER SADHE
        chars.append(0x10B52)  #glyph00022	INSCRIPTIONAL PARTHIAN LETTER QOPH
        chars.append(0x10B53)  #glyph00023	INSCRIPTIONAL PARTHIAN LETTER RESH
        chars.append(0x10B54)  #glyph00024	INSCRIPTIONAL PARTHIAN LETTER SHIN
        chars.append(0x10B55)  #glyph00025	INSCRIPTIONAL PARTHIAN LETTER TAW
        chars.append(0x10B58)  #glyph00026	INSCRIPTIONAL PARTHIAN NUMBER ONE
        chars.append(0x10B59)  #glyph00027	INSCRIPTIONAL PARTHIAN NUMBER TWO
        chars.append(0x10B5A)  #glyph00028	INSCRIPTIONAL PARTHIAN NUMBER THREE
        chars.append(0x10B5B)  #glyph00029	INSCRIPTIONAL PARTHIAN NUMBER FOUR
        chars.append(0x10B5C)  #glyph00030	INSCRIPTIONAL PARTHIAN NUMBER TEN
        chars.append(0x10B5D)  #glyph00031	INSCRIPTIONAL PARTHIAN NUMBER TWENTY
        chars.append(0x10B5E)  #glyph00032	INSCRIPTIONAL PARTHIAN NUMBER ONE HUNDRED
        chars.append(0x10B5F)  #glyph00033	INSCRIPTIONAL PARTHIAN NUMBER ONE THOUSAND
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


