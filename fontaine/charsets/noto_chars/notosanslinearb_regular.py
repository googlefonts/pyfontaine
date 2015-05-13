# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansLinearB-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10000)  #glyph00004	LINEAR B SYLLABLE B008 A
        chars.append(0x10002)  #glyph00006	LINEAR B SYLLABLE B028 I
        chars.append(0x10003)  #glyph00007	LINEAR B SYLLABLE B061 O
        chars.append(0x10004)  #glyph00008	LINEAR B SYLLABLE B010 U
        chars.append(0x10005)  #glyph00009	LINEAR B SYLLABLE B001 DA
        chars.append(0x10006)  #glyph00010	LINEAR B SYLLABLE B045 DE
        chars.append(0x10001)  #glyph00005	LINEAR B SYLLABLE B038 E
        chars.append(0x10008)  #glyph00012	LINEAR B SYLLABLE B014 DO
        chars.append(0x10009)  #glyph00013	LINEAR B SYLLABLE B051 DU
        chars.append(0x1000A)  #glyph00014	LINEAR B SYLLABLE B057 JA
        chars.append(0x1000B)  #glyph00015	LINEAR B SYLLABLE B046 JE
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1000E)  #glyph00017	LINEAR B SYLLABLE B065 JU
        chars.append(0x1000F)  #glyph00018	LINEAR B SYLLABLE B077 KA
        chars.append(0x10010)  #glyph00019	LINEAR B SYLLABLE B044 KE
        chars.append(0x10011)  #glyph00020	LINEAR B SYLLABLE B067 KI
        chars.append(0x10012)  #glyph00021	LINEAR B SYLLABLE B070 KO
        chars.append(0x10013)  #glyph00022	LINEAR B SYLLABLE B081 KU
        chars.append(0x10014)  #glyph00023	LINEAR B SYLLABLE B080 MA
        chars.append(0x10015)  #glyph00024	LINEAR B SYLLABLE B013 ME
        chars.append(0x10016)  #glyph00025	LINEAR B SYLLABLE B073 MI
        chars.append(0x10017)  #glyph00026	LINEAR B SYLLABLE B015 MO
        chars.append(0x10018)  #glyph00027	LINEAR B SYLLABLE B023 MU
        chars.append(0x10019)  #glyph00028	LINEAR B SYLLABLE B006 NA
        chars.append(0x1001A)  #glyph00029	LINEAR B SYLLABLE B024 NE
        chars.append(0x1001B)  #glyph00030	LINEAR B SYLLABLE B030 NI
        chars.append(0x1001C)  #glyph00031	LINEAR B SYLLABLE B052 NO
        chars.append(0x1001D)  #glyph00032	LINEAR B SYLLABLE B055 NU
        chars.append(0x1001E)  #glyph00033	LINEAR B SYLLABLE B003 PA
        chars.append(0x1001F)  #glyph00034	LINEAR B SYLLABLE B072 PE
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10021)  #glyph00036	LINEAR B SYLLABLE B011 PO
        chars.append(0x10022)  #glyph00037	LINEAR B SYLLABLE B050 PU
        chars.append(0x10023)  #glyph00038	LINEAR B SYLLABLE B016 QA
        chars.append(0x10024)  #glyph00039	LINEAR B SYLLABLE B078 QE
        chars.append(0x10025)  #glyph00040	LINEAR B SYLLABLE B021 QI
        chars.append(0x10026)  #glyph00041	LINEAR B SYLLABLE B032 QO
        chars.append(0x10028)  #glyph00042	LINEAR B SYLLABLE B060 RA
        chars.append(0x10029)  #glyph00043	LINEAR B SYLLABLE B027 RE
        chars.append(0x1002A)  #glyph00044	LINEAR B SYLLABLE B053 RI
        chars.append(0x10007)  #glyph00011	LINEAR B SYLLABLE B007 DI
        chars.append(0x1002C)  #glyph00046	LINEAR B SYLLABLE B026 RU
        chars.append(0x1002D)  #glyph00047	LINEAR B SYLLABLE B031 SA
        chars.append(0x1002E)  #glyph00048	LINEAR B SYLLABLE B009 SE
        chars.append(0x1002F)  #glyph00049	LINEAR B SYLLABLE B041 SI
        chars.append(0x10030)  #glyph00050	LINEAR B SYLLABLE B012 SO
        chars.append(0x10031)  #glyph00051	LINEAR B SYLLABLE B058 SU
        chars.append(0x10032)  #glyph00052	LINEAR B SYLLABLE B059 TA
        chars.append(0x10033)  #glyph00053	LINEAR B SYLLABLE B004 TE
        chars.append(0x10034)  #glyph00054	LINEAR B SYLLABLE B037 TI
        chars.append(0x10035)  #glyph00055	LINEAR B SYLLABLE B005 TO
        chars.append(0x10036)  #glyph00056	LINEAR B SYLLABLE B069 TU
        chars.append(0x10037)  #glyph00057	LINEAR B SYLLABLE B054 WA
        chars.append(0x10038)  #glyph00058	LINEAR B SYLLABLE B075 WE
        chars.append(0x10039)  #glyph00059	LINEAR B SYLLABLE B040 WI
        chars.append(0x1003A)  #glyph00060	LINEAR B SYLLABLE B042 WO
        chars.append(0x1003C)  #glyph00061	LINEAR B SYLLABLE B017 ZA
        chars.append(0x1003D)  #glyph00062	LINEAR B SYLLABLE B074 ZE
        chars.append(0x1003F)  #glyph00063	LINEAR B SYLLABLE B020 ZO
        chars.append(0x10040)  #glyph00064	LINEAR B SYLLABLE B025 A2
        chars.append(0x10041)  #glyph00065	LINEAR B SYLLABLE B043 A3
        chars.append(0x10042)  #glyph00066	LINEAR B SYLLABLE B085 AU
        chars.append(0x10043)  #glyph00067	LINEAR B SYLLABLE B071 DWE
        chars.append(0x10044)  #glyph00068	LINEAR B SYLLABLE B090 DWO
        chars.append(0x10045)  #glyph00069	LINEAR B SYLLABLE B048 NWA
        chars.append(0x10046)  #glyph00070	LINEAR B SYLLABLE B029 PU2
        chars.append(0x10047)  #glyph00071	LINEAR B SYLLABLE B062 PTE
        chars.append(0x10048)  #glyph00072	LINEAR B SYLLABLE B076 RA2
        chars.append(0x10049)  #glyph00073	LINEAR B SYLLABLE B033 RA3
        chars.append(0x1004A)  #glyph00074	LINEAR B SYLLABLE B068 RO2
        chars.append(0x1004B)  #glyph00075	LINEAR B SYLLABLE B066 TA2
        chars.append(0x1004C)  #glyph00076	LINEAR B SYLLABLE B087 TWE
        chars.append(0x1004D)  #glyph00077	LINEAR B SYLLABLE B091 TWO
        chars.append(0x1000D)  #glyph00016	LINEAR B SYLLABLE B036 JO
        chars.append(0x10050)  #glyph00078	LINEAR B SYMBOL B018
        chars.append(0x10051)  #glyph00079	LINEAR B SYMBOL B019
        chars.append(0x10052)  #glyph00080	LINEAR B SYMBOL B022
        chars.append(0x10053)  #glyph00081	LINEAR B SYMBOL B034
        chars.append(0x10054)  #glyph00082	LINEAR B SYMBOL B047
        chars.append(0x10055)  #glyph00083	LINEAR B SYMBOL B049
        chars.append(0x10056)  #glyph00084	LINEAR B SYMBOL B056
        chars.append(0x10057)  #glyph00085	LINEAR B SYMBOL B063
        chars.append(0x10058)  #glyph00086	LINEAR B SYMBOL B064
        chars.append(0x10059)  #glyph00087	LINEAR B SYMBOL B079
        chars.append(0x1005A)  #glyph00088	LINEAR B SYMBOL B082
        chars.append(0x1005B)  #glyph00089	LINEAR B SYMBOL B083
        chars.append(0x1005C)  #glyph00090	LINEAR B SYMBOL B086
        chars.append(0x1005D)  #glyph00091	LINEAR B SYMBOL B089
        chars.append(0x10080)  #glyph00092	LINEAR B IDEOGRAM B100 MAN
        chars.append(0x10081)  #glyph00093	LINEAR B IDEOGRAM B102 WOMAN
        chars.append(0x10082)  #glyph00094	LINEAR B IDEOGRAM B104 DEER
        chars.append(0x10083)  #glyph00095	LINEAR B IDEOGRAM B105 EQUID
        chars.append(0x10084)  #glyph00096	LINEAR B IDEOGRAM B105F MARE
        chars.append(0x10085)  #glyph00097	LINEAR B IDEOGRAM B105M STALLION
        chars.append(0x10086)  #glyph00098	LINEAR B IDEOGRAM B106F EWE
        chars.append(0x10087)  #glyph00099	LINEAR B IDEOGRAM B106M RAM
        chars.append(0x10088)  #glyph00100	LINEAR B IDEOGRAM B107F SHE-GOAT
        chars.append(0x10089)  #glyph00101	LINEAR B IDEOGRAM B107M HE-GOAT
        chars.append(0x1008A)  #glyph00102	LINEAR B IDEOGRAM B108F SOW
        chars.append(0x1008B)  #glyph00103	LINEAR B IDEOGRAM B108M BOAR
        chars.append(0x1008C)  #glyph00104	LINEAR B IDEOGRAM B109F COW
        chars.append(0x1008D)  #glyph00105	LINEAR B IDEOGRAM B109M BULL
        chars.append(0x1008E)  #glyph00106	LINEAR B IDEOGRAM B120 WHEAT
        chars.append(0x1008F)  #glyph00107	LINEAR B IDEOGRAM B121 BARLEY
        chars.append(0x10090)  #glyph00108	LINEAR B IDEOGRAM B122 OLIVE
        chars.append(0x10091)  #glyph00109	LINEAR B IDEOGRAM B123 SPICE
        chars.append(0x10092)  #glyph00110	LINEAR B IDEOGRAM B125 CYPERUS
        chars.append(0x10093)  #glyph00111	LINEAR B MONOGRAM B127 KAPO
        chars.append(0x10094)  #glyph00112	LINEAR B MONOGRAM B128 KANAKO
        chars.append(0x10095)  #glyph00113	LINEAR B IDEOGRAM B130 OIL
        chars.append(0x10096)  #glyph00114	LINEAR B IDEOGRAM B131 WINE
        chars.append(0x10097)  #glyph00115	LINEAR B IDEOGRAM B132
        chars.append(0x10098)  #glyph00116	LINEAR B MONOGRAM B133 AREPA
        chars.append(0x10099)  #glyph00117	LINEAR B MONOGRAM B135 MERI
        chars.append(0x1009A)  #glyph00118	LINEAR B IDEOGRAM B140 BRONZE
        chars.append(0x1009B)  #glyph00119	LINEAR B IDEOGRAM B141 GOLD
        chars.append(0x1009C)  #glyph00120	LINEAR B IDEOGRAM B142
        chars.append(0x1009D)  #glyph00121	LINEAR B IDEOGRAM B145 WOOL
        chars.append(0x1009E)  #glyph00122	LINEAR B IDEOGRAM B146
        chars.append(0x1009F)  #glyph00123	LINEAR B IDEOGRAM B150
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x100A1)  #glyph00125	LINEAR B IDEOGRAM B152
        chars.append(0x100A2)  #glyph00126	LINEAR B IDEOGRAM B153
        chars.append(0x100A3)  #glyph00127	LINEAR B IDEOGRAM B154
        chars.append(0x100A4)  #glyph00128	LINEAR B MONOGRAM B156 TURO2
        chars.append(0x100A5)  #glyph00129	LINEAR B IDEOGRAM B157
        chars.append(0x100A6)  #glyph00130	LINEAR B IDEOGRAM B158
        chars.append(0x100A7)  #glyph00131	LINEAR B IDEOGRAM B159 CLOTH
        chars.append(0x100A8)  #glyph00132	LINEAR B IDEOGRAM B160
        chars.append(0x100A9)  #glyph00133	LINEAR B IDEOGRAM B161
        chars.append(0x100AA)  #glyph00134	LINEAR B IDEOGRAM B162 GARMENT
        chars.append(0x100AB)  #glyph00135	LINEAR B IDEOGRAM B163 ARMOUR
        chars.append(0x100AC)  #glyph00136	LINEAR B IDEOGRAM B164
        chars.append(0x100AD)  #glyph00137	LINEAR B IDEOGRAM B165
        chars.append(0x100AE)  #glyph00138	LINEAR B IDEOGRAM B166
        chars.append(0x100AF)  #glyph00139	LINEAR B IDEOGRAM B167
        chars.append(0x100B0)  #glyph00140	LINEAR B IDEOGRAM B168
        chars.append(0x100B1)  #glyph00141	LINEAR B IDEOGRAM B169
        chars.append(0x100B2)  #glyph00142	LINEAR B IDEOGRAM B170
        chars.append(0x100B3)  #glyph00143	LINEAR B IDEOGRAM B171
        chars.append(0x100B4)  #glyph00144	LINEAR B IDEOGRAM B172
        chars.append(0x100B5)  #glyph00145	LINEAR B IDEOGRAM B173 MONTH
        chars.append(0x100B6)  #glyph00146	LINEAR B IDEOGRAM B174
        chars.append(0x100B7)  #glyph00147	LINEAR B IDEOGRAM B176 TREE
        chars.append(0x100B8)  #glyph00148	LINEAR B IDEOGRAM B177
        chars.append(0x100B9)  #glyph00149	LINEAR B IDEOGRAM B178
        chars.append(0x100BA)  #glyph00150	LINEAR B IDEOGRAM B179
        chars.append(0x100BB)  #glyph00151	LINEAR B IDEOGRAM B180
        chars.append(0x100BC)  #glyph00152	LINEAR B IDEOGRAM B181
        chars.append(0x100BD)  #glyph00153	LINEAR B IDEOGRAM B182
        chars.append(0x100BE)  #glyph00154	LINEAR B IDEOGRAM B183
        chars.append(0x100BF)  #glyph00155	LINEAR B IDEOGRAM B184
        chars.append(0x100C0)  #glyph00156	LINEAR B IDEOGRAM B185
        chars.append(0x10020)  #glyph00035	LINEAR B SYLLABLE B039 PI
        chars.append(0x100C2)  #glyph00158	LINEAR B IDEOGRAM B190
        chars.append(0x100C3)  #glyph00159	LINEAR B IDEOGRAM B191 HELMET
        chars.append(0x100C4)  #glyph00160	LINEAR B IDEOGRAM B220 FOOTSTOOL
        chars.append(0x100C5)  #glyph00161	LINEAR B IDEOGRAM B225 BATHTUB
        chars.append(0x100C6)  #glyph00162	LINEAR B IDEOGRAM B230 SPEAR
        chars.append(0x100C7)  #glyph00163	LINEAR B IDEOGRAM B231 ARROW
        chars.append(0x100C8)  #glyph00164	LINEAR B IDEOGRAM B232
        chars.append(0x100C9)  #glyph00165	LINEAR B IDEOGRAM B233 SWORD
        chars.append(0x100CA)  #glyph00166	LINEAR B IDEOGRAM B234
        chars.append(0x100CB)  #glyph00167	LINEAR B IDEOGRAM B236
        chars.append(0x100CC)  #glyph00168	LINEAR B IDEOGRAM B240 WHEELED CHARIOT
        chars.append(0x100CD)  #glyph00169	LINEAR B IDEOGRAM B241 CHARIOT
        chars.append(0x100CE)  #glyph00170	LINEAR B IDEOGRAM B242 CHARIOT FRAME
        chars.append(0x100CF)  #glyph00171	LINEAR B IDEOGRAM B243 WHEEL
        chars.append(0x100D0)  #glyph00172	LINEAR B IDEOGRAM B245
        chars.append(0x100D1)  #glyph00173	LINEAR B IDEOGRAM B246
        chars.append(0x100D2)  #glyph00174	LINEAR B MONOGRAM B247 DIPTE
        chars.append(0x100D3)  #glyph00175	LINEAR B IDEOGRAM B248
        chars.append(0x100D4)  #glyph00176	LINEAR B IDEOGRAM B249
        chars.append(0x100D5)  #glyph00177	LINEAR B IDEOGRAM B251
        chars.append(0x100D6)  #glyph00178	LINEAR B IDEOGRAM B252
        chars.append(0x100D7)  #glyph00179	LINEAR B IDEOGRAM B253
        chars.append(0x100D8)  #glyph00180	LINEAR B IDEOGRAM B254 DART
        chars.append(0x100D9)  #glyph00181	LINEAR B IDEOGRAM B255
        chars.append(0x100DA)  #glyph00182	LINEAR B IDEOGRAM B256
        chars.append(0x100DB)  #glyph00183	LINEAR B IDEOGRAM B257
        chars.append(0x100DC)  #glyph00184	LINEAR B IDEOGRAM B258
        chars.append(0x100DD)  #glyph00185	LINEAR B IDEOGRAM B259
        chars.append(0x100DE)  #glyph00186	LINEAR B IDEOGRAM VESSEL B155
        chars.append(0x100DF)  #glyph00187	LINEAR B IDEOGRAM VESSEL B200
        chars.append(0x100E0)  #glyph00188	LINEAR B IDEOGRAM VESSEL B201
        chars.append(0x100E1)  #glyph00189	LINEAR B IDEOGRAM VESSEL B202
        chars.append(0x100E2)  #glyph00190	LINEAR B IDEOGRAM VESSEL B203
        chars.append(0x100E3)  #glyph00191	LINEAR B IDEOGRAM VESSEL B204
        chars.append(0x100E4)  #glyph00192	LINEAR B IDEOGRAM VESSEL B205
        chars.append(0x100E5)  #glyph00193	LINEAR B IDEOGRAM VESSEL B206
        chars.append(0x100E6)  #glyph00194	LINEAR B IDEOGRAM VESSEL B207
        chars.append(0x100E7)  #glyph00195	LINEAR B IDEOGRAM VESSEL B208
        chars.append(0x100E8)  #glyph00196	LINEAR B IDEOGRAM VESSEL B209
        chars.append(0x100E9)  #glyph00197	LINEAR B IDEOGRAM VESSEL B210
        chars.append(0x100EA)  #glyph00198	LINEAR B IDEOGRAM VESSEL B211
        chars.append(0x100EB)  #glyph00199	LINEAR B IDEOGRAM VESSEL B212
        chars.append(0x100EC)  #glyph00200	LINEAR B IDEOGRAM VESSEL B213
        chars.append(0x100ED)  #glyph00201	LINEAR B IDEOGRAM VESSEL B214
        chars.append(0x100EE)  #glyph00202	LINEAR B IDEOGRAM VESSEL B215
        chars.append(0x100EF)  #glyph00203	LINEAR B IDEOGRAM VESSEL B216
        chars.append(0x100F0)  #glyph00204	LINEAR B IDEOGRAM VESSEL B217
        chars.append(0x100F1)  #glyph00205	LINEAR B IDEOGRAM VESSEL B218
        chars.append(0x100F2)  #glyph00206	LINEAR B IDEOGRAM VESSEL B219
        chars.append(0x100F3)  #glyph00207	LINEAR B IDEOGRAM VESSEL B221
        chars.append(0x100F4)  #glyph00208	LINEAR B IDEOGRAM VESSEL B222
        chars.append(0x100F5)  #glyph00209	LINEAR B IDEOGRAM VESSEL B226
        chars.append(0x100F6)  #glyph00210	LINEAR B IDEOGRAM VESSEL B227
        chars.append(0x100F7)  #glyph00211	LINEAR B IDEOGRAM VESSEL B228
        chars.append(0x100F8)  #glyph00212	LINEAR B IDEOGRAM VESSEL B229
        chars.append(0x100F9)  #glyph00213	LINEAR B IDEOGRAM VESSEL B250
        chars.append(0x100FA)  #glyph00214	LINEAR B IDEOGRAM VESSEL B305
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x10100)  #glyph00215	AEGEAN WORD SEPARATOR LINE
        chars.append(0x10101)  #glyph00216	AEGEAN WORD SEPARATOR DOT
        chars.append(0x10102)  #glyph00217	AEGEAN CHECK MARK
        chars.append(0x1002B)  #glyph00045	LINEAR B SYLLABLE B002 RO
        chars.append(0x10107)  #glyph00218	AEGEAN NUMBER ONE
        chars.append(0x10108)  #glyph00219	AEGEAN NUMBER TWO
        chars.append(0x10109)  #glyph00220	AEGEAN NUMBER THREE
        chars.append(0x1010A)  #glyph00221	AEGEAN NUMBER FOUR
        chars.append(0x1010B)  #glyph00222	AEGEAN NUMBER FIVE
        chars.append(0x1010C)  #glyph00223	AEGEAN NUMBER SIX
        chars.append(0x1010D)  #glyph00224	AEGEAN NUMBER SEVEN
        chars.append(0x1010E)  #glyph00225	AEGEAN NUMBER EIGHT
        chars.append(0x1010F)  #glyph00226	AEGEAN NUMBER NINE
        chars.append(0x10110)  #glyph00227	AEGEAN NUMBER TEN
        chars.append(0x10111)  #glyph00228	AEGEAN NUMBER TWENTY
        chars.append(0x10112)  #glyph00229	AEGEAN NUMBER THIRTY
        chars.append(0x10113)  #glyph00230	AEGEAN NUMBER FORTY
        chars.append(0x10114)  #glyph00231	AEGEAN NUMBER FIFTY
        chars.append(0x10115)  #glyph00232	AEGEAN NUMBER SIXTY
        chars.append(0x10116)  #glyph00233	AEGEAN NUMBER SEVENTY
        chars.append(0x10117)  #glyph00234	AEGEAN NUMBER EIGHTY
        chars.append(0x10118)  #glyph00235	AEGEAN NUMBER NINETY
        chars.append(0x10119)  #glyph00236	AEGEAN NUMBER ONE HUNDRED
        chars.append(0x1011A)  #glyph00237	AEGEAN NUMBER TWO HUNDRED
        chars.append(0x1011B)  #glyph00238	AEGEAN NUMBER THREE HUNDRED
        chars.append(0x1011C)  #glyph00239	AEGEAN NUMBER FOUR HUNDRED
        chars.append(0x1011D)  #glyph00240	AEGEAN NUMBER FIVE HUNDRED
        chars.append(0x1011E)  #glyph00241	AEGEAN NUMBER SIX HUNDRED
        chars.append(0x1011F)  #glyph00242	AEGEAN NUMBER SEVEN HUNDRED
        chars.append(0x10120)  #glyph00243	AEGEAN NUMBER EIGHT HUNDRED
        chars.append(0x10121)  #glyph00244	AEGEAN NUMBER NINE HUNDRED
        chars.append(0x10122)  #glyph00245	AEGEAN NUMBER ONE THOUSAND
        chars.append(0x10123)  #glyph00246	AEGEAN NUMBER TWO THOUSAND
        chars.append(0x10124)  #glyph00247	AEGEAN NUMBER THREE THOUSAND
        chars.append(0x10125)  #glyph00248	AEGEAN NUMBER FOUR THOUSAND
        chars.append(0x10126)  #glyph00249	AEGEAN NUMBER FIVE THOUSAND
        chars.append(0x10127)  #glyph00250	AEGEAN NUMBER SIX THOUSAND
        chars.append(0x10128)  #glyph00251	AEGEAN NUMBER SEVEN THOUSAND
        chars.append(0x10129)  #glyph00252	AEGEAN NUMBER EIGHT THOUSAND
        chars.append(0x1012A)  #glyph00253	AEGEAN NUMBER NINE THOUSAND
        chars.append(0x1012B)  #glyph00254	AEGEAN NUMBER TEN THOUSAND
        chars.append(0x1012C)  #glyph00255	AEGEAN NUMBER TWENTY THOUSAND
        chars.append(0x1012D)  #glyph00256	AEGEAN NUMBER THIRTY THOUSAND
        chars.append(0x1012E)  #glyph00257	AEGEAN NUMBER FORTY THOUSAND
        chars.append(0x1012F)  #glyph00258	AEGEAN NUMBER FIFTY THOUSAND
        chars.append(0x10130)  #glyph00259	AEGEAN NUMBER SIXTY THOUSAND
        chars.append(0x10131)  #glyph00260	AEGEAN NUMBER SEVENTY THOUSAND
        chars.append(0x10132)  #glyph00261	AEGEAN NUMBER EIGHTY THOUSAND
        chars.append(0x10133)  #glyph00262	AEGEAN NUMBER NINETY THOUSAND
        chars.append(0x10137)  #glyph00263	AEGEAN WEIGHT BASE UNIT
        chars.append(0x10138)  #glyph00264	AEGEAN WEIGHT FIRST SUBUNIT
        chars.append(0x10139)  #glyph00265	AEGEAN WEIGHT SECOND SUBUNIT
        chars.append(0x1013A)  #glyph00266	AEGEAN WEIGHT THIRD SUBUNIT
        chars.append(0x1013B)  #glyph00267	AEGEAN WEIGHT FOURTH SUBUNIT
        chars.append(0x1013C)  #glyph00268	AEGEAN DRY MEASURE FIRST SUBUNIT
        chars.append(0x1013D)  #glyph00269	AEGEAN LIQUID MEASURE FIRST SUBUNIT
        chars.append(0x1013E)  #glyph00270	AEGEAN MEASURE SECOND SUBUNIT
        chars.append(0x1013F)  #glyph00271	AEGEAN MEASURE THIRD SUBUNIT
        chars.append(0x100C1)  #glyph00157	LINEAR B IDEOGRAM B189
        chars.append(0x100A0)  #glyph00124	LINEAR B IDEOGRAM B151 HORN
        return chars


