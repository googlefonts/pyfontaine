# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTamil-Bold'
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
        chars.append(0x0B82)  #uni0B82	TAMIL SIGN ANUSVARA
        chars.append(0x0B83)  #uni0B83	TAMIL SIGN VISARGA
        chars.append(0x0B85)  #uni0B85	TAMIL LETTER A
        chars.append(0x0B86)  #uni0B86	TAMIL LETTER AA
        chars.append(0x0B87)  #uni0B87	TAMIL LETTER I
        chars.append(0x0B88)  #uni0B88	TAMIL LETTER II
        chars.append(0x0B89)  #uni0B89	TAMIL LETTER U
        chars.append(0x0B8A)  #uni0B8A	TAMIL LETTER UU
        chars.append(0x0B8E)  #uni0B8E	TAMIL LETTER E
        chars.append(0x0B8F)  #uni0B8F	TAMIL LETTER EE
        chars.append(0x0B90)  #uni0B90	TAMIL LETTER AI
        chars.append(0x0B92)  #uni0B92	TAMIL LETTER O
        chars.append(0x0B93)  #uni0B93	TAMIL LETTER OO
        chars.append(0x0B94)  #uni0B94	TAMIL LETTER AU
        chars.append(0x0B95)  #uni0B95	TAMIL LETTER KA
        chars.append(0x0B99)  #uni0B99	TAMIL LETTER NGA
        chars.append(0x0B9A)  #uni0B9A	TAMIL LETTER CA
        chars.append(0x0B9C)  #uni0B9C	TAMIL LETTER JA
        chars.append(0x0B9E)  #uni0B9E	TAMIL LETTER NYA
        chars.append(0x0B9F)  #uni0B9F	TAMIL LETTER TTA
        chars.append(0x0BA3)  #uni0BA3	TAMIL LETTER NNA
        chars.append(0x0BA4)  #uni0BA4	TAMIL LETTER TA
        chars.append(0x0BA8)  #uni0BA8	TAMIL LETTER NA
        chars.append(0x0BA9)  #uni0BA9	TAMIL LETTER NNNA
        chars.append(0x0BAA)  #uni0BAA	TAMIL LETTER PA
        chars.append(0x0BAE)  #uni0BAE	TAMIL LETTER MA
        chars.append(0x0BAF)  #uni0BAF	TAMIL LETTER YA
        chars.append(0x0BB0)  #uni0BB0	TAMIL LETTER RA
        chars.append(0x0BB1)  #uni0BB1	TAMIL LETTER RRA
        chars.append(0x0BB2)  #uni0BB2	TAMIL LETTER LA
        chars.append(0x0BB3)  #uni0BB3	TAMIL LETTER LLA
        chars.append(0x0BB4)  #uni0BB4	TAMIL LETTER LLLA
        chars.append(0x0BB5)  #uni0BB5	TAMIL LETTER VA
        chars.append(0x0BB6)  #uni0BB6	TAMIL LETTER SHA
        chars.append(0x0BB7)  #uni0BB7	TAMIL LETTER SSA
        chars.append(0x0BB8)  #uni0BB8	TAMIL LETTER SA
        chars.append(0x0BB9)  #uni0BB9	TAMIL LETTER HA
        chars.append(0x0BBE)  #uni0BBE	TAMIL VOWEL SIGN AA
        chars.append(0x0BBF)  #uni0BBF	TAMIL VOWEL SIGN I
        chars.append(0x0BC0)  #uni0BC0	TAMIL VOWEL SIGN II
        chars.append(0x0BC1)  #uni0BC1	TAMIL VOWEL SIGN U
        chars.append(0x0BC2)  #uni0BC2	TAMIL VOWEL SIGN UU
        chars.append(0x0BC6)  #uni0BC6	TAMIL VOWEL SIGN E
        chars.append(0x0BC7)  #uni0BC7	TAMIL VOWEL SIGN EE
        chars.append(0x0BC8)  #uni0BC8	TAMIL VOWEL SIGN AI
        chars.append(0x0BCA)  #uni0BCA	TAMIL VOWEL SIGN O
        chars.append(0x0BCB)  #uni0BCB	TAMIL VOWEL SIGN OO
        chars.append(0x0BCC)  #uni0BCC	TAMIL VOWEL SIGN AU
        chars.append(0x0BCD)  #uni0BCD	TAMIL SIGN VIRAMA
        chars.append(0x0BD0)  #uni0BD0	TAMIL OM
        chars.append(0x0BD7)  #uni0BD7	TAMIL AU LENGTH MARK
        chars.append(0x0BE6)  #uni0BE6	TAMIL DIGIT ZERO
        chars.append(0x0BE7)  #uni0BE7	TAMIL DIGIT ONE
        chars.append(0x0BE8)  #uni0BE8	TAMIL DIGIT TWO
        chars.append(0x0BE9)  #uni0BE9	TAMIL DIGIT THREE
        chars.append(0x0BEA)  #uni0BEA	TAMIL DIGIT FOUR
        chars.append(0x0BEB)  #uni0BEB	TAMIL DIGIT FIVE
        chars.append(0x0BEC)  #uni0BEC	TAMIL DIGIT SIX
        chars.append(0x0BED)  #uni0BED	TAMIL DIGIT SEVEN
        chars.append(0x0BEE)  #uni0BEE	TAMIL DIGIT EIGHT
        chars.append(0x0BEF)  #uni0BEF	TAMIL DIGIT NINE
        chars.append(0x0BF0)  #uni0BF0	TAMIL NUMBER TEN
        chars.append(0x0BF1)  #uni0BF1	TAMIL NUMBER ONE HUNDRED
        chars.append(0x0BF2)  #uni0BF2	TAMIL NUMBER ONE THOUSAND
        chars.append(0x0BF3)  #uni0BF3	TAMIL DAY SIGN
        chars.append(0x0BF4)  #uni0BF4	TAMIL MONTH SIGN
        chars.append(0x0BF5)  #uni0BF5	TAMIL YEAR SIGN
        chars.append(0x0BF6)  #uni0BF6	TAMIL DEBIT SIGN
        chars.append(0x0BF7)  #uni0BF7	TAMIL CREDIT SIGN
        chars.append(0x0BF8)  #uni0BF8	TAMIL AS ABOVE SIGN
        chars.append(0x0BF9)  #uni0BF9	TAMIL RUPEE SIGN
        chars.append(0x0BFA)  #uni0BFA	TAMIL NUMBER SIGN
        return chars


