# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoNastaliqUrduDraft'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0600)  #uni0600	ARABIC NUMBER SIGN
        chars.append(0x0602)  #uni0602	ARABIC FOOTNOTE MARKER
        chars.append(0x0603)  #uni0603	ARABIC SIGN SAFHA
        chars.append(0x0604)  #uni0604	????
        chars.append(0x0601)  #uni0601	ARABIC SIGN SANAH
        chars.append(0x0609)  #uni0609	ARABIC-INDIC PER MILLE SIGN
        chars.append(0x060A)  #uni060A	ARABIC-INDIC PER TEN THOUSAND SIGN
        chars.append(0x060B)  #uni060B	AFGHANI SIGN
        chars.append(0x060C)  #uni060C	ARABIC COMMA
        chars.append(0x000D)  #uni000D	????
        chars.append(0x060E)  #uni060E	ARABIC POETIC VERSE SIGN
        chars.append(0x060F)  #uni060F	ARABIC SIGN MISRA
        chars.append(0x0610)  #uni0610	ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM
        chars.append(0x0611)  #uni0611	ARABIC SIGN ALAYHE ASSALLAM
        chars.append(0x0612)  #uni0612	ARABIC SIGN RAHMATULLAH ALAYHE
        chars.append(0x0613)  #uni0613	ARABIC SIGN RADI ALLAHOU ANHU
        chars.append(0x0614)  #uni0614	ARABIC SIGN TAKHALLUS
        chars.append(0x2018)  #quoteleft	LEFT SINGLE QUOTATION MARK
        chars.append(0x2019)  #quoteright	RIGHT SINGLE QUOTATION MARK
        chars.append(0x061B)  #uni061B	ARABIC SEMICOLON
        chars.append(0x061C)  #uni061C	????
        chars.append(0x201D)  #quotedblright	RIGHT DOUBLE QUOTATION MARK
        chars.append(0x061E)  #uni061E	ARABIC TRIPLE DOT PUNCTUATION MARK
        chars.append(0x061F)  #uni061F	ARABIC QUESTION MARK
        chars.append(0x0020)  #space	SPACE
        chars.append(0x0621)  #uni0621	ARABIC LETTER HAMZA
        chars.append(0x0622)  #uni0622	ARABIC LETTER ALEF WITH MADDA ABOVE
        chars.append(0x0623)  #uni0623	ARABIC LETTER ALEF WITH HAMZA ABOVE
        chars.append(0x0624)  #uni0624	ARABIC LETTER WAW WITH HAMZA ABOVE
        chars.append(0x0625)  #uni0625	ARABIC LETTER ALEF WITH HAMZA BELOW
        chars.append(0x0626)  #uni0626	ARABIC LETTER YEH WITH HAMZA ABOVE
        chars.append(0x0627)  #uni0627	ARABIC LETTER ALEF
        chars.append(0x0028)  #parenleft	LEFT PARENTHESIS
        chars.append(0x0629)  #uni0629	ARABIC LETTER TEH MARBUTA
        chars.append(0x062A)  #uni062A	ARABIC LETTER TEH
        chars.append(0x002B)  #plus	PLUS SIGN
        chars.append(0x062C)  #uni062C	ARABIC LETTER JEEM
        chars.append(0x002D)  #hyphen	HYPHEN-MINUS
        chars.append(0x062E)  #uni062E	ARABIC LETTER KHAH
        chars.append(0x002F)  #slash	SOLIDUS
        chars.append(0x0630)  #uni0630	ARABIC LETTER THAL
        chars.append(0x0631)  #uni0631	ARABIC LETTER REH
        chars.append(0x0632)  #uni0632	ARABIC LETTER ZAIN
        chars.append(0x0633)  #uni0633	ARABIC LETTER SEEN
        chars.append(0x0634)  #uni0634	ARABIC LETTER SHEEN
        chars.append(0x0635)  #uni0635	ARABIC LETTER SAD
        chars.append(0x0636)  #uni0636	ARABIC LETTER DAD
        chars.append(0x0637)  #uni0637	ARABIC LETTER TAH
        chars.append(0x0638)  #uni0638	ARABIC LETTER ZAH
        chars.append(0x0639)  #uni0639	ARABIC LETTER AIN
        chars.append(0x003A)  #colon	COLON
        chars.append(0x063B)  #uni063B	ARABIC LETTER KEHEH WITH TWO DOTS ABOVE
        chars.append(0x063C)  #uni063C	ARABIC LETTER KEHEH WITH THREE DOTS BELOW
        chars.append(0x003D)  #equal	EQUALS SIGN
        chars.append(0x063E)  #uni063E	ARABIC LETTER FARSI YEH WITH TWO DOTS ABOVE
        chars.append(0x063F)  #uni063F	ARABIC LETTER FARSI YEH WITH THREE DOTS ABOVE
        chars.append(0x0640)  #uni0640	ARABIC TATWEEL
        chars.append(0x0641)  #uni0641	ARABIC LETTER FEH
        chars.append(0x0642)  #uni0642	ARABIC LETTER QAF
        chars.append(0x0643)  #uni0643	ARABIC LETTER KAF
        chars.append(0x0644)  #uni0644	ARABIC LETTER LAM
        chars.append(0x0645)  #uni0645	ARABIC LETTER MEEM
        chars.append(0x0646)  #uni0646	ARABIC LETTER NOON
        chars.append(0x0647)  #uni0647	ARABIC LETTER HEH
        chars.append(0x0648)  #uni0648	ARABIC LETTER WAW
        chars.append(0x0649)  #uni0649	ARABIC LETTER ALEF MAKSURA
        chars.append(0x064A)  #uni064A	ARABIC LETTER YEH
        chars.append(0x064B)  #uni064B	ARABIC FATHATAN
        chars.append(0x064C)  #uni064C	ARABIC DAMMATAN
        chars.append(0x064D)  #uni064D	ARABIC KASRATAN
        chars.append(0x064E)  #uni064E	ARABIC FATHA
        chars.append(0x060D)  #uni060D	ARABIC DATE SEPARATOR
        chars.append(0x0650)  #uni0650	ARABIC KASRA
        chars.append(0x0651)  #uni0651	ARABIC SHADDA
        chars.append(0x0652)  #uni0652	ARABIC SUKUN
        chars.append(0x0653)  #uni0653	ARABIC MADDAH ABOVE
        chars.append(0x0654)  #uni0654	ARABIC HAMZA ABOVE
        chars.append(0x0655)  #uni0655	ARABIC HAMZA BELOW
        chars.append(0x0656)  #uni0656	ARABIC SUBSCRIPT ALEF
        chars.append(0x0657)  #uni0657	ARABIC INVERTED DAMMA
        chars.append(0x0658)  #uni0658	ARABIC MARK NOON GHUNNA
        chars.append(0x0659)  #uni0659	ARABIC ZWARAKAY
        chars.append(0x005B)  #bracketleft	LEFT SQUARE BRACKET
        chars.append(0x005C)  #backslash	REVERSE SOLIDUS
        chars.append(0x005D)  #bracketright	RIGHT SQUARE BRACKET
        chars.append(0x065E)  #uni065E	ARABIC FATHA WITH TWO DOTS
        chars.append(0x065F)  #uni065F	????
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
        chars.append(0x066D)  #uni066D	ARABIC FIVE POINTED STAR
        chars.append(0x066E)  #uni066E	ARABIC LETTER DOTLESS BEH
        chars.append(0x066F)  #uni066F	ARABIC LETTER DOTLESS QAF
        chars.append(0x0670)  #uni0670	ARABIC LETTER SUPERSCRIPT ALEF
        chars.append(0x0671)  #uni0671	ARABIC LETTER ALEF WASLA
        chars.append(0x0672)  #uni0672	ARABIC LETTER ALEF WITH WAVY HAMZA ABOVE
        chars.append(0x0673)  #uni0673	ARABIC LETTER ALEF WITH WAVY HAMZA BELOW
        chars.append(0x0679)  #uni0679	ARABIC LETTER TTEH
        chars.append(0x067A)  #uni067A	ARABIC LETTER TTEHEH
        chars.append(0x007B)  #braceleft	LEFT CURLY BRACKET
        chars.append(0x007C)  #bar	VERTICAL LINE
        chars.append(0x007D)  #braceright	RIGHT CURLY BRACKET
        chars.append(0x067E)  #uni067E	ARABIC LETTER PEH
        chars.append(0x067F)  #uni067F	ARABIC LETTER TEHEH
        chars.append(0x0680)  #uni0680	ARABIC LETTER BEHEH
        chars.append(0x0681)  #uni0681	ARABIC LETTER HAH WITH HAMZA ABOVE
        chars.append(0x0683)  #uni0683	ARABIC LETTER NYEH
        chars.append(0x0684)  #uni0684	ARABIC LETTER DYEH
        chars.append(0x0685)  #uni0685	ARABIC LETTER HAH WITH THREE DOTS ABOVE
        chars.append(0x0686)  #uni0686	ARABIC LETTER TCHEH
        chars.append(0x0687)  #uni0687	ARABIC LETTER TCHEHEH
        chars.append(0x0688)  #uni0688	ARABIC LETTER DDAL
        chars.append(0x0689)  #uni0689	ARABIC LETTER DAL WITH RING
        chars.append(0x068A)  #uni068A	ARABIC LETTER DAL WITH DOT BELOW
        chars.append(0x068B)  #uni068B	ARABIC LETTER DAL WITH DOT BELOW AND SMALL TAH
        chars.append(0x068C)  #uni068C	ARABIC LETTER DAHAL
        chars.append(0x068D)  #uni068D	ARABIC LETTER DDAHAL
        chars.append(0x068E)  #uni068E	ARABIC LETTER DUL
        chars.append(0x068F)  #uni068F	ARABIC LETTER DAL WITH THREE DOTS ABOVE DOWNWARDS
        chars.append(0x0691)  #uni0691	ARABIC LETTER RREH
        chars.append(0x0693)  #uni0693	ARABIC LETTER REH WITH RING
        chars.append(0x0696)  #uni0696	ARABIC LETTER REH WITH DOT BELOW AND DOT ABOVE
        chars.append(0x0698)  #uni0698	ARABIC LETTER JEH
        chars.append(0x0699)  #uni0699	ARABIC LETTER REH WITH FOUR DOTS ABOVE
        chars.append(0x069A)  #uni069A	ARABIC LETTER SEEN WITH DOT BELOW AND DOT ABOVE
        chars.append(0x076F)  #uni076F	ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH AND TWO DOTS
        chars.append(0x069E)  #uni069E	ARABIC LETTER SAD WITH THREE DOTS ABOVE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x06A1)  #uni06A1	ARABIC LETTER DOTLESS FEH
        chars.append(0x06A4)  #uni06A4	ARABIC LETTER VEH
        chars.append(0x06A6)  #uni06A6	ARABIC LETTER PEHEH
        chars.append(0x06A9)  #uni06A9	ARABIC LETTER KEHEH
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x00AB)  #guillemotleft	LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x06AF)  #uni06AF	ARABIC LETTER GAF
        chars.append(0x06B0)  #uni06B0	ARABIC LETTER GAF WITH RING
        chars.append(0x06B1)  #uni06B1	ARABIC LETTER NGOEH
        chars.append(0x06B3)  #uni06B3	ARABIC LETTER GUEH
        chars.append(0x00B7)  #periodcentered	MIDDLE DOT
        chars.append(0x06BA)  #uni06BA	ARABIC LETTER NOON GHUNNA
        chars.append(0x00BB)  #guillemotright	RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x06BC)  #uni06BC	ARABIC LETTER NOON WITH RING
        chars.append(0x06BE)  #uni06BE	ARABIC LETTER HEH DOACHASHMEE
        chars.append(0x06C0)  #uni06C0	ARABIC LETTER HEH WITH YEH ABOVE
        chars.append(0x0620)  #uni0620	????
        chars.append(0x06C2)  #uni06C2	ARABIC LETTER HEH GOAL WITH HAMZA ABOVE
        chars.append(0x06C3)  #uni06C3	ARABIC LETTER TEH MARBUTA GOAL
        chars.append(0x06C4)  #uni06C4	ARABIC LETTER WAW WITH RING
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x0777)  #uni0777	ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT FOUR BELOW
        chars.append(0x06CC)  #uni06CC	ARABIC LETTER FARSI YEH
        chars.append(0x06CD)  #uni06CD	ARABIC LETTER YEH WITH TAIL
        chars.append(0x06D0)  #uni06D0	ARABIC LETTER E
        chars.append(0x06D2)  #uni06D2	ARABIC LETTER YEH BARREE
        chars.append(0x06D3)  #uni06D3	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE
        chars.append(0x06D4)  #uni06D4	ARABIC FULL STOP
        chars.append(0x06D5)  #uni06D5	ARABIC LETTER AE
        chars.append(0x00D7)  #multiply	MULTIPLICATION SIGN
        chars.append(0x06C1)  #uni06C1	ARABIC LETTER HEH GOAL
        chars.append(0x06DD)  #uni06DD	ARABIC END OF AYAH
        chars.append(0x06DE)  #uni06DE	ARABIC START OF RUB EL HIZB
        chars.append(0x06E0)  #uni06E0	ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO
        chars.append(0x06E1)  #uni06E1	ARABIC SMALL HIGH DOTLESS HEAD OF KHAH
        chars.append(0x067B)  #uni067B	ARABIC LETTER BEEH
        chars.append(0x2010)  #uni2010	HYPHEN
        chars.append(0x067C)  #uni067C	ARABIC LETTER TEH WITH RING
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x06EE)  #uni06EE	ARABIC LETTER DAL WITH INVERTED V
        chars.append(0x067D)  #uni067D	ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS
        chars.append(0x06F0)  #uni06F0	EXTENDED ARABIC-INDIC DIGIT ZERO
        chars.append(0x0628)  #uni0628	ARABIC LETTER BEH
        chars.append(0x06F2)  #uni06F2	EXTENDED ARABIC-INDIC DIGIT TWO
        chars.append(0x06F3)  #uni06F3	EXTENDED ARABIC-INDIC DIGIT THREE
        chars.append(0x06F4)  #uni06F4	EXTENDED ARABIC-INDIC DIGIT FOUR
        chars.append(0x06F5)  #uni06F5	EXTENDED ARABIC-INDIC DIGIT FIVE
        chars.append(0x06F6)  #uni06F6	EXTENDED ARABIC-INDIC DIGIT SIX
        chars.append(0x0029)  #parenright	RIGHT PARENTHESIS
        chars.append(0x06F8)  #uni06F8	EXTENDED ARABIC-INDIC DIGIT EIGHT
        chars.append(0x06F9)  #uni06F9	EXTENDED ARABIC-INDIC DIGIT NINE
        chars.append(0x06FF)  #uni06FF	ARABIC LETTER HEH WITH INVERTED V
        chars.append(0x062B)  #uni062B	ARABIC LETTER THEH
        chars.append(0x2011)  #uni2011	NON-BREAKING HYPHEN
        chars.append(0x062D)  #uni062D	ARABIC LETTER HAH
        chars.append(0x002E)  #period	FULL STOP
        chars.append(0x062F)  #uni062F	ARABIC LETTER DAL
        chars.append(0x065D)  #uni065D	ARABIC REVERSED DAMMA
        chars.append(0x06F7)  #uni06F7	EXTENDED ARABIC-INDIC DIGIT SEVEN
        chars.append(0x2212)  #minus	MINUS SIGN
        chars.append(0xFD3E)  #uniFD3E	ORNATE LEFT PARENTHESIS
        chars.append(0xFD3F)  #uniFD3F	ORNATE RIGHT PARENTHESIS
        chars.append(0x2013)  #endash	EN DASH
        chars.append(0x2039)  #guilsinglleft	SINGLE LEFT-POINTING ANGLE QUOTATION MARK
        chars.append(0x0759)  #uni0759	ARABIC LETTER DAL WITH TWO DOTS VERTICALLY BELOW AND SMALL TAH
        chars.append(0x06AB)  #uni06AB	ARABIC LETTER KAF WITH RING
        chars.append(0x075C)  #uni075C	ARABIC LETTER SEEN WITH FOUR DOTS ABOVE
        chars.append(0x063A)  #uni063A	ARABIC LETTER GHAIN
        chars.append(0x2014)  #emdash	EM DASH
        chars.append(0x0763)  #uni0763	ARABIC LETTER KEHEH WITH THREE DOTS ABOVE
        chars.append(0x0767)  #uni0767	ARABIC LETTER NOON WITH TWO DOTS BELOW
        chars.append(0x0768)  #uni0768	ARABIC LETTER NOON WITH SMALL TAH
        chars.append(0x0769)  #uni0769	ARABIC LETTER NOON WITH SMALL V
        chars.append(0x076B)  #uni076B	ARABIC LETTER REH WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0x076C)  #uni076C	ARABIC LETTER REH WITH HAMZA ABOVE
        chars.append(0x076D)  #uni076D	ARABIC LETTER SEEN WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0x076E)  #uni076E	ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH BELOW
        chars.append(0x063D)  #uni063D	ARABIC LETTER FARSI YEH WITH INVERTED V
        chars.append(0x0770)  #uni0770	ARABIC LETTER SEEN WITH SMALL ARABIC LETTER TAH AND TWO DOTS
        chars.append(0x0771)  #uni0771	ARABIC LETTER REH WITH SMALL ARABIC LETTER TAH AND TWO DOTS
        chars.append(0x0772)  #uni0772	ARABIC LETTER HAH WITH SMALL ARABIC LETTER TAH ABOVE
        chars.append(0x0773)  #uni0773	ARABIC LETTER ALEF WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(0x0774)  #uni0774	ARABIC LETTER ALEF WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(0x0775)  #uni0775	ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(0x0776)  #uni0776	ARABIC LETTER FARSI YEH WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(0x06E9)  #uni06E9	ARABIC PLACE OF SAJDAH
        chars.append(0x0778)  #uni0778	ARABIC LETTER WAW WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(0x0779)  #uni0779	ARABIC LETTER WAW WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(0x077A)  #uni077A	ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT TWO ABOVE
        chars.append(0x077B)  #uni077B	ARABIC LETTER YEH BARREE WITH EXTENDED ARABIC-INDIC DIGIT THREE ABOVE
        chars.append(0x077C)  #uni077C	ARABIC LETTER HAH WITH EXTENDED ARABIC-INDIC DIGIT FOUR BELOW
        chars.append(0x077D)  #uni077D	ARABIC LETTER SEEN WITH EXTENDED ARABIC-INDIC DIGIT FOUR ABOVE
        chars.append(0x201C)  #quotedblleft	LEFT DOUBLE QUOTATION MARK
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x06EF)  #uni06EF	ARABIC LETTER REH WITH INVERTED V
        chars.append(0x06F1)  #uni06F1	EXTENDED ARABIC-INDIC DIGIT ONE
        chars.append(0x06BB)  #uni06BB	ARABIC LETTER RNOON
        chars.append(0x06B7)  #uni06B7	ARABIC LETTER LAM WITH THREE DOTS ABOVE
        chars.append(0xFBB2)  #uniFBB2	????
        chars.append(0xFBB3)  #uniFBB3	????
        chars.append(0xFBB4)  #uniFBB4	????
        chars.append(0xFBB5)  #uniFBB5	????
        chars.append(0xFBB6)  #uniFBB6	????
        chars.append(0xFBB7)  #uniFBB7	????
        chars.append(0xFBB8)  #uniFBB8	????
        chars.append(0xFBB9)  #uniFBB9	????
        chars.append(0xFBBA)  #uniFBBA	????
        chars.append(0xFBBB)  #uniFBBB	????
        chars.append(0xFBBC)  #uniFBBC	????
        chars.append(0xFBBD)  #uniFBBD	????
        chars.append(0xFBBE)  #uniFBBE	????
        chars.append(0xFBBF)  #uniFBBF	????
        chars.append(0xFBC0)  #uniFBC0	????
        chars.append(0xFBC1)  #uniFBC1	????
        chars.append(0x00F7)  #divide	DIVISION SIGN
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x203A)  #guilsinglright	SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
        chars.append(0x064F)  #uni064F	ARABIC DAMMA
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xFDF2)  #uniFDF2	ARABIC LIGATURE ALLAH ISOLATED FORM
        chars.append(0xFDF4)  #uniFDF4	ARABIC LIGATURE MOHAMMAD ISOLATED FORM
        chars.append(0xFDFA)  #uniFDFA	ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM
        chars.append(0xFDFB)  #uniFDFB	ARABIC LIGATURE JALLAJALALOUHOU
        chars.append(0xFDFC)  #uniFDFC	RIAL SIGN
        chars.append(0xFDFD)  #uniFDFD	ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM
        return chars


