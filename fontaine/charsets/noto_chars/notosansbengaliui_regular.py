# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansBengaliUI-Regular'
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
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0964)  #uni0964	DEVANAGARI DANDA
        chars.append(0x0965)  #uni0965	DEVANAGARI DOUBLE DANDA
        chars.append(0x0981)  #uni0981	BENGALI SIGN CANDRABINDU
        chars.append(0x0982)  #uni0982	BENGALI SIGN ANUSVARA
        chars.append(0x0983)  #uni0983	BENGALI SIGN VISARGA
        chars.append(0x0985)  #uni0985	BENGALI LETTER A
        chars.append(0x0986)  #uni0986	BENGALI LETTER AA
        chars.append(0x0987)  #uni0987	BENGALI LETTER I
        chars.append(0x0988)  #uni0988	BENGALI LETTER II
        chars.append(0x0989)  #uni0989	BENGALI LETTER U
        chars.append(0x098A)  #uni098A	BENGALI LETTER UU
        chars.append(0x098B)  #uni098B	BENGALI LETTER VOCALIC R
        chars.append(0x098C)  #uni098C	BENGALI LETTER VOCALIC L
        chars.append(0x098F)  #uni098F	BENGALI LETTER E
        chars.append(0x0990)  #uni0990	BENGALI LETTER AI
        chars.append(0x0993)  #uni0993	BENGALI LETTER O
        chars.append(0x0994)  #uni0994	BENGALI LETTER AU
        chars.append(0x0995)  #uni0995	BENGALI LETTER KA
        chars.append(0x0996)  #uni0996	BENGALI LETTER KHA
        chars.append(0x0997)  #uni0997	BENGALI LETTER GA
        chars.append(0x0998)  #uni0998	BENGALI LETTER GHA
        chars.append(0x0999)  #uni0999	BENGALI LETTER NGA
        chars.append(0x099A)  #uni099A	BENGALI LETTER CA
        chars.append(0x099B)  #uni099B	BENGALI LETTER CHA
        chars.append(0x099C)  #uni099C	BENGALI LETTER JA
        chars.append(0x099D)  #uni099D	BENGALI LETTER JHA
        chars.append(0x099E)  #uni099E	BENGALI LETTER NYA
        chars.append(0x099F)  #uni099F	BENGALI LETTER TTA
        chars.append(0x09A0)  #uni09A0	BENGALI LETTER TTHA
        chars.append(0x09A1)  #uni09A1	BENGALI LETTER DDA
        chars.append(0x09A2)  #uni09A2	BENGALI LETTER DDHA
        chars.append(0x09A3)  #uni09A3	BENGALI LETTER NNA
        chars.append(0x09A4)  #uni09A4	BENGALI LETTER TA
        chars.append(0x09A5)  #uni09A5	BENGALI LETTER THA
        chars.append(0x09A6)  #uni09A6	BENGALI LETTER DA
        chars.append(0x09A7)  #uni09A7	BENGALI LETTER DHA
        chars.append(0x09A8)  #uni09A8	BENGALI LETTER NA
        chars.append(0x09AA)  #uni09AA	BENGALI LETTER PA
        chars.append(0x09AB)  #uni09AB	BENGALI LETTER PHA
        chars.append(0x09AC)  #uni09AC	BENGALI LETTER BA
        chars.append(0x09AD)  #uni09AD	BENGALI LETTER BHA
        chars.append(0x09AE)  #uni09AE	BENGALI LETTER MA
        chars.append(0x09AF)  #uni09AF	BENGALI LETTER YA
        chars.append(0x09B0)  #uni09B0	BENGALI LETTER RA
        chars.append(0x09B2)  #uni09B2	BENGALI LETTER LA
        chars.append(0x09B6)  #uni09B6	BENGALI LETTER SHA
        chars.append(0x09B7)  #uni09B7	BENGALI LETTER SSA
        chars.append(0x09B8)  #uni09B8	BENGALI LETTER SA
        chars.append(0x09B9)  #uni09B9	BENGALI LETTER HA
        chars.append(0x09BC)  #uni09BC	BENGALI SIGN NUKTA
        chars.append(0x09BD)  #uni09BD	BENGALI SIGN AVAGRAHA
        chars.append(0x09BE)  #uni09BE	BENGALI VOWEL SIGN AA
        chars.append(0x09BF)  #uni09BF	BENGALI VOWEL SIGN I
        chars.append(0x09C0)  #uni09C0	BENGALI VOWEL SIGN II
        chars.append(0x09C1)  #uni09C1	BENGALI VOWEL SIGN U
        chars.append(0x09C2)  #uni09C2	BENGALI VOWEL SIGN UU
        chars.append(0x09C3)  #uni09C3	BENGALI VOWEL SIGN VOCALIC R
        chars.append(0x09C4)  #uni09C4	BENGALI VOWEL SIGN VOCALIC RR
        chars.append(0x09C7)  #uni09C7	BENGALI VOWEL SIGN E
        chars.append(0x09C8)  #uni09C8	BENGALI VOWEL SIGN AI
        chars.append(0x09CB)  #uni09CB	BENGALI VOWEL SIGN O
        chars.append(0x09CC)  #uni09CC	BENGALI VOWEL SIGN AU
        chars.append(0x09CD)  #uni09CD	BENGALI SIGN VIRAMA
        chars.append(0x09CE)  #uni09CE	BENGALI LETTER KHANDA TA
        chars.append(0x09D7)  #uni09D7	BENGALI AU LENGTH MARK
        chars.append(0x09DC)  #uni09DC	BENGALI LETTER RRA
        chars.append(0x09DD)  #uni09DD	BENGALI LETTER RHA
        chars.append(0x09DF)  #uni09DF	BENGALI LETTER YYA
        chars.append(0x09E0)  #uni09E0	BENGALI LETTER VOCALIC RR
        chars.append(0x09E1)  #uni09E1	BENGALI LETTER VOCALIC LL
        chars.append(0x09E2)  #uni09E2	BENGALI VOWEL SIGN VOCALIC L
        chars.append(0x09E3)  #uni09E3	BENGALI VOWEL SIGN VOCALIC LL
        chars.append(0x09E6)  #uni09E6	BENGALI DIGIT ZERO
        chars.append(0x09E7)  #uni09E7	BENGALI DIGIT ONE
        chars.append(0x09E8)  #uni09E8	BENGALI DIGIT TWO
        chars.append(0x09E9)  #uni09E9	BENGALI DIGIT THREE
        chars.append(0x09EA)  #uni09EA	BENGALI DIGIT FOUR
        chars.append(0x09EB)  #uni09EB	BENGALI DIGIT FIVE
        chars.append(0x09EC)  #uni09EC	BENGALI DIGIT SIX
        chars.append(0x09ED)  #uni09ED	BENGALI DIGIT SEVEN
        chars.append(0x09EE)  #uni09EE	BENGALI DIGIT EIGHT
        chars.append(0x09EF)  #uni09EF	BENGALI DIGIT NINE
        chars.append(0x09F0)  #uni09F0	BENGALI LETTER RA WITH MIDDLE DIAGONAL
        chars.append(0x09F1)  #uni09F1	BENGALI LETTER RA WITH LOWER DIAGONAL
        chars.append(0x09F2)  #uni09F2	BENGALI RUPEE MARK
        chars.append(0x09F3)  #uni09F3	BENGALI RUPEE SIGN
        chars.append(0x09F4)  #uni09F4	BENGALI CURRENCY NUMERATOR ONE
        chars.append(0x09F5)  #uni09F5	BENGALI CURRENCY NUMERATOR TWO
        chars.append(0x09F6)  #uni09F6	BENGALI CURRENCY NUMERATOR THREE
        chars.append(0x09F7)  #uni09F7	BENGALI CURRENCY NUMERATOR FOUR
        chars.append(0x09F8)  #uni09F8	BENGALI CURRENCY NUMERATOR ONE LESS THAN THE DENOMINATOR
        chars.append(0x09F9)  #uni09F9	BENGALI CURRENCY DENOMINATOR SIXTEEN
        chars.append(0x09FA)  #uni09FA	BENGALI ISSHAR
        chars.append(0x09FB)  #uni09FB	BENGALI GANDA MARK
        return chars


