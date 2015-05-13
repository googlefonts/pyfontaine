# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTagalog-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x1701)  #uni1701	TAGALOG LETTER I
        chars.append(0x1702)  #uni1702	TAGALOG LETTER U
        chars.append(0x1703)  #uni1703	TAGALOG LETTER KA
        chars.append(0x1704)  #uni1704	TAGALOG LETTER GA
        chars.append(0x1705)  #uni1705	TAGALOG LETTER NGA
        chars.append(0x1706)  #uni1706	TAGALOG LETTER TA
        chars.append(0x1707)  #uni1707	TAGALOG LETTER DA
        chars.append(0x1708)  #uni1708	TAGALOG LETTER NA
        chars.append(0x1709)  #uni1709	TAGALOG LETTER PA
        chars.append(0x170A)  #uni170A	TAGALOG LETTER BA
        chars.append(0x170B)  #uni170B	TAGALOG LETTER MA
        chars.append(0x170C)  #uni170C	TAGALOG LETTER YA
        chars.append(0x000D)  #uni000D	????
        chars.append(0x170E)  #uni170E	TAGALOG LETTER LA
        chars.append(0x170F)  #uni170F	TAGALOG LETTER WA
        chars.append(0x1710)  #uni1710	TAGALOG LETTER SA
        chars.append(0x1711)  #uni1711	TAGALOG LETTER HA
        chars.append(0x1712)  #uni1712	TAGALOG VOWEL SIGN I
        chars.append(0x1713)  #uni1713	TAGALOG VOWEL SIGN U
        chars.append(0x1714)  #uni1714	TAGALOG SIGN VIRAMA
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x1735)  #uni1735	PHILIPPINE SINGLE PUNCTUATION
        chars.append(0x1736)  #uni1736	PHILIPPINE DOUBLE PUNCTUATION
        chars.append(0x1700)  #uni1700	TAGALOG LETTER A
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


