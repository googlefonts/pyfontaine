# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansPhagsPa-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x1801)  #uni1801	MONGOLIAN ELLIPSIS
        chars.append(0x1802)  #uni1802	MONGOLIAN COMMA
        chars.append(0x1803)  #uni1803	MONGOLIAN FULL STOP
        chars.append(0x1805)  #uni1805	MONGOLIAN FOUR DOTS
        chars.append(0x3007)  #uni3007	IDEOGRAPHIC NUMBER ZERO
        chars.append(0x3008)  #uni3008	LEFT ANGLE BRACKET
        chars.append(0x3009)  #uni3009	RIGHT ANGLE BRACKET
        chars.append(0x300A)  #uni300A	LEFT DOUBLE ANGLE BRACKET
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x3010)  #uni3010	LEFT BLACK LENTICULAR BRACKET
        chars.append(0x3011)  #uni3011	RIGHT BLACK LENTICULAR BRACKET
        chars.append(0x3014)  #uni3014	LEFT TORTOISE SHELL BRACKET
        chars.append(0x3015)  #uni3015	RIGHT TORTOISE SHELL BRACKET
        chars.append(0x3016)  #uni3016	LEFT WHITE LENTICULAR BRACKET
        chars.append(0x3017)  #uni3017	RIGHT WHITE LENTICULAR BRACKET
        chars.append(0x3018)  #uni3018	LEFT WHITE TORTOISE SHELL BRACKET
        chars.append(0x3019)  #uni3019	RIGHT WHITE TORTOISE SHELL BRACKET
        chars.append(0x301A)  #uni301A	LEFT WHITE SQUARE BRACKET
        chars.append(0x301B)  #uni301B	RIGHT WHITE SQUARE BRACKET
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0021)  #exclam	EXCLAMATION MARK
        chars.append(0x2025)  #twodotenleader	TWO DOT LEADER
        chars.append(0x2026)  #ellipsis	HORIZONTAL ELLIPSIS
        chars.append(0x003F)  #question	QUESTION MARK
        chars.append(0xA840)  #uniA840	PHAGS-PA LETTER KA
        chars.append(0xA841)  #uniA841	PHAGS-PA LETTER KHA
        chars.append(0xA842)  #uniA842	PHAGS-PA LETTER GA
        chars.append(0xA843)  #uniA843	PHAGS-PA LETTER NGA
        chars.append(0xA844)  #uniA844	PHAGS-PA LETTER CA
        chars.append(0xA845)  #uniA845	PHAGS-PA LETTER CHA
        chars.append(0xA846)  #uniA846	PHAGS-PA LETTER JA
        chars.append(0xA847)  #uniA847	PHAGS-PA LETTER NYA
        chars.append(0xA848)  #uniA848	PHAGS-PA LETTER TA
        chars.append(0xA849)  #uniA849	PHAGS-PA LETTER THA
        chars.append(0xA84A)  #uniA84A	PHAGS-PA LETTER DA
        chars.append(0xA84B)  #uniA84B	PHAGS-PA LETTER NA
        chars.append(0xA84C)  #uniA84C	PHAGS-PA LETTER PA
        chars.append(0xA84D)  #uniA84D	PHAGS-PA LETTER PHA
        chars.append(0xA84E)  #uniA84E	PHAGS-PA LETTER BA
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0xA850)  #uniA850	PHAGS-PA LETTER TSA
        chars.append(0xA851)  #uniA851	PHAGS-PA LETTER TSHA
        chars.append(0xA852)  #uniA852	PHAGS-PA LETTER DZA
        chars.append(0xA853)  #uniA853	PHAGS-PA LETTER WA
        chars.append(0xA854)  #uniA854	PHAGS-PA LETTER ZHA
        chars.append(0x300E)  #uni300E	LEFT WHITE CORNER BRACKET
        chars.append(0xA856)  #uniA856	PHAGS-PA LETTER SMALL A
        chars.append(0xA857)  #uniA857	PHAGS-PA LETTER YA
        chars.append(0xA858)  #uniA858	PHAGS-PA LETTER RA
        chars.append(0xA859)  #uniA859	PHAGS-PA LETTER LA
        chars.append(0xA85A)  #uniA85A	PHAGS-PA LETTER SHA
        chars.append(0xA85B)  #uniA85B	PHAGS-PA LETTER SA
        chars.append(0xA85C)  #uniA85C	PHAGS-PA LETTER HA
        chars.append(0xA85D)  #uniA85D	PHAGS-PA LETTER A
        chars.append(0xA85E)  #uniA85E	PHAGS-PA LETTER I
        chars.append(0xA85F)  #uniA85F	PHAGS-PA LETTER U
        chars.append(0xA860)  #uniA860	PHAGS-PA LETTER E
        chars.append(0xA861)  #uniA861	PHAGS-PA LETTER O
        chars.append(0xA862)  #uniA862	PHAGS-PA LETTER QA
        chars.append(0xA863)  #uniA863	PHAGS-PA LETTER XA
        chars.append(0xA864)  #uniA864	PHAGS-PA LETTER FA
        chars.append(0xA865)  #uniA865	PHAGS-PA LETTER GGA
        chars.append(0xA866)  #uniA866	PHAGS-PA LETTER EE
        chars.append(0xA867)  #uniA867	PHAGS-PA SUBJOINED LETTER WA
        chars.append(0xA868)  #uniA868	PHAGS-PA SUBJOINED LETTER YA
        chars.append(0xA869)  #uniA869	PHAGS-PA LETTER TTA
        chars.append(0xA86A)  #uniA86A	PHAGS-PA LETTER TTHA
        chars.append(0xA86B)  #uniA86B	PHAGS-PA LETTER DDA
        chars.append(0xA86C)  #uniA86C	PHAGS-PA LETTER NNA
        chars.append(0xA86D)  #uniA86D	PHAGS-PA LETTER ALTERNATE YA
        chars.append(0xA86E)  #uniA86E	PHAGS-PA LETTER VOICELESS SHA
        chars.append(0xA86F)  #uniA86F	PHAGS-PA LETTER VOICED HA
        chars.append(0xA870)  #uniA870	PHAGS-PA LETTER ASPIRATED FA
        chars.append(0xA871)  #uniA871	PHAGS-PA SUBJOINED LETTER RA
        chars.append(0xA872)  #uniA872	PHAGS-PA SUPERFIXED LETTER RA
        chars.append(0xA873)  #uniA873	PHAGS-PA LETTER CANDRABINDU
        chars.append(0xA874)  #uniA874	PHAGS-PA SINGLE HEAD MARK
        chars.append(0xA875)  #uniA875	PHAGS-PA DOUBLE HEAD MARK
        chars.append(0xA876)  #uniA876	PHAGS-PA MARK SHAD
        chars.append(0xA877)  #uniA877	PHAGS-PA MARK DOUBLE SHAD
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x300B)  #uni300B	RIGHT DOUBLE ANGLE BRACKET
        chars.append(0x300C)  #uni300C	LEFT CORNER BRACKET
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x300D)  #uni300D	RIGHT CORNER BRACKET
        chars.append(0x300F)  #uni300F	RIGHT WHITE CORNER BRACKET
        chars.append(0x3001)  #uni3001	IDEOGRAPHIC COMMA
        chars.append(0x3002)  #uni3002	IDEOGRAPHIC FULL STOP
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0xA84F)  #uniA84F	PHAGS-PA LETTER MA
        chars.append(0xFE00)  #uniFE00	VARIATION SELECTOR-1
        chars.append(0xA855)  #uniA855	PHAGS-PA LETTER ZA
        return chars


