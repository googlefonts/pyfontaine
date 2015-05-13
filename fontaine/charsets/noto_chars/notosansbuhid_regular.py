# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansBuhid-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x174B)  #uni174B	BUHID LETTER MA
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x1735)  #uni1735	PHILIPPINE SINGLE PUNCTUATION
        chars.append(0x1736)  #uni1736	PHILIPPINE DOUBLE PUNCTUATION
        chars.append(0x1740)  #uni1740	BUHID LETTER A
        chars.append(0x1741)  #uni1741	BUHID LETTER I
        chars.append(0x1742)  #uni1742	BUHID LETTER U
        chars.append(0x1743)  #uni1743	BUHID LETTER KA
        chars.append(0x1744)  #uni1744	BUHID LETTER GA
        chars.append(0x1745)  #uni1745	BUHID LETTER NGA
        chars.append(0x1746)  #uni1746	BUHID LETTER TA
        chars.append(0x1747)  #uni1747	BUHID LETTER DA
        chars.append(0x1748)  #uni1748	BUHID LETTER NA
        chars.append(0x1749)  #uni1749	BUHID LETTER PA
        chars.append(0x174A)  #uni174A	BUHID LETTER BA
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x174C)  #uni174C	BUHID LETTER YA
        chars.append(0x174D)  #uni174D	BUHID LETTER RA
        chars.append(0x174E)  #uni174E	BUHID LETTER LA
        chars.append(0x174F)  #uni174F	BUHID LETTER WA
        chars.append(0x1750)  #uni1750	BUHID LETTER SA
        chars.append(0x1751)  #uni1751	BUHID LETTER HA
        chars.append(0x1752)  #uni1752	BUHID VOWEL SIGN I
        chars.append(0x1753)  #uni1753	BUHID VOWEL SIGN U
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


