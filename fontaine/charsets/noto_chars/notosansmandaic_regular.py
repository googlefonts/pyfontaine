# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansMandaic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0640)  #uni0640	ARABIC TATWEEL
        chars.append(0x000D)  #uni000D	????
        chars.append(0x084B)  #uni084B	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0840)  #uni0840	????
        chars.append(0x0841)  #uni0841	????
        chars.append(0x0842)  #uni0842	????
        chars.append(0x0843)  #uni0843	????
        chars.append(0x0844)  #uni0844	????
        chars.append(0x0845)  #uni0845	????
        chars.append(0x0846)  #uni0846	????
        chars.append(0x0847)  #uni0847	????
        chars.append(0x0848)  #uni0848	????
        chars.append(0x0849)  #uni0849	????
        chars.append(0x084A)  #uni084A	????
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x084C)  #uni084C	????
        chars.append(0x084D)  #uni084D	????
        chars.append(0x084E)  #uni084E	????
        chars.append(0x084F)  #uni084F	????
        chars.append(0x0850)  #uni0850	????
        chars.append(0x0851)  #uni0851	????
        chars.append(0x0852)  #uni0852	????
        chars.append(0x0853)  #uni0853	????
        chars.append(0x0854)  #uni0854	????
        chars.append(0x0855)  #uni0855	????
        chars.append(0x0856)  #uni0856	????
        chars.append(0x0857)  #uni0857	????
        chars.append(0x0858)  #uni0858	????
        chars.append(0x0859)  #uni0859	????
        chars.append(0x085A)  #uni085A	????
        chars.append(0x085B)  #uni085B	????
        chars.append(0x085E)  #uni085E	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


