# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansBuginese-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x1A01)  #uni1A01	BUGINESE LETTER GA
        chars.append(0x1A02)  #uni1A02	BUGINESE LETTER NGA
        chars.append(0x1A03)  #uni1A03	BUGINESE LETTER NGKA
        chars.append(0x1A04)  #uni1A04	BUGINESE LETTER PA
        chars.append(0x1A05)  #uni1A05	BUGINESE LETTER BA
        chars.append(0x1A06)  #uni1A06	BUGINESE LETTER MA
        chars.append(0x1A07)  #uni1A07	BUGINESE LETTER MPA
        chars.append(0x1A08)  #uni1A08	BUGINESE LETTER TA
        chars.append(0x1A09)  #uni1A09	BUGINESE LETTER DA
        chars.append(0x1A0A)  #uni1A0A	BUGINESE LETTER NA
        chars.append(0x1A0B)  #uni1A0B	BUGINESE LETTER NRA
        chars.append(0x1A0C)  #uni1A0C	BUGINESE LETTER CA
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1A0E)  #uni1A0E	BUGINESE LETTER NYA
        chars.append(0x1A0F)  #uni1A0F	BUGINESE LETTER NYCA
        chars.append(0x1A10)  #uni1A10	BUGINESE LETTER YA
        chars.append(0x1A11)  #uni1A11	BUGINESE LETTER RA
        chars.append(0x1A12)  #uni1A12	BUGINESE LETTER LA
        chars.append(0x1A13)  #uni1A13	BUGINESE LETTER VA
        chars.append(0x1A14)  #uni1A14	BUGINESE LETTER SA
        chars.append(0x1A15)  #uni1A15	BUGINESE LETTER A
        chars.append(0x1A16)  #uni1A16	BUGINESE LETTER HA
        chars.append(0x1A17)  #uni1A17	BUGINESE VOWEL SIGN I
        chars.append(0x1A18)  #uni1A18	BUGINESE VOWEL SIGN U
        chars.append(0x1A19)  #uni1A19	BUGINESE VOWEL SIGN E
        chars.append(0x1A1A)  #uni1A1A	BUGINESE VOWEL SIGN O
        chars.append(0x1A1B)  #uni1A1B	BUGINESE VOWEL SIGN AE
        chars.append(0x1A1E)  #uni1A1E	BUGINESE PALLAWA
        chars.append(0x1A1F)  #uni1A1F	BUGINESE END OF SECTION
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x1A0D)  #uni1A0D	BUGINESE LETTER JA
        chars.append(0x1A00)  #uni1A00	BUGINESE LETTER KA
        chars.append(0xA9CF)  #uniA9CF	JAVANESE PANGRANGKEP
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


