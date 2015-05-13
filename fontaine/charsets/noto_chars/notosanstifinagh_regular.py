# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTifinagh-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0301)  #acutecomb	COMBINING ACUTE ACCENT
        chars.append(0x0302)  #uni0302	COMBINING CIRCUMFLEX ACCENT
        chars.append(0x0304)  #uni0304	COMBINING MACRON
        chars.append(0x0306)  #uni0306	COMBINING BREVE
        chars.append(0x0307)  #uni0307	COMBINING DOT ABOVE
        chars.append(0x000D)  #uni000D	????
        chars.append(0x2D41)  #uni2D41	TIFINAGH LETTER BERBER ACADEMY YAH
        chars.append(0x2D5B)  #uni2D5B	TIFINAGH LETTER YASH
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0323)  #dotbelowcomb	COMBINING DOT BELOW
        chars.append(0x2D31)  #uni2D31	TIFINAGH LETTER YAB
        chars.append(0x2D30)  #uni2D30	TIFINAGH LETTER YA
        chars.append(0x0331)  #uni0331	COMBINING MACRON BELOW
        chars.append(0x2D32)  #uni2D32	TIFINAGH LETTER YABH
        chars.append(0x2D33)  #uni2D33	TIFINAGH LETTER YAG
        chars.append(0x2D34)  #uni2D34	TIFINAGH LETTER YAGHH
        chars.append(0x2D35)  #uni2D35	TIFINAGH LETTER BERBER ACADEMY YAJ
        chars.append(0x2D36)  #uni2D36	TIFINAGH LETTER YAJ
        chars.append(0x2D37)  #uni2D37	TIFINAGH LETTER YAD
        chars.append(0x2D38)  #uni2D38	TIFINAGH LETTER YADH
        chars.append(0x2D39)  #uni2D39	TIFINAGH LETTER YADD
        chars.append(0x2D3A)  #uni2D3A	TIFINAGH LETTER YADDH
        chars.append(0x2D3B)  #uni2D3B	TIFINAGH LETTER YEY
        chars.append(0x2D3C)  #uni2D3C	TIFINAGH LETTER YAF
        chars.append(0x2D3D)  #uni2D3D	TIFINAGH LETTER YAK
        chars.append(0x2D3E)  #uni2D3E	TIFINAGH LETTER TUAREG YAK
        chars.append(0x2D3F)  #uni2D3F	TIFINAGH LETTER YAKHH
        chars.append(0x2D40)  #uni2D40	TIFINAGH LETTER YAH
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x2D42)  #uni2D42	TIFINAGH LETTER TUAREG YAH
        chars.append(0x2D43)  #uni2D43	TIFINAGH LETTER YAHH
        chars.append(0x2D44)  #uni2D44	TIFINAGH LETTER YAA
        chars.append(0x2D45)  #uni2D45	TIFINAGH LETTER YAKH
        chars.append(0x2D46)  #uni2D46	TIFINAGH LETTER TUAREG YAKH
        chars.append(0x2D47)  #uni2D47	TIFINAGH LETTER YAQ
        chars.append(0x2D48)  #uni2D48	TIFINAGH LETTER TUAREG YAQ
        chars.append(0x2D49)  #uni2D49	TIFINAGH LETTER YI
        chars.append(0x2D4A)  #uni2D4A	TIFINAGH LETTER YAZH
        chars.append(0x2D4B)  #uni2D4B	TIFINAGH LETTER AHAGGAR YAZH
        chars.append(0x2D4C)  #uni2D4C	TIFINAGH LETTER TUAREG YAZH
        chars.append(0x2D4D)  #uni2D4D	TIFINAGH LETTER YAL
        chars.append(0x2D4E)  #uni2D4E	TIFINAGH LETTER YAM
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x2D50)  #uni2D50	TIFINAGH LETTER TUAREG YAGN
        chars.append(0x2D51)  #uni2D51	TIFINAGH LETTER TUAREG YANG
        chars.append(0x2D52)  #uni2D52	TIFINAGH LETTER YAP
        chars.append(0x2D53)  #uni2D53	TIFINAGH LETTER YU
        chars.append(0x2D54)  #uni2D54	TIFINAGH LETTER YAR
        chars.append(0x2D55)  #uni2D55	TIFINAGH LETTER YARR
        chars.append(0x2D56)  #uni2D56	TIFINAGH LETTER YAGH
        chars.append(0x2D57)  #uni2D57	TIFINAGH LETTER TUAREG YAGH
        chars.append(0x2D58)  #uni2D58	TIFINAGH LETTER AYER YAGH
        chars.append(0x2D59)  #uni2D59	TIFINAGH LETTER YAS
        chars.append(0x2D5A)  #uni2D5A	TIFINAGH LETTER YASS
        chars.append(0x2D4F)  #uni2D4F	TIFINAGH LETTER YAN
        chars.append(0x2D5C)  #uni2D5C	TIFINAGH LETTER YAT
        chars.append(0x2D5D)  #uni2D5D	TIFINAGH LETTER YATH
        chars.append(0x2D5E)  #uni2D5E	TIFINAGH LETTER YACH
        chars.append(0x2D5F)  #uni2D5F	TIFINAGH LETTER YATT
        chars.append(0x2D60)  #uni2D60	TIFINAGH LETTER YAV
        chars.append(0x2D61)  #uni2D61	TIFINAGH LETTER YAW
        chars.append(0x2D62)  #uni2D62	TIFINAGH LETTER YAY
        chars.append(0x2D63)  #uni2D63	TIFINAGH LETTER YAZ
        chars.append(0x2D64)  #uni2D64	TIFINAGH LETTER TAWELLEMET YAZ
        chars.append(0x2D65)  #uni2D65	TIFINAGH LETTER YAZZ
        chars.append(0x2D66)  #uni2D66	????
        chars.append(0x2D67)  #uni2D67	????
        chars.append(0x2D6F)  #uni2D6F	TIFINAGH MODIFIER LETTER LABIALIZATION MARK
        chars.append(0x2D70)  #uni2D70	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x2D7F)  #uni2D7F	????
        return chars


