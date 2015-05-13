# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansThaana-Bold'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #null	????
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x060C)  #uni060C	ARABIC COMMA
        chars.append(0x000D)  #nonmarkingreturn	????
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x2018)  #quoteleft	LEFT SINGLE QUOTATION MARK
        chars.append(0x2019)  #quoteright	RIGHT SINGLE QUOTATION MARK
        chars.append(0x061B)  #uni061B	ARABIC SEMICOLON
        chars.append(0x061C)  #uni061C	????
        chars.append(0x201D)  #quotedblright	RIGHT DOUBLE QUOTATION MARK
        chars.append(0x061F)  #uni061F	ARABIC QUESTION MARK
        chars.append(0x0020)  #space	SPACE
        chars.append(0x0021)  #exclam	EXCLAMATION MARK
        chars.append(0x0028)  #parenleft	LEFT PARENTHESIS
        chars.append(0x0029)  #parenright	RIGHT PARENTHESIS
        chars.append(0x002C)  #comma	COMMA
        chars.append(0x002E)  #period	FULL STOP
        chars.append(0x003A)  #colon	COLON
        chars.append(0x003B)  #semicolon	SEMICOLON
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
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
        chars.append(0x00A0)  #space	NO-BREAK SPACE
        chars.append(0x201C)  #quotedblleft	LEFT DOUBLE QUOTATION MARK
        chars.append(0xFEFF)  #null	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0780)  #uni0780	THAANA LETTER HAA
        chars.append(0x0781)  #uni0781	THAANA LETTER SHAVIYANI
        chars.append(0x0782)  #uni0782	THAANA LETTER NOONU
        chars.append(0x0783)  #uni0783	THAANA LETTER RAA
        chars.append(0x0784)  #uni0784	THAANA LETTER BAA
        chars.append(0x0785)  #uni0785	THAANA LETTER LHAVIYANI
        chars.append(0x0786)  #uni0786	THAANA LETTER KAAFU
        chars.append(0x0787)  #uni0787	THAANA LETTER ALIFU
        chars.append(0x0788)  #uni0788	THAANA LETTER VAAVU
        chars.append(0x0789)  #uni0789	THAANA LETTER MEEMU
        chars.append(0x078A)  #uni078A	THAANA LETTER FAAFU
        chars.append(0x078B)  #uni078B	THAANA LETTER DHAALU
        chars.append(0x078C)  #uni078C	THAANA LETTER THAA
        chars.append(0x078D)  #uni078D	THAANA LETTER LAAMU
        chars.append(0x078E)  #uni078E	THAANA LETTER GAAFU
        chars.append(0x078F)  #uni078F	THAANA LETTER GNAVIYANI
        chars.append(0x0790)  #uni0790	THAANA LETTER SEENU
        chars.append(0x0791)  #uni0791	THAANA LETTER DAVIYANI
        chars.append(0x0792)  #uni0792	THAANA LETTER ZAVIYANI
        chars.append(0x0793)  #uni0793	THAANA LETTER TAVIYANI
        chars.append(0x0794)  #uni0794	THAANA LETTER YAA
        chars.append(0x0795)  #uni0795	THAANA LETTER PAVIYANI
        chars.append(0x0796)  #uni0796	THAANA LETTER JAVIYANI
        chars.append(0x0797)  #uni0797	THAANA LETTER CHAVIYANI
        chars.append(0x0798)  #uni0798	THAANA LETTER TTAA
        chars.append(0x0799)  #uni0799	THAANA LETTER HHAA
        chars.append(0x079A)  #uni079A	THAANA LETTER KHAA
        chars.append(0x079B)  #uni079B	THAANA LETTER THAALU
        chars.append(0x079C)  #uni079C	THAANA LETTER ZAA
        chars.append(0x079D)  #uni079D	THAANA LETTER SHEENU
        chars.append(0x079E)  #uni079E	THAANA LETTER SAADHU
        chars.append(0x079F)  #uni079F	THAANA LETTER DAADHU
        chars.append(0x07A0)  #uni07A0	THAANA LETTER TO
        chars.append(0x07A1)  #uni07A1	THAANA LETTER ZO
        chars.append(0x07A2)  #uni07A2	THAANA LETTER AINU
        chars.append(0x07A3)  #uni07A3	THAANA LETTER GHAINU
        chars.append(0x07A4)  #uni07A4	THAANA LETTER QAAFU
        chars.append(0x07A5)  #uni07A5	THAANA LETTER WAAVU
        chars.append(0x07A6)  #uni07A6	THAANA ABAFILI
        chars.append(0x07A7)  #uni07A7	THAANA AABAAFILI
        chars.append(0x07A8)  #uni07A8	THAANA IBIFILI
        chars.append(0x07A9)  #uni07A9	THAANA EEBEEFILI
        chars.append(0x07AA)  #uni07AA	THAANA UBUFILI
        chars.append(0x07AB)  #uni07AB	THAANA OOBOOFILI
        chars.append(0x07AC)  #uni07AC	THAANA EBEFILI
        chars.append(0x07AD)  #uni07AD	THAANA EYBEYFILI
        chars.append(0x07AE)  #uni07AE	THAANA OBOFILI
        chars.append(0x07AF)  #uni07AF	THAANA OABOAFILI
        chars.append(0x07B0)  #uni07B0	THAANA SUKUN
        chars.append(0x07B1)  #uni07B1	THAANA LETTER NAA
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0xFDF2)  #uniFDF2	ARABIC LIGATURE ALLAH ISOLATED FORM
        chars.append(0xFDFD)  #uniFDFD	ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM
        return chars


