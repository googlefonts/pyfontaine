# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansKaithi-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0xA830)  #uniA830	NORTH INDIC FRACTION ONE QUARTER
        chars.append(0xA831)  #uniA831	NORTH INDIC FRACTION ONE HALF
        chars.append(0xA832)  #uniA832	NORTH INDIC FRACTION THREE QUARTERS
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
        chars.append(0xA835)  #uniA835	NORTH INDIC FRACTION THREE SIXTEENTHS
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xA836)  #uniA836	NORTH INDIC QUARTER MARK
        chars.append(0xA837)  #uniA837	NORTH INDIC PLACEHOLDER MARK
        chars.append(0xA838)  #uniA838	NORTH INDIC RUPEE MARK
        chars.append(0xA839)  #uniA839	NORTH INDIC QUANTITY MARK
        chars.append(0xA834)  #uniA834	NORTH INDIC FRACTION ONE EIGHTH
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
        chars.append(0xA833)  #uniA833	NORTH INDIC FRACTION ONE SIXTEENTH
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0xA830)  #uniA830	NORTH INDIC FRACTION ONE QUARTER
        chars.append(0xA831)  #uniA831	NORTH INDIC FRACTION ONE HALF
        chars.append(0xA832)  #uniA832	NORTH INDIC FRACTION THREE QUARTERS
        chars.append(0x0033)  #three	DIGIT THREE
        chars.append(0x0034)  #four	DIGIT FOUR
        chars.append(0x0035)  #five	DIGIT FIVE
        chars.append(0x0036)  #six	DIGIT SIX
        chars.append(0x0037)  #seven	DIGIT SEVEN
        chars.append(0x0038)  #eight	DIGIT EIGHT
        chars.append(0x0039)  #nine	DIGIT NINE
        chars.append(0x11080)  #glyph00004	KAITHI SIGN CANDRABINDU
        chars.append(0x11081)  #glyph00005	KAITHI SIGN ANUSVARA
        chars.append(0x11082)  #glyph00006	KAITHI SIGN VISARGA
        chars.append(0x11083)  #glyph00007	KAITHI LETTER A
        chars.append(0x11084)  #glyph00008	KAITHI LETTER AA
        chars.append(0x11085)  #glyph00009	KAITHI LETTER I
        chars.append(0x11086)  #glyph00010	KAITHI LETTER II
        chars.append(0x11087)  #glyph00011	KAITHI LETTER U
        chars.append(0x11088)  #glyph00012	KAITHI LETTER UU
        chars.append(0x11089)  #glyph00013	KAITHI LETTER E
        chars.append(0x1108A)  #glyph00014	KAITHI LETTER AI
        chars.append(0x1108B)  #glyph00015	KAITHI LETTER O
        chars.append(0x1108C)  #glyph00016	KAITHI LETTER AU
        chars.append(0x1108D)  #glyph00017	KAITHI LETTER KA
        chars.append(0x1108E)  #glyph00018	KAITHI LETTER KHA
        chars.append(0x1108F)  #glyph00019	KAITHI LETTER GA
        chars.append(0x11090)  #glyph00020	KAITHI LETTER GHA
        chars.append(0x11091)  #glyph00021	KAITHI LETTER NGA
        chars.append(0x11092)  #glyph00022	KAITHI LETTER CA
        chars.append(0x11093)  #glyph00023	KAITHI LETTER CHA
        chars.append(0x11094)  #glyph00024	KAITHI LETTER JA
        chars.append(0x11095)  #glyph00025	KAITHI LETTER JHA
        chars.append(0x11096)  #glyph00026	KAITHI LETTER NYA
        chars.append(0x11097)  #glyph00027	KAITHI LETTER TTA
        chars.append(0x11098)  #glyph00028	KAITHI LETTER TTHA
        chars.append(0x11099)  #glyph00029	KAITHI LETTER DDA
        chars.append(0x1109A)  #glyph00030	KAITHI LETTER DDDHA
        chars.append(0x1109B)  #glyph00031	KAITHI LETTER DDHA
        chars.append(0x1109C)  #glyph00032	KAITHI LETTER RHA
        chars.append(0x1109D)  #glyph00033	KAITHI LETTER NNA
        chars.append(0x1109E)  #glyph00034	KAITHI LETTER TA
        chars.append(0x1109F)  #glyph00035	KAITHI LETTER THA
        chars.append(0x110A0)  #glyph00036	KAITHI LETTER DA
        chars.append(0x110A1)  #glyph00037	KAITHI LETTER DHA
        chars.append(0x110A2)  #glyph00038	KAITHI LETTER NA
        chars.append(0x110A3)  #glyph00039	KAITHI LETTER PA
        chars.append(0x110A4)  #glyph00040	KAITHI LETTER PHA
        chars.append(0x110A5)  #glyph00041	KAITHI LETTER BA
        chars.append(0x110A6)  #glyph00042	KAITHI LETTER BHA
        chars.append(0x110A7)  #glyph00043	KAITHI LETTER MA
        chars.append(0x110A8)  #glyph00044	KAITHI LETTER YA
        chars.append(0x110A9)  #glyph00045	KAITHI LETTER RA
        chars.append(0x110AA)  #glyph00046	KAITHI LETTER LA
        chars.append(0x110AB)  #glyph00047	KAITHI LETTER VA
        chars.append(0x110AC)  #glyph00048	KAITHI LETTER SHA
        chars.append(0x110AD)  #glyph00049	KAITHI LETTER SSA
        chars.append(0x110AE)  #glyph00050	KAITHI LETTER SA
        chars.append(0x110AF)  #glyph00051	KAITHI LETTER HA
        chars.append(0x110B0)  #glyph00052	KAITHI VOWEL SIGN AA
        chars.append(0x110B1)  #glyph00053	KAITHI VOWEL SIGN I
        chars.append(0x110B2)  #glyph00054	KAITHI VOWEL SIGN II
        chars.append(0x110B3)  #glyph00055	KAITHI VOWEL SIGN U
        chars.append(0x110B4)  #glyph00056	KAITHI VOWEL SIGN UU
        chars.append(0x110B5)  #glyph00057	KAITHI VOWEL SIGN E
        chars.append(0x110B6)  #glyph00058	KAITHI VOWEL SIGN AI
        chars.append(0x110B7)  #glyph00059	KAITHI VOWEL SIGN O
        chars.append(0x110B8)  #glyph00060	KAITHI VOWEL SIGN AU
        chars.append(0x110B9)  #glyph00061	KAITHI SIGN VIRAMA
        chars.append(0x110BA)  #glyph00062	KAITHI SIGN NUKTA
        chars.append(0x110BB)  #glyph00063	KAITHI ABBREVIATION SIGN
        chars.append(0x110BC)  #glyph00064	KAITHI ENUMERATION SIGN
        chars.append(0x110BD)  #glyph00065	KAITHI NUMBER SIGN
        chars.append(0x110BE)  #glyph00214	KAITHI SECTION MARK
        chars.append(0x110BF)  #glyph00215	KAITHI DOUBLE SECTION MARK
        chars.append(0x110C0)  #glyph00066	KAITHI DANDA
        chars.append(0x110C1)  #glyph00067	KAITHI DOUBLE DANDA
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0030)  #zero	DIGIT ZERO
        chars.append(0x0031)  #one	DIGIT ONE
        chars.append(0x0032)  #two	DIGIT TWO
        chars.append(0xA833)  #uniA833	NORTH INDIC FRACTION ONE SIXTEENTH
        chars.append(0xA834)  #uniA834	NORTH INDIC FRACTION ONE EIGHTH
        chars.append(0xA835)  #uniA835	NORTH INDIC FRACTION THREE SIXTEENTHS
        chars.append(0xA836)  #uniA836	NORTH INDIC QUARTER MARK
        chars.append(0xA837)  #uniA837	NORTH INDIC PLACEHOLDER MARK
        chars.append(0xA838)  #uniA838	NORTH INDIC RUPEE MARK
        chars.append(0xA839)  #uniA839	NORTH INDIC QUANTITY MARK
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
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        return chars


