# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansOldSouthArabian-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10A7F)  #glyph00035	OLD SOUTH ARABIAN NUMERIC INDICATOR
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10A60)  #glyph00004	OLD SOUTH ARABIAN LETTER HE
        chars.append(0x10A61)  #glyph00005	OLD SOUTH ARABIAN LETTER LAMEDH
        chars.append(0x10A62)  #glyph00006	OLD SOUTH ARABIAN LETTER HETH
        chars.append(0x10A63)  #glyph00007	OLD SOUTH ARABIAN LETTER MEM
        chars.append(0x10A64)  #glyph00008	OLD SOUTH ARABIAN LETTER QOPH
        chars.append(0x10A65)  #glyph00009	OLD SOUTH ARABIAN LETTER WAW
        chars.append(0x10A66)  #glyph00010	OLD SOUTH ARABIAN LETTER SHIN
        chars.append(0x10A67)  #glyph00011	OLD SOUTH ARABIAN LETTER RESH
        chars.append(0x10A68)  #glyph00012	OLD SOUTH ARABIAN LETTER BETH
        chars.append(0x10A69)  #glyph00013	OLD SOUTH ARABIAN LETTER TAW
        chars.append(0x10A6A)  #glyph00014	OLD SOUTH ARABIAN LETTER SAT
        chars.append(0x10A6B)  #glyph00015	OLD SOUTH ARABIAN LETTER KAPH
        chars.append(0x10A6C)  #glyph00016	OLD SOUTH ARABIAN LETTER NUN
        chars.append(0x10A6D)  #glyph00017	OLD SOUTH ARABIAN LETTER KHETH
        chars.append(0x10A6E)  #glyph00018	OLD SOUTH ARABIAN LETTER SADHE
        chars.append(0x10A6F)  #glyph00019	OLD SOUTH ARABIAN LETTER SAMEKH
        chars.append(0x10A70)  #glyph00020	OLD SOUTH ARABIAN LETTER FE
        chars.append(0x10A71)  #glyph00021	OLD SOUTH ARABIAN LETTER ALEF
        chars.append(0x10A72)  #glyph00022	OLD SOUTH ARABIAN LETTER AYN
        chars.append(0x10A73)  #glyph00023	OLD SOUTH ARABIAN LETTER DHADHE
        chars.append(0x10A74)  #glyph00024	OLD SOUTH ARABIAN LETTER GIMEL
        chars.append(0x10A75)  #glyph00025	OLD SOUTH ARABIAN LETTER DALETH
        chars.append(0x10A76)  #glyph00026	OLD SOUTH ARABIAN LETTER GHAYN
        chars.append(0x10A77)  #glyph00027	OLD SOUTH ARABIAN LETTER TETH
        chars.append(0x10A78)  #glyph00028	OLD SOUTH ARABIAN LETTER ZAYN
        chars.append(0x10A79)  #glyph00029	OLD SOUTH ARABIAN LETTER DHALETH
        chars.append(0x10A7A)  #glyph00030	OLD SOUTH ARABIAN LETTER YODH
        chars.append(0x10A7B)  #glyph00031	OLD SOUTH ARABIAN LETTER THAW
        chars.append(0x10A7C)  #glyph00032	OLD SOUTH ARABIAN LETTER THETH
        chars.append(0x10A7D)  #glyph00033	OLD SOUTH ARABIAN NUMBER ONE
        chars.append(0x10A7E)  #glyph00034	OLD SOUTH ARABIAN NUMBER FIFTY
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


