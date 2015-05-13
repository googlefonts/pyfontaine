# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansDevanagari-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uni0000	????
        chars.append(0xA8E4)  #uniA8E4	COMBINING DEVANAGARI DIGIT FOUR
        chars.append(0xA8E7)  #uniA8E7	COMBINING DEVANAGARI DIGIT SEVEN
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
        chars.append(0x1CD7)  #uni1CD7	VEDIC TONE YAJURVEDIC KATHAKA INDEPENDENT SVARITA
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
        chars.append(0xA8E6)  #uniA8E6	COMBINING DEVANAGARI DIGIT SIX
        chars.append(0xA8E5)  #uniA8E5	COMBINING DEVANAGARI DIGIT FIVE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0xA831)  #uniA831	NORTH INDIC FRACTION ONE HALF
        chars.append(0x005B)  #bracketleft	LEFT SQUARE BRACKET
        chars.append(0x005C)  #backslash	REVERSE SOLIDUS
        chars.append(0x005D)  #bracketright	RIGHT SQUARE BRACKET
        chars.append(0x005E)  #asciicircum	CIRCUMFLEX ACCENT
        chars.append(0x005F)  #underscore	LOW LINE
        chars.append(0xA833)  #uniA833	NORTH INDIC FRACTION ONE SIXTEENTH
        chars.append(0xA8F0)  #uniA8F0	COMBINING DEVANAGARI LETTER VI
        chars.append(0x007B)  #braceleft	LEFT CURLY BRACKET
        chars.append(0x007C)  #bar	VERTICAL LINE
        chars.append(0x007D)  #braceright	RIGHT CURLY BRACKET
        chars.append(0x007E)  #asciitilde	TILDE
        chars.append(0xA8E9)  #uniA8E9	COMBINING DEVANAGARI DIGIT NINE
        chars.append(0xA8E8)  #uniA8E8	COMBINING DEVANAGARI DIGIT EIGHT
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xA830)  #uniA830	NORTH INDIC FRACTION ONE QUARTER
        chars.append(0x00AF)  #macron	MACRON
        chars.append(0xA8EF)  #uniA8EF	COMBINING DEVANAGARI LETTER RA
        chars.append(0x20B9)  #uni20B9	????
        chars.append(0x02BC)  #uni02BC	MODIFIER LETTER APOSTROPHE
        chars.append(0x1CD0)  #uni1CD0	VEDIC TONE KARSHANA
        chars.append(0x1CD1)  #uni1CD1	VEDIC TONE SHARA
        chars.append(0x1CD2)  #uni1CD2	VEDIC TONE PRENKHA
        chars.append(0x1CD3)  #uni1CD3	VEDIC SIGN NIHSHVASA
        chars.append(0x1CD4)  #uni1CD4	VEDIC SIGN YAJURVEDIC MIDLINE SVARITA
        chars.append(0x1CD5)  #uni1CD5	VEDIC TONE YAJURVEDIC AGGRAVATED INDEPENDENT SVARITA
        chars.append(0x1CD6)  #uni1CD6	VEDIC TONE YAJURVEDIC INDEPENDENT SVARITA
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x1CD8)  #uni1CD8	VEDIC TONE CANDRA BELOW
        chars.append(0x1CD9)  #uni1CD9	VEDIC TONE YAJURVEDIC KATHAKA INDEPENDENT SVARITA SCHROEDER
        chars.append(0x1CDA)  #uni1CDA	VEDIC TONE DOUBLE SVARITA
        chars.append(0x1CDB)  #uni1CDB	VEDIC TONE TRIPLE SVARITA
        chars.append(0x1CDC)  #uni1CDC	VEDIC TONE KATHAKA ANUDATTA
        chars.append(0x1CDD)  #uni1CDD	VEDIC TONE DOT BELOW
        chars.append(0x1CDE)  #uni1CDE	VEDIC TONE TWO DOTS BELOW
        chars.append(0x1CDF)  #uni1CDF	VEDIC TONE THREE DOTS BELOW
        chars.append(0x1CE0)  #uni1CE0	VEDIC TONE RIGVEDIC KASHMIRI INDEPENDENT SVARITA
        chars.append(0x1CE1)  #uni1CE1	VEDIC TONE ATHARVAVEDIC INDEPENDENT SVARITA
        chars.append(0x1CE2)  #uni1CE2	VEDIC SIGN VISARGA SVARITA
        chars.append(0x1CE3)  #uni1CE3	VEDIC SIGN VISARGA UDATTA
        chars.append(0x1CE4)  #uni1CE4	VEDIC SIGN REVERSED VISARGA UDATTA
        chars.append(0x1CE5)  #uni1CE5	VEDIC SIGN VISARGA ANUDATTA
        chars.append(0x1CE6)  #uni1CE6	VEDIC SIGN REVERSED VISARGA ANUDATTA
        chars.append(0x1CE7)  #uni1CE7	VEDIC SIGN VISARGA UDATTA WITH TAIL
        chars.append(0x1CE8)  #uni1CE8	VEDIC SIGN VISARGA ANUDATTA WITH TAIL
        chars.append(0x1CE9)  #uni1CE9	VEDIC SIGN ANUSVARA ANTARGOMUKHA
        chars.append(0x1CEA)  #uni1CEA	VEDIC SIGN ANUSVARA BAHIRGOMUKHA
        chars.append(0x1CEB)  #uni1CEB	VEDIC SIGN ANUSVARA VAMAGOMUKHA
        chars.append(0x1CEC)  #uni1CEC	VEDIC SIGN ANUSVARA VAMAGOMUKHA WITH TAIL
        chars.append(0x1CED)  #uni1CED	VEDIC SIGN TIRYAK
        chars.append(0x1CEE)  #uni1CEE	VEDIC SIGN HEXIFORM LONG ANUSVARA
        chars.append(0x1CEF)  #uni1CEF	VEDIC SIGN LONG ANUSVARA
        chars.append(0x1CF0)  #uni1CF0	VEDIC SIGN RTHANG LONG ANUSVARA
        chars.append(0x1CF1)  #uni1CF1	VEDIC SIGN ANUSVARA UBHAYATO MUKHA
        chars.append(0x1CF2)  #uni1CF2	VEDIC SIGN ARDHAVISARGA
        chars.append(0x1CF3)  #uni1CF3	????
        chars.append(0x1CF4)  #uni1CF4	????
        chars.append(0x1CF5)  #uni1CF5	????
        chars.append(0x1CF6)  #uni1CF6	????
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0xA8F8)  #uniA8F8	DEVANAGARI SIGN PUSHPIKA
        chars.append(0xA8F9)  #uniA8F9	DEVANAGARI GAP FILLER
        chars.append(0xA8FA)  #uniA8FA	DEVANAGARI CARET
        chars.append(0xA8FB)  #uniA8FB	DEVANAGARI HEADSTROKE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0900)  #uni0900	DEVANAGARI SIGN INVERTED CANDRABINDU
        chars.append(0x0901)  #uni0901	DEVANAGARI SIGN CANDRABINDU
        chars.append(0x0902)  #uni0902	DEVANAGARI SIGN ANUSVARA
        chars.append(0x0903)  #uni0903	DEVANAGARI SIGN VISARGA
        chars.append(0x0904)  #uni0904	DEVANAGARI LETTER SHORT A
        chars.append(0x0905)  #uni0905	DEVANAGARI LETTER A
        chars.append(0x0906)  #uni0906	DEVANAGARI LETTER AA
        chars.append(0x0907)  #uni0907	DEVANAGARI LETTER I
        chars.append(0x0908)  #uni0908	DEVANAGARI LETTER II
        chars.append(0x0909)  #uni0909	DEVANAGARI LETTER U
        chars.append(0x090A)  #uni090A	DEVANAGARI LETTER UU
        chars.append(0x090B)  #uni090B	DEVANAGARI LETTER VOCALIC R
        chars.append(0x090C)  #uni090C	DEVANAGARI LETTER VOCALIC L
        chars.append(0x090D)  #uni090D	DEVANAGARI LETTER CANDRA E
        chars.append(0x090E)  #uni090E	DEVANAGARI LETTER SHORT E
        chars.append(0x090F)  #uni090F	DEVANAGARI LETTER E
        chars.append(0x0910)  #uni0910	DEVANAGARI LETTER AI
        chars.append(0x0911)  #uni0911	DEVANAGARI LETTER CANDRA O
        chars.append(0x0912)  #uni0912	DEVANAGARI LETTER SHORT O
        chars.append(0x0913)  #uni0913	DEVANAGARI LETTER O
        chars.append(0x0914)  #uni0914	DEVANAGARI LETTER AU
        chars.append(0x0915)  #uni0915	DEVANAGARI LETTER KA
        chars.append(0x0916)  #uni0916	DEVANAGARI LETTER KHA
        chars.append(0x0917)  #uni0917	DEVANAGARI LETTER GA
        chars.append(0x0918)  #uni0918	DEVANAGARI LETTER GHA
        chars.append(0x0919)  #uni0919	DEVANAGARI LETTER NGA
        chars.append(0x091A)  #uni091A	DEVANAGARI LETTER CA
        chars.append(0x091B)  #uni091B	DEVANAGARI LETTER CHA
        chars.append(0x091C)  #uni091C	DEVANAGARI LETTER JA
        chars.append(0x091D)  #uni091D	DEVANAGARI LETTER JHA
        chars.append(0x091E)  #uni091E	DEVANAGARI LETTER NYA
        chars.append(0x091F)  #uni091F	DEVANAGARI LETTER TTA
        chars.append(0x0920)  #uni0920	DEVANAGARI LETTER TTHA
        chars.append(0x0921)  #uni0921	DEVANAGARI LETTER DDA
        chars.append(0x0922)  #uni0922	DEVANAGARI LETTER DDHA
        chars.append(0x0923)  #uni0923	DEVANAGARI LETTER NNA
        chars.append(0x0924)  #uni0924	DEVANAGARI LETTER TA
        chars.append(0x0925)  #uni0925	DEVANAGARI LETTER THA
        chars.append(0x0926)  #uni0926	DEVANAGARI LETTER DA
        chars.append(0x0927)  #uni0927	DEVANAGARI LETTER DHA
        chars.append(0x0928)  #uni0928	DEVANAGARI LETTER NA
        chars.append(0x0929)  #uni0929	DEVANAGARI LETTER NNNA
        chars.append(0x092A)  #uni092A	DEVANAGARI LETTER PA
        chars.append(0x092B)  #uni092B	DEVANAGARI LETTER PHA
        chars.append(0x092C)  #uni092C	DEVANAGARI LETTER BA
        chars.append(0x092D)  #uni092D	DEVANAGARI LETTER BHA
        chars.append(0x092E)  #uni092E	DEVANAGARI LETTER MA
        chars.append(0x092F)  #uni092F	DEVANAGARI LETTER YA
        chars.append(0x0930)  #uni0930	DEVANAGARI LETTER RA
        chars.append(0x0931)  #uni0931	DEVANAGARI LETTER RRA
        chars.append(0x0932)  #uni0932	DEVANAGARI LETTER LA
        chars.append(0x0933)  #uni0933	DEVANAGARI LETTER LLA
        chars.append(0x0934)  #uni0934	DEVANAGARI LETTER LLLA
        chars.append(0x0935)  #uni0935	DEVANAGARI LETTER VA
        chars.append(0x0936)  #uni0936	DEVANAGARI LETTER SHA
        chars.append(0x0937)  #uni0937	DEVANAGARI LETTER SSA
        chars.append(0x0938)  #uni0938	DEVANAGARI LETTER SA
        chars.append(0x0939)  #uni0939	DEVANAGARI LETTER HA
        chars.append(0x093A)  #uni093A	????
        chars.append(0x093B)  #uni093B	????
        chars.append(0x093C)  #uni093C	DEVANAGARI SIGN NUKTA
        chars.append(0x093D)  #uni093D	DEVANAGARI SIGN AVAGRAHA
        chars.append(0x093E)  #uni093E	DEVANAGARI VOWEL SIGN AA
        chars.append(0x093F)  #uni093F	DEVANAGARI VOWEL SIGN I
        chars.append(0x0940)  #uni0940	DEVANAGARI VOWEL SIGN II
        chars.append(0x0941)  #uni0941	DEVANAGARI VOWEL SIGN U
        chars.append(0x0942)  #uni0942	DEVANAGARI VOWEL SIGN UU
        chars.append(0x0943)  #uni0943	DEVANAGARI VOWEL SIGN VOCALIC R
        chars.append(0x0944)  #uni0944	DEVANAGARI VOWEL SIGN VOCALIC RR
        chars.append(0x0945)  #uni0945	DEVANAGARI VOWEL SIGN CANDRA E
        chars.append(0x0946)  #uni0946	DEVANAGARI VOWEL SIGN SHORT E
        chars.append(0x0947)  #uni0947	DEVANAGARI VOWEL SIGN E
        chars.append(0x0948)  #uni0948	DEVANAGARI VOWEL SIGN AI
        chars.append(0x0949)  #uni0949	DEVANAGARI VOWEL SIGN CANDRA O
        chars.append(0x094A)  #uni094A	DEVANAGARI VOWEL SIGN SHORT O
        chars.append(0x094B)  #uni094B	DEVANAGARI VOWEL SIGN O
        chars.append(0x094C)  #uni094C	DEVANAGARI VOWEL SIGN AU
        chars.append(0x094D)  #uni094D	DEVANAGARI SIGN VIRAMA
        chars.append(0x094E)  #uni094E	DEVANAGARI VOWEL SIGN PRISHTHAMATRA E
        chars.append(0x094F)  #uni094F	????
        chars.append(0x0950)  #uni0950	DEVANAGARI OM
        chars.append(0x0951)  #uni0951	DEVANAGARI STRESS SIGN UDATTA
        chars.append(0x0952)  #uni0952	DEVANAGARI STRESS SIGN ANUDATTA
        chars.append(0x0953)  #uni0953	DEVANAGARI GRAVE ACCENT
        chars.append(0x0954)  #uni0954	DEVANAGARI ACUTE ACCENT
        chars.append(0x0955)  #uni0955	DEVANAGARI VOWEL SIGN CANDRA LONG E
        chars.append(0x0956)  #uni0956	????
        chars.append(0x0957)  #uni0957	????
        chars.append(0x0958)  #uni0958	DEVANAGARI LETTER QA
        chars.append(0x0959)  #uni0959	DEVANAGARI LETTER KHHA
        chars.append(0x095A)  #uni095A	DEVANAGARI LETTER GHHA
        chars.append(0x095B)  #uni095B	DEVANAGARI LETTER ZA
        chars.append(0x095C)  #uni095C	DEVANAGARI LETTER DDDHA
        chars.append(0x095D)  #uni095D	DEVANAGARI LETTER RHA
        chars.append(0x095E)  #uni095E	DEVANAGARI LETTER FA
        chars.append(0x095F)  #uni095F	DEVANAGARI LETTER YYA
        chars.append(0x0960)  #uni0960	DEVANAGARI LETTER VOCALIC RR
        chars.append(0x0961)  #uni0961	DEVANAGARI LETTER VOCALIC LL
        chars.append(0x0962)  #uni0962	DEVANAGARI VOWEL SIGN VOCALIC L
        chars.append(0x0963)  #uni0963	DEVANAGARI VOWEL SIGN VOCALIC LL
        chars.append(0x0964)  #uni0964	DEVANAGARI DANDA
        chars.append(0x0965)  #uni0965	DEVANAGARI DOUBLE DANDA
        chars.append(0x0966)  #uni0966	DEVANAGARI DIGIT ZERO
        chars.append(0x0967)  #uni0967	DEVANAGARI DIGIT ONE
        chars.append(0x0968)  #uni0968	DEVANAGARI DIGIT TWO
        chars.append(0x0969)  #uni0969	DEVANAGARI DIGIT THREE
        chars.append(0x096A)  #uni096A	DEVANAGARI DIGIT FOUR
        chars.append(0x096B)  #uni096B	DEVANAGARI DIGIT FIVE
        chars.append(0x096C)  #uni096C	DEVANAGARI DIGIT SIX
        chars.append(0x096D)  #uni096D	DEVANAGARI DIGIT SEVEN
        chars.append(0x096E)  #uni096E	DEVANAGARI DIGIT EIGHT
        chars.append(0x096F)  #uni096F	DEVANAGARI DIGIT NINE
        chars.append(0x0970)  #uni0970	DEVANAGARI ABBREVIATION SIGN
        chars.append(0x0971)  #uni0971	DEVANAGARI SIGN HIGH SPACING DOT
        chars.append(0x0972)  #uni0972	DEVANAGARI LETTER CANDRA A
        chars.append(0x0973)  #uni0973	????
        chars.append(0x0974)  #uni0974	????
        chars.append(0x0975)  #uni0975	????
        chars.append(0x0976)  #uni0976	????
        chars.append(0x0977)  #uni0977	????
        chars.append(0x0978)  #uni0978	????
        chars.append(0x0979)  #uni0979	DEVANAGARI LETTER ZHA
        chars.append(0x097A)  #uni097A	DEVANAGARI LETTER HEAVY YA
        chars.append(0x097B)  #uni097B	DEVANAGARI LETTER GGA
        chars.append(0x097C)  #uni097C	DEVANAGARI LETTER JJA
        chars.append(0x097D)  #uni097D	DEVANAGARI LETTER GLOTTAL STOP
        chars.append(0x097E)  #uni097E	DEVANAGARI LETTER DDDA
        chars.append(0x097F)  #uni097F	DEVANAGARI LETTER BBA
        chars.append(0xA8EB)  #uniA8EB	COMBINING DEVANAGARI LETTER U
        chars.append(0xA8EC)  #uniA8EC	COMBINING DEVANAGARI LETTER KA
        chars.append(0xA8E0)  #uniA8E0	COMBINING DEVANAGARI DIGIT ZERO
        chars.append(0xA8ED)  #uniA8ED	COMBINING DEVANAGARI LETTER NA
        chars.append(0xA8EE)  #uniA8EE	COMBINING DEVANAGARI LETTER PA
        chars.append(0xA836)  #uniA836	NORTH INDIC QUARTER MARK
        chars.append(0xA835)  #uniA835	NORTH INDIC FRACTION THREE SIXTEENTHS
        chars.append(0xA834)  #uniA834	NORTH INDIC FRACTION ONE EIGHTH
        chars.append(0xA8F1)  #uniA8F1	COMBINING DEVANAGARI SIGN AVAGRAHA
        chars.append(0xA8E1)  #uniA8E1	COMBINING DEVANAGARI DIGIT ONE
        chars.append(0xA8F2)  #uniA8F2	DEVANAGARI SIGN SPACING CANDRABINDU
        chars.append(0xA8F3)  #uniA8F3	DEVANAGARI SIGN CANDRABINDU VIRAMA
        chars.append(0xA837)  #uniA837	NORTH INDIC PLACEHOLDER MARK
        chars.append(0xA8F5)  #uniA8F5	DEVANAGARI SIGN CANDRABINDU TWO
        chars.append(0xA8F6)  #uniA8F6	DEVANAGARI SIGN CANDRABINDU THREE
        chars.append(0xA8EA)  #uniA8EA	COMBINING DEVANAGARI LETTER A
        chars.append(0xA8E2)  #uniA8E2	COMBINING DEVANAGARI DIGIT TWO
        chars.append(0xA8F7)  #uniA8F7	DEVANAGARI SIGN CANDRABINDU AVAGRAHA
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0xA838)  #uniA838	NORTH INDIC RUPEE MARK
        chars.append(0xA832)  #uniA832	NORTH INDIC FRACTION THREE QUARTERS
        chars.append(0xA8F4)  #uniA8F4	DEVANAGARI SIGN DOUBLE CANDRABINDU VIRAMA
        chars.append(0xA8E3)  #uniA8E3	COMBINING DEVANAGARI DIGIT THREE
        chars.append(0xA839)  #uniA839	NORTH INDIC QUANTITY MARK
        return chars


