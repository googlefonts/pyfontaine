# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'Arimo-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x2000)  #uni2000	EN QUAD
        chars.append(0x2001)  #uni2001	EM QUAD
        chars.append(0x2002)  #uni2002	EN SPACE
        chars.append(0x2003)  #uni2003	EM SPACE
        chars.append(0x2004)  #uni2004	THREE-PER-EM SPACE
        chars.append(0x2005)  #uni2005	FOUR-PER-EM SPACE
        chars.append(0x2006)  #uni2006	SIX-PER-EM SPACE
        chars.append(0x2007)  #uni2007	FIGURE SPACE
        chars.append(0x2008)  #uni2008	PUNCTUATION SPACE
        chars.append(0x2009)  #uni2009	THIN SPACE
        chars.append(0x200A)  #uni200A	HAIR SPACE
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x2012)  #uni2012	FIGURE DASH
        chars.append(0x2013)  #endash	EN DASH
        chars.append(0x2014)  #emdash	EM DASH
        chars.append(0x2015)  #uni2015	HORIZONTAL BAR
        chars.append(0x2016)  #uni01C1	DOUBLE VERTICAL LINE
        chars.append(0x2017)  #underscoredbl	DOUBLE LOW LINE
        chars.append(0x2018)  #quoteleft	LEFT SINGLE QUOTATION MARK
        chars.append(0x2019)  #quoteright	RIGHT SINGLE QUOTATION MARK
        chars.append(0x201A)  #quotesinglbase	SINGLE LOW-9 QUOTATION MARK
        chars.append(0x201B)  #quotereversed	SINGLE HIGH-REVERSED-9 QUOTATION MARK
        chars.append(0x201C)  #quotedblleft	LEFT DOUBLE QUOTATION MARK
        chars.append(0x201D)  #quotedblright	RIGHT DOUBLE QUOTATION MARK
        chars.append(0x201E)  #quotedblbase	DOUBLE LOW-9 QUOTATION MARK
        chars.append(0x201F)  #uni201F	DOUBLE HIGH-REVERSED-9 QUOTATION MARK
        chars.append(0x0020)  #space	SPACE
        chars.append(0x0021)  #exclam	EXCLAMATION MARK
        chars.append(0x0022)  #quotedbl	QUOTATION MARK
        chars.append(0x0023)  #numbersign	NUMBER SIGN
        chars.append(0x0024)  #dollar	DOLLAR SIGN
        chars.append(0x0025)  #percent	PERCENT SIGN
        chars.append(0x0026)  #ampersand	AMPERSAND
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
        chars.append(0x0040)  #at	COMMERCIAL AT
        chars.append(0x0041)  #A	LATIN CAPITAL LETTER A
        chars.append(0x0042)  #B	LATIN CAPITAL LETTER B
        chars.append(0x0043)  #C	LATIN CAPITAL LETTER C
        chars.append(0x0044)  #D	LATIN CAPITAL LETTER D
        chars.append(0x0045)  #E	LATIN CAPITAL LETTER E
        chars.append(0x0046)  #F	LATIN CAPITAL LETTER F
        chars.append(0x0047)  #G	LATIN CAPITAL LETTER G
        chars.append(0x0048)  #H	LATIN CAPITAL LETTER H
        chars.append(0x0049)  #I	LATIN CAPITAL LETTER I
        chars.append(0x004A)  #J	LATIN CAPITAL LETTER J
        chars.append(0x004B)  #K	LATIN CAPITAL LETTER K
        chars.append(0x004C)  #L	LATIN CAPITAL LETTER L
        chars.append(0x004D)  #M	LATIN CAPITAL LETTER M
        chars.append(0x004E)  #N	LATIN CAPITAL LETTER N
        chars.append(0x004F)  #O	LATIN CAPITAL LETTER O
        chars.append(0x0050)  #P	LATIN CAPITAL LETTER P
        chars.append(0x0051)  #Q	LATIN CAPITAL LETTER Q
        chars.append(0x0052)  #R	LATIN CAPITAL LETTER R
        chars.append(0x0053)  #S	LATIN CAPITAL LETTER S
        chars.append(0x0054)  #T	LATIN CAPITAL LETTER T
        chars.append(0x0055)  #U	LATIN CAPITAL LETTER U
        chars.append(0x0056)  #V	LATIN CAPITAL LETTER V
        chars.append(0x0057)  #W	LATIN CAPITAL LETTER W
        chars.append(0x0058)  #X	LATIN CAPITAL LETTER X
        chars.append(0x0059)  #Y	LATIN CAPITAL LETTER Y
        chars.append(0x005A)  #Z	LATIN CAPITAL LETTER Z
        chars.append(0x005B)  #bracketleft	LEFT SQUARE BRACKET
        chars.append(0x005C)  #backslash	REVERSE SOLIDUS
        chars.append(0x005D)  #bracketright	RIGHT SQUARE BRACKET
        chars.append(0x005E)  #asciicircum	CIRCUMFLEX ACCENT
        chars.append(0x005F)  #underscore	LOW LINE
        chars.append(0x0060)  #grave	GRAVE ACCENT
        chars.append(0x0061)  #a	LATIN SMALL LETTER A
        chars.append(0x0062)  #b	LATIN SMALL LETTER B
        chars.append(0x0063)  #c	LATIN SMALL LETTER C
        chars.append(0x0064)  #d	LATIN SMALL LETTER D
        chars.append(0x0065)  #e	LATIN SMALL LETTER E
        chars.append(0x0066)  #f	LATIN SMALL LETTER F
        chars.append(0x0067)  #g	LATIN SMALL LETTER G
        chars.append(0x0068)  #h	LATIN SMALL LETTER H
        chars.append(0x0069)  #i	LATIN SMALL LETTER I
        chars.append(0x006A)  #j	LATIN SMALL LETTER J
        chars.append(0x006B)  #k	LATIN SMALL LETTER K
        chars.append(0x006C)  #l	LATIN SMALL LETTER L
        chars.append(0x006D)  #m	LATIN SMALL LETTER M
        chars.append(0x006E)  #n	LATIN SMALL LETTER N
        chars.append(0x006F)  #o	LATIN SMALL LETTER O
        chars.append(0x0070)  #p	LATIN SMALL LETTER P
        chars.append(0x0071)  #q	LATIN SMALL LETTER Q
        chars.append(0x0072)  #r	LATIN SMALL LETTER R
        chars.append(0x0073)  #s	LATIN SMALL LETTER S
        chars.append(0x0074)  #t	LATIN SMALL LETTER T
        chars.append(0x0075)  #u	LATIN SMALL LETTER U
        chars.append(0x0076)  #v	LATIN SMALL LETTER V
        chars.append(0x0077)  #w	LATIN SMALL LETTER W
        chars.append(0x0078)  #x	LATIN SMALL LETTER X
        chars.append(0x0079)  #y	LATIN SMALL LETTER Y
        chars.append(0x007A)  #z	LATIN SMALL LETTER Z
        chars.append(0x007B)  #braceleft	LEFT CURLY BRACKET
        chars.append(0x007C)  #bar	VERTICAL LINE
        chars.append(0x007D)  #braceright	RIGHT CURLY BRACKET
        chars.append(0x007E)  #asciitilde	TILDE
        chars.append(0x207F)  #nsuperior	SUPERSCRIPT LATIN SMALL LETTER N
        chars.append(0x2090)  #uni2090	LATIN SUBSCRIPT SMALL LETTER A
        chars.append(0x2091)  #uni2091	LATIN SUBSCRIPT SMALL LETTER E
        chars.append(0x2092)  #uni2092	LATIN SUBSCRIPT SMALL LETTER O
        chars.append(0x2093)  #uni2093	LATIN SUBSCRIPT SMALL LETTER X
        chars.append(0x2094)  #uni2094	LATIN SUBSCRIPT SMALL LETTER SCHWA
        chars.append(0x00A0)  #space	NO-BREAK SPACE
        chars.append(0x00A1)  #exclamdown	INVERTED EXCLAMATION MARK
        chars.append(0x00A2)  #cent	CENT SIGN
        chars.append(0x00A3)  #sterling	POUND SIGN
        chars.append(0x00A4)  #currency	CURRENCY SIGN
        chars.append(0x00A5)  #yen	YEN SIGN
        chars.append(0x00A6)  #brokenbar	BROKEN BAR
        chars.append(0x00A7)  #section	SECTION SIGN
        chars.append(0x00A8)  #dieresis	DIAERESIS
        chars.append(0x00A9)  #copyright	COPYRIGHT SIGN
        chars.append(0x00AA)  #ordfeminine	FEMININE ORDINAL INDICATOR
        chars.append(0x00AB)  #guillemotleft	LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x00AC)  #logicalnot	NOT SIGN
        chars.append(0x00AD)  #hyphen	SOFT HYPHEN
        chars.append(0x00AE)  #registered	REGISTERED SIGN
        chars.append(0x00AF)  #overscore	MACRON
        chars.append(0x00B0)  #degree	DEGREE SIGN
        chars.append(0x00B1)  #plusminus	PLUS-MINUS SIGN
        chars.append(0x00B2)  #twosuperior	SUPERSCRIPT TWO
        chars.append(0x00B3)  #threesuperior	SUPERSCRIPT THREE
        chars.append(0x00B4)  #acute	ACUTE ACCENT
        chars.append(0x00B5)  #mu1	MICRO SIGN
        chars.append(0x00B6)  #paragraph	PILCROW SIGN
        chars.append(0x00B7)  #middot	MIDDLE DOT
        chars.append(0x00B8)  #cedilla	CEDILLA
        chars.append(0x00B9)  #onesuperior	SUPERSCRIPT ONE
        chars.append(0x00BA)  #ordmasculine	MASCULINE ORDINAL INDICATOR
        chars.append(0x00BB)  #guillemotright	RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x00BC)  #onequarter	VULGAR FRACTION ONE QUARTER
        chars.append(0x00BD)  #onehalf	VULGAR FRACTION ONE HALF
        chars.append(0x00BE)  #threequarters	VULGAR FRACTION THREE QUARTERS
        chars.append(0x00BF)  #questiondown	INVERTED QUESTION MARK
        chars.append(0x00C0)  #Agrave	LATIN CAPITAL LETTER A WITH GRAVE
        chars.append(0x00C1)  #Aacute	LATIN CAPITAL LETTER A WITH ACUTE
        chars.append(0x00C2)  #Acircumflex	LATIN CAPITAL LETTER A WITH CIRCUMFLEX
        chars.append(0x00C3)  #Atilde	LATIN CAPITAL LETTER A WITH TILDE
        chars.append(0x00C4)  #Adieresis	LATIN CAPITAL LETTER A WITH DIAERESIS
        chars.append(0x00C5)  #Aring	LATIN CAPITAL LETTER A WITH RING ABOVE
        chars.append(0x00C6)  #AE	LATIN CAPITAL LETTER AE
        chars.append(0x00C7)  #Ccedilla	LATIN CAPITAL LETTER C WITH CEDILLA
        chars.append(0x00C8)  #Egrave	LATIN CAPITAL LETTER E WITH GRAVE
        chars.append(0x00C9)  #Eacute	LATIN CAPITAL LETTER E WITH ACUTE
        chars.append(0x00CA)  #Ecircumflex	LATIN CAPITAL LETTER E WITH CIRCUMFLEX
        chars.append(0x00CB)  #Edieresis	LATIN CAPITAL LETTER E WITH DIAERESIS
        chars.append(0x00CC)  #Igrave	LATIN CAPITAL LETTER I WITH GRAVE
        chars.append(0x00CD)  #Iacute	LATIN CAPITAL LETTER I WITH ACUTE
        chars.append(0x00CE)  #Icircumflex	LATIN CAPITAL LETTER I WITH CIRCUMFLEX
        chars.append(0x00CF)  #Idieresis	LATIN CAPITAL LETTER I WITH DIAERESIS
        chars.append(0x00D0)  #Eth	LATIN CAPITAL LETTER ETH
        chars.append(0x00D1)  #Ntilde	LATIN CAPITAL LETTER N WITH TILDE
        chars.append(0x00D2)  #Ograve	LATIN CAPITAL LETTER O WITH GRAVE
        chars.append(0x00D3)  #Oacute	LATIN CAPITAL LETTER O WITH ACUTE
        chars.append(0x00D4)  #Ocircumflex	LATIN CAPITAL LETTER O WITH CIRCUMFLEX
        chars.append(0x00D5)  #Otilde	LATIN CAPITAL LETTER O WITH TILDE
        chars.append(0x00D6)  #Odieresis	LATIN CAPITAL LETTER O WITH DIAERESIS
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x00D8)  #Oslash	LATIN CAPITAL LETTER O WITH STROKE
        chars.append(0x00D9)  #Ugrave	LATIN CAPITAL LETTER U WITH GRAVE
        chars.append(0x00DA)  #Uacute	LATIN CAPITAL LETTER U WITH ACUTE
        chars.append(0x00DB)  #Ucircumflex	LATIN CAPITAL LETTER U WITH CIRCUMFLEX
        chars.append(0x00DC)  #Udieresis	LATIN CAPITAL LETTER U WITH DIAERESIS
        chars.append(0x00DD)  #Yacute	LATIN CAPITAL LETTER Y WITH ACUTE
        chars.append(0x00DE)  #Thorn	LATIN CAPITAL LETTER THORN
        chars.append(0x00DF)  #germandbls	LATIN SMALL LETTER SHARP S
        chars.append(0x00E0)  #agrave	LATIN SMALL LETTER A WITH GRAVE
        chars.append(0x00E1)  #aacute	LATIN SMALL LETTER A WITH ACUTE
        chars.append(0x00E2)  #acircumflex	LATIN SMALL LETTER A WITH CIRCUMFLEX
        chars.append(0x00E3)  #atilde	LATIN SMALL LETTER A WITH TILDE
        chars.append(0x00E4)  #adieresis	LATIN SMALL LETTER A WITH DIAERESIS
        chars.append(0x00E5)  #aring	LATIN SMALL LETTER A WITH RING ABOVE
        chars.append(0x00E6)  #ae	LATIN SMALL LETTER AE
        chars.append(0x00E7)  #ccedilla	LATIN SMALL LETTER C WITH CEDILLA
        chars.append(0x00E8)  #egrave	LATIN SMALL LETTER E WITH GRAVE
        chars.append(0x00E9)  #eacute	LATIN SMALL LETTER E WITH ACUTE
        chars.append(0x00EA)  #ecircumflex	LATIN SMALL LETTER E WITH CIRCUMFLEX
        chars.append(0x00EB)  #edieresis	LATIN SMALL LETTER E WITH DIAERESIS
        chars.append(0x00EC)  #igrave	LATIN SMALL LETTER I WITH GRAVE
        chars.append(0x00ED)  #iacute	LATIN SMALL LETTER I WITH ACUTE
        chars.append(0x00EE)  #icircumflex	LATIN SMALL LETTER I WITH CIRCUMFLEX
        chars.append(0x00EF)  #idieresis	LATIN SMALL LETTER I WITH DIAERESIS
        chars.append(0x00F0)  #eth	LATIN SMALL LETTER ETH
        chars.append(0x00F1)  #ntilde	LATIN SMALL LETTER N WITH TILDE
        chars.append(0x00F2)  #ograve	LATIN SMALL LETTER O WITH GRAVE
        chars.append(0x00F3)  #oacute	LATIN SMALL LETTER O WITH ACUTE
        chars.append(0x00F4)  #ocircumflex	LATIN SMALL LETTER O WITH CIRCUMFLEX
        chars.append(0x00F5)  #otilde	LATIN SMALL LETTER O WITH TILDE
        chars.append(0x00F6)  #odieresis	LATIN SMALL LETTER O WITH DIAERESIS
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0x00F8)  #oslash	LATIN SMALL LETTER O WITH STROKE
        chars.append(0x00F9)  #ugrave	LATIN SMALL LETTER U WITH GRAVE
        chars.append(0x00FA)  #uacute	LATIN SMALL LETTER U WITH ACUTE
        chars.append(0x00FB)  #ucircumflex	LATIN SMALL LETTER U WITH CIRCUMFLEX
        chars.append(0x00FC)  #udieresis	LATIN SMALL LETTER U WITH DIAERESIS
        chars.append(0x00FD)  #yacute	LATIN SMALL LETTER Y WITH ACUTE
        chars.append(0x00FE)  #thorn	LATIN SMALL LETTER THORN
        chars.append(0x00FF)  #ydieresis	LATIN SMALL LETTER Y WITH DIAERESIS
        chars.append(0x0100)  #Amacron	LATIN CAPITAL LETTER A WITH MACRON
        chars.append(0x0101)  #amacron	LATIN SMALL LETTER A WITH MACRON
        chars.append(0x0102)  #Abreve	LATIN CAPITAL LETTER A WITH BREVE
        chars.append(0x0103)  #abreve	LATIN SMALL LETTER A WITH BREVE
        chars.append(0x0104)  #Aogonek	LATIN CAPITAL LETTER A WITH OGONEK
        chars.append(0x0105)  #aogonek	LATIN SMALL LETTER A WITH OGONEK
        chars.append(0x0106)  #Cacute	LATIN CAPITAL LETTER C WITH ACUTE
        chars.append(0x0107)  #cacute	LATIN SMALL LETTER C WITH ACUTE
        chars.append(0x0108)  #Ccircumflex	LATIN CAPITAL LETTER C WITH CIRCUMFLEX
        chars.append(0x0109)  #ccircumflex	LATIN SMALL LETTER C WITH CIRCUMFLEX
        chars.append(0x010A)  #Cdotaccent	LATIN CAPITAL LETTER C WITH DOT ABOVE
        chars.append(0x010B)  #cdotaccent	LATIN SMALL LETTER C WITH DOT ABOVE
        chars.append(0x010C)  #Ccaron	LATIN CAPITAL LETTER C WITH CARON
        chars.append(0x010D)  #ccaron	LATIN SMALL LETTER C WITH CARON
        chars.append(0x010E)  #Dcaron	LATIN CAPITAL LETTER D WITH CARON
        chars.append(0x010F)  #dcaron	LATIN SMALL LETTER D WITH CARON
        chars.append(0x0110)  #Dcroat	LATIN CAPITAL LETTER D WITH STROKE
        chars.append(0x0111)  #dcroat	LATIN SMALL LETTER D WITH STROKE
        chars.append(0x0112)  #Emacron	LATIN CAPITAL LETTER E WITH MACRON
        chars.append(0x0113)  #emacron	LATIN SMALL LETTER E WITH MACRON
        chars.append(0x0114)  #Ebreve	LATIN CAPITAL LETTER E WITH BREVE
        chars.append(0x0115)  #ebreve	LATIN SMALL LETTER E WITH BREVE
        chars.append(0x0116)  #Edotaccent	LATIN CAPITAL LETTER E WITH DOT ABOVE
        chars.append(0x0117)  #edotaccent	LATIN SMALL LETTER E WITH DOT ABOVE
        chars.append(0x0118)  #Eogonek	LATIN CAPITAL LETTER E WITH OGONEK
        chars.append(0x0119)  #eogonek	LATIN SMALL LETTER E WITH OGONEK
        chars.append(0x011A)  #Ecaron	LATIN CAPITAL LETTER E WITH CARON
        chars.append(0x011B)  #ecaron	LATIN SMALL LETTER E WITH CARON
        chars.append(0x011C)  #Gcircumflex	LATIN CAPITAL LETTER G WITH CIRCUMFLEX
        chars.append(0x011D)  #gcircumflex	LATIN SMALL LETTER G WITH CIRCUMFLEX
        chars.append(0x011E)  #Gbreve	LATIN CAPITAL LETTER G WITH BREVE
        chars.append(0x011F)  #gbreve	LATIN SMALL LETTER G WITH BREVE
        chars.append(0x0120)  #Gdotaccent	LATIN CAPITAL LETTER G WITH DOT ABOVE
        chars.append(0x0121)  #gdotaccent	LATIN SMALL LETTER G WITH DOT ABOVE
        chars.append(0x0122)  #Gcommaaccent	LATIN CAPITAL LETTER G WITH CEDILLA
        chars.append(0x0123)  #gcommaaccent	LATIN SMALL LETTER G WITH CEDILLA
        chars.append(0x0124)  #Hcircumflex	LATIN CAPITAL LETTER H WITH CIRCUMFLEX
        chars.append(0x0125)  #hcircumflex	LATIN SMALL LETTER H WITH CIRCUMFLEX
        chars.append(0x0126)  #Hbar	LATIN CAPITAL LETTER H WITH STROKE
        chars.append(0x0127)  #hbar	LATIN SMALL LETTER H WITH STROKE
        chars.append(0x0128)  #Itilde	LATIN CAPITAL LETTER I WITH TILDE
        chars.append(0x0129)  #itilde	LATIN SMALL LETTER I WITH TILDE
        chars.append(0x012A)  #Imacron	LATIN CAPITAL LETTER I WITH MACRON
        chars.append(0x012B)  #imacron	LATIN SMALL LETTER I WITH MACRON
        chars.append(0x012C)  #Ibreve	LATIN CAPITAL LETTER I WITH BREVE
        chars.append(0x012D)  #ibreve	LATIN SMALL LETTER I WITH BREVE
        chars.append(0x012E)  #Iogonek	LATIN CAPITAL LETTER I WITH OGONEK
        chars.append(0x012F)  #iogonek	LATIN SMALL LETTER I WITH OGONEK
        chars.append(0x0130)  #Idotaccent	LATIN CAPITAL LETTER I WITH DOT ABOVE
        chars.append(0x0131)  #dotlessi	LATIN SMALL LETTER DOTLESS I
        chars.append(0x0132)  #IJ	LATIN CAPITAL LIGATURE IJ
        chars.append(0x0133)  #ij	LATIN SMALL LIGATURE IJ
        chars.append(0x0134)  #Jcircumflex	LATIN CAPITAL LETTER J WITH CIRCUMFLEX
        chars.append(0x0135)  #jcircumflex	LATIN SMALL LETTER J WITH CIRCUMFLEX
        chars.append(0x0136)  #Kcommaaccent	LATIN CAPITAL LETTER K WITH CEDILLA
        chars.append(0x0137)  #kcommaaccent	LATIN SMALL LETTER K WITH CEDILLA
        chars.append(0x0138)  #kgreenlandic	LATIN SMALL LETTER KRA
        chars.append(0x0139)  #Lacute	LATIN CAPITAL LETTER L WITH ACUTE
        chars.append(0x013A)  #lacute	LATIN SMALL LETTER L WITH ACUTE
        chars.append(0x013B)  #Lcommaaccent	LATIN CAPITAL LETTER L WITH CEDILLA
        chars.append(0x013C)  #lcommaaccent	LATIN SMALL LETTER L WITH CEDILLA
        chars.append(0x013D)  #Lcaron	LATIN CAPITAL LETTER L WITH CARON
        chars.append(0x013E)  #lcaron	LATIN SMALL LETTER L WITH CARON
        chars.append(0x013F)  #Ldot	LATIN CAPITAL LETTER L WITH MIDDLE DOT
        chars.append(0x0140)  #ldot	LATIN SMALL LETTER L WITH MIDDLE DOT
        chars.append(0x0141)  #Lslash	LATIN CAPITAL LETTER L WITH STROKE
        chars.append(0x0142)  #lslash	LATIN SMALL LETTER L WITH STROKE
        chars.append(0x0143)  #Nacute	LATIN CAPITAL LETTER N WITH ACUTE
        chars.append(0x0144)  #nacute	LATIN SMALL LETTER N WITH ACUTE
        chars.append(0x0145)  #Ncommaaccent	LATIN CAPITAL LETTER N WITH CEDILLA
        chars.append(0x0146)  #ncommaaccent	LATIN SMALL LETTER N WITH CEDILLA
        chars.append(0x0147)  #Ncaron	LATIN CAPITAL LETTER N WITH CARON
        chars.append(0x0148)  #ncaron	LATIN SMALL LETTER N WITH CARON
        chars.append(0x0149)  #napostrophe	LATIN SMALL LETTER N PRECEDED BY APOSTROPHE
        chars.append(0x014A)  #Eng	LATIN CAPITAL LETTER ENG
        chars.append(0x014B)  #eng	LATIN SMALL LETTER ENG
        chars.append(0x014C)  #Omacron	LATIN CAPITAL LETTER O WITH MACRON
        chars.append(0x014D)  #omacron	LATIN SMALL LETTER O WITH MACRON
        chars.append(0x014E)  #Obreve	LATIN CAPITAL LETTER O WITH BREVE
        chars.append(0x014F)  #obreve	LATIN SMALL LETTER O WITH BREVE
        chars.append(0x0150)  #Ohungarumlaut	LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
        chars.append(0x0151)  #ohungarumlaut	LATIN SMALL LETTER O WITH DOUBLE ACUTE
        chars.append(0x0152)  #OE	LATIN CAPITAL LIGATURE OE
        chars.append(0x0153)  #oe	LATIN SMALL LIGATURE OE
        chars.append(0x0154)  #Racute	LATIN CAPITAL LETTER R WITH ACUTE
        chars.append(0x0155)  #racute	LATIN SMALL LETTER R WITH ACUTE
        chars.append(0x0156)  #Rcommaaccent	LATIN CAPITAL LETTER R WITH CEDILLA
        chars.append(0x0157)  #rcommaaccent	LATIN SMALL LETTER R WITH CEDILLA
        chars.append(0x0158)  #Rcaron	LATIN CAPITAL LETTER R WITH CARON
        chars.append(0x0159)  #rcaron	LATIN SMALL LETTER R WITH CARON
        chars.append(0x015A)  #Sacute	LATIN CAPITAL LETTER S WITH ACUTE
        chars.append(0x015B)  #sacute	LATIN SMALL LETTER S WITH ACUTE
        chars.append(0x015C)  #Scircumflex	LATIN CAPITAL LETTER S WITH CIRCUMFLEX
        chars.append(0x015D)  #scircumflex	LATIN SMALL LETTER S WITH CIRCUMFLEX
        chars.append(0x015E)  #Scedilla	LATIN CAPITAL LETTER S WITH CEDILLA
        chars.append(0x015F)  #scedilla	LATIN SMALL LETTER S WITH CEDILLA
        chars.append(0x0160)  #Scaron	LATIN CAPITAL LETTER S WITH CARON
        chars.append(0x0161)  #scaron	LATIN SMALL LETTER S WITH CARON
        chars.append(0x0162)  #Tcommaaccent	LATIN CAPITAL LETTER T WITH CEDILLA
        chars.append(0x0163)  #tcommaaccent	LATIN SMALL LETTER T WITH CEDILLA
        chars.append(0x0164)  #Tcaron	LATIN CAPITAL LETTER T WITH CARON
        chars.append(0x0165)  #tcaron	LATIN SMALL LETTER T WITH CARON
        chars.append(0x0166)  #Tbar	LATIN CAPITAL LETTER T WITH STROKE
        chars.append(0x0167)  #tbar	LATIN SMALL LETTER T WITH STROKE
        chars.append(0x0168)  #Utilde	LATIN CAPITAL LETTER U WITH TILDE
        chars.append(0x0169)  #utilde	LATIN SMALL LETTER U WITH TILDE
        chars.append(0x016A)  #Umacron	LATIN CAPITAL LETTER U WITH MACRON
        chars.append(0x016B)  #umacron	LATIN SMALL LETTER U WITH MACRON
        chars.append(0x016C)  #Ubreve	LATIN CAPITAL LETTER U WITH BREVE
        chars.append(0x016D)  #ubreve	LATIN SMALL LETTER U WITH BREVE
        chars.append(0x016E)  #Uring	LATIN CAPITAL LETTER U WITH RING ABOVE
        chars.append(0x016F)  #uring	LATIN SMALL LETTER U WITH RING ABOVE
        chars.append(0x0170)  #Uhungarumlaut	LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
        chars.append(0x0171)  #uhungarumlaut	LATIN SMALL LETTER U WITH DOUBLE ACUTE
        chars.append(0x0172)  #Uogonek	LATIN CAPITAL LETTER U WITH OGONEK
        chars.append(0x0173)  #uogonek	LATIN SMALL LETTER U WITH OGONEK
        chars.append(0x0174)  #Wcircumflex	LATIN CAPITAL LETTER W WITH CIRCUMFLEX
        chars.append(0x0175)  #wcircumflex	LATIN SMALL LETTER W WITH CIRCUMFLEX
        chars.append(0x0176)  #Ycircumflex	LATIN CAPITAL LETTER Y WITH CIRCUMFLEX
        chars.append(0x0177)  #ycircumflex	LATIN SMALL LETTER Y WITH CIRCUMFLEX
        chars.append(0x0178)  #Ydieresis	LATIN CAPITAL LETTER Y WITH DIAERESIS
        chars.append(0x0179)  #Zacute	LATIN CAPITAL LETTER Z WITH ACUTE
        chars.append(0x017A)  #zacute	LATIN SMALL LETTER Z WITH ACUTE
        chars.append(0x017B)  #Zdotaccent	LATIN CAPITAL LETTER Z WITH DOT ABOVE
        chars.append(0x017C)  #zdotaccent	LATIN SMALL LETTER Z WITH DOT ABOVE
        chars.append(0x017D)  #Zcaron	LATIN CAPITAL LETTER Z WITH CARON
        chars.append(0x017E)  #zcaron	LATIN SMALL LETTER Z WITH CARON
        chars.append(0x017F)  #longs	LATIN SMALL LETTER LONG S
        chars.append(0x0180)  #uni0180	LATIN SMALL LETTER B WITH STROKE
        chars.append(0x0181)  #uni0181	LATIN CAPITAL LETTER B WITH HOOK
        chars.append(0x0182)  #uni0182	LATIN CAPITAL LETTER B WITH TOPBAR
        chars.append(0x0183)  #uni0183	LATIN SMALL LETTER B WITH TOPBAR
        chars.append(0x0184)  #uni0184	LATIN CAPITAL LETTER TONE SIX
        chars.append(0x0185)  #uni0185	LATIN SMALL LETTER TONE SIX
        chars.append(0x0186)  #uni0186	LATIN CAPITAL LETTER OPEN O
        chars.append(0x0187)  #uni0187	LATIN CAPITAL LETTER C WITH HOOK
        chars.append(0x0188)  #uni0188	LATIN SMALL LETTER C WITH HOOK
        chars.append(0x0189)  #uni0189	LATIN CAPITAL LETTER AFRICAN D
        chars.append(0x018A)  #uni018A	LATIN CAPITAL LETTER D WITH HOOK
        chars.append(0x018B)  #uni018B	LATIN CAPITAL LETTER D WITH TOPBAR
        chars.append(0x018C)  #uni018C	LATIN SMALL LETTER D WITH TOPBAR
        chars.append(0x018D)  #uni018D	LATIN SMALL LETTER TURNED DELTA
        chars.append(0x018E)  #uni018E	LATIN CAPITAL LETTER REVERSED E
        chars.append(0x018F)  #uni018F	LATIN CAPITAL LETTER SCHWA
        chars.append(0x0190)  #uni0190	LATIN CAPITAL LETTER OPEN E
        chars.append(0x0191)  #uni0191	LATIN CAPITAL LETTER F WITH HOOK
        chars.append(0x0192)  #florin	LATIN SMALL LETTER F WITH HOOK
        chars.append(0x0193)  #uni0193	LATIN CAPITAL LETTER G WITH HOOK
        chars.append(0x0194)  #uni0194	LATIN CAPITAL LETTER GAMMA
        chars.append(0x0195)  #uni0195	LATIN SMALL LETTER HV
        chars.append(0x0196)  #uni0196	LATIN CAPITAL LETTER IOTA
        chars.append(0x0197)  #uni0197	LATIN CAPITAL LETTER I WITH STROKE
        chars.append(0x0198)  #uni0198	LATIN CAPITAL LETTER K WITH HOOK
        chars.append(0x0199)  #uni0199	LATIN SMALL LETTER K WITH HOOK
        chars.append(0x019A)  #uni019A	LATIN SMALL LETTER L WITH BAR
        chars.append(0x019B)  #uni019B	LATIN SMALL LETTER LAMBDA WITH STROKE
        chars.append(0x019C)  #uni019C	LATIN CAPITAL LETTER TURNED M
        chars.append(0x019D)  #uni019D	LATIN CAPITAL LETTER N WITH LEFT HOOK
        chars.append(0x019E)  #uni019E	LATIN SMALL LETTER N WITH LONG RIGHT LEG
        chars.append(0x019F)  #uni019F	LATIN CAPITAL LETTER O WITH MIDDLE TILDE
        chars.append(0x01A0)  #Ohorn	LATIN CAPITAL LETTER O WITH HORN
        chars.append(0x01A1)  #ohorn	LATIN SMALL LETTER O WITH HORN
        chars.append(0x01A2)  #uni01A2	LATIN CAPITAL LETTER OI
        chars.append(0x01A3)  #uni01A3	LATIN SMALL LETTER OI
        chars.append(0x01A4)  #uni01A4	LATIN CAPITAL LETTER P WITH HOOK
        chars.append(0x01A5)  #uni01A5	LATIN SMALL LETTER P WITH HOOK
        chars.append(0x01A6)  #uni01A6	LATIN LETTER YR
        chars.append(0x01A7)  #uni01A7	LATIN CAPITAL LETTER TONE TWO
        chars.append(0x01A8)  #uni01A8	LATIN SMALL LETTER TONE TWO
        chars.append(0x01A9)  #uni01A9	LATIN CAPITAL LETTER ESH
        chars.append(0x01AA)  #uni01AA	LATIN LETTER REVERSED ESH LOOP
        chars.append(0x01AB)  #uni01AB	LATIN SMALL LETTER T WITH PALATAL HOOK
        chars.append(0x01AC)  #uni01AC	LATIN CAPITAL LETTER T WITH HOOK
        chars.append(0x01AD)  #uni01AD	LATIN SMALL LETTER T WITH HOOK
        chars.append(0x01AE)  #uni01AE	LATIN CAPITAL LETTER T WITH RETROFLEX HOOK
        chars.append(0x01AF)  #Uhorn	LATIN CAPITAL LETTER U WITH HORN
        chars.append(0x01B0)  #uhorn	LATIN SMALL LETTER U WITH HORN
        chars.append(0x01B1)  #uni01B1	LATIN CAPITAL LETTER UPSILON
        chars.append(0x01B2)  #uni01B2	LATIN CAPITAL LETTER V WITH HOOK
        chars.append(0x01B3)  #uni01B3	LATIN CAPITAL LETTER Y WITH HOOK
        chars.append(0x01B4)  #uni01B4	LATIN SMALL LETTER Y WITH HOOK
        chars.append(0x01B5)  #uni01B5	LATIN CAPITAL LETTER Z WITH STROKE
        chars.append(0x01B6)  #uni01B6	LATIN SMALL LETTER Z WITH STROKE
        chars.append(0x01B7)  #uni01B7	LATIN CAPITAL LETTER EZH
        chars.append(0x01B8)  #uni01B8	LATIN CAPITAL LETTER EZH REVERSED
        chars.append(0x01B9)  #uni01B9	LATIN SMALL LETTER EZH REVERSED
        chars.append(0x01BA)  #uni01BA	LATIN SMALL LETTER EZH WITH TAIL
        chars.append(0x01BB)  #uni01BB	LATIN LETTER TWO WITH STROKE
        chars.append(0x01BC)  #uni01BC	LATIN CAPITAL LETTER TONE FIVE
        chars.append(0x01BD)  #uni01BD	LATIN SMALL LETTER TONE FIVE
        chars.append(0x01BE)  #uni01BE	LATIN LETTER INVERTED GLOTTAL STOP WITH STROKE
        chars.append(0x01BF)  #uni01BF	LATIN LETTER WYNN
        chars.append(0x01C0)  #uni01C0	LATIN LETTER DENTAL CLICK
        chars.append(0x01C1)  #uni01C1	LATIN LETTER LATERAL CLICK
        chars.append(0x01C2)  #uni01C2	LATIN LETTER ALVEOLAR CLICK
        chars.append(0x01C3)  #uni01C3	LATIN LETTER RETROFLEX CLICK
        chars.append(0x01C4)  #uni01C4	LATIN CAPITAL LETTER DZ WITH CARON
        chars.append(0x01C5)  #uni01C5	LATIN CAPITAL LETTER D WITH SMALL LETTER Z WITH CARON
        chars.append(0x01C6)  #uni01C6	LATIN SMALL LETTER DZ WITH CARON
        chars.append(0x01C7)  #uni01C7	LATIN CAPITAL LETTER LJ
        chars.append(0x01C8)  #uni01C8	LATIN CAPITAL LETTER L WITH SMALL LETTER J
        chars.append(0x01C9)  #uni01C9	LATIN SMALL LETTER LJ
        chars.append(0x01CA)  #uni01CA	LATIN CAPITAL LETTER NJ
        chars.append(0x01CB)  #uni01CB	LATIN CAPITAL LETTER N WITH SMALL LETTER J
        chars.append(0x01CC)  #uni01CC	LATIN SMALL LETTER NJ
        chars.append(0x01CD)  #uni01CD	LATIN CAPITAL LETTER A WITH CARON
        chars.append(0x01CE)  #uni01CE	LATIN SMALL LETTER A WITH CARON
        chars.append(0x01CF)  #uni01CF	LATIN CAPITAL LETTER I WITH CARON
        chars.append(0x01D0)  #uni01D0	LATIN SMALL LETTER I WITH CARON
        chars.append(0x01D1)  #uni01D1	LATIN CAPITAL LETTER O WITH CARON
        chars.append(0x01D2)  #uni01D2	LATIN SMALL LETTER O WITH CARON
        chars.append(0x01D3)  #uni01D3	LATIN CAPITAL LETTER U WITH CARON
        chars.append(0x01D4)  #uni01D4	LATIN SMALL LETTER U WITH CARON
        chars.append(0x01D5)  #uni01D5	LATIN CAPITAL LETTER U WITH DIAERESIS AND MACRON
        chars.append(0x01D6)  #uni01D6	LATIN SMALL LETTER U WITH DIAERESIS AND MACRON
        chars.append(0x01D7)  #uni01D7	LATIN CAPITAL LETTER U WITH DIAERESIS AND ACUTE
        chars.append(0x01D8)  #uni01D8	LATIN SMALL LETTER U WITH DIAERESIS AND ACUTE
        chars.append(0x01D9)  #uni01D9	LATIN CAPITAL LETTER U WITH DIAERESIS AND CARON
        chars.append(0x01DA)  #uni01DA	LATIN SMALL LETTER U WITH DIAERESIS AND CARON
        chars.append(0x01DB)  #uni01DB	LATIN CAPITAL LETTER U WITH DIAERESIS AND GRAVE
        chars.append(0x01DC)  #uni01DC	LATIN SMALL LETTER U WITH DIAERESIS AND GRAVE
        chars.append(0x01DD)  #uni01DD	LATIN SMALL LETTER TURNED E
        chars.append(0x01DE)  #uni01DE	LATIN CAPITAL LETTER A WITH DIAERESIS AND MACRON
        chars.append(0x01DF)  #uni01DF	LATIN SMALL LETTER A WITH DIAERESIS AND MACRON
        chars.append(0x01E0)  #uni01E0	LATIN CAPITAL LETTER A WITH DOT ABOVE AND MACRON
        chars.append(0x01E1)  #uni01E1	LATIN SMALL LETTER A WITH DOT ABOVE AND MACRON
        chars.append(0x01E2)  #uni01E2	LATIN CAPITAL LETTER AE WITH MACRON
        chars.append(0x01E3)  #uni01E3	LATIN SMALL LETTER AE WITH MACRON
        chars.append(0x01E4)  #uni01E4	LATIN CAPITAL LETTER G WITH STROKE
        chars.append(0x01E5)  #uni01E5	LATIN SMALL LETTER G WITH STROKE
        chars.append(0x01E6)  #uni01E6	LATIN CAPITAL LETTER G WITH CARON
        chars.append(0x01E7)  #uni01E7	LATIN SMALL LETTER G WITH CARON
        chars.append(0x01E8)  #uni01E8	LATIN CAPITAL LETTER K WITH CARON
        chars.append(0x01E9)  #uni01E9	LATIN SMALL LETTER K WITH CARON
        chars.append(0x01EA)  #uni01EA	LATIN CAPITAL LETTER O WITH OGONEK
        chars.append(0x01EB)  #uni01EB	LATIN SMALL LETTER O WITH OGONEK
        chars.append(0x01EC)  #uni01EC	LATIN CAPITAL LETTER O WITH OGONEK AND MACRON
        chars.append(0x01ED)  #uni01ED	LATIN SMALL LETTER O WITH OGONEK AND MACRON
        chars.append(0x01EE)  #uni01EE	LATIN CAPITAL LETTER EZH WITH CARON
        chars.append(0x01EF)  #uni01EF	LATIN SMALL LETTER EZH WITH CARON
        chars.append(0x01F0)  #uni01F0	LATIN SMALL LETTER J WITH CARON
        chars.append(0x01F1)  #uni01F1	LATIN CAPITAL LETTER DZ
        chars.append(0x01F2)  #uni01F2	LATIN CAPITAL LETTER D WITH SMALL LETTER Z
        chars.append(0x01F3)  #uni01F3	LATIN SMALL LETTER DZ
        chars.append(0x01F4)  #uni01F4	LATIN CAPITAL LETTER G WITH ACUTE
        chars.append(0x01F5)  #uni01F5	LATIN SMALL LETTER G WITH ACUTE
        chars.append(0x01F6)  #uni01F6	LATIN CAPITAL LETTER HWAIR
        chars.append(0x01F7)  #uni01F7	LATIN CAPITAL LETTER WYNN
        chars.append(0x01F8)  #uni01F8	LATIN CAPITAL LETTER N WITH GRAVE
        chars.append(0x01F9)  #uni01F9	LATIN SMALL LETTER N WITH GRAVE
        chars.append(0x01FA)  #Aringacute	LATIN CAPITAL LETTER A WITH RING ABOVE AND ACUTE
        chars.append(0x01FB)  #aringacute	LATIN SMALL LETTER A WITH RING ABOVE AND ACUTE
        chars.append(0x01FC)  #AEacute	LATIN CAPITAL LETTER AE WITH ACUTE
        chars.append(0x01FD)  #aeacute	LATIN SMALL LETTER AE WITH ACUTE
        chars.append(0x01FE)  #Oslashacute	LATIN CAPITAL LETTER O WITH STROKE AND ACUTE
        chars.append(0x01FF)  #oslashacute	LATIN SMALL LETTER O WITH STROKE AND ACUTE
        chars.append(0x0200)  #uni0200	LATIN CAPITAL LETTER A WITH DOUBLE GRAVE
        chars.append(0x0201)  #uni0201	LATIN SMALL LETTER A WITH DOUBLE GRAVE
        chars.append(0x0202)  #uni0202	LATIN CAPITAL LETTER A WITH INVERTED BREVE
        chars.append(0x0203)  #uni0203	LATIN SMALL LETTER A WITH INVERTED BREVE
        chars.append(0x0204)  #uni0204	LATIN CAPITAL LETTER E WITH DOUBLE GRAVE
        chars.append(0x0205)  #uni0205	LATIN SMALL LETTER E WITH DOUBLE GRAVE
        chars.append(0x0206)  #uni0206	LATIN CAPITAL LETTER E WITH INVERTED BREVE
        chars.append(0x0207)  #uni0207	LATIN SMALL LETTER E WITH INVERTED BREVE
        chars.append(0x0208)  #uni0208	LATIN CAPITAL LETTER I WITH DOUBLE GRAVE
        chars.append(0x0209)  #uni0209	LATIN SMALL LETTER I WITH DOUBLE GRAVE
        chars.append(0x020A)  #uni020A	LATIN CAPITAL LETTER I WITH INVERTED BREVE
        chars.append(0x020B)  #uni020B	LATIN SMALL LETTER I WITH INVERTED BREVE
        chars.append(0x020C)  #uni020C	LATIN CAPITAL LETTER O WITH DOUBLE GRAVE
        chars.append(0x020D)  #uni020D	LATIN SMALL LETTER O WITH DOUBLE GRAVE
        chars.append(0x020E)  #uni020E	LATIN CAPITAL LETTER O WITH INVERTED BREVE
        chars.append(0x020F)  #uni020F	LATIN SMALL LETTER O WITH INVERTED BREVE
        chars.append(0x0210)  #uni0210	LATIN CAPITAL LETTER R WITH DOUBLE GRAVE
        chars.append(0x0211)  #uni0211	LATIN SMALL LETTER R WITH DOUBLE GRAVE
        chars.append(0x0212)  #uni0212	LATIN CAPITAL LETTER R WITH INVERTED BREVE
        chars.append(0x0213)  #uni0213	LATIN SMALL LETTER R WITH INVERTED BREVE
        chars.append(0x0214)  #uni0214	LATIN CAPITAL LETTER U WITH DOUBLE GRAVE
        chars.append(0x0215)  #uni0215	LATIN SMALL LETTER U WITH DOUBLE GRAVE
        chars.append(0x0216)  #uni0216	LATIN CAPITAL LETTER U WITH INVERTED BREVE
        chars.append(0x0217)  #uni0217	LATIN SMALL LETTER U WITH INVERTED BREVE
        chars.append(0x0218)  #Scommaaccent	LATIN CAPITAL LETTER S WITH COMMA BELOW
        chars.append(0x0219)  #scommaaccent	LATIN SMALL LETTER S WITH COMMA BELOW
        chars.append(0x021A)  #uni021A	LATIN CAPITAL LETTER T WITH COMMA BELOW
        chars.append(0x021B)  #uni021B	LATIN SMALL LETTER T WITH COMMA BELOW
        chars.append(0x021C)  #uni021C	LATIN CAPITAL LETTER YOGH
        chars.append(0x021D)  #uni021D	LATIN SMALL LETTER YOGH
        chars.append(0x021E)  #uni021E	LATIN CAPITAL LETTER H WITH CARON
        chars.append(0x021F)  #uni021F	LATIN SMALL LETTER H WITH CARON
        chars.append(0x0220)  #uni0220	LATIN CAPITAL LETTER N WITH LONG RIGHT LEG
        chars.append(0x0221)  #uni0221	LATIN SMALL LETTER D WITH CURL
        chars.append(0x0222)  #uni0222	LATIN CAPITAL LETTER OU
        chars.append(0x0223)  #uni0223	LATIN SMALL LETTER OU
        chars.append(0x0224)  #uni0224	LATIN CAPITAL LETTER Z WITH HOOK
        chars.append(0x0225)  #uni0225	LATIN SMALL LETTER Z WITH HOOK
        chars.append(0x0226)  #uni0226	LATIN CAPITAL LETTER A WITH DOT ABOVE
        chars.append(0x0227)  #uni0227	LATIN SMALL LETTER A WITH DOT ABOVE
        chars.append(0x0228)  #uni0228	LATIN CAPITAL LETTER E WITH CEDILLA
        chars.append(0x0229)  #uni0229	LATIN SMALL LETTER E WITH CEDILLA
        chars.append(0x022A)  #uni022A	LATIN CAPITAL LETTER O WITH DIAERESIS AND MACRON
        chars.append(0x022B)  #uni022B	LATIN SMALL LETTER O WITH DIAERESIS AND MACRON
        chars.append(0x022C)  #uni022C	LATIN CAPITAL LETTER O WITH TILDE AND MACRON
        chars.append(0x022D)  #uni022D	LATIN SMALL LETTER O WITH TILDE AND MACRON
        chars.append(0x022E)  #uni022E	LATIN CAPITAL LETTER O WITH DOT ABOVE
        chars.append(0x022F)  #uni022F	LATIN SMALL LETTER O WITH DOT ABOVE
        chars.append(0x0230)  #uni0230	LATIN CAPITAL LETTER O WITH DOT ABOVE AND MACRON
        chars.append(0x0231)  #uni0231	LATIN SMALL LETTER O WITH DOT ABOVE AND MACRON
        chars.append(0x0232)  #uni0232	LATIN CAPITAL LETTER Y WITH MACRON
        chars.append(0x0233)  #uni0233	LATIN SMALL LETTER Y WITH MACRON
        chars.append(0x0234)  #uni0234	LATIN SMALL LETTER L WITH CURL
        chars.append(0x0235)  #uni0235	LATIN SMALL LETTER N WITH CURL
        chars.append(0x0236)  #uni0236	LATIN SMALL LETTER T WITH CURL
        chars.append(0x0237)  #j.dotless	LATIN SMALL LETTER DOTLESS J
        chars.append(0x0238)  #uni0238	LATIN SMALL LETTER DB DIGRAPH
        chars.append(0x0239)  #uni0239	LATIN SMALL LETTER QP DIGRAPH
        chars.append(0x023A)  #uni023A	LATIN CAPITAL LETTER A WITH STROKE
        chars.append(0x023B)  #uni023B	LATIN CAPITAL LETTER C WITH STROKE
        chars.append(0x023C)  #uni023C	LATIN SMALL LETTER C WITH STROKE
        chars.append(0x023D)  #uni023D	LATIN CAPITAL LETTER L WITH BAR
        chars.append(0x023E)  #uni023E	LATIN CAPITAL LETTER T WITH DIAGONAL STROKE
        chars.append(0x023F)  #uni023F	LATIN SMALL LETTER S WITH SWASH TAIL
        chars.append(0x0240)  #uni0240	LATIN SMALL LETTER Z WITH SWASH TAIL
        chars.append(0x0241)  #uni0241	LATIN CAPITAL LETTER GLOTTAL STOP
        chars.append(0x0242)  #uni0242	LATIN SMALL LETTER GLOTTAL STOP
        chars.append(0x0243)  #uni0243	LATIN CAPITAL LETTER B WITH STROKE
        chars.append(0x0244)  #uni0244	LATIN CAPITAL LETTER U BAR
        chars.append(0x0245)  #uni0245	LATIN CAPITAL LETTER TURNED V
        chars.append(0x0246)  #uni0246	LATIN CAPITAL LETTER E WITH STROKE
        chars.append(0x0247)  #uni0247	LATIN SMALL LETTER E WITH STROKE
        chars.append(0x0248)  #uni0248	LATIN CAPITAL LETTER J WITH STROKE
        chars.append(0x0249)  #uni0249	LATIN SMALL LETTER J WITH STROKE
        chars.append(0x024A)  #uni024A	LATIN CAPITAL LETTER SMALL Q WITH HOOK TAIL
        chars.append(0x024B)  #uni024B	LATIN SMALL LETTER Q WITH HOOK TAIL
        chars.append(0x024C)  #uni024C	LATIN CAPITAL LETTER R WITH STROKE
        chars.append(0x024D)  #uni024D	LATIN SMALL LETTER R WITH STROKE
        chars.append(0x024E)  #uni024E	LATIN CAPITAL LETTER Y WITH STROKE
        chars.append(0x024F)  #uni024F	LATIN SMALL LETTER Y WITH STROKE
        chars.append(0x0250)  #uni0250	LATIN SMALL LETTER TURNED A
        chars.append(0x0251)  #uni0251	LATIN SMALL LETTER ALPHA
        chars.append(0x0252)  #uni0252	LATIN SMALL LETTER TURNED ALPHA
        chars.append(0x0253)  #uni0253	LATIN SMALL LETTER B WITH HOOK
        chars.append(0x0254)  #uni0254	LATIN SMALL LETTER OPEN O
        chars.append(0x0255)  #uni0255	LATIN SMALL LETTER C WITH CURL
        chars.append(0x0256)  #uni0256	LATIN SMALL LETTER D WITH TAIL
        chars.append(0x0257)  #uni0257	LATIN SMALL LETTER D WITH HOOK
        chars.append(0x0258)  #uni0258	LATIN SMALL LETTER REVERSED E
        chars.append(0x0259)  #uni0259	LATIN SMALL LETTER SCHWA
        chars.append(0x025A)  #uni025A	LATIN SMALL LETTER SCHWA WITH HOOK
        chars.append(0x025B)  #uni025B	LATIN SMALL LETTER OPEN E
        chars.append(0x025C)  #uni025C	LATIN SMALL LETTER REVERSED OPEN E
        chars.append(0x025D)  #uni025D	LATIN SMALL LETTER REVERSED OPEN E WITH HOOK
        chars.append(0x025E)  #uni025E	LATIN SMALL LETTER CLOSED REVERSED OPEN E
        chars.append(0x025F)  #uni025F	LATIN SMALL LETTER DOTLESS J WITH STROKE
        chars.append(0x0260)  #uni0260	LATIN SMALL LETTER G WITH HOOK
        chars.append(0x0261)  #uni0261	LATIN SMALL LETTER SCRIPT G
        chars.append(0x0262)  #uni0262	LATIN LETTER SMALL CAPITAL G
        chars.append(0x0263)  #uni0263	LATIN SMALL LETTER GAMMA
        chars.append(0x0264)  #uni0264	LATIN SMALL LETTER RAMS HORN
        chars.append(0x0265)  #uni0265	LATIN SMALL LETTER TURNED H
        chars.append(0x0266)  #uni0266	LATIN SMALL LETTER H WITH HOOK
        chars.append(0x0267)  #uni0267	LATIN SMALL LETTER HENG WITH HOOK
        chars.append(0x0268)  #uni0268	LATIN SMALL LETTER I WITH STROKE
        chars.append(0x0269)  #uni0269	LATIN SMALL LETTER IOTA
        chars.append(0x026A)  #uni026A	LATIN LETTER SMALL CAPITAL I
        chars.append(0x026B)  #uni026B	LATIN SMALL LETTER L WITH MIDDLE TILDE
        chars.append(0x026C)  #uni026C	LATIN SMALL LETTER L WITH BELT
        chars.append(0x026D)  #uni026D	LATIN SMALL LETTER L WITH RETROFLEX HOOK
        chars.append(0x026E)  #uni026E	LATIN SMALL LETTER LEZH
        chars.append(0x026F)  #uni026F	LATIN SMALL LETTER TURNED M
        chars.append(0x0270)  #uni0270	LATIN SMALL LETTER TURNED M WITH LONG LEG
        chars.append(0x0271)  #uni0271	LATIN SMALL LETTER M WITH HOOK
        chars.append(0x0272)  #uni0272	LATIN SMALL LETTER N WITH LEFT HOOK
        chars.append(0x0273)  #uni0273	LATIN SMALL LETTER N WITH RETROFLEX HOOK
        chars.append(0x0274)  #uni0274	LATIN LETTER SMALL CAPITAL N
        chars.append(0x0275)  #uni0275	LATIN SMALL LETTER BARRED O
        chars.append(0x0276)  #uni0276	LATIN LETTER SMALL CAPITAL OE
        chars.append(0x0277)  #uni0277	LATIN SMALL LETTER CLOSED OMEGA
        chars.append(0x0278)  #uni0278	LATIN SMALL LETTER PHI
        chars.append(0x0279)  #uni0279	LATIN SMALL LETTER TURNED R
        chars.append(0x027A)  #uni027A	LATIN SMALL LETTER TURNED R WITH LONG LEG
        chars.append(0x027B)  #uni027B	LATIN SMALL LETTER TURNED R WITH HOOK
        chars.append(0x027C)  #uni027C	LATIN SMALL LETTER R WITH LONG LEG
        chars.append(0x027D)  #uni027D	LATIN SMALL LETTER R WITH TAIL
        chars.append(0x027E)  #uni027E	LATIN SMALL LETTER R WITH FISHHOOK
        chars.append(0x027F)  #uni027F	LATIN SMALL LETTER REVERSED R WITH FISHHOOK
        chars.append(0x0280)  #uni0280	LATIN LETTER SMALL CAPITAL R
        chars.append(0x0281)  #uni0281	LATIN LETTER SMALL CAPITAL INVERTED R
        chars.append(0x0282)  #uni0282	LATIN SMALL LETTER S WITH HOOK
        chars.append(0x0283)  #uni0283	LATIN SMALL LETTER ESH
        chars.append(0x0284)  #uni0284	LATIN SMALL LETTER DOTLESS J WITH STROKE AND HOOK
        chars.append(0x0285)  #uni0285	LATIN SMALL LETTER SQUAT REVERSED ESH
        chars.append(0x0286)  #uni0286	LATIN SMALL LETTER ESH WITH CURL
        chars.append(0x0287)  #uni0287	LATIN SMALL LETTER TURNED T
        chars.append(0x0288)  #uni0288	LATIN SMALL LETTER T WITH RETROFLEX HOOK
        chars.append(0x0289)  #uni0289	LATIN SMALL LETTER U BAR
        chars.append(0x028A)  #uni028A	LATIN SMALL LETTER UPSILON
        chars.append(0x028B)  #uni028B	LATIN SMALL LETTER V WITH HOOK
        chars.append(0x028C)  #uni028C	LATIN SMALL LETTER TURNED V
        chars.append(0x028D)  #uni028D	LATIN SMALL LETTER TURNED W
        chars.append(0x028E)  #uni028E	LATIN SMALL LETTER TURNED Y
        chars.append(0x028F)  #uni028F	LATIN LETTER SMALL CAPITAL Y
        chars.append(0x0290)  #uni0290	LATIN SMALL LETTER Z WITH RETROFLEX HOOK
        chars.append(0x0291)  #uni0291	LATIN SMALL LETTER Z WITH CURL
        chars.append(0x0292)  #uni0292	LATIN SMALL LETTER EZH
        chars.append(0x0293)  #uni0293	LATIN SMALL LETTER EZH WITH CURL
        chars.append(0x0294)  #uni0294	LATIN LETTER GLOTTAL STOP
        chars.append(0x0295)  #uni0295	LATIN LETTER PHARYNGEAL VOICED FRICATIVE
        chars.append(0x0296)  #uni0296	LATIN LETTER INVERTED GLOTTAL STOP
        chars.append(0x0297)  #uni0297	LATIN LETTER STRETCHED C
        chars.append(0x0298)  #uni0298	LATIN LETTER BILABIAL CLICK
        chars.append(0x0299)  #uni0299	LATIN LETTER SMALL CAPITAL B
        chars.append(0x029A)  #uni029A	LATIN SMALL LETTER CLOSED OPEN E
        chars.append(0x029B)  #uni029B	LATIN LETTER SMALL CAPITAL G WITH HOOK
        chars.append(0x029C)  #uni029C	LATIN LETTER SMALL CAPITAL H
        chars.append(0x029D)  #uni029D	LATIN SMALL LETTER J WITH CROSSED-TAIL
        chars.append(0x029E)  #uni029E	LATIN SMALL LETTER TURNED K
        chars.append(0x029F)  #uni029F	LATIN LETTER SMALL CAPITAL L
        chars.append(0x02A0)  #uni02A0	LATIN SMALL LETTER Q WITH HOOK
        chars.append(0x02A1)  #uni02A1	LATIN LETTER GLOTTAL STOP WITH STROKE
        chars.append(0x02A2)  #uni02A2	LATIN LETTER REVERSED GLOTTAL STOP WITH STROKE
        chars.append(0x02A3)  #uni02A3	LATIN SMALL LETTER DZ DIGRAPH
        chars.append(0x02A4)  #uni02A4	LATIN SMALL LETTER DEZH DIGRAPH
        chars.append(0x02A5)  #uni02A5	LATIN SMALL LETTER DZ DIGRAPH WITH CURL
        chars.append(0x02A6)  #uni02A6	LATIN SMALL LETTER TS DIGRAPH
        chars.append(0x02A7)  #uni02A7	LATIN SMALL LETTER TESH DIGRAPH
        chars.append(0x02A8)  #uni02A8	LATIN SMALL LETTER TC DIGRAPH WITH CURL
        chars.append(0x02A9)  #uni02A9	LATIN SMALL LETTER FENG DIGRAPH
        chars.append(0x02AA)  #uni02AA	LATIN SMALL LETTER LS DIGRAPH
        chars.append(0x02AB)  #uni02AB	LATIN SMALL LETTER LZ DIGRAPH
        chars.append(0x02AC)  #uni02AC	LATIN LETTER BILABIAL PERCUSSIVE
        chars.append(0x02AD)  #uni02AD	LATIN LETTER BIDENTAL PERCUSSIVE
        chars.append(0x02AE)  #uni02AE	LATIN SMALL LETTER TURNED H WITH FISHHOOK
        chars.append(0x02AF)  #uni02AF	LATIN SMALL LETTER TURNED H WITH FISHHOOK AND TAIL
        chars.append(0x02B0)  #uni02B0	MODIFIER LETTER SMALL H
        chars.append(0x02B1)  #uni02B1	MODIFIER LETTER SMALL H WITH HOOK
        chars.append(0x02B2)  #uni02B2	MODIFIER LETTER SMALL J
        chars.append(0x02B3)  #uni02B3	MODIFIER LETTER SMALL R
        chars.append(0x02B4)  #uni02B4	MODIFIER LETTER SMALL TURNED R
        chars.append(0x02B5)  #uni02B5	MODIFIER LETTER SMALL TURNED R WITH HOOK
        chars.append(0x02B6)  #uni02B6	MODIFIER LETTER SMALL CAPITAL INVERTED R
        chars.append(0x02B7)  #uni02B7	MODIFIER LETTER SMALL W
        chars.append(0x02B8)  #uni02B8	MODIFIER LETTER SMALL Y
        chars.append(0x02B9)  #uni02B9	MODIFIER LETTER PRIME
        chars.append(0x02BA)  #uni02BA	MODIFIER LETTER DOUBLE PRIME
        chars.append(0x02BB)  #uni02BB	MODIFIER LETTER TURNED COMMA
        chars.append(0x02BC)  #uni02BC	MODIFIER LETTER APOSTROPHE
        chars.append(0x02BD)  #uni02BD	MODIFIER LETTER REVERSED COMMA
        chars.append(0x02BE)  #uni02BE	MODIFIER LETTER RIGHT HALF RING
        chars.append(0x02BF)  #uni02BF	MODIFIER LETTER LEFT HALF RING
        chars.append(0x02C0)  #uni02C0	MODIFIER LETTER GLOTTAL STOP
        chars.append(0x02C1)  #uni02C1	MODIFIER LETTER REVERSED GLOTTAL STOP
        chars.append(0x02C2)  #uni02C2	MODIFIER LETTER LEFT ARROWHEAD
        chars.append(0x02C3)  #uni02C3	MODIFIER LETTER RIGHT ARROWHEAD
        chars.append(0x02C4)  #uni02C4	MODIFIER LETTER UP ARROWHEAD
        chars.append(0x02C5)  #uni02C5	MODIFIER LETTER DOWN ARROWHEAD
        chars.append(0x02C6)  #circumflex	MODIFIER LETTER CIRCUMFLEX ACCENT
        chars.append(0x02C7)  #caron	CARON
        chars.append(0x02C8)  #uni02C8	MODIFIER LETTER VERTICAL LINE
        chars.append(0x02C9)  #macron	MODIFIER LETTER MACRON
        chars.append(0x02CA)  #uni02CA	MODIFIER LETTER ACUTE ACCENT
        chars.append(0x02CB)  #uni02CB	MODIFIER LETTER GRAVE ACCENT
        chars.append(0x02CC)  #uni02CC	MODIFIER LETTER LOW VERTICAL LINE
        chars.append(0x02CD)  #uni02CD	MODIFIER LETTER LOW MACRON
        chars.append(0x02CE)  #uni02CE	MODIFIER LETTER LOW GRAVE ACCENT
        chars.append(0x02CF)  #uni02CF	MODIFIER LETTER LOW ACUTE ACCENT
        chars.append(0x02D0)  #uni02D0	MODIFIER LETTER TRIANGULAR COLON
        chars.append(0x02D1)  #uni02D1	MODIFIER LETTER HALF TRIANGULAR COLON
        chars.append(0x02D2)  #uni02D2	MODIFIER LETTER CENTRED RIGHT HALF RING
        chars.append(0x02D3)  #uni02D3	MODIFIER LETTER CENTRED LEFT HALF RING
        chars.append(0x02D4)  #uni02D4	MODIFIER LETTER UP TACK
        chars.append(0x02D5)  #uni02D5	MODIFIER LETTER DOWN TACK
        chars.append(0x02D6)  #uni02D6	MODIFIER LETTER PLUS SIGN
        chars.append(0x02D7)  #uni02D7	MODIFIER LETTER MINUS SIGN
        chars.append(0x02D8)  #breve	BREVE
        chars.append(0x02D9)  #dotaccent	DOT ABOVE
        chars.append(0x02DA)  #ring	RING ABOVE
        chars.append(0x02DB)  #ogonek	OGONEK
        chars.append(0x02DC)  #tilde	SMALL TILDE
        chars.append(0x02DD)  #hungarumlaut	DOUBLE ACUTE ACCENT
        chars.append(0x02DE)  #uni02DE	MODIFIER LETTER RHOTIC HOOK
        chars.append(0x02DF)  #uni02DF	MODIFIER LETTER CROSS ACCENT
        chars.append(0x02E0)  #uni02E0	MODIFIER LETTER SMALL GAMMA
        chars.append(0x02E1)  #uni02E1	MODIFIER LETTER SMALL L
        chars.append(0x02E2)  #uni02E2	MODIFIER LETTER SMALL S
        chars.append(0x02E3)  #uni02E3	MODIFIER LETTER SMALL X
        chars.append(0x02E4)  #uni02E4	MODIFIER LETTER SMALL REVERSED GLOTTAL STOP
        chars.append(0x02E5)  #uni02E5	MODIFIER LETTER EXTRA-HIGH TONE BAR
        chars.append(0x02E6)  #uni02E6	MODIFIER LETTER HIGH TONE BAR
        chars.append(0x02E7)  #uni02E7	MODIFIER LETTER MID TONE BAR
        chars.append(0x02E8)  #uni02E8	MODIFIER LETTER LOW TONE BAR
        chars.append(0x02E9)  #uni02E9	MODIFIER LETTER EXTRA-LOW TONE BAR
        chars.append(0x02EA)  #uni02EA	MODIFIER LETTER YIN DEPARTING TONE MARK
        chars.append(0x02EB)  #uni02EB	MODIFIER LETTER YANG DEPARTING TONE MARK
        chars.append(0x02EC)  #uni02EC	MODIFIER LETTER VOICING
        chars.append(0x02ED)  #uni02ED	MODIFIER LETTER UNASPIRATED
        chars.append(0x02EE)  #uni02EE	MODIFIER LETTER DOUBLE APOSTROPHE
        chars.append(0x02EF)  #uni02EF	MODIFIER LETTER LOW DOWN ARROWHEAD
        chars.append(0x02F0)  #uni02F0	MODIFIER LETTER LOW UP ARROWHEAD
        chars.append(0x02F1)  #uni02F1	MODIFIER LETTER LOW LEFT ARROWHEAD
        chars.append(0x02F2)  #uni02F2	MODIFIER LETTER LOW RIGHT ARROWHEAD
        chars.append(0x02F3)  #uni02F3	MODIFIER LETTER LOW RING
        chars.append(0x02F4)  #uni02F4	MODIFIER LETTER MIDDLE GRAVE ACCENT
        chars.append(0x02F5)  #uni02F5	MODIFIER LETTER MIDDLE DOUBLE GRAVE ACCENT
        chars.append(0x02F6)  #uni02F6	MODIFIER LETTER MIDDLE DOUBLE ACUTE ACCENT
        chars.append(0x02F7)  #uni02F7	MODIFIER LETTER LOW TILDE
        chars.append(0x02F8)  #uni02F8	MODIFIER LETTER RAISED COLON
        chars.append(0x02F9)  #uni02F9	MODIFIER LETTER BEGIN HIGH TONE
        chars.append(0x02FA)  #uni02FA	MODIFIER LETTER END HIGH TONE
        chars.append(0x02FB)  #uni02FB	MODIFIER LETTER BEGIN LOW TONE
        chars.append(0x02FC)  #uni02FC	MODIFIER LETTER END LOW TONE
        chars.append(0x02FD)  #uni02FD	MODIFIER LETTER SHELF
        chars.append(0x02FE)  #uni02FE	MODIFIER LETTER OPEN SHELF
        chars.append(0x02FF)  #uni02FF	MODIFIER LETTER LOW LEFT ARROW
        chars.append(0x0300)  #gravecomb	COMBINING GRAVE ACCENT
        chars.append(0x0301)  #acutecomb	COMBINING ACUTE ACCENT
        chars.append(0x0302)  #uni0302	COMBINING CIRCUMFLEX ACCENT
        chars.append(0x0303)  #tildecomb	COMBINING TILDE
        chars.append(0x0304)  #uni0304	COMBINING MACRON
        chars.append(0x0305)  #uni0305	COMBINING OVERLINE
        chars.append(0x0306)  #uni0306	COMBINING BREVE
        chars.append(0x0307)  #uni0307	COMBINING DOT ABOVE
        chars.append(0x0308)  #uni0308	COMBINING DIAERESIS
        chars.append(0x0309)  #hookabovecomb	COMBINING HOOK ABOVE
        chars.append(0x030A)  #uni030A	COMBINING RING ABOVE
        chars.append(0x030B)  #uni030B	COMBINING DOUBLE ACUTE ACCENT
        chars.append(0x030C)  #uni030C	COMBINING CARON
        chars.append(0x030D)  #uni030D	COMBINING VERTICAL LINE ABOVE
        chars.append(0x030E)  #uni030E	COMBINING DOUBLE VERTICAL LINE ABOVE
        chars.append(0x030F)  #uni030F	COMBINING DOUBLE GRAVE ACCENT
        chars.append(0x0310)  #uni0310	COMBINING CANDRABINDU
        chars.append(0x0311)  #uni0311	COMBINING INVERTED BREVE
        chars.append(0x0312)  #uni0312	COMBINING TURNED COMMA ABOVE
        chars.append(0x0313)  #uni0313	COMBINING COMMA ABOVE
        chars.append(0x0314)  #uni0314	COMBINING REVERSED COMMA ABOVE
        chars.append(0x0315)  #uni0315	COMBINING COMMA ABOVE RIGHT
        chars.append(0x0316)  #uni0316	COMBINING GRAVE ACCENT BELOW
        chars.append(0x0317)  #uni0317	COMBINING ACUTE ACCENT BELOW
        chars.append(0x0318)  #uni0318	COMBINING LEFT TACK BELOW
        chars.append(0x0319)  #uni0319	COMBINING RIGHT TACK BELOW
        chars.append(0x031A)  #uni031A	COMBINING LEFT ANGLE ABOVE
        chars.append(0x031B)  #uni031B	COMBINING HORN
        chars.append(0x031C)  #uni031C	COMBINING LEFT HALF RING BELOW
        chars.append(0x031D)  #uni031D	COMBINING UP TACK BELOW
        chars.append(0x031E)  #uni031E	COMBINING DOWN TACK BELOW
        chars.append(0x031F)  #uni031F	COMBINING PLUS SIGN BELOW
        chars.append(0x0320)  #uni0320	COMBINING MINUS SIGN BELOW
        chars.append(0x0321)  #uni0321	COMBINING PALATALIZED HOOK BELOW
        chars.append(0x0322)  #uni0322	COMBINING RETROFLEX HOOK BELOW
        chars.append(0x0323)  #dotbelowcomb	COMBINING DOT BELOW
        chars.append(0x0324)  #uni0324	COMBINING DIAERESIS BELOW
        chars.append(0x0325)  #uni0325	COMBINING RING BELOW
        chars.append(0x0326)  #uni0326	COMBINING COMMA BELOW
        chars.append(0x0327)  #uni0327	COMBINING CEDILLA
        chars.append(0x0328)  #uni0328	COMBINING OGONEK
        chars.append(0x0329)  #uni0329	COMBINING VERTICAL LINE BELOW
        chars.append(0x032A)  #uni032A	COMBINING BRIDGE BELOW
        chars.append(0x032B)  #uni032B	COMBINING INVERTED DOUBLE ARCH BELOW
        chars.append(0x032C)  #uni032C	COMBINING CARON BELOW
        chars.append(0x032D)  #uni032D	COMBINING CIRCUMFLEX ACCENT BELOW
        chars.append(0x032E)  #uni032E	COMBINING BREVE BELOW
        chars.append(0x032F)  #uni032F	COMBINING INVERTED BREVE BELOW
        chars.append(0x0330)  #uni0330	COMBINING TILDE BELOW
        chars.append(0x0331)  #uni0331	COMBINING MACRON BELOW
        chars.append(0x0332)  #uni0332	COMBINING LOW LINE
        chars.append(0x0333)  #uni0333	COMBINING DOUBLE LOW LINE
        chars.append(0x0334)  #uni0334	COMBINING TILDE OVERLAY
        chars.append(0x0335)  #uni0335	COMBINING SHORT STROKE OVERLAY
        chars.append(0x0336)  #uni0336	COMBINING LONG STROKE OVERLAY
        chars.append(0x0337)  #uni0337	COMBINING SHORT SOLIDUS OVERLAY
        chars.append(0x0338)  #uni0338	COMBINING LONG SOLIDUS OVERLAY
        chars.append(0x0339)  #uni0339	COMBINING RIGHT HALF RING BELOW
        chars.append(0x033A)  #uni033A	COMBINING INVERTED BRIDGE BELOW
        chars.append(0x033B)  #uni033B	COMBINING SQUARE BELOW
        chars.append(0x033C)  #uni033C	COMBINING SEAGULL BELOW
        chars.append(0x033D)  #uni033D	COMBINING X ABOVE
        chars.append(0x033E)  #uni033E	COMBINING VERTICAL TILDE
        chars.append(0x033F)  #uni033F	COMBINING DOUBLE OVERLINE
        chars.append(0x0340)  #uni0340	COMBINING GRAVE TONE MARK
        chars.append(0x0341)  #uni0341	COMBINING ACUTE TONE MARK
        chars.append(0x0342)  #uni0342	COMBINING GREEK PERISPOMENI
        chars.append(0x0343)  #uni0343	COMBINING GREEK KORONIS
        chars.append(0x0344)  #uni0344	COMBINING GREEK DIALYTIKA TONOS
        chars.append(0x0345)  #uni0345	COMBINING GREEK YPOGEGRAMMENI
        chars.append(0x0346)  #uni0346	COMBINING BRIDGE ABOVE
        chars.append(0x0347)  #uni0347	COMBINING EQUALS SIGN BELOW
        chars.append(0x0348)  #uni0348	COMBINING DOUBLE VERTICAL LINE BELOW
        chars.append(0x0349)  #uni0349	COMBINING LEFT ANGLE BELOW
        chars.append(0x034A)  #uni034A	COMBINING NOT TILDE ABOVE
        chars.append(0x034B)  #uni034B	COMBINING HOMOTHETIC ABOVE
        chars.append(0x034C)  #uni034C	COMBINING ALMOST EQUAL TO ABOVE
        chars.append(0x034D)  #uni034D	COMBINING LEFT RIGHT ARROW BELOW
        chars.append(0x034E)  #uni034E	COMBINING UPWARDS ARROW BELOW
        chars.append(0x034F)  #uni034F	COMBINING GRAPHEME JOINER
        chars.append(0x0350)  #uni0350	COMBINING RIGHT ARROWHEAD ABOVE
        chars.append(0x0351)  #uni0351	COMBINING LEFT HALF RING ABOVE
        chars.append(0x0352)  #uni0352	COMBINING FERMATA
        chars.append(0x0353)  #uni0353	COMBINING X BELOW
        chars.append(0x0354)  #uni0354	COMBINING LEFT ARROWHEAD BELOW
        chars.append(0x0355)  #uni0355	COMBINING RIGHT ARROWHEAD BELOW
        chars.append(0x0356)  #uni0356	COMBINING RIGHT ARROWHEAD AND UP ARROWHEAD BELOW
        chars.append(0x0357)  #uni0357	COMBINING RIGHT HALF RING ABOVE
        chars.append(0x0358)  #uni0358	COMBINING DOT ABOVE RIGHT
        chars.append(0x0359)  #uni0359	COMBINING ASTERISK BELOW
        chars.append(0x035A)  #uni035A	COMBINING DOUBLE RING BELOW
        chars.append(0x035B)  #uni035B	COMBINING ZIGZAG ABOVE
        chars.append(0x035C)  #uni035C	COMBINING DOUBLE BREVE BELOW
        chars.append(0x035D)  #uni035D	COMBINING DOUBLE BREVE
        chars.append(0x035E)  #uni035E	COMBINING DOUBLE MACRON
        chars.append(0x035F)  #uni035F	COMBINING DOUBLE MACRON BELOW
        chars.append(0x0360)  #uni0360	COMBINING DOUBLE TILDE
        chars.append(0x0361)  #uni0361	COMBINING DOUBLE INVERTED BREVE
        chars.append(0x0362)  #uni0362	COMBINING DOUBLE RIGHTWARDS ARROW BELOW
        chars.append(0x0363)  #uni0363	COMBINING LATIN SMALL LETTER A
        chars.append(0x0364)  #uni0364	COMBINING LATIN SMALL LETTER E
        chars.append(0x0365)  #uni0365	COMBINING LATIN SMALL LETTER I
        chars.append(0x0366)  #uni0366	COMBINING LATIN SMALL LETTER O
        chars.append(0x0367)  #uni0367	COMBINING LATIN SMALL LETTER U
        chars.append(0x0368)  #uni0368	COMBINING LATIN SMALL LETTER C
        chars.append(0x0369)  #uni0369	COMBINING LATIN SMALL LETTER D
        chars.append(0x036A)  #uni036A	COMBINING LATIN SMALL LETTER H
        chars.append(0x036B)  #uni036B	COMBINING LATIN SMALL LETTER M
        chars.append(0x036C)  #uni036C	COMBINING LATIN SMALL LETTER R
        chars.append(0x036D)  #uni036D	COMBINING LATIN SMALL LETTER T
        chars.append(0x036E)  #uni036E	COMBINING LATIN SMALL LETTER V
        chars.append(0x036F)  #uni036F	COMBINING LATIN SMALL LETTER X
        chars.append(0x0374)  #uni0374	GREEK NUMERAL SIGN
        chars.append(0x0375)  #uni0375	GREEK LOWER NUMERAL SIGN
        chars.append(0x037A)  #uni037A	GREEK YPOGEGRAMMENI
        chars.append(0x037B)  #uni037B	GREEK SMALL REVERSED LUNATE SIGMA SYMBOL
        chars.append(0x037C)  #uni037C	GREEK SMALL DOTTED LUNATE SIGMA SYMBOL
        chars.append(0x037D)  #uni037D	GREEK SMALL REVERSED DOTTED LUNATE SIGMA SYMBOL
        chars.append(0x037E)  #semicolon	GREEK QUESTION MARK
        chars.append(0x0384)  #tonos	GREEK TONOS
        chars.append(0x0385)  #dieresistonos	GREEK DIALYTIKA TONOS
        chars.append(0x0386)  #Alphatonos	GREEK CAPITAL LETTER ALPHA WITH TONOS
        chars.append(0x0387)  #anoteleia	GREEK ANO TELEIA
        chars.append(0x0388)  #Epsilontonos	GREEK CAPITAL LETTER EPSILON WITH TONOS
        chars.append(0x0389)  #Etatonos	GREEK CAPITAL LETTER ETA WITH TONOS
        chars.append(0x038A)  #Iotatonos	GREEK CAPITAL LETTER IOTA WITH TONOS
        chars.append(0x038C)  #Omicrontonos	GREEK CAPITAL LETTER OMICRON WITH TONOS
        chars.append(0x038E)  #Upsilontonos	GREEK CAPITAL LETTER UPSILON WITH TONOS
        chars.append(0x038F)  #Omegatonos	GREEK CAPITAL LETTER OMEGA WITH TONOS
        chars.append(0x0390)  #iotadieresistonos	GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
        chars.append(0x0391)  #Alpha	GREEK CAPITAL LETTER ALPHA
        chars.append(0x0392)  #Beta	GREEK CAPITAL LETTER BETA
        chars.append(0x0393)  #Gamma	GREEK CAPITAL LETTER GAMMA
        chars.append(0x0394)  #Delta	GREEK CAPITAL LETTER DELTA
        chars.append(0x0395)  #Epsilon	GREEK CAPITAL LETTER EPSILON
        chars.append(0x0396)  #Zeta	GREEK CAPITAL LETTER ZETA
        chars.append(0x0397)  #Eta	GREEK CAPITAL LETTER ETA
        chars.append(0x0398)  #Theta	GREEK CAPITAL LETTER THETA
        chars.append(0x0399)  #Iota	GREEK CAPITAL LETTER IOTA
        chars.append(0x039A)  #Kappa	GREEK CAPITAL LETTER KAPPA
        chars.append(0x039B)  #Lambda	GREEK CAPITAL LETTER LAMDA
        chars.append(0x039C)  #Mu	GREEK CAPITAL LETTER MU
        chars.append(0x039D)  #Nu	GREEK CAPITAL LETTER NU
        chars.append(0x039E)  #Xi	GREEK CAPITAL LETTER XI
        chars.append(0x039F)  #Omicron	GREEK CAPITAL LETTER OMICRON
        chars.append(0x03A0)  #Pi	GREEK CAPITAL LETTER PI
        chars.append(0x03A1)  #Rho	GREEK CAPITAL LETTER RHO
        chars.append(0x03A3)  #Sigma	GREEK CAPITAL LETTER SIGMA
        chars.append(0x03A4)  #Tau	GREEK CAPITAL LETTER TAU
        chars.append(0x03A5)  #Upsilon	GREEK CAPITAL LETTER UPSILON
        chars.append(0x03A6)  #Phi	GREEK CAPITAL LETTER PHI
        chars.append(0x03A7)  #Chi	GREEK CAPITAL LETTER CHI
        chars.append(0x03A8)  #Psi	GREEK CAPITAL LETTER PSI
        chars.append(0x03A9)  #Omega	GREEK CAPITAL LETTER OMEGA
        chars.append(0x03AA)  #Iotadieresis	GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
        chars.append(0x03AB)  #Upsilondieresis	GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
        chars.append(0x03AC)  #alphatonos	GREEK SMALL LETTER ALPHA WITH TONOS
        chars.append(0x03AD)  #epsilontonos	GREEK SMALL LETTER EPSILON WITH TONOS
        chars.append(0x03AE)  #etatonos	GREEK SMALL LETTER ETA WITH TONOS
        chars.append(0x03AF)  #iotatonos	GREEK SMALL LETTER IOTA WITH TONOS
        chars.append(0x03B0)  #upsilondieresistonos	GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
        chars.append(0x03B1)  #alpha	GREEK SMALL LETTER ALPHA
        chars.append(0x03B2)  #beta	GREEK SMALL LETTER BETA
        chars.append(0x03B3)  #gamma	GREEK SMALL LETTER GAMMA
        chars.append(0x03B4)  #delta	GREEK SMALL LETTER DELTA
        chars.append(0x03B5)  #epsilon	GREEK SMALL LETTER EPSILON
        chars.append(0x03B6)  #zeta	GREEK SMALL LETTER ZETA
        chars.append(0x03B7)  #eta	GREEK SMALL LETTER ETA
        chars.append(0x03B8)  #theta	GREEK SMALL LETTER THETA
        chars.append(0x03B9)  #iota	GREEK SMALL LETTER IOTA
        chars.append(0x03BA)  #kappa	GREEK SMALL LETTER KAPPA
        chars.append(0x03BB)  #lambda	GREEK SMALL LETTER LAMDA
        chars.append(0x03BC)  #mu	GREEK SMALL LETTER MU
        chars.append(0x03BD)  #nu	GREEK SMALL LETTER NU
        chars.append(0x03BE)  #xi	GREEK SMALL LETTER XI
        chars.append(0x03BF)  #omicron	GREEK SMALL LETTER OMICRON
        chars.append(0x03C0)  #pi	GREEK SMALL LETTER PI
        chars.append(0x03C1)  #rho	GREEK SMALL LETTER RHO
        chars.append(0x03C2)  #sigma1	GREEK SMALL LETTER FINAL SIGMA
        chars.append(0x03C3)  #sigma	GREEK SMALL LETTER SIGMA
        chars.append(0x03C4)  #tau	GREEK SMALL LETTER TAU
        chars.append(0x03C5)  #upsilon	GREEK SMALL LETTER UPSILON
        chars.append(0x03C6)  #phi	GREEK SMALL LETTER PHI
        chars.append(0x03C7)  #chi	GREEK SMALL LETTER CHI
        chars.append(0x03C8)  #psi	GREEK SMALL LETTER PSI
        chars.append(0x03C9)  #omega	GREEK SMALL LETTER OMEGA
        chars.append(0x03CA)  #iotadieresis	GREEK SMALL LETTER IOTA WITH DIALYTIKA
        chars.append(0x03CB)  #upsilondieresis	GREEK SMALL LETTER UPSILON WITH DIALYTIKA
        chars.append(0x03CC)  #omicrontonos	GREEK SMALL LETTER OMICRON WITH TONOS
        chars.append(0x03CD)  #upsilontonos	GREEK SMALL LETTER UPSILON WITH TONOS
        chars.append(0x03CE)  #omegatonos	GREEK SMALL LETTER OMEGA WITH TONOS
        chars.append(0x03D0)  #uni03D0	GREEK BETA SYMBOL
        chars.append(0x03D1)  #uni03D1	GREEK THETA SYMBOL
        chars.append(0x03D2)  #uni03D2	GREEK UPSILON WITH HOOK SYMBOL
        chars.append(0x03D3)  #uni03D3	GREEK UPSILON WITH ACUTE AND HOOK SYMBOL
        chars.append(0x03D4)  #uni03D4	GREEK UPSILON WITH DIAERESIS AND HOOK SYMBOL
        chars.append(0x03D5)  #uni03D5	GREEK PHI SYMBOL
        chars.append(0x03D6)  #uni03D6	GREEK PI SYMBOL
        chars.append(0x03D7)  #uni03D7	GREEK KAI SYMBOL
        chars.append(0x03D8)  #uni03D8	GREEK LETTER ARCHAIC KOPPA
        chars.append(0x03D9)  #uni03D9	GREEK SMALL LETTER ARCHAIC KOPPA
        chars.append(0x03DA)  #uni03DA	GREEK LETTER STIGMA
        chars.append(0x03DB)  #uni03DB	GREEK SMALL LETTER STIGMA
        chars.append(0x03DC)  #uni03DC	GREEK LETTER DIGAMMA
        chars.append(0x03DD)  #uni03DD	GREEK SMALL LETTER DIGAMMA
        chars.append(0x03DE)  #uni03DE	GREEK LETTER KOPPA
        chars.append(0x03DF)  #uni03DF	GREEK SMALL LETTER KOPPA
        chars.append(0x03E0)  #uni03E0	GREEK LETTER SAMPI
        chars.append(0x03E1)  #uni03E1	GREEK SMALL LETTER SAMPI
        chars.append(0x03E2)  #uni03E2	COPTIC CAPITAL LETTER SHEI
        chars.append(0x03E3)  #uni03E3	COPTIC SMALL LETTER SHEI
        chars.append(0x03E4)  #uni03E4	COPTIC CAPITAL LETTER FEI
        chars.append(0x03E5)  #uni03E5	COPTIC SMALL LETTER FEI
        chars.append(0x03E6)  #uni03E6	COPTIC CAPITAL LETTER KHEI
        chars.append(0x03E7)  #uni03E7	COPTIC SMALL LETTER KHEI
        chars.append(0x03E8)  #uni03E8	COPTIC CAPITAL LETTER HORI
        chars.append(0x03E9)  #uni03E9	COPTIC SMALL LETTER HORI
        chars.append(0x03EA)  #uni03EA	COPTIC CAPITAL LETTER GANGIA
        chars.append(0x03EB)  #uni03EB	COPTIC SMALL LETTER GANGIA
        chars.append(0x03EC)  #uni03EC	COPTIC CAPITAL LETTER SHIMA
        chars.append(0x03ED)  #uni03ED	COPTIC SMALL LETTER SHIMA
        chars.append(0x03EE)  #uni03EE	COPTIC CAPITAL LETTER DEI
        chars.append(0x03EF)  #uni03EF	COPTIC SMALL LETTER DEI
        chars.append(0x03F0)  #uni03F0	GREEK KAPPA SYMBOL
        chars.append(0x03F1)  #uni03F1	GREEK RHO SYMBOL
        chars.append(0x03F2)  #uni03F2	GREEK LUNATE SIGMA SYMBOL
        chars.append(0x03F3)  #uni03F3	GREEK LETTER YOT
        chars.append(0x03F4)  #uni03F4	GREEK CAPITAL THETA SYMBOL
        chars.append(0x03F5)  #uni03F5	GREEK LUNATE EPSILON SYMBOL
        chars.append(0x03F6)  #uni03F6	GREEK REVERSED LUNATE EPSILON SYMBOL
        chars.append(0x03F7)  #uni03F7	GREEK CAPITAL LETTER SHO
        chars.append(0x03F8)  #uni03F8	GREEK SMALL LETTER SHO
        chars.append(0x03F9)  #uni03F9	GREEK CAPITAL LUNATE SIGMA SYMBOL
        chars.append(0x03FA)  #uni03FA	GREEK CAPITAL LETTER SAN
        chars.append(0x03FB)  #uni03FB	GREEK SMALL LETTER SAN
        chars.append(0x03FC)  #uni03FC	GREEK RHO WITH STROKE SYMBOL
        chars.append(0x03FD)  #uni03FD	GREEK CAPITAL REVERSED LUNATE SIGMA SYMBOL
        chars.append(0x03FE)  #uni03FE	GREEK CAPITAL DOTTED LUNATE SIGMA SYMBOL
        chars.append(0x03FF)  #uni03FF	GREEK CAPITAL REVERSED DOTTED LUNATE SIGMA SYMBOL
        chars.append(0x0400)  #uni0400	CYRILLIC CAPITAL LETTER IE WITH GRAVE
        chars.append(0x0401)  #uni0401	CYRILLIC CAPITAL LETTER IO
        chars.append(0x0402)  #uni0402	CYRILLIC CAPITAL LETTER DJE
        chars.append(0x0403)  #uni0403	CYRILLIC CAPITAL LETTER GJE
        chars.append(0x0404)  #uni0404	CYRILLIC CAPITAL LETTER UKRAINIAN IE
        chars.append(0x0405)  #uni0405	CYRILLIC CAPITAL LETTER DZE
        chars.append(0x0406)  #uni0406	CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
        chars.append(0x0407)  #uni0407	CYRILLIC CAPITAL LETTER YI
        chars.append(0x0408)  #uni0408	CYRILLIC CAPITAL LETTER JE
        chars.append(0x0409)  #uni0409	CYRILLIC CAPITAL LETTER LJE
        chars.append(0x040A)  #uni040A	CYRILLIC CAPITAL LETTER NJE
        chars.append(0x040B)  #uni040B	CYRILLIC CAPITAL LETTER TSHE
        chars.append(0x040C)  #uni040C	CYRILLIC CAPITAL LETTER KJE
        chars.append(0x040D)  #uni040D	CYRILLIC CAPITAL LETTER I WITH GRAVE
        chars.append(0x040E)  #uni040E	CYRILLIC CAPITAL LETTER SHORT U
        chars.append(0x040F)  #uni040F	CYRILLIC CAPITAL LETTER DZHE
        chars.append(0x0410)  #uni0410	CYRILLIC CAPITAL LETTER A
        chars.append(0x0411)  #uni0411	CYRILLIC CAPITAL LETTER BE
        chars.append(0x0412)  #uni0412	CYRILLIC CAPITAL LETTER VE
        chars.append(0x0413)  #uni0413	CYRILLIC CAPITAL LETTER GHE
        chars.append(0x0414)  #uni0414	CYRILLIC CAPITAL LETTER DE
        chars.append(0x0415)  #uni0415	CYRILLIC CAPITAL LETTER IE
        chars.append(0x0416)  #uni0416	CYRILLIC CAPITAL LETTER ZHE
        chars.append(0x0417)  #uni0417	CYRILLIC CAPITAL LETTER ZE
        chars.append(0x0418)  #uni0418	CYRILLIC CAPITAL LETTER I
        chars.append(0x0419)  #uni0419	CYRILLIC CAPITAL LETTER SHORT I
        chars.append(0x041A)  #uni041A	CYRILLIC CAPITAL LETTER KA
        chars.append(0x041B)  #uni041B	CYRILLIC CAPITAL LETTER EL
        chars.append(0x041C)  #uni041C	CYRILLIC CAPITAL LETTER EM
        chars.append(0x041D)  #uni041D	CYRILLIC CAPITAL LETTER EN
        chars.append(0x041E)  #uni041E	CYRILLIC CAPITAL LETTER O
        chars.append(0x041F)  #uni041F	CYRILLIC CAPITAL LETTER PE
        chars.append(0x0420)  #uni0420	CYRILLIC CAPITAL LETTER ER
        chars.append(0x0421)  #uni0421	CYRILLIC CAPITAL LETTER ES
        chars.append(0x0422)  #uni0422	CYRILLIC CAPITAL LETTER TE
        chars.append(0x0423)  #uni0423	CYRILLIC CAPITAL LETTER U
        chars.append(0x0424)  #uni0424	CYRILLIC CAPITAL LETTER EF
        chars.append(0x0425)  #uni0425	CYRILLIC CAPITAL LETTER HA
        chars.append(0x0426)  #uni0426	CYRILLIC CAPITAL LETTER TSE
        chars.append(0x0427)  #uni0427	CYRILLIC CAPITAL LETTER CHE
        chars.append(0x0428)  #uni0428	CYRILLIC CAPITAL LETTER SHA
        chars.append(0x0429)  #uni0429	CYRILLIC CAPITAL LETTER SHCHA
        chars.append(0x042A)  #uni042A	CYRILLIC CAPITAL LETTER HARD SIGN
        chars.append(0x042B)  #uni042B	CYRILLIC CAPITAL LETTER YERU
        chars.append(0x042C)  #uni042C	CYRILLIC CAPITAL LETTER SOFT SIGN
        chars.append(0x042D)  #uni042D	CYRILLIC CAPITAL LETTER E
        chars.append(0x042E)  #uni042E	CYRILLIC CAPITAL LETTER YU
        chars.append(0x042F)  #uni042F	CYRILLIC CAPITAL LETTER YA
        chars.append(0x0430)  #uni0430	CYRILLIC SMALL LETTER A
        chars.append(0x0431)  #uni0431	CYRILLIC SMALL LETTER BE
        chars.append(0x0432)  #uni0432	CYRILLIC SMALL LETTER VE
        chars.append(0x0433)  #uni0433	CYRILLIC SMALL LETTER GHE
        chars.append(0x0434)  #uni0434	CYRILLIC SMALL LETTER DE
        chars.append(0x0435)  #uni0435	CYRILLIC SMALL LETTER IE
        chars.append(0x0436)  #uni0436	CYRILLIC SMALL LETTER ZHE
        chars.append(0x0437)  #uni0437	CYRILLIC SMALL LETTER ZE
        chars.append(0x0438)  #uni0438	CYRILLIC SMALL LETTER I
        chars.append(0x0439)  #uni0439	CYRILLIC SMALL LETTER SHORT I
        chars.append(0x043A)  #uni043A	CYRILLIC SMALL LETTER KA
        chars.append(0x043B)  #uni043B	CYRILLIC SMALL LETTER EL
        chars.append(0x043C)  #uni043C	CYRILLIC SMALL LETTER EM
        chars.append(0x043D)  #uni043D	CYRILLIC SMALL LETTER EN
        chars.append(0x043E)  #uni043E	CYRILLIC SMALL LETTER O
        chars.append(0x043F)  #uni043F	CYRILLIC SMALL LETTER PE
        chars.append(0x0440)  #uni0440	CYRILLIC SMALL LETTER ER
        chars.append(0x0441)  #uni0441	CYRILLIC SMALL LETTER ES
        chars.append(0x0442)  #uni0442	CYRILLIC SMALL LETTER TE
        chars.append(0x0443)  #uni0443	CYRILLIC SMALL LETTER U
        chars.append(0x0444)  #uni0444	CYRILLIC SMALL LETTER EF
        chars.append(0x0445)  #uni0445	CYRILLIC SMALL LETTER HA
        chars.append(0x0446)  #uni0446	CYRILLIC SMALL LETTER TSE
        chars.append(0x0447)  #uni0447	CYRILLIC SMALL LETTER CHE
        chars.append(0x0448)  #uni0448	CYRILLIC SMALL LETTER SHA
        chars.append(0x0449)  #uni0449	CYRILLIC SMALL LETTER SHCHA
        chars.append(0x044A)  #uni044A	CYRILLIC SMALL LETTER HARD SIGN
        chars.append(0x044B)  #uni044B	CYRILLIC SMALL LETTER YERU
        chars.append(0x044C)  #uni044C	CYRILLIC SMALL LETTER SOFT SIGN
        chars.append(0x044D)  #uni044D	CYRILLIC SMALL LETTER E
        chars.append(0x044E)  #uni044E	CYRILLIC SMALL LETTER YU
        chars.append(0x044F)  #uni044F	CYRILLIC SMALL LETTER YA
        chars.append(0x0450)  #uni0450	CYRILLIC SMALL LETTER IE WITH GRAVE
        chars.append(0x0451)  #uni0451	CYRILLIC SMALL LETTER IO
        chars.append(0x0452)  #uni0452	CYRILLIC SMALL LETTER DJE
        chars.append(0x0453)  #uni0453	CYRILLIC SMALL LETTER GJE
        chars.append(0x0454)  #uni0454	CYRILLIC SMALL LETTER UKRAINIAN IE
        chars.append(0x0455)  #uni0455	CYRILLIC SMALL LETTER DZE
        chars.append(0x0456)  #uni0456	CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
        chars.append(0x0457)  #uni0457	CYRILLIC SMALL LETTER YI
        chars.append(0x0458)  #uni0458	CYRILLIC SMALL LETTER JE
        chars.append(0x0459)  #uni0459	CYRILLIC SMALL LETTER LJE
        chars.append(0x045A)  #uni045A	CYRILLIC SMALL LETTER NJE
        chars.append(0x045B)  #uni045B	CYRILLIC SMALL LETTER TSHE
        chars.append(0x045C)  #uni045C	CYRILLIC SMALL LETTER KJE
        chars.append(0x045D)  #uni045D	CYRILLIC SMALL LETTER I WITH GRAVE
        chars.append(0x045E)  #uni045E	CYRILLIC SMALL LETTER SHORT U
        chars.append(0x045F)  #uni045F	CYRILLIC SMALL LETTER DZHE
        chars.append(0x0460)  #uni0460	CYRILLIC CAPITAL LETTER OMEGA
        chars.append(0x0461)  #uni0461	CYRILLIC SMALL LETTER OMEGA
        chars.append(0x0462)  #uni0462	CYRILLIC CAPITAL LETTER YAT
        chars.append(0x0463)  #uni0463	CYRILLIC SMALL LETTER YAT
        chars.append(0x0464)  #uni0464	CYRILLIC CAPITAL LETTER IOTIFIED E
        chars.append(0x0465)  #uni0465	CYRILLIC SMALL LETTER IOTIFIED E
        chars.append(0x0466)  #uni0466	CYRILLIC CAPITAL LETTER LITTLE YUS
        chars.append(0x0467)  #uni0467	CYRILLIC SMALL LETTER LITTLE YUS
        chars.append(0x0468)  #uni0468	CYRILLIC CAPITAL LETTER IOTIFIED LITTLE YUS
        chars.append(0x0469)  #uni0469	CYRILLIC SMALL LETTER IOTIFIED LITTLE YUS
        chars.append(0x046A)  #uni046A	CYRILLIC CAPITAL LETTER BIG YUS
        chars.append(0x046B)  #uni046B	CYRILLIC SMALL LETTER BIG YUS
        chars.append(0x046C)  #uni046C	CYRILLIC CAPITAL LETTER IOTIFIED BIG YUS
        chars.append(0x046D)  #uni046D	CYRILLIC SMALL LETTER IOTIFIED BIG YUS
        chars.append(0x046E)  #uni046E	CYRILLIC CAPITAL LETTER KSI
        chars.append(0x046F)  #uni046F	CYRILLIC SMALL LETTER KSI
        chars.append(0x0470)  #uni0470	CYRILLIC CAPITAL LETTER PSI
        chars.append(0x0471)  #uni0471	CYRILLIC SMALL LETTER PSI
        chars.append(0x0472)  #uni0472	CYRILLIC CAPITAL LETTER FITA
        chars.append(0x0473)  #uni0473	CYRILLIC SMALL LETTER FITA
        chars.append(0x0474)  #uni0474	CYRILLIC CAPITAL LETTER IZHITSA
        chars.append(0x0475)  #uni0475	CYRILLIC SMALL LETTER IZHITSA
        chars.append(0x0476)  #uni0476	CYRILLIC CAPITAL LETTER IZHITSA WITH DOUBLE GRAVE ACCENT
        chars.append(0x0477)  #uni0477	CYRILLIC SMALL LETTER IZHITSA WITH DOUBLE GRAVE ACCENT
        chars.append(0x0478)  #uni0478	CYRILLIC CAPITAL LETTER UK
        chars.append(0x0479)  #uni0479	CYRILLIC SMALL LETTER UK
        chars.append(0x047A)  #uni047A	CYRILLIC CAPITAL LETTER ROUND OMEGA
        chars.append(0x047B)  #uni047B	CYRILLIC SMALL LETTER ROUND OMEGA
        chars.append(0x047C)  #uni047C	CYRILLIC CAPITAL LETTER OMEGA WITH TITLO
        chars.append(0x047D)  #uni047D	CYRILLIC SMALL LETTER OMEGA WITH TITLO
        chars.append(0x047E)  #uni047E	CYRILLIC CAPITAL LETTER OT
        chars.append(0x047F)  #uni047F	CYRILLIC SMALL LETTER OT
        chars.append(0x0480)  #uni0480	CYRILLIC CAPITAL LETTER KOPPA
        chars.append(0x0481)  #uni0481	CYRILLIC SMALL LETTER KOPPA
        chars.append(0x0482)  #uni0482	CYRILLIC THOUSANDS SIGN
        chars.append(0x0483)  #uni0483	COMBINING CYRILLIC TITLO
        chars.append(0x0484)  #uni0484	COMBINING CYRILLIC PALATALIZATION
        chars.append(0x0485)  #uni0485	COMBINING CYRILLIC DASIA PNEUMATA
        chars.append(0x0486)  #uni0486	COMBINING CYRILLIC PSILI PNEUMATA
        chars.append(0x0487)  #uni0487	COMBINING CYRILLIC POKRYTIE
        chars.append(0x0488)  #uni0488	COMBINING CYRILLIC HUNDRED THOUSANDS SIGN
        chars.append(0x0489)  #uni0489	COMBINING CYRILLIC MILLIONS SIGN
        chars.append(0x048A)  #uni048A	CYRILLIC CAPITAL LETTER SHORT I WITH TAIL
        chars.append(0x048B)  #uni048B	CYRILLIC SMALL LETTER SHORT I WITH TAIL
        chars.append(0x048C)  #uni048C	CYRILLIC CAPITAL LETTER SEMISOFT SIGN
        chars.append(0x048D)  #uni048D	CYRILLIC SMALL LETTER SEMISOFT SIGN
        chars.append(0x048E)  #uni048E	CYRILLIC CAPITAL LETTER ER WITH TICK
        chars.append(0x048F)  #uni048F	CYRILLIC SMALL LETTER ER WITH TICK
        chars.append(0x0490)  #uni0490	CYRILLIC CAPITAL LETTER GHE WITH UPTURN
        chars.append(0x0491)  #uni0491	CYRILLIC SMALL LETTER GHE WITH UPTURN
        chars.append(0x0492)  #uni0492	CYRILLIC CAPITAL LETTER GHE WITH STROKE
        chars.append(0x0493)  #uni0493	CYRILLIC SMALL LETTER GHE WITH STROKE
        chars.append(0x0494)  #uni0494	CYRILLIC CAPITAL LETTER GHE WITH MIDDLE HOOK
        chars.append(0x0495)  #uni0495	CYRILLIC SMALL LETTER GHE WITH MIDDLE HOOK
        chars.append(0x0496)  #uni0496	CYRILLIC CAPITAL LETTER ZHE WITH DESCENDER
        chars.append(0x0497)  #uni0497	CYRILLIC SMALL LETTER ZHE WITH DESCENDER
        chars.append(0x0498)  #uni0498	CYRILLIC CAPITAL LETTER ZE WITH DESCENDER
        chars.append(0x0499)  #uni0499	CYRILLIC SMALL LETTER ZE WITH DESCENDER
        chars.append(0x049A)  #uni049A	CYRILLIC CAPITAL LETTER KA WITH DESCENDER
        chars.append(0x049B)  #uni049B	CYRILLIC SMALL LETTER KA WITH DESCENDER
        chars.append(0x049C)  #uni049C	CYRILLIC CAPITAL LETTER KA WITH VERTICAL STROKE
        chars.append(0x049D)  #uni049D	CYRILLIC SMALL LETTER KA WITH VERTICAL STROKE
        chars.append(0x049E)  #uni049E	CYRILLIC CAPITAL LETTER KA WITH STROKE
        chars.append(0x049F)  #uni049F	CYRILLIC SMALL LETTER KA WITH STROKE
        chars.append(0x04A0)  #uni04A0	CYRILLIC CAPITAL LETTER BASHKIR KA
        chars.append(0x04A1)  #uni04A1	CYRILLIC SMALL LETTER BASHKIR KA
        chars.append(0x04A2)  #uni04A2	CYRILLIC CAPITAL LETTER EN WITH DESCENDER
        chars.append(0x04A3)  #uni04A3	CYRILLIC SMALL LETTER EN WITH DESCENDER
        chars.append(0x04A4)  #uni04A4	CYRILLIC CAPITAL LIGATURE EN GHE
        chars.append(0x04A5)  #uni04A5	CYRILLIC SMALL LIGATURE EN GHE
        chars.append(0x04A6)  #uni04A6	CYRILLIC CAPITAL LETTER PE WITH MIDDLE HOOK
        chars.append(0x04A7)  #uni04A7	CYRILLIC SMALL LETTER PE WITH MIDDLE HOOK
        chars.append(0x04A8)  #uni04A8	CYRILLIC CAPITAL LETTER ABKHASIAN HA
        chars.append(0x04A9)  #uni04A9	CYRILLIC SMALL LETTER ABKHASIAN HA
        chars.append(0x04AA)  #uni04AA	CYRILLIC CAPITAL LETTER ES WITH DESCENDER
        chars.append(0x04AB)  #uni04AB	CYRILLIC SMALL LETTER ES WITH DESCENDER
        chars.append(0x04AC)  #uni04AC	CYRILLIC CAPITAL LETTER TE WITH DESCENDER
        chars.append(0x04AD)  #uni04AD	CYRILLIC SMALL LETTER TE WITH DESCENDER
        chars.append(0x04AE)  #uni04AE	CYRILLIC CAPITAL LETTER STRAIGHT U
        chars.append(0x04AF)  #uni04AF	CYRILLIC SMALL LETTER STRAIGHT U
        chars.append(0x04B0)  #uni04B0	CYRILLIC CAPITAL LETTER STRAIGHT U WITH STROKE
        chars.append(0x04B1)  #uni04B1	CYRILLIC SMALL LETTER STRAIGHT U WITH STROKE
        chars.append(0x04B2)  #uni04B2	CYRILLIC CAPITAL LETTER HA WITH DESCENDER
        chars.append(0x04B3)  #uni04B3	CYRILLIC SMALL LETTER HA WITH DESCENDER
        chars.append(0x04B4)  #uni04B4	CYRILLIC CAPITAL LIGATURE TE TSE
        chars.append(0x04B5)  #uni04B5	CYRILLIC SMALL LIGATURE TE TSE
        chars.append(0x04B6)  #uni04B6	CYRILLIC CAPITAL LETTER CHE WITH DESCENDER
        chars.append(0x04B7)  #uni04B7	CYRILLIC SMALL LETTER CHE WITH DESCENDER
        chars.append(0x04B8)  #uni04B8	CYRILLIC CAPITAL LETTER CHE WITH VERTICAL STROKE
        chars.append(0x04B9)  #uni04B9	CYRILLIC SMALL LETTER CHE WITH VERTICAL STROKE
        chars.append(0x04BA)  #uni04BA	CYRILLIC CAPITAL LETTER SHHA
        chars.append(0x04BB)  #uni04BB	CYRILLIC SMALL LETTER SHHA
        chars.append(0x04BC)  #uni04BC	CYRILLIC CAPITAL LETTER ABKHASIAN CHE
        chars.append(0x04BD)  #uni04BD	CYRILLIC SMALL LETTER ABKHASIAN CHE
        chars.append(0x04BE)  #uni04BE	CYRILLIC CAPITAL LETTER ABKHASIAN CHE WITH DESCENDER
        chars.append(0x04BF)  #uni04BF	CYRILLIC SMALL LETTER ABKHASIAN CHE WITH DESCENDER
        chars.append(0x04C0)  #uni04C0	CYRILLIC LETTER PALOCHKA
        chars.append(0x04C1)  #uni04C1	CYRILLIC CAPITAL LETTER ZHE WITH BREVE
        chars.append(0x04C2)  #uni04C2	CYRILLIC SMALL LETTER ZHE WITH BREVE
        chars.append(0x04C3)  #uni04C3	CYRILLIC CAPITAL LETTER KA WITH HOOK
        chars.append(0x04C4)  #uni04C4	CYRILLIC SMALL LETTER KA WITH HOOK
        chars.append(0x04C5)  #uni04C5	CYRILLIC CAPITAL LETTER EL WITH TAIL
        chars.append(0x04C6)  #uni04C6	CYRILLIC SMALL LETTER EL WITH TAIL
        chars.append(0x04C7)  #uni04C7	CYRILLIC CAPITAL LETTER EN WITH HOOK
        chars.append(0x04C8)  #uni04C8	CYRILLIC SMALL LETTER EN WITH HOOK
        chars.append(0x04C9)  #uni04C9	CYRILLIC CAPITAL LETTER EN WITH TAIL
        chars.append(0x04CA)  #uni04CA	CYRILLIC SMALL LETTER EN WITH TAIL
        chars.append(0x04CB)  #uni04CB	CYRILLIC CAPITAL LETTER KHAKASSIAN CHE
        chars.append(0x04CC)  #uni04CC	CYRILLIC SMALL LETTER KHAKASSIAN CHE
        chars.append(0x04CD)  #uni04CD	CYRILLIC CAPITAL LETTER EM WITH TAIL
        chars.append(0x04CE)  #uni04CE	CYRILLIC SMALL LETTER EM WITH TAIL
        chars.append(0x04CF)  #uni04CF	CYRILLIC SMALL LETTER PALOCHKA
        chars.append(0x04D0)  #uni04D0	CYRILLIC CAPITAL LETTER A WITH BREVE
        chars.append(0x04D1)  #uni04D1	CYRILLIC SMALL LETTER A WITH BREVE
        chars.append(0x04D2)  #uni04D2	CYRILLIC CAPITAL LETTER A WITH DIAERESIS
        chars.append(0x04D3)  #uni04D3	CYRILLIC SMALL LETTER A WITH DIAERESIS
        chars.append(0x04D4)  #uni04D4	CYRILLIC CAPITAL LIGATURE A IE
        chars.append(0x04D5)  #uni04D5	CYRILLIC SMALL LIGATURE A IE
        chars.append(0x04D6)  #uni04D6	CYRILLIC CAPITAL LETTER IE WITH BREVE
        chars.append(0x04D7)  #uni04D7	CYRILLIC SMALL LETTER IE WITH BREVE
        chars.append(0x04D8)  #uni018F	CYRILLIC CAPITAL LETTER SCHWA
        chars.append(0x04D9)  #uni0259	CYRILLIC SMALL LETTER SCHWA
        chars.append(0x04DA)  #uni04DA	CYRILLIC CAPITAL LETTER SCHWA WITH DIAERESIS
        chars.append(0x04DB)  #uni04DB	CYRILLIC SMALL LETTER SCHWA WITH DIAERESIS
        chars.append(0x04DC)  #uni04DC	CYRILLIC CAPITAL LETTER ZHE WITH DIAERESIS
        chars.append(0x04DD)  #uni04DD	CYRILLIC SMALL LETTER ZHE WITH DIAERESIS
        chars.append(0x04DE)  #uni04DE	CYRILLIC CAPITAL LETTER ZE WITH DIAERESIS
        chars.append(0x04DF)  #uni04DF	CYRILLIC SMALL LETTER ZE WITH DIAERESIS
        chars.append(0x04E0)  #uni04E0	CYRILLIC CAPITAL LETTER ABKHASIAN DZE
        chars.append(0x04E1)  #uni04E1	CYRILLIC SMALL LETTER ABKHASIAN DZE
        chars.append(0x04E2)  #uni04E2	CYRILLIC CAPITAL LETTER I WITH MACRON
        chars.append(0x04E3)  #uni04E3	CYRILLIC SMALL LETTER I WITH MACRON
        chars.append(0x04E4)  #uni04E4	CYRILLIC CAPITAL LETTER I WITH DIAERESIS
        chars.append(0x04E5)  #uni04E5	CYRILLIC SMALL LETTER I WITH DIAERESIS
        chars.append(0x04E6)  #uni04E6	CYRILLIC CAPITAL LETTER O WITH DIAERESIS
        chars.append(0x04E7)  #uni04E7	CYRILLIC SMALL LETTER O WITH DIAERESIS
        chars.append(0x04E8)  #uni04E8	CYRILLIC CAPITAL LETTER BARRED O
        chars.append(0x04E9)  #uni04E9	CYRILLIC SMALL LETTER BARRED O
        chars.append(0x04EA)  #uni04EA	CYRILLIC CAPITAL LETTER BARRED O WITH DIAERESIS
        chars.append(0x04EB)  #uni04EB	CYRILLIC SMALL LETTER BARRED O WITH DIAERESIS
        chars.append(0x04EC)  #uni04EC	CYRILLIC CAPITAL LETTER E WITH DIAERESIS
        chars.append(0x04ED)  #uni04ED	CYRILLIC SMALL LETTER E WITH DIAERESIS
        chars.append(0x04EE)  #uni04EE	CYRILLIC CAPITAL LETTER U WITH MACRON
        chars.append(0x04EF)  #uni04EF	CYRILLIC SMALL LETTER U WITH MACRON
        chars.append(0x04F0)  #uni04F0	CYRILLIC CAPITAL LETTER U WITH DIAERESIS
        chars.append(0x04F1)  #uni04F1	CYRILLIC SMALL LETTER U WITH DIAERESIS
        chars.append(0x04F2)  #uni04F2	CYRILLIC CAPITAL LETTER U WITH DOUBLE ACUTE
        chars.append(0x04F3)  #uni04F3	CYRILLIC SMALL LETTER U WITH DOUBLE ACUTE
        chars.append(0x04F4)  #uni04F4	CYRILLIC CAPITAL LETTER CHE WITH DIAERESIS
        chars.append(0x04F5)  #uni04F5	CYRILLIC SMALL LETTER CHE WITH DIAERESIS
        chars.append(0x04F6)  #uni04F6	CYRILLIC CAPITAL LETTER GHE WITH DESCENDER
        chars.append(0x04F7)  #uni04F7	CYRILLIC SMALL LETTER GHE WITH DESCENDER
        chars.append(0x04F8)  #uni04F8	CYRILLIC CAPITAL LETTER YERU WITH DIAERESIS
        chars.append(0x04F9)  #uni04F9	CYRILLIC SMALL LETTER YERU WITH DIAERESIS
        chars.append(0x04FA)  #uni04FA	CYRILLIC CAPITAL LETTER GHE WITH STROKE AND HOOK
        chars.append(0x04FB)  #uni04FB	CYRILLIC SMALL LETTER GHE WITH STROKE AND HOOK
        chars.append(0x04FC)  #uni04FC	CYRILLIC CAPITAL LETTER HA WITH HOOK
        chars.append(0x04FD)  #uni04FD	CYRILLIC SMALL LETTER HA WITH HOOK
        chars.append(0x04FE)  #uni04FE	CYRILLIC CAPITAL LETTER HA WITH STROKE
        chars.append(0x04FF)  #uni04FF	CYRILLIC SMALL LETTER HA WITH STROKE
        chars.append(0x0500)  #uni0500	CYRILLIC CAPITAL LETTER KOMI DE
        chars.append(0x0501)  #uni0501	CYRILLIC SMALL LETTER KOMI DE
        chars.append(0x0502)  #uni0502	CYRILLIC CAPITAL LETTER KOMI DJE
        chars.append(0x0503)  #uni0503	CYRILLIC SMALL LETTER KOMI DJE
        chars.append(0x0504)  #uni0504	CYRILLIC CAPITAL LETTER KOMI ZJE
        chars.append(0x0505)  #uni0505	CYRILLIC SMALL LETTER KOMI ZJE
        chars.append(0x0506)  #uni0506	CYRILLIC CAPITAL LETTER KOMI DZJE
        chars.append(0x0507)  #uni0507	CYRILLIC SMALL LETTER KOMI DZJE
        chars.append(0x0508)  #uni0508	CYRILLIC CAPITAL LETTER KOMI LJE
        chars.append(0x0509)  #uni0509	CYRILLIC SMALL LETTER KOMI LJE
        chars.append(0x050A)  #uni050A	CYRILLIC CAPITAL LETTER KOMI NJE
        chars.append(0x050B)  #uni050B	CYRILLIC SMALL LETTER KOMI NJE
        chars.append(0x050C)  #uni050C	CYRILLIC CAPITAL LETTER KOMI SJE
        chars.append(0x050D)  #uni050D	CYRILLIC SMALL LETTER KOMI SJE
        chars.append(0x050E)  #uni050E	CYRILLIC CAPITAL LETTER KOMI TJE
        chars.append(0x050F)  #uni050F	CYRILLIC SMALL LETTER KOMI TJE
        chars.append(0x0510)  #uni0510	CYRILLIC CAPITAL LETTER REVERSED ZE
        chars.append(0x0511)  #uni0511	CYRILLIC SMALL LETTER REVERSED ZE
        chars.append(0x0512)  #uni0512	CYRILLIC CAPITAL LETTER EL WITH HOOK
        chars.append(0x0513)  #uni0513	CYRILLIC SMALL LETTER EL WITH HOOK
        chars.append(0x2514)  #uni2514	BOX DRAWINGS LIGHT UP AND RIGHT
        chars.append(0x2518)  #uni2518	BOX DRAWINGS LIGHT UP AND LEFT
        chars.append(0x051A)  #uni051A	CYRILLIC CAPITAL LETTER QA
        chars.append(0x051B)  #uni051B	CYRILLIC SMALL LETTER QA
        chars.append(0x051C)  #uni051C	CYRILLIC CAPITAL LETTER WE
        chars.append(0x051D)  #uni051D	CYRILLIC SMALL LETTER WE
        chars.append(0x2524)  #uni2524	BOX DRAWINGS LIGHT VERTICAL AND LEFT
        chars.append(0x252C)  #uni252C	BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
        chars.append(0x2534)  #uni2534	BOX DRAWINGS LIGHT UP AND HORIZONTAL
        chars.append(0x253C)  #uni253C	BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
        chars.append(0x2550)  #uni2550	BOX DRAWINGS DOUBLE HORIZONTAL
        chars.append(0x2551)  #uni2551	BOX DRAWINGS DOUBLE VERTICAL
        chars.append(0x2552)  #uni2552	BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
        chars.append(0x2553)  #uni2553	BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
        chars.append(0x2554)  #uni2554	BOX DRAWINGS DOUBLE DOWN AND RIGHT
        chars.append(0x2555)  #uni2555	BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
        chars.append(0x2556)  #uni2556	BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
        chars.append(0x2557)  #uni2557	BOX DRAWINGS DOUBLE DOWN AND LEFT
        chars.append(0x2558)  #uni2558	BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
        chars.append(0x2559)  #uni2559	BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
        chars.append(0x255A)  #uni255A	BOX DRAWINGS DOUBLE UP AND RIGHT
        chars.append(0x255B)  #uni255B	BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
        chars.append(0x255C)  #uni255C	BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
        chars.append(0x255D)  #uni255D	BOX DRAWINGS DOUBLE UP AND LEFT
        chars.append(0x255E)  #uni255E	BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
        chars.append(0x255F)  #uni255F	BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
        chars.append(0x2560)  #uni2560	BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
        chars.append(0x2561)  #uni2561	BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
        chars.append(0x2562)  #uni2562	BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
        chars.append(0x2563)  #uni2563	BOX DRAWINGS DOUBLE VERTICAL AND LEFT
        chars.append(0x2564)  #uni2564	BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x2565)  #uni2565	BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x2566)  #uni2566	BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
        chars.append(0x2567)  #uni2567	BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x2568)  #uni2568	BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x2569)  #uni2569	BOX DRAWINGS DOUBLE UP AND HORIZONTAL
        chars.append(0x256A)  #uni256A	BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x256B)  #uni256B	BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x256C)  #uni256C	BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
        chars.append(0x2026)  #ellipsis	HORIZONTAL ELLIPSIS
        chars.append(0x2580)  #upblock	UPPER HALF BLOCK
        chars.append(0x2584)  #dnblock	LOWER HALF BLOCK
        chars.append(0x2248)  #approxequal	ALMOST EQUAL TO
        chars.append(0x258C)  #lfblock	LEFT HALF BLOCK
        chars.append(0x2590)  #rtblock	RIGHT HALF BLOCK
        chars.append(0x0591)  #uni0591	HEBREW ACCENT ETNAHTA
        chars.append(0x0592)  #uni0592	HEBREW ACCENT SEGOL
        chars.append(0x0593)  #uni0593	HEBREW ACCENT SHALSHELET
        chars.append(0x0594)  #uni0594	HEBREW ACCENT ZAQEF QATAN
        chars.append(0x0595)  #uni0595	HEBREW ACCENT ZAQEF GADOL
        chars.append(0x0596)  #uni0596	HEBREW ACCENT TIPEHA
        chars.append(0x0597)  #uni0597	HEBREW ACCENT REVIA
        chars.append(0x0598)  #uni0598	HEBREW ACCENT ZARQA
        chars.append(0x0599)  #uni0599	HEBREW ACCENT PASHTA
        chars.append(0x059A)  #uni059A	HEBREW ACCENT YETIV
        chars.append(0x059B)  #uni059B	HEBREW ACCENT TEVIR
        chars.append(0x059C)  #uni059C	HEBREW ACCENT GERESH
        chars.append(0x059D)  #uni059D	HEBREW ACCENT GERESH MUQDAM
        chars.append(0x059E)  #uni059E	HEBREW ACCENT GERSHAYIM
        chars.append(0x059F)  #uni059F	HEBREW ACCENT QARNEY PARA
        chars.append(0x05A0)  #uni05A0	HEBREW ACCENT TELISHA GEDOLA
        chars.append(0x05A1)  #uni05A1	HEBREW ACCENT PAZER
        chars.append(0x05A2)  #uni05A2	HEBREW ACCENT ATNAH HAFUKH
        chars.append(0x05A3)  #uni05A3	HEBREW ACCENT MUNAH
        chars.append(0x05A4)  #uni05A4	HEBREW ACCENT MAHAPAKH
        chars.append(0x05A5)  #uni05A5	HEBREW ACCENT MERKHA
        chars.append(0x05A6)  #uni05A6	HEBREW ACCENT MERKHA KEFULA
        chars.append(0x05A7)  #uni05A7	HEBREW ACCENT DARGA
        chars.append(0x05A8)  #uni05A8	HEBREW ACCENT QADMA
        chars.append(0x05A9)  #uni05A9	HEBREW ACCENT TELISHA QETANA
        chars.append(0x05AA)  #uni05AA	HEBREW ACCENT YERAH BEN YOMO
        chars.append(0x05AB)  #uni05AB	HEBREW ACCENT OLE
        chars.append(0x05AC)  #uni05AC	HEBREW ACCENT ILUY
        chars.append(0x05AD)  #uni05AD	HEBREW ACCENT DEHI
        chars.append(0x05AE)  #uni05AE	HEBREW ACCENT ZINOR
        chars.append(0x05AF)  #uni05AF	HEBREW MARK MASORA CIRCLE
        chars.append(0x05B0)  #sheva	HEBREW POINT SHEVA
        chars.append(0x05B1)  #hatafsegol	HEBREW POINT HATAF SEGOL
        chars.append(0x05B2)  #hatafpatah	HEBREW POINT HATAF PATAH
        chars.append(0x05B3)  #hatafqamats	HEBREW POINT HATAF QAMATS
        chars.append(0x05B4)  #hiriq	HEBREW POINT HIRIQ
        chars.append(0x05B5)  #tsere	HEBREW POINT TSERE
        chars.append(0x05B6)  #segol	HEBREW POINT SEGOL
        chars.append(0x05B7)  #patah	HEBREW POINT PATAH
        chars.append(0x05B8)  #qamats	HEBREW POINT QAMATS
        chars.append(0x05B9)  #holam	HEBREW POINT HOLAM
        chars.append(0x05BA)  #uni05BA	HEBREW POINT HOLAM HASER FOR VAV
        chars.append(0x05BB)  #qubuts	HEBREW POINT QUBUTS
        chars.append(0x05BC)  #dagesh	HEBREW POINT DAGESH OR MAPIQ
        chars.append(0x05BD)  #meteg	HEBREW POINT METEG
        chars.append(0x05BE)  #maqaf	HEBREW PUNCTUATION MAQAF
        chars.append(0x05BF)  #rafe	HEBREW POINT RAFE
        chars.append(0x05C0)  #paseq	HEBREW PUNCTUATION PASEQ
        chars.append(0x05C1)  #shindot	HEBREW POINT SHIN DOT
        chars.append(0x05C2)  #sindot	HEBREW POINT SIN DOT
        chars.append(0x05C3)  #sofpasuq	HEBREW PUNCTUATION SOF PASUQ
        chars.append(0x05C4)  #upper_dot	HEBREW MARK UPPER DOT
        chars.append(0x05C5)  #lowerdot	HEBREW MARK LOWER DOT
        chars.append(0x05C6)  #uni05C6	HEBREW PUNCTUATION NUN HAFUKHA
        chars.append(0x05C7)  #qamatsqatan	HEBREW POINT QAMATS QATAN
        chars.append(0x25CA)  #lozenge	LOZENGE
        chars.append(0x25CB)  #circle	WHITE CIRCLE
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x25CF)  #uni25CF	BLACK CIRCLE
        chars.append(0x05D0)  #alef	HEBREW LETTER ALEF
        chars.append(0x05D1)  #bet	HEBREW LETTER BET
        chars.append(0x05D2)  #gimel	HEBREW LETTER GIMEL
        chars.append(0x05D3)  #dalet	HEBREW LETTER DALET
        chars.append(0x05D4)  #he	HEBREW LETTER HE
        chars.append(0x05D5)  #vav	HEBREW LETTER VAV
        chars.append(0x05D6)  #zayin	HEBREW LETTER ZAYIN
        chars.append(0x05D7)  #het	HEBREW LETTER HET
        chars.append(0x05D8)  #tet	HEBREW LETTER TET
        chars.append(0x05D9)  #yod	HEBREW LETTER YOD
        chars.append(0x05DA)  #finalkaf	HEBREW LETTER FINAL KAF
        chars.append(0x05DB)  #kaf	HEBREW LETTER KAF
        chars.append(0x05DC)  #lamed	HEBREW LETTER LAMED
        chars.append(0x05DD)  #finalmem	HEBREW LETTER FINAL MEM
        chars.append(0x05DE)  #mem	HEBREW LETTER MEM
        chars.append(0x05DF)  #finalnun	HEBREW LETTER FINAL NUN
        chars.append(0x05E0)  #nun	HEBREW LETTER NUN
        chars.append(0x05E1)  #samekh	HEBREW LETTER SAMEKH
        chars.append(0x05E2)  #ayin	HEBREW LETTER AYIN
        chars.append(0x05E3)  #finalpe	HEBREW LETTER FINAL PE
        chars.append(0x05E4)  #pe	HEBREW LETTER PE
        chars.append(0x05E5)  #finaltsadi	HEBREW LETTER FINAL TSADI
        chars.append(0x05E6)  #tsadi	HEBREW LETTER TSADI
        chars.append(0x05E7)  #qof	HEBREW LETTER QOF
        chars.append(0x05E8)  #resh	HEBREW LETTER RESH
        chars.append(0x05E9)  #shin	HEBREW LETTER SHIN
        chars.append(0x05EA)  #tav	HEBREW LETTER TAV
        chars.append(0x05F0)  #vavvav	HEBREW LIGATURE YIDDISH DOUBLE VAV
        chars.append(0x05F1)  #vavyod	HEBREW LIGATURE YIDDISH VAV YOD
        chars.append(0x05F2)  #yodyod	HEBREW LIGATURE YIDDISH DOUBLE YOD
        chars.append(0x05F3)  #geresh	HEBREW PUNCTUATION GERESH
        chars.append(0x05F4)  #gershayim	HEBREW PUNCTUATION GERSHAYIM
        chars.append(0x202B)  #uni202B	RIGHT-TO-LEFT EMBEDDING
        chars.append(0x2105)  #uni2105	CARE OF
        chars.append(0x202C)  #uni202C	POP DIRECTIONAL FORMATTING
        chars.append(0x263A)  #smileface	WHITE SMILING FACE
        chars.append(0x263B)  #invsmileface	BLACK SMILING FACE
        chars.append(0x263C)  #sun	WHITE SUN WITH RAYS
        chars.append(0x2640)  #female	FEMALE SIGN
        chars.append(0x2642)  #male	MALE SIGN
        chars.append(0x202D)  #uni202D	LEFT-TO-RIGHT OVERRIDE
        chars.append(0x2660)  #spade	BLACK SPADE SUIT
        chars.append(0x2663)  #club	BLACK CLUB SUIT
        chars.append(0x2665)  #heart	BLACK HEART SUIT
        chars.append(0x2666)  #diamond	BLACK DIAMOND SUIT
        chars.append(0x266A)  #musicalnote	EIGHTH NOTE
        chars.append(0x202E)  #uni202E	RIGHT-TO-LEFT OVERRIDE
        chars.append(0x266F)  #uni266F	MUSIC SHARP SIGN
        chars.append(0x2113)  #uni2113	SCRIPT SMALL L
        chars.append(0x266B)  #musicalnotedbl	BEAMED EIGHTH NOTES
        chars.append(0x2116)  #uni2116	NUMERO SIGN
        chars.append(0x202F)  #uni2009	NARROW NO-BREAK SPACE
        chars.append(0x2117)  #uni2117	SOUND RECORDING COPYRIGHT
        chars.append(0x2030)  #perthousand	PER MILLE SIGN
        chars.append(0x2122)  #trademark	TRADE MARK SIGN
        chars.append(0x2032)  #minute	PRIME
        chars.append(0x2126)  #Ohm	OHM SIGN
        chars.append(0x2033)  #second	DOUBLE PRIME
        chars.append(0x212E)  #estimated	ESTIMATED SYMBOL
        chars.append(0xA717)  #uniA717	MODIFIER LETTER DOT VERTICAL BAR
        chars.append(0xA718)  #uniA718	MODIFIER LETTER DOT SLASH
        chars.append(0xA719)  #uniA719	MODIFIER LETTER DOT HORIZONTAL BAR
        chars.append(0xA71A)  #uniA71A	MODIFIER LETTER LOWER RIGHT CORNER ANGLE
        chars.append(0xA71B)  #uniA71B	MODIFIER LETTER RAISED UP ARROW
        chars.append(0xA71C)  #uniA71C	MODIFIER LETTER RAISED DOWN ARROW
        chars.append(0xA71D)  #uniA71D	MODIFIER LETTER RAISED EXCLAMATION MARK
        chars.append(0xA71E)  #uniA71E	MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK
        chars.append(0x2034)  #uni2034	TRIPLE PRIME
        chars.append(0xA720)  #uniA720	MODIFIER LETTER STRESS AND HIGH TONE
        chars.append(0xA721)  #uniA721	MODIFIER LETTER STRESS AND LOW TONE
        chars.append(0x2588)  #block	FULL BLOCK
        chars.append(0xA788)  #uniA788	MODIFIER LETTER LOW CIRCUMFLEX ACCENT
        chars.append(0xA789)  #uniA789	MODIFIER LETTER COLON
        chars.append(0xA78A)  #uniA78A	MODIFIER LETTER SHORT EQUALS SIGN
        chars.append(0xA78B)  #uniA78B	LATIN CAPITAL LETTER SALTILLO
        chars.append(0xA78C)  #uniA78C	LATIN SMALL LETTER SALTILLO
        chars.append(0xFFFC)  #uniFFFC	OBJECT REPLACEMENT CHARACTER
        chars.append(0x2039)  #guilsinglleft	SINGLE LEFT-POINTING ANGLE QUOTATION MARK
        chars.append(0x214D)  #uni214D	AKTIESELSKAB
        chars.append(0x203A)  #guilsinglright	SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
        chars.append(0x214E)  #uni214E	TURNED SMALL F
        chars.append(0x2153)  #onethird	VULGAR FRACTION ONE THIRD
        chars.append(0x2154)  #twothirds	VULGAR FRACTION TWO THIRDS
        chars.append(0x203C)  #exclamdbl	DOUBLE EXCLAMATION MARK
        chars.append(0x215B)  #oneeighth	VULGAR FRACTION ONE EIGHTH
        chars.append(0x215C)  #threeeighths	VULGAR FRACTION THREE EIGHTHS
        chars.append(0x215D)  #fiveeighths	VULGAR FRACTION FIVE EIGHTHS
        chars.append(0x2591)  #ltshade	LIGHT SHADE
        chars.append(0x215E)  #seveneighths	VULGAR FRACTION SEVEN EIGHTHS
        chars.append(0x203E)  #radicalex	OVERLINE
        chars.append(0x2592)  #shade	MEDIUM SHADE
        chars.append(0x2593)  #dkshade	DARK SHADE
        chars.append(0x2044)  #fraction	FRACTION SLASH
        chars.append(0x2184)  #uni2184	LATIN SMALL LETTER REVERSED C
        chars.append(0x2190)  #arrowleft	LEFTWARDS ARROW
        chars.append(0x2191)  #arrowup	UPWARDS ARROW
        chars.append(0x2192)  #arrowright	RIGHTWARDS ARROW
        chars.append(0x2193)  #arrowdown	DOWNWARDS ARROW
        chars.append(0x2194)  #arrowboth	LEFT RIGHT ARROW
        chars.append(0x2195)  #arrowupdn	UP DOWN ARROW
        chars.append(0x21A8)  #arrowupdnbse	UP DOWN ARROW WITH BASE
        chars.append(0x25A0)  #filledbox	BLACK SQUARE
        chars.append(0x25A1)  #uni25A1	WHITE SQUARE
        chars.append(0x2C67)  #uni2C67	LATIN CAPITAL LETTER H WITH DESCENDER
        chars.append(0x2C6D)  #uni2C6D	LATIN CAPITAL LETTER ALPHA
        chars.append(0xA71F)  #uniA71F	MODIFIER LETTER LOW INVERTED EXCLAMATION MARK
        chars.append(0x25AA)  #uni25AA	BLACK SMALL SQUARE
        chars.append(0x25AB)  #uni25AB	WHITE SMALL SQUARE
        chars.append(0x25AC)  #filledrect	BLACK RECTANGLE
        chars.append(0x205E)  #uni205E	VERTICAL FOUR DOTS
        chars.append(0x2202)  #partialdiff	PARTIAL DIFFERENTIAL
        chars.append(0x25B2)  #triagup	BLACK UP-POINTING TRIANGLE
        chars.append(0x2206)  #uni2206	INCREMENT
        chars.append(0x220F)  #product	N-ARY PRODUCT
        chars.append(0x2C60)  #uni2C60	LATIN CAPITAL LETTER L WITH DOUBLE BAR
        chars.append(0x2C61)  #uni2C61	LATIN SMALL LETTER L WITH DOUBLE BAR
        chars.append(0x2C62)  #uni2C62	LATIN CAPITAL LETTER L WITH MIDDLE TILDE
        chars.append(0x2C63)  #uni2C63	LATIN CAPITAL LETTER P WITH STROKE
        chars.append(0x2C64)  #uni2C64	LATIN CAPITAL LETTER R WITH TAIL
        chars.append(0x2C65)  #uni2C65	LATIN SMALL LETTER A WITH STROKE
        chars.append(0x2C66)  #uni2C66	LATIN SMALL LETTER T WITH DIAGONAL STROKE
        chars.append(0x2211)  #summation	N-ARY SUMMATION
        chars.append(0x2C68)  #uni2C68	LATIN SMALL LETTER H WITH DESCENDER
        chars.append(0x2C69)  #uni2C69	LATIN CAPITAL LETTER K WITH DESCENDER
        chars.append(0x2C6A)  #uni2C6A	LATIN SMALL LETTER K WITH DESCENDER
        chars.append(0x2C6B)  #uni2C6B	LATIN CAPITAL LETTER Z WITH DESCENDER
        chars.append(0x2C6C)  #uni2C6C	LATIN SMALL LETTER Z WITH DESCENDER
        chars.append(0x2212)  #minus	MINUS SIGN
        chars.append(0x2C71)  #uni2C71	LATIN SMALL LETTER V WITH RIGHT HOOK
        chars.append(0x2C72)  #uni2C72	LATIN CAPITAL LETTER W WITH HOOK
        chars.append(0x2C73)  #uni2C73	LATIN SMALL LETTER W WITH HOOK
        chars.append(0x2C74)  #uni2C74	LATIN SMALL LETTER V WITH CURL
        chars.append(0x2C75)  #uni2C75	LATIN CAPITAL LETTER HALF H
        chars.append(0x2C76)  #uni2C76	LATIN SMALL LETTER HALF H
        chars.append(0x2C77)  #uni2C77	LATIN SMALL LETTER TAILLESS PHI
        chars.append(0x2215)  #fraction	DIVISION SLASH
        chars.append(0x2219)  #periodcentered	BULLET OPERATOR
        chars.append(0x221A)  #radical	SQUARE ROOT
        chars.append(0x221E)  #infinity	INFINITY
        chars.append(0x221F)  #orthogonal	RIGHT ANGLE
        chars.append(0x2229)  #intersection	INTERSECTION
        chars.append(0x25BA)  #triagrt	BLACK RIGHT-POINTING POINTER
        chars.append(0x222B)  #integral	INTEGRAL
        chars.append(0x25BC)  #triagdn	BLACK DOWN-POINTING TRIANGLE
        chars.append(0x206A)  #uni206A	INHIBIT SYMMETRIC SWAPPING
        chars.append(0x206B)  #uni206B	ACTIVATE SYMMETRIC SWAPPING
        chars.append(0x206C)  #uni206C	INHIBIT ARABIC FORM SHAPING
        chars.append(0x206D)  #uni206D	ACTIVATE ARABIC FORM SHAPING
        chars.append(0x206E)  #uni206E	NATIONAL DIGIT SHAPES
        chars.append(0x206F)  #uni206F	NOMINAL DIGIT SHAPES
        chars.append(0x2E17)  #uni2E17	DOUBLE OBLIQUE HYPHEN
        chars.append(0x25C4)  #triaglf	BLACK LEFT-POINTING POINTER
        chars.append(0x2260)  #notequal	NOT EQUAL TO
        chars.append(0x2261)  #equivalence	IDENTICAL TO
        chars.append(0x2264)  #lessequal	LESS-THAN OR EQUAL TO
        chars.append(0x2265)  #greaterequal	GREATER-THAN OR EQUAL TO
        chars.append(0x2074)  #foursuperior	SUPERSCRIPT FOUR
        chars.append(0x2075)  #fivesuperior	SUPERSCRIPT FIVE
        chars.append(0x2077)  #sevensuperior	SUPERSCRIPT SEVEN
        chars.append(0x2078)  #eightsuperior	SUPERSCRIPT EIGHT
        chars.append(0xF001)  #fi	????
        chars.append(0xF002)  #fl	????
        chars.append(0xF005)  #undercommaaccent	????
        chars.append(0xF00A)  #uniF00A	????
        chars.append(0xF00B)  #uniF00B	????
        chars.append(0xF00C)  #uniF00C	????
        chars.append(0xF00D)  #uniF00D	????
        chars.append(0xF00E)  #uniF00E	????
        chars.append(0x25D8)  #invbullet	INVERSE BULLET
        chars.append(0x25D9)  #invcircle	INVERSE WHITE CIRCLE
        chars.append(0x20F0)  #uni20F0	COMBINING ASTERISK ABOVE
        chars.append(0x2302)  #house	HOUSE
        chars.append(0x25E6)  #openbullet	WHITE BULLET
        chars.append(0x2310)  #revlogicalnot	REVERSED NOT SIGN
        chars.append(0x2320)  #integraltp	TOP HALF INTEGRAL
        chars.append(0x2321)  #integralbt	BOTTOM HALF INTEGRAL
        chars.append(0x20A0)  #uni20A0	EURO-CURRENCY SIGN
        chars.append(0x20A1)  #uni20A1	COLON SIGN
        chars.append(0x20A2)  #uni20A2	CRUZEIRO SIGN
        chars.append(0x20A3)  #franc	FRENCH FRANC SIGN
        chars.append(0x20A4)  #lira	LIRA SIGN
        chars.append(0x20A5)  #uni20A5	MILL SIGN
        chars.append(0x20A6)  #uni20A6	NAIRA SIGN
        chars.append(0x20A7)  #peseta	PESETA SIGN
        chars.append(0x20A8)  #uni20A8	RUPEE SIGN
        chars.append(0xFE20)  #uniFE20	COMBINING LIGATURE LEFT HALF
        chars.append(0xFE21)  #uniFE21	COMBINING LIGATURE RIGHT HALF
        chars.append(0xFE22)  #uniFE22	COMBINING DOUBLE TILDE LEFT HALF
        chars.append(0xFE23)  #uniFE23	COMBINING DOUBLE TILDE RIGHT HALF
        chars.append(0x20A9)  #uni20A9	WON SIGN
        chars.append(0x202A)  #uni202A	LEFT-TO-RIGHT EMBEDDING
        chars.append(0x20AA)  #sheqel	NEW SHEQEL SIGN
        chars.append(0x20AB)  #dong	DONG SIGN
        chars.append(0x20AC)  #Euro	EURO SIGN
        chars.append(0x20AD)  #uni20AD	KIP SIGN
        chars.append(0x20AE)  #uni20AE	TUGRIK SIGN
        chars.append(0x20AF)  #uni20AF	DRACHMA SIGN
        chars.append(0x20B0)  #uni20B0	GERMAN PENNY SIGN
        chars.append(0x20B1)  #uni20B1	PESO SIGN
        chars.append(0x20B2)  #uni20B2	GUARANI SIGN
        chars.append(0x20B3)  #uni20B3	AUSTRAL SIGN
        chars.append(0x20B4)  #uni20B4	HRYVNIA SIGN
        chars.append(0x20B5)  #uni20B5	CEDI SIGN
        chars.append(0x2500)  #uni2500	BOX DRAWINGS LIGHT HORIZONTAL
        chars.append(0x2502)  #uni2502	BOX DRAWINGS LIGHT VERTICAL
        chars.append(0x2020)  #dagger	DAGGER
        chars.append(0x2021)  #daggerdbl	DOUBLE DAGGER
        chars.append(0x250C)  #uni250C	BOX DRAWINGS LIGHT DOWN AND RIGHT
        chars.append(0x2510)  #uni2510	BOX DRAWINGS LIGHT DOWN AND LEFT
        chars.append(0x2022)  #bullet	BULLET
        chars.append(0x251C)  #uni251C	BOX DRAWINGS LIGHT VERTICAL AND RIGHT
        chars.append(0xFB01)  #fi	LATIN SMALL LIGATURE FI
        chars.append(0xFB02)  #fl	LATIN SMALL LIGATURE FL
        chars.append(0xFB1D)  #uniFB1D	HEBREW LETTER YOD WITH HIRIQ
        chars.append(0xFB1E)  #uniFB1E	HEBREW POINT JUDEO-SPANISH VARIKA
        chars.append(0xFB1F)  #yodyod_patah	HEBREW LIGATURE YIDDISH YOD YOD PATAH
        chars.append(0xFB20)  #alternativeayin	HEBREW LETTER ALTERNATIVE AYIN
        chars.append(0xFB21)  #alefwide	HEBREW LETTER WIDE ALEF
        chars.append(0xFB22)  #daletwide	HEBREW LETTER WIDE DALET
        chars.append(0xFB23)  #hewide	HEBREW LETTER WIDE HE
        chars.append(0xFB24)  #kafwide	HEBREW LETTER WIDE KAF
        chars.append(0xFB25)  #lamedwide	HEBREW LETTER WIDE LAMED
        chars.append(0xFB26)  #finalmemwide	HEBREW LETTER WIDE FINAL MEM
        chars.append(0xFB27)  #reshwide	HEBREW LETTER WIDE RESH
        chars.append(0xFB28)  #tavwide	HEBREW LETTER WIDE TAV
        chars.append(0xFB29)  #alt_plussign	HEBREW LETTER ALTERNATIVE PLUS SIGN
        chars.append(0xFB2A)  #shinshindot	HEBREW LETTER SHIN WITH SHIN DOT
        chars.append(0xFB2B)  #shinsindot	HEBREW LETTER SHIN WITH SIN DOT
        chars.append(0xFB2C)  #shindageshshindot	HEBREW LETTER SHIN WITH DAGESH AND SHIN DOT
        chars.append(0xFB2D)  #shindageshsindot	HEBREW LETTER SHIN WITH DAGESH AND SIN DOT
        chars.append(0xFB2E)  #alefpatah	HEBREW LETTER ALEF WITH PATAH
        chars.append(0xFB2F)  #alefqamats	HEBREW LETTER ALEF WITH QAMATS
        chars.append(0xFB30)  #alefmapiq	HEBREW LETTER ALEF WITH MAPIQ
        chars.append(0xFB31)  #betdagesh	HEBREW LETTER BET WITH DAGESH
        chars.append(0xFB32)  #gimeldagesh	HEBREW LETTER GIMEL WITH DAGESH
        chars.append(0xFB33)  #daletdagesh	HEBREW LETTER DALET WITH DAGESH
        chars.append(0xFB34)  #hedagesh	HEBREW LETTER HE WITH MAPIQ
        chars.append(0xFB35)  #vavdagesh	HEBREW LETTER VAV WITH DAGESH
        chars.append(0xFB36)  #zayindagesh	HEBREW LETTER ZAYIN WITH DAGESH
        chars.append(0xFB38)  #tetdagesh	HEBREW LETTER TET WITH DAGESH
        chars.append(0xFB39)  #yoddagesh	HEBREW LETTER YOD WITH DAGESH
        chars.append(0xFB3A)  #finalkafdagesh	HEBREW LETTER FINAL KAF WITH DAGESH
        chars.append(0xFB3B)  #kafdagesh	HEBREW LETTER KAF WITH DAGESH
        chars.append(0xFB3C)  #lameddagesh	HEBREW LETTER LAMED WITH DAGESH
        chars.append(0xFB3E)  #memdagesh	HEBREW LETTER MEM WITH DAGESH
        chars.append(0xFB40)  #nundagesh	HEBREW LETTER NUN WITH DAGESH
        chars.append(0xFB41)  #samekhdagesh	HEBREW LETTER SAMEKH WITH DAGESH
        chars.append(0xFB43)  #finalpedagesh	HEBREW LETTER FINAL PE WITH DAGESH
        chars.append(0xFB44)  #pedagesh	HEBREW LETTER PE WITH DAGESH
        chars.append(0xFB46)  #tsadidagesh	HEBREW LETTER TSADI WITH DAGESH
        chars.append(0xFB47)  #qofdagesh	HEBREW LETTER QOF WITH DAGESH
        chars.append(0xFB48)  #reshdagesh	HEBREW LETTER RESH WITH DAGESH
        chars.append(0xFB49)  #shindagesh	HEBREW LETTER SHIN WITH DAGESH
        chars.append(0xFB4A)  #tavdagesh	HEBREW LETTER TAV WITH DAGESH
        chars.append(0xFB4B)  #vavholam	HEBREW LETTER VAV WITH HOLAM
        chars.append(0xFB4C)  #betrafe	HEBREW LETTER BET WITH RAFE
        chars.append(0xFB4D)  #kafrafe	HEBREW LETTER KAF WITH RAFE
        chars.append(0xFB4E)  #perafe	HEBREW LETTER PE WITH RAFE
        chars.append(0xFB4F)  #aleflamed	HEBREW LIGATURE ALEF LAMED
        chars.append(0x1D00)  #uni1D00	LATIN LETTER SMALL CAPITAL A
        chars.append(0x1D01)  #uni1D01	LATIN LETTER SMALL CAPITAL AE
        chars.append(0x1D02)  #uni1D02	LATIN SMALL LETTER TURNED AE
        chars.append(0x1D03)  #uni1D03	LATIN LETTER SMALL CAPITAL BARRED B
        chars.append(0x1D04)  #uni1D04	LATIN LETTER SMALL CAPITAL C
        chars.append(0x1D05)  #uni1D05	LATIN LETTER SMALL CAPITAL D
        chars.append(0x1D06)  #uni1D06	LATIN LETTER SMALL CAPITAL ETH
        chars.append(0x1D07)  #uni1D07	LATIN LETTER SMALL CAPITAL E
        chars.append(0x1D08)  #uni1D08	LATIN SMALL LETTER TURNED OPEN E
        chars.append(0x1D09)  #uni1D09	LATIN SMALL LETTER TURNED I
        chars.append(0x1D0A)  #uni1D0A	LATIN LETTER SMALL CAPITAL J
        chars.append(0x1D0B)  #uni1D0B	LATIN LETTER SMALL CAPITAL K
        chars.append(0x1D0C)  #uni1D0C	LATIN LETTER SMALL CAPITAL L WITH STROKE
        chars.append(0x1D0D)  #uni1D0D	LATIN LETTER SMALL CAPITAL M
        chars.append(0x1D0E)  #uni1D0E	LATIN LETTER SMALL CAPITAL REVERSED N
        chars.append(0x1D0F)  #uni1D0F	LATIN LETTER SMALL CAPITAL O
        chars.append(0x1D10)  #uni1D10	LATIN LETTER SMALL CAPITAL OPEN O
        chars.append(0x1D11)  #uni1D11	LATIN SMALL LETTER SIDEWAYS O
        chars.append(0x1D12)  #uni1D12	LATIN SMALL LETTER SIDEWAYS OPEN O
        chars.append(0x1D13)  #uni1D13	LATIN SMALL LETTER SIDEWAYS O WITH STROKE
        chars.append(0x1D14)  #uni1D14	LATIN SMALL LETTER TURNED OE
        chars.append(0x1D15)  #uni1D15	LATIN LETTER SMALL CAPITAL OU
        chars.append(0x1D16)  #uni1D16	LATIN SMALL LETTER TOP HALF O
        chars.append(0x1D17)  #uni1D17	LATIN SMALL LETTER BOTTOM HALF O
        chars.append(0x1D18)  #uni1D18	LATIN LETTER SMALL CAPITAL P
        chars.append(0x1D19)  #uni1D19	LATIN LETTER SMALL CAPITAL REVERSED R
        chars.append(0x1D1A)  #uni1D1A	LATIN LETTER SMALL CAPITAL TURNED R
        chars.append(0x1D1B)  #uni1D1B	LATIN LETTER SMALL CAPITAL T
        chars.append(0x1D1C)  #uni1D1C	LATIN LETTER SMALL CAPITAL U
        chars.append(0x1D1D)  #uni1D1D	LATIN SMALL LETTER SIDEWAYS U
        chars.append(0x1D1E)  #uni1D1E	LATIN SMALL LETTER SIDEWAYS DIAERESIZED U
        chars.append(0x1D1F)  #uni1D1F	LATIN SMALL LETTER SIDEWAYS TURNED M
        chars.append(0x1D20)  #uni1D20	LATIN LETTER SMALL CAPITAL V
        chars.append(0x1D21)  #uni1D21	LATIN LETTER SMALL CAPITAL W
        chars.append(0x1D22)  #uni1D22	LATIN LETTER SMALL CAPITAL Z
        chars.append(0x1D23)  #uni1D23	LATIN LETTER SMALL CAPITAL EZH
        chars.append(0x1D24)  #uni1D24	LATIN LETTER VOICED LARYNGEAL SPIRANT
        chars.append(0x1D25)  #uni1D25	LATIN LETTER AIN
        chars.append(0x1D26)  #uni1D26	GREEK LETTER SMALL CAPITAL GAMMA
        chars.append(0x1D27)  #uni1D27	GREEK LETTER SMALL CAPITAL LAMDA
        chars.append(0x1D28)  #uni1D28	GREEK LETTER SMALL CAPITAL PI
        chars.append(0x1D29)  #uni1D29	GREEK LETTER SMALL CAPITAL RHO
        chars.append(0x1D2A)  #uni1D2A	GREEK LETTER SMALL CAPITAL PSI
        chars.append(0x1D2B)  #uni1D2B	CYRILLIC LETTER SMALL CAPITAL EL
        chars.append(0x1D2C)  #uni1D2C	MODIFIER LETTER CAPITAL A
        chars.append(0x1D2D)  #uni1D2D	MODIFIER LETTER CAPITAL AE
        chars.append(0x1D2E)  #uni1D2E	MODIFIER LETTER CAPITAL B
        chars.append(0x1D2F)  #uni1D2F	MODIFIER LETTER CAPITAL BARRED B
        chars.append(0x1D30)  #uni1D30	MODIFIER LETTER CAPITAL D
        chars.append(0x1D31)  #uni1D31	MODIFIER LETTER CAPITAL E
        chars.append(0x1D32)  #uni1D32	MODIFIER LETTER CAPITAL REVERSED E
        chars.append(0x1D33)  #uni1D33	MODIFIER LETTER CAPITAL G
        chars.append(0x1D34)  #uni1D34	MODIFIER LETTER CAPITAL H
        chars.append(0x1D35)  #uni1D35	MODIFIER LETTER CAPITAL I
        chars.append(0x1D36)  #uni1D36	MODIFIER LETTER CAPITAL J
        chars.append(0x1D37)  #uni1D37	MODIFIER LETTER CAPITAL K
        chars.append(0x1D38)  #uni1D38	MODIFIER LETTER CAPITAL L
        chars.append(0x1D39)  #uni1D39	MODIFIER LETTER CAPITAL M
        chars.append(0x1D3A)  #uni1D3A	MODIFIER LETTER CAPITAL N
        chars.append(0x1D3B)  #uni1D3B	MODIFIER LETTER CAPITAL REVERSED N
        chars.append(0x1D3C)  #uni1D3C	MODIFIER LETTER CAPITAL O
        chars.append(0x1D3D)  #uni1D3D	MODIFIER LETTER CAPITAL OU
        chars.append(0x1D3E)  #uni1D3E	MODIFIER LETTER CAPITAL P
        chars.append(0x1D3F)  #uni1D3F	MODIFIER LETTER CAPITAL R
        chars.append(0x1D40)  #uni1D40	MODIFIER LETTER CAPITAL T
        chars.append(0x1D41)  #uni1D41	MODIFIER LETTER CAPITAL U
        chars.append(0x1D42)  #uni1D42	MODIFIER LETTER CAPITAL W
        chars.append(0x1D43)  #uni1D43	MODIFIER LETTER SMALL A
        chars.append(0x1D44)  #uni1D44	MODIFIER LETTER SMALL TURNED A
        chars.append(0x1D45)  #uni1D45	MODIFIER LETTER SMALL ALPHA
        chars.append(0x1D46)  #uni1D46	MODIFIER LETTER SMALL TURNED AE
        chars.append(0x1D47)  #uni1D47	MODIFIER LETTER SMALL B
        chars.append(0x1D48)  #uni1D48	MODIFIER LETTER SMALL D
        chars.append(0x1D49)  #uni1D49	MODIFIER LETTER SMALL E
        chars.append(0x1D4A)  #uni1D4A	MODIFIER LETTER SMALL SCHWA
        chars.append(0x1D4B)  #uni1D4B	MODIFIER LETTER SMALL OPEN E
        chars.append(0x1D4C)  #uni1D4C	MODIFIER LETTER SMALL TURNED OPEN E
        chars.append(0x1D4D)  #uni1D4D	MODIFIER LETTER SMALL G
        chars.append(0x1D4E)  #uni1D4E	MODIFIER LETTER SMALL TURNED I
        chars.append(0x1D4F)  #uni1D4F	MODIFIER LETTER SMALL K
        chars.append(0x1D50)  #uni1D50	MODIFIER LETTER SMALL M
        chars.append(0x1D51)  #uni1D51	MODIFIER LETTER SMALL ENG
        chars.append(0x1D52)  #uni1D52	MODIFIER LETTER SMALL O
        chars.append(0x1D53)  #uni1D53	MODIFIER LETTER SMALL OPEN O
        chars.append(0x1D54)  #uni1D54	MODIFIER LETTER SMALL TOP HALF O
        chars.append(0x1D55)  #uni1D55	MODIFIER LETTER SMALL BOTTOM HALF O
        chars.append(0x1D56)  #uni1D56	MODIFIER LETTER SMALL P
        chars.append(0x1D57)  #uni1D57	MODIFIER LETTER SMALL T
        chars.append(0x1D58)  #uni1D58	MODIFIER LETTER SMALL U
        chars.append(0x1D59)  #uni1D59	MODIFIER LETTER SMALL SIDEWAYS U
        chars.append(0x1D5A)  #uni1D5A	MODIFIER LETTER SMALL TURNED M
        chars.append(0x1D5B)  #uni1D5B	MODIFIER LETTER SMALL V
        chars.append(0x1D5C)  #uni1D5C	MODIFIER LETTER SMALL AIN
        chars.append(0x1D5D)  #uni1D5D	MODIFIER LETTER SMALL BETA
        chars.append(0x1D5E)  #uni1D5E	MODIFIER LETTER SMALL GREEK GAMMA
        chars.append(0x1D5F)  #uni1D5F	MODIFIER LETTER SMALL DELTA
        chars.append(0x1D60)  #uni1D60	MODIFIER LETTER SMALL GREEK PHI
        chars.append(0x1D61)  #uni1D61	MODIFIER LETTER SMALL CHI
        chars.append(0x1D62)  #uni1D62	LATIN SUBSCRIPT SMALL LETTER I
        chars.append(0x1D63)  #uni1D63	LATIN SUBSCRIPT SMALL LETTER R
        chars.append(0x1D64)  #uni1D64	LATIN SUBSCRIPT SMALL LETTER U
        chars.append(0x1D65)  #uni1D65	LATIN SUBSCRIPT SMALL LETTER V
        chars.append(0x1D66)  #uni1D66	GREEK SUBSCRIPT SMALL LETTER BETA
        chars.append(0x1D67)  #uni1D67	GREEK SUBSCRIPT SMALL LETTER GAMMA
        chars.append(0x1D68)  #uni1D68	GREEK SUBSCRIPT SMALL LETTER RHO
        chars.append(0x1D69)  #uni1D69	GREEK SUBSCRIPT SMALL LETTER PHI
        chars.append(0x1D6A)  #uni1D6A	GREEK SUBSCRIPT SMALL LETTER CHI
        chars.append(0x1D6B)  #uni1D6B	LATIN SMALL LETTER UE
        chars.append(0x1D6C)  #uni1D6C	LATIN SMALL LETTER B WITH MIDDLE TILDE
        chars.append(0x1D6D)  #uni1D6D	LATIN SMALL LETTER D WITH MIDDLE TILDE
        chars.append(0x1D6E)  #uni1D6E	LATIN SMALL LETTER F WITH MIDDLE TILDE
        chars.append(0x1D6F)  #uni1D6F	LATIN SMALL LETTER M WITH MIDDLE TILDE
        chars.append(0x1D70)  #uni1D70	LATIN SMALL LETTER N WITH MIDDLE TILDE
        chars.append(0x1D71)  #uni1D71	LATIN SMALL LETTER P WITH MIDDLE TILDE
        chars.append(0x1D72)  #uni1D72	LATIN SMALL LETTER R WITH MIDDLE TILDE
        chars.append(0x1D73)  #uni1D73	LATIN SMALL LETTER R WITH FISHHOOK AND MIDDLE TILDE
        chars.append(0x1D74)  #uni1D74	LATIN SMALL LETTER S WITH MIDDLE TILDE
        chars.append(0x1D75)  #uni1D75	LATIN SMALL LETTER T WITH MIDDLE TILDE
        chars.append(0x1D76)  #uni1D76	LATIN SMALL LETTER Z WITH MIDDLE TILDE
        chars.append(0x1D77)  #uni1D77	LATIN SMALL LETTER TURNED G
        chars.append(0x1D78)  #uni1D78	MODIFIER LETTER CYRILLIC EN
        chars.append(0x1D79)  #uni1D79	LATIN SMALL LETTER INSULAR G
        chars.append(0x1D7A)  #uni1D7A	LATIN SMALL LETTER TH WITH STRIKETHROUGH
        chars.append(0x1D7B)  #uni1D7B	LATIN SMALL CAPITAL LETTER I WITH STROKE
        chars.append(0x1D7C)  #uni1D7C	LATIN SMALL LETTER IOTA WITH STROKE
        chars.append(0x1D7D)  #uni1D7D	LATIN SMALL LETTER P WITH STROKE
        chars.append(0x1D7E)  #uni1D7E	LATIN SMALL CAPITAL LETTER U WITH STROKE
        chars.append(0x1D7F)  #uni1D7F	LATIN SMALL LETTER UPSILON WITH STROKE
        chars.append(0x1D80)  #uni1D80	LATIN SMALL LETTER B WITH PALATAL HOOK
        chars.append(0x1D81)  #uni1D81	LATIN SMALL LETTER D WITH PALATAL HOOK
        chars.append(0x1D82)  #uni1D82	LATIN SMALL LETTER F WITH PALATAL HOOK
        chars.append(0x1D83)  #uni1D83	LATIN SMALL LETTER G WITH PALATAL HOOK
        chars.append(0x1D84)  #uni1D84	LATIN SMALL LETTER K WITH PALATAL HOOK
        chars.append(0x1D85)  #uni1D85	LATIN SMALL LETTER L WITH PALATAL HOOK
        chars.append(0x1D86)  #uni1D86	LATIN SMALL LETTER M WITH PALATAL HOOK
        chars.append(0x1D87)  #uni1D87	LATIN SMALL LETTER N WITH PALATAL HOOK
        chars.append(0x1D88)  #uni1D88	LATIN SMALL LETTER P WITH PALATAL HOOK
        chars.append(0x1D89)  #uni1D89	LATIN SMALL LETTER R WITH PALATAL HOOK
        chars.append(0x1D8A)  #uni1D8A	LATIN SMALL LETTER S WITH PALATAL HOOK
        chars.append(0x1D8B)  #uni1D8B	LATIN SMALL LETTER ESH WITH PALATAL HOOK
        chars.append(0x1D8C)  #uni1D8C	LATIN SMALL LETTER V WITH PALATAL HOOK
        chars.append(0x1D8D)  #uni1D8D	LATIN SMALL LETTER X WITH PALATAL HOOK
        chars.append(0x1D8E)  #uni1D8E	LATIN SMALL LETTER Z WITH PALATAL HOOK
        chars.append(0x1D8F)  #uni1D8F	LATIN SMALL LETTER A WITH RETROFLEX HOOK
        chars.append(0x1D90)  #uni1D90	LATIN SMALL LETTER ALPHA WITH RETROFLEX HOOK
        chars.append(0x1D91)  #uni1D91	LATIN SMALL LETTER D WITH HOOK AND TAIL
        chars.append(0x1D92)  #uni1D92	LATIN SMALL LETTER E WITH RETROFLEX HOOK
        chars.append(0x1D93)  #uni1D93	LATIN SMALL LETTER OPEN E WITH RETROFLEX HOOK
        chars.append(0x1D94)  #uni1D94	LATIN SMALL LETTER REVERSED OPEN E WITH RETROFLEX HOOK
        chars.append(0x1D95)  #uni1D95	LATIN SMALL LETTER SCHWA WITH RETROFLEX HOOK
        chars.append(0x1D96)  #uni1D96	LATIN SMALL LETTER I WITH RETROFLEX HOOK
        chars.append(0x1D97)  #uni1D97	LATIN SMALL LETTER OPEN O WITH RETROFLEX HOOK
        chars.append(0x1D98)  #uni1D98	LATIN SMALL LETTER ESH WITH RETROFLEX HOOK
        chars.append(0x1D99)  #uni1D99	LATIN SMALL LETTER U WITH RETROFLEX HOOK
        chars.append(0x1D9A)  #uni1D9A	LATIN SMALL LETTER EZH WITH RETROFLEX HOOK
        chars.append(0x1D9B)  #uni1D9B	MODIFIER LETTER SMALL TURNED ALPHA
        chars.append(0x1D9C)  #uni1D9C	MODIFIER LETTER SMALL C
        chars.append(0x1D9D)  #uni1D9D	MODIFIER LETTER SMALL C WITH CURL
        chars.append(0x1D9E)  #uni1D9E	MODIFIER LETTER SMALL ETH
        chars.append(0x1D9F)  #uni1D9F	MODIFIER LETTER SMALL REVERSED OPEN E
        chars.append(0x1DA0)  #uni1DA0	MODIFIER LETTER SMALL F
        chars.append(0x1DA1)  #uni1DA1	MODIFIER LETTER SMALL DOTLESS J WITH STROKE
        chars.append(0x1DA2)  #uni1DA2	MODIFIER LETTER SMALL SCRIPT G
        chars.append(0x1DA3)  #uni1DA3	MODIFIER LETTER SMALL TURNED H
        chars.append(0x1DA4)  #uni1DA4	MODIFIER LETTER SMALL I WITH STROKE
        chars.append(0x1DA5)  #uni1DA5	MODIFIER LETTER SMALL IOTA
        chars.append(0x1DA6)  #uni1DA6	MODIFIER LETTER SMALL CAPITAL I
        chars.append(0x1DA7)  #uni1DA7	MODIFIER LETTER SMALL CAPITAL I WITH STROKE
        chars.append(0x1DA8)  #uni1DA8	MODIFIER LETTER SMALL J WITH CROSSED-TAIL
        chars.append(0x1DA9)  #uni1DA9	MODIFIER LETTER SMALL L WITH RETROFLEX HOOK
        chars.append(0x1DAA)  #uni1DAA	MODIFIER LETTER SMALL L WITH PALATAL HOOK
        chars.append(0x1DAB)  #uni1DAB	MODIFIER LETTER SMALL CAPITAL L
        chars.append(0x1DAC)  #uni1DAC	MODIFIER LETTER SMALL M WITH HOOK
        chars.append(0x1DAD)  #uni1DAD	MODIFIER LETTER SMALL TURNED M WITH LONG LEG
        chars.append(0x1DAE)  #uni1DAE	MODIFIER LETTER SMALL N WITH LEFT HOOK
        chars.append(0x1DAF)  #uni1DAF	MODIFIER LETTER SMALL N WITH RETROFLEX HOOK
        chars.append(0x1DB0)  #uni1DB0	MODIFIER LETTER SMALL CAPITAL N
        chars.append(0x1DB1)  #uni1DB1	MODIFIER LETTER SMALL BARRED O
        chars.append(0x1DB2)  #uni1DB2	MODIFIER LETTER SMALL PHI
        chars.append(0x1DB3)  #uni1DB3	MODIFIER LETTER SMALL S WITH HOOK
        chars.append(0x1DB4)  #uni1DB4	MODIFIER LETTER SMALL ESH
        chars.append(0x1DB5)  #uni1DB5	MODIFIER LETTER SMALL T WITH PALATAL HOOK
        chars.append(0x1DB6)  #uni1DB6	MODIFIER LETTER SMALL U BAR
        chars.append(0x1DB7)  #uni1DB7	MODIFIER LETTER SMALL UPSILON
        chars.append(0x1DB8)  #uni1DB8	MODIFIER LETTER SMALL CAPITAL U
        chars.append(0x1DB9)  #uni1DB9	MODIFIER LETTER SMALL V WITH HOOK
        chars.append(0x1DBA)  #uni1DBA	MODIFIER LETTER SMALL TURNED V
        chars.append(0x1DBB)  #uni1DBB	MODIFIER LETTER SMALL Z
        chars.append(0x1DBC)  #uni1DBC	MODIFIER LETTER SMALL Z WITH RETROFLEX HOOK
        chars.append(0x1DBD)  #uni1DBD	MODIFIER LETTER SMALL Z WITH CURL
        chars.append(0x1DBE)  #uni1DBE	MODIFIER LETTER SMALL EZH
        chars.append(0x1DBF)  #uni1DBF	MODIFIER LETTER SMALL THETA
        chars.append(0x1DC0)  #uni1DC0	COMBINING DOTTED GRAVE ACCENT
        chars.append(0x1DC1)  #uni1DC1	COMBINING DOTTED ACUTE ACCENT
        chars.append(0x1DC2)  #uni1DC2	COMBINING SNAKE BELOW
        chars.append(0x1DC3)  #uni1DC3	COMBINING SUSPENSION MARK
        chars.append(0x1DC4)  #uni1DC4	COMBINING MACRON-ACUTE
        chars.append(0x1DC5)  #uni1DC5	COMBINING GRAVE-MACRON
        chars.append(0x1DC6)  #uni1DC6	COMBINING MACRON-GRAVE
        chars.append(0x1DC7)  #uni1DC7	COMBINING ACUTE-MACRON
        chars.append(0x1DC8)  #uni1DC8	COMBINING GRAVE-ACUTE-GRAVE
        chars.append(0x1DC9)  #uni1DC9	COMBINING ACUTE-GRAVE-ACUTE
        chars.append(0x1DCA)  #uni1DCA	COMBINING LATIN SMALL LETTER R BELOW
        chars.append(0x1DFE)  #uni1DFE	COMBINING LEFT ARROWHEAD ABOVE
        chars.append(0x1DFF)  #uni1DFF	COMBINING RIGHT ARROWHEAD AND DOWN ARROWHEAD BELOW
        chars.append(0x1E00)  #uni1E00	LATIN CAPITAL LETTER A WITH RING BELOW
        chars.append(0x1E01)  #uni1E01	LATIN SMALL LETTER A WITH RING BELOW
        chars.append(0x1E02)  #uni1E02	LATIN CAPITAL LETTER B WITH DOT ABOVE
        chars.append(0x1E03)  #uni1E03	LATIN SMALL LETTER B WITH DOT ABOVE
        chars.append(0x1E04)  #uni1E04	LATIN CAPITAL LETTER B WITH DOT BELOW
        chars.append(0x1E05)  #uni1E05	LATIN SMALL LETTER B WITH DOT BELOW
        chars.append(0x1E06)  #uni1E06	LATIN CAPITAL LETTER B WITH LINE BELOW
        chars.append(0x1E07)  #uni1E07	LATIN SMALL LETTER B WITH LINE BELOW
        chars.append(0x1E08)  #uni1E08	LATIN CAPITAL LETTER C WITH CEDILLA AND ACUTE
        chars.append(0x1E09)  #uni1E09	LATIN SMALL LETTER C WITH CEDILLA AND ACUTE
        chars.append(0x1E0A)  #uni1E0A	LATIN CAPITAL LETTER D WITH DOT ABOVE
        chars.append(0x1E0B)  #uni1E0B	LATIN SMALL LETTER D WITH DOT ABOVE
        chars.append(0x1E0C)  #uni1E0C	LATIN CAPITAL LETTER D WITH DOT BELOW
        chars.append(0x1E0D)  #uni1E0D	LATIN SMALL LETTER D WITH DOT BELOW
        chars.append(0x1E0E)  #uni1E0E	LATIN CAPITAL LETTER D WITH LINE BELOW
        chars.append(0x1E0F)  #uni1E0F	LATIN SMALL LETTER D WITH LINE BELOW
        chars.append(0x1E10)  #uni1E10	LATIN CAPITAL LETTER D WITH CEDILLA
        chars.append(0x1E11)  #uni1E11	LATIN SMALL LETTER D WITH CEDILLA
        chars.append(0x1E12)  #uni1E12	LATIN CAPITAL LETTER D WITH CIRCUMFLEX BELOW
        chars.append(0x1E13)  #uni1E13	LATIN SMALL LETTER D WITH CIRCUMFLEX BELOW
        chars.append(0x1E14)  #uni1E14	LATIN CAPITAL LETTER E WITH MACRON AND GRAVE
        chars.append(0x1E15)  #uni1E15	LATIN SMALL LETTER E WITH MACRON AND GRAVE
        chars.append(0x1E16)  #uni1E16	LATIN CAPITAL LETTER E WITH MACRON AND ACUTE
        chars.append(0x1E17)  #uni1E17	LATIN SMALL LETTER E WITH MACRON AND ACUTE
        chars.append(0x1E18)  #uni1E18	LATIN CAPITAL LETTER E WITH CIRCUMFLEX BELOW
        chars.append(0x1E19)  #uni1E19	LATIN SMALL LETTER E WITH CIRCUMFLEX BELOW
        chars.append(0x1E1A)  #uni1E1A	LATIN CAPITAL LETTER E WITH TILDE BELOW
        chars.append(0x1E1B)  #uni1E1B	LATIN SMALL LETTER E WITH TILDE BELOW
        chars.append(0x1E1C)  #uni1E1C	LATIN CAPITAL LETTER E WITH CEDILLA AND BREVE
        chars.append(0x1E1D)  #uni1E1D	LATIN SMALL LETTER E WITH CEDILLA AND BREVE
        chars.append(0x1E1E)  #uni1E1E	LATIN CAPITAL LETTER F WITH DOT ABOVE
        chars.append(0x1E1F)  #uni1E1F	LATIN SMALL LETTER F WITH DOT ABOVE
        chars.append(0x1E20)  #uni1E20	LATIN CAPITAL LETTER G WITH MACRON
        chars.append(0x1E21)  #uni1E21	LATIN SMALL LETTER G WITH MACRON
        chars.append(0x1E22)  #uni1E22	LATIN CAPITAL LETTER H WITH DOT ABOVE
        chars.append(0x1E23)  #uni1E23	LATIN SMALL LETTER H WITH DOT ABOVE
        chars.append(0x1E24)  #uni1E24	LATIN CAPITAL LETTER H WITH DOT BELOW
        chars.append(0x1E25)  #uni1E25	LATIN SMALL LETTER H WITH DOT BELOW
        chars.append(0x1E26)  #uni1E26	LATIN CAPITAL LETTER H WITH DIAERESIS
        chars.append(0x1E27)  #uni1E27	LATIN SMALL LETTER H WITH DIAERESIS
        chars.append(0x1E28)  #uni1E28	LATIN CAPITAL LETTER H WITH CEDILLA
        chars.append(0x1E29)  #uni1E29	LATIN SMALL LETTER H WITH CEDILLA
        chars.append(0x1E2A)  #uni1E2A	LATIN CAPITAL LETTER H WITH BREVE BELOW
        chars.append(0x1E2B)  #uni1E2B	LATIN SMALL LETTER H WITH BREVE BELOW
        chars.append(0x1E2C)  #uni1E2C	LATIN CAPITAL LETTER I WITH TILDE BELOW
        chars.append(0x1E2D)  #uni1E2D	LATIN SMALL LETTER I WITH TILDE BELOW
        chars.append(0x1E2E)  #uni1E2E	LATIN CAPITAL LETTER I WITH DIAERESIS AND ACUTE
        chars.append(0x1E2F)  #uni1E2F	LATIN SMALL LETTER I WITH DIAERESIS AND ACUTE
        chars.append(0x1E30)  #uni1E30	LATIN CAPITAL LETTER K WITH ACUTE
        chars.append(0x1E31)  #uni1E31	LATIN SMALL LETTER K WITH ACUTE
        chars.append(0x1E32)  #uni1E32	LATIN CAPITAL LETTER K WITH DOT BELOW
        chars.append(0x1E33)  #uni1E33	LATIN SMALL LETTER K WITH DOT BELOW
        chars.append(0x1E34)  #uni1E34	LATIN CAPITAL LETTER K WITH LINE BELOW
        chars.append(0x1E35)  #uni1E35	LATIN SMALL LETTER K WITH LINE BELOW
        chars.append(0x1E36)  #uni1E36	LATIN CAPITAL LETTER L WITH DOT BELOW
        chars.append(0x1E37)  #uni1E37	LATIN SMALL LETTER L WITH DOT BELOW
        chars.append(0x1E38)  #uni1E38	LATIN CAPITAL LETTER L WITH DOT BELOW AND MACRON
        chars.append(0x1E39)  #uni1E39	LATIN SMALL LETTER L WITH DOT BELOW AND MACRON
        chars.append(0x1E3A)  #uni1E3A	LATIN CAPITAL LETTER L WITH LINE BELOW
        chars.append(0x1E3B)  #uni1E3B	LATIN SMALL LETTER L WITH LINE BELOW
        chars.append(0x1E3C)  #uni1E3C	LATIN CAPITAL LETTER L WITH CIRCUMFLEX BELOW
        chars.append(0x1E3D)  #uni1E3D	LATIN SMALL LETTER L WITH CIRCUMFLEX BELOW
        chars.append(0x1E3E)  #uni1E3E	LATIN CAPITAL LETTER M WITH ACUTE
        chars.append(0x1E3F)  #uni1E3F	LATIN SMALL LETTER M WITH ACUTE
        chars.append(0x1E40)  #uni1E40	LATIN CAPITAL LETTER M WITH DOT ABOVE
        chars.append(0x1E41)  #uni1E41	LATIN SMALL LETTER M WITH DOT ABOVE
        chars.append(0x1E42)  #uni1E42	LATIN CAPITAL LETTER M WITH DOT BELOW
        chars.append(0x1E43)  #uni1E43	LATIN SMALL LETTER M WITH DOT BELOW
        chars.append(0x1E44)  #uni1E44	LATIN CAPITAL LETTER N WITH DOT ABOVE
        chars.append(0x1E45)  #uni1E45	LATIN SMALL LETTER N WITH DOT ABOVE
        chars.append(0x1E46)  #uni1E46	LATIN CAPITAL LETTER N WITH DOT BELOW
        chars.append(0x1E47)  #uni1E47	LATIN SMALL LETTER N WITH DOT BELOW
        chars.append(0x1E48)  #uni1E48	LATIN CAPITAL LETTER N WITH LINE BELOW
        chars.append(0x1E49)  #uni1E49	LATIN SMALL LETTER N WITH LINE BELOW
        chars.append(0x1E4A)  #uni1E4A	LATIN CAPITAL LETTER N WITH CIRCUMFLEX BELOW
        chars.append(0x1E4B)  #uni1E4B	LATIN SMALL LETTER N WITH CIRCUMFLEX BELOW
        chars.append(0x1E4C)  #uni1E4C	LATIN CAPITAL LETTER O WITH TILDE AND ACUTE
        chars.append(0x1E4D)  #uni1E4D	LATIN SMALL LETTER O WITH TILDE AND ACUTE
        chars.append(0x1E4E)  #uni1E4E	LATIN CAPITAL LETTER O WITH TILDE AND DIAERESIS
        chars.append(0x1E4F)  #uni1E4F	LATIN SMALL LETTER O WITH TILDE AND DIAERESIS
        chars.append(0x1E50)  #uni1E50	LATIN CAPITAL LETTER O WITH MACRON AND GRAVE
        chars.append(0x1E51)  #uni1E51	LATIN SMALL LETTER O WITH MACRON AND GRAVE
        chars.append(0x1E52)  #uni1E52	LATIN CAPITAL LETTER O WITH MACRON AND ACUTE
        chars.append(0x1E53)  #uni1E53	LATIN SMALL LETTER O WITH MACRON AND ACUTE
        chars.append(0x1E54)  #uni1E54	LATIN CAPITAL LETTER P WITH ACUTE
        chars.append(0x1E55)  #uni1E55	LATIN SMALL LETTER P WITH ACUTE
        chars.append(0x1E56)  #uni1E56	LATIN CAPITAL LETTER P WITH DOT ABOVE
        chars.append(0x1E57)  #uni1E57	LATIN SMALL LETTER P WITH DOT ABOVE
        chars.append(0x1E58)  #uni1E58	LATIN CAPITAL LETTER R WITH DOT ABOVE
        chars.append(0x1E59)  #uni1E59	LATIN SMALL LETTER R WITH DOT ABOVE
        chars.append(0x1E5A)  #uni1E5A	LATIN CAPITAL LETTER R WITH DOT BELOW
        chars.append(0x1E5B)  #uni1E5B	LATIN SMALL LETTER R WITH DOT BELOW
        chars.append(0x1E5C)  #uni1E5C	LATIN CAPITAL LETTER R WITH DOT BELOW AND MACRON
        chars.append(0x1E5D)  #uni1E5D	LATIN SMALL LETTER R WITH DOT BELOW AND MACRON
        chars.append(0x1E5E)  #uni1E5E	LATIN CAPITAL LETTER R WITH LINE BELOW
        chars.append(0x1E5F)  #uni1E5F	LATIN SMALL LETTER R WITH LINE BELOW
        chars.append(0x1E60)  #uni1E60	LATIN CAPITAL LETTER S WITH DOT ABOVE
        chars.append(0x1E61)  #uni1E61	LATIN SMALL LETTER S WITH DOT ABOVE
        chars.append(0x1E62)  #uni1E62	LATIN CAPITAL LETTER S WITH DOT BELOW
        chars.append(0x1E63)  #uni1E63	LATIN SMALL LETTER S WITH DOT BELOW
        chars.append(0x1E64)  #uni1E64	LATIN CAPITAL LETTER S WITH ACUTE AND DOT ABOVE
        chars.append(0x1E65)  #uni1E65	LATIN SMALL LETTER S WITH ACUTE AND DOT ABOVE
        chars.append(0x1E66)  #uni1E66	LATIN CAPITAL LETTER S WITH CARON AND DOT ABOVE
        chars.append(0x1E67)  #uni1E67	LATIN SMALL LETTER S WITH CARON AND DOT ABOVE
        chars.append(0x1E68)  #uni1E68	LATIN CAPITAL LETTER S WITH DOT BELOW AND DOT ABOVE
        chars.append(0x1E69)  #uni1E69	LATIN SMALL LETTER S WITH DOT BELOW AND DOT ABOVE
        chars.append(0x1E6A)  #uni1E6A	LATIN CAPITAL LETTER T WITH DOT ABOVE
        chars.append(0x1E6B)  #uni1E6B	LATIN SMALL LETTER T WITH DOT ABOVE
        chars.append(0x1E6C)  #uni1E6C	LATIN CAPITAL LETTER T WITH DOT BELOW
        chars.append(0x1E6D)  #uni1E6D	LATIN SMALL LETTER T WITH DOT BELOW
        chars.append(0x1E6E)  #uni1E6E	LATIN CAPITAL LETTER T WITH LINE BELOW
        chars.append(0x1E6F)  #uni1E6F	LATIN SMALL LETTER T WITH LINE BELOW
        chars.append(0x1E70)  #uni1E70	LATIN CAPITAL LETTER T WITH CIRCUMFLEX BELOW
        chars.append(0x1E71)  #uni1E71	LATIN SMALL LETTER T WITH CIRCUMFLEX BELOW
        chars.append(0x1E72)  #uni1E72	LATIN CAPITAL LETTER U WITH DIAERESIS BELOW
        chars.append(0x1E73)  #uni1E73	LATIN SMALL LETTER U WITH DIAERESIS BELOW
        chars.append(0x1E74)  #uni1E74	LATIN CAPITAL LETTER U WITH TILDE BELOW
        chars.append(0x1E75)  #uni1E75	LATIN SMALL LETTER U WITH TILDE BELOW
        chars.append(0x1E76)  #uni1E76	LATIN CAPITAL LETTER U WITH CIRCUMFLEX BELOW
        chars.append(0x1E77)  #uni1E77	LATIN SMALL LETTER U WITH CIRCUMFLEX BELOW
        chars.append(0x1E78)  #uni1E78	LATIN CAPITAL LETTER U WITH TILDE AND ACUTE
        chars.append(0x1E79)  #uni1E79	LATIN SMALL LETTER U WITH TILDE AND ACUTE
        chars.append(0x1E7A)  #uni1E7A	LATIN CAPITAL LETTER U WITH MACRON AND DIAERESIS
        chars.append(0x1E7B)  #uni1E7B	LATIN SMALL LETTER U WITH MACRON AND DIAERESIS
        chars.append(0x1E7C)  #uni1E7C	LATIN CAPITAL LETTER V WITH TILDE
        chars.append(0x1E7D)  #uni1E7D	LATIN SMALL LETTER V WITH TILDE
        chars.append(0x1E7E)  #uni1E7E	LATIN CAPITAL LETTER V WITH DOT BELOW
        chars.append(0x1E7F)  #uni1E7F	LATIN SMALL LETTER V WITH DOT BELOW
        chars.append(0x1E80)  #Wgrave	LATIN CAPITAL LETTER W WITH GRAVE
        chars.append(0x1E81)  #wgrave	LATIN SMALL LETTER W WITH GRAVE
        chars.append(0x1E82)  #Wacute	LATIN CAPITAL LETTER W WITH ACUTE
        chars.append(0x1E83)  #wacute	LATIN SMALL LETTER W WITH ACUTE
        chars.append(0x1E84)  #Wdieresis	LATIN CAPITAL LETTER W WITH DIAERESIS
        chars.append(0x1E85)  #wdieresis	LATIN SMALL LETTER W WITH DIAERESIS
        chars.append(0x1E86)  #uni1E86	LATIN CAPITAL LETTER W WITH DOT ABOVE
        chars.append(0x1E87)  #uni1E87	LATIN SMALL LETTER W WITH DOT ABOVE
        chars.append(0x1E88)  #uni1E88	LATIN CAPITAL LETTER W WITH DOT BELOW
        chars.append(0x1E89)  #uni1E89	LATIN SMALL LETTER W WITH DOT BELOW
        chars.append(0x1E8A)  #uni1E8A	LATIN CAPITAL LETTER X WITH DOT ABOVE
        chars.append(0x1E8B)  #uni1E8B	LATIN SMALL LETTER X WITH DOT ABOVE
        chars.append(0x1E8C)  #uni1E8C	LATIN CAPITAL LETTER X WITH DIAERESIS
        chars.append(0x1E8D)  #uni1E8D	LATIN SMALL LETTER X WITH DIAERESIS
        chars.append(0x1E8E)  #uni1E8E	LATIN CAPITAL LETTER Y WITH DOT ABOVE
        chars.append(0x1E8F)  #uni1E8F	LATIN SMALL LETTER Y WITH DOT ABOVE
        chars.append(0x1E90)  #uni1E90	LATIN CAPITAL LETTER Z WITH CIRCUMFLEX
        chars.append(0x1E91)  #uni1E91	LATIN SMALL LETTER Z WITH CIRCUMFLEX
        chars.append(0x1E92)  #uni1E92	LATIN CAPITAL LETTER Z WITH DOT BELOW
        chars.append(0x1E93)  #uni1E93	LATIN SMALL LETTER Z WITH DOT BELOW
        chars.append(0x1E94)  #uni1E94	LATIN CAPITAL LETTER Z WITH LINE BELOW
        chars.append(0x1E95)  #uni1E95	LATIN SMALL LETTER Z WITH LINE BELOW
        chars.append(0x1E96)  #uni1E96	LATIN SMALL LETTER H WITH LINE BELOW
        chars.append(0x1E97)  #uni1E97	LATIN SMALL LETTER T WITH DIAERESIS
        chars.append(0x1E98)  #uni1E98	LATIN SMALL LETTER W WITH RING ABOVE
        chars.append(0x1E99)  #uni1E99	LATIN SMALL LETTER Y WITH RING ABOVE
        chars.append(0x1E9A)  #uni1E9A	LATIN SMALL LETTER A WITH RIGHT HALF RING
        chars.append(0x1E9B)  #uni1E9B	LATIN SMALL LETTER LONG S WITH DOT ABOVE
        chars.append(0x1E9E)  #uni1E9E	LATIN CAPITAL LETTER SHARP S
        chars.append(0x1EA0)  #Adotbelow	LATIN CAPITAL LETTER A WITH DOT BELOW
        chars.append(0x1EA1)  #adotbelow	LATIN SMALL LETTER A WITH DOT BELOW
        chars.append(0x1EA2)  #Ahookabove	LATIN CAPITAL LETTER A WITH HOOK ABOVE
        chars.append(0x1EA3)  #ahookabove	LATIN SMALL LETTER A WITH HOOK ABOVE
        chars.append(0x1EA4)  #Acircumflexacute	LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND ACUTE
        chars.append(0x1EA5)  #acircumflexacute	LATIN SMALL LETTER A WITH CIRCUMFLEX AND ACUTE
        chars.append(0x1EA6)  #Acircumflexgrave	LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND GRAVE
        chars.append(0x1EA7)  #acircumflexgrave	LATIN SMALL LETTER A WITH CIRCUMFLEX AND GRAVE
        chars.append(0x1EA8)  #Acircumflexhookabove	LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
        chars.append(0x1EA9)  #acircumflexhookabove	LATIN SMALL LETTER A WITH CIRCUMFLEX AND HOOK ABOVE
        chars.append(0x1EAA)  #Acircumflextilde	LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND TILDE
        chars.append(0x1EAB)  #acircumflextilde	LATIN SMALL LETTER A WITH CIRCUMFLEX AND TILDE
        chars.append(0x1EAC)  #Acircumflexdotbelow	LATIN CAPITAL LETTER A WITH CIRCUMFLEX AND DOT BELOW
        chars.append(0x1EAD)  #acircumflexdotbelow	LATIN SMALL LETTER A WITH CIRCUMFLEX AND DOT BELOW
        chars.append(0x1EAE)  #Abreveacute	LATIN CAPITAL LETTER A WITH BREVE AND ACUTE
        chars.append(0x1EAF)  #abreveacute	LATIN SMALL LETTER A WITH BREVE AND ACUTE
        chars.append(0x1EB0)  #Abrevegrave	LATIN CAPITAL LETTER A WITH BREVE AND GRAVE
        chars.append(0x1EB1)  #abrevegrave	LATIN SMALL LETTER A WITH BREVE AND GRAVE
        chars.append(0x1EB2)  #Abrevehookabove	LATIN CAPITAL LETTER A WITH BREVE AND HOOK ABOVE
        chars.append(0x1EB3)  #abrevehookabove	LATIN SMALL LETTER A WITH BREVE AND HOOK ABOVE
        chars.append(0x1EB4)  #Abrevetilde	LATIN CAPITAL LETTER A WITH BREVE AND TILDE
        chars.append(0x1EB5)  #abrevetilde	LATIN SMALL LETTER A WITH BREVE AND TILDE
        chars.append(0x1EB6)  #Abrevedotbelow	LATIN CAPITAL LETTER A WITH BREVE AND DOT BELOW
        chars.append(0x1EB7)  #abrevedotbelow	LATIN SMALL LETTER A WITH BREVE AND DOT BELOW
        chars.append(0x1EB8)  #Edotbelow	LATIN CAPITAL LETTER E WITH DOT BELOW
        chars.append(0x1EB9)  #edotbelow	LATIN SMALL LETTER E WITH DOT BELOW
        chars.append(0x1EBA)  #Ehookabove	LATIN CAPITAL LETTER E WITH HOOK ABOVE
        chars.append(0x1EBB)  #ehookabove	LATIN SMALL LETTER E WITH HOOK ABOVE
        chars.append(0x1EBC)  #Etilde	LATIN CAPITAL LETTER E WITH TILDE
        chars.append(0x1EBD)  #etilde	LATIN SMALL LETTER E WITH TILDE
        chars.append(0x1EBE)  #Ecircumflexacute	LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND ACUTE
        chars.append(0x1EBF)  #ecircumflexacute	LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE
        chars.append(0x1EC0)  #Ecircumflexgrave	LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND GRAVE
        chars.append(0x1EC1)  #ecircumflexgrave	LATIN SMALL LETTER E WITH CIRCUMFLEX AND GRAVE
        chars.append(0x1EC2)  #Ecircumflexhookabove	LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
        chars.append(0x1EC3)  #ecircumflexhookabove	LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE
        chars.append(0x1EC4)  #Ecircumflextilde	LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND TILDE
        chars.append(0x1EC5)  #ecircumflextilde	LATIN SMALL LETTER E WITH CIRCUMFLEX AND TILDE
        chars.append(0x1EC6)  #Ecircumflexdotbelow	LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND DOT BELOW
        chars.append(0x1EC7)  #ecircumflexdotbelow	LATIN SMALL LETTER E WITH CIRCUMFLEX AND DOT BELOW
        chars.append(0x1EC8)  #Ihookabove	LATIN CAPITAL LETTER I WITH HOOK ABOVE
        chars.append(0x1EC9)  #ihookabove	LATIN SMALL LETTER I WITH HOOK ABOVE
        chars.append(0x1ECA)  #Idotbelow	LATIN CAPITAL LETTER I WITH DOT BELOW
        chars.append(0x1ECB)  #idotbelow	LATIN SMALL LETTER I WITH DOT BELOW
        chars.append(0x1ECC)  #Odotbelow	LATIN CAPITAL LETTER O WITH DOT BELOW
        chars.append(0x1ECD)  #odotbelow	LATIN SMALL LETTER O WITH DOT BELOW
        chars.append(0x1ECE)  #Ohookabove	LATIN CAPITAL LETTER O WITH HOOK ABOVE
        chars.append(0x1ECF)  #ohookabove	LATIN SMALL LETTER O WITH HOOK ABOVE
        chars.append(0x1ED0)  #Ocircumflexacute	LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND ACUTE
        chars.append(0x1ED1)  #ocircumflexacute	LATIN SMALL LETTER O WITH CIRCUMFLEX AND ACUTE
        chars.append(0x1ED2)  #Ocircumflexgrave	LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND GRAVE
        chars.append(0x1ED3)  #ocircumflexgrave	LATIN SMALL LETTER O WITH CIRCUMFLEX AND GRAVE
        chars.append(0x1ED4)  #Ocircumflexhookabove	LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
        chars.append(0x1ED5)  #ocircumflexhookabove	LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE
        chars.append(0x1ED6)  #Ocircumflextilde	LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND TILDE
        chars.append(0x1ED7)  #ocircumflextilde	LATIN SMALL LETTER O WITH CIRCUMFLEX AND TILDE
        chars.append(0x1ED8)  #Ocircumflexdotbelow	LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND DOT BELOW
        chars.append(0x1ED9)  #ocircumflexdotbelow	LATIN SMALL LETTER O WITH CIRCUMFLEX AND DOT BELOW
        chars.append(0x1EDA)  #Ohornacute	LATIN CAPITAL LETTER O WITH HORN AND ACUTE
        chars.append(0x1EDB)  #ohornacute	LATIN SMALL LETTER O WITH HORN AND ACUTE
        chars.append(0x1EDC)  #Ohorngrave	LATIN CAPITAL LETTER O WITH HORN AND GRAVE
        chars.append(0x1EDD)  #ohorngrave	LATIN SMALL LETTER O WITH HORN AND GRAVE
        chars.append(0x1EDE)  #Ohornhookabove	LATIN CAPITAL LETTER O WITH HORN AND HOOK ABOVE
        chars.append(0x1EDF)  #ohornhookabove	LATIN SMALL LETTER O WITH HORN AND HOOK ABOVE
        chars.append(0x1EE0)  #Ohorntilde	LATIN CAPITAL LETTER O WITH HORN AND TILDE
        chars.append(0x1EE1)  #ohorntilde	LATIN SMALL LETTER O WITH HORN AND TILDE
        chars.append(0x1EE2)  #Ohorndotbelow	LATIN CAPITAL LETTER O WITH HORN AND DOT BELOW
        chars.append(0x1EE3)  #ohorndotbelow	LATIN SMALL LETTER O WITH HORN AND DOT BELOW
        chars.append(0x1EE4)  #Udotbelow	LATIN CAPITAL LETTER U WITH DOT BELOW
        chars.append(0x1EE5)  #udotbelow	LATIN SMALL LETTER U WITH DOT BELOW
        chars.append(0x1EE6)  #Uhookabove	LATIN CAPITAL LETTER U WITH HOOK ABOVE
        chars.append(0x1EE7)  #uhookabove	LATIN SMALL LETTER U WITH HOOK ABOVE
        chars.append(0x1EE8)  #Uhornacute	LATIN CAPITAL LETTER U WITH HORN AND ACUTE
        chars.append(0x1EE9)  #uhornacute	LATIN SMALL LETTER U WITH HORN AND ACUTE
        chars.append(0x1EEA)  #Uhorngrave	LATIN CAPITAL LETTER U WITH HORN AND GRAVE
        chars.append(0x1EEB)  #uhorngrave	LATIN SMALL LETTER U WITH HORN AND GRAVE
        chars.append(0x1EEC)  #Uhornhookabove	LATIN CAPITAL LETTER U WITH HORN AND HOOK ABOVE
        chars.append(0x1EED)  #uhornhookabove	LATIN SMALL LETTER U WITH HORN AND HOOK ABOVE
        chars.append(0x1EEE)  #Uhorntilde	LATIN CAPITAL LETTER U WITH HORN AND TILDE
        chars.append(0x1EEF)  #uhorntilde	LATIN SMALL LETTER U WITH HORN AND TILDE
        chars.append(0x1EF0)  #Uhorndotbelow	LATIN CAPITAL LETTER U WITH HORN AND DOT BELOW
        chars.append(0x1EF1)  #uhorndotbelow	LATIN SMALL LETTER U WITH HORN AND DOT BELOW
        chars.append(0x1EF2)  #Ygrave	LATIN CAPITAL LETTER Y WITH GRAVE
        chars.append(0x1EF3)  #ygrave	LATIN SMALL LETTER Y WITH GRAVE
        chars.append(0x1EF4)  #Ydotbelow	LATIN CAPITAL LETTER Y WITH DOT BELOW
        chars.append(0x1EF5)  #ydotbelow	LATIN SMALL LETTER Y WITH DOT BELOW
        chars.append(0x1EF6)  #Yhookabove	LATIN CAPITAL LETTER Y WITH HOOK ABOVE
        chars.append(0x1EF7)  #yhookabove	LATIN SMALL LETTER Y WITH HOOK ABOVE
        chars.append(0x1EF8)  #Ytilde	LATIN CAPITAL LETTER Y WITH TILDE
        chars.append(0x1EF9)  #ytilde	LATIN SMALL LETTER Y WITH TILDE
        chars.append(0x1F00)  #uni1F00	GREEK SMALL LETTER ALPHA WITH PSILI
        chars.append(0x1F01)  #uni1F01	GREEK SMALL LETTER ALPHA WITH DASIA
        chars.append(0x1F02)  #uni1F02	GREEK SMALL LETTER ALPHA WITH PSILI AND VARIA
        chars.append(0x1F03)  #uni1F03	GREEK SMALL LETTER ALPHA WITH DASIA AND VARIA
        chars.append(0x1F04)  #uni1F04	GREEK SMALL LETTER ALPHA WITH PSILI AND OXIA
        chars.append(0x1F05)  #uni1F05	GREEK SMALL LETTER ALPHA WITH DASIA AND OXIA
        chars.append(0x1F06)  #uni1F06	GREEK SMALL LETTER ALPHA WITH PSILI AND PERISPOMENI
        chars.append(0x1F07)  #uni1F07	GREEK SMALL LETTER ALPHA WITH DASIA AND PERISPOMENI
        chars.append(0x1F08)  #uni1F08	GREEK CAPITAL LETTER ALPHA WITH PSILI
        chars.append(0x1F09)  #uni1F09	GREEK CAPITAL LETTER ALPHA WITH DASIA
        chars.append(0x1F0A)  #uni1F0A	GREEK CAPITAL LETTER ALPHA WITH PSILI AND VARIA
        chars.append(0x1F0B)  #uni1F0B	GREEK CAPITAL LETTER ALPHA WITH DASIA AND VARIA
        chars.append(0x1F0C)  #uni1F0C	GREEK CAPITAL LETTER ALPHA WITH PSILI AND OXIA
        chars.append(0x1F0D)  #uni1F0D	GREEK CAPITAL LETTER ALPHA WITH DASIA AND OXIA
        chars.append(0x1F0E)  #uni1F0E	GREEK CAPITAL LETTER ALPHA WITH PSILI AND PERISPOMENI
        chars.append(0x1F0F)  #uni1F0F	GREEK CAPITAL LETTER ALPHA WITH DASIA AND PERISPOMENI
        chars.append(0x1F10)  #uni1F10	GREEK SMALL LETTER EPSILON WITH PSILI
        chars.append(0x1F11)  #uni1F11	GREEK SMALL LETTER EPSILON WITH DASIA
        chars.append(0x1F12)  #uni1F12	GREEK SMALL LETTER EPSILON WITH PSILI AND VARIA
        chars.append(0x1F13)  #uni1F13	GREEK SMALL LETTER EPSILON WITH DASIA AND VARIA
        chars.append(0x1F14)  #uni1F14	GREEK SMALL LETTER EPSILON WITH PSILI AND OXIA
        chars.append(0x1F15)  #uni1F15	GREEK SMALL LETTER EPSILON WITH DASIA AND OXIA
        chars.append(0x1F18)  #uni1F18	GREEK CAPITAL LETTER EPSILON WITH PSILI
        chars.append(0x1F19)  #uni1F19	GREEK CAPITAL LETTER EPSILON WITH DASIA
        chars.append(0x1F1A)  #uni1F1A	GREEK CAPITAL LETTER EPSILON WITH PSILI AND VARIA
        chars.append(0x1F1B)  #uni1F1B	GREEK CAPITAL LETTER EPSILON WITH DASIA AND VARIA
        chars.append(0x1F1C)  #uni1F1C	GREEK CAPITAL LETTER EPSILON WITH PSILI AND OXIA
        chars.append(0x1F1D)  #uni1F1D	GREEK CAPITAL LETTER EPSILON WITH DASIA AND OXIA
        chars.append(0x1F20)  #uni1F20	GREEK SMALL LETTER ETA WITH PSILI
        chars.append(0x1F21)  #uni1F21	GREEK SMALL LETTER ETA WITH DASIA
        chars.append(0x1F22)  #uni1F22	GREEK SMALL LETTER ETA WITH PSILI AND VARIA
        chars.append(0x1F23)  #uni1F23	GREEK SMALL LETTER ETA WITH DASIA AND VARIA
        chars.append(0x1F24)  #uni1F24	GREEK SMALL LETTER ETA WITH PSILI AND OXIA
        chars.append(0x1F25)  #uni1F25	GREEK SMALL LETTER ETA WITH DASIA AND OXIA
        chars.append(0x1F26)  #uni1F26	GREEK SMALL LETTER ETA WITH PSILI AND PERISPOMENI
        chars.append(0x1F27)  #uni1F27	GREEK SMALL LETTER ETA WITH DASIA AND PERISPOMENI
        chars.append(0x1F28)  #uni1F28	GREEK CAPITAL LETTER ETA WITH PSILI
        chars.append(0x1F29)  #uni1F29	GREEK CAPITAL LETTER ETA WITH DASIA
        chars.append(0x1F2A)  #uni1F2A	GREEK CAPITAL LETTER ETA WITH PSILI AND VARIA
        chars.append(0x1F2B)  #uni1F2B	GREEK CAPITAL LETTER ETA WITH DASIA AND VARIA
        chars.append(0x1F2C)  #uni1F2C	GREEK CAPITAL LETTER ETA WITH PSILI AND OXIA
        chars.append(0x1F2D)  #uni1F2D	GREEK CAPITAL LETTER ETA WITH DASIA AND OXIA
        chars.append(0x1F2E)  #uni1F2E	GREEK CAPITAL LETTER ETA WITH PSILI AND PERISPOMENI
        chars.append(0x1F2F)  #uni1F2F	GREEK CAPITAL LETTER ETA WITH DASIA AND PERISPOMENI
        chars.append(0x1F30)  #uni1F30	GREEK SMALL LETTER IOTA WITH PSILI
        chars.append(0x1F31)  #uni1F31	GREEK SMALL LETTER IOTA WITH DASIA
        chars.append(0x1F32)  #uni1F32	GREEK SMALL LETTER IOTA WITH PSILI AND VARIA
        chars.append(0x1F33)  #uni1F33	GREEK SMALL LETTER IOTA WITH DASIA AND VARIA
        chars.append(0x1F34)  #uni1F34	GREEK SMALL LETTER IOTA WITH PSILI AND OXIA
        chars.append(0x1F35)  #uni1F35	GREEK SMALL LETTER IOTA WITH DASIA AND OXIA
        chars.append(0x1F36)  #uni1F36	GREEK SMALL LETTER IOTA WITH PSILI AND PERISPOMENI
        chars.append(0x1F37)  #uni1F37	GREEK SMALL LETTER IOTA WITH DASIA AND PERISPOMENI
        chars.append(0x1F38)  #uni1F38	GREEK CAPITAL LETTER IOTA WITH PSILI
        chars.append(0x1F39)  #uni1F39	GREEK CAPITAL LETTER IOTA WITH DASIA
        chars.append(0x1F3A)  #uni1F3A	GREEK CAPITAL LETTER IOTA WITH PSILI AND VARIA
        chars.append(0x1F3B)  #uni1F3B	GREEK CAPITAL LETTER IOTA WITH DASIA AND VARIA
        chars.append(0x1F3C)  #uni1F3C	GREEK CAPITAL LETTER IOTA WITH PSILI AND OXIA
        chars.append(0x1F3D)  #uni1F3D	GREEK CAPITAL LETTER IOTA WITH DASIA AND OXIA
        chars.append(0x1F3E)  #uni1F3E	GREEK CAPITAL LETTER IOTA WITH PSILI AND PERISPOMENI
        chars.append(0x1F3F)  #uni1F3F	GREEK CAPITAL LETTER IOTA WITH DASIA AND PERISPOMENI
        chars.append(0x1F40)  #uni1F40	GREEK SMALL LETTER OMICRON WITH PSILI
        chars.append(0x1F41)  #uni1F41	GREEK SMALL LETTER OMICRON WITH DASIA
        chars.append(0x1F42)  #uni1F42	GREEK SMALL LETTER OMICRON WITH PSILI AND VARIA
        chars.append(0x1F43)  #uni1F43	GREEK SMALL LETTER OMICRON WITH DASIA AND VARIA
        chars.append(0x1F44)  #uni1F44	GREEK SMALL LETTER OMICRON WITH PSILI AND OXIA
        chars.append(0x1F45)  #uni1F45	GREEK SMALL LETTER OMICRON WITH DASIA AND OXIA
        chars.append(0x1F48)  #uni1F48	GREEK CAPITAL LETTER OMICRON WITH PSILI
        chars.append(0x1F49)  #uni1F49	GREEK CAPITAL LETTER OMICRON WITH DASIA
        chars.append(0x1F4A)  #uni1F4A	GREEK CAPITAL LETTER OMICRON WITH PSILI AND VARIA
        chars.append(0x1F4B)  #uni1F4B	GREEK CAPITAL LETTER OMICRON WITH DASIA AND VARIA
        chars.append(0x1F4C)  #uni1F4C	GREEK CAPITAL LETTER OMICRON WITH PSILI AND OXIA
        chars.append(0x1F4D)  #uni1F4D	GREEK CAPITAL LETTER OMICRON WITH DASIA AND OXIA
        chars.append(0x1F50)  #uni1F50	GREEK SMALL LETTER UPSILON WITH PSILI
        chars.append(0x1F51)  #uni1F51	GREEK SMALL LETTER UPSILON WITH DASIA
        chars.append(0x1F52)  #uni1F52	GREEK SMALL LETTER UPSILON WITH PSILI AND VARIA
        chars.append(0x1F53)  #uni1F53	GREEK SMALL LETTER UPSILON WITH DASIA AND VARIA
        chars.append(0x1F54)  #uni1F54	GREEK SMALL LETTER UPSILON WITH PSILI AND OXIA
        chars.append(0x1F55)  #uni1F55	GREEK SMALL LETTER UPSILON WITH DASIA AND OXIA
        chars.append(0x1F56)  #uni1F56	GREEK SMALL LETTER UPSILON WITH PSILI AND PERISPOMENI
        chars.append(0x1F57)  #uni1F57	GREEK SMALL LETTER UPSILON WITH DASIA AND PERISPOMENI
        chars.append(0x1F59)  #uni1F59	GREEK CAPITAL LETTER UPSILON WITH DASIA
        chars.append(0x1F5B)  #uni1F5B	GREEK CAPITAL LETTER UPSILON WITH DASIA AND VARIA
        chars.append(0x1F5D)  #uni1F5D	GREEK CAPITAL LETTER UPSILON WITH DASIA AND OXIA
        chars.append(0x1F5F)  #uni1F5F	GREEK CAPITAL LETTER UPSILON WITH DASIA AND PERISPOMENI
        chars.append(0x1F60)  #uni1F60	GREEK SMALL LETTER OMEGA WITH PSILI
        chars.append(0x1F61)  #uni1F61	GREEK SMALL LETTER OMEGA WITH DASIA
        chars.append(0x1F62)  #uni1F62	GREEK SMALL LETTER OMEGA WITH PSILI AND VARIA
        chars.append(0x1F63)  #uni1F63	GREEK SMALL LETTER OMEGA WITH DASIA AND VARIA
        chars.append(0x1F64)  #uni1F64	GREEK SMALL LETTER OMEGA WITH PSILI AND OXIA
        chars.append(0x1F65)  #uni1F65	GREEK SMALL LETTER OMEGA WITH DASIA AND OXIA
        chars.append(0x1F66)  #uni1F66	GREEK SMALL LETTER OMEGA WITH PSILI AND PERISPOMENI
        chars.append(0x1F67)  #uni1F67	GREEK SMALL LETTER OMEGA WITH DASIA AND PERISPOMENI
        chars.append(0x1F68)  #uni1F68	GREEK CAPITAL LETTER OMEGA WITH PSILI
        chars.append(0x1F69)  #uni1F69	GREEK CAPITAL LETTER OMEGA WITH DASIA
        chars.append(0x1F6A)  #uni1F6A	GREEK CAPITAL LETTER OMEGA WITH PSILI AND VARIA
        chars.append(0x1F6B)  #uni1F6B	GREEK CAPITAL LETTER OMEGA WITH DASIA AND VARIA
        chars.append(0x1F6C)  #uni1F6C	GREEK CAPITAL LETTER OMEGA WITH PSILI AND OXIA
        chars.append(0x1F6D)  #uni1F6D	GREEK CAPITAL LETTER OMEGA WITH DASIA AND OXIA
        chars.append(0x1F6E)  #uni1F6E	GREEK CAPITAL LETTER OMEGA WITH PSILI AND PERISPOMENI
        chars.append(0x1F6F)  #uni1F6F	GREEK CAPITAL LETTER OMEGA WITH DASIA AND PERISPOMENI
        chars.append(0x1F70)  #uni1F70	GREEK SMALL LETTER ALPHA WITH VARIA
        chars.append(0x1F71)  #uni1F71	GREEK SMALL LETTER ALPHA WITH OXIA
        chars.append(0x1F72)  #uni1F72	GREEK SMALL LETTER EPSILON WITH VARIA
        chars.append(0x1F73)  #uni1F73	GREEK SMALL LETTER EPSILON WITH OXIA
        chars.append(0x1F74)  #uni1F74	GREEK SMALL LETTER ETA WITH VARIA
        chars.append(0x1F75)  #uni1F75	GREEK SMALL LETTER ETA WITH OXIA
        chars.append(0x1F76)  #uni1F76	GREEK SMALL LETTER IOTA WITH VARIA
        chars.append(0x1F77)  #uni1F77	GREEK SMALL LETTER IOTA WITH OXIA
        chars.append(0x1F78)  #uni1F78	GREEK SMALL LETTER OMICRON WITH VARIA
        chars.append(0x1F79)  #uni1F79	GREEK SMALL LETTER OMICRON WITH OXIA
        chars.append(0x1F7A)  #uni1F7A	GREEK SMALL LETTER UPSILON WITH VARIA
        chars.append(0x1F7B)  #uni1F7B	GREEK SMALL LETTER UPSILON WITH OXIA
        chars.append(0x1F7C)  #uni1F7C	GREEK SMALL LETTER OMEGA WITH VARIA
        chars.append(0x1F7D)  #uni1F7D	GREEK SMALL LETTER OMEGA WITH OXIA
        chars.append(0x1F80)  #uni1F80	GREEK SMALL LETTER ALPHA WITH PSILI AND YPOGEGRAMMENI
        chars.append(0x1F81)  #uni1F81	GREEK SMALL LETTER ALPHA WITH DASIA AND YPOGEGRAMMENI
        chars.append(0x1F82)  #uni1F82	GREEK SMALL LETTER ALPHA WITH PSILI AND VARIA AND YPOGEGRAMMENI
        chars.append(0x1F83)  #uni1F83	GREEK SMALL LETTER ALPHA WITH DASIA AND VARIA AND YPOGEGRAMMENI
        chars.append(0x1F84)  #uni1F84	GREEK SMALL LETTER ALPHA WITH PSILI AND OXIA AND YPOGEGRAMMENI
        chars.append(0x1F85)  #uni1F85	GREEK SMALL LETTER ALPHA WITH DASIA AND OXIA AND YPOGEGRAMMENI
        chars.append(0x1F86)  #uni1F86	GREEK SMALL LETTER ALPHA WITH PSILI AND PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1F87)  #uni1F87	GREEK SMALL LETTER ALPHA WITH DASIA AND PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1F88)  #uni1F88	GREEK CAPITAL LETTER ALPHA WITH PSILI AND PROSGEGRAMMENI
        chars.append(0x1F89)  #uni1F89	GREEK CAPITAL LETTER ALPHA WITH DASIA AND PROSGEGRAMMENI
        chars.append(0x1F8A)  #uni1F8A	GREEK CAPITAL LETTER ALPHA WITH PSILI AND VARIA AND PROSGEGRAMMENI
        chars.append(0x1F8B)  #uni1F8B	GREEK CAPITAL LETTER ALPHA WITH DASIA AND VARIA AND PROSGEGRAMMENI
        chars.append(0x1F8C)  #uni1F8C	GREEK CAPITAL LETTER ALPHA WITH PSILI AND OXIA AND PROSGEGRAMMENI
        chars.append(0x1F8D)  #uni1F8D	GREEK CAPITAL LETTER ALPHA WITH DASIA AND OXIA AND PROSGEGRAMMENI
        chars.append(0x1F8E)  #uni1F8E	GREEK CAPITAL LETTER ALPHA WITH PSILI AND PERISPOMENI AND PROSGEGRAMMENI
        chars.append(0x1F8F)  #uni1F8F	GREEK CAPITAL LETTER ALPHA WITH DASIA AND PERISPOMENI AND PROSGEGRAMMENI
        chars.append(0x1F90)  #uni1F90	GREEK SMALL LETTER ETA WITH PSILI AND YPOGEGRAMMENI
        chars.append(0x1F91)  #uni1F91	GREEK SMALL LETTER ETA WITH DASIA AND YPOGEGRAMMENI
        chars.append(0x1F92)  #uni1F92	GREEK SMALL LETTER ETA WITH PSILI AND VARIA AND YPOGEGRAMMENI
        chars.append(0x1F93)  #uni1F93	GREEK SMALL LETTER ETA WITH DASIA AND VARIA AND YPOGEGRAMMENI
        chars.append(0x1F94)  #uni1F94	GREEK SMALL LETTER ETA WITH PSILI AND OXIA AND YPOGEGRAMMENI
        chars.append(0x1F95)  #uni1F95	GREEK SMALL LETTER ETA WITH DASIA AND OXIA AND YPOGEGRAMMENI
        chars.append(0x1F96)  #uni1F96	GREEK SMALL LETTER ETA WITH PSILI AND PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1F97)  #uni1F97	GREEK SMALL LETTER ETA WITH DASIA AND PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1F98)  #uni1F98	GREEK CAPITAL LETTER ETA WITH PSILI AND PROSGEGRAMMENI
        chars.append(0x1F99)  #uni1F99	GREEK CAPITAL LETTER ETA WITH DASIA AND PROSGEGRAMMENI
        chars.append(0x1F9A)  #uni1F9A	GREEK CAPITAL LETTER ETA WITH PSILI AND VARIA AND PROSGEGRAMMENI
        chars.append(0x1F9B)  #uni1F9B	GREEK CAPITAL LETTER ETA WITH DASIA AND VARIA AND PROSGEGRAMMENI
        chars.append(0x1F9C)  #uni1F9C	GREEK CAPITAL LETTER ETA WITH PSILI AND OXIA AND PROSGEGRAMMENI
        chars.append(0x1F9D)  #uni1F9D	GREEK CAPITAL LETTER ETA WITH DASIA AND OXIA AND PROSGEGRAMMENI
        chars.append(0x1F9E)  #uni1F9E	GREEK CAPITAL LETTER ETA WITH PSILI AND PERISPOMENI AND PROSGEGRAMMENI
        chars.append(0x1F9F)  #uni1F9F	GREEK CAPITAL LETTER ETA WITH DASIA AND PERISPOMENI AND PROSGEGRAMMENI
        chars.append(0x1FA0)  #uni1FA0	GREEK SMALL LETTER OMEGA WITH PSILI AND YPOGEGRAMMENI
        chars.append(0x1FA1)  #uni1FA1	GREEK SMALL LETTER OMEGA WITH DASIA AND YPOGEGRAMMENI
        chars.append(0x1FA2)  #uni1FA2	GREEK SMALL LETTER OMEGA WITH PSILI AND VARIA AND YPOGEGRAMMENI
        chars.append(0x1FA3)  #uni1FA3	GREEK SMALL LETTER OMEGA WITH DASIA AND VARIA AND YPOGEGRAMMENI
        chars.append(0x1FA4)  #uni1FA4	GREEK SMALL LETTER OMEGA WITH PSILI AND OXIA AND YPOGEGRAMMENI
        chars.append(0x1FA5)  #uni1FA5	GREEK SMALL LETTER OMEGA WITH DASIA AND OXIA AND YPOGEGRAMMENI
        chars.append(0x1FA6)  #uni1FA6	GREEK SMALL LETTER OMEGA WITH PSILI AND PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1FA7)  #uni1FA7	GREEK SMALL LETTER OMEGA WITH DASIA AND PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1FA8)  #uni1FA8	GREEK CAPITAL LETTER OMEGA WITH PSILI AND PROSGEGRAMMENI
        chars.append(0x1FA9)  #uni1FA9	GREEK CAPITAL LETTER OMEGA WITH DASIA AND PROSGEGRAMMENI
        chars.append(0x1FAA)  #uni1FAA	GREEK CAPITAL LETTER OMEGA WITH PSILI AND VARIA AND PROSGEGRAMMENI
        chars.append(0x1FAB)  #uni1FAB	GREEK CAPITAL LETTER OMEGA WITH DASIA AND VARIA AND PROSGEGRAMMENI
        chars.append(0x1FAC)  #uni1FAC	GREEK CAPITAL LETTER OMEGA WITH PSILI AND OXIA AND PROSGEGRAMMENI
        chars.append(0x1FAD)  #uni1FAD	GREEK CAPITAL LETTER OMEGA WITH DASIA AND OXIA AND PROSGEGRAMMENI
        chars.append(0x1FAE)  #uni1FAE	GREEK CAPITAL LETTER OMEGA WITH PSILI AND PERISPOMENI AND PROSGEGRAMMENI
        chars.append(0x1FAF)  #uni1FAF	GREEK CAPITAL LETTER OMEGA WITH DASIA AND PERISPOMENI AND PROSGEGRAMMENI
        chars.append(0x1FB0)  #uni1FB0	GREEK SMALL LETTER ALPHA WITH VRACHY
        chars.append(0x1FB1)  #uni1FB1	GREEK SMALL LETTER ALPHA WITH MACRON
        chars.append(0x1FB2)  #uni1FB2	GREEK SMALL LETTER ALPHA WITH VARIA AND YPOGEGRAMMENI
        chars.append(0x1FB3)  #uni1FB3	GREEK SMALL LETTER ALPHA WITH YPOGEGRAMMENI
        chars.append(0x1FB4)  #uni1FB4	GREEK SMALL LETTER ALPHA WITH OXIA AND YPOGEGRAMMENI
        chars.append(0x1FB6)  #uni1FB6	GREEK SMALL LETTER ALPHA WITH PERISPOMENI
        chars.append(0x1FB7)  #uni1FB7	GREEK SMALL LETTER ALPHA WITH PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1FB8)  #uni1FB8	GREEK CAPITAL LETTER ALPHA WITH VRACHY
        chars.append(0x1FB9)  #uni1FB9	GREEK CAPITAL LETTER ALPHA WITH MACRON
        chars.append(0x1FBA)  #uni1FBA	GREEK CAPITAL LETTER ALPHA WITH VARIA
        chars.append(0x1FBB)  #uni1FBB	GREEK CAPITAL LETTER ALPHA WITH OXIA
        chars.append(0x1FBC)  #uni1FBC	GREEK CAPITAL LETTER ALPHA WITH PROSGEGRAMMENI
        chars.append(0x1FBD)  #uni1FBD	GREEK KORONIS
        chars.append(0x1FBE)  #uni1FBE	GREEK PROSGEGRAMMENI
        chars.append(0x1FBF)  #uni1FBF	GREEK PSILI
        chars.append(0x1FC0)  #uni1FC0	GREEK PERISPOMENI
        chars.append(0x1FC1)  #uni1FC1	GREEK DIALYTIKA AND PERISPOMENI
        chars.append(0x1FC2)  #uni1FC2	GREEK SMALL LETTER ETA WITH VARIA AND YPOGEGRAMMENI
        chars.append(0x1FC3)  #uni1FC3	GREEK SMALL LETTER ETA WITH YPOGEGRAMMENI
        chars.append(0x1FC4)  #uni1FC4	GREEK SMALL LETTER ETA WITH OXIA AND YPOGEGRAMMENI
        chars.append(0x1FC6)  #uni1FC6	GREEK SMALL LETTER ETA WITH PERISPOMENI
        chars.append(0x1FC7)  #uni1FC7	GREEK SMALL LETTER ETA WITH PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1FC8)  #uni1FC8	GREEK CAPITAL LETTER EPSILON WITH VARIA
        chars.append(0x1FC9)  #uni1FC9	GREEK CAPITAL LETTER EPSILON WITH OXIA
        chars.append(0x1FCA)  #uni1FCA	GREEK CAPITAL LETTER ETA WITH VARIA
        chars.append(0x1FCB)  #uni1FCB	GREEK CAPITAL LETTER ETA WITH OXIA
        chars.append(0x1FCC)  #uni1FCC	GREEK CAPITAL LETTER ETA WITH PROSGEGRAMMENI
        chars.append(0x1FCD)  #uni1FCD	GREEK PSILI AND VARIA
        chars.append(0x1FCE)  #uni1FCE	GREEK PSILI AND OXIA
        chars.append(0x1FCF)  #uni1FCF	GREEK PSILI AND PERISPOMENI
        chars.append(0x1FD0)  #uni1FD0	GREEK SMALL LETTER IOTA WITH VRACHY
        chars.append(0x1FD1)  #uni1FD1	GREEK SMALL LETTER IOTA WITH MACRON
        chars.append(0x1FD2)  #uni1FD2	GREEK SMALL LETTER IOTA WITH DIALYTIKA AND VARIA
        chars.append(0x1FD3)  #uni1FD3	GREEK SMALL LETTER IOTA WITH DIALYTIKA AND OXIA
        chars.append(0x1FD6)  #uni1FD6	GREEK SMALL LETTER IOTA WITH PERISPOMENI
        chars.append(0x1FD7)  #uni1FD7	GREEK SMALL LETTER IOTA WITH DIALYTIKA AND PERISPOMENI
        chars.append(0x1FD8)  #uni1FD8	GREEK CAPITAL LETTER IOTA WITH VRACHY
        chars.append(0x1FD9)  #uni1FD9	GREEK CAPITAL LETTER IOTA WITH MACRON
        chars.append(0x1FDA)  #uni1FDA	GREEK CAPITAL LETTER IOTA WITH VARIA
        chars.append(0x1FDB)  #uni1FDB	GREEK CAPITAL LETTER IOTA WITH OXIA
        chars.append(0x1FDD)  #uni1FDD	GREEK DASIA AND VARIA
        chars.append(0x1FDE)  #uni1FDE	GREEK DASIA AND OXIA
        chars.append(0x1FDF)  #uni1FDF	GREEK DASIA AND PERISPOMENI
        chars.append(0x1FE0)  #uni1FE0	GREEK SMALL LETTER UPSILON WITH VRACHY
        chars.append(0x1FE1)  #uni1FE1	GREEK SMALL LETTER UPSILON WITH MACRON
        chars.append(0x1FE2)  #uni1FE2	GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND VARIA
        chars.append(0x1FE3)  #uni1FE3	GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND OXIA
        chars.append(0x1FE4)  #uni1FE4	GREEK SMALL LETTER RHO WITH PSILI
        chars.append(0x1FE5)  #uni1FE5	GREEK SMALL LETTER RHO WITH DASIA
        chars.append(0x1FE6)  #uni1FE6	GREEK SMALL LETTER UPSILON WITH PERISPOMENI
        chars.append(0x1FE7)  #uni1FE7	GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND PERISPOMENI
        chars.append(0x1FE8)  #uni1FE8	GREEK CAPITAL LETTER UPSILON WITH VRACHY
        chars.append(0x1FE9)  #uni1FE9	GREEK CAPITAL LETTER UPSILON WITH MACRON
        chars.append(0x1FEA)  #uni1FEA	GREEK CAPITAL LETTER UPSILON WITH VARIA
        chars.append(0x1FEB)  #uni1FEB	GREEK CAPITAL LETTER UPSILON WITH OXIA
        chars.append(0x1FEC)  #uni1FEC	GREEK CAPITAL LETTER RHO WITH DASIA
        chars.append(0x1FED)  #uni1FED	GREEK DIALYTIKA AND VARIA
        chars.append(0x1FEE)  #uni1FEE	GREEK DIALYTIKA AND OXIA
        chars.append(0x1FEF)  #uni1FEF	GREEK VARIA
        chars.append(0x1FF2)  #uni1FF2	GREEK SMALL LETTER OMEGA WITH VARIA AND YPOGEGRAMMENI
        chars.append(0x1FF3)  #uni1FF3	GREEK SMALL LETTER OMEGA WITH YPOGEGRAMMENI
        chars.append(0x1FF4)  #uni1FF4	GREEK SMALL LETTER OMEGA WITH OXIA AND YPOGEGRAMMENI
        chars.append(0x1FF6)  #uni1FF6	GREEK SMALL LETTER OMEGA WITH PERISPOMENI
        chars.append(0x1FF7)  #uni1FF7	GREEK SMALL LETTER OMEGA WITH PERISPOMENI AND YPOGEGRAMMENI
        chars.append(0x1FF8)  #uni1FF8	GREEK CAPITAL LETTER OMICRON WITH VARIA
        chars.append(0x1FF9)  #uni1FF9	GREEK CAPITAL LETTER OMICRON WITH OXIA
        chars.append(0x1FFA)  #uni1FFA	GREEK CAPITAL LETTER OMEGA WITH VARIA
        chars.append(0x1FFB)  #uni1FFB	GREEK CAPITAL LETTER OMEGA WITH OXIA
        chars.append(0x1FFC)  #uni1FFC	GREEK CAPITAL LETTER OMEGA WITH PROSGEGRAMMENI
        chars.append(0x1FFD)  #uni1FFD	GREEK OXIA
        chars.append(0x1FFE)  #uni1FFE	GREEK DASIA
        return chars


