# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSerifArmenian-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #null	????
        chars.append(0x000D)  #nonmarkingreturn	????
        chars.append(0x0020)  #space	SPACE
        chars.append(0x00A0)  #space	NO-BREAK SPACE
        chars.append(0xFEFF)  #null	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xFB13)  #uniFB13	ARMENIAN SMALL LIGATURE MEN NOW
        chars.append(0xFB14)  #uniFB14	ARMENIAN SMALL LIGATURE MEN ECH
        chars.append(0xFB15)  #uniFB15	ARMENIAN SMALL LIGATURE MEN INI
        chars.append(0xFB16)  #uniFB16	ARMENIAN SMALL LIGATURE VEW NOW
        chars.append(0xFB17)  #uniFB17	ARMENIAN SMALL LIGATURE MEN XEH
        chars.append(0x0531)  #uni0531	ARMENIAN CAPITAL LETTER AYB
        chars.append(0x0532)  #uni0532	ARMENIAN CAPITAL LETTER BEN
        chars.append(0x0533)  #uni0533	ARMENIAN CAPITAL LETTER GIM
        chars.append(0x0534)  #uni0534	ARMENIAN CAPITAL LETTER DA
        chars.append(0x0535)  #uni0535	ARMENIAN CAPITAL LETTER ECH
        chars.append(0x0536)  #uni0536	ARMENIAN CAPITAL LETTER ZA
        chars.append(0x0537)  #uni0537	ARMENIAN CAPITAL LETTER EH
        chars.append(0x0538)  #uni0538	ARMENIAN CAPITAL LETTER ET
        chars.append(0x0539)  #uni0539	ARMENIAN CAPITAL LETTER TO
        chars.append(0x053A)  #uni053A	ARMENIAN CAPITAL LETTER ZHE
        chars.append(0x053B)  #uni053B	ARMENIAN CAPITAL LETTER INI
        chars.append(0x053C)  #uni053C	ARMENIAN CAPITAL LETTER LIWN
        chars.append(0x053D)  #uni053D	ARMENIAN CAPITAL LETTER XEH
        chars.append(0x053E)  #uni053E	ARMENIAN CAPITAL LETTER CA
        chars.append(0x053F)  #uni053F	ARMENIAN CAPITAL LETTER KEN
        chars.append(0x0540)  #uni0540	ARMENIAN CAPITAL LETTER HO
        chars.append(0x0541)  #uni0541	ARMENIAN CAPITAL LETTER JA
        chars.append(0x0542)  #uni0542	ARMENIAN CAPITAL LETTER GHAD
        chars.append(0x0543)  #uni0543	ARMENIAN CAPITAL LETTER CHEH
        chars.append(0x0544)  #uni0544	ARMENIAN CAPITAL LETTER MEN
        chars.append(0x0545)  #uni0545	ARMENIAN CAPITAL LETTER YI
        chars.append(0x0546)  #uni0546	ARMENIAN CAPITAL LETTER NOW
        chars.append(0x0547)  #uni0547	ARMENIAN CAPITAL LETTER SHA
        chars.append(0x0548)  #uni0548	ARMENIAN CAPITAL LETTER VO
        chars.append(0x0549)  #uni0549	ARMENIAN CAPITAL LETTER CHA
        chars.append(0x054A)  #uni054A	ARMENIAN CAPITAL LETTER PEH
        chars.append(0x054B)  #uni054B	ARMENIAN CAPITAL LETTER JHEH
        chars.append(0x054C)  #uni054C	ARMENIAN CAPITAL LETTER RA
        chars.append(0x054D)  #uni054D	ARMENIAN CAPITAL LETTER SEH
        chars.append(0x054E)  #uni054E	ARMENIAN CAPITAL LETTER VEW
        chars.append(0x054F)  #uni054F	ARMENIAN CAPITAL LETTER TIWN
        chars.append(0x0550)  #uni0550	ARMENIAN CAPITAL LETTER REH
        chars.append(0x0551)  #uni0551	ARMENIAN CAPITAL LETTER CO
        chars.append(0x0552)  #uni0552	ARMENIAN CAPITAL LETTER YIWN
        chars.append(0x0553)  #uni0553	ARMENIAN CAPITAL LETTER PIWR
        chars.append(0x0554)  #uni0554	ARMENIAN CAPITAL LETTER KEH
        chars.append(0x0555)  #uni0555	ARMENIAN CAPITAL LETTER OH
        chars.append(0x0556)  #uni0556	ARMENIAN CAPITAL LETTER FEH
        chars.append(0x0559)  #uni0559	ARMENIAN MODIFIER LETTER LEFT HALF RING
        chars.append(0x055A)  #uni055A	ARMENIAN APOSTROPHE
        chars.append(0x055B)  #uni055B	ARMENIAN EMPHASIS MARK
        chars.append(0x055C)  #uni055C	ARMENIAN EXCLAMATION MARK
        chars.append(0x055D)  #uni055D	ARMENIAN COMMA
        chars.append(0x055E)  #uni055E	ARMENIAN QUESTION MARK
        chars.append(0x055F)  #uni055F	ARMENIAN ABBREVIATION MARK
        chars.append(0x0561)  #uni0561	ARMENIAN SMALL LETTER AYB
        chars.append(0x0562)  #uni0562	ARMENIAN SMALL LETTER BEN
        chars.append(0x0563)  #uni0563	ARMENIAN SMALL LETTER GIM
        chars.append(0x0564)  #uni0564	ARMENIAN SMALL LETTER DA
        chars.append(0x0565)  #uni0565	ARMENIAN SMALL LETTER ECH
        chars.append(0x0566)  #uni0566	ARMENIAN SMALL LETTER ZA
        chars.append(0x0567)  #uni0567	ARMENIAN SMALL LETTER EH
        chars.append(0x0568)  #uni0568	ARMENIAN SMALL LETTER ET
        chars.append(0x0569)  #uni0569	ARMENIAN SMALL LETTER TO
        chars.append(0x056A)  #uni056A	ARMENIAN SMALL LETTER ZHE
        chars.append(0x056B)  #uni056B	ARMENIAN SMALL LETTER INI
        chars.append(0x056C)  #uni056C	ARMENIAN SMALL LETTER LIWN
        chars.append(0x056D)  #uni056D	ARMENIAN SMALL LETTER XEH
        chars.append(0x056E)  #uni056E	ARMENIAN SMALL LETTER CA
        chars.append(0x056F)  #uni056F	ARMENIAN SMALL LETTER KEN
        chars.append(0x0570)  #uni0570	ARMENIAN SMALL LETTER HO
        chars.append(0x0571)  #uni0571	ARMENIAN SMALL LETTER JA
        chars.append(0x0572)  #uni0572	ARMENIAN SMALL LETTER GHAD
        chars.append(0x0573)  #uni0573	ARMENIAN SMALL LETTER CHEH
        chars.append(0x0574)  #uni0574	ARMENIAN SMALL LETTER MEN
        chars.append(0x0575)  #uni0575	ARMENIAN SMALL LETTER YI
        chars.append(0x0576)  #uni0576	ARMENIAN SMALL LETTER NOW
        chars.append(0x0577)  #uni0577	ARMENIAN SMALL LETTER SHA
        chars.append(0x0578)  #uni0578	ARMENIAN SMALL LETTER VO
        chars.append(0x0579)  #uni0579	ARMENIAN SMALL LETTER CHA
        chars.append(0x057A)  #uni057A	ARMENIAN SMALL LETTER PEH
        chars.append(0x057B)  #uni057B	ARMENIAN SMALL LETTER JHEH
        chars.append(0x057C)  #uni057C	ARMENIAN SMALL LETTER RA
        chars.append(0x057D)  #uni057D	ARMENIAN SMALL LETTER SEH
        chars.append(0x057E)  #uni057E	ARMENIAN SMALL LETTER VEW
        chars.append(0x057F)  #uni057F	ARMENIAN SMALL LETTER TIWN
        chars.append(0x0580)  #uni0580	ARMENIAN SMALL LETTER REH
        chars.append(0x0581)  #uni0581	ARMENIAN SMALL LETTER CO
        chars.append(0x0582)  #uni0582	ARMENIAN SMALL LETTER YIWN
        chars.append(0x0583)  #uni0583	ARMENIAN SMALL LETTER PIWR
        chars.append(0x0584)  #uni0584	ARMENIAN SMALL LETTER KEH
        chars.append(0x0585)  #uni0585	ARMENIAN SMALL LETTER OH
        chars.append(0x0586)  #uni0586	ARMENIAN SMALL LETTER FEH
        chars.append(0x0587)  #uni0587	ARMENIAN SMALL LIGATURE ECH YIWN
        chars.append(0x0589)  #uni0589	ARMENIAN FULL STOP
        chars.append(0x058A)  #uni058A	ARMENIAN HYPHEN
        chars.append(0x058F)  #uni058F	????
        return chars


