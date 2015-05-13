# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansUgaritic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10380)  #glyph00034	UGARITIC LETTER ALPA
        chars.append(0x10382)  #glyph00005	UGARITIC LETTER GAMLA
        chars.append(0x10383)  #glyph00006	UGARITIC LETTER KHA
        chars.append(0x10384)  #glyph00011	UGARITIC LETTER DELTA
        chars.append(0x10385)  #glyph00013	UGARITIC LETTER HO
        chars.append(0x10386)  #glyph00031	UGARITIC LETTER WO
        chars.append(0x10381)  #glyph00004	UGARITIC LETTER BETA
        chars.append(0x10388)  #glyph00008	UGARITIC LETTER HOTA
        chars.append(0x10389)  #glyph00015	UGARITIC LETTER TET
        chars.append(0x1038A)  #glyph00016	UGARITIC LETTER YOD
        chars.append(0x1038B)  #glyph00033	UGARITIC LETTER KAF
        chars.append(0x1038C)  #glyph00017	UGARITIC LETTER SHIN
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1038E)  #glyph00029	UGARITIC LETTER MEM
        chars.append(0x1038F)  #glyph00027	UGARITIC LETTER DHAL
        chars.append(0x10390)  #glyph00007	UGARITIC LETTER NUN
        chars.append(0x10391)  #glyph00025	UGARITIC LETTER ZU
        chars.append(0x10392)  #glyph00024	UGARITIC LETTER SAMKA
        chars.append(0x10393)  #glyph00023	UGARITIC LETTER AIN
        chars.append(0x10394)  #glyph00019	UGARITIC LETTER PU
        chars.append(0x10395)  #glyph00020	UGARITIC LETTER SADE
        chars.append(0x10396)  #glyph00021	UGARITIC LETTER QOPA
        chars.append(0x10397)  #glyph00032	UGARITIC LETTER RASHA
        chars.append(0x10398)  #glyph00026	UGARITIC LETTER THANNA
        chars.append(0x10399)  #glyph00030	UGARITIC LETTER GHAIN
        chars.append(0x1039A)  #glyph00018	UGARITIC LETTER TO
        chars.append(0x1039B)  #glyph00022	UGARITIC LETTER I
        chars.append(0x1039C)  #glyph00028	UGARITIC LETTER U
        chars.append(0x1039D)  #glyph00009	UGARITIC LETTER SSU
        chars.append(0x1039F)  #glyph00010	UGARITIC WORD DIVIDER
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10387)  #glyph00014	UGARITIC LETTER ZETA
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1038D)  #glyph00012	UGARITIC LETTER LAMDA
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


