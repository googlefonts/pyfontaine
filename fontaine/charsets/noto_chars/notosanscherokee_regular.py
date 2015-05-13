# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansCherokee-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x13A0)  #uni13A0	CHEROKEE LETTER A
        chars.append(0x13A1)  #uni13A1	CHEROKEE LETTER E
        chars.append(0x13A2)  #uni13A2	CHEROKEE LETTER I
        chars.append(0x13A3)  #uni13A3	CHEROKEE LETTER O
        chars.append(0x13A4)  #uni13A4	CHEROKEE LETTER U
        chars.append(0x13A5)  #uni13A5	CHEROKEE LETTER V
        chars.append(0x13A6)  #uni13A6	CHEROKEE LETTER GA
        chars.append(0x13A7)  #uni13A7	CHEROKEE LETTER KA
        chars.append(0x13A8)  #uni13A8	CHEROKEE LETTER GE
        chars.append(0x13A9)  #uni13A9	CHEROKEE LETTER GI
        chars.append(0x13AA)  #uni13AA	CHEROKEE LETTER GO
        chars.append(0x13AB)  #uni13AB	CHEROKEE LETTER GU
        chars.append(0x13AC)  #uni13AC	CHEROKEE LETTER GV
        chars.append(0x13AD)  #uni13AD	CHEROKEE LETTER HA
        chars.append(0x13AE)  #uni13AE	CHEROKEE LETTER HE
        chars.append(0x13AF)  #uni13AF	CHEROKEE LETTER HI
        chars.append(0x13B0)  #uni13B0	CHEROKEE LETTER HO
        chars.append(0x13B1)  #uni13B1	CHEROKEE LETTER HU
        chars.append(0x13B2)  #uni13B2	CHEROKEE LETTER HV
        chars.append(0x13B3)  #uni13B3	CHEROKEE LETTER LA
        chars.append(0x13B4)  #uni13B4	CHEROKEE LETTER LE
        chars.append(0x13B5)  #uni13B5	CHEROKEE LETTER LI
        chars.append(0x13B6)  #uni13B6	CHEROKEE LETTER LO
        chars.append(0x13B7)  #uni13B7	CHEROKEE LETTER LU
        chars.append(0x13B8)  #uni13B8	CHEROKEE LETTER LV
        chars.append(0x13B9)  #uni13B9	CHEROKEE LETTER MA
        chars.append(0x13BA)  #uni13BA	CHEROKEE LETTER ME
        chars.append(0x13BB)  #uni13BB	CHEROKEE LETTER MI
        chars.append(0x13BC)  #uni13BC	CHEROKEE LETTER MO
        chars.append(0x13BD)  #uni13BD	CHEROKEE LETTER MU
        chars.append(0x13BE)  #uni13BE	CHEROKEE LETTER NA
        chars.append(0x13BF)  #uni13BF	CHEROKEE LETTER HNA
        chars.append(0x13C0)  #uni13C0	CHEROKEE LETTER NAH
        chars.append(0x13C1)  #uni13C1	CHEROKEE LETTER NE
        chars.append(0x13C2)  #uni13C2	CHEROKEE LETTER NI
        chars.append(0x13C3)  #uni13C3	CHEROKEE LETTER NO
        chars.append(0x13C4)  #uni13C4	CHEROKEE LETTER NU
        chars.append(0x13C5)  #uni13C5	CHEROKEE LETTER NV
        chars.append(0x13C6)  #uni13C6	CHEROKEE LETTER QUA
        chars.append(0x13C7)  #uni13C7	CHEROKEE LETTER QUE
        chars.append(0x13C8)  #uni13C8	CHEROKEE LETTER QUI
        chars.append(0x13C9)  #uni13C9	CHEROKEE LETTER QUO
        chars.append(0x13CA)  #uni13CA	CHEROKEE LETTER QUU
        chars.append(0x13CB)  #uni13CB	CHEROKEE LETTER QUV
        chars.append(0x13CC)  #uni13CC	CHEROKEE LETTER SA
        chars.append(0x13CD)  #uni13CD	CHEROKEE LETTER S
        chars.append(0x13CE)  #uni13CE	CHEROKEE LETTER SE
        chars.append(0x13CF)  #uni13CF	CHEROKEE LETTER SI
        chars.append(0x13D0)  #uni13D0	CHEROKEE LETTER SO
        chars.append(0x13D1)  #uni13D1	CHEROKEE LETTER SU
        chars.append(0x13D2)  #uni13D2	CHEROKEE LETTER SV
        chars.append(0x13D3)  #uni13D3	CHEROKEE LETTER DA
        chars.append(0x13D4)  #uni13D4	CHEROKEE LETTER TA
        chars.append(0x13D5)  #uni13D5	CHEROKEE LETTER DE
        chars.append(0x13D6)  #uni13D6	CHEROKEE LETTER TE
        chars.append(0x13D7)  #uni13D7	CHEROKEE LETTER DI
        chars.append(0x13D8)  #uni13D8	CHEROKEE LETTER TI
        chars.append(0x13D9)  #uni13D9	CHEROKEE LETTER DO
        chars.append(0x13DA)  #uni13DA	CHEROKEE LETTER DU
        chars.append(0x13DB)  #uni13DB	CHEROKEE LETTER DV
        chars.append(0x13DC)  #uni13DC	CHEROKEE LETTER DLA
        chars.append(0x13DD)  #uni13DD	CHEROKEE LETTER TLA
        chars.append(0x13DE)  #uni13DE	CHEROKEE LETTER TLE
        chars.append(0x13DF)  #uni13DF	CHEROKEE LETTER TLI
        chars.append(0x13E0)  #uni13E0	CHEROKEE LETTER TLO
        chars.append(0x13E1)  #uni13E1	CHEROKEE LETTER TLU
        chars.append(0x13E2)  #uni13E2	CHEROKEE LETTER TLV
        chars.append(0x13E3)  #uni13E3	CHEROKEE LETTER TSA
        chars.append(0x13E4)  #uni13E4	CHEROKEE LETTER TSE
        chars.append(0x13E5)  #uni13E5	CHEROKEE LETTER TSI
        chars.append(0x13E6)  #uni13E6	CHEROKEE LETTER TSO
        chars.append(0x13E7)  #uni13E7	CHEROKEE LETTER TSU
        chars.append(0x13E8)  #uni13E8	CHEROKEE LETTER TSV
        chars.append(0x13E9)  #uni13E9	CHEROKEE LETTER WA
        chars.append(0x13EA)  #uni13EA	CHEROKEE LETTER WE
        chars.append(0x13EB)  #uni13EB	CHEROKEE LETTER WI
        chars.append(0x13EC)  #uni13EC	CHEROKEE LETTER WO
        chars.append(0x13ED)  #uni13ED	CHEROKEE LETTER WU
        chars.append(0x13EE)  #uni13EE	CHEROKEE LETTER WV
        chars.append(0x13EF)  #uni13EF	CHEROKEE LETTER YA
        chars.append(0x13F0)  #uni13F0	CHEROKEE LETTER YE
        chars.append(0x13F1)  #uni13F1	CHEROKEE LETTER YI
        chars.append(0x13F2)  #uni13F2	CHEROKEE LETTER YO
        chars.append(0x13F3)  #uni13F3	CHEROKEE LETTER YU
        chars.append(0x13F4)  #uni13F4	CHEROKEE LETTER YV
        return chars


