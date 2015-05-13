# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansNewTaiLue-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x1980)  #uni1980	NEW TAI LUE LETTER HIGH QA
        chars.append(0x1981)  #uni1981	NEW TAI LUE LETTER LOW QA
        chars.append(0x1982)  #uni1982	NEW TAI LUE LETTER HIGH KA
        chars.append(0x1983)  #uni1983	NEW TAI LUE LETTER HIGH XA
        chars.append(0x1984)  #uni1984	NEW TAI LUE LETTER HIGH NGA
        chars.append(0x1985)  #uni1985	NEW TAI LUE LETTER LOW KA
        chars.append(0x1986)  #uni1986	NEW TAI LUE LETTER LOW XA
        chars.append(0x1987)  #uni1987	NEW TAI LUE LETTER LOW NGA
        chars.append(0x1988)  #uni1988	NEW TAI LUE LETTER HIGH TSA
        chars.append(0x1989)  #uni1989	NEW TAI LUE LETTER HIGH SA
        chars.append(0x198A)  #uni198A	NEW TAI LUE LETTER HIGH YA
        chars.append(0x198B)  #uni198B	NEW TAI LUE LETTER LOW TSA
        chars.append(0x198C)  #uni198C	NEW TAI LUE LETTER LOW SA
        chars.append(0x198D)  #uni198D	NEW TAI LUE LETTER LOW YA
        chars.append(0x198E)  #uni198E	NEW TAI LUE LETTER HIGH TA
        chars.append(0x198F)  #uni198F	NEW TAI LUE LETTER HIGH THA
        chars.append(0x1990)  #uni1990	NEW TAI LUE LETTER HIGH NA
        chars.append(0x1991)  #uni1991	NEW TAI LUE LETTER LOW TA
        chars.append(0x1992)  #uni1992	NEW TAI LUE LETTER LOW THA
        chars.append(0x1993)  #uni1993	NEW TAI LUE LETTER LOW NA
        chars.append(0x1994)  #uni1994	NEW TAI LUE LETTER HIGH PA
        chars.append(0x1995)  #uni1995	NEW TAI LUE LETTER HIGH PHA
        chars.append(0x1996)  #uni1996	NEW TAI LUE LETTER HIGH MA
        chars.append(0x1997)  #uni1997	NEW TAI LUE LETTER LOW PA
        chars.append(0x1998)  #uni1998	NEW TAI LUE LETTER LOW PHA
        chars.append(0x1999)  #uni1999	NEW TAI LUE LETTER LOW MA
        chars.append(0x199A)  #uni199A	NEW TAI LUE LETTER HIGH FA
        chars.append(0x199B)  #uni199B	NEW TAI LUE LETTER HIGH VA
        chars.append(0x199C)  #uni199C	NEW TAI LUE LETTER HIGH LA
        chars.append(0x199D)  #uni199D	NEW TAI LUE LETTER LOW FA
        chars.append(0x199E)  #uni199E	NEW TAI LUE LETTER LOW VA
        chars.append(0x199F)  #uni199F	NEW TAI LUE LETTER LOW LA
        chars.append(0x19A0)  #uni19A0	NEW TAI LUE LETTER HIGH HA
        chars.append(0x19A1)  #uni19A1	NEW TAI LUE LETTER HIGH DA
        chars.append(0x19A2)  #uni19A2	NEW TAI LUE LETTER HIGH BA
        chars.append(0x19A3)  #uni19A3	NEW TAI LUE LETTER LOW HA
        chars.append(0x19A4)  #uni19A4	NEW TAI LUE LETTER LOW DA
        chars.append(0x19A5)  #uni19A5	NEW TAI LUE LETTER LOW BA
        chars.append(0x19A6)  #uni19A6	NEW TAI LUE LETTER HIGH KVA
        chars.append(0x19A7)  #uni19A7	NEW TAI LUE LETTER HIGH XVA
        chars.append(0x19A8)  #uni19A8	NEW TAI LUE LETTER LOW KVA
        chars.append(0x19A9)  #uni19A9	NEW TAI LUE LETTER LOW XVA
        chars.append(0x19AA)  #uni19AA	NEW TAI LUE LETTER HIGH SUA
        chars.append(0x19AB)  #uni19AB	NEW TAI LUE LETTER LOW SUA
        chars.append(0x19B0)  #uni19B0	NEW TAI LUE VOWEL SIGN VOWEL SHORTENER
        chars.append(0x19B1)  #uni19B1	NEW TAI LUE VOWEL SIGN AA
        chars.append(0x19B2)  #uni19B2	NEW TAI LUE VOWEL SIGN II
        chars.append(0x19B3)  #uni19B3	NEW TAI LUE VOWEL SIGN U
        chars.append(0x19B4)  #uni19B4	NEW TAI LUE VOWEL SIGN UU
        chars.append(0x19B5)  #uni19B5	NEW TAI LUE VOWEL SIGN E
        chars.append(0x19B6)  #uni19B6	NEW TAI LUE VOWEL SIGN AE
        chars.append(0x19B7)  #uni19B7	NEW TAI LUE VOWEL SIGN O
        chars.append(0x19B8)  #uni19B8	NEW TAI LUE VOWEL SIGN OA
        chars.append(0x19B9)  #uni19B9	NEW TAI LUE VOWEL SIGN UE
        chars.append(0x19BA)  #uni19BA	NEW TAI LUE VOWEL SIGN AY
        chars.append(0x19BB)  #uni19BB	NEW TAI LUE VOWEL SIGN AAY
        chars.append(0x19BC)  #uni19BC	NEW TAI LUE VOWEL SIGN UY
        chars.append(0x19BD)  #uni19BD	NEW TAI LUE VOWEL SIGN OY
        chars.append(0x19BE)  #uni19BE	NEW TAI LUE VOWEL SIGN OAY
        chars.append(0x19BF)  #uni19BF	NEW TAI LUE VOWEL SIGN UEY
        chars.append(0x19C0)  #uni19C0	NEW TAI LUE VOWEL SIGN IY
        chars.append(0x19C1)  #uni19C1	NEW TAI LUE LETTER FINAL V
        chars.append(0x19C2)  #uni19C2	NEW TAI LUE LETTER FINAL NG
        chars.append(0x19C3)  #uni19C3	NEW TAI LUE LETTER FINAL N
        chars.append(0x19C4)  #uni19C4	NEW TAI LUE LETTER FINAL M
        chars.append(0x19C5)  #uni19C5	NEW TAI LUE LETTER FINAL K
        chars.append(0x19C6)  #uni19C6	NEW TAI LUE LETTER FINAL D
        chars.append(0x19C7)  #uni19C7	NEW TAI LUE LETTER FINAL B
        chars.append(0x19C8)  #uni19C8	NEW TAI LUE TONE MARK-1
        chars.append(0x19C9)  #uni19C9	NEW TAI LUE TONE MARK-2
        chars.append(0x19D0)  #uni19D0	NEW TAI LUE DIGIT ZERO
        chars.append(0x19D1)  #uni19D1	NEW TAI LUE DIGIT ONE
        chars.append(0x19D2)  #uni19D2	NEW TAI LUE DIGIT TWO
        chars.append(0x19D3)  #uni19D3	NEW TAI LUE DIGIT THREE
        chars.append(0x19D4)  #uni19D4	NEW TAI LUE DIGIT FOUR
        chars.append(0x19D5)  #uni19D5	NEW TAI LUE DIGIT FIVE
        chars.append(0x19D6)  #uni19D6	NEW TAI LUE DIGIT SIX
        chars.append(0x19D7)  #uni19D7	NEW TAI LUE DIGIT SEVEN
        chars.append(0x19D8)  #uni19D8	NEW TAI LUE DIGIT EIGHT
        chars.append(0x19D9)  #uni19D9	NEW TAI LUE DIGIT NINE
        chars.append(0x19DA)  #uni19DA	NEW TAI LUE THAM DIGIT ONE
        chars.append(0x19DE)  #uni19DE	NEW TAI LUE SIGN LAE
        chars.append(0x19DF)  #uni19DF	NEW TAI LUE SIGN LAEV
        return chars


