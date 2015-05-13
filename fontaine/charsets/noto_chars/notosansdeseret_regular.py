# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansDeseret-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10400)  #glyph00004	DESERET CAPITAL LETTER LONG I
        chars.append(0x10402)  #glyph00006	DESERET CAPITAL LETTER LONG A
        chars.append(0x10403)  #glyph00007	DESERET CAPITAL LETTER LONG AH
        chars.append(0x10404)  #glyph00008	DESERET CAPITAL LETTER LONG O
        chars.append(0x10405)  #glyph00009	DESERET CAPITAL LETTER LONG OO
        chars.append(0x10406)  #glyph00010	DESERET CAPITAL LETTER SHORT I
        chars.append(0x10401)  #glyph00005	DESERET CAPITAL LETTER LONG E
        chars.append(0x10408)  #glyph00012	DESERET CAPITAL LETTER SHORT A
        chars.append(0x10409)  #glyph00013	DESERET CAPITAL LETTER SHORT AH
        chars.append(0x1040A)  #glyph00014	DESERET CAPITAL LETTER SHORT O
        chars.append(0x1040B)  #glyph00015	DESERET CAPITAL LETTER SHORT OO
        chars.append(0x1040C)  #glyph00016	DESERET CAPITAL LETTER AY
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1040E)  #glyph00018	DESERET CAPITAL LETTER WU
        chars.append(0x1040F)  #glyph00019	DESERET CAPITAL LETTER YEE
        chars.append(0x10410)  #glyph00020	DESERET CAPITAL LETTER H
        chars.append(0x10411)  #glyph00021	DESERET CAPITAL LETTER PEE
        chars.append(0x10412)  #glyph00022	DESERET CAPITAL LETTER BEE
        chars.append(0x10413)  #glyph00023	DESERET CAPITAL LETTER TEE
        chars.append(0x10414)  #glyph00024	DESERET CAPITAL LETTER DEE
        chars.append(0x10415)  #glyph00025	DESERET CAPITAL LETTER CHEE
        chars.append(0x10416)  #glyph00026	DESERET CAPITAL LETTER JEE
        chars.append(0x10417)  #glyph00027	DESERET CAPITAL LETTER KAY
        chars.append(0x10418)  #glyph00028	DESERET CAPITAL LETTER GAY
        chars.append(0x10419)  #glyph00029	DESERET CAPITAL LETTER EF
        chars.append(0x1041A)  #glyph00030	DESERET CAPITAL LETTER VEE
        chars.append(0x1041B)  #glyph00031	DESERET CAPITAL LETTER ETH
        chars.append(0x1041C)  #glyph00032	DESERET CAPITAL LETTER THEE
        chars.append(0x1041D)  #glyph00033	DESERET CAPITAL LETTER ES
        chars.append(0x1041E)  #glyph00034	DESERET CAPITAL LETTER ZEE
        chars.append(0x1041F)  #glyph00035	DESERET CAPITAL LETTER ESH
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10421)  #glyph00037	DESERET CAPITAL LETTER ER
        chars.append(0x10422)  #glyph00038	DESERET CAPITAL LETTER EL
        chars.append(0x10423)  #glyph00039	DESERET CAPITAL LETTER EM
        chars.append(0x10424)  #glyph00040	DESERET CAPITAL LETTER EN
        chars.append(0x10425)  #glyph00041	DESERET CAPITAL LETTER ENG
        chars.append(0x10426)  #glyph00042	DESERET CAPITAL LETTER OI
        chars.append(0x10427)  #glyph00043	DESERET CAPITAL LETTER EW
        chars.append(0x10428)  #glyph00044	DESERET SMALL LETTER LONG I
        chars.append(0x10429)  #glyph00045	DESERET SMALL LETTER LONG E
        chars.append(0x1042A)  #glyph00046	DESERET SMALL LETTER LONG A
        chars.append(0x10407)  #glyph00011	DESERET CAPITAL LETTER SHORT E
        chars.append(0x1042C)  #glyph00048	DESERET SMALL LETTER LONG O
        chars.append(0x1042D)  #glyph00049	DESERET SMALL LETTER LONG OO
        chars.append(0x1042E)  #glyph00050	DESERET SMALL LETTER SHORT I
        chars.append(0x1042F)  #glyph00051	DESERET SMALL LETTER SHORT E
        chars.append(0x10430)  #glyph00052	DESERET SMALL LETTER SHORT A
        chars.append(0x1042B)  #glyph00047	DESERET SMALL LETTER LONG AH
        chars.append(0x10432)  #glyph00054	DESERET SMALL LETTER SHORT O
        chars.append(0x10433)  #glyph00055	DESERET SMALL LETTER SHORT OO
        chars.append(0x10434)  #glyph00056	DESERET SMALL LETTER AY
        chars.append(0x10435)  #glyph00057	DESERET SMALL LETTER OW
        chars.append(0x10436)  #glyph00058	DESERET SMALL LETTER WU
        chars.append(0x10437)  #glyph00059	DESERET SMALL LETTER YEE
        chars.append(0x10438)  #glyph00060	DESERET SMALL LETTER H
        chars.append(0x10439)  #glyph00061	DESERET SMALL LETTER PEE
        chars.append(0x1043A)  #glyph00062	DESERET SMALL LETTER BEE
        chars.append(0x1043B)  #glyph00063	DESERET SMALL LETTER TEE
        chars.append(0x1043C)  #glyph00064	DESERET SMALL LETTER DEE
        chars.append(0x1043D)  #glyph00065	DESERET SMALL LETTER CHEE
        chars.append(0x1043E)  #glyph00066	DESERET SMALL LETTER JEE
        chars.append(0x1043F)  #glyph00067	DESERET SMALL LETTER KAY
        chars.append(0x10440)  #glyph00068	DESERET SMALL LETTER GAY
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10442)  #glyph00070	DESERET SMALL LETTER VEE
        chars.append(0x10443)  #glyph00071	DESERET SMALL LETTER ETH
        chars.append(0x10444)  #glyph00072	DESERET SMALL LETTER THEE
        chars.append(0x10445)  #glyph00073	DESERET SMALL LETTER ES
        chars.append(0x10441)  #glyph00069	DESERET SMALL LETTER EF
        chars.append(0x10447)  #glyph00075	DESERET SMALL LETTER ESH
        chars.append(0x10448)  #glyph00076	DESERET SMALL LETTER ZHEE
        chars.append(0x10449)  #glyph00077	DESERET SMALL LETTER ER
        chars.append(0x1044A)  #glyph00078	DESERET SMALL LETTER EL
        chars.append(0x1044B)  #glyph00079	DESERET SMALL LETTER EM
        chars.append(0x1044C)  #glyph00080	DESERET SMALL LETTER EN
        chars.append(0x1044D)  #glyph00081	DESERET SMALL LETTER ENG
        chars.append(0x1044E)  #glyph00082	DESERET SMALL LETTER OI
        chars.append(0x1040D)  #glyph00017	DESERET CAPITAL LETTER OW
        chars.append(0x1044F)  #glyph00083	DESERET SMALL LETTER EW
        chars.append(0x10446)  #glyph00074	DESERET SMALL LETTER ZEE
        chars.append(0x10431)  #glyph00053	DESERET SMALL LETTER SHORT AH
        chars.append(0x10420)  #glyph00036	DESERET CAPITAL LETTER ZHEE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


