# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansOldItalic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10301)  #glyph00005	OLD ITALIC LETTER BE
        chars.append(0x10302)  #glyph00006	OLD ITALIC LETTER KE
        chars.append(0x10303)  #glyph00007	OLD ITALIC LETTER DE
        chars.append(0x10304)  #glyph00008	OLD ITALIC LETTER E
        chars.append(0x10305)  #glyph00009	OLD ITALIC LETTER VE
        chars.append(0x10306)  #glyph00010	OLD ITALIC LETTER ZE
        chars.append(0x10307)  #glyph00011	OLD ITALIC LETTER HE
        chars.append(0x10308)  #glyph00012	OLD ITALIC LETTER THE
        chars.append(0x10309)  #glyph00013	OLD ITALIC LETTER I
        chars.append(0x1030A)  #glyph00014	OLD ITALIC LETTER KA
        chars.append(0x1030B)  #glyph00015	OLD ITALIC LETTER EL
        chars.append(0x1030C)  #glyph00016	OLD ITALIC LETTER EM
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1030E)  #glyph00018	OLD ITALIC LETTER ESH
        chars.append(0x1030F)  #glyph00019	OLD ITALIC LETTER O
        chars.append(0x10310)  #glyph00020	OLD ITALIC LETTER PE
        chars.append(0x10311)  #glyph00021	OLD ITALIC LETTER SHE
        chars.append(0x10312)  #glyph00022	OLD ITALIC LETTER KU
        chars.append(0x10313)  #glyph00023	OLD ITALIC LETTER ER
        chars.append(0x10314)  #glyph00024	OLD ITALIC LETTER ES
        chars.append(0x10315)  #glyph00025	OLD ITALIC LETTER TE
        chars.append(0x10316)  #glyph00026	OLD ITALIC LETTER U
        chars.append(0x10317)  #glyph00027	OLD ITALIC LETTER EKS
        chars.append(0x10318)  #glyph00028	OLD ITALIC LETTER PHE
        chars.append(0x10319)  #glyph00029	OLD ITALIC LETTER KHE
        chars.append(0x1031A)  #glyph00030	OLD ITALIC LETTER EF
        chars.append(0x1031B)  #glyph00031	OLD ITALIC LETTER ERS
        chars.append(0x1031C)  #glyph00032	OLD ITALIC LETTER CHE
        chars.append(0x1031D)  #glyph00033	OLD ITALIC LETTER II
        chars.append(0x10300)  #glyph00004	OLD ITALIC LETTER A
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10321)  #glyph00036	OLD ITALIC NUMERAL FIVE
        chars.append(0x10322)  #glyph00037	OLD ITALIC NUMERAL TEN
        chars.append(0x10323)  #glyph00038	OLD ITALIC NUMERAL FIFTY
        chars.append(0x1031E)  #glyph00034	OLD ITALIC LETTER UU
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1030D)  #glyph00017	OLD ITALIC LETTER EN
        chars.append(0x10320)  #glyph00035	OLD ITALIC NUMERAL ONE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


