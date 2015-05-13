# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansOlChiki-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1C50)  #uni1C50	OL CHIKI DIGIT ZERO
        chars.append(0x1C51)  #uni1C51	OL CHIKI DIGIT ONE
        chars.append(0x1C52)  #uni1C52	OL CHIKI DIGIT TWO
        chars.append(0x1C53)  #uni1C53	OL CHIKI DIGIT THREE
        chars.append(0x1C54)  #uni1C54	OL CHIKI DIGIT FOUR
        chars.append(0x1C55)  #uni1C55	OL CHIKI DIGIT FIVE
        chars.append(0x1C56)  #uni1C56	OL CHIKI DIGIT SIX
        chars.append(0x1C57)  #uni1C57	OL CHIKI DIGIT SEVEN
        chars.append(0x1C58)  #uni1C58	OL CHIKI DIGIT EIGHT
        chars.append(0x1C59)  #uni1C59	OL CHIKI DIGIT NINE
        chars.append(0x1C5A)  #uni1C5A	OL CHIKI LETTER LA
        chars.append(0x1C5B)  #uni1C5B	OL CHIKI LETTER AT
        chars.append(0x1C5C)  #uni1C5C	OL CHIKI LETTER AG
        chars.append(0x1C5D)  #uni1C5D	OL CHIKI LETTER ANG
        chars.append(0x1C5E)  #uni1C5E	OL CHIKI LETTER AL
        chars.append(0x1C5F)  #uni1C5F	OL CHIKI LETTER LAA
        chars.append(0x1C60)  #uni1C60	OL CHIKI LETTER AAK
        chars.append(0x1C61)  #uni1C61	OL CHIKI LETTER AAJ
        chars.append(0x1C62)  #uni1C62	OL CHIKI LETTER AAM
        chars.append(0x1C63)  #uni1C63	OL CHIKI LETTER AAW
        chars.append(0x1C64)  #uni1C64	OL CHIKI LETTER LI
        chars.append(0x1C65)  #uni1C65	OL CHIKI LETTER IS
        chars.append(0x1C66)  #uni1C66	OL CHIKI LETTER IH
        chars.append(0x1C67)  #uni1C67	OL CHIKI LETTER INY
        chars.append(0x1C68)  #uni1C68	OL CHIKI LETTER IR
        chars.append(0x1C69)  #uni1C69	OL CHIKI LETTER LU
        chars.append(0x1C6A)  #uni1C6A	OL CHIKI LETTER UC
        chars.append(0x1C6B)  #uni1C6B	OL CHIKI LETTER UD
        chars.append(0x1C6C)  #uni1C6C	OL CHIKI LETTER UNN
        chars.append(0x1C6D)  #uni1C6D	OL CHIKI LETTER UY
        chars.append(0x1C6E)  #uni1C6E	OL CHIKI LETTER LE
        chars.append(0x1C6F)  #uni1C6F	OL CHIKI LETTER EP
        chars.append(0x1C70)  #uni1C70	OL CHIKI LETTER EDD
        chars.append(0x1C71)  #uni1C71	OL CHIKI LETTER EN
        chars.append(0x1C72)  #uni1C72	OL CHIKI LETTER ERR
        chars.append(0x1C73)  #uni1C73	OL CHIKI LETTER LO
        chars.append(0x1C74)  #uni1C74	OL CHIKI LETTER OTT
        chars.append(0x1C75)  #uni1C75	OL CHIKI LETTER OB
        chars.append(0x1C76)  #uni1C76	OL CHIKI LETTER OV
        chars.append(0x1C77)  #uni1C77	OL CHIKI LETTER OH
        chars.append(0x1C78)  #uni1C78	OL CHIKI MU TTUDDAG
        chars.append(0x1C79)  #uni1C79	OL CHIKI GAAHLAA TTUDDAAG
        chars.append(0x1C7A)  #uni1C7A	OL CHIKI MU-GAAHLAA TTUDDAAG
        chars.append(0x1C7B)  #uni1C7B	OL CHIKI RELAA
        chars.append(0x1C7C)  #uni1C7C	OL CHIKI PHAARKAA
        chars.append(0x1C7D)  #uni1C7D	OL CHIKI AHAD
        chars.append(0x1C7E)  #uni1C7E	OL CHIKI PUNCTUATION MUCAAD
        chars.append(0x1C7F)  #uni1C7F	OL CHIKI PUNCTUATION DOUBLE MUCAAD
        return chars


