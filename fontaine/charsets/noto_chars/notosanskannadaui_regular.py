# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansKannadaUI-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uni0000	????
        chars.append(0x200B)  #uniFEFF	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0CAD)  #uni0CAD	KANNADA LETTER BHA
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
        chars.append(0x0C82)  #uni0C82	KANNADA SIGN ANUSVARA
        chars.append(0x0C83)  #uni0C83	KANNADA SIGN VISARGA
        chars.append(0x0C85)  #uni0C85	KANNADA LETTER A
        chars.append(0x0C86)  #uni0C86	KANNADA LETTER AA
        chars.append(0x0C87)  #uni0C87	KANNADA LETTER I
        chars.append(0x0C88)  #uni0C88	KANNADA LETTER II
        chars.append(0x0C89)  #uni0C89	KANNADA LETTER U
        chars.append(0x0C8A)  #uni0C8A	KANNADA LETTER UU
        chars.append(0x0C8B)  #uni0C8B	KANNADA LETTER VOCALIC R
        chars.append(0x0C8C)  #uni0C8C	KANNADA LETTER VOCALIC L
        chars.append(0x0C8E)  #uni0C8E	KANNADA LETTER E
        chars.append(0x0C8F)  #uni0C8F	KANNADA LETTER EE
        chars.append(0x0C90)  #uni0C90	KANNADA LETTER AI
        chars.append(0x0C92)  #uni0C92	KANNADA LETTER O
        chars.append(0x0C93)  #uni0C93	KANNADA LETTER OO
        chars.append(0x0C94)  #uni0C94	KANNADA LETTER AU
        chars.append(0x0C95)  #uni0C95	KANNADA LETTER KA
        chars.append(0x0C96)  #uni0C96	KANNADA LETTER KHA
        chars.append(0x0C97)  #uni0C97	KANNADA LETTER GA
        chars.append(0x0C98)  #uni0C98	KANNADA LETTER GHA
        chars.append(0x0C99)  #uni0C99	KANNADA LETTER NGA
        chars.append(0x0C9A)  #uni0C9A	KANNADA LETTER CA
        chars.append(0x0C9B)  #uni0C9B	KANNADA LETTER CHA
        chars.append(0x0C9C)  #uni0C9C	KANNADA LETTER JA
        chars.append(0x0C9D)  #uni0C9D	KANNADA LETTER JHA
        chars.append(0x0C9E)  #uni0C9E	KANNADA LETTER NYA
        chars.append(0x0C9F)  #uni0C9F	KANNADA LETTER TTA
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x0CA1)  #uni0CA1	KANNADA LETTER DDA
        chars.append(0x0CA2)  #uni0CA2	KANNADA LETTER DDHA
        chars.append(0x0CA3)  #uni0CA3	KANNADA LETTER NNA
        chars.append(0x0CA4)  #uni0CA4	KANNADA LETTER TA
        chars.append(0x0CA5)  #uni0CA5	KANNADA LETTER THA
        chars.append(0x0CA6)  #uni0CA6	KANNADA LETTER DA
        chars.append(0x0CA7)  #uni0CA7	KANNADA LETTER DHA
        chars.append(0x0CA8)  #uni0CA8	KANNADA LETTER NA
        chars.append(0x0CAA)  #uni0CAA	KANNADA LETTER PA
        chars.append(0x0CAB)  #uni0CAB	KANNADA LETTER PHA
        chars.append(0x0CAC)  #uni0CAC	KANNADA LETTER BA
        chars.append(0x00AD)  #uni00AD	SOFT HYPHEN
        chars.append(0x0CAE)  #uni0CAE	KANNADA LETTER MA
        chars.append(0x0CAF)  #uni0CAF	KANNADA LETTER YA
        chars.append(0x0CB0)  #uni0CB0	KANNADA LETTER RA
        chars.append(0x0CB1)  #uni0CB1	KANNADA LETTER RRA
        chars.append(0x0CB2)  #uni0CB2	KANNADA LETTER LA
        chars.append(0x0CB3)  #uni0CB3	KANNADA LETTER LLA
        chars.append(0x0CB5)  #uni0CB5	KANNADA LETTER VA
        chars.append(0x0CB6)  #uni0CB6	KANNADA LETTER SHA
        chars.append(0x0CB7)  #uni0CB7	KANNADA LETTER SSA
        chars.append(0x0CB8)  #uni0CB8	KANNADA LETTER SA
        chars.append(0x0CB9)  #uni0CB9	KANNADA LETTER HA
        chars.append(0x0CBC)  #uni0CBC	KANNADA SIGN NUKTA
        chars.append(0x0CBD)  #uni0CBD	KANNADA SIGN AVAGRAHA
        chars.append(0x0CBE)  #uni0CBE	KANNADA VOWEL SIGN AA
        chars.append(0x0CBF)  #uni0CBF	KANNADA VOWEL SIGN I
        chars.append(0x0CC0)  #uni0CC0	KANNADA VOWEL SIGN II
        chars.append(0x0CC1)  #uni0CC1	KANNADA VOWEL SIGN U
        chars.append(0x0CC2)  #uni0CC2	KANNADA VOWEL SIGN UU
        chars.append(0x0CC3)  #uni0CC3	KANNADA VOWEL SIGN VOCALIC R
        chars.append(0x0CC4)  #uni0CC4	KANNADA VOWEL SIGN VOCALIC RR
        chars.append(0x0CC6)  #uni0CC6	KANNADA VOWEL SIGN E
        chars.append(0x0CC7)  #uni0CC7	KANNADA VOWEL SIGN EE
        chars.append(0x0CC8)  #uni0CC8	KANNADA VOWEL SIGN AI
        chars.append(0x0CCA)  #uni0CCA	KANNADA VOWEL SIGN O
        chars.append(0x0CCB)  #uni0CCB	KANNADA VOWEL SIGN OO
        chars.append(0x0CCC)  #uni0CCC	KANNADA VOWEL SIGN AU
        chars.append(0x0CCD)  #uni0CCD	KANNADA SIGN VIRAMA
        chars.append(0x0CD5)  #uni0CD5	KANNADA LENGTH MARK
        chars.append(0x0CD6)  #uni0CD6	KANNADA AI LENGTH MARK
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x0CDE)  #uni0CDE	KANNADA LETTER FA
        chars.append(0x0CE0)  #uni0CE0	KANNADA LETTER VOCALIC RR
        chars.append(0x0CE1)  #uni0CE1	KANNADA LETTER VOCALIC LL
        chars.append(0x0CE2)  #uni0CE2	KANNADA VOWEL SIGN VOCALIC L
        chars.append(0x0CE3)  #uni0CE3	KANNADA VOWEL SIGN VOCALIC LL
        chars.append(0x0CE6)  #uni0CE6	KANNADA DIGIT ZERO
        chars.append(0x0CE7)  #uni0CE7	KANNADA DIGIT ONE
        chars.append(0x0CE8)  #uni0CE8	KANNADA DIGIT TWO
        chars.append(0x0CE9)  #uni0CE9	KANNADA DIGIT THREE
        chars.append(0x0CEA)  #uni0CEA	KANNADA DIGIT FOUR
        chars.append(0x0CEB)  #uni0CEB	KANNADA DIGIT FIVE
        chars.append(0x0CEC)  #uni0CEC	KANNADA DIGIT SIX
        chars.append(0x0CED)  #uni0CED	KANNADA DIGIT SEVEN
        chars.append(0x0CEE)  #uni0CEE	KANNADA DIGIT EIGHT
        chars.append(0x0CEF)  #uni0CEF	KANNADA DIGIT NINE
        chars.append(0x0CF1)  #uni0CF1	KANNADA SIGN JIHVAMULIYA
        chars.append(0x0CF2)  #uni0CF2	KANNADA SIGN UPADHMANIYA
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0964)  #uni0964	DEVANAGARI DANDA
        chars.append(0x0965)  #uni0965	DEVANAGARI DOUBLE DANDA
        chars.append(0x0CA0)  #uni0CA0	KANNADA LETTER TTHA
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        return chars


