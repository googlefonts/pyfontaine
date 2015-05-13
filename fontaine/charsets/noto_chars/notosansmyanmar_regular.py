# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansMyanmar-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #null	????
        chars.append(0x1000)  #ka	MYANMAR LETTER KA
        chars.append(0x1002)  #ga	MYANMAR LETTER GA
        chars.append(0x1003)  #gha	MYANMAR LETTER GHA
        chars.append(0x1004)  #nga	MYANMAR LETTER NGA
        chars.append(0x1005)  #ca	MYANMAR LETTER CA
        chars.append(0x1006)  #cha	MYANMAR LETTER CHA
        chars.append(0x1001)  #kha	MYANMAR LETTER KHA
        chars.append(0x1008)  #jha	MYANMAR LETTER JHA
        chars.append(0x1009)  #nya	MYANMAR LETTER NYA
        chars.append(0x100A)  #nnya	MYANMAR LETTER NNYA
        chars.append(0x100B)  #tta	MYANMAR LETTER TTA
        chars.append(0x100C)  #ttha	MYANMAR LETTER TTHA
        chars.append(0x000D)  #nonmarkingreturn	????
        chars.append(0x100E)  #ddha	MYANMAR LETTER DDHA
        chars.append(0x100F)  #nna	MYANMAR LETTER NNA
        chars.append(0x1010)  #ta	MYANMAR LETTER TA
        chars.append(0x1011)  #tha	MYANMAR LETTER THA
        chars.append(0x1012)  #da	MYANMAR LETTER DA
        chars.append(0x1013)  #dha	MYANMAR LETTER DHA
        chars.append(0x1014)  #na	MYANMAR LETTER NA
        chars.append(0x1015)  #pa	MYANMAR LETTER PA
        chars.append(0x1016)  #pha	MYANMAR LETTER PHA
        chars.append(0x1017)  #ba	MYANMAR LETTER BA
        chars.append(0x1018)  #bha	MYANMAR LETTER BHA
        chars.append(0x1019)  #ma	MYANMAR LETTER MA
        chars.append(0x101A)  #ya	MYANMAR LETTER YA
        chars.append(0x101B)  #ra	MYANMAR LETTER RA
        chars.append(0x101C)  #la	MYANMAR LETTER LA
        chars.append(0x101D)  #wa	MYANMAR LETTER WA
        chars.append(0x101E)  #sa	MYANMAR LETTER SA
        chars.append(0x101F)  #ha	MYANMAR LETTER HA
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
        chars.append(0x107F)  #ba_shn	MYANMAR LETTER SHAN BA
        chars.append(0x1080)  #tha_shn	MYANMAR LETTER SHAN THA
        chars.append(0x1081)  #ha_shn	MYANMAR LETTER SHAN HA
        chars.append(0x1082)  #medial_wa_shn	MYANMAR CONSONANT SIGN SHAN MEDIAL WA
        chars.append(0x106B)  #tone3_wpk	MYANMAR SIGN WESTERN PWO KAREN TONE-3
        chars.append(0x1084)  #e_shn	MYANMAR VOWEL SIGN SHAN E
        chars.append(0x1085)  #_e_above_shn	MYANMAR VOWEL SIGN SHAN E ABOVE
        chars.append(0x1086)  #_f_above_shn	MYANMAR VOWEL SIGN SHAN FINAL Y
        chars.append(0x1087)  #tone2_shn	MYANMAR SIGN SHAN TONE-2
        chars.append(0x1088)  #tone3_shn	MYANMAR SIGN SHAN TONE-3
        chars.append(0x106C)  #tone4_wpk	MYANMAR SIGN WESTERN PWO KAREN TONE-4
        chars.append(0x108A)  #tone6_shn	MYANMAR SIGN SHAN TONE-6
        chars.append(0x108B)  #ctone2_shn	MYANMAR SIGN SHAN COUNCIL TONE-2
        chars.append(0x108C)  #ctone3_shn	MYANMAR SIGN SHAN COUNCIL TONE-3
        chars.append(0x108D)  #etone_shn	MYANMAR SIGN SHAN COUNCIL EMPHATIC TONE
        chars.append(0x108E)  #fa_rpg	MYANMAR LETTER RUMAI PALAUNG FA
        chars.append(0x106D)  #tone5_wpk	MYANMAR SIGN WESTERN PWO KAREN TONE-5
        chars.append(0x1090)  #zero_shn	MYANMAR SHAN DIGIT ZERO
        chars.append(0x1091)  #one_shn	MYANMAR SHAN DIGIT ONE
        chars.append(0x1092)  #two_shn	MYANMAR SHAN DIGIT TWO
        chars.append(0x1093)  #three_shn	MYANMAR SHAN DIGIT THREE
        chars.append(0x1094)  #four_shn	MYANMAR SHAN DIGIT FOUR
        chars.append(0x106E)  #nna_epk	MYANMAR LETTER EASTERN PWO KAREN NNA
        chars.append(0x1096)  #six_shn	MYANMAR SHAN DIGIT SIX
        chars.append(0x1062)  #eu_skn	MYANMAR VOWEL SIGN SGAW KAREN EU
        chars.append(0x1098)  #eight_shn	MYANMAR SHAN DIGIT EIGHT
        chars.append(0x1099)  #nine_shn	MYANMAR SHAN DIGIT NINE
        chars.append(0x109A)  #tone1_khm	MYANMAR SIGN KHAMTI TONE-1
        chars.append(0x1067)  #eu_wpk	MYANMAR VOWEL SIGN WESTERN PWO KAREN EU
        chars.append(0x1056)  #_vocR_skt	MYANMAR VOWEL SIGN VOCALIC R
        chars.append(0x109D)  #_ai_atn	MYANMAR VOWEL SIGN AITON AI
        chars.append(0x109E)  #sone_shn	MYANMAR SYMBOL SHAN ONE
        chars.append(0x109F)  #exclam_shn	MYANMAR SYMBOL SHAN EXCLAMATION
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
        chars.append(0x00AD)  #uni00AD	SOFT HYPHEN
        chars.append(0x00AE)  #registered	REGISTERED SIGN
        chars.append(0x00B0)  #degree	DEGREE SIGN
        chars.append(0x00B1)  #plusminus	PLUS-MINUS SIGN
        chars.append(0x00B2)  #twosuperior	SUPERSCRIPT TWO
        chars.append(0x00B3)  #threesuperior	SUPERSCRIPT THREE
        chars.append(0x00B4)  #acute	ACUTE ACCENT
        chars.append(0xAA72)  #za_khm	MYANMAR LETTER KHAMTI ZA
        chars.append(0x00B6)  #paragraph	PILCROW SIGN
        chars.append(0x1079)  #za_shn	MYANMAR LETTER SHAN ZA
        chars.append(0x00B8)  #cedilla	CEDILLA
        chars.append(0x00B9)  #onesuperior	SUPERSCRIPT ONE
        chars.append(0x00BA)  #ordmasculine	MASCULINE ORDINAL INDICATOR
        chars.append(0x00BB)  #guillemotright	RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        chars.append(0x00BC)  #onequarter	VULGAR FRACTION ONE QUARTER
        chars.append(0x00BD)  #onehalf	VULGAR FRACTION ONE HALF
        chars.append(0x00BE)  #threequarters	VULGAR FRACTION THREE QUARTERS
        chars.append(0x1075)  #ka_shn	MYANMAR LETTER SHAN KA
        chars.append(0x1020)  #lla	MYANMAR LETTER LLA
        chars.append(0x1076)  #kha_shn	MYANMAR LETTER SHAN KHA
        chars.append(0xAA6D)  #ha_khm	MYANMAR LETTER KHAMTI HA
        chars.append(0x1021)  #a_m	MYANMAR LETTER A
        chars.append(0xAA69)  #ddha_khm	MYANMAR LETTER KHAMTI DDHA
        chars.append(0x1077)  #ga_shn	MYANMAR LETTER SHAN GA
        chars.append(0x1022)  #a_shn	MYANMAR LETTER SHAN A
        chars.append(0x1078)  #ca_shn	MYANMAR LETTER SHAN CA
        chars.append(0x109C)  #_a_atn	MYANMAR VOWEL SIGN AITON A
        chars.append(0x1023)  #i_m	MYANMAR LETTER I
        chars.append(0xAA62)  #cha_khm	MYANMAR LETTER KHAMTI CHA
        chars.append(0x1069)  #tone1_wpk	MYANMAR SIGN WESTERN PWO KAREN TONE-1
        chars.append(0x1058)  #_vocL_skt	MYANMAR VOWEL SIGN VOCALIC L
        chars.append(0x1024)  #ii	MYANMAR LETTER II
        chars.append(0x107A)  #nya_shn	MYANMAR LETTER SHAN NYA
        chars.append(0x1025)  #u_m	MYANMAR LETTER U
        chars.append(0xAA74)  #qay_khm	MYANMAR LOGOGRAM KHAMTI OAY
        chars.append(0x107B)  #da_shn	MYANMAR LETTER SHAN DA
        chars.append(0x1026)  #uu	MYANMAR LETTER UU
        chars.append(0x107C)  #na_shn	MYANMAR LETTER SHAN NA
        chars.append(0x1027)  #e_m	MYANMAR LETTER E
        chars.append(0x200C)  #afii61664	ZERO WIDTH NON-JOINER
        chars.append(0x107D)  #pha_shn	MYANMAR LETTER SHAN PHA
        chars.append(0x1028)  #e_mon	MYANMAR LETTER MON E
        chars.append(0x1060)  #_medialLa_mon	MYANMAR CONSONANT SIGN MON MEDIAL LA
        chars.append(0xAA63)  #ja_khm	MYANMAR LETTER KHAMTI JA
        chars.append(0x106A)  #tone2_wpk	MYANMAR SIGN WESTERN PWO KAREN TONE-2
        chars.append(0x1059)  #_vocLL_skt	MYANMAR VOWEL SIGN VOCALIC LL
        chars.append(0x1029)  #o_m	MYANMAR LETTER O
        chars.append(0xAA7B)  #tone_pak	MYANMAR SIGN PAO KAREN TONE
        chars.append(0x102A)  #au	MYANMAR LETTER AU
        chars.append(0xFEFF)  #null	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x102B)  #_tall_aa	MYANMAR VOWEL SIGN TALL AA
        chars.append(0x102C)  #_aa	MYANMAR VOWEL SIGN AA
        chars.append(0x102D)  #_i	MYANMAR VOWEL SIGN I
        chars.append(0xAA64)  #jha_khm	MYANMAR LETTER KHAMTI JHA
        chars.append(0x1083)  #aa_shn	MYANMAR VOWEL SIGN SHAN AA
        chars.append(0x105A)  #nga_mon	MYANMAR LETTER MON NGA
        chars.append(0x102E)  #_ii	MYANMAR VOWEL SIGN II
        chars.append(0x102F)  #_u	MYANMAR VOWEL SIGN U
        chars.append(0xAA71)  #xa_khm	MYANMAR LETTER KHAMTI XA
        chars.append(0x1030)  #_uu	MYANMAR VOWEL SIGN UU
        chars.append(0x1031)  #_e	MYANMAR VOWEL SIGN E
        chars.append(0xAA60)  #ga_khm	MYANMAR LETTER KHAMTI GA
        chars.append(0xAA77)  #exclam_atn	MYANMAR SYMBOL AITON EXCLAMATION
        chars.append(0x1032)  #_ai	MYANMAR VOWEL SIGN AI
        chars.append(0xA92E)  #uA92E	KAYAH LI SIGN CWI
        chars.append(0xAA65)  #nya_khmn	MYANMAR LETTER KHAMTI NYA
        chars.append(0x1097)  #seven_shn	MYANMAR SHAN DIGIT SEVEN
        chars.append(0x105B)  #jha_mon	MYANMAR LETTER MON JHA
        chars.append(0x1033)  #_ii_mon	MYANMAR VOWEL SIGN MON II
        chars.append(0x1089)  #tone5_shn	MYANMAR SIGN SHAN TONE-5
        chars.append(0xAA78)  #one_atn	MYANMAR SYMBOL AITON ONE
        chars.append(0x1034)  #_o_mon	MYANMAR VOWEL SIGN MON O
        chars.append(0x1035)  #_e_above	MYANMAR VOWEL SIGN E ABOVE
        chars.append(0x1036)  #anusvara	MYANMAR SIGN ANUSVARA
        chars.append(0x100D)  #dda	MYANMAR LETTER DDA
        chars.append(0x1064)  #kepho_skn	MYANMAR TONE MARK SGAW KAREN KE PHO
        chars.append(0x1037)  #dot_below	MYANMAR SIGN DOT BELOW
        chars.append(0x107E)  #fa_shn	MYANMAR LETTER SHAN FA
        chars.append(0x105C)  #bba_mon	MYANMAR LETTER MON BBA
        chars.append(0x1038)  #visarga	MYANMAR SIGN VISARGA
        chars.append(0x1074)  #ee_kyh	MYANMAR VOWEL SIGN KAYAH EE
        chars.append(0x1039)  #virama	MYANMAR SIGN VIRAMA
        chars.append(0x1007)  #ja	MYANMAR LETTER JA
        chars.append(0x108F)  #tone5_rpg	MYANMAR SIGN RUMAI PALAUNG TONE-5
        chars.append(0xAA6E)  #hha_khm	MYANMAR LETTER KHAMTI HHA
        chars.append(0x103A)  #asat	MYANMAR SIGN ASAT
        chars.append(0xAA66)  #tta_khm	MYANMAR LETTER KHAMTI TTA
        chars.append(0x103B)  #medial_ya	MYANMAR CONSONANT SIGN MEDIAL YA
        chars.append(0x1066)  #pwa_wpk	MYANMAR LETTER WESTERN PWO KAREN PWA
        chars.append(0x103C)  #medial_ra	MYANMAR CONSONANT SIGN MEDIAL RA
        chars.append(0xAA67)  #ttha_khm	MYANMAR LETTER KHAMTI TTHA
        chars.append(0x105D)  #bbe_mon	MYANMAR LETTER MON BBE
        chars.append(0x103D)  #medial_wa	MYANMAR CONSONANT SIGN MEDIAL WA
        chars.append(0xAA76)  #hm_khm	MYANMAR LOGOGRAM KHAMTI HM
        chars.append(0xAA73)  #ra_khm	MYANMAR LETTER KHAMTI RA
        chars.append(0x103E)  #medial_ha	MYANMAR CONSONANT SIGN MEDIAL HA
        chars.append(0xAA75)  #qn_khm	MYANMAR LOGOGRAM KHAMTI QN
        chars.append(0x103F)  #great_sa	MYANMAR LETTER GREAT SA
        chars.append(0x1095)  #five_shn	MYANMAR SHAN DIGIT FIVE
        chars.append(0x1040)  #zero_m	MYANMAR DIGIT ZERO
        chars.append(0x1063)  #hathi_skn	MYANMAR TONE MARK SGAW KAREN HATHI
        chars.append(0x1041)  #one_m	MYANMAR DIGIT ONE
        chars.append(0x1061)  #sha_skn	MYANMAR LETTER SGAW KAREN SHA
        chars.append(0xAA68)  #dda_khm	MYANMAR LETTER KHAMTI DDA
        chars.append(0x106F)  #ywa_epk	MYANMAR LETTER EASTERN PWO KAREN YWA
        chars.append(0x105E)  #_medialNa_mon	MYANMAR CONSONANT SIGN MON MEDIAL NA
        chars.append(0x1042)  #two_m	MYANMAR DIGIT TWO
        chars.append(0x1043)  #three_m	MYANMAR DIGIT THREE
        chars.append(0x1044)  #four_m	MYANMAR DIGIT FOUR
        chars.append(0x1045)  #five_m	MYANMAR DIGIT FIVE
        chars.append(0x1068)  #ue_wpk	MYANMAR VOWEL SIGN WESTERN PWO KAREN UE
        chars.append(0x109B)  #tone3_khm	MYANMAR SIGN KHAMTI TONE-3
        chars.append(0x1046)  #six_m	MYANMAR DIGIT SIX
        chars.append(0xAA70)  #redup_khm	MYANMAR MODIFIER LETTER KHAMTI REDUPLICATION
        chars.append(0x1057)  #_vocRR_skt	MYANMAR VOWEL SIGN VOCALIC RR
        chars.append(0xAA6C)  #sa_khm	MYANMAR LETTER KHAMTI SA
        chars.append(0x1070)  #ghwa_epk	MYANMAR LETTER EASTERN PWO KAREN GHWA
        chars.append(0x105F)  #_medialMa_mon	MYANMAR CONSONANT SIGN MON MEDIAL MA
        chars.append(0x1047)  #seven_m	MYANMAR DIGIT SEVEN
        chars.append(0x1048)  #eight_m	MYANMAR DIGIT EIGHT
        chars.append(0x1049)  #nine_m	MYANMAR DIGIT NINE
        chars.append(0x104A)  #little_section	MYANMAR SIGN LITTLE SECTION
        chars.append(0xAA61)  #ca_khm	MYANMAR LETTER KHAMTI CA
        chars.append(0x104B)  #big_section	MYANMAR SIGN SECTION
        chars.append(0xAA6A)  #dha_khm	MYANMAR LETTER KHAMTI DHA
        chars.append(0x1071)  #i_gkn	MYANMAR VOWEL SIGN GEBA KAREN I
        chars.append(0x104C)  #locative	MYANMAR SYMBOL LOCATIVE
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0xAA79)  #two_atn	MYANMAR SYMBOL AITON TWO
        chars.append(0x104D)  #completed	MYANMAR SYMBOL COMPLETED
        chars.append(0x104E)  #aforementioned	MYANMAR SYMBOL AFOREMENTIONED
        chars.append(0x200D)  #afii301	ZERO WIDTH JOINER
        chars.append(0x104F)  #genitive	MYANMAR SYMBOL GENITIVE
        chars.append(0x1065)  #tha_wpk	MYANMAR LETTER WESTERN PWO KAREN THA
        chars.append(0x1050)  #sha_skt	MYANMAR LETTER SHA
        chars.append(0xAA6B)  #na_khm	MYANMAR LETTER KHAMTI NA
        chars.append(0x1072)  #oe_kyh	MYANMAR VOWEL SIGN KAYAH OE
        chars.append(0x1051)  #ssa_skt	MYANMAR LETTER SSA
        chars.append(0x1052)  #vocR_skt	MYANMAR LETTER VOCALIC R
        chars.append(0xAA6F)  #fa_khm	MYANMAR LETTER KHAMTI FA
        chars.append(0x1053)  #vocRR_skt	MYANMAR LETTER VOCALIC RR
        chars.append(0xAA7A)  #ra_atn	MYANMAR LETTER AITON RA
        chars.append(0x1054)  #vocL_skt	MYANMAR LETTER VOCALIC L
        chars.append(0x1073)  #u_kyh	MYANMAR VOWEL SIGN KAYAH U
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x1055)  #vocLL_skt	MYANMAR LETTER VOCALIC LL
        return chars


