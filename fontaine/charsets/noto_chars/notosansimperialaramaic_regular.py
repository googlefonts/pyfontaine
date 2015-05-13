# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansImperialAramaic-Regular'
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
        chars.append(0x1084B)  #glyph00015	IMPERIAL ARAMAIC LETTER LAMEDH
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10840)  #glyph00004	IMPERIAL ARAMAIC LETTER ALEPH
        chars.append(0x10841)  #glyph00005	IMPERIAL ARAMAIC LETTER BETH
        chars.append(0x10842)  #glyph00006	IMPERIAL ARAMAIC LETTER GIMEL
        chars.append(0x10843)  #glyph00007	IMPERIAL ARAMAIC LETTER DALETH
        chars.append(0x10844)  #glyph00008	IMPERIAL ARAMAIC LETTER HE
        chars.append(0x10845)  #glyph00009	IMPERIAL ARAMAIC LETTER WAW
        chars.append(0x10846)  #glyph00010	IMPERIAL ARAMAIC LETTER ZAYIN
        chars.append(0x10847)  #glyph00011	IMPERIAL ARAMAIC LETTER HETH
        chars.append(0x10848)  #glyph00012	IMPERIAL ARAMAIC LETTER TETH
        chars.append(0x10849)  #glyph00013	IMPERIAL ARAMAIC LETTER YODH
        chars.append(0x1084A)  #glyph00014	IMPERIAL ARAMAIC LETTER KAPH
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1084C)  #glyph00016	IMPERIAL ARAMAIC LETTER MEM
        chars.append(0x1084D)  #glyph00017	IMPERIAL ARAMAIC LETTER NUN
        chars.append(0x1084E)  #glyph00018	IMPERIAL ARAMAIC LETTER SAMEKH
        chars.append(0x1084F)  #glyph00019	IMPERIAL ARAMAIC LETTER AYIN
        chars.append(0x10850)  #glyph00020	IMPERIAL ARAMAIC LETTER PE
        chars.append(0x10851)  #glyph00021	IMPERIAL ARAMAIC LETTER SADHE
        chars.append(0x10852)  #glyph00022	IMPERIAL ARAMAIC LETTER QOPH
        chars.append(0x10853)  #glyph00023	IMPERIAL ARAMAIC LETTER RESH
        chars.append(0x10854)  #glyph00024	IMPERIAL ARAMAIC LETTER SHIN
        chars.append(0x10855)  #glyph00025	IMPERIAL ARAMAIC LETTER TAW
        chars.append(0x10857)  #glyph00026	IMPERIAL ARAMAIC SECTION SIGN
        chars.append(0x10858)  #glyph00027	IMPERIAL ARAMAIC NUMBER ONE
        chars.append(0x10859)  #glyph00028	IMPERIAL ARAMAIC NUMBER TWO
        chars.append(0x1085A)  #glyph00029	IMPERIAL ARAMAIC NUMBER THREE
        chars.append(0x1085B)  #glyph00030	IMPERIAL ARAMAIC NUMBER TEN
        chars.append(0x1085C)  #glyph00031	IMPERIAL ARAMAIC NUMBER TWENTY
        chars.append(0x1085D)  #glyph00032	IMPERIAL ARAMAIC NUMBER ONE HUNDRED
        chars.append(0x1085E)  #glyph00033	IMPERIAL ARAMAIC NUMBER ONE THOUSAND
        chars.append(0x1085F)  #glyph00034	IMPERIAL ARAMAIC NUMBER TEN THOUSAND
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


