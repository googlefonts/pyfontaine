# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoKufiArabic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #.null	????
        chars.append(0xFEAB)  #uni0630	ARABIC LETTER THAL ISOLATED FORM
        chars.append(0xFEAC)  #uni0630.fina	ARABIC LETTER THAL FINAL FORM
        chars.append(0x200B)  #ZWSP	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #nonmarkingreturn	????
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0xFEAE)  #uni0631.fina	ARABIC LETTER REH FINAL FORM
        chars.append(0xFEAF)  #uni0632	ARABIC LETTER ZAIN ISOLATED FORM
        chars.append(0x0020)  #space	SPACE
        chars.append(0xFEB0)  #uni0632.fina	ARABIC LETTER ZAIN FINAL FORM
        chars.append(0xFEB1)  #uni0633	ARABIC LETTER SEEN ISOLATED FORM
        chars.append(0xFEB2)  #uni0633.fina	ARABIC LETTER SEEN FINAL FORM
        chars.append(0xFEB3)  #uni0633.init	ARABIC LETTER SEEN INITIAL FORM
        chars.append(0xFEB4)  #uni0633.medi	ARABIC LETTER SEEN MEDIAL FORM
        chars.append(0xFEB5)  #uni0634	ARABIC LETTER SHEEN ISOLATED FORM
        chars.append(0xFEAD)  #uni0631	ARABIC LETTER REH ISOLATED FORM
        chars.append(0xFEB6)  #uni0634.fina	ARABIC LETTER SHEEN FINAL FORM
        chars.append(0xFEB7)  #uni0634.init	ARABIC LETTER SHEEN INITIAL FORM
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0xFEB8)  #uni0634.medi	ARABIC LETTER SHEEN MEDIAL FORM
        chars.append(0xFEB9)  #uni0635	ARABIC LETTER SAD ISOLATED FORM
        chars.append(0xFEBA)  #uni0635.fina	ARABIC LETTER SAD FINAL FORM
        chars.append(0xFEBB)  #uni0635.init	ARABIC LETTER SAD INITIAL FORM
        chars.append(0xFEBC)  #uni0635.medi	ARABIC LETTER SAD MEDIAL FORM
        chars.append(0xFEBD)  #uni0636	ARABIC LETTER DAD ISOLATED FORM
        chars.append(0xFEBE)  #uni0636.fina	ARABIC LETTER DAD FINAL FORM
        chars.append(0xFEBF)  #uni0636.init	ARABIC LETTER DAD INITIAL FORM
        chars.append(0xFEC0)  #uni0636.medi	ARABIC LETTER DAD MEDIAL FORM
        chars.append(0xFEC1)  #uni0637	ARABIC LETTER TAH ISOLATED FORM
        chars.append(0xFEC2)  #uni0637.fina	ARABIC LETTER TAH FINAL FORM
        chars.append(0xFEC3)  #uni0637.init	ARABIC LETTER TAH INITIAL FORM
        chars.append(0xFEC4)  #uni0637.medi	ARABIC LETTER TAH MEDIAL FORM
        chars.append(0xFEC5)  #uni0638	ARABIC LETTER ZAH ISOLATED FORM
        chars.append(0x00A0)  #space	NO-BREAK SPACE
        chars.append(0xFEC6)  #uni0638.fina	ARABIC LETTER ZAH FINAL FORM
        chars.append(0xFEC7)  #uni0638.init	ARABIC LETTER ZAH INITIAL FORM
        chars.append(0xFEC8)  #uni0638.medi	ARABIC LETTER ZAH MEDIAL FORM
        chars.append(0xFEC9)  #uni0639	ARABIC LETTER AIN ISOLATED FORM
        chars.append(0xFECA)  #uni0639.fina	ARABIC LETTER AIN FINAL FORM
        chars.append(0xFECB)  #uni0639.init	ARABIC LETTER AIN INITIAL FORM
        chars.append(0xFECC)  #uni0639.medi	ARABIC LETTER AIN MEDIAL FORM
        chars.append(0xFECD)  #uni063A	ARABIC LETTER GHAIN ISOLATED FORM
        chars.append(0xFECE)  #uni063A.fina	ARABIC LETTER GHAIN FINAL FORM
        chars.append(0xFECF)  #uni063A.init	ARABIC LETTER GHAIN INITIAL FORM
        chars.append(0xFED0)  #uni063A.medi	ARABIC LETTER GHAIN MEDIAL FORM
        chars.append(0xFED1)  #uni0641	ARABIC LETTER FEH ISOLATED FORM
        chars.append(0xFED2)  #uni0641.fina	ARABIC LETTER FEH FINAL FORM
        chars.append(0xFED3)  #uni0641.init	ARABIC LETTER FEH INITIAL FORM
        chars.append(0xFED4)  #uni0641.medi	ARABIC LETTER FEH MEDIAL FORM
        chars.append(0xFED5)  #uni0642	ARABIC LETTER QAF ISOLATED FORM
        chars.append(0xFED6)  #uni0642.fina	ARABIC LETTER QAF FINAL FORM
        chars.append(0xFED7)  #uni0642.init	ARABIC LETTER QAF INITIAL FORM
        chars.append(0xFED8)  #uni0642.medi	ARABIC LETTER QAF MEDIAL FORM
        chars.append(0xFED9)  #uni0643	ARABIC LETTER KAF ISOLATED FORM
        chars.append(0xFE70)  #fathatan_01	ARABIC FATHATAN ISOLATED FORM
        chars.append(0xFEDA)  #uni0643.fina	ARABIC LETTER KAF FINAL FORM
        chars.append(0xFEDB)  #uni0643.init	ARABIC LETTER KAF INITIAL FORM
        chars.append(0xFEDC)  #uni0643.medi	ARABIC LETTER KAF MEDIAL FORM
        chars.append(0xFEDD)  #uni0644	ARABIC LETTER LAM ISOLATED FORM
        chars.append(0xFEDE)  #uni0644.fina	ARABIC LETTER LAM FINAL FORM
        chars.append(0xFEDF)  #uni0644.init	ARABIC LETTER LAM INITIAL FORM
        chars.append(0xFEE0)  #uni0644.medi	ARABIC LETTER LAM MEDIAL FORM
        chars.append(0xFEE1)  #uni0645	ARABIC LETTER MEEM ISOLATED FORM
        chars.append(0xFEE2)  #uni0645.fina	ARABIC LETTER MEEM FINAL FORM
        chars.append(0xFEE3)  #uni0645.init	ARABIC LETTER MEEM INITIAL FORM
        chars.append(0xFE72)  #dammatan_01	ARABIC DAMMATAN ISOLATED FORM
        chars.append(0xFEE4)  #uni0645.medi	ARABIC LETTER MEEM MEDIAL FORM
        chars.append(0xFEE5)  #uni0646	ARABIC LETTER NOON ISOLATED FORM
        chars.append(0xFEE6)  #uni0646.fina	ARABIC LETTER NOON FINAL FORM
        chars.append(0xFEE7)  #uni0646.init	ARABIC LETTER NOON INITIAL FORM
        chars.append(0xFEE8)  #uni0646.medi	ARABIC LETTER NOON MEDIAL FORM
        chars.append(0xFEE9)  #uni0647	ARABIC LETTER HEH ISOLATED FORM
        chars.append(0xFEEA)  #uni0647.fina	ARABIC LETTER HEH FINAL FORM
        chars.append(0xFEEB)  #uni0647.init	ARABIC LETTER HEH INITIAL FORM
        chars.append(0xFEED)  #uni0648	ARABIC LETTER WAW ISOLATED FORM
        chars.append(0xFEEE)  #uni0648.fina	ARABIC LETTER WAW FINAL FORM
        chars.append(0xFEEF)  #uni0649	ARABIC LETTER ALEF MAKSURA ISOLATED FORM
        chars.append(0xFEF0)  #uni0649.fina	ARABIC LETTER ALEF MAKSURA FINAL FORM
        chars.append(0xFEF1)  #uni064A	ARABIC LETTER YEH ISOLATED FORM
        chars.append(0xFEF2)  #uni064A.fina	ARABIC LETTER YEH FINAL FORM
        chars.append(0xFEF3)  #uni064A.init	ARABIC LETTER YEH INITIAL FORM
        chars.append(0xFEF4)  #uni064A.medi	ARABIC LETTER YEH MEDIAL FORM
        chars.append(0xFEF5)  #uni06440622.isol	ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM
        chars.append(0xFEF6)  #uni06440622.fina	ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE FINAL FORM
        chars.append(0xFEF7)  #uni06440623.isol	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFE76)  #fatha_01	ARABIC FATHA ISOLATED FORM
        chars.append(0xFEF8)  #uni06440623.fina	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE FINAL FORM
        chars.append(0xFEF9)  #uni06440625.isol	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW ISOLATED FORM
        chars.append(0xFEFA)  #uni06440625.fina	ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW FINAL FORM
        chars.append(0xFEFB)  #uni06440627.isol	ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
        chars.append(0xFEFC)  #uni06440627.fina	ARABIC LIGATURE LAM WITH ALEF FINAL FORM
        chars.append(0xFEFF)  #.null	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xFE78)  #damma_01	ARABIC DAMMA ISOLATED FORM
        chars.append(0xFE7A)  #kasra_01	ARABIC KASRA ISOLATED FORM
        chars.append(0xFE7C)  #shadda_01	ARABIC SHADDA ISOLATED FORM
        chars.append(0xFE7E)  #sukun_01	ARABIC SUKUN ISOLATED FORM
        chars.append(0xFB50)  #uni0671	ARABIC LETTER ALEF WASLA ISOLATED FORM
        chars.append(0xFB51)  #uni0671.fina	ARABIC LETTER ALEF WASLA FINAL FORM
        chars.append(0xFB56)  #uni067E	ARABIC LETTER PEH ISOLATED FORM
        chars.append(0xFB57)  #uni067E.fina	ARABIC LETTER PEH FINAL FORM
        chars.append(0xFB58)  #uni067E.init	ARABIC LETTER PEH INITIAL FORM
        chars.append(0xFB59)  #uni067E.medi	ARABIC LETTER PEH MEDIAL FORM
        chars.append(0xFB66)  #uni0679	ARABIC LETTER TTEH ISOLATED FORM
        chars.append(0xFB67)  #uni0679.fina	ARABIC LETTER TTEH FINAL FORM
        chars.append(0xFB68)  #uni0679.init	ARABIC LETTER TTEH INITIAL FORM
        chars.append(0xFB69)  #uni0679.medi	ARABIC LETTER TTEH MEDIAL FORM
        chars.append(0xFB6A)  #veh.isol	ARABIC LETTER VEH ISOLATED FORM
        chars.append(0xFB6B)  #veh.fina	ARABIC LETTER VEH FINAL FORM
        chars.append(0xFB6C)  #veh.init	ARABIC LETTER VEH INITIAL FORM
        chars.append(0xFB6D)  #veh.medi	ARABIC LETTER VEH MEDIAL FORM
        chars.append(0xFB7A)  #uni0686	ARABIC LETTER TCHEH ISOLATED FORM
        chars.append(0xFB7B)  #uni0686.fina	ARABIC LETTER TCHEH FINAL FORM
        chars.append(0xFB7C)  #uni0686.init	ARABIC LETTER TCHEH INITIAL FORM
        chars.append(0xFB7D)  #uni0686.medi	ARABIC LETTER TCHEH MEDIAL FORM
        chars.append(0xFB88)  #uni0688	ARABIC LETTER DDAL ISOLATED FORM
        chars.append(0xFB89)  #uni0688.fina	ARABIC LETTER DDAL FINAL FORM
        chars.append(0xFB8A)  #uni0698	ARABIC LETTER JEH ISOLATED FORM
        chars.append(0xFB8B)  #uni0698.fina	ARABIC LETTER JEH FINAL FORM
        chars.append(0xFB8C)  #uni0691	ARABIC LETTER RREH ISOLATED FORM
        chars.append(0xFB8D)  #uni0691.fina	ARABIC LETTER RREH FINAL FORM
        chars.append(0xFB8E)  #uni06A9	ARABIC LETTER KEHEH ISOLATED FORM
        chars.append(0xFB8F)  #uni06A9.fina	ARABIC LETTER KEHEH FINAL FORM
        chars.append(0xFB90)  #uni06A9.init	ARABIC LETTER KEHEH INITIAL FORM
        chars.append(0xFB91)  #uni06A9.medi	ARABIC LETTER KEHEH MEDIAL FORM
        chars.append(0xFB92)  #uni06AF	ARABIC LETTER GAF ISOLATED FORM
        chars.append(0xFB93)  #uni06AF.fina	ARABIC LETTER GAF FINAL FORM
        chars.append(0xFB94)  #uni06AF.init	ARABIC LETTER GAF INITIAL FORM
        chars.append(0xFB95)  #uni06AF.medi	ARABIC LETTER GAF MEDIAL FORM
        chars.append(0xFB9E)  #uni06BA	ARABIC LETTER NOON GHUNNA ISOLATED FORM
        chars.append(0xFB9F)  #uni06BA.fina	ARABIC LETTER NOON GHUNNA FINAL FORM
        chars.append(0xFBA4)  #uni06C0	ARABIC LETTER HEH WITH YEH ABOVE ISOLATED FORM
        chars.append(0xFBA5)  #uni06C0.fina	ARABIC LETTER HEH WITH YEH ABOVE FINAL FORM
        chars.append(0xFBA6)  #uni06C1	ARABIC LETTER HEH GOAL ISOLATED FORM
        chars.append(0xFBA7)  #uni06C1.fina	ARABIC LETTER HEH GOAL FINAL FORM
        chars.append(0xFBA8)  #uni06C1.init	ARABIC LETTER HEH GOAL INITIAL FORM
        chars.append(0xFBA9)  #uni06C1.medi	ARABIC LETTER HEH GOAL MEDIAL FORM
        chars.append(0xFBAA)  #uni06BE	ARABIC LETTER HEH DOACHASHMEE ISOLATED FORM
        chars.append(0xFBAB)  #uni06BE.fina	ARABIC LETTER HEH DOACHASHMEE FINAL FORM
        chars.append(0xFBAC)  #uni06BE.init	ARABIC LETTER HEH DOACHASHMEE INITIAL FORM
        chars.append(0xFBAD)  #uni06BE.medi	ARABIC LETTER HEH DOACHASHMEE MEDIAL FORM
        chars.append(0xFBAE)  #uni06D2	ARABIC LETTER YEH BARREE ISOLATED FORM
        chars.append(0xFBAF)  #uni06D2.fina	ARABIC LETTER YEH BARREE FINAL FORM
        chars.append(0xFBB0)  #uni06D3	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFBB1)  #uni06D3.fina	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE FINAL FORM
        chars.append(0xFBE6)  #uni06D0.init	ARABIC LETTER E INITIAL FORM
        chars.append(0xFBE7)  #uni06D0.medi	ARABIC LETTER E MEDIAL FORM
        chars.append(0xFBE8)  #uni0649.init	ARABIC LETTER UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA INITIAL FORM
        chars.append(0xFBE9)  #uni0649.medi	ARABIC LETTER UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA MEDIAL FORM
        chars.append(0xFBFC)  #uni06CC	ARABIC LETTER FARSI YEH ISOLATED FORM
        chars.append(0xFBFD)  #uni06CC.fina	ARABIC LETTER FARSI YEH FINAL FORM
        chars.append(0xFBFE)  #uni06CC.init	ARABIC LETTER FARSI YEH INITIAL FORM
        chars.append(0xFBFF)  #uni06CC.medi	ARABIC LETTER FARSI YEH MEDIAL FORM
        chars.append(0xFC5E)  #uni0651064C	ARABIC LIGATURE SHADDA WITH DAMMATAN ISOLATED FORM
        chars.append(0xFC5F)  #uni0651064D	ARABIC LIGATURE SHADDA WITH KASRATAN ISOLATED FORM
        chars.append(0xFC60)  #uni0651064E	ARABIC LIGATURE SHADDA WITH FATHA ISOLATED FORM
        chars.append(0xFC61)  #uni0651064F	ARABIC LIGATURE SHADDA WITH DAMMA ISOLATED FORM
        chars.append(0xFC62)  #uni06510650	ARABIC LIGATURE SHADDA WITH KASRA ISOLATED FORM
        chars.append(0xFC63)  #uniFC63	ARABIC LIGATURE SHADDA WITH SUPERSCRIPT ALEF ISOLATED FORM
        chars.append(0xFE8E)  #uni0627.fina	ARABIC LETTER ALEF FINAL FORM
        chars.append(0xFE8F)  #uni0628	ARABIC LETTER BEH ISOLATED FORM
        chars.append(0xFE90)  #uni0628.fina	ARABIC LETTER BEH FINAL FORM
        chars.append(0xFE91)  #uni0628.init	ARABIC LETTER BEH INITIAL FORM
        chars.append(0xFE92)  #uni0628.medi	ARABIC LETTER BEH MEDIAL FORM
        chars.append(0xFD3E)  #uniFD3E	ORNATE LEFT PARENTHESIS
        chars.append(0xFD3F)  #uniFD3F	ORNATE RIGHT PARENTHESIS
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0xFDF2)  #allah	ARABIC LIGATURE ALLAH ISOLATED FORM
        chars.append(0xFDFC)  #riyal	RIAL SIGN
        chars.append(0x0600)  #uni0600	ARABIC NUMBER SIGN
        chars.append(0x0601)  #uni0601	ARABIC SIGN SANAH
        chars.append(0x0602)  #uni0602	ARABIC FOOTNOTE MARKER
        chars.append(0x0603)  #uni0603	ARABIC SIGN SAFHA
        chars.append(0x060B)  #uni060B	AFGHANI SIGN
        chars.append(0x060C)  #uni060C	ARABIC COMMA
        chars.append(0x060D)  #uni060D	ARABIC DATE SEPARATOR
        chars.append(0x060E)  #uni060E	ARABIC POETIC VERSE SIGN
        chars.append(0x060F)  #uni060F	ARABIC SIGN MISRA
        chars.append(0x0610)  #uni0610	ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM
        chars.append(0x0611)  #uni0611	ARABIC SIGN ALAYHE ASSALLAM
        chars.append(0x0612)  #uni0612	ARABIC SIGN RAHMATULLAH ALAYHE
        chars.append(0x0613)  #uni0613	ARABIC SIGN RADI ALLAHOU ANHU
        chars.append(0x0614)  #uni0614	ARABIC SIGN TAKHALLUS
        chars.append(0x0615)  #uni0615	ARABIC SMALL HIGH TAH
        chars.append(0x061B)  #uni061B	ARABIC SEMICOLON
        chars.append(0x061E)  #uni061E	ARABIC TRIPLE DOT PUNCTUATION MARK
        chars.append(0x061F)  #uni061F	ARABIC QUESTION MARK
        chars.append(0x0621)  #uni0621	ARABIC LETTER HAMZA
        chars.append(0x0622)  #uni0622	ARABIC LETTER ALEF WITH MADDA ABOVE
        chars.append(0x0623)  #uni0623	ARABIC LETTER ALEF WITH HAMZA ABOVE
        chars.append(0x0624)  #uni0624	ARABIC LETTER WAW WITH HAMZA ABOVE
        chars.append(0x0625)  #uni0625	ARABIC LETTER ALEF WITH HAMZA BELOW
        chars.append(0x0626)  #uni0626	ARABIC LETTER YEH WITH HAMZA ABOVE
        chars.append(0x0627)  #uni0627	ARABIC LETTER ALEF
        chars.append(0x0628)  #uni0628	ARABIC LETTER BEH
        chars.append(0x0629)  #uni0629	ARABIC LETTER TEH MARBUTA
        chars.append(0x062A)  #uni062A	ARABIC LETTER TEH
        chars.append(0x062B)  #uni062B	ARABIC LETTER THEH
        chars.append(0x062C)  #uni062C	ARABIC LETTER JEEM
        chars.append(0x062D)  #uni062D	ARABIC LETTER HAH
        chars.append(0x062E)  #uni062E	ARABIC LETTER KHAH
        chars.append(0x062F)  #uni062F	ARABIC LETTER DAL
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
        chars.append(0x063A)  #uni063A	ARABIC LETTER GHAIN
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
        chars.append(0x064F)  #uni064F	ARABIC DAMMA
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
        chars.append(0x065A)  #uni065A	ARABIC VOWEL SIGN SMALL V ABOVE
        chars.append(0x065B)  #uni065B	ARABIC VOWEL SIGN INVERTED SMALL V ABOVE
        chars.append(0x065C)  #uni065C	ARABIC VOWEL SIGN DOT BELOW
        chars.append(0x065D)  #uni065D	ARABIC REVERSED DAMMA
        chars.append(0x065E)  #uni065E	ARABIC FATHA WITH TWO DOTS
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
        chars.append(0xFE74)  #kasratan_01	ARABIC KASRATAN ISOLATED FORM
        chars.append(0x0675)  #uni0675	ARABIC LETTER HIGH HAMZA ALEF
        chars.append(0x0676)  #uni0676	ARABIC LETTER HIGH HAMZA WAW
        chars.append(0x0677)  #uni0677	ARABIC LETTER U WITH HAMZA ABOVE
        chars.append(0x0678)  #uni0678	ARABIC LETTER HIGH HAMZA YEH
        chars.append(0x0679)  #uni0679	ARABIC LETTER TTEH
        chars.append(0x067A)  #uni067A	ARABIC LETTER TTEHEH
        chars.append(0x067B)  #uni067B	ARABIC LETTER BEEH
        chars.append(0x067C)  #uni067C	ARABIC LETTER TEH WITH RING
        chars.append(0x067D)  #uni067D	ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS
        chars.append(0x067E)  #uni067E	ARABIC LETTER PEH
        chars.append(0x067F)  #uni067F	ARABIC LETTER TEHEH
        chars.append(0x0680)  #uni0680	ARABIC LETTER BEHEH
        chars.append(0x0681)  #uni0681	ARABIC LETTER HAH WITH HAMZA ABOVE
        chars.append(0x0682)  #uni0682	ARABIC LETTER HAH WITH TWO DOTS VERTICAL ABOVE
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
        chars.append(0x0690)  #uni0690	ARABIC LETTER DAL WITH FOUR DOTS ABOVE
        chars.append(0x0691)  #uni0691	ARABIC LETTER RREH
        chars.append(0x0692)  #uni0692	ARABIC LETTER REH WITH SMALL V
        chars.append(0x0693)  #uni0693	ARABIC LETTER REH WITH RING
        chars.append(0x0694)  #uni0694	ARABIC LETTER REH WITH DOT BELOW
        chars.append(0x0695)  #uni0695	ARABIC LETTER REH WITH SMALL V BELOW
        chars.append(0x0696)  #uni0696	ARABIC LETTER REH WITH DOT BELOW AND DOT ABOVE
        chars.append(0x0697)  #uni0697	ARABIC LETTER REH WITH TWO DOTS ABOVE
        chars.append(0x0698)  #uni0698	ARABIC LETTER JEH
        chars.append(0x0699)  #uni0699	ARABIC LETTER REH WITH FOUR DOTS ABOVE
        chars.append(0x069A)  #uni069A	ARABIC LETTER SEEN WITH DOT BELOW AND DOT ABOVE
        chars.append(0x069B)  #uni069B	ARABIC LETTER SEEN WITH THREE DOTS BELOW
        chars.append(0x069C)  #uni069C	ARABIC LETTER SEEN WITH THREE DOTS BELOW AND THREE DOTS ABOVE
        chars.append(0x069D)  #uni069D	ARABIC LETTER SAD WITH TWO DOTS BELOW
        chars.append(0x069E)  #uni069E	ARABIC LETTER SAD WITH THREE DOTS ABOVE
        chars.append(0x069F)  #uni069F	ARABIC LETTER TAH WITH THREE DOTS ABOVE
        chars.append(0x06A0)  #uni06A0	ARABIC LETTER AIN WITH THREE DOTS ABOVE
        chars.append(0x06A1)  #uni06A1	ARABIC LETTER DOTLESS FEH
        chars.append(0x06A2)  #uni06A2	ARABIC LETTER FEH WITH DOT MOVED BELOW
        chars.append(0x06A3)  #uni06A3	ARABIC LETTER FEH WITH DOT BELOW
        chars.append(0x06A4)  #uni06A4	ARABIC LETTER VEH
        chars.append(0x06A5)  #uni06A5	ARABIC LETTER FEH WITH THREE DOTS BELOW
        chars.append(0x06A6)  #uni06A6	ARABIC LETTER PEHEH
        chars.append(0x06A7)  #uni06A7	ARABIC LETTER QAF WITH DOT ABOVE
        chars.append(0x06A8)  #uni06A8	ARABIC LETTER QAF WITH THREE DOTS ABOVE
        chars.append(0x06A9)  #uni06A9	ARABIC LETTER KEHEH
        chars.append(0x06AA)  #uni06AA	ARABIC LETTER SWASH KAF
        chars.append(0x06AB)  #uni06AB	ARABIC LETTER KAF WITH RING
        chars.append(0x06AC)  #uni06AC	ARABIC LETTER KAF WITH DOT ABOVE
        chars.append(0x06AD)  #uni06AD	ARABIC LETTER NG
        chars.append(0x06AE)  #uni06AE	ARABIC LETTER KAF WITH THREE DOTS BELOW
        chars.append(0x06AF)  #uni06AF	ARABIC LETTER GAF
        chars.append(0x06B0)  #uni06B0	ARABIC LETTER GAF WITH RING
        chars.append(0x06B1)  #uni06B1	ARABIC LETTER NGOEH
        chars.append(0x06B2)  #uni06B2	ARABIC LETTER GAF WITH TWO DOTS BELOW
        chars.append(0x06B3)  #uni06B3	ARABIC LETTER GUEH
        chars.append(0x06B4)  #uni06B4	ARABIC LETTER GAF WITH THREE DOTS ABOVE
        chars.append(0x06B5)  #uni06B5	ARABIC LETTER LAM WITH SMALL V
        chars.append(0x06B6)  #uni06B6	ARABIC LETTER LAM WITH DOT ABOVE
        chars.append(0x06B7)  #uni06B7	ARABIC LETTER LAM WITH THREE DOTS ABOVE
        chars.append(0x06B8)  #uni06B8	ARABIC LETTER LAM WITH THREE DOTS BELOW
        chars.append(0x06B9)  #uni06B9	ARABIC LETTER NOON WITH DOT BELOW
        chars.append(0x06BA)  #uni06BA	ARABIC LETTER NOON GHUNNA
        chars.append(0x06BB)  #uni06BB	ARABIC LETTER RNOON
        chars.append(0x06BC)  #uni06BC	ARABIC LETTER NOON WITH RING
        chars.append(0x06BD)  #uni06BD	ARABIC LETTER NOON WITH THREE DOTS ABOVE
        chars.append(0x06BE)  #uni06BE	ARABIC LETTER HEH DOACHASHMEE
        chars.append(0x06BF)  #uni06BF	ARABIC LETTER TCHEH WITH DOT ABOVE
        chars.append(0x06C0)  #uni06C0	ARABIC LETTER HEH WITH YEH ABOVE
        chars.append(0x06C1)  #uni06C1.fina	ARABIC LETTER HEH GOAL
        chars.append(0x06C2)  #uni06C2.fina	ARABIC LETTER HEH GOAL WITH HAMZA ABOVE
        chars.append(0x06C3)  #uni06C3.fina	ARABIC LETTER TEH MARBUTA GOAL
        chars.append(0x06C4)  #uni06C4	ARABIC LETTER WAW WITH RING
        chars.append(0x06C5)  #uni06C5	ARABIC LETTER KIRGHIZ OE
        chars.append(0x06C6)  #uni06C6	ARABIC LETTER OE
        chars.append(0x06C7)  #uni06C7	ARABIC LETTER U
        chars.append(0x06C8)  #uni06C8	ARABIC LETTER YU
        chars.append(0x06C9)  #uni06C9	ARABIC LETTER KIRGHIZ YU
        chars.append(0x06CA)  #uni06CA	ARABIC LETTER WAW WITH TWO DOTS ABOVE
        chars.append(0x06CB)  #uni06CB	ARABIC LETTER VE
        chars.append(0x06CC)  #uni06CC	ARABIC LETTER FARSI YEH
        chars.append(0x06CD)  #uni06CD	ARABIC LETTER YEH WITH TAIL
        chars.append(0x06CE)  #uni06CE	ARABIC LETTER YEH WITH SMALL V
        chars.append(0x06CF)  #uni06CF	ARABIC LETTER WAW WITH DOT ABOVE
        chars.append(0x06D0)  #uni06D0	ARABIC LETTER E
        chars.append(0x06D1)  #uni06D1	ARABIC LETTER YEH WITH THREE DOTS BELOW
        chars.append(0x06D2)  #uni06D2	ARABIC LETTER YEH BARREE
        chars.append(0x06D3)  #uni06D3	ARABIC LETTER YEH BARREE WITH HAMZA ABOVE
        chars.append(0x06D4)  #uni06D4	ARABIC FULL STOP
        chars.append(0x06D5)  #uni06D5	ARABIC LETTER AE
        chars.append(0x06D6)  #uni06D6	ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA
        chars.append(0x06D7)  #uni06D7	ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA
        chars.append(0x06D8)  #uni06D8	ARABIC SMALL HIGH MEEM INITIAL FORM
        chars.append(0x06D9)  #uni06D9	ARABIC SMALL HIGH LAM ALEF
        chars.append(0x06DA)  #uni06DA	ARABIC SMALL HIGH JEEM
        chars.append(0x06DB)  #uni06DB	ARABIC SMALL HIGH THREE DOTS
        chars.append(0x06DC)  #uni06DC	ARABIC SMALL HIGH SEEN
        chars.append(0x06DD)  #uni06DD	ARABIC END OF AYAH
        chars.append(0x06DE)  #uni06DE	ARABIC START OF RUB EL HIZB
        chars.append(0x06DF)  #uni06DF	ARABIC SMALL HIGH ROUNDED ZERO
        chars.append(0x06E0)  #uni06E0	ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO
        chars.append(0x06E1)  #uni06E1	ARABIC SMALL HIGH DOTLESS HEAD OF KHAH
        chars.append(0x06E2)  #uni06E2	ARABIC SMALL HIGH MEEM ISOLATED FORM
        chars.append(0x06E3)  #uni06E3	ARABIC SMALL LOW SEEN
        chars.append(0x06E4)  #uni06E4	ARABIC SMALL HIGH MADDA
        chars.append(0x06E5)  #uni06E5	ARABIC SMALL WAW
        chars.append(0x06E6)  #uni06E6	ARABIC SMALL YEH
        chars.append(0x06E7)  #uni06E7	ARABIC SMALL HIGH YEH
        chars.append(0x06E8)  #uni06E8	ARABIC SMALL HIGH NOON
        chars.append(0x06E9)  #uni06E9	ARABIC PLACE OF SAJDAH
        chars.append(0x06EA)  #uni06EA	ARABIC EMPTY CENTRE LOW STOP
        chars.append(0x06EB)  #uni06EB	ARABIC EMPTY CENTRE HIGH STOP
        chars.append(0xFEEC)  #uni0647.medi	ARABIC LETTER HEH MEDIAL FORM
        chars.append(0x06ED)  #uni06ED	ARABIC SMALL LOW MEEM
        chars.append(0x06EE)  #uni06EE	ARABIC LETTER DAL WITH INVERTED V
        chars.append(0x06EF)  #uni06EF	ARABIC LETTER REH WITH INVERTED V
        chars.append(0x06F0)  #uni06F0	EXTENDED ARABIC-INDIC DIGIT ZERO
        chars.append(0x06F1)  #uni06F1	EXTENDED ARABIC-INDIC DIGIT ONE
        chars.append(0x06F2)  #uni06F2	EXTENDED ARABIC-INDIC DIGIT TWO
        chars.append(0x06F3)  #uni06F3	EXTENDED ARABIC-INDIC DIGIT THREE
        chars.append(0x06F4)  #uni06F4	EXTENDED ARABIC-INDIC DIGIT FOUR
        chars.append(0x06F5)  #uni06F5	EXTENDED ARABIC-INDIC DIGIT FIVE
        chars.append(0x06F6)  #uni06F6	EXTENDED ARABIC-INDIC DIGIT SIX
        chars.append(0x06F7)  #uni06F7	EXTENDED ARABIC-INDIC DIGIT SEVEN
        chars.append(0x06F8)  #uni06F8	EXTENDED ARABIC-INDIC DIGIT EIGHT
        chars.append(0x06F9)  #uni06F9	EXTENDED ARABIC-INDIC DIGIT NINE
        chars.append(0x06FA)  #uni06FA	ARABIC LETTER SHEEN WITH DOT BELOW
        chars.append(0x06FB)  #uni06FB	ARABIC LETTER DAD WITH DOT BELOW
        chars.append(0x06FC)  #uni06FC	ARABIC LETTER GHAIN WITH DOT BELOW
        chars.append(0x06FD)  #uni06FD	ARABIC SIGN SINDHI AMPERSAND
        chars.append(0x06FE)  #uni06FE	ARABIC SIGN SINDHI POSTPOSITION MEN
        chars.append(0x06FF)  #uni06FF	ARABIC LETTER HEH WITH INVERTED V
        chars.append(0xFE80)  #uni0621	ARABIC LETTER HAMZA ISOLATED FORM
        chars.append(0xFE81)  #uni0622	ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
        chars.append(0xFE82)  #uni0622.fina	ARABIC LETTER ALEF WITH MADDA ABOVE FINAL FORM
        chars.append(0xFE83)  #uni0623	ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFE84)  #uni0623.fina	ARABIC LETTER ALEF WITH HAMZA ABOVE FINAL FORM
        chars.append(0xFE85)  #uni0624	ARABIC LETTER WAW WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFE86)  #uni0624.fina	ARABIC LETTER WAW WITH HAMZA ABOVE FINAL FORM
        chars.append(0xFE87)  #uni0625	ARABIC LETTER ALEF WITH HAMZA BELOW ISOLATED FORM
        chars.append(0xFE88)  #uni0625.fina	ARABIC LETTER ALEF WITH HAMZA BELOW FINAL FORM
        chars.append(0xFE89)  #uni0626	ARABIC LETTER YEH WITH HAMZA ABOVE ISOLATED FORM
        chars.append(0xFE8A)  #uni0626.fina	ARABIC LETTER YEH WITH HAMZA ABOVE FINAL FORM
        chars.append(0xFE8B)  #uni0626.init	ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
        chars.append(0xFE8C)  #uni0626.medi	ARABIC LETTER YEH WITH HAMZA ABOVE MEDIAL FORM
        chars.append(0xFE8D)  #uni0627	ARABIC LETTER ALEF ISOLATED FORM
        chars.append(0x0750)  #uni0750	ARABIC LETTER BEH WITH THREE DOTS HORIZONTALLY BELOW
        chars.append(0x0751)  #uni0751	ARABIC LETTER BEH WITH DOT BELOW AND THREE DOTS ABOVE
        chars.append(0x0752)  #uni0752	ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(0x0753)  #uni0753	ARABIC LETTER BEH WITH THREE DOTS POINTING UPWARDS BELOW AND TWO DOTS ABOVE
        chars.append(0x0754)  #uni0754	ARABIC LETTER BEH WITH TWO DOTS BELOW AND DOT ABOVE
        chars.append(0x0755)  #uni0755	ARABIC LETTER BEH WITH INVERTED SMALL V BELOW
        chars.append(0x0756)  #uni0756	ARABIC LETTER BEH WITH SMALL V
        chars.append(0x0757)  #uni0757	ARABIC LETTER HAH WITH TWO DOTS ABOVE
        chars.append(0x0758)  #uni0758	ARABIC LETTER HAH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(0x0759)  #uni0759	ARABIC LETTER DAL WITH TWO DOTS VERTICALLY BELOW AND SMALL TAH
        chars.append(0x075A)  #uni075A	ARABIC LETTER DAL WITH INVERTED SMALL V BELOW
        chars.append(0x075B)  #uni075B	ARABIC LETTER REH WITH STROKE
        chars.append(0x075C)  #uni075C	ARABIC LETTER SEEN WITH FOUR DOTS ABOVE
        chars.append(0x075D)  #uni075D	ARABIC LETTER AIN WITH TWO DOTS ABOVE
        chars.append(0x075E)  #uni075E	ARABIC LETTER AIN WITH THREE DOTS POINTING DOWNWARDS ABOVE
        chars.append(0x075F)  #uni075F	ARABIC LETTER AIN WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0x0760)  #uni0760	ARABIC LETTER FEH WITH TWO DOTS BELOW
        chars.append(0x0761)  #uni0761	ARABIC LETTER FEH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(0x0762)  #uni0762	ARABIC LETTER KEHEH WITH DOT ABOVE
        chars.append(0x0763)  #uni0763	ARABIC LETTER KEHEH WITH THREE DOTS ABOVE
        chars.append(0x0764)  #uni0764	ARABIC LETTER KEHEH WITH THREE DOTS POINTING UPWARDS BELOW
        chars.append(0x0765)  #uni0765	ARABIC LETTER MEEM WITH DOT ABOVE
        chars.append(0x0766)  #uni0766	ARABIC LETTER MEEM WITH DOT BELOW
        chars.append(0x0767)  #uni0767	ARABIC LETTER NOON WITH TWO DOTS BELOW
        chars.append(0x0768)  #uni0768	ARABIC LETTER NOON WITH SMALL TAH
        chars.append(0x0769)  #uni0769	ARABIC LETTER NOON WITH SMALL V
        chars.append(0x076A)  #uni076A	ARABIC LETTER LAM WITH BAR
        chars.append(0x076B)  #uni076B	ARABIC LETTER REH WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0x076C)  #uni076C	ARABIC LETTER REH WITH HAMZA ABOVE
        chars.append(0x076D)  #uni076D	ARABIC LETTER SEEN WITH TWO DOTS VERTICALLY ABOVE
        chars.append(0xFE93)  #uni0629	ARABIC LETTER TEH MARBUTA ISOLATED FORM
        chars.append(0xFE94)  #uni0629.fina	ARABIC LETTER TEH MARBUTA FINAL FORM
        chars.append(0xFE95)  #uni062A	ARABIC LETTER TEH ISOLATED FORM
        chars.append(0xFE96)  #uni062A.fina	ARABIC LETTER TEH FINAL FORM
        chars.append(0xFE97)  #uni062A.init	ARABIC LETTER TEH INITIAL FORM
        chars.append(0xFE98)  #uni062A.medi	ARABIC LETTER TEH MEDIAL FORM
        chars.append(0xFE99)  #uni062B	ARABIC LETTER THEH ISOLATED FORM
        chars.append(0xFE9A)  #uni062B.fina	ARABIC LETTER THEH FINAL FORM
        chars.append(0xFE9B)  #uni062B.init	ARABIC LETTER THEH INITIAL FORM
        chars.append(0xFE9C)  #uni062B.medi	ARABIC LETTER THEH MEDIAL FORM
        chars.append(0xFE9D)  #uni062C	ARABIC LETTER JEEM ISOLATED FORM
        chars.append(0xFE9E)  #uni062C.fina	ARABIC LETTER JEEM FINAL FORM
        chars.append(0xFE9F)  #uni062C.init	ARABIC LETTER JEEM INITIAL FORM
        chars.append(0xFEA0)  #uni062C.medi	ARABIC LETTER JEEM MEDIAL FORM
        chars.append(0xFEA1)  #uni062D	ARABIC LETTER HAH ISOLATED FORM
        chars.append(0xFEA2)  #uni062D.fina	ARABIC LETTER HAH FINAL FORM
        chars.append(0xFEA3)  #uni062D.init	ARABIC LETTER HAH INITIAL FORM
        chars.append(0xFEA4)  #uni062D.medi	ARABIC LETTER HAH MEDIAL FORM
        chars.append(0xFEA5)  #uni062E	ARABIC LETTER KHAH ISOLATED FORM
        chars.append(0xFEA6)  #uni062E.fina	ARABIC LETTER KHAH FINAL FORM
        chars.append(0xFEA7)  #uni062E.init	ARABIC LETTER KHAH INITIAL FORM
        chars.append(0xFEA8)  #uni062E.medi	ARABIC LETTER KHAH MEDIAL FORM
        chars.append(0xFEA9)  #uni062F	ARABIC LETTER DAL ISOLATED FORM
        chars.append(0xFEAA)  #uni062F.fina	ARABIC LETTER DAL FINAL FORM
        return chars


