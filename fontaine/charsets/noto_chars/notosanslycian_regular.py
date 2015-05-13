# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansLycian-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10281)  #glyph00005	LYCIAN LETTER E
        chars.append(0x10282)  #glyph00006	LYCIAN LETTER B
        chars.append(0x10283)  #glyph00007	LYCIAN LETTER BH
        chars.append(0x10284)  #glyph00008	LYCIAN LETTER G
        chars.append(0x10285)  #glyph00009	LYCIAN LETTER D
        chars.append(0x10286)  #glyph00010	LYCIAN LETTER I
        chars.append(0x10287)  #glyph00011	LYCIAN LETTER W
        chars.append(0x10288)  #glyph00012	LYCIAN LETTER Z
        chars.append(0x10289)  #glyph00013	LYCIAN LETTER TH
        chars.append(0x1028A)  #glyph00014	LYCIAN LETTER J
        chars.append(0x1028B)  #glyph00015	LYCIAN LETTER K
        chars.append(0x1028C)  #glyph00016	LYCIAN LETTER Q
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1028E)  #glyph00018	LYCIAN LETTER M
        chars.append(0x1028F)  #glyph00019	LYCIAN LETTER N
        chars.append(0x10290)  #glyph00020	LYCIAN LETTER MM
        chars.append(0x10291)  #glyph00021	LYCIAN LETTER NN
        chars.append(0x10292)  #glyph00022	LYCIAN LETTER U
        chars.append(0x10293)  #glyph00023	LYCIAN LETTER P
        chars.append(0x10294)  #glyph00024	LYCIAN LETTER KK
        chars.append(0x10295)  #glyph00025	LYCIAN LETTER R
        chars.append(0x10296)  #glyph00026	LYCIAN LETTER S
        chars.append(0x10297)  #glyph00027	LYCIAN LETTER T
        chars.append(0x10298)  #glyph00028	LYCIAN LETTER TT
        chars.append(0x10299)  #glyph00029	LYCIAN LETTER AN
        chars.append(0x10280)  #glyph00004	LYCIAN LETTER A
        chars.append(0x1029B)  #glyph00031	LYCIAN LETTER H
        chars.append(0x1029C)  #glyph00032	LYCIAN LETTER X
        chars.append(0x1029A)  #glyph00030	LYCIAN LETTER EN
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1028D)  #glyph00017	LYCIAN LETTER L
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


