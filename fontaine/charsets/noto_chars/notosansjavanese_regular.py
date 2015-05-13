# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansJavanese-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xA9CC)  #uniA9CC	JAVANESE PADA PISELEH
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xA980)  #uniA980	JAVANESE SIGN PANYANGGA
        chars.append(0xA981)  #uniA981	JAVANESE SIGN CECAK
        chars.append(0xA982)  #uniA982	JAVANESE SIGN LAYAR
        chars.append(0xA983)  #uniA983	JAVANESE SIGN WIGNYAN
        chars.append(0xA984)  #uniA984	JAVANESE LETTER A
        chars.append(0xA985)  #uniA985	JAVANESE LETTER I KAWI
        chars.append(0xA986)  #uniA986	JAVANESE LETTER I
        chars.append(0xA987)  #uniA987	JAVANESE LETTER II
        chars.append(0xA988)  #uniA988	JAVANESE LETTER U
        chars.append(0xA989)  #uniA989	JAVANESE LETTER PA CEREK
        chars.append(0xA98A)  #uniA98A	JAVANESE LETTER NGA LELET
        chars.append(0xA98B)  #uniA98B	JAVANESE LETTER NGA LELET RASWADI
        chars.append(0xA98C)  #uniA98C	JAVANESE LETTER E
        chars.append(0xA98D)  #uniA98D	JAVANESE LETTER AI
        chars.append(0xA98E)  #uniA98E	JAVANESE LETTER O
        chars.append(0xA98F)  #uniA98F	JAVANESE LETTER KA
        chars.append(0xA990)  #uniA990	JAVANESE LETTER KA SASAK
        chars.append(0xA991)  #uniA991	JAVANESE LETTER KA MURDA
        chars.append(0xA992)  #uniA992	JAVANESE LETTER GA
        chars.append(0xA993)  #uniA993	JAVANESE LETTER GA MURDA
        chars.append(0xA994)  #uniA994	JAVANESE LETTER NGA
        chars.append(0xA995)  #uniA995	JAVANESE LETTER CA
        chars.append(0xA996)  #uniA996	JAVANESE LETTER CA MURDA
        chars.append(0xA997)  #uniA997	JAVANESE LETTER JA
        chars.append(0xA998)  #uniA998	JAVANESE LETTER NYA MURDA
        chars.append(0xA999)  #uniA999	JAVANESE LETTER JA MAHAPRANA
        chars.append(0xA99A)  #uniA99A	JAVANESE LETTER NYA
        chars.append(0xA99B)  #uniA99B	JAVANESE LETTER TTA
        chars.append(0xA99C)  #uniA99C	JAVANESE LETTER TTA MAHAPRANA
        chars.append(0xA99D)  #uniA99D	JAVANESE LETTER DDA
        chars.append(0xA99E)  #uniA99E	JAVANESE LETTER DDA MAHAPRANA
        chars.append(0xA99F)  #uniA99F	JAVANESE LETTER NA MURDA
        chars.append(0xA9A0)  #uniA9A0	JAVANESE LETTER TA
        chars.append(0xA9A1)  #uniA9A1	JAVANESE LETTER TA MURDA
        chars.append(0xA9A2)  #uniA9A2	JAVANESE LETTER DA
        chars.append(0xA9A3)  #uniA9A3	JAVANESE LETTER DA MAHAPRANA
        chars.append(0xA9A4)  #uniA9A4	JAVANESE LETTER NA
        chars.append(0xA9A5)  #uniA9A5	JAVANESE LETTER PA
        chars.append(0xA9A6)  #uniA9A6	JAVANESE LETTER PA MURDA
        chars.append(0xA9A7)  #uniA9A7	JAVANESE LETTER BA
        chars.append(0xA9A8)  #uniA9A8	JAVANESE LETTER BA MURDA
        chars.append(0xA9A9)  #uniA9A9	JAVANESE LETTER MA
        chars.append(0xA9AA)  #uniA9AA	JAVANESE LETTER YA
        chars.append(0xA9AB)  #uniA9AB	JAVANESE LETTER RA
        chars.append(0xA9AC)  #uniA9AC	JAVANESE LETTER RA AGUNG
        chars.append(0xA9AD)  #uniA9AD	JAVANESE LETTER LA
        chars.append(0xA9AE)  #uniA9AE	JAVANESE LETTER WA
        chars.append(0xA9AF)  #uniA9AF	JAVANESE LETTER SA MURDA
        chars.append(0xA9B0)  #uniA9B0	JAVANESE LETTER SA MAHAPRANA
        chars.append(0xA9B1)  #uniA9B1	JAVANESE LETTER SA
        chars.append(0xA9B2)  #uniA9B2	JAVANESE LETTER HA
        chars.append(0xA9B3)  #uniA9B3	JAVANESE SIGN CECAK TELU
        chars.append(0xA9B4)  #uniA9B4	JAVANESE VOWEL SIGN TARUNG
        chars.append(0xA9B5)  #uniA9B5	JAVANESE VOWEL SIGN TOLONG
        chars.append(0xA9B6)  #uniA9B6	JAVANESE VOWEL SIGN WULU
        chars.append(0xA9B7)  #uniA9B7	JAVANESE VOWEL SIGN WULU MELIK
        chars.append(0xA9B8)  #uniA9B8	JAVANESE VOWEL SIGN SUKU
        chars.append(0xA9B9)  #uniA9B9	JAVANESE VOWEL SIGN SUKU MENDUT
        chars.append(0xA9BA)  #uniA9BA	JAVANESE VOWEL SIGN TALING
        chars.append(0xA9BB)  #uniA9BB	JAVANESE VOWEL SIGN DIRGA MURE
        chars.append(0xA9BC)  #uniA9BC	JAVANESE VOWEL SIGN PEPET
        chars.append(0xA9BD)  #uniA9BD	JAVANESE CONSONANT SIGN KERET
        chars.append(0xA9BE)  #uniA9BE	JAVANESE CONSONANT SIGN PENGKAL
        chars.append(0xA9BF)  #uniA9BF	JAVANESE CONSONANT SIGN CAKRA
        chars.append(0xA9C0)  #uniA9C0	JAVANESE PANGKON
        chars.append(0xA9C1)  #uniA9C1	JAVANESE LEFT RERENGGAN
        chars.append(0xA9C2)  #uniA9C2	JAVANESE RIGHT RERENGGAN
        chars.append(0xA9C3)  #uniA9C3	JAVANESE PADA ANDAP
        chars.append(0xA9C4)  #uniA9C4	JAVANESE PADA MADYA
        chars.append(0xA9C5)  #uniA9C5	JAVANESE PADA LUHUR
        chars.append(0xA9C6)  #uniA9C6	JAVANESE PADA WINDU
        chars.append(0xA9C7)  #uniA9C7	JAVANESE PADA PANGKAT
        chars.append(0xA9C8)  #uniA9C8	JAVANESE PADA LINGSA
        chars.append(0xA9C9)  #uniA9C9	JAVANESE PADA LUNGSI
        chars.append(0xA9CA)  #uniA9CA	JAVANESE PADA ADEG
        chars.append(0xA9CB)  #uniA9CB	JAVANESE PADA ADEG ADEG
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0xA9CD)  #uniA9CD	JAVANESE TURNED PADA PISELEH
        chars.append(0xA9CF)  #uniA9CF	JAVANESE PANGRANGKEP
        chars.append(0xA9D0)  #uniA9D0	JAVANESE DIGIT ZERO
        chars.append(0xA9D1)  #uniA9D1	JAVANESE DIGIT ONE
        chars.append(0xA9D2)  #uniA9D2	JAVANESE DIGIT TWO
        chars.append(0xA9D3)  #uniA9D3	JAVANESE DIGIT THREE
        chars.append(0xA9D4)  #uniA9D4	JAVANESE DIGIT FOUR
        chars.append(0xA9D5)  #uniA9D5	JAVANESE DIGIT FIVE
        chars.append(0xA9D6)  #uniA9D6	JAVANESE DIGIT SIX
        chars.append(0xA9D7)  #uniA9D7	JAVANESE DIGIT SEVEN
        chars.append(0xA9D8)  #uniA9D8	JAVANESE DIGIT EIGHT
        chars.append(0xA9D9)  #uniA9D9	JAVANESE DIGIT NINE
        chars.append(0xA9DE)  #uniA9DE	JAVANESE PADA TIRTA TUMETES
        chars.append(0xA9DF)  #uniA9DF	JAVANESE PADA ISEN-ISEN
        return chars


