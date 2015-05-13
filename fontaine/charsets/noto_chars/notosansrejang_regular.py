# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansRejang-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0xA94B)  #uniA94B	REJANG VOWEL SIGN O
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0xA930)  #uniA930	REJANG LETTER KA
        chars.append(0xA931)  #uniA931	REJANG LETTER GA
        chars.append(0xA932)  #uniA932	REJANG LETTER NGA
        chars.append(0xA933)  #uniA933	REJANG LETTER TA
        chars.append(0xA934)  #uniA934	REJANG LETTER DA
        chars.append(0xA935)  #uniA935	REJANG LETTER NA
        chars.append(0xA936)  #uniA936	REJANG LETTER PA
        chars.append(0xA937)  #uniA937	REJANG LETTER BA
        chars.append(0xA938)  #uniA938	REJANG LETTER MA
        chars.append(0xA939)  #uniA939	REJANG LETTER CA
        chars.append(0xA93A)  #uniA93A	REJANG LETTER JA
        chars.append(0xA93B)  #uniA93B	REJANG LETTER NYA
        chars.append(0xA93C)  #uniA93C	REJANG LETTER SA
        chars.append(0xA93D)  #uniA93D	REJANG LETTER RA
        chars.append(0xA93E)  #uniA93E	REJANG LETTER LA
        chars.append(0xA93F)  #uniA93F	REJANG LETTER YA
        chars.append(0xA940)  #uniA940	REJANG LETTER WA
        chars.append(0xA941)  #uniA941	REJANG LETTER HA
        chars.append(0xA942)  #uniA942	REJANG LETTER MBA
        chars.append(0xA943)  #uniA943	REJANG LETTER NGGA
        chars.append(0xA944)  #uniA944	REJANG LETTER NDA
        chars.append(0xA945)  #uniA945	REJANG LETTER NYJA
        chars.append(0xA946)  #uniA946	REJANG LETTER A
        chars.append(0xA947)  #uniA947	REJANG VOWEL SIGN I
        chars.append(0xA948)  #uniA948	REJANG VOWEL SIGN U
        chars.append(0xA949)  #uniA949	REJANG VOWEL SIGN E
        chars.append(0xA94A)  #uniA94A	REJANG VOWEL SIGN AI
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xA94C)  #uniA94C	REJANG VOWEL SIGN AU
        chars.append(0xA94D)  #uniA94D	REJANG VOWEL SIGN EU
        chars.append(0xA94E)  #uniA94E	REJANG VOWEL SIGN EA
        chars.append(0xA94F)  #uniA94F	REJANG CONSONANT SIGN NG
        chars.append(0xA950)  #uniA950	REJANG CONSONANT SIGN N
        chars.append(0xA951)  #uniA951	REJANG CONSONANT SIGN R
        chars.append(0xA952)  #uniA952	REJANG CONSONANT SIGN H
        chars.append(0xA953)  #uniA953	REJANG VIRAMA
        chars.append(0xA95F)  #uniA95F	REJANG SECTION MARK
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


