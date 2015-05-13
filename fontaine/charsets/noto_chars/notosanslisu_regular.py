# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansLisu-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x02BC)  #uni02BC	MODIFIER LETTER APOSTROPHE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x02CD)  #uni02CD	MODIFIER LETTER LOW MACRON
        chars.append(0xA4D0)  #uniA4D0	LISU LETTER BA
        chars.append(0xA4D1)  #uniA4D1	LISU LETTER PA
        chars.append(0xA4D2)  #uniA4D2	LISU LETTER PHA
        chars.append(0xA4D3)  #uniA4D3	LISU LETTER DA
        chars.append(0xA4D4)  #uniA4D4	LISU LETTER TA
        chars.append(0xA4D5)  #uniA4D5	LISU LETTER THA
        chars.append(0xA4D6)  #uniA4D6	LISU LETTER GA
        chars.append(0xA4D7)  #uniA4D7	LISU LETTER KA
        chars.append(0xA4D8)  #uniA4D8	LISU LETTER KHA
        chars.append(0xA4D9)  #uniA4D9	LISU LETTER JA
        chars.append(0xA4DA)  #uniA4DA	LISU LETTER CA
        chars.append(0xA4DB)  #uniA4DB	LISU LETTER CHA
        chars.append(0xA4DC)  #uniA4DC	LISU LETTER DZA
        chars.append(0xA4DD)  #uniA4DD	LISU LETTER TSA
        chars.append(0xA4DE)  #uniA4DE	LISU LETTER TSHA
        chars.append(0xA4DF)  #uniA4DF	LISU LETTER MA
        chars.append(0xA4E0)  #uniA4E0	LISU LETTER NA
        chars.append(0xA4E1)  #uniA4E1	LISU LETTER LA
        chars.append(0xA4E2)  #uniA4E2	LISU LETTER SA
        chars.append(0xA4E3)  #uniA4E3	LISU LETTER ZHA
        chars.append(0xA4E4)  #uniA4E4	LISU LETTER ZA
        chars.append(0xA4E5)  #uniA4E5	LISU LETTER NGA
        chars.append(0xA4E6)  #uniA4E6	LISU LETTER HA
        chars.append(0xA4E7)  #uniA4E7	LISU LETTER XA
        chars.append(0xA4E8)  #uniA4E8	LISU LETTER HHA
        chars.append(0xA4E9)  #uniA4E9	LISU LETTER FA
        chars.append(0xA4EA)  #uniA4EA	LISU LETTER WA
        chars.append(0xA4EB)  #uniA4EB	LISU LETTER SHA
        chars.append(0xA4EC)  #uniA4EC	LISU LETTER YA
        chars.append(0xA4ED)  #uniA4ED	LISU LETTER GHA
        chars.append(0xA4EE)  #uniA4EE	LISU LETTER A
        chars.append(0xA4EF)  #uniA4EF	LISU LETTER AE
        chars.append(0xA4F0)  #uniA4F0	LISU LETTER E
        chars.append(0xA4F1)  #uniA4F1	LISU LETTER EU
        chars.append(0xA4F2)  #uniA4F2	LISU LETTER I
        chars.append(0xA4F3)  #uniA4F3	LISU LETTER O
        chars.append(0xA4F4)  #uniA4F4	LISU LETTER U
        chars.append(0xA4F5)  #uniA4F5	LISU LETTER UE
        chars.append(0xA4F6)  #uniA4F6	LISU LETTER UH
        chars.append(0xA4F7)  #uniA4F7	LISU LETTER OE
        chars.append(0xA4F8)  #uniA4F8	LISU LETTER TONE MYA TI
        chars.append(0xA4F9)  #uniA4F9	LISU LETTER TONE NA PO
        chars.append(0xA4FA)  #uniA4FA	LISU LETTER TONE MYA CYA
        chars.append(0xA4FB)  #uniA4FB	LISU LETTER TONE MYA BO
        chars.append(0xA4FC)  #uniA4FC	LISU LETTER TONE MYA NA
        chars.append(0xA4FD)  #uniA4FD	LISU LETTER TONE MYA JEU
        chars.append(0xA4FE)  #uniA4FE	LISU PUNCTUATION COMMA
        chars.append(0xA4FF)  #uniA4FF	LISU PUNCTUATION FULL STOP
        return chars


