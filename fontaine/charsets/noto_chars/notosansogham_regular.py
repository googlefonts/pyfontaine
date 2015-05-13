# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansOgham-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x1681)  #uni1681	OGHAM LETTER BEITH
        chars.append(0x1682)  #uni1682	OGHAM LETTER LUIS
        chars.append(0x1683)  #uni1683	OGHAM LETTER FEARN
        chars.append(0x1684)  #uni1684	OGHAM LETTER SAIL
        chars.append(0x1685)  #uni1685	OGHAM LETTER NION
        chars.append(0x1686)  #uni1686	OGHAM LETTER UATH
        chars.append(0x1687)  #uni1687	OGHAM LETTER DAIR
        chars.append(0x1688)  #uni1688	OGHAM LETTER TINNE
        chars.append(0x1689)  #uni1689	OGHAM LETTER COLL
        chars.append(0x168A)  #uni168A	OGHAM LETTER CEIRT
        chars.append(0x168B)  #uni168B	OGHAM LETTER MUIN
        chars.append(0x168C)  #uni168C	OGHAM LETTER GORT
        chars.append(0x000D)  #uni000D	????
        chars.append(0x168E)  #uni168E	OGHAM LETTER STRAIF
        chars.append(0x168F)  #uni168F	OGHAM LETTER RUIS
        chars.append(0x1690)  #uni1690	OGHAM LETTER AILM
        chars.append(0x1691)  #uni1691	OGHAM LETTER ONN
        chars.append(0x1692)  #uni1692	OGHAM LETTER UR
        chars.append(0x1693)  #uni1693	OGHAM LETTER EADHADH
        chars.append(0x1694)  #uni1694	OGHAM LETTER IODHADH
        chars.append(0x1695)  #uni1695	OGHAM LETTER EABHADH
        chars.append(0x1696)  #uni1696	OGHAM LETTER OR
        chars.append(0x1697)  #uni1697	OGHAM LETTER UILLEANN
        chars.append(0x1698)  #uni1698	OGHAM LETTER IFIN
        chars.append(0x1699)  #uni1699	OGHAM LETTER EAMHANCHOLL
        chars.append(0x169A)  #uni169A	OGHAM LETTER PEITH
        chars.append(0x169B)  #uni169B	OGHAM FEATHER MARK
        chars.append(0x169C)  #uni169C	OGHAM REVERSED FEATHER MARK
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x1680)  #uni1680	OGHAM SPACE MARK
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x168D)  #uni168D	OGHAM LETTER NGEADAL
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


