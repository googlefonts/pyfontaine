# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTagbanwa-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x1735)  #uni1735	PHILIPPINE SINGLE PUNCTUATION
        chars.append(0x1736)  #uni1736	PHILIPPINE DOUBLE PUNCTUATION
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x1760)  #uni1760	TAGBANWA LETTER A
        chars.append(0x1761)  #uni1761	TAGBANWA LETTER I
        chars.append(0x1762)  #uni1762	TAGBANWA LETTER U
        chars.append(0x1763)  #uni1763	TAGBANWA LETTER KA
        chars.append(0x1764)  #uni1764	TAGBANWA LETTER GA
        chars.append(0x1765)  #uni1765	TAGBANWA LETTER NGA
        chars.append(0x1766)  #uni1766	TAGBANWA LETTER TA
        chars.append(0x1767)  #uni1767	TAGBANWA LETTER DA
        chars.append(0x1768)  #uni1768	TAGBANWA LETTER NA
        chars.append(0x1769)  #uni1769	TAGBANWA LETTER PA
        chars.append(0x176A)  #uni176A	TAGBANWA LETTER BA
        chars.append(0x176B)  #uni176B	TAGBANWA LETTER MA
        chars.append(0x176C)  #uni176C	TAGBANWA LETTER YA
        chars.append(0x176E)  #uni176E	TAGBANWA LETTER LA
        chars.append(0x176F)  #uni176F	TAGBANWA LETTER WA
        chars.append(0x1770)  #uni1770	TAGBANWA LETTER SA
        chars.append(0x1772)  #uni1772	TAGBANWA VOWEL SIGN I
        chars.append(0x1773)  #uni1773	TAGBANWA VOWEL SIGN U
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


