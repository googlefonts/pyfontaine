# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansMalayalamUI-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uni0000	????
        chars.append(0x200B)  #uniFEFF	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
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
        chars.append(0x005B)  #bracketleft	LEFT SQUARE BRACKET
        chars.append(0x005C)  #backslash	REVERSE SOLIDUS
        chars.append(0x005D)  #bracketright	RIGHT SQUARE BRACKET
        chars.append(0x005E)  #asciicircum	CIRCUMFLEX ACCENT
        chars.append(0x005F)  #underscore	LOW LINE
        chars.append(0x007B)  #braceleft	LEFT CURLY BRACKET
        chars.append(0x007C)  #bar	VERTICAL LINE
        chars.append(0x007D)  #braceright	RIGHT CURLY BRACKET
        chars.append(0x007E)  #asciitilde	TILDE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x00AD)  #uni00AD	SOFT HYPHEN
        chars.append(0x20B9)  #uni20B9	????
        chars.append(0x0D23)  #uni0D23	MALAYALAM LETTER NNA
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0D02)  #uni0D02	MALAYALAM SIGN ANUSVARA
        chars.append(0x0D03)  #uni0D03	MALAYALAM SIGN VISARGA
        chars.append(0x0D05)  #uni0D05	MALAYALAM LETTER A
        chars.append(0x0D06)  #uni0D06	MALAYALAM LETTER AA
        chars.append(0x0307)  #uni0307	COMBINING DOT ABOVE
        chars.append(0x0D08)  #uni0D08	MALAYALAM LETTER II
        chars.append(0x0D09)  #uni0D09	MALAYALAM LETTER U
        chars.append(0x0D0A)  #uni0D0A	MALAYALAM LETTER UU
        chars.append(0x0D0B)  #uni0D0B	MALAYALAM LETTER VOCALIC R
        chars.append(0x0D0C)  #uni0D0C	MALAYALAM LETTER VOCALIC L
        chars.append(0x0D0E)  #uni0D0E	MALAYALAM LETTER E
        chars.append(0x0D0F)  #uni0D0F	MALAYALAM LETTER EE
        chars.append(0x0D10)  #uni0D10	MALAYALAM LETTER AI
        chars.append(0x0D12)  #uni0D12	MALAYALAM LETTER O
        chars.append(0x0D13)  #uni0D13	MALAYALAM LETTER OO
        chars.append(0x0D14)  #uni0D14	MALAYALAM LETTER AU
        chars.append(0x0D15)  #uni0D15	MALAYALAM LETTER KA
        chars.append(0x0D16)  #uni0D16	MALAYALAM LETTER KHA
        chars.append(0x0D17)  #uni0D17	MALAYALAM LETTER GA
        chars.append(0x0D18)  #uni0D18	MALAYALAM LETTER GHA
        chars.append(0x0D19)  #uni0D19	MALAYALAM LETTER NGA
        chars.append(0x0D1A)  #uni0D1A	MALAYALAM LETTER CA
        chars.append(0x0D1B)  #uni0D1B	MALAYALAM LETTER CHA
        chars.append(0x0D1C)  #uni0D1C	MALAYALAM LETTER JA
        chars.append(0x0D1D)  #uni0D1D	MALAYALAM LETTER JHA
        chars.append(0x0D1E)  #uni0D1E	MALAYALAM LETTER NYA
        chars.append(0x0D1F)  #uni0D1F	MALAYALAM LETTER TTA
        chars.append(0x0D20)  #uni0D20	MALAYALAM LETTER TTHA
        chars.append(0x0D21)  #uni0D21	MALAYALAM LETTER DDA
        chars.append(0x0D22)  #uni0D22	MALAYALAM LETTER DDHA
        chars.append(0x0323)  #dotbelowcomb	COMBINING DOT BELOW
        chars.append(0x0D24)  #uni0D24	MALAYALAM LETTER TA
        chars.append(0x0D25)  #uni0D25	MALAYALAM LETTER THA
        chars.append(0x0D26)  #uni0D26	MALAYALAM LETTER DA
        chars.append(0x0D27)  #uni0D27	MALAYALAM LETTER DHA
        chars.append(0x0D28)  #uni0D28	MALAYALAM LETTER NA
        chars.append(0x0D29)  #uni0D29	????
        chars.append(0x0D2A)  #uni0D2A	MALAYALAM LETTER PA
        chars.append(0x0D2B)  #uni0D2B	MALAYALAM LETTER PHA
        chars.append(0x0D2C)  #uni0D2C	MALAYALAM LETTER BA
        chars.append(0x0D2D)  #uni0D2D	MALAYALAM LETTER BHA
        chars.append(0x0D2E)  #uni0D2E	MALAYALAM LETTER MA
        chars.append(0x0D2F)  #uni0D2F	MALAYALAM LETTER YA
        chars.append(0x0D30)  #uni0D30	MALAYALAM LETTER RA
        chars.append(0x0D31)  #uni0D31	MALAYALAM LETTER RRA
        chars.append(0x0D32)  #uni0D32	MALAYALAM LETTER LA
        chars.append(0x0D33)  #uni0D33	MALAYALAM LETTER LLA
        chars.append(0x0D34)  #uni0D34	MALAYALAM LETTER LLLA
        chars.append(0x0D35)  #uni0D35	MALAYALAM LETTER VA
        chars.append(0x0D36)  #uni0D36	MALAYALAM LETTER SHA
        chars.append(0x0D37)  #uni0D37	MALAYALAM LETTER SSA
        chars.append(0x0D38)  #uni0D38	MALAYALAM LETTER SA
        chars.append(0x0D39)  #uni0D39	MALAYALAM LETTER HA
        chars.append(0x0D3A)  #uni0D3A	????
        chars.append(0x0D3D)  #uni0D3D	MALAYALAM SIGN AVAGRAHA
        chars.append(0x0D3E)  #uni0D3E	MALAYALAM VOWEL SIGN AA
        chars.append(0x0D3F)  #uni0D3F	MALAYALAM VOWEL SIGN I
        chars.append(0x0D07)  #uni0D07	MALAYALAM LETTER I
        chars.append(0x0D41)  #uni0D41	MALAYALAM VOWEL SIGN U
        chars.append(0x0D42)  #uni0D42	MALAYALAM VOWEL SIGN UU
        chars.append(0x0D43)  #uni0D43	MALAYALAM VOWEL SIGN VOCALIC R
        chars.append(0x0D44)  #uni0D44	MALAYALAM VOWEL SIGN VOCALIC RR
        chars.append(0x0D46)  #uni0D46	MALAYALAM VOWEL SIGN E
        chars.append(0x0D47)  #uni0D47	MALAYALAM VOWEL SIGN EE
        chars.append(0x0D48)  #uni0D48	MALAYALAM VOWEL SIGN AI
        chars.append(0x0D4A)  #uni0D4A	MALAYALAM VOWEL SIGN O
        chars.append(0x0D4B)  #uni0D4B	MALAYALAM VOWEL SIGN OO
        chars.append(0x0D4C)  #uni0D4C	MALAYALAM VOWEL SIGN AU
        chars.append(0x0D4D)  #uni0D4D	MALAYALAM SIGN VIRAMA
        chars.append(0x0D4E)  #uni0D4E	????
        chars.append(0x0D57)  #uni0D57	MALAYALAM AU LENGTH MARK
        chars.append(0x0D60)  #uni0D60	MALAYALAM LETTER VOCALIC RR
        chars.append(0x0D61)  #uni0D61	MALAYALAM LETTER VOCALIC LL
        chars.append(0x0D62)  #uni0D62	MALAYALAM VOWEL SIGN VOCALIC L
        chars.append(0x0D63)  #uni0D63	MALAYALAM VOWEL SIGN VOCALIC LL
        chars.append(0x0964)  #uni0964	DEVANAGARI DANDA
        chars.append(0x0965)  #uni0965	DEVANAGARI DOUBLE DANDA
        chars.append(0x0D66)  #uni0D66	MALAYALAM DIGIT ZERO
        chars.append(0x0D67)  #uni0D67	MALAYALAM DIGIT ONE
        chars.append(0x0D68)  #uni0D68	MALAYALAM DIGIT TWO
        chars.append(0x0D69)  #uni0D69	MALAYALAM DIGIT THREE
        chars.append(0x0D6A)  #uni0D6A	MALAYALAM DIGIT FOUR
        chars.append(0x0D6B)  #uni0D6B	MALAYALAM DIGIT FIVE
        chars.append(0x0D6C)  #uni0D6C	MALAYALAM DIGIT SIX
        chars.append(0x0D6D)  #uni0D6D	MALAYALAM DIGIT SEVEN
        chars.append(0x0D6E)  #uni0D6E	MALAYALAM DIGIT EIGHT
        chars.append(0x0D6F)  #uni0D6F	MALAYALAM DIGIT NINE
        chars.append(0x0D70)  #uni0D70	MALAYALAM NUMBER TEN
        chars.append(0x0D71)  #uni0D71	MALAYALAM NUMBER ONE HUNDRED
        chars.append(0x0D72)  #uni0D72	MALAYALAM NUMBER ONE THOUSAND
        chars.append(0x0D73)  #uni0D73	MALAYALAM FRACTION ONE QUARTER
        chars.append(0x0D74)  #uni0D74	MALAYALAM FRACTION ONE HALF
        chars.append(0x0D75)  #uni0D75	MALAYALAM FRACTION THREE QUARTERS
        chars.append(0x0D79)  #uni0D79	MALAYALAM DATE MARK
        chars.append(0x0D7A)  #uni0D7A	MALAYALAM LETTER CHILLU NN
        chars.append(0x0D7B)  #uni0D7B	MALAYALAM LETTER CHILLU N
        chars.append(0x0D7C)  #uni0D7C	MALAYALAM LETTER CHILLU RR
        chars.append(0x0D7D)  #uni0D7D	MALAYALAM LETTER CHILLU L
        chars.append(0x0D7E)  #uni0D7E	MALAYALAM LETTER CHILLU LL
        chars.append(0x0D7F)  #uni0D7F	MALAYALAM LETTER CHILLU K
        chars.append(0x0D40)  #uni0D40	MALAYALAM VOWEL SIGN II
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        return chars


