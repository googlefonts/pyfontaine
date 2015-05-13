# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansGujarati-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uni0000	????
        chars.append(0x200B)  #uniFEFF	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0AAD)  #uni0AAD	GUJARATI LETTER BHA
        chars.append(0x2212)  #minus	MINUS SIGN
        chars.append(0x2013)  #endash	EN DASH
        chars.append(0x2014)  #emdash	EM DASH
        chars.append(0x2018)  #quoteleft	LEFT SINGLE QUOTATION MARK
        chars.append(0x2019)  #quoteright	RIGHT SINGLE QUOTATION MARK
        chars.append(0x201C)  #quotedblleft	LEFT DOUBLE QUOTATION MARK
        chars.append(0x201D)  #quotedblright	RIGHT DOUBLE QUOTATION MARK
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x0021)  #exclam	EXCLAMATION MARK
        chars.append(0x0022)  #quotedbl	QUOTATION MARK
        chars.append(0x0023)  #numbersign	NUMBER SIGN
        chars.append(0x0025)  #percent	PERCENT SIGN
        chars.append(0x2026)  #ellipsis	HORIZONTAL ELLIPSIS
        chars.append(0x0027)  #quotesingle	APOSTROPHE
        chars.append(0x0028)  #parenleft	LEFT PARENTHESIS
        chars.append(0x0029)  #parenright	RIGHT PARENTHESIS
        chars.append(0x002A)  #asterisk	ASTERISK
        chars.append(0x002B)  #plus	PLUS SIGN
        chars.append(0x002C)  #comma	COMMA
        chars.append(0x002D)  #hyphen	HYPHEN-MINUS
        chars.append(0x002E)  #period	FULL STOP
        chars.append(0x002F)  #slash	SOLIDUS
        chars.append(0x0030)  #zero	DIGIT ZERO
        chars.append(0x0031)  #one	DIGIT ONE
        chars.append(0x0032)  #two	DIGIT TWO
        chars.append(0x0033)  #three	DIGIT THREE
        chars.append(0x0034)  #four	DIGIT FOUR
        chars.append(0x0035)  #five	DIGIT FIVE
        chars.append(0x0036)  #six	DIGIT SIX
        chars.append(0x0037)  #seven	DIGIT SEVEN
        chars.append(0x0038)  #eight	DIGIT EIGHT
        chars.append(0x0039)  #nine	DIGIT NINE
        chars.append(0x003A)  #colon	COLON
        chars.append(0x003B)  #semicolon	SEMICOLON
        chars.append(0x003C)  #less	LESS-THAN SIGN
        chars.append(0x003D)  #equal	EQUALS SIGN
        chars.append(0x003E)  #greater	GREATER-THAN SIGN
        chars.append(0x003F)  #question	QUESTION MARK
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x20B9)  #uni20B9	????
        chars.append(0x005B)  #bracketleft	LEFT SQUARE BRACKET
        chars.append(0x005C)  #backslash	REVERSE SOLIDUS
        chars.append(0x005D)  #bracketright	RIGHT SQUARE BRACKET
        chars.append(0x005E)  #asciicircum	CIRCUMFLEX ACCENT
        chars.append(0x005F)  #underscore	LOW LINE
        chars.append(0x007B)  #braceleft	LEFT CURLY BRACKET
        chars.append(0x007C)  #bar	VERTICAL LINE
        chars.append(0x007D)  #braceright	RIGHT CURLY BRACKET
        chars.append(0x007E)  #asciitilde	TILDE
        chars.append(0x0A81)  #uni0A81	GUJARATI SIGN CANDRABINDU
        chars.append(0x0A82)  #uni0A82	GUJARATI SIGN ANUSVARA
        chars.append(0x0A83)  #uni0A83	GUJARATI SIGN VISARGA
        chars.append(0x0A85)  #uni0A85	GUJARATI LETTER A
        chars.append(0x0A86)  #uni0A86	GUJARATI LETTER AA
        chars.append(0x0A87)  #uni0A87	GUJARATI LETTER I
        chars.append(0x0A88)  #uni0A88	GUJARATI LETTER II
        chars.append(0x0A89)  #uni0A89	GUJARATI LETTER U
        chars.append(0x0A8A)  #uni0A8A	GUJARATI LETTER UU
        chars.append(0x0A8B)  #uni0A8B	GUJARATI LETTER VOCALIC R
        chars.append(0x0A8C)  #uni0A8C	GUJARATI LETTER VOCALIC L
        chars.append(0x0A8D)  #uni0A8D	GUJARATI VOWEL CANDRA E
        chars.append(0x0A8F)  #uni0A8F	GUJARATI LETTER E
        chars.append(0x0A90)  #uni0A90	GUJARATI LETTER AI
        chars.append(0x0A91)  #uni0A91	GUJARATI VOWEL CANDRA O
        chars.append(0x0A93)  #uni0A93	GUJARATI LETTER O
        chars.append(0x0A94)  #uni0A94	GUJARATI LETTER AU
        chars.append(0x0A95)  #uni0A95	GUJARATI LETTER KA
        chars.append(0x0A96)  #uni0A96	GUJARATI LETTER KHA
        chars.append(0x0A97)  #uni0A97	GUJARATI LETTER GA
        chars.append(0x0A98)  #uni0A98	GUJARATI LETTER GHA
        chars.append(0x0A99)  #uni0A99	GUJARATI LETTER NGA
        chars.append(0x0A9A)  #uni0A9A	GUJARATI LETTER CA
        chars.append(0x0A9B)  #uni0A9B	GUJARATI LETTER CHA
        chars.append(0x0A9C)  #uni0A9C	GUJARATI LETTER JA
        chars.append(0x0A9D)  #uni0A9D	GUJARATI LETTER JHA
        chars.append(0x0A9E)  #uni0A9E	GUJARATI LETTER NYA
        chars.append(0x0A9F)  #uni0A9F	GUJARATI LETTER TTA
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x0AA1)  #uni0AA1	GUJARATI LETTER DDA
        chars.append(0x0AA2)  #uni0AA2	GUJARATI LETTER DDHA
        chars.append(0x0AA3)  #uni0AA3	GUJARATI LETTER NNA
        chars.append(0x0AA4)  #uni0AA4	GUJARATI LETTER TA
        chars.append(0x0AA5)  #uni0AA5	GUJARATI LETTER THA
        chars.append(0x0AA6)  #uni0AA6	GUJARATI LETTER DA
        chars.append(0x0AA7)  #uni0AA7	GUJARATI LETTER DHA
        chars.append(0x0AA8)  #uni0AA8	GUJARATI LETTER NA
        chars.append(0x0AAA)  #uni0AAA	GUJARATI LETTER PA
        chars.append(0x0AAB)  #uni0AAB	GUJARATI LETTER PHA
        chars.append(0x0AAC)  #uni0AAC	GUJARATI LETTER BA
        chars.append(0x00AD)  #uni00AD	SOFT HYPHEN
        chars.append(0x0AAE)  #uni0AAE	GUJARATI LETTER MA
        chars.append(0x0AAF)  #uni0AAF	GUJARATI LETTER YA
        chars.append(0x0AB0)  #uni0AB0	GUJARATI LETTER RA
        chars.append(0x0AB2)  #uni0AB2	GUJARATI LETTER LA
        chars.append(0x0AB3)  #uni0AB3	GUJARATI LETTER LLA
        chars.append(0x0AB5)  #uni0AB5	GUJARATI LETTER VA
        chars.append(0x0AB6)  #uni0AB6	GUJARATI LETTER SHA
        chars.append(0x0AB7)  #uni0AB7	GUJARATI LETTER SSA
        chars.append(0x0AB8)  #uni0AB8	GUJARATI LETTER SA
        chars.append(0x0AB9)  #uni0AB9	GUJARATI LETTER HA
        chars.append(0x0ABC)  #uni0ABC	GUJARATI SIGN NUKTA
        chars.append(0x0ABD)  #uni0ABD	GUJARATI SIGN AVAGRAHA
        chars.append(0x0ABE)  #uni0ABE	GUJARATI VOWEL SIGN AA
        chars.append(0x0ABF)  #uni0ABF	GUJARATI VOWEL SIGN I
        chars.append(0x0AC0)  #uni0AC0	GUJARATI VOWEL SIGN II
        chars.append(0x0AC1)  #uni0AC1	GUJARATI VOWEL SIGN U
        chars.append(0x0AC2)  #uni0AC2	GUJARATI VOWEL SIGN UU
        chars.append(0x0AC3)  #uni0AC3	GUJARATI VOWEL SIGN VOCALIC R
        chars.append(0x0AC4)  #uni0AC4	GUJARATI VOWEL SIGN VOCALIC RR
        chars.append(0x0AC5)  #uni0AC5	GUJARATI VOWEL SIGN CANDRA E
        chars.append(0x0AC7)  #uni0AC7	GUJARATI VOWEL SIGN E
        chars.append(0x0AC8)  #uni0AC8	GUJARATI VOWEL SIGN AI
        chars.append(0x0AC9)  #uni0AC9	GUJARATI VOWEL SIGN CANDRA O
        chars.append(0x0ACB)  #uni0ACB	GUJARATI VOWEL SIGN O
        chars.append(0x0ACC)  #uni0ACC	GUJARATI VOWEL SIGN AU
        chars.append(0x0ACD)  #uni0ACD	GUJARATI SIGN VIRAMA
        chars.append(0x0AD0)  #uni0AD0	GUJARATI OM
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x0AE0)  #uni0AE0	GUJARATI LETTER VOCALIC RR
        chars.append(0x0AE1)  #uni0AE1	GUJARATI LETTER VOCALIC LL
        chars.append(0x0AE2)  #uni0AE2	GUJARATI VOWEL SIGN VOCALIC L
        chars.append(0x0AE3)  #uni0AE3	GUJARATI VOWEL SIGN VOCALIC LL
        chars.append(0x0AE6)  #uni0AE6	GUJARATI DIGIT ZERO
        chars.append(0x0AE7)  #uni0AE7	GUJARATI DIGIT ONE
        chars.append(0x0AE8)  #uni0AE8	GUJARATI DIGIT TWO
        chars.append(0x0AE9)  #uni0AE9	GUJARATI DIGIT THREE
        chars.append(0x0AEA)  #uni0AEA	GUJARATI DIGIT FOUR
        chars.append(0x0AEB)  #uni0AEB	GUJARATI DIGIT FIVE
        chars.append(0x0AEC)  #uni0AEC	GUJARATI DIGIT SIX
        chars.append(0x0AED)  #uni0AED	GUJARATI DIGIT SEVEN
        chars.append(0x0AEE)  #uni0AEE	GUJARATI DIGIT EIGHT
        chars.append(0x0AEF)  #uni0AEF	GUJARATI DIGIT NINE
        chars.append(0x0AF0)  #uni0AF0	????
        chars.append(0x0AF1)  #uni0AF1	GUJARATI RUPEE SIGN
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xA830)  #uniA830	NORTH INDIC FRACTION ONE QUARTER
        chars.append(0xA831)  #uniA831	NORTH INDIC FRACTION ONE HALF
        chars.append(0xA832)  #uniA832	NORTH INDIC FRACTION THREE QUARTERS
        chars.append(0xA833)  #uniA833	NORTH INDIC FRACTION ONE SIXTEENTH
        chars.append(0xA834)  #uniA834	NORTH INDIC FRACTION ONE EIGHTH
        chars.append(0xA835)  #uniA835	NORTH INDIC FRACTION THREE SIXTEENTHS
        chars.append(0xA836)  #uniA836	NORTH INDIC QUARTER MARK
        chars.append(0xA837)  #uniA837	NORTH INDIC PLACEHOLDER MARK
        chars.append(0xA838)  #uniA838	NORTH INDIC RUPEE MARK
        chars.append(0xA839)  #uniA839	NORTH INDIC QUANTITY MARK
        chars.append(0x0964)  #uni0964	DEVANAGARI DANDA
        chars.append(0x0965)  #uni0965	DEVANAGARI DOUBLE DANDA
        chars.append(0x0AA0)  #uni0AA0	GUJARATI LETTER TTHA
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        return chars


