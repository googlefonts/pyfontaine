# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTaiViet-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0xAA81)  #uniAA81	TAI VIET LETTER HIGH KO
        chars.append(0xAA82)  #uniAA82	TAI VIET LETTER LOW KHO
        chars.append(0xAA83)  #uniAA83	TAI VIET LETTER HIGH KHO
        chars.append(0xAA84)  #uniAA84	TAI VIET LETTER LOW KHHO
        chars.append(0xAA85)  #uniAA85	TAI VIET LETTER HIGH KHHO
        chars.append(0xAA86)  #uniAA86	TAI VIET LETTER LOW GO
        chars.append(0xAA87)  #uniAA87	TAI VIET LETTER HIGH GO
        chars.append(0xAA88)  #uniAA88	TAI VIET LETTER LOW NGO
        chars.append(0xAA89)  #uniAA89	TAI VIET LETTER HIGH NGO
        chars.append(0xAA8A)  #uniAA8A	TAI VIET LETTER LOW CO
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0xA78C)  #uniA78C	LATIN SMALL LETTER SALTILLO
        chars.append(0x000D)  #uni000D	????
        chars.append(0xAA8E)  #uniAA8E	TAI VIET LETTER LOW SO
        chars.append(0xAA8F)  #uniAA8F	TAI VIET LETTER HIGH SO
        chars.append(0xAA90)  #uniAA90	TAI VIET LETTER LOW NYO
        chars.append(0xAA91)  #uniAA91	TAI VIET LETTER HIGH NYO
        chars.append(0xAA92)  #uniAA92	TAI VIET LETTER LOW DO
        chars.append(0xAA93)  #uniAA93	TAI VIET LETTER HIGH DO
        chars.append(0xAA94)  #uniAA94	TAI VIET LETTER LOW TO
        chars.append(0xAA95)  #uniAA95	TAI VIET LETTER HIGH TO
        chars.append(0xAA96)  #uniAA96	TAI VIET LETTER LOW THO
        chars.append(0xAA97)  #uniAA97	TAI VIET LETTER HIGH THO
        chars.append(0xAA98)  #uniAA98	TAI VIET LETTER LOW NO
        chars.append(0xAA99)  #uniAA99	TAI VIET LETTER HIGH NO
        chars.append(0xAA9A)  #uniAA9A	TAI VIET LETTER LOW BO
        chars.append(0xAA9B)  #uniAA9B	TAI VIET LETTER HIGH BO
        chars.append(0xAA9C)  #uniAA9C	TAI VIET LETTER LOW PO
        chars.append(0xAA9D)  #uniAA9D	TAI VIET LETTER HIGH PO
        chars.append(0xAA9E)  #uniAA9E	TAI VIET LETTER LOW PHO
        chars.append(0xAA9F)  #uniAA9F	TAI VIET LETTER HIGH PHO
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0xAAA1)  #uniAAA1	TAI VIET LETTER HIGH FO
        chars.append(0xAAA2)  #uniAAA2	TAI VIET LETTER LOW MO
        chars.append(0xAAA3)  #uniAAA3	TAI VIET LETTER HIGH MO
        chars.append(0xAAA4)  #uniAAA4	TAI VIET LETTER LOW YO
        chars.append(0xAAA5)  #uniAAA5	TAI VIET LETTER HIGH YO
        chars.append(0xAAA6)  #uniAAA6	TAI VIET LETTER LOW RO
        chars.append(0xAAA7)  #uniAAA7	TAI VIET LETTER HIGH RO
        chars.append(0xAAA8)  #uniAAA8	TAI VIET LETTER LOW LO
        chars.append(0xAAA9)  #uniAAA9	TAI VIET LETTER HIGH LO
        chars.append(0xAAAA)  #uniAAAA	TAI VIET LETTER LOW VO
        chars.append(0xAAAB)  #uniAAAB	TAI VIET LETTER HIGH VO
        chars.append(0xAAAC)  #uniAAAC	TAI VIET LETTER LOW HO
        chars.append(0xAAAD)  #uniAAAD	TAI VIET LETTER HIGH HO
        chars.append(0xAAAE)  #uniAAAE	TAI VIET LETTER LOW O
        chars.append(0xAAAF)  #uniAAAF	TAI VIET LETTER HIGH O
        chars.append(0xAAB0)  #uniAAB0	TAI VIET MAI KANG
        chars.append(0xAAB1)  #uniAAB1	TAI VIET VOWEL AA
        chars.append(0xAAA0)  #uniAAA0	TAI VIET LETTER LOW FO
        chars.append(0xAAB3)  #uniAAB3	TAI VIET VOWEL UE
        chars.append(0xAAB4)  #uniAAB4	TAI VIET VOWEL U
        chars.append(0xAAB5)  #uniAAB5	TAI VIET VOWEL E
        chars.append(0xAAB6)  #uniAAB6	TAI VIET VOWEL O
        chars.append(0xAAB2)  #uniAAB2	TAI VIET VOWEL I
        chars.append(0xAAB8)  #uniAAB8	TAI VIET VOWEL IA
        chars.append(0xAAB9)  #uniAAB9	TAI VIET VOWEL UEA
        chars.append(0xAABA)  #uniAABA	TAI VIET VOWEL UA
        chars.append(0xAABB)  #uniAABB	TAI VIET VOWEL AUE
        chars.append(0xAABC)  #uniAABC	TAI VIET VOWEL AY
        chars.append(0xAABD)  #uniAABD	TAI VIET VOWEL AN
        chars.append(0xAABE)  #uniAABE	TAI VIET VOWEL AM
        chars.append(0xAABF)  #uniAABF	TAI VIET TONE MAI EK
        chars.append(0xAAC0)  #uniAAC0	TAI VIET TONE MAI NUENG
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xAA8C)  #uniAA8C	TAI VIET LETTER LOW CHO
        chars.append(0xAA8B)  #uniAA8B	TAI VIET LETTER HIGH CO
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0xAAB7)  #uniAAB7	TAI VIET MAI KHIT
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0xAA80)  #uniAA80	TAI VIET LETTER LOW KO
        chars.append(0xAADB)  #uniAADB	TAI VIET SYMBOL KON
        chars.append(0xAADC)  #uniAADC	TAI VIET SYMBOL NUENG
        chars.append(0xAADD)  #uniAADD	TAI VIET SYMBOL SAM
        chars.append(0xAADE)  #uniAADE	TAI VIET SYMBOL HO HOI
        chars.append(0xAADF)  #uniAADF	TAI VIET SYMBOL KOI KOI
        chars.append(0xAA8D)  #uniAA8D	TAI VIET LETTER HIGH CHO
        chars.append(0xAAC2)  #uniAAC2	TAI VIET TONE MAI SONG
        chars.append(0xAAC1)  #uniAAC1	TAI VIET TONE MAI THO
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


