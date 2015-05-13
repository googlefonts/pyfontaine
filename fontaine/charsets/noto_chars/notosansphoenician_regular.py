# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansPhoenician-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10901)  #glyph00005	PHOENICIAN LETTER BET
        chars.append(0x10902)  #glyph00006	PHOENICIAN LETTER GAML
        chars.append(0x10903)  #glyph00007	PHOENICIAN LETTER DELT
        chars.append(0x10904)  #glyph00008	PHOENICIAN LETTER HE
        chars.append(0x10905)  #glyph00009	PHOENICIAN LETTER WAU
        chars.append(0x10906)  #glyph00010	PHOENICIAN LETTER ZAI
        chars.append(0x10907)  #glyph00011	PHOENICIAN LETTER HET
        chars.append(0x10908)  #glyph00012	PHOENICIAN LETTER TET
        chars.append(0x10909)  #glyph00013	PHOENICIAN LETTER YOD
        chars.append(0x1090A)  #glyph00014	PHOENICIAN LETTER KAF
        chars.append(0x1090B)  #glyph00015	PHOENICIAN LETTER LAMD
        chars.append(0x1090C)  #glyph00016	PHOENICIAN LETTER MEM
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1090E)  #glyph00018	PHOENICIAN LETTER SEMK
        chars.append(0x1090F)  #glyph00019	PHOENICIAN LETTER AIN
        chars.append(0x10910)  #glyph00020	PHOENICIAN LETTER PE
        chars.append(0x10911)  #glyph00021	PHOENICIAN LETTER SADE
        chars.append(0x10912)  #glyph00022	PHOENICIAN LETTER QOF
        chars.append(0x10913)  #glyph00023	PHOENICIAN LETTER ROSH
        chars.append(0x10914)  #glyph00024	PHOENICIAN LETTER SHIN
        chars.append(0x10915)  #glyph00025	PHOENICIAN LETTER TAU
        chars.append(0x10916)  #glyph00026	PHOENICIAN NUMBER ONE
        chars.append(0x10917)  #glyph00027	PHOENICIAN NUMBER TEN
        chars.append(0x10918)  #glyph00028	PHOENICIAN NUMBER TWENTY
        chars.append(0x10919)  #glyph00029	PHOENICIAN NUMBER ONE HUNDRED
        chars.append(0x1091A)  #glyph00030	PHOENICIAN NUMBER TWO
        chars.append(0x1091B)  #glyph00031	PHOENICIAN NUMBER THREE
        chars.append(0x1091F)  #glyph00032	PHOENICIAN WORD SEPARATOR
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10900)  #glyph00004	PHOENICIAN LETTER ALF
        chars.append(0x1090D)  #glyph00017	PHOENICIAN LETTER NUN
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


