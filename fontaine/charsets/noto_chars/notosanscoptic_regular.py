# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansCoptic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0xFE24)  #uniFE24	COMBINING MACRON LEFT HALF
        chars.append(0xFE25)  #uniFE25	COMBINING MACRON RIGHT HALF
        chars.append(0xFE26)  #uniFE26	COMBINING CONJOINING MACRON
        chars.append(0x0251)  #uni0251	LATIN SMALL LETTER ALPHA
        chars.append(0x0254)  #uni0254	LATIN SMALL LETTER OPEN O
        chars.append(0x0259)  #uni0259	LATIN SMALL LETTER SCHWA
        chars.append(0x025B)  #uni025B	LATIN SMALL LETTER OPEN E
        chars.append(0x025F)  #uni025F	LATIN SMALL LETTER DOTLESS J WITH STROKE
        chars.append(0x0261)  #uni0261	LATIN SMALL LETTER SCRIPT G
        chars.append(0x0272)  #uni0272	LATIN SMALL LETTER N WITH LEFT HOOK
        chars.append(0x027E)  #uni027E	LATIN SMALL LETTER R WITH FISHHOOK
        chars.append(0x2C80)  #uni2C80	COPTIC CAPITAL LETTER ALFA
        chars.append(0x2C81)  #uni2C81	COPTIC SMALL LETTER ALFA
        chars.append(0x2C82)  #uni2C82	COPTIC CAPITAL LETTER VIDA
        chars.append(0x0283)  #uni0283	LATIN SMALL LETTER ESH
        chars.append(0x2C84)  #uni2C84	COPTIC CAPITAL LETTER GAMMA
        chars.append(0x2C85)  #uni2C85	COPTIC SMALL LETTER GAMMA
        chars.append(0x2C86)  #uni2C86	COPTIC CAPITAL LETTER DALDA
        chars.append(0x2C87)  #uni2C87	COPTIC SMALL LETTER DALDA
        chars.append(0x2C88)  #uni2C88	COPTIC CAPITAL LETTER EIE
        chars.append(0x2C89)  #uni2C89	COPTIC SMALL LETTER EIE
        chars.append(0x2C8A)  #uni2C8A	COPTIC CAPITAL LETTER SOU
        chars.append(0x2C8B)  #uni2C8B	COPTIC SMALL LETTER SOU
        chars.append(0x2C8C)  #uni2C8C	COPTIC CAPITAL LETTER ZATA
        chars.append(0x2C8D)  #uni2C8D	COPTIC SMALL LETTER ZATA
        chars.append(0x2C8E)  #uni2C8E	COPTIC CAPITAL LETTER HATE
        chars.append(0x2C8F)  #uni2C8F	COPTIC SMALL LETTER HATE
        chars.append(0x2C90)  #uni2C90	COPTIC CAPITAL LETTER THETHE
        chars.append(0x2C91)  #uni2C91	COPTIC SMALL LETTER THETHE
        chars.append(0x0292)  #uni0292	LATIN SMALL LETTER EZH
        chars.append(0x2C93)  #uni2C93	COPTIC SMALL LETTER IAUDA
        chars.append(0x2C94)  #uni2C94	COPTIC CAPITAL LETTER KAPA
        chars.append(0x2C95)  #uni2C95	COPTIC SMALL LETTER KAPA
        chars.append(0x2C96)  #uni2C96	COPTIC CAPITAL LETTER LAULA
        chars.append(0x2C97)  #uni2C97	COPTIC SMALL LETTER LAULA
        chars.append(0x2C98)  #uni2C98	COPTIC CAPITAL LETTER MI
        chars.append(0x2C99)  #uni2C99	COPTIC SMALL LETTER MI
        chars.append(0x2C9A)  #uni2C9A	COPTIC CAPITAL LETTER NI
        chars.append(0x2C9B)  #uni2C9B	COPTIC SMALL LETTER NI
        chars.append(0x2C9C)  #uni2C9C	COPTIC CAPITAL LETTER KSI
        chars.append(0x2C9D)  #uni2C9D	COPTIC SMALL LETTER KSI
        chars.append(0x2C9E)  #uni2C9E	COPTIC CAPITAL LETTER O
        chars.append(0x2C9F)  #uni2C9F	COPTIC SMALL LETTER O
        chars.append(0x2CA0)  #uni2CA0	COPTIC CAPITAL LETTER PI
        chars.append(0x2CA1)  #uni2CA1	COPTIC SMALL LETTER PI
        chars.append(0x2CA2)  #uni2CA2	COPTIC CAPITAL LETTER RO
        chars.append(0x2CA3)  #uni2CA3	COPTIC SMALL LETTER RO
        chars.append(0x02A4)  #uni02A4	LATIN SMALL LETTER DEZH DIGRAPH
        chars.append(0x2CA5)  #uni2CA5	COPTIC SMALL LETTER SIMA
        chars.append(0x2CA6)  #uni2CA6	COPTIC CAPITAL LETTER TAU
        chars.append(0x02A7)  #uni02A7	LATIN SMALL LETTER TESH DIGRAPH
        chars.append(0x2CA8)  #uni2CA8	COPTIC CAPITAL LETTER UA
        chars.append(0x2CA9)  #uni2CA9	COPTIC SMALL LETTER UA
        chars.append(0x2CAA)  #uni2CAA	COPTIC CAPITAL LETTER FI
        chars.append(0x2CAB)  #uni2CAB	COPTIC SMALL LETTER FI
        chars.append(0x2CAC)  #uni2CAC	COPTIC CAPITAL LETTER KHI
        chars.append(0x2CAD)  #uni2CAD	COPTIC SMALL LETTER KHI
        chars.append(0x2CAE)  #uni2CAE	COPTIC CAPITAL LETTER PSI
        chars.append(0x2CAF)  #uni2CAF	COPTIC SMALL LETTER PSI
        chars.append(0x2CB0)  #uni2CB0	COPTIC CAPITAL LETTER OOU
        chars.append(0x2CB1)  #uni2CB1	COPTIC SMALL LETTER OOU
        chars.append(0x2CB2)  #uni2CB2	COPTIC CAPITAL LETTER DIALECT-P ALEF
        chars.append(0x2CB3)  #uni2CB3	COPTIC SMALL LETTER DIALECT-P ALEF
        chars.append(0x2CB4)  #uni2CB4	COPTIC CAPITAL LETTER OLD COPTIC AIN
        chars.append(0x2CB5)  #uni2CB5	COPTIC SMALL LETTER OLD COPTIC AIN
        chars.append(0x2CB6)  #uni2CB6	COPTIC CAPITAL LETTER CRYPTOGRAMMIC EIE
        chars.append(0x2CB7)  #uni2CB7	COPTIC SMALL LETTER CRYPTOGRAMMIC EIE
        chars.append(0x2CB8)  #uni2CB8	COPTIC CAPITAL LETTER DIALECT-P KAPA
        chars.append(0x2CB9)  #uni2CB9	COPTIC SMALL LETTER DIALECT-P KAPA
        chars.append(0x2CBA)  #uni2CBA	COPTIC CAPITAL LETTER DIALECT-P NI
        chars.append(0x2CBB)  #uni2CBB	COPTIC SMALL LETTER DIALECT-P NI
        chars.append(0x2CBC)  #uni2CBC	COPTIC CAPITAL LETTER CRYPTOGRAMMIC NI
        chars.append(0x2CBD)  #uni2CBD	COPTIC SMALL LETTER CRYPTOGRAMMIC NI
        chars.append(0x2CBE)  #uni2CBE	COPTIC CAPITAL LETTER OLD COPTIC OOU
        chars.append(0x2CBF)  #uni2CBF	COPTIC SMALL LETTER OLD COPTIC OOU
        chars.append(0x2CC0)  #uni2CC0	COPTIC CAPITAL LETTER SAMPI
        chars.append(0x2CC1)  #uni2CC1	COPTIC SMALL LETTER SAMPI
        chars.append(0x2CC2)  #uni2CC2	COPTIC CAPITAL LETTER CROSSED SHEI
        chars.append(0x2CC3)  #uni2CC3	COPTIC SMALL LETTER CROSSED SHEI
        chars.append(0x2CC4)  #uni2CC4	COPTIC CAPITAL LETTER OLD COPTIC SHEI
        chars.append(0x2CC5)  #uni2CC5	COPTIC SMALL LETTER OLD COPTIC SHEI
        chars.append(0x2CC6)  #uni2CC6	COPTIC CAPITAL LETTER OLD COPTIC ESH
        chars.append(0x02C7)  #caron	CARON
        chars.append(0x2CC8)  #uni2CC8	COPTIC CAPITAL LETTER AKHMIMIC KHEI
        chars.append(0x2CC9)  #uni2CC9	COPTIC SMALL LETTER AKHMIMIC KHEI
        chars.append(0x2CCA)  #uni2CCA	COPTIC CAPITAL LETTER DIALECT-P HORI
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x2CCC)  #uni2CCC	COPTIC CAPITAL LETTER OLD COPTIC HORI
        chars.append(0x2CCD)  #uni2CCD	COPTIC SMALL LETTER OLD COPTIC HORI
        chars.append(0x2CCE)  #uni2CCE	COPTIC CAPITAL LETTER OLD COPTIC HA
        chars.append(0x2CCF)  #uni2CCF	COPTIC SMALL LETTER OLD COPTIC HA
        chars.append(0x02D0)  #uni02D0	MODIFIER LETTER TRIANGULAR COLON
        chars.append(0x2CD1)  #uni2CD1	COPTIC SMALL LETTER L-SHAPED HA
        chars.append(0x2CD2)  #uni2CD2	COPTIC CAPITAL LETTER OLD COPTIC HEI
        chars.append(0x2CD3)  #uni2CD3	COPTIC SMALL LETTER OLD COPTIC HEI
        chars.append(0x2CD4)  #uni2CD4	COPTIC CAPITAL LETTER OLD COPTIC HAT
        chars.append(0x2CD5)  #uni2CD5	COPTIC SMALL LETTER OLD COPTIC HAT
        chars.append(0x2CD6)  #uni2CD6	COPTIC CAPITAL LETTER OLD COPTIC GANGIA
        chars.append(0x2CD7)  #uni2CD7	COPTIC SMALL LETTER OLD COPTIC GANGIA
        chars.append(0x02D8)  #breve	BREVE
        chars.append(0x02D9)  #dotaccent	DOT ABOVE
        chars.append(0x02DA)  #ring	RING ABOVE
        chars.append(0x02DB)  #ogonek	OGONEK
        chars.append(0x2CDC)  #uni2CDC	COPTIC CAPITAL LETTER OLD NUBIAN SHIMA
        chars.append(0x02DD)  #hungarumlaut	DOUBLE ACUTE ACCENT
        chars.append(0x2CDE)  #uni2CDE	COPTIC CAPITAL LETTER OLD NUBIAN NGI
        chars.append(0x2CDF)  #uni2CDF	COPTIC SMALL LETTER OLD NUBIAN NGI
        chars.append(0x2CE0)  #uni2CE0	COPTIC CAPITAL LETTER OLD NUBIAN NYI
        chars.append(0x2CD0)  #uni2CD0	COPTIC CAPITAL LETTER L-SHAPED HA
        chars.append(0x2CE2)  #uni2CE2	COPTIC CAPITAL LETTER OLD NUBIAN WAU
        chars.append(0x2CE3)  #uni2CE3	COPTIC SMALL LETTER OLD NUBIAN WAU
        chars.append(0x2CE4)  #uni2CE4	COPTIC SYMBOL KAI
        chars.append(0x2CE5)  #uni2CE5	COPTIC SYMBOL MI RO
        chars.append(0x2CE6)  #uni2CE6	COPTIC SYMBOL PI RO
        chars.append(0x2CE7)  #uni2CE7	COPTIC SYMBOL STAUROS
        chars.append(0x2CE8)  #uni2CE8	COPTIC SYMBOL TAU RO
        chars.append(0x2CE9)  #uni2CE9	COPTIC SYMBOL KHI RO
        chars.append(0x2CEA)  #uni2CEA	COPTIC SYMBOL SHIMA SIMA
        chars.append(0x2CEB)  #uni2CEB	COPTIC CAPITAL LETTER CRYPTOGRAMMIC SHEI
        chars.append(0x2CEC)  #uni2CEC	COPTIC SMALL LETTER CRYPTOGRAMMIC SHEI
        chars.append(0x2CED)  #uni2CED	COPTIC CAPITAL LETTER CRYPTOGRAMMIC GANGIA
        chars.append(0x2CEE)  #uni2CEE	COPTIC SMALL LETTER CRYPTOGRAMMIC GANGIA
        chars.append(0x2CEF)  #uni2CEF	COPTIC COMBINING NI ABOVE
        chars.append(0x2CF0)  #uni2CF0	COPTIC COMBINING SPIRITUS ASPER
        chars.append(0x2CF1)  #uni2CF1	COPTIC COMBINING SPIRITUS LENIS
        chars.append(0x2CF2)  #uni2CF2	????
        chars.append(0x2CF3)  #uni2CF3	????
        chars.append(0x2CF9)  #uni2CF9	COPTIC OLD NUBIAN FULL STOP
        chars.append(0x2CFA)  #uni2CFA	COPTIC OLD NUBIAN DIRECT QUESTION MARK
        chars.append(0x2CFB)  #uni2CFB	COPTIC OLD NUBIAN INDIRECT QUESTION MARK
        chars.append(0x2CFC)  #uni2CFC	COPTIC OLD NUBIAN VERSE DIVIDER
        chars.append(0x2CA7)  #uni2CA7	COPTIC SMALL LETTER TAU
        chars.append(0x2CFE)  #uni2CFE	COPTIC FULL STOP
        chars.append(0x2CFF)  #uni2CFF	COPTIC MORPHOLOGICAL DIVIDER
        chars.append(0x0300)  #gravecomb	COMBINING GRAVE ACCENT
        chars.append(0x0301)  #acutecomb	COMBINING ACUTE ACCENT
        chars.append(0x0302)  #uni0302	COMBINING CIRCUMFLEX ACCENT
        chars.append(0x0304)  #uni0304	COMBINING MACRON
        chars.append(0x0305)  #uni0305	COMBINING OVERLINE
        chars.append(0x0307)  #uni0307	COMBINING DOT ABOVE
        chars.append(0x0308)  #uni0308	COMBINING DIAERESIS
        chars.append(0x2CD8)  #uni2CD8	COPTIC CAPITAL LETTER OLD COPTIC DJA
        chars.append(0x2C83)  #uni2C83	COPTIC SMALL LETTER VIDA
        chars.append(0x2CDB)  #uni2CDB	COPTIC SMALL LETTER OLD COPTIC SHIMA
        chars.append(0x2CD9)  #uni2CD9	COPTIC SMALL LETTER OLD COPTIC DJA
        chars.append(0x2CDA)  #uni2CDA	COPTIC CAPITAL LETTER OLD COPTIC SHIMA
        chars.append(0x0323)  #dotbelowcomb	COMBINING DOT BELOW
        chars.append(0x2CDD)  #uni2CDD	COPTIC SMALL LETTER OLD NUBIAN SHIMA
        chars.append(0x2CCB)  #uni2CCB	COPTIC SMALL LETTER DIALECT-P HORI
        chars.append(0x033F)  #uni033F	COMBINING DOUBLE OVERLINE
        chars.append(0x2CE1)  #uni2CE1	COPTIC SMALL LETTER OLD NUBIAN NYI
        chars.append(0x014B)  #eng	LATIN SMALL LETTER ENG
        chars.append(0x0361)  #uni1DCD	COMBINING DOUBLE INVERTED BREVE
        chars.append(0x2CFD)  #uni2CFD	COPTIC FRACTION ONE HALF
        chars.append(0x2C92)  #uni2C92	COPTIC CAPITAL LETTER IAUDA
        chars.append(0x01C1)  #uni01C1	LATIN LETTER LATERAL CLICK
        chars.append(0x2CC7)  #uni2CC7	COPTIC SMALL LETTER OLD COPTIC ESH
        chars.append(0x1DCD)  #uni1DCD	COMBINING DOUBLE CIRCUMFLEX ABOVE
        chars.append(0x2CA4)  #uni2CA4	COPTIC CAPITAL LETTER SIMA
        chars.append(0x03E2)  #uni03E2	COPTIC CAPITAL LETTER SHEI
        chars.append(0x03E3)  #uni03E3	COPTIC SMALL LETTER SHEI
        chars.append(0x03E4)  #uni03E4	COPTIC CAPITAL LETTER FEI
        chars.append(0x03E5)  #uni03E5	COPTIC SMALL LETTER FEI
        chars.append(0x03E6)  #uni03E6	COPTIC CAPITAL LETTER KHEI
        chars.append(0x03E7)  #uni03E7	COPTIC SMALL LETTER KHEI
        chars.append(0x03E8)  #uni03E8	COPTIC CAPITAL LETTER HORI
        chars.append(0x03E9)  #uni03E9	COPTIC SMALL LETTER HORI
        chars.append(0x03EA)  #uni03EA	COPTIC CAPITAL LETTER GANGIA
        chars.append(0x03EB)  #uni03EB	COPTIC SMALL LETTER GANGIA
        chars.append(0x03EC)  #uni03EC	COPTIC CAPITAL LETTER SHIMA
        chars.append(0x03ED)  #uni03ED	COPTIC SMALL LETTER SHIMA
        chars.append(0x03EE)  #uni03EE	COPTIC CAPITAL LETTER DEI
        chars.append(0x03EF)  #uni03EF	COPTIC SMALL LETTER DEI
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


