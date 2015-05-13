# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTagalog-Regular'
    native_name = ''

    def glyphs(self):
        glyphs = []
        glyphs.append(0x0001)  #uniFEFF
        glyphs.append(0x000D)  #uni1709
        glyphs.append(0x000C)  #uni1708
        glyphs.append(0x0009)  #uni1705
        glyphs.append(0x0008)  #uni1704
        glyphs.append(0x000B)  #uni1707
        glyphs.append(0x000A)  #uni1706
        glyphs.append(0x0005)  #uni1701
        glyphs.append(0x0004)  #uni1700
        glyphs.append(0x0007)  #uni1703
        glyphs.append(0x0006)  #uni1702
        glyphs.append(0x0002)  #uni000D
        glyphs.append(0x0003)  #uni00A0
        glyphs.append(0x0018)  #uni1735
        glyphs.append(0x0019)  #uni1736
        glyphs.append(0x0015)  #uni1712
        glyphs.append(0x0016)  #uni1713
        glyphs.append(0x0013)  #uni1710
        glyphs.append(0x0014)  #uni1711
        glyphs.append(0x0017)  #uni1714
        glyphs.append(0x0011)  #uni170E
        glyphs.append(0x0012)  #uni170F
        glyphs.append(0x000E)  #uni170A
        glyphs.append(0x0010)  #uni170C
        glyphs.append(0x000F)  #uni170B
        glyphs.append(0x0000)  #.notdef
        return glyphs


