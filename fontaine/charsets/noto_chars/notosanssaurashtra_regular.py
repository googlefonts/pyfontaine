# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansSaurashtra-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0xA880)  #uniA880	SAURASHTRA SIGN ANUSVARA
        chars.append(0xA881)  #uniA881	SAURASHTRA SIGN VISARGA
        chars.append(0xA882)  #uniA882	SAURASHTRA LETTER A
        chars.append(0xA883)  #uniA883	SAURASHTRA LETTER AA
        chars.append(0xA884)  #uniA884	SAURASHTRA LETTER I
        chars.append(0xA885)  #uniA885	SAURASHTRA LETTER II
        chars.append(0xA886)  #uniA886	SAURASHTRA LETTER U
        chars.append(0xA887)  #uniA887	SAURASHTRA LETTER UU
        chars.append(0xA888)  #uniA888	SAURASHTRA LETTER VOCALIC R
        chars.append(0xA889)  #uniA889	SAURASHTRA LETTER VOCALIC RR
        chars.append(0xA88A)  #uniA88A	SAURASHTRA LETTER VOCALIC L
        chars.append(0xA88B)  #uniA88B	SAURASHTRA LETTER VOCALIC LL
        chars.append(0xA88C)  #uniA88C	SAURASHTRA LETTER E
        chars.append(0xA88D)  #uniA88D	SAURASHTRA LETTER EE
        chars.append(0xA88E)  #uniA88E	SAURASHTRA LETTER AI
        chars.append(0xA88F)  #uniA88F	SAURASHTRA LETTER O
        chars.append(0xA890)  #uniA890	SAURASHTRA LETTER OO
        chars.append(0xA891)  #uniA891	SAURASHTRA LETTER AU
        chars.append(0xA892)  #uniA892	SAURASHTRA LETTER KA
        chars.append(0xA893)  #uniA893	SAURASHTRA LETTER KHA
        chars.append(0xA894)  #uniA894	SAURASHTRA LETTER GA
        chars.append(0xA895)  #uniA895	SAURASHTRA LETTER GHA
        chars.append(0xA896)  #uniA896	SAURASHTRA LETTER NGA
        chars.append(0xA897)  #uniA897	SAURASHTRA LETTER CA
        chars.append(0xA898)  #uniA898	SAURASHTRA LETTER CHA
        chars.append(0xA899)  #uniA899	SAURASHTRA LETTER JA
        chars.append(0xA89A)  #uniA89A	SAURASHTRA LETTER JHA
        chars.append(0xA89B)  #uniA89B	SAURASHTRA LETTER NYA
        chars.append(0xA89C)  #uniA89C	SAURASHTRA LETTER TTA
        chars.append(0xA89D)  #uniA89D	SAURASHTRA LETTER TTHA
        chars.append(0xA89E)  #uniA89E	SAURASHTRA LETTER DDA
        chars.append(0xA89F)  #uniA89F	SAURASHTRA LETTER DDHA
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xA8A1)  #uniA8A1	SAURASHTRA LETTER TA
        chars.append(0xA8A2)  #uniA8A2	SAURASHTRA LETTER THA
        chars.append(0xA8A3)  #uniA8A3	SAURASHTRA LETTER DA
        chars.append(0xA8A4)  #uniA8A4	SAURASHTRA LETTER DHA
        chars.append(0xA8A5)  #uniA8A5	SAURASHTRA LETTER NA
        chars.append(0xA8A6)  #uniA8A6	SAURASHTRA LETTER PA
        chars.append(0xA8A7)  #uniA8A7	SAURASHTRA LETTER PHA
        chars.append(0xA8A8)  #uniA8A8	SAURASHTRA LETTER BA
        chars.append(0xA8A9)  #uniA8A9	SAURASHTRA LETTER BHA
        chars.append(0xA8AA)  #uniA8AA	SAURASHTRA LETTER MA
        chars.append(0xA8AB)  #uniA8AB	SAURASHTRA LETTER YA
        chars.append(0xA8AC)  #uniA8AC	SAURASHTRA LETTER RA
        chars.append(0xA8AD)  #uniA8AD	SAURASHTRA LETTER LA
        chars.append(0xA8AE)  #uniA8AE	SAURASHTRA LETTER VA
        chars.append(0xA8AF)  #uniA8AF	SAURASHTRA LETTER SHA
        chars.append(0xA8B0)  #uniA8B0	SAURASHTRA LETTER SSA
        chars.append(0xA8B1)  #uniA8B1	SAURASHTRA LETTER SA
        chars.append(0xA8B2)  #uniA8B2	SAURASHTRA LETTER HA
        chars.append(0xA8B3)  #uniA8B3	SAURASHTRA LETTER LLA
        chars.append(0xA8B4)  #uniA8B4	SAURASHTRA CONSONANT SIGN HAARU
        chars.append(0xA8B5)  #uniA8B5	SAURASHTRA VOWEL SIGN AA
        chars.append(0xA8B6)  #uniA8B6	SAURASHTRA VOWEL SIGN I
        chars.append(0xA8B7)  #uniA8B7	SAURASHTRA VOWEL SIGN II
        chars.append(0xA8B8)  #uniA8B8	SAURASHTRA VOWEL SIGN U
        chars.append(0xA8B9)  #uniA8B9	SAURASHTRA VOWEL SIGN UU
        chars.append(0xA8BA)  #uniA8BA	SAURASHTRA VOWEL SIGN VOCALIC R
        chars.append(0xA8BB)  #uniA8BB	SAURASHTRA VOWEL SIGN VOCALIC RR
        chars.append(0xA8BC)  #uniA8BC	SAURASHTRA VOWEL SIGN VOCALIC L
        chars.append(0xA8BD)  #uniA8BD	SAURASHTRA VOWEL SIGN VOCALIC LL
        chars.append(0xA8BE)  #uniA8BE	SAURASHTRA VOWEL SIGN E
        chars.append(0xA8BF)  #uniA8BF	SAURASHTRA VOWEL SIGN EE
        chars.append(0xA8C0)  #uniA8C0	SAURASHTRA VOWEL SIGN AI
        chars.append(0xA8C1)  #uniA8C1	SAURASHTRA VOWEL SIGN O
        chars.append(0xA8C2)  #uniA8C2	SAURASHTRA VOWEL SIGN OO
        chars.append(0xA8C3)  #uniA8C3	SAURASHTRA VOWEL SIGN AU
        chars.append(0xA8C4)  #uniA8C4	SAURASHTRA SIGN VIRAMA
        chars.append(0xA8CE)  #uniA8CE	SAURASHTRA DANDA
        chars.append(0xA8CF)  #uniA8CF	SAURASHTRA DOUBLE DANDA
        chars.append(0xA8D0)  #uniA8D0	SAURASHTRA DIGIT ZERO
        chars.append(0xA8D1)  #uniA8D1	SAURASHTRA DIGIT ONE
        chars.append(0xA8D2)  #uniA8D2	SAURASHTRA DIGIT TWO
        chars.append(0xA8D3)  #uniA8D3	SAURASHTRA DIGIT THREE
        chars.append(0xA8D4)  #uniA8D4	SAURASHTRA DIGIT FOUR
        chars.append(0xA8D5)  #uniA8D5	SAURASHTRA DIGIT FIVE
        chars.append(0xA8D6)  #uniA8D6	SAURASHTRA DIGIT SIX
        chars.append(0xA8D7)  #uniA8D7	SAURASHTRA DIGIT SEVEN
        chars.append(0xA8D8)  #uniA8D8	SAURASHTRA DIGIT EIGHT
        chars.append(0xA8D9)  #uniA8D9	SAURASHTRA DIGIT NINE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xA8A0)  #uniA8A0	SAURASHTRA LETTER NNA
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        return chars


