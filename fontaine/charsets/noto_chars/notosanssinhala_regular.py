# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansSinhala-Regular'
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
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0964)  #uni0964	DEVANAGARI DANDA
        chars.append(0x0965)  #uni0965	DEVANAGARI DOUBLE DANDA
        chars.append(0x0D82)  #uni0D82	SINHALA SIGN ANUSVARAYA
        chars.append(0x0D83)  #uni0D83	SINHALA SIGN VISARGAYA
        chars.append(0x0D85)  #uni0D85	SINHALA LETTER AYANNA
        chars.append(0x0D86)  #uni0D86	SINHALA LETTER AAYANNA
        chars.append(0x0D87)  #uni0D87	SINHALA LETTER AEYANNA
        chars.append(0x0D88)  #uni0D88	SINHALA LETTER AEEYANNA
        chars.append(0x0D89)  #uni0D89	SINHALA LETTER IYANNA
        chars.append(0x0D8A)  #uni0D8A	SINHALA LETTER IIYANNA
        chars.append(0x0D8B)  #uni0D8B	SINHALA LETTER UYANNA
        chars.append(0x0D8C)  #uni0D8C	SINHALA LETTER UUYANNA
        chars.append(0x0D8D)  #uni0D8D	SINHALA LETTER IRUYANNA
        chars.append(0x0D8E)  #uni0D8E	SINHALA LETTER IRUUYANNA
        chars.append(0x0D8F)  #uni0D8F	SINHALA LETTER ILUYANNA
        chars.append(0x0D90)  #uni0D90	SINHALA LETTER ILUUYANNA
        chars.append(0x0D91)  #uni0D91	SINHALA LETTER EYANNA
        chars.append(0x0D92)  #uni0D92	SINHALA LETTER EEYANNA
        chars.append(0x0D93)  #uni0D93	SINHALA LETTER AIYANNA
        chars.append(0x0D94)  #uni0D94	SINHALA LETTER OYANNA
        chars.append(0x0D95)  #uni0D95	SINHALA LETTER OOYANNA
        chars.append(0x0D96)  #uni0D96	SINHALA LETTER AUYANNA
        chars.append(0x0D9A)  #uni0D9A	SINHALA LETTER ALPAPRAANA KAYANNA
        chars.append(0x0D9B)  #uni0D9B	SINHALA LETTER MAHAAPRAANA KAYANNA
        chars.append(0x0D9C)  #uni0D9C	SINHALA LETTER ALPAPRAANA GAYANNA
        chars.append(0x0D9D)  #uni0D9D	SINHALA LETTER MAHAAPRAANA GAYANNA
        chars.append(0x0D9E)  #uni0D9E	SINHALA LETTER KANTAJA NAASIKYAYA
        chars.append(0x0D9F)  #uni0D9F	SINHALA LETTER SANYAKA GAYANNA
        chars.append(0x0DA0)  #uni0DA0	SINHALA LETTER ALPAPRAANA CAYANNA
        chars.append(0x0DA1)  #uni0DA1	SINHALA LETTER MAHAAPRAANA CAYANNA
        chars.append(0x0DA2)  #uni0DA2	SINHALA LETTER ALPAPRAANA JAYANNA
        chars.append(0x0DA3)  #uni0DA3	SINHALA LETTER MAHAAPRAANA JAYANNA
        chars.append(0x0DA4)  #uni0DA4	SINHALA LETTER TAALUJA NAASIKYAYA
        chars.append(0x0DA5)  #uni0DA5	SINHALA LETTER TAALUJA SANYOOGA NAAKSIKYAYA
        chars.append(0x0DA6)  #uni0DA6	SINHALA LETTER SANYAKA JAYANNA
        chars.append(0x0DA7)  #uni0DA7	SINHALA LETTER ALPAPRAANA TTAYANNA
        chars.append(0x0DA8)  #uni0DA8	SINHALA LETTER MAHAAPRAANA TTAYANNA
        chars.append(0x0DA9)  #uni0DA9	SINHALA LETTER ALPAPRAANA DDAYANNA
        chars.append(0x0DAA)  #uni0DAA	SINHALA LETTER MAHAAPRAANA DDAYANNA
        chars.append(0x0DAB)  #uni0DAB	SINHALA LETTER MUURDHAJA NAYANNA
        chars.append(0x0DAC)  #uni0DAC	SINHALA LETTER SANYAKA DDAYANNA
        chars.append(0x0DAD)  #uni0DAD	SINHALA LETTER ALPAPRAANA TAYANNA
        chars.append(0x0DAE)  #uni0DAE	SINHALA LETTER MAHAAPRAANA TAYANNA
        chars.append(0x0DAF)  #uni0DAF	SINHALA LETTER ALPAPRAANA DAYANNA
        chars.append(0x0DB0)  #uni0DB0	SINHALA LETTER MAHAAPRAANA DAYANNA
        chars.append(0x0DB1)  #uni0DB1	SINHALA LETTER DANTAJA NAYANNA
        chars.append(0x0DB3)  #uni0DB3	SINHALA LETTER SANYAKA DAYANNA
        chars.append(0x0DB4)  #uni0DB4	SINHALA LETTER ALPAPRAANA PAYANNA
        chars.append(0x0DB5)  #uni0DB5	SINHALA LETTER MAHAAPRAANA PAYANNA
        chars.append(0x0DB6)  #uni0DB6	SINHALA LETTER ALPAPRAANA BAYANNA
        chars.append(0x0DB7)  #uni0DB7	SINHALA LETTER MAHAAPRAANA BAYANNA
        chars.append(0x0DB8)  #uni0DB8	SINHALA LETTER MAYANNA
        chars.append(0x0DB9)  #uni0DB9	SINHALA LETTER AMBA BAYANNA
        chars.append(0x0DBA)  #uni0DBA	SINHALA LETTER YAYANNA
        chars.append(0x0DBB)  #uni0DBB	SINHALA LETTER RAYANNA
        chars.append(0x0DBD)  #uni0DBD	SINHALA LETTER DANTAJA LAYANNA
        chars.append(0x0DC0)  #uni0DC0	SINHALA LETTER VAYANNA
        chars.append(0x0DC1)  #uni0DC1	SINHALA LETTER TAALUJA SAYANNA
        chars.append(0x0DC2)  #uni0DC2	SINHALA LETTER MUURDHAJA SAYANNA
        chars.append(0x0DC3)  #uni0DC3	SINHALA LETTER DANTAJA SAYANNA
        chars.append(0x0DC4)  #uni0DC4	SINHALA LETTER HAYANNA
        chars.append(0x0DC5)  #uni0DC5	SINHALA LETTER MUURDHAJA LAYANNA
        chars.append(0x0DC6)  #uni0DC6	SINHALA LETTER FAYANNA
        chars.append(0x0DCA)  #uni0DCA	SINHALA SIGN AL-LAKUNA
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x0DCF)  #uni0DCF	SINHALA VOWEL SIGN AELA-PILLA
        chars.append(0x0DD0)  #uni0DD0	SINHALA VOWEL SIGN KETTI AEDA-PILLA
        chars.append(0x0DD1)  #uni0DD1	SINHALA VOWEL SIGN DIGA AEDA-PILLA
        chars.append(0x0DD2)  #uni0DD2	SINHALA VOWEL SIGN KETTI IS-PILLA
        chars.append(0x0DD3)  #uni0DD3	SINHALA VOWEL SIGN DIGA IS-PILLA
        chars.append(0x0DD4)  #uni0DD4	SINHALA VOWEL SIGN KETTI PAA-PILLA
        chars.append(0x0DD6)  #uni0DD6	SINHALA VOWEL SIGN DIGA PAA-PILLA
        chars.append(0x0DD8)  #uni0DD8	SINHALA VOWEL SIGN GAETTA-PILLA
        chars.append(0x0DD9)  #uni0DD9	SINHALA VOWEL SIGN KOMBUVA
        chars.append(0x0DDA)  #uni0DDA	SINHALA VOWEL SIGN DIGA KOMBUVA
        chars.append(0x0DDB)  #uni0DDB	SINHALA VOWEL SIGN KOMBU DEKA
        chars.append(0x0DDC)  #uni0DDC	SINHALA VOWEL SIGN KOMBUVA HAA AELA-PILLA
        chars.append(0x0DDD)  #uni0DDD	SINHALA VOWEL SIGN KOMBUVA HAA DIGA AELA-PILLA
        chars.append(0x0DDE)  #uni0DDE	SINHALA VOWEL SIGN KOMBUVA HAA GAYANUKITTA
        chars.append(0x0DDF)  #uni0DDF	SINHALA VOWEL SIGN GAYANUKITTA
        chars.append(0x0DF2)  #uni0DF2	SINHALA VOWEL SIGN DIGA GAETTA-PILLA
        chars.append(0x0DF3)  #uni0DF3	SINHALA VOWEL SIGN DIGA GAYANUKITTA
        chars.append(0x0DF4)  #uni0DF4	SINHALA PUNCTUATION KUNDDALIYA
        return chars


