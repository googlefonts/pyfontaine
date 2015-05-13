# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansHanunoo-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x1721)  #uni1721	HANUNOO LETTER I
        chars.append(0x1722)  #uni1722	HANUNOO LETTER U
        chars.append(0x1723)  #uni1723	HANUNOO LETTER KA
        chars.append(0x1724)  #uni1724	HANUNOO LETTER GA
        chars.append(0x1725)  #uni1725	HANUNOO LETTER NGA
        chars.append(0x1726)  #uni1726	HANUNOO LETTER TA
        chars.append(0x1727)  #uni1727	HANUNOO LETTER DA
        chars.append(0x1728)  #uni1728	HANUNOO LETTER NA
        chars.append(0x1729)  #uni1729	HANUNOO LETTER PA
        chars.append(0x172A)  #uni172A	HANUNOO LETTER BA
        chars.append(0x172B)  #uni172B	HANUNOO LETTER MA
        chars.append(0x172C)  #uni172C	HANUNOO LETTER YA
        chars.append(0x172D)  #uni172D	HANUNOO LETTER RA
        chars.append(0x172E)  #uni172E	HANUNOO LETTER LA
        chars.append(0x172F)  #uni172F	HANUNOO LETTER WA
        chars.append(0x1730)  #uni1730	HANUNOO LETTER SA
        chars.append(0x1731)  #uni1731	HANUNOO LETTER HA
        chars.append(0x1732)  #uni1732	HANUNOO VOWEL SIGN I
        chars.append(0x1733)  #uni1733	HANUNOO VOWEL SIGN U
        chars.append(0x1734)  #uni1734	HANUNOO SIGN PAMUDPOD
        chars.append(0x1735)  #uni1735	PHILIPPINE SINGLE PUNCTUATION
        chars.append(0x1736)  #uni1736	PHILIPPINE DOUBLE PUNCTUATION
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x1720)  #uni1720	HANUNOO LETTER A
        return chars


