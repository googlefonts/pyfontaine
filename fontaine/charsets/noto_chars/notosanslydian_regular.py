# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansLydian-Regular'
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
        chars.append(0x10920)  #glyph00004	LYDIAN LETTER A
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10921)  #glyph00005	LYDIAN LETTER B
        chars.append(0x10922)  #glyph00006	LYDIAN LETTER G
        chars.append(0x10923)  #glyph00007	LYDIAN LETTER D
        chars.append(0x10924)  #glyph00008	LYDIAN LETTER E
        chars.append(0x10925)  #glyph00009	LYDIAN LETTER V
        chars.append(0x10926)  #glyph00010	LYDIAN LETTER I
        chars.append(0x10927)  #glyph00011	LYDIAN LETTER Y
        chars.append(0x10928)  #glyph00012	LYDIAN LETTER K
        chars.append(0x10929)  #glyph00013	LYDIAN LETTER L
        chars.append(0x1092A)  #glyph00014	LYDIAN LETTER M
        chars.append(0x1092B)  #glyph00015	LYDIAN LETTER N
        chars.append(0x1092C)  #glyph00016	LYDIAN LETTER O
        chars.append(0x1092D)  #glyph00017	LYDIAN LETTER R
        chars.append(0x1092E)  #glyph00018	LYDIAN LETTER SS
        chars.append(0x1092F)  #glyph00019	LYDIAN LETTER T
        chars.append(0x10930)  #glyph00020	LYDIAN LETTER U
        chars.append(0x10931)  #glyph00021	LYDIAN LETTER F
        chars.append(0x10932)  #glyph00022	LYDIAN LETTER Q
        chars.append(0x10933)  #glyph00023	LYDIAN LETTER S
        chars.append(0x10934)  #glyph00024	LYDIAN LETTER TT
        chars.append(0x10935)  #glyph00025	LYDIAN LETTER AN
        chars.append(0x10936)  #glyph00026	LYDIAN LETTER EN
        chars.append(0x10937)  #glyph00027	LYDIAN LETTER LY
        chars.append(0x10938)  #glyph00028	LYDIAN LETTER NN
        chars.append(0x10939)  #glyph00029	LYDIAN LETTER C
        chars.append(0x1093F)  #glyph00030	LYDIAN TRIANGULAR MARK
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


