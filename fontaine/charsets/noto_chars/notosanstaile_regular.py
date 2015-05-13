# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTaiLe-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x3001)  #uni3001	IDEOGRAPHIC COMMA
        chars.append(0x3002)  #uni3002	IDEOGRAPHIC FULL STOP
        chars.append(0x3008)  #uni3008	LEFT ANGLE BRACKET
        chars.append(0x3009)  #uni3009	RIGHT ANGLE BRACKET
        chars.append(0x300A)  #uni300A	LEFT DOUBLE ANGLE BRACKET
        chars.append(0x300B)  #uni300B	RIGHT DOUBLE ANGLE BRACKET
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x1040)  #uni1040	MYANMAR DIGIT ZERO
        chars.append(0x1041)  #uni1041	MYANMAR DIGIT ONE
        chars.append(0x1042)  #uni1042	MYANMAR DIGIT TWO
        chars.append(0x1043)  #uni1043	MYANMAR DIGIT THREE
        chars.append(0x1044)  #uni1044	MYANMAR DIGIT FOUR
        chars.append(0x1045)  #uni1045	MYANMAR DIGIT FIVE
        chars.append(0x1046)  #uni1046	MYANMAR DIGIT SIX
        chars.append(0x1047)  #uni1047	MYANMAR DIGIT SEVEN
        chars.append(0x1048)  #uni1048	MYANMAR DIGIT EIGHT
        chars.append(0x1049)  #uni1049	MYANMAR DIGIT NINE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1950)  #uni1950	TAI LE LETTER KA
        chars.append(0x1951)  #uni1951	TAI LE LETTER XA
        chars.append(0x1952)  #uni1952	TAI LE LETTER NGA
        chars.append(0x1953)  #uni1953	TAI LE LETTER TSA
        chars.append(0x1954)  #uni1954	TAI LE LETTER SA
        chars.append(0x1955)  #uni1955	TAI LE LETTER YA
        chars.append(0x1956)  #uni1956	TAI LE LETTER TA
        chars.append(0x1957)  #uni1957	TAI LE LETTER THA
        chars.append(0x1958)  #uni1958	TAI LE LETTER LA
        chars.append(0x1959)  #uni1959	TAI LE LETTER PA
        chars.append(0x195A)  #uni195A	TAI LE LETTER PHA
        chars.append(0x195B)  #uni195B	TAI LE LETTER MA
        chars.append(0x195C)  #uni195C	TAI LE LETTER FA
        chars.append(0x195D)  #uni195D	TAI LE LETTER VA
        chars.append(0x195E)  #uni195E	TAI LE LETTER HA
        chars.append(0x195F)  #uni195F	TAI LE LETTER QA
        chars.append(0x1960)  #uni1960	TAI LE LETTER KHA
        chars.append(0x1961)  #uni1961	TAI LE LETTER TSHA
        chars.append(0x1962)  #uni1962	TAI LE LETTER NA
        chars.append(0x1963)  #uni1963	TAI LE LETTER A
        chars.append(0x1964)  #uni1964	TAI LE LETTER I
        chars.append(0x1965)  #uni1965	TAI LE LETTER EE
        chars.append(0x1966)  #uni1966	TAI LE LETTER EH
        chars.append(0x1967)  #uni1967	TAI LE LETTER U
        chars.append(0x1968)  #uni1968	TAI LE LETTER OO
        chars.append(0x1969)  #uni1969	TAI LE LETTER O
        chars.append(0x196A)  #uni196A	TAI LE LETTER UE
        chars.append(0x196B)  #uni196B	TAI LE LETTER E
        chars.append(0x196C)  #uni196C	TAI LE LETTER AUE
        chars.append(0x196D)  #uni196D	TAI LE LETTER AI
        chars.append(0x1970)  #uni1970	TAI LE LETTER TONE-2
        chars.append(0x1971)  #uni1971	TAI LE LETTER TONE-3
        chars.append(0x1972)  #uni1972	TAI LE LETTER TONE-4
        chars.append(0x1973)  #uni1973	TAI LE LETTER TONE-5
        chars.append(0x1974)  #uni1974	TAI LE LETTER TONE-6
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


