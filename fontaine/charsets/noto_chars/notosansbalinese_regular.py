# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansBalinese-Regular'
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
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x1B00)  #uni1B00	BALINESE SIGN ULU RICEM
        chars.append(0x1B01)  #uni1B01	BALINESE SIGN ULU CANDRA
        chars.append(0x1B02)  #uni1B02	BALINESE SIGN CECEK
        chars.append(0x1B03)  #uni1B03	BALINESE SIGN SURANG
        chars.append(0x1B04)  #uni1B04	BALINESE SIGN BISAH
        chars.append(0x1B05)  #uni1B05	BALINESE LETTER AKARA
        chars.append(0x1B06)  #uni1B06	BALINESE LETTER AKARA TEDUNG
        chars.append(0x1B07)  #uni1B07	BALINESE LETTER IKARA
        chars.append(0x1B08)  #uni1B08	BALINESE LETTER IKARA TEDUNG
        chars.append(0x1B09)  #uni1B09	BALINESE LETTER UKARA
        chars.append(0x1B0A)  #uni1B0A	BALINESE LETTER UKARA TEDUNG
        chars.append(0x1B0B)  #uni1B0B	BALINESE LETTER RA REPA
        chars.append(0x1B0C)  #uni1B0C	BALINESE LETTER RA REPA TEDUNG
        chars.append(0x1B0D)  #uni1B0D	BALINESE LETTER LA LENGA
        chars.append(0x1B0E)  #uni1B0E	BALINESE LETTER LA LENGA TEDUNG
        chars.append(0x1B0F)  #uni1B0F	BALINESE LETTER EKARA
        chars.append(0x1B10)  #uni1B10	BALINESE LETTER AIKARA
        chars.append(0x1B11)  #uni1B11	BALINESE LETTER OKARA
        chars.append(0x1B12)  #uni1B12	BALINESE LETTER OKARA TEDUNG
        chars.append(0x1B13)  #uni1B13	BALINESE LETTER KA
        chars.append(0x1B14)  #uni1B14	BALINESE LETTER KA MAHAPRANA
        chars.append(0x1B15)  #uni1B15	BALINESE LETTER GA
        chars.append(0x1B16)  #uni1B16	BALINESE LETTER GA GORA
        chars.append(0x1B17)  #uni1B17	BALINESE LETTER NGA
        chars.append(0x1B18)  #uni1B18	BALINESE LETTER CA
        chars.append(0x1B19)  #uni1B19	BALINESE LETTER CA LACA
        chars.append(0x1B1A)  #uni1B1A	BALINESE LETTER JA
        chars.append(0x1B1B)  #uni1B1B	BALINESE LETTER JA JERA
        chars.append(0x1B1C)  #uni1B1C	BALINESE LETTER NYA
        chars.append(0x1B1D)  #uni1B1D	BALINESE LETTER TA LATIK
        chars.append(0x1B1E)  #uni1B1E	BALINESE LETTER TA MURDA MAHAPRANA
        chars.append(0x1B1F)  #uni1B1F	BALINESE LETTER DA MURDA ALPAPRANA
        chars.append(0x1B20)  #uni1B20	BALINESE LETTER DA MURDA MAHAPRANA
        chars.append(0x1B21)  #uni1B21	BALINESE LETTER NA RAMBAT
        chars.append(0x1B22)  #uni1B22	BALINESE LETTER TA
        chars.append(0x1B23)  #uni1B23	BALINESE LETTER TA TAWA
        chars.append(0x1B24)  #uni1B24	BALINESE LETTER DA
        chars.append(0x1B25)  #uni1B25	BALINESE LETTER DA MADU
        chars.append(0x1B26)  #uni1B26	BALINESE LETTER NA
        chars.append(0x1B27)  #uni1B27	BALINESE LETTER PA
        chars.append(0x1B28)  #uni1B28	BALINESE LETTER PA KAPAL
        chars.append(0x1B29)  #uni1B29	BALINESE LETTER BA
        chars.append(0x1B2A)  #uni1B2A	BALINESE LETTER BA KEMBANG
        chars.append(0x1B2B)  #uni1B2B	BALINESE LETTER MA
        chars.append(0x1B2C)  #uni1B2C	BALINESE LETTER YA
        chars.append(0x1B2D)  #uni1B2D	BALINESE LETTER RA
        chars.append(0x1B2E)  #uni1B2E	BALINESE LETTER LA
        chars.append(0x1B2F)  #uni1B2F	BALINESE LETTER WA
        chars.append(0x1B30)  #uni1B30	BALINESE LETTER SA SAGA
        chars.append(0x1B31)  #uni1B31	BALINESE LETTER SA SAPA
        chars.append(0x1B32)  #uni1B32	BALINESE LETTER SA
        chars.append(0x1B33)  #uni1B33	BALINESE LETTER HA
        chars.append(0x1B34)  #uni1B34	BALINESE SIGN REREKAN
        chars.append(0x1B35)  #uni1B35	BALINESE VOWEL SIGN TEDUNG
        chars.append(0x1B36)  #uni1B36	BALINESE VOWEL SIGN ULU
        chars.append(0x1B37)  #uni1B37	BALINESE VOWEL SIGN ULU SARI
        chars.append(0x1B38)  #uni1B38	BALINESE VOWEL SIGN SUKU
        chars.append(0x1B39)  #uni1B39	BALINESE VOWEL SIGN SUKU ILUT
        chars.append(0x1B3A)  #uni1B3A	BALINESE VOWEL SIGN RA REPA
        chars.append(0x1B3B)  #uni1B3B	BALINESE VOWEL SIGN RA REPA TEDUNG
        chars.append(0x1B3C)  #uni1B3C	BALINESE VOWEL SIGN LA LENGA
        chars.append(0x1B3D)  #uni1B3D	BALINESE VOWEL SIGN LA LENGA TEDUNG
        chars.append(0x1B3E)  #uni1B3E	BALINESE VOWEL SIGN TALING
        chars.append(0x1B3F)  #uni1B3F	BALINESE VOWEL SIGN TALING REPA
        chars.append(0x1B40)  #uni1B40	BALINESE VOWEL SIGN TALING TEDUNG
        chars.append(0x1B41)  #uni1B41	BALINESE VOWEL SIGN TALING REPA TEDUNG
        chars.append(0x1B42)  #uni1B42	BALINESE VOWEL SIGN PEPET
        chars.append(0x1B43)  #uni1B43	BALINESE VOWEL SIGN PEPET TEDUNG
        chars.append(0x1B44)  #uni1B44	BALINESE ADEG ADEG
        chars.append(0x1B45)  #uni1B45	BALINESE LETTER KAF SASAK
        chars.append(0x1B46)  #uni1B46	BALINESE LETTER KHOT SASAK
        chars.append(0x1B47)  #uni1B47	BALINESE LETTER TZIR SASAK
        chars.append(0x1B48)  #uni1B48	BALINESE LETTER EF SASAK
        chars.append(0x1B49)  #uni1B49	BALINESE LETTER VE SASAK
        chars.append(0x1B4A)  #uni1B4A	BALINESE LETTER ZAL SASAK
        chars.append(0x1B4B)  #uni1B4B	BALINESE LETTER ASYURA SASAK
        chars.append(0x1B50)  #uni1B50	BALINESE DIGIT ZERO
        chars.append(0x1B51)  #uni1B51	BALINESE DIGIT ONE
        chars.append(0x1B52)  #uni1B52	BALINESE DIGIT TWO
        chars.append(0x1B53)  #uni1B53	BALINESE DIGIT THREE
        chars.append(0x1B54)  #uni1B54	BALINESE DIGIT FOUR
        chars.append(0x1B55)  #uni1B55	BALINESE DIGIT FIVE
        chars.append(0x1B56)  #uni1B56	BALINESE DIGIT SIX
        chars.append(0x1B57)  #uni1B57	BALINESE DIGIT SEVEN
        chars.append(0x1B58)  #uni1B58	BALINESE DIGIT EIGHT
        chars.append(0x1B59)  #uni1B59	BALINESE DIGIT NINE
        chars.append(0x1B5A)  #uni1B5A	BALINESE PANTI
        chars.append(0x1B5B)  #uni1B5B	BALINESE PAMADA
        chars.append(0x1B5C)  #uni1B5C	BALINESE WINDU
        chars.append(0x1B5D)  #uni1B5D	BALINESE CARIK PAMUNGKAH
        chars.append(0x1B5E)  #uni1B5E	BALINESE CARIK SIKI
        chars.append(0x1B5F)  #uni1B5F	BALINESE CARIK PAREREN
        chars.append(0x1B60)  #uni1B60	BALINESE PAMENENG
        chars.append(0x1B61)  #uni1B61	BALINESE MUSICAL SYMBOL DONG
        chars.append(0x1B62)  #uni1B62	BALINESE MUSICAL SYMBOL DENG
        chars.append(0x1B63)  #uni1B63	BALINESE MUSICAL SYMBOL DUNG
        chars.append(0x1B64)  #uni1B64	BALINESE MUSICAL SYMBOL DANG
        chars.append(0x1B65)  #uni1B65	BALINESE MUSICAL SYMBOL DANG SURANG
        chars.append(0x1B66)  #uni1B66	BALINESE MUSICAL SYMBOL DING
        chars.append(0x1B67)  #uni1B67	BALINESE MUSICAL SYMBOL DAENG
        chars.append(0x1B68)  #uni1B68	BALINESE MUSICAL SYMBOL DEUNG
        chars.append(0x1B69)  #uni1B69	BALINESE MUSICAL SYMBOL DAING
        chars.append(0x1B6A)  #uni1B6A	BALINESE MUSICAL SYMBOL DANG GEDE
        chars.append(0x1B6B)  #uni1B6B	BALINESE MUSICAL SYMBOL COMBINING TEGEH
        chars.append(0x1B6C)  #uni1B6C	BALINESE MUSICAL SYMBOL COMBINING ENDEP
        chars.append(0x1B6D)  #uni1B6D	BALINESE MUSICAL SYMBOL COMBINING KEMPUL
        chars.append(0x1B6E)  #uni1B6E	BALINESE MUSICAL SYMBOL COMBINING KEMPLI
        chars.append(0x1B6F)  #uni1B6F	BALINESE MUSICAL SYMBOL COMBINING JEGOGAN
        chars.append(0x1B70)  #uni1B70	BALINESE MUSICAL SYMBOL COMBINING KEMPUL WITH JEGOGAN
        chars.append(0x1B71)  #uni1B71	BALINESE MUSICAL SYMBOL COMBINING KEMPLI WITH JEGOGAN
        chars.append(0x1B72)  #uni1B72	BALINESE MUSICAL SYMBOL COMBINING BENDE
        chars.append(0x1B73)  #uni1B73	BALINESE MUSICAL SYMBOL COMBINING GONG
        chars.append(0x1B74)  #uni1B74	BALINESE MUSICAL SYMBOL RIGHT-HAND OPEN DUG
        chars.append(0x1B75)  #uni1B75	BALINESE MUSICAL SYMBOL RIGHT-HAND OPEN DAG
        chars.append(0x1B76)  #uni1B76	BALINESE MUSICAL SYMBOL RIGHT-HAND CLOSED TUK
        chars.append(0x1B77)  #uni1B77	BALINESE MUSICAL SYMBOL RIGHT-HAND CLOSED TAK
        chars.append(0x1B78)  #uni1B78	BALINESE MUSICAL SYMBOL LEFT-HAND OPEN PANG
        chars.append(0x1B79)  #uni1B79	BALINESE MUSICAL SYMBOL LEFT-HAND OPEN PUNG
        chars.append(0x1B7A)  #uni1B7A	BALINESE MUSICAL SYMBOL LEFT-HAND CLOSED PLAK
        chars.append(0x1B7B)  #uni1B7B	BALINESE MUSICAL SYMBOL LEFT-HAND CLOSED PLUK
        chars.append(0x1B7C)  #uni1B7C	BALINESE MUSICAL SYMBOL LEFT-HAND OPEN PING
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        return chars


