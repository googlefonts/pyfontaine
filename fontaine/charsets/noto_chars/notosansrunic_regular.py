# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansRunic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x16A1)  #uni16A1	RUNIC LETTER V
        chars.append(0x16A2)  #uni16A2	RUNIC LETTER URUZ UR U
        chars.append(0x16A3)  #uni16A3	RUNIC LETTER YR
        chars.append(0x16A4)  #uni16A4	RUNIC LETTER Y
        chars.append(0x16A5)  #uni16A5	RUNIC LETTER W
        chars.append(0x16A6)  #uni16A6	RUNIC LETTER THURISAZ THURS THORN
        chars.append(0x16A7)  #uni16A7	RUNIC LETTER ETH
        chars.append(0x16A8)  #uni16A8	RUNIC LETTER ANSUZ A
        chars.append(0x16A9)  #uni16A9	RUNIC LETTER OS O
        chars.append(0x16AA)  #uni16AA	RUNIC LETTER AC A
        chars.append(0x16AB)  #uni16AB	RUNIC LETTER AESC
        chars.append(0x16AC)  #uni16AC	RUNIC LETTER LONG-BRANCH-OSS O
        chars.append(0x16AD)  #uni16AD	RUNIC LETTER SHORT-TWIG-OSS O
        chars.append(0x16AE)  #uni16AE	RUNIC LETTER O
        chars.append(0x16AF)  #uni16AF	RUNIC LETTER OE
        chars.append(0x16B0)  #uni16B0	RUNIC LETTER ON
        chars.append(0x16B1)  #uni16B1	RUNIC LETTER RAIDO RAD REID R
        chars.append(0x16B2)  #uni16B2	RUNIC LETTER KAUNA
        chars.append(0x16B3)  #uni16B3	RUNIC LETTER CEN
        chars.append(0x16B4)  #uni16B4	RUNIC LETTER KAUN K
        chars.append(0x16B5)  #uni16B5	RUNIC LETTER G
        chars.append(0x16B6)  #uni16B6	RUNIC LETTER ENG
        chars.append(0x16B7)  #uni16B7	RUNIC LETTER GEBO GYFU G
        chars.append(0x16B8)  #uni16B8	RUNIC LETTER GAR
        chars.append(0x16B9)  #uni16B9	RUNIC LETTER WUNJO WYNN W
        chars.append(0x16BA)  #uni16BA	RUNIC LETTER HAGLAZ H
        chars.append(0x16BB)  #uni16BB	RUNIC LETTER HAEGL H
        chars.append(0x16BC)  #uni16BC	RUNIC LETTER LONG-BRANCH-HAGALL H
        chars.append(0x16BD)  #uni16BD	RUNIC LETTER SHORT-TWIG-HAGALL H
        chars.append(0x16BE)  #uni16BE	RUNIC LETTER NAUDIZ NYD NAUD N
        chars.append(0x16BF)  #uni16BF	RUNIC LETTER SHORT-TWIG-NAUD N
        chars.append(0x16C0)  #uni16C0	RUNIC LETTER DOTTED-N
        chars.append(0x16C1)  #uni16C1	RUNIC LETTER ISAZ IS ISS I
        chars.append(0x16C2)  #uni16C2	RUNIC LETTER E
        chars.append(0x16C3)  #uni16C3	RUNIC LETTER JERAN J
        chars.append(0x16C4)  #uni16C4	RUNIC LETTER GER
        chars.append(0x16C5)  #uni16C5	RUNIC LETTER LONG-BRANCH-AR AE
        chars.append(0x16C6)  #uni16C6	RUNIC LETTER SHORT-TWIG-AR A
        chars.append(0x16C7)  #uni16C7	RUNIC LETTER IWAZ EOH
        chars.append(0x16C8)  #uni16C8	RUNIC LETTER PERTHO PEORTH P
        chars.append(0x16C9)  #uni16C9	RUNIC LETTER ALGIZ EOLHX
        chars.append(0x16CA)  #uni16CA	RUNIC LETTER SOWILO S
        chars.append(0x16CB)  #uni16CB	RUNIC LETTER SIGEL LONG-BRANCH-SOL S
        chars.append(0x16CC)  #uni16CC	RUNIC LETTER SHORT-TWIG-SOL S
        chars.append(0x16CD)  #uni16CD	RUNIC LETTER C
        chars.append(0x16CE)  #uni16CE	RUNIC LETTER Z
        chars.append(0x16CF)  #uni16CF	RUNIC LETTER TIWAZ TIR TYR T
        chars.append(0x16D0)  #uni16D0	RUNIC LETTER SHORT-TWIG-TYR T
        chars.append(0x16D1)  #uni16D1	RUNIC LETTER D
        chars.append(0x16D2)  #uni16D2	RUNIC LETTER BERKANAN BEORC BJARKAN B
        chars.append(0x16D3)  #uni16D3	RUNIC LETTER SHORT-TWIG-BJARKAN B
        chars.append(0x16D4)  #uni16D4	RUNIC LETTER DOTTED-P
        chars.append(0x16D5)  #uni16D5	RUNIC LETTER OPEN-P
        chars.append(0x16D6)  #uni16D6	RUNIC LETTER EHWAZ EH E
        chars.append(0x16D7)  #uni16D7	RUNIC LETTER MANNAZ MAN M
        chars.append(0x16D8)  #uni16D8	RUNIC LETTER LONG-BRANCH-MADR M
        chars.append(0x16D9)  #uni16D9	RUNIC LETTER SHORT-TWIG-MADR M
        chars.append(0x16DA)  #uni16DA	RUNIC LETTER LAUKAZ LAGU LOGR L
        chars.append(0x16DB)  #uni16DB	RUNIC LETTER DOTTED-L
        chars.append(0x16DC)  #uni16DC	RUNIC LETTER INGWAZ
        chars.append(0x16DD)  #uni16DD	RUNIC LETTER ING
        chars.append(0x16DE)  #uni16DE	RUNIC LETTER DAGAZ DAEG D
        chars.append(0x16DF)  #uni16DF	RUNIC LETTER OTHALAN ETHEL O
        chars.append(0x16E0)  #uni16E0	RUNIC LETTER EAR
        chars.append(0x16E1)  #uni16E1	RUNIC LETTER IOR
        chars.append(0x16E2)  #uni16E2	RUNIC LETTER CWEORTH
        chars.append(0x16E3)  #uni16E3	RUNIC LETTER CALC
        chars.append(0x16E4)  #uni16E4	RUNIC LETTER CEALC
        chars.append(0x16E5)  #uni16E5	RUNIC LETTER STAN
        chars.append(0x16E6)  #uni16E6	RUNIC LETTER LONG-BRANCH-YR
        chars.append(0x16E7)  #uni16E7	RUNIC LETTER SHORT-TWIG-YR
        chars.append(0x16E8)  #uni16E8	RUNIC LETTER ICELANDIC-YR
        chars.append(0x16E9)  #uni16E9	RUNIC LETTER Q
        chars.append(0x16EA)  #uni16EA	RUNIC LETTER X
        chars.append(0x16EB)  #uni16EB	RUNIC SINGLE PUNCTUATION
        chars.append(0x16EC)  #uni16EC	RUNIC MULTIPLE PUNCTUATION
        chars.append(0x16ED)  #uni16ED	RUNIC CROSS PUNCTUATION
        chars.append(0x16EE)  #uni16EE	RUNIC ARLAUG SYMBOL
        chars.append(0x16EF)  #uni16EF	RUNIC TVIMADUR SYMBOL
        chars.append(0x16F0)  #uni16F0	RUNIC BELGTHOR SYMBOL
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x16A0)  #uni16A0	RUNIC LETTER FEHU FEOH FE F
        return chars


