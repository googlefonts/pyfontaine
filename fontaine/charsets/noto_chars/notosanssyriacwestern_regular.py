# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansSyriacWestern-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x060C)  #uni060C	ARABIC COMMA
        chars.append(0x000D)  #uni000D	????
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x2212)  #minus	MINUS SIGN
        chars.append(0x0703)  #uni0703	SYRIAC SUPRALINEAR COLON
        chars.append(0x0704)  #uni0704	SYRIAC SUBLINEAR COLON
        chars.append(0x061B)  #uni061B	ARABIC SEMICOLON
        chars.append(0x061F)  #uni061F	ARABIC QUESTION MARK
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0021)  #exclam	EXCLAMATION MARK
        chars.append(0x2026)  #ellipsis	HORIZONTAL ELLIPSIS
        chars.append(0x0028)  #parenleft	LEFT PARENTHESIS
        chars.append(0x0029)  #parenright	RIGHT PARENTHESIS
        chars.append(0x002A)  #asterisk	ASTERISK
        chars.append(0x0707)  #uni0707	SYRIAC COLON SKEWED RIGHT
        chars.append(0x002D)  #hyphen	HYPHEN-MINUS
        chars.append(0x002E)  #period	FULL STOP
        chars.append(0x002F)  #slash	SOLIDUS
        chars.append(0x0708)  #uni0708	SYRIAC SUPRALINEAR COLON SKEWED LEFT
        chars.append(0x003A)  #colon	COLON
        chars.append(0x070A)  #uni070A	SYRIAC CONTRACTION
        chars.append(0x0640)  #uni0640	ARABIC TATWEEL
        chars.append(0x2044)  #fraction	FRACTION SLASH
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x064B)  #uni064B	ARABIC FATHATAN
        chars.append(0x064C)  #uni064C	ARABIC DAMMATAN
        chars.append(0x064D)  #uni064D	ARABIC KASRATAN
        chars.append(0x064E)  #uni064E	ARABIC FATHA
        chars.append(0x064F)  #uni064F	ARABIC DAMMA
        chars.append(0x0650)  #uni0650	ARABIC KASRA
        chars.append(0x0651)  #uni0651	ARABIC SHADDA
        chars.append(0x0652)  #uni0652	ARABIC SUKUN
        chars.append(0x0653)  #uni0653	ARABIC MADDAH ABOVE
        chars.append(0x0654)  #uni0654	ARABIC HAMZA ABOVE
        chars.append(0x0655)  #uni0655	ARABIC HAMZA BELOW
        chars.append(0x005B)  #bracketleft	LEFT SQUARE BRACKET
        chars.append(0x005C)  #backslash	REVERSE SOLIDUS
        chars.append(0x005D)  #bracketright	RIGHT SQUARE BRACKET
        chars.append(0x0660)  #uni0660	ARABIC-INDIC DIGIT ZERO
        chars.append(0x0661)  #uni0661	ARABIC-INDIC DIGIT ONE
        chars.append(0x0662)  #uni0662	ARABIC-INDIC DIGIT TWO
        chars.append(0x0663)  #uni0663	ARABIC-INDIC DIGIT THREE
        chars.append(0x0664)  #uni0664	ARABIC-INDIC DIGIT FOUR
        chars.append(0x0665)  #uni0665	ARABIC-INDIC DIGIT FIVE
        chars.append(0x0666)  #uni0666	ARABIC-INDIC DIGIT SIX
        chars.append(0x0667)  #uni0667	ARABIC-INDIC DIGIT SEVEN
        chars.append(0x0668)  #uni0668	ARABIC-INDIC DIGIT EIGHT
        chars.append(0x0669)  #uni0669	ARABIC-INDIC DIGIT NINE
        chars.append(0x066A)  #uni066A	ARABIC PERCENT SIGN
        chars.append(0x066B)  #uni066B	ARABIC DECIMAL SEPARATOR
        chars.append(0x066C)  #uni066C	ARABIC THOUSANDS SEPARATOR
        chars.append(0x0670)  #uni0670	ARABIC LETTER SUPERSCRIPT ALEF
        chars.append(0x2671)  #uni2671	EAST SYRIAC CROSS
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x250C)  #SF010000	BOX DRAWINGS LIGHT DOWN AND RIGHT
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x2670)  #uni2670	WEST SYRIAC CROSS
        chars.append(0x00AB)  #guillemotleft	LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x00B0)  #degree	DEGREE SIGN
        chars.append(0x00BB)  #guillemotright	RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x0621)  #uni0621	ARABIC LETTER HAMZA
        chars.append(0x0723)  #uni0723	SYRIAC LETTER SEMKATH
        chars.append(0x0724)  #uni0724	SYRIAC LETTER FINAL SEMKATH
        chars.append(0x0725)  #uni0725	SYRIAC LETTER E
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0700)  #uni0700	SYRIAC END OF PARAGRAPH
        chars.append(0x0701)  #uni0701	SYRIAC SUPRALINEAR FULL STOP
        chars.append(0x0702)  #uni0702	SYRIAC SUBLINEAR FULL STOP
        chars.append(0x0303)  #tildecomb	COMBINING TILDE
        chars.append(0x0304)  #uni0304	COMBINING MACRON
        chars.append(0x0705)  #uni0705	SYRIAC HORIZONTAL COLON
        chars.append(0x0706)  #uni0706	SYRIAC COLON SKEWED LEFT
        chars.append(0x0307)  #uni0307	COMBINING DOT ABOVE
        chars.append(0x0308)  #uni0308	COMBINING DIAERESIS
        chars.append(0x0709)  #uni0709	SYRIAC SUBLINEAR COLON SKEWED RIGHT
        chars.append(0x030A)  #uni030A	COMBINING RING ABOVE
        chars.append(0x070B)  #uni070B	SYRIAC HARKLEAN OBELUS
        chars.append(0x070C)  #uni070C	SYRIAC HARKLEAN METOBELUS
        chars.append(0x070D)  #uni070D	SYRIAC HARKLEAN ASTERISCUS
        chars.append(0x2510)  #SF030000	BOX DRAWINGS LIGHT DOWN AND LEFT
        chars.append(0x070F)  #uni070F	SYRIAC ABBREVIATION MARK
        chars.append(0x0710)  #uni0710	SYRIAC LETTER ALAPH
        chars.append(0x0711)  #uni0711	SYRIAC LETTER SUPERSCRIPT ALAPH
        chars.append(0x0712)  #uni0712	SYRIAC LETTER BETH
        chars.append(0x0713)  #uni0713	SYRIAC LETTER GAMAL
        chars.append(0x0714)  #uni0714	SYRIAC LETTER GAMAL GARSHUNI
        chars.append(0x0715)  #uni0715	SYRIAC LETTER DALATH
        chars.append(0x0716)  #uni0716	SYRIAC LETTER DOTLESS DALATH RISH
        chars.append(0x0717)  #uni0717	SYRIAC LETTER HE
        chars.append(0x0718)  #uni0718	SYRIAC LETTER WAW
        chars.append(0x0719)  #uni0719	SYRIAC LETTER ZAIN
        chars.append(0x071A)  #uni071A	SYRIAC LETTER HETH
        chars.append(0x071B)  #uni071B	SYRIAC LETTER TETH
        chars.append(0x071C)  #uni071C	SYRIAC LETTER TETH GARSHUNI
        chars.append(0x071D)  #uni071D	SYRIAC LETTER YUDH
        chars.append(0x071E)  #uni071E	SYRIAC LETTER YUDH HE
        chars.append(0x071F)  #uni071F	SYRIAC LETTER KAPH
        chars.append(0x0720)  #uni0720	SYRIAC LETTER LAMADH
        chars.append(0x0721)  #uni0721	SYRIAC LETTER MIM
        chars.append(0x0722)  #uni0722	SYRIAC LETTER NUN
        chars.append(0x0323)  #dotbelowcomb	COMBINING DOT BELOW
        chars.append(0x0324)  #uni0324	COMBINING DIAERESIS BELOW
        chars.append(0x0325)  #uni0325	COMBINING RING BELOW
        chars.append(0x0726)  #uni0726	SYRIAC LETTER PE
        chars.append(0x0727)  #uni0727	SYRIAC LETTER REVERSED PE
        chars.append(0x0728)  #uni0728	SYRIAC LETTER SADHE
        chars.append(0x0729)  #uni0729	SYRIAC LETTER QAPH
        chars.append(0x072A)  #uni072A	SYRIAC LETTER RISH
        chars.append(0x072B)  #uni072B	SYRIAC LETTER SHIN
        chars.append(0x072C)  #uni072C	SYRIAC LETTER TAW
        chars.append(0x032D)  #uni032D	COMBINING CIRCUMFLEX ACCENT BELOW
        chars.append(0x032E)  #uni032E	COMBINING BREVE BELOW
        chars.append(0x072F)  #uni072F	SYRIAC LETTER PERSIAN DHALATH
        chars.append(0x0330)  #uni0330	COMBINING TILDE BELOW
        chars.append(0x0331)  #uni0331	COMBINING MACRON BELOW
        chars.append(0x0732)  #uni0732	SYRIAC PTHAHA DOTTED
        chars.append(0x0733)  #uni0733	SYRIAC ZQAPHA ABOVE
        chars.append(0x0734)  #uni0734	SYRIAC ZQAPHA BELOW
        chars.append(0x0735)  #uni0735	SYRIAC ZQAPHA DOTTED
        chars.append(0x0736)  #uni0736	SYRIAC RBASA ABOVE
        chars.append(0x0737)  #uni0737	SYRIAC RBASA BELOW
        chars.append(0x0738)  #uni0738	SYRIAC DOTTED ZLAMA HORIZONTAL
        chars.append(0x0739)  #uni0739	SYRIAC DOTTED ZLAMA ANGULAR
        chars.append(0x073A)  #uni073A	SYRIAC HBASA ABOVE
        chars.append(0x073B)  #uni073B	SYRIAC HBASA BELOW
        chars.append(0x073C)  #uni073C	SYRIAC HBASA-ESASA DOTTED
        chars.append(0x073D)  #uni073D	SYRIAC ESASA ABOVE
        chars.append(0x073E)  #uni073E	SYRIAC ESASA BELOW
        chars.append(0x073F)  #uni073F	SYRIAC RWAHA
        chars.append(0x0740)  #uni0740	SYRIAC FEMININE DOT
        chars.append(0x0741)  #uni0741	SYRIAC QUSHSHAYA
        chars.append(0x0742)  #uni0742	SYRIAC RUKKAKHA
        chars.append(0x0743)  #uni0743	SYRIAC TWO VERTICAL DOTS ABOVE
        chars.append(0x0744)  #uni0744	SYRIAC TWO VERTICAL DOTS BELOW
        chars.append(0x0745)  #uni0745	SYRIAC THREE DOTS ABOVE
        chars.append(0x0746)  #uni0746	SYRIAC THREE DOTS BELOW
        chars.append(0x0747)  #uni0747	SYRIAC OBLIQUE LINE ABOVE
        chars.append(0x0748)  #uni0748	SYRIAC OBLIQUE LINE BELOW
        chars.append(0x0749)  #uni0749	SYRIAC MUSIC
        chars.append(0x074A)  #uni074A	SYRIAC BARREKH
        chars.append(0x074D)  #uni074D	SYRIAC LETTER SOGDIAN ZHAIN
        chars.append(0x074E)  #uni074E	SYRIAC LETTER SOGDIAN KHAPH
        chars.append(0x074F)  #uni074F	SYRIAC LETTER SOGDIAN FE
        chars.append(0x002B)  #plus	PLUS SIGN
        chars.append(0x003D)  #equal	EQUALS SIGN
        chars.append(0x072D)  #uni072D	SYRIAC LETTER PERSIAN BHETH
        chars.append(0x072E)  #uni072E	SYRIAC LETTER PERSIAN GHAMAL
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x0730)  #uni0730	SYRIAC PTHAHA ABOVE
        chars.append(0x0731)  #uni0731	SYRIAC PTHAHA BELOW
        return chars


