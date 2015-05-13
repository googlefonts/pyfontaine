# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansCuneiform-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x12000)  #glyph00004	CUNEIFORM SIGN A
        chars.append(0x12002)  #glyph00006	CUNEIFORM SIGN A TIMES BAD
        chars.append(0x12003)  #glyph00007	CUNEIFORM SIGN A TIMES GAN2 TENU
        chars.append(0x12004)  #glyph00008	CUNEIFORM SIGN A TIMES HA
        chars.append(0x12005)  #glyph00009	CUNEIFORM SIGN A TIMES IGI
        chars.append(0x12006)  #glyph00010	CUNEIFORM SIGN A TIMES LAGAR GUNU
        chars.append(0x12001)  #glyph00005	CUNEIFORM SIGN A TIMES A
        chars.append(0x12008)  #glyph00012	CUNEIFORM SIGN A TIMES SAG
        chars.append(0x12009)  #glyph00013	CUNEIFORM SIGN A2
        chars.append(0x1200A)  #glyph00014	CUNEIFORM SIGN AB
        chars.append(0x1200B)  #glyph00015	CUNEIFORM SIGN AB TIMES ASH2
        chars.append(0x1200C)  #glyph00016	CUNEIFORM SIGN AB TIMES DUN3 GUNU
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1200E)  #glyph00018	CUNEIFORM SIGN AB TIMES GAN2 TENU
        chars.append(0x1200F)  #glyph00019	CUNEIFORM SIGN AB TIMES HA
        chars.append(0x12010)  #glyph00020	CUNEIFORM SIGN AB TIMES IGI GUNU
        chars.append(0x12011)  #glyph00021	CUNEIFORM SIGN AB TIMES IMIN
        chars.append(0x12012)  #glyph00022	CUNEIFORM SIGN AB TIMES LAGAB
        chars.append(0x12013)  #glyph00023	CUNEIFORM SIGN AB TIMES SHESH
        chars.append(0x12014)  #glyph00024	CUNEIFORM SIGN AB TIMES U PLUS U PLUS U
        chars.append(0x12015)  #glyph00025	CUNEIFORM SIGN AB GUNU
        chars.append(0x12016)  #glyph00026	CUNEIFORM SIGN AB2
        chars.append(0x12017)  #glyph00027	CUNEIFORM SIGN AB2 TIMES BALAG
        chars.append(0x12018)  #glyph00028	CUNEIFORM SIGN AB2 TIMES GAN2 TENU
        chars.append(0x12019)  #glyph00029	CUNEIFORM SIGN AB2 TIMES ME PLUS EN
        chars.append(0x1201A)  #glyph00030	CUNEIFORM SIGN AB2 TIMES SHA3
        chars.append(0x1201B)  #glyph00031	CUNEIFORM SIGN AB2 TIMES TAK4
        chars.append(0x1201C)  #glyph00032	CUNEIFORM SIGN AD
        chars.append(0x1201D)  #glyph00033	CUNEIFORM SIGN AK
        chars.append(0x1201E)  #glyph00034	CUNEIFORM SIGN AK TIMES ERIN2
        chars.append(0x1201F)  #glyph00035	CUNEIFORM SIGN AK TIMES SHITA PLUS GISH
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x12021)  #glyph00037	CUNEIFORM SIGN AL TIMES AL
        chars.append(0x12022)  #glyph00038	CUNEIFORM SIGN AL TIMES DIM2
        chars.append(0x12023)  #glyph00039	CUNEIFORM SIGN AL TIMES GISH
        chars.append(0x12024)  #glyph00040	CUNEIFORM SIGN AL TIMES HA
        chars.append(0x12025)  #glyph00041	CUNEIFORM SIGN AL TIMES KAD3
        chars.append(0x12026)  #glyph00042	CUNEIFORM SIGN AL TIMES KI
        chars.append(0x12027)  #glyph00043	CUNEIFORM SIGN AL TIMES SHE
        chars.append(0x12028)  #glyph00044	CUNEIFORM SIGN AL TIMES USH
        chars.append(0x12029)  #glyph00045	CUNEIFORM SIGN ALAN
        chars.append(0x1202A)  #glyph00046	CUNEIFORM SIGN ALEPH
        chars.append(0x12007)  #glyph00011	CUNEIFORM SIGN A TIMES MUSH
        chars.append(0x1202C)  #glyph00048	CUNEIFORM SIGN AMAR TIMES SHE
        chars.append(0x1202D)  #glyph00049	CUNEIFORM SIGN AN
        chars.append(0x1202E)  #glyph00050	CUNEIFORM SIGN AN OVER AN
        chars.append(0x1202F)  #glyph00051	CUNEIFORM SIGN AN THREE TIMES
        chars.append(0x12030)  #glyph00052	CUNEIFORM SIGN AN PLUS NAGA OPPOSING AN PLUS NAGA
        chars.append(0x12031)  #glyph00053	CUNEIFORM SIGN AN PLUS NAGA SQUARED
        chars.append(0x12032)  #glyph00054	CUNEIFORM SIGN ANSHE
        chars.append(0x12033)  #glyph00055	CUNEIFORM SIGN APIN
        chars.append(0x12034)  #glyph00056	CUNEIFORM SIGN ARAD
        chars.append(0x12035)  #glyph00057	CUNEIFORM SIGN ARAD TIMES KUR
        chars.append(0x12036)  #glyph00058	CUNEIFORM SIGN ARKAB
        chars.append(0x12037)  #glyph00059	CUNEIFORM SIGN ASAL2
        chars.append(0x12038)  #glyph00060	CUNEIFORM SIGN ASH
        chars.append(0x12039)  #glyph00061	CUNEIFORM SIGN ASH ZIDA TENU
        chars.append(0x1203A)  #glyph00062	CUNEIFORM SIGN ASH KABA TENU
        chars.append(0x1203B)  #glyph00063	CUNEIFORM SIGN ASH OVER ASH TUG2 OVER TUG2 TUG2 OVER TUG2 PAP
        chars.append(0x1203C)  #glyph00064	CUNEIFORM SIGN ASH OVER ASH OVER ASH
        chars.append(0x1203D)  #glyph00065	CUNEIFORM SIGN ASH OVER ASH OVER ASH CROSSING ASH OVER ASH OVER ASH
        chars.append(0x1203E)  #glyph00066	CUNEIFORM SIGN ASH2
        chars.append(0x1203F)  #glyph00067	CUNEIFORM SIGN ASHGAB
        chars.append(0x12040)  #glyph00068	CUNEIFORM SIGN BA
        chars.append(0x12041)  #glyph00069	CUNEIFORM SIGN BAD
        chars.append(0x12042)  #glyph00070	CUNEIFORM SIGN BAG3
        chars.append(0x12043)  #glyph00071	CUNEIFORM SIGN BAHAR2
        chars.append(0x12044)  #glyph00072	CUNEIFORM SIGN BAL
        chars.append(0x12045)  #glyph00073	CUNEIFORM SIGN BAL OVER BAL
        chars.append(0x12046)  #glyph00074	CUNEIFORM SIGN BALAG
        chars.append(0x12047)  #glyph00075	CUNEIFORM SIGN BAR
        chars.append(0x12048)  #glyph00076	CUNEIFORM SIGN BARA2
        chars.append(0x12049)  #glyph00077	CUNEIFORM SIGN BI
        chars.append(0x1204A)  #glyph00078	CUNEIFORM SIGN BI TIMES A
        chars.append(0x1204B)  #glyph00079	CUNEIFORM SIGN BI TIMES GAR
        chars.append(0x1204C)  #glyph00080	CUNEIFORM SIGN BI TIMES IGI GUNU
        chars.append(0x1204D)  #glyph00081	CUNEIFORM SIGN BU
        chars.append(0x1204E)  #glyph00082	CUNEIFORM SIGN BU OVER BU AB
        chars.append(0x1200D)  #glyph00017	CUNEIFORM SIGN AB TIMES GAL
        chars.append(0x12050)  #glyph00084	CUNEIFORM SIGN BU CROSSING BU
        chars.append(0x12051)  #glyph00085	CUNEIFORM SIGN BULUG
        chars.append(0x12052)  #glyph00086	CUNEIFORM SIGN BULUG OVER BULUG
        chars.append(0x12053)  #glyph00087	CUNEIFORM SIGN BUR
        chars.append(0x12054)  #glyph00088	CUNEIFORM SIGN BUR2
        chars.append(0x12055)  #glyph00089	CUNEIFORM SIGN DA
        chars.append(0x12056)  #glyph00090	CUNEIFORM SIGN DAG
        chars.append(0x12057)  #glyph00091	CUNEIFORM SIGN DAG KISIM5 TIMES A PLUS MASH
        chars.append(0x12058)  #glyph00092	CUNEIFORM SIGN DAG KISIM5 TIMES AMAR
        chars.append(0x12059)  #glyph00093	CUNEIFORM SIGN DAG KISIM5 TIMES BALAG
        chars.append(0x1205A)  #glyph00094	CUNEIFORM SIGN DAG KISIM5 TIMES BI
        chars.append(0x1205B)  #glyph00095	CUNEIFORM SIGN DAG KISIM5 TIMES GA
        chars.append(0x1205C)  #glyph00096	CUNEIFORM SIGN DAG KISIM5 TIMES GA PLUS MASH
        chars.append(0x1205D)  #glyph00097	CUNEIFORM SIGN DAG KISIM5 TIMES GI
        chars.append(0x1205E)  #glyph00098	CUNEIFORM SIGN DAG KISIM5 TIMES GIR2
        chars.append(0x1205F)  #glyph00099	CUNEIFORM SIGN DAG KISIM5 TIMES GUD
        chars.append(0x12060)  #glyph00100	CUNEIFORM SIGN DAG KISIM5 TIMES HA
        chars.append(0x12061)  #glyph00101	CUNEIFORM SIGN DAG KISIM5 TIMES IR
        chars.append(0x12062)  #glyph00102	CUNEIFORM SIGN DAG KISIM5 TIMES IR PLUS LU
        chars.append(0x12063)  #glyph00103	CUNEIFORM SIGN DAG KISIM5 TIMES KAK
        chars.append(0x12064)  #glyph00104	CUNEIFORM SIGN DAG KISIM5 TIMES LA
        chars.append(0x12065)  #glyph00105	CUNEIFORM SIGN DAG KISIM5 TIMES LU
        chars.append(0x12066)  #glyph00106	CUNEIFORM SIGN DAG KISIM5 TIMES LU PLUS MASH2
        chars.append(0x12067)  #glyph00107	CUNEIFORM SIGN DAG KISIM5 TIMES LUM
        chars.append(0x12068)  #glyph00108	CUNEIFORM SIGN DAG KISIM5 TIMES NE
        chars.append(0x12069)  #glyph00109	CUNEIFORM SIGN DAG KISIM5 TIMES PAP PLUS PAP
        chars.append(0x1206A)  #glyph00110	CUNEIFORM SIGN DAG KISIM5 TIMES SI
        chars.append(0x1206B)  #glyph00111	CUNEIFORM SIGN DAG KISIM5 TIMES TAK4
        chars.append(0x1206C)  #glyph00112	CUNEIFORM SIGN DAG KISIM5 TIMES U2 PLUS GIR2
        chars.append(0x1206D)  #glyph00113	CUNEIFORM SIGN DAG KISIM5 TIMES USH
        chars.append(0x1206E)  #glyph00114	CUNEIFORM SIGN DAM
        chars.append(0x1206F)  #glyph00115	CUNEIFORM SIGN DAR
        chars.append(0x12070)  #glyph00116	CUNEIFORM SIGN DARA3
        chars.append(0x12071)  #glyph00117	CUNEIFORM SIGN DARA4
        chars.append(0x12072)  #glyph00118	CUNEIFORM SIGN DI
        chars.append(0x12073)  #glyph00119	CUNEIFORM SIGN DIB
        chars.append(0x12074)  #glyph00120	CUNEIFORM SIGN DIM
        chars.append(0x12075)  #glyph00121	CUNEIFORM SIGN DIM TIMES SHE
        chars.append(0x12076)  #glyph00122	CUNEIFORM SIGN DIM2
        chars.append(0x12077)  #glyph00123	CUNEIFORM SIGN DIN
        chars.append(0x12078)  #glyph00124	CUNEIFORM SIGN DIN KASKAL U GUNU DISH
        chars.append(0x12079)  #glyph00125	CUNEIFORM SIGN DISH
        chars.append(0x1207A)  #glyph00126	CUNEIFORM SIGN DU
        chars.append(0x1207B)  #glyph00127	CUNEIFORM SIGN DU OVER DU
        chars.append(0x1207C)  #glyph00128	CUNEIFORM SIGN DU GUNU
        chars.append(0x1207D)  #glyph00129	CUNEIFORM SIGN DU SHESHIG
        chars.append(0x1207E)  #glyph00130	CUNEIFORM SIGN DUB
        chars.append(0x1207F)  #glyph00131	CUNEIFORM SIGN DUB TIMES ESH2
        chars.append(0x12080)  #glyph00132	CUNEIFORM SIGN DUB2
        chars.append(0x12081)  #glyph00133	CUNEIFORM SIGN DUG
        chars.append(0x12082)  #glyph00134	CUNEIFORM SIGN DUGUD
        chars.append(0x12083)  #glyph00135	CUNEIFORM SIGN DUH
        chars.append(0x12084)  #glyph00136	CUNEIFORM SIGN DUN
        chars.append(0x12085)  #glyph00137	CUNEIFORM SIGN DUN3
        chars.append(0x12086)  #glyph00138	CUNEIFORM SIGN DUN3 GUNU
        chars.append(0x12087)  #glyph00139	CUNEIFORM SIGN DUN3 GUNU GUNU
        chars.append(0x12088)  #glyph00140	CUNEIFORM SIGN DUN4
        chars.append(0x12089)  #glyph00141	CUNEIFORM SIGN DUR2
        chars.append(0x1208A)  #glyph00142	CUNEIFORM SIGN E
        chars.append(0x1208B)  #glyph00143	CUNEIFORM SIGN E TIMES PAP
        chars.append(0x1208C)  #glyph00144	CUNEIFORM SIGN E OVER E NUN OVER NUN
        chars.append(0x1208D)  #glyph00145	CUNEIFORM SIGN E2
        chars.append(0x1208E)  #glyph00146	CUNEIFORM SIGN E2 TIMES A PLUS HA PLUS DA
        chars.append(0x1208F)  #glyph00147	CUNEIFORM SIGN E2 TIMES GAR
        chars.append(0x12090)  #glyph00148	CUNEIFORM SIGN E2 TIMES MI
        chars.append(0x12091)  #glyph00149	CUNEIFORM SIGN E2 TIMES SAL
        chars.append(0x12092)  #glyph00150	CUNEIFORM SIGN E2 TIMES SHE
        chars.append(0x12093)  #glyph00151	CUNEIFORM SIGN E2 TIMES U
        chars.append(0x12094)  #glyph00152	CUNEIFORM SIGN EDIN
        chars.append(0x12095)  #glyph00153	CUNEIFORM SIGN EGIR
        chars.append(0x12096)  #glyph00154	CUNEIFORM SIGN EL
        chars.append(0x12097)  #glyph00155	CUNEIFORM SIGN EN
        chars.append(0x12098)  #glyph00156	CUNEIFORM SIGN EN TIMES GAN2
        chars.append(0x12099)  #glyph00157	CUNEIFORM SIGN EN TIMES GAN2 TENU
        chars.append(0x1209A)  #glyph00158	CUNEIFORM SIGN EN TIMES ME
        chars.append(0x1209B)  #glyph00159	CUNEIFORM SIGN EN CROSSING EN
        chars.append(0x1209C)  #glyph00160	CUNEIFORM SIGN EN OPPOSING EN
        chars.append(0x1209D)  #glyph00161	CUNEIFORM SIGN EN SQUARED
        chars.append(0x1209E)  #glyph00162	CUNEIFORM SIGN EREN
        chars.append(0x1209F)  #glyph00163	CUNEIFORM SIGN ERIN2
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x120A1)  #glyph00165	CUNEIFORM SIGN EZEN
        chars.append(0x120A2)  #glyph00166	CUNEIFORM SIGN EZEN TIMES A
        chars.append(0x120A3)  #glyph00167	CUNEIFORM SIGN EZEN TIMES A PLUS LAL
        chars.append(0x120A4)  #glyph00168	CUNEIFORM SIGN EZEN TIMES A PLUS LAL TIMES LAL
        chars.append(0x120A5)  #glyph00169	CUNEIFORM SIGN EZEN TIMES AN
        chars.append(0x120A6)  #glyph00170	CUNEIFORM SIGN EZEN TIMES BAD
        chars.append(0x120A7)  #glyph00171	CUNEIFORM SIGN EZEN TIMES DUN3 GUNU
        chars.append(0x120A8)  #glyph00172	CUNEIFORM SIGN EZEN TIMES DUN3 GUNU GUNU
        chars.append(0x120A9)  #glyph00173	CUNEIFORM SIGN EZEN TIMES HA
        chars.append(0x120AA)  #glyph00174	CUNEIFORM SIGN EZEN TIMES HA GUNU
        chars.append(0x120AB)  #glyph00175	CUNEIFORM SIGN EZEN TIMES IGI GUNU
        chars.append(0x120AC)  #glyph00176	CUNEIFORM SIGN EZEN TIMES KASKAL
        chars.append(0x120AD)  #glyph00177	CUNEIFORM SIGN EZEN TIMES KASKAL SQUARED
        chars.append(0x120AE)  #glyph00178	CUNEIFORM SIGN EZEN TIMES KU3
        chars.append(0x120AF)  #glyph00179	CUNEIFORM SIGN EZEN TIMES LA
        chars.append(0x120B0)  #glyph00180	CUNEIFORM SIGN EZEN TIMES LAL TIMES LAL
        chars.append(0x120B1)  #glyph00181	CUNEIFORM SIGN EZEN TIMES LI
        chars.append(0x120B2)  #glyph00182	CUNEIFORM SIGN EZEN TIMES LU
        chars.append(0x120B3)  #glyph00183	CUNEIFORM SIGN EZEN TIMES U2
        chars.append(0x120B4)  #glyph00184	CUNEIFORM SIGN EZEN TIMES UD
        chars.append(0x120B5)  #glyph00185	CUNEIFORM SIGN GA
        chars.append(0x120B6)  #glyph00186	CUNEIFORM SIGN GA GUNU
        chars.append(0x120B7)  #glyph00187	CUNEIFORM SIGN GA2
        chars.append(0x120B8)  #glyph00188	CUNEIFORM SIGN GA2 TIMES A PLUS DA PLUS HA
        chars.append(0x120B9)  #glyph00189	CUNEIFORM SIGN GA2 TIMES A PLUS HA
        chars.append(0x120BA)  #glyph00190	CUNEIFORM SIGN GA2 TIMES A PLUS IGI
        chars.append(0x120BB)  #glyph00191	CUNEIFORM SIGN GA2 TIMES AB2 TENU PLUS TAB
        chars.append(0x120BC)  #glyph00192	CUNEIFORM SIGN GA2 TIMES AN
        chars.append(0x120BD)  #glyph00193	CUNEIFORM SIGN GA2 TIMES ASH
        chars.append(0x120BE)  #glyph00194	CUNEIFORM SIGN GA2 TIMES ASH2 PLUS GAL
        chars.append(0x120BF)  #glyph00195	CUNEIFORM SIGN GA2 TIMES BAD
        chars.append(0x120C0)  #glyph00196	CUNEIFORM SIGN GA2 TIMES BAR PLUS RA
        chars.append(0x12020)  #glyph00036	CUNEIFORM SIGN AL
        chars.append(0x120C2)  #glyph00198	CUNEIFORM SIGN GA2 TIMES BUR PLUS RA
        chars.append(0x120C3)  #glyph00199	CUNEIFORM SIGN GA2 TIMES DA
        chars.append(0x120C4)  #glyph00200	CUNEIFORM SIGN GA2 TIMES DI
        chars.append(0x120C5)  #glyph00201	CUNEIFORM SIGN GA2 TIMES DIM TIMES SHE
        chars.append(0x120C6)  #glyph00202	CUNEIFORM SIGN GA2 TIMES DUB
        chars.append(0x120C7)  #glyph00203	CUNEIFORM SIGN GA2 TIMES EL
        chars.append(0x120C8)  #glyph00204	CUNEIFORM SIGN GA2 TIMES EL PLUS LA
        chars.append(0x120C9)  #glyph00205	CUNEIFORM SIGN GA2 TIMES EN
        chars.append(0x120CA)  #glyph00206	CUNEIFORM SIGN GA2 TIMES EN TIMES GAN2 TENU
        chars.append(0x120CB)  #glyph00207	CUNEIFORM SIGN GA2 TIMES GAN2 TENU
        chars.append(0x120CC)  #glyph00208	CUNEIFORM SIGN GA2 TIMES GAR
        chars.append(0x120CD)  #glyph00209	CUNEIFORM SIGN GA2 TIMES GI
        chars.append(0x120CE)  #glyph00210	CUNEIFORM SIGN GA2 TIMES GI4
        chars.append(0x120CF)  #glyph00211	CUNEIFORM SIGN GA2 TIMES GI4 PLUS A
        chars.append(0x120D0)  #glyph00212	CUNEIFORM SIGN GA2 TIMES GIR2 PLUS SU
        chars.append(0x120D1)  #glyph00213	CUNEIFORM SIGN GA2 TIMES HA PLUS LU PLUS ESH2
        chars.append(0x120D2)  #glyph00214	CUNEIFORM SIGN GA2 TIMES HAL
        chars.append(0x120D3)  #glyph00215	CUNEIFORM SIGN GA2 TIMES HAL PLUS LA
        chars.append(0x120D4)  #glyph00216	CUNEIFORM SIGN GA2 TIMES HI PLUS LI
        chars.append(0x120D5)  #glyph00217	CUNEIFORM SIGN GA2 TIMES HUB2
        chars.append(0x120D6)  #glyph00218	CUNEIFORM SIGN GA2 TIMES IGI GUNU
        chars.append(0x120D7)  #glyph00219	CUNEIFORM SIGN GA2 TIMES ISH PLUS HU PLUS ASH
        chars.append(0x120D8)  #glyph00220	CUNEIFORM SIGN GA2 TIMES KAK
        chars.append(0x120D9)  #glyph00221	CUNEIFORM SIGN GA2 TIMES KASKAL
        chars.append(0x120DA)  #glyph00222	CUNEIFORM SIGN GA2 TIMES KID
        chars.append(0x120DB)  #glyph00223	CUNEIFORM SIGN GA2 TIMES KID PLUS LAL
        chars.append(0x120DC)  #glyph00224	CUNEIFORM SIGN GA2 TIMES KU3 PLUS AN
        chars.append(0x120DD)  #glyph00225	CUNEIFORM SIGN GA2 TIMES LA
        chars.append(0x120DE)  #glyph00226	CUNEIFORM SIGN GA2 TIMES ME PLUS EN
        chars.append(0x120DF)  #glyph00227	CUNEIFORM SIGN GA2 TIMES MI
        chars.append(0x120E0)  #glyph00228	CUNEIFORM SIGN GA2 TIMES NUN
        chars.append(0x120E1)  #glyph00229	CUNEIFORM SIGN GA2 TIMES NUN OVER NUN
        chars.append(0x120E2)  #glyph00230	CUNEIFORM SIGN GA2 TIMES PA
        chars.append(0x120E3)  #glyph00231	CUNEIFORM SIGN GA2 TIMES SAL
        chars.append(0x120E4)  #glyph00232	CUNEIFORM SIGN GA2 TIMES SAR
        chars.append(0x120E5)  #glyph00233	CUNEIFORM SIGN GA2 TIMES SHE
        chars.append(0x120E6)  #glyph00234	CUNEIFORM SIGN GA2 TIMES SHE PLUS TUR
        chars.append(0x120E7)  #glyph00235	CUNEIFORM SIGN GA2 TIMES SHID
        chars.append(0x120E8)  #glyph00236	CUNEIFORM SIGN GA2 TIMES SUM
        chars.append(0x120E9)  #glyph00237	CUNEIFORM SIGN GA2 TIMES TAK4
        chars.append(0x120EA)  #glyph00238	CUNEIFORM SIGN GA2 TIMES U
        chars.append(0x120EB)  #glyph00239	CUNEIFORM SIGN GA2 TIMES UD
        chars.append(0x120EC)  #glyph00240	CUNEIFORM SIGN GA2 TIMES UD PLUS DU
        chars.append(0x120ED)  #glyph00241	CUNEIFORM SIGN GA2 OVER GA2
        chars.append(0x120EE)  #glyph00242	CUNEIFORM SIGN GABA
        chars.append(0x120EF)  #glyph00243	CUNEIFORM SIGN GABA CROSSING GABA
        chars.append(0x120F0)  #glyph00244	CUNEIFORM SIGN GAD
        chars.append(0x120F1)  #glyph00245	CUNEIFORM SIGN GAD OVER GAD GAR OVER GAR
        chars.append(0x120F2)  #glyph00246	CUNEIFORM SIGN GAL
        chars.append(0x120F3)  #glyph00247	CUNEIFORM SIGN GAL GAD OVER GAD GAR OVER GAR
        chars.append(0x120F4)  #glyph00248	CUNEIFORM SIGN GALAM
        chars.append(0x120F5)  #glyph00249	CUNEIFORM SIGN GAM
        chars.append(0x120F6)  #glyph00250	CUNEIFORM SIGN GAN
        chars.append(0x120F7)  #glyph00251	CUNEIFORM SIGN GAN2
        chars.append(0x120F8)  #glyph00252	CUNEIFORM SIGN GAN2 TENU
        chars.append(0x120F9)  #glyph00253	CUNEIFORM SIGN GAN2 OVER GAN2
        chars.append(0x120FA)  #glyph00254	CUNEIFORM SIGN GAN2 CROSSING GAN2
        chars.append(0x120FB)  #glyph00255	CUNEIFORM SIGN GAR
        chars.append(0x120FC)  #glyph00256	CUNEIFORM SIGN GAR3
        chars.append(0x120FD)  #glyph00257	CUNEIFORM SIGN GASHAN
        chars.append(0x120FE)  #glyph00258	CUNEIFORM SIGN GESHTIN
        chars.append(0x120FF)  #glyph00259	CUNEIFORM SIGN GESHTIN TIMES KUR
        chars.append(0x12100)  #glyph00260	CUNEIFORM SIGN GI
        chars.append(0x12101)  #glyph00261	CUNEIFORM SIGN GI TIMES E
        chars.append(0x12102)  #glyph00262	CUNEIFORM SIGN GI TIMES U
        chars.append(0x1202B)  #glyph00047	CUNEIFORM SIGN AMAR
        chars.append(0x12104)  #glyph00264	CUNEIFORM SIGN GI4
        chars.append(0x12105)  #glyph00265	CUNEIFORM SIGN GI4 OVER GI4
        chars.append(0x12106)  #glyph00266	CUNEIFORM SIGN GI4 CROSSING GI4
        chars.append(0x12107)  #glyph00267	CUNEIFORM SIGN GIDIM
        chars.append(0x12108)  #glyph00268	CUNEIFORM SIGN GIR2
        chars.append(0x12109)  #glyph00269	CUNEIFORM SIGN GIR2 GUNU
        chars.append(0x1210A)  #glyph00270	CUNEIFORM SIGN GIR3
        chars.append(0x1210B)  #glyph00271	CUNEIFORM SIGN GIR3 TIMES A PLUS IGI
        chars.append(0x1210C)  #glyph00272	CUNEIFORM SIGN GIR3 TIMES GAN2 TENU
        chars.append(0x1210D)  #glyph00273	CUNEIFORM SIGN GIR3 TIMES IGI
        chars.append(0x1210E)  #glyph00274	CUNEIFORM SIGN GIR3 TIMES LU PLUS IGI
        chars.append(0x1210F)  #glyph00275	CUNEIFORM SIGN GIR3 TIMES PA
        chars.append(0x12110)  #glyph00276	CUNEIFORM SIGN GISAL
        chars.append(0x12111)  #glyph00277	CUNEIFORM SIGN GISH
        chars.append(0x12112)  #glyph00278	CUNEIFORM SIGN GISH CROSSING GISH
        chars.append(0x12113)  #glyph00279	CUNEIFORM SIGN GISH TIMES BAD
        chars.append(0x12114)  #glyph00280	CUNEIFORM SIGN GISH TIMES TAK4
        chars.append(0x12115)  #glyph00281	CUNEIFORM SIGN GISH TENU
        chars.append(0x12116)  #glyph00282	CUNEIFORM SIGN GU
        chars.append(0x12117)  #glyph00283	CUNEIFORM SIGN GU CROSSING GU
        chars.append(0x12118)  #glyph00284	CUNEIFORM SIGN GU2
        chars.append(0x12119)  #glyph00285	CUNEIFORM SIGN GU2 TIMES KAK
        chars.append(0x1211A)  #glyph00286	CUNEIFORM SIGN GU2 TIMES KAK TIMES IGI GUNU
        chars.append(0x1211B)  #glyph00287	CUNEIFORM SIGN GU2 TIMES NUN
        chars.append(0x1211C)  #glyph00288	CUNEIFORM SIGN GU2 TIMES SAL PLUS TUG2
        chars.append(0x1211D)  #glyph00289	CUNEIFORM SIGN GU2 GUNU
        chars.append(0x1211E)  #glyph00290	CUNEIFORM SIGN GUD
        chars.append(0x1211F)  #glyph00291	CUNEIFORM SIGN GUD TIMES A PLUS KUR
        chars.append(0x12120)  #glyph00292	CUNEIFORM SIGN GUD TIMES KUR
        chars.append(0x12121)  #glyph00293	CUNEIFORM SIGN GUD OVER GUD LUGAL
        chars.append(0x12122)  #glyph00294	CUNEIFORM SIGN GUL
        chars.append(0x12123)  #glyph00295	CUNEIFORM SIGN GUM
        chars.append(0x12124)  #glyph00296	CUNEIFORM SIGN GUM TIMES SHE
        chars.append(0x12125)  #glyph00297	CUNEIFORM SIGN GUR
        chars.append(0x12126)  #glyph00298	CUNEIFORM SIGN GUR7
        chars.append(0x12127)  #glyph00299	CUNEIFORM SIGN GURUN
        chars.append(0x12128)  #glyph00300	CUNEIFORM SIGN GURUSH
        chars.append(0x12129)  #glyph00301	CUNEIFORM SIGN HA
        chars.append(0x1212A)  #glyph00302	CUNEIFORM SIGN HA TENU
        chars.append(0x1212B)  #glyph00303	CUNEIFORM SIGN HA GUNU
        chars.append(0x1212C)  #glyph00304	CUNEIFORM SIGN HAL
        chars.append(0x1212D)  #glyph00305	CUNEIFORM SIGN HI
        chars.append(0x1212E)  #glyph00306	CUNEIFORM SIGN HI TIMES ASH
        chars.append(0x1212F)  #glyph00307	CUNEIFORM SIGN HI TIMES ASH2
        chars.append(0x12130)  #glyph00308	CUNEIFORM SIGN HI TIMES BAD
        chars.append(0x12131)  #glyph00309	CUNEIFORM SIGN HI TIMES DISH
        chars.append(0x12132)  #glyph00310	CUNEIFORM SIGN HI TIMES GAD
        chars.append(0x12133)  #glyph00311	CUNEIFORM SIGN HI TIMES KIN
        chars.append(0x12134)  #glyph00312	CUNEIFORM SIGN HI TIMES NUN
        chars.append(0x12135)  #glyph00313	CUNEIFORM SIGN HI TIMES SHE
        chars.append(0x12136)  #glyph00314	CUNEIFORM SIGN HI TIMES U
        chars.append(0x12137)  #glyph00315	CUNEIFORM SIGN HU
        chars.append(0x12138)  #glyph00316	CUNEIFORM SIGN HUB2
        chars.append(0x12139)  #glyph00317	CUNEIFORM SIGN HUB2 TIMES AN
        chars.append(0x1213A)  #glyph00318	CUNEIFORM SIGN HUB2 TIMES HAL
        chars.append(0x1213B)  #glyph00319	CUNEIFORM SIGN HUB2 TIMES KASKAL
        chars.append(0x1213C)  #glyph00320	CUNEIFORM SIGN HUB2 TIMES LISH
        chars.append(0x1213D)  #glyph00321	CUNEIFORM SIGN HUB2 TIMES UD
        chars.append(0x1213E)  #glyph00322	CUNEIFORM SIGN HUL2
        chars.append(0x1213F)  #glyph00323	CUNEIFORM SIGN I
        chars.append(0x12140)  #glyph00324	CUNEIFORM SIGN I A
        chars.append(0x12141)  #glyph00325	CUNEIFORM SIGN IB
        chars.append(0x12142)  #glyph00326	CUNEIFORM SIGN IDIM
        chars.append(0x12143)  #glyph00327	CUNEIFORM SIGN IDIM OVER IDIM BUR
        chars.append(0x12144)  #glyph00328	CUNEIFORM SIGN IDIM OVER IDIM SQUARED
        chars.append(0x12145)  #glyph00329	CUNEIFORM SIGN IG
        chars.append(0x12146)  #glyph00330	CUNEIFORM SIGN IGI
        chars.append(0x12147)  #glyph00331	CUNEIFORM SIGN IGI DIB
        chars.append(0x12148)  #glyph00332	CUNEIFORM SIGN IGI RI
        chars.append(0x12149)  #glyph00333	CUNEIFORM SIGN IGI OVER IGI SHIR OVER SHIR UD OVER UD
        chars.append(0x1214A)  #glyph00334	CUNEIFORM SIGN IGI GUNU
        chars.append(0x1214B)  #glyph00335	CUNEIFORM SIGN IL
        chars.append(0x1214C)  #glyph00336	CUNEIFORM SIGN IL TIMES GAN2 TENU
        chars.append(0x1214D)  #glyph00337	CUNEIFORM SIGN IL2
        chars.append(0x1214E)  #glyph00338	CUNEIFORM SIGN IM
        chars.append(0x1214F)  #glyph00339	CUNEIFORM SIGN IM TIMES TAK4
        chars.append(0x12150)  #glyph00340	CUNEIFORM SIGN IM CROSSING IM
        chars.append(0x12151)  #glyph00341	CUNEIFORM SIGN IM OPPOSING IM
        chars.append(0x12152)  #glyph00342	CUNEIFORM SIGN IM SQUARED
        chars.append(0x12153)  #glyph00343	CUNEIFORM SIGN IMIN
        chars.append(0x12154)  #glyph00344	CUNEIFORM SIGN IN
        chars.append(0x12155)  #glyph00345	CUNEIFORM SIGN IR
        chars.append(0x12156)  #glyph00346	CUNEIFORM SIGN ISH
        chars.append(0x12157)  #glyph00347	CUNEIFORM SIGN KA
        chars.append(0x12158)  #glyph00348	CUNEIFORM SIGN KA TIMES A
        chars.append(0x12159)  #glyph00349	CUNEIFORM SIGN KA TIMES AD
        chars.append(0x1215A)  #glyph00350	CUNEIFORM SIGN KA TIMES AD PLUS KU3
        chars.append(0x1215B)  #glyph00351	CUNEIFORM SIGN KA TIMES ASH2
        chars.append(0x1215C)  #glyph00352	CUNEIFORM SIGN KA TIMES BAD
        chars.append(0x1215D)  #glyph00353	CUNEIFORM SIGN KA TIMES BALAG
        chars.append(0x1215E)  #glyph00354	CUNEIFORM SIGN KA TIMES BAR
        chars.append(0x1215F)  #glyph00355	CUNEIFORM SIGN KA TIMES BI
        chars.append(0x12160)  #glyph00356	CUNEIFORM SIGN KA TIMES ERIN2
        chars.append(0x12161)  #glyph00357	CUNEIFORM SIGN KA TIMES ESH2
        chars.append(0x12162)  #glyph00358	CUNEIFORM SIGN KA TIMES GA
        chars.append(0x12163)  #glyph00359	CUNEIFORM SIGN KA TIMES GAL
        chars.append(0x12164)  #glyph00360	CUNEIFORM SIGN KA TIMES GAN2 TENU
        chars.append(0x12165)  #glyph00361	CUNEIFORM SIGN KA TIMES GAR
        chars.append(0x12166)  #glyph00362	CUNEIFORM SIGN KA TIMES GAR PLUS SHA3 PLUS A
        chars.append(0x12167)  #glyph00363	CUNEIFORM SIGN KA TIMES GI
        chars.append(0x12168)  #glyph00364	CUNEIFORM SIGN KA TIMES GIR2
        chars.append(0x12169)  #glyph00365	CUNEIFORM SIGN KA TIMES GISH PLUS SAR
        chars.append(0x1216A)  #glyph00366	CUNEIFORM SIGN KA TIMES GISH CROSSING GISH
        chars.append(0x1216B)  #glyph00367	CUNEIFORM SIGN KA TIMES GU
        chars.append(0x1216C)  #glyph00368	CUNEIFORM SIGN KA TIMES GUR7
        chars.append(0x1216D)  #glyph00369	CUNEIFORM SIGN KA TIMES IGI
        chars.append(0x1216E)  #glyph00370	CUNEIFORM SIGN KA TIMES IM
        chars.append(0x1216F)  #glyph00371	CUNEIFORM SIGN KA TIMES KAK
        chars.append(0x12170)  #glyph00372	CUNEIFORM SIGN KA TIMES KI
        chars.append(0x12171)  #glyph00373	CUNEIFORM SIGN KA TIMES KID
        chars.append(0x12172)  #glyph00374	CUNEIFORM SIGN KA TIMES LI
        chars.append(0x12173)  #glyph00375	CUNEIFORM SIGN KA TIMES LU
        chars.append(0x12174)  #glyph00376	CUNEIFORM SIGN KA TIMES ME
        chars.append(0x12175)  #glyph00377	CUNEIFORM SIGN KA TIMES ME PLUS DU
        chars.append(0x12176)  #glyph00378	CUNEIFORM SIGN KA TIMES ME PLUS GI
        chars.append(0x12177)  #glyph00379	CUNEIFORM SIGN KA TIMES ME PLUS TE
        chars.append(0x12178)  #glyph00380	CUNEIFORM SIGN KA TIMES MI
        chars.append(0x12179)  #glyph00381	CUNEIFORM SIGN KA TIMES MI PLUS NUNUZ
        chars.append(0x1217A)  #glyph00382	CUNEIFORM SIGN KA TIMES NE
        chars.append(0x1217B)  #glyph00383	CUNEIFORM SIGN KA TIMES NUN
        chars.append(0x1217C)  #glyph00384	CUNEIFORM SIGN KA TIMES PI
        chars.append(0x1217D)  #glyph00385	CUNEIFORM SIGN KA TIMES RU
        chars.append(0x1217E)  #glyph00386	CUNEIFORM SIGN KA TIMES SA
        chars.append(0x1217F)  #glyph00387	CUNEIFORM SIGN KA TIMES SAR
        chars.append(0x12180)  #glyph00388	CUNEIFORM SIGN KA TIMES SHA
        chars.append(0x12181)  #glyph00389	CUNEIFORM SIGN KA TIMES SHE
        chars.append(0x12182)  #glyph00390	CUNEIFORM SIGN KA TIMES SHID
        chars.append(0x12183)  #glyph00391	CUNEIFORM SIGN KA TIMES SHU
        chars.append(0x12184)  #glyph00392	CUNEIFORM SIGN KA TIMES SIG
        chars.append(0x12185)  #glyph00393	CUNEIFORM SIGN KA TIMES SUHUR
        chars.append(0x12186)  #glyph00394	CUNEIFORM SIGN KA TIMES TAR
        chars.append(0x12187)  #glyph00395	CUNEIFORM SIGN KA TIMES U
        chars.append(0x12188)  #glyph00396	CUNEIFORM SIGN KA TIMES U2
        chars.append(0x12189)  #glyph00397	CUNEIFORM SIGN KA TIMES UD
        chars.append(0x1218A)  #glyph00398	CUNEIFORM SIGN KA TIMES UMUM TIMES PA
        chars.append(0x1218B)  #glyph00399	CUNEIFORM SIGN KA TIMES USH
        chars.append(0x1218C)  #glyph00400	CUNEIFORM SIGN KA TIMES ZI
        chars.append(0x1218D)  #glyph00401	CUNEIFORM SIGN KA2
        chars.append(0x1218E)  #glyph00402	CUNEIFORM SIGN KA2 CROSSING KA2
        chars.append(0x1218F)  #glyph00403	CUNEIFORM SIGN KAB
        chars.append(0x12190)  #glyph00404	CUNEIFORM SIGN KAD2
        chars.append(0x12191)  #glyph00405	CUNEIFORM SIGN KAD3
        chars.append(0x12192)  #glyph00406	CUNEIFORM SIGN KAD4
        chars.append(0x12193)  #glyph00407	CUNEIFORM SIGN KAD5
        chars.append(0x12194)  #glyph00408	CUNEIFORM SIGN KAD5 OVER KAD5
        chars.append(0x12195)  #glyph00409	CUNEIFORM SIGN KAK
        chars.append(0x12196)  #glyph00410	CUNEIFORM SIGN KAK TIMES IGI GUNU
        chars.append(0x12197)  #glyph00411	CUNEIFORM SIGN KAL
        chars.append(0x12198)  #glyph00412	CUNEIFORM SIGN KAL TIMES BAD
        chars.append(0x12199)  #glyph00413	CUNEIFORM SIGN KAL CROSSING KAL
        chars.append(0x1219A)  #glyph00414	CUNEIFORM SIGN KAM2
        chars.append(0x1219B)  #glyph00415	CUNEIFORM SIGN KAM4
        chars.append(0x1219C)  #glyph00416	CUNEIFORM SIGN KASKAL
        chars.append(0x1219D)  #glyph00417	CUNEIFORM SIGN KASKAL LAGAB TIMES U OVER LAGAB TIMES U
        chars.append(0x1219E)  #glyph00418	CUNEIFORM SIGN KASKAL OVER KASKAL LAGAB TIMES U OVER LAGAB TIMES U
        chars.append(0x1219F)  #glyph00419	CUNEIFORM SIGN KESH2
        chars.append(0x121A0)  #glyph00420	CUNEIFORM SIGN KI
        chars.append(0x121A1)  #glyph00421	CUNEIFORM SIGN KI TIMES BAD
        chars.append(0x121A2)  #glyph00422	CUNEIFORM SIGN KI TIMES U
        chars.append(0x121A3)  #glyph00423	CUNEIFORM SIGN KI TIMES UD
        chars.append(0x121A4)  #glyph00424	CUNEIFORM SIGN KID
        chars.append(0x121A5)  #glyph00425	CUNEIFORM SIGN KIN
        chars.append(0x121A6)  #glyph00426	CUNEIFORM SIGN KISAL
        chars.append(0x121A7)  #glyph00427	CUNEIFORM SIGN KISH
        chars.append(0x121A8)  #glyph00428	CUNEIFORM SIGN KISIM5
        chars.append(0x121A9)  #glyph00429	CUNEIFORM SIGN KISIM5 OVER KISIM5
        chars.append(0x121AA)  #glyph00430	CUNEIFORM SIGN KU
        chars.append(0x121AB)  #glyph00431	CUNEIFORM SIGN KU OVER HI TIMES ASH2 KU OVER HI TIMES ASH2
        chars.append(0x121AC)  #glyph00432	CUNEIFORM SIGN KU3
        chars.append(0x121AD)  #glyph00433	CUNEIFORM SIGN KU4
        chars.append(0x121AE)  #glyph00434	CUNEIFORM SIGN KU4 VARIANT FORM
        chars.append(0x121AF)  #glyph00435	CUNEIFORM SIGN KU7
        chars.append(0x121B0)  #glyph00436	CUNEIFORM SIGN KUL
        chars.append(0x121B1)  #glyph00437	CUNEIFORM SIGN KUL GUNU
        chars.append(0x121B2)  #glyph00438	CUNEIFORM SIGN KUN
        chars.append(0x121B3)  #glyph00439	CUNEIFORM SIGN KUR
        chars.append(0x121B4)  #glyph00440	CUNEIFORM SIGN KUR OPPOSING KUR
        chars.append(0x121B5)  #glyph00441	CUNEIFORM SIGN KUSHU2
        chars.append(0x121B6)  #glyph00442	CUNEIFORM SIGN KWU318
        chars.append(0x121B7)  #glyph00443	CUNEIFORM SIGN LA
        chars.append(0x121B8)  #glyph00444	CUNEIFORM SIGN LAGAB
        chars.append(0x121B9)  #glyph00445	CUNEIFORM SIGN LAGAB TIMES A
        chars.append(0x121BA)  #glyph00446	CUNEIFORM SIGN LAGAB TIMES A PLUS DA PLUS HA
        chars.append(0x121BB)  #glyph00447	CUNEIFORM SIGN LAGAB TIMES A PLUS GAR
        chars.append(0x121BC)  #glyph00448	CUNEIFORM SIGN LAGAB TIMES A PLUS LAL
        chars.append(0x121BD)  #glyph00449	CUNEIFORM SIGN LAGAB TIMES AL
        chars.append(0x121BE)  #glyph00450	CUNEIFORM SIGN LAGAB TIMES AN
        chars.append(0x121BF)  #glyph00451	CUNEIFORM SIGN LAGAB TIMES ASH ZIDA TENU
        chars.append(0x121C0)  #glyph00452	CUNEIFORM SIGN LAGAB TIMES BAD
        chars.append(0x121C1)  #glyph00453	CUNEIFORM SIGN LAGAB TIMES BI
        chars.append(0x121C2)  #glyph00454	CUNEIFORM SIGN LAGAB TIMES DAR
        chars.append(0x121C3)  #glyph00455	CUNEIFORM SIGN LAGAB TIMES EN
        chars.append(0x121C4)  #glyph00456	CUNEIFORM SIGN LAGAB TIMES GA
        chars.append(0x121C5)  #glyph00457	CUNEIFORM SIGN LAGAB TIMES GAR
        chars.append(0x121C6)  #glyph00458	CUNEIFORM SIGN LAGAB TIMES GUD
        chars.append(0x121C7)  #glyph00459	CUNEIFORM SIGN LAGAB TIMES GUD PLUS GUD
        chars.append(0x121C8)  #glyph00460	CUNEIFORM SIGN LAGAB TIMES HA
        chars.append(0x121C9)  #glyph00461	CUNEIFORM SIGN LAGAB TIMES HAL
        chars.append(0x121CA)  #glyph00462	CUNEIFORM SIGN LAGAB TIMES HI TIMES NUN
        chars.append(0x121CB)  #glyph00463	CUNEIFORM SIGN LAGAB TIMES IGI GUNU
        chars.append(0x121CC)  #glyph00464	CUNEIFORM SIGN LAGAB TIMES IM
        chars.append(0x121CD)  #glyph00465	CUNEIFORM SIGN LAGAB TIMES IM PLUS HA
        chars.append(0x121CE)  #glyph00466	CUNEIFORM SIGN LAGAB TIMES IM PLUS LU
        chars.append(0x121CF)  #glyph00467	CUNEIFORM SIGN LAGAB TIMES KI
        chars.append(0x121D0)  #glyph00468	CUNEIFORM SIGN LAGAB TIMES KIN
        chars.append(0x121D1)  #glyph00469	CUNEIFORM SIGN LAGAB TIMES KU3
        chars.append(0x121D2)  #glyph00470	CUNEIFORM SIGN LAGAB TIMES KUL
        chars.append(0x121D3)  #glyph00471	CUNEIFORM SIGN LAGAB TIMES KUL PLUS HI PLUS A
        chars.append(0x121D4)  #glyph00472	CUNEIFORM SIGN LAGAB TIMES LAGAB
        chars.append(0x121D5)  #glyph00473	CUNEIFORM SIGN LAGAB TIMES LISH
        chars.append(0x121D6)  #glyph00474	CUNEIFORM SIGN LAGAB TIMES LU
        chars.append(0x121D7)  #glyph00475	CUNEIFORM SIGN LAGAB TIMES LUL
        chars.append(0x121D8)  #glyph00476	CUNEIFORM SIGN LAGAB TIMES ME
        chars.append(0x121D9)  #glyph00477	CUNEIFORM SIGN LAGAB TIMES ME PLUS EN
        chars.append(0x121DA)  #glyph00478	CUNEIFORM SIGN LAGAB TIMES MUSH
        chars.append(0x1204F)  #glyph00083	CUNEIFORM SIGN BU OVER BU UN
        chars.append(0x121DC)  #glyph00480	CUNEIFORM SIGN LAGAB TIMES SHE PLUS SUM
        chars.append(0x121DD)  #glyph00481	CUNEIFORM SIGN LAGAB TIMES SHITA PLUS GISH PLUS ERIN2
        chars.append(0x121DE)  #glyph00482	CUNEIFORM SIGN LAGAB TIMES SHITA PLUS GISH TENU
        chars.append(0x121DF)  #glyph00483	CUNEIFORM SIGN LAGAB TIMES SHU2
        chars.append(0x121E0)  #glyph00484	CUNEIFORM SIGN LAGAB TIMES SHU2 PLUS SHU2
        chars.append(0x121E1)  #glyph00485	CUNEIFORM SIGN LAGAB TIMES SUM
        chars.append(0x121E2)  #glyph00486	CUNEIFORM SIGN LAGAB TIMES TAG
        chars.append(0x121E3)  #glyph00487	CUNEIFORM SIGN LAGAB TIMES TAK4
        chars.append(0x121E4)  #glyph00488	CUNEIFORM SIGN LAGAB TIMES TE PLUS A PLUS SU PLUS NA
        chars.append(0x121E5)  #glyph00489	CUNEIFORM SIGN LAGAB TIMES U
        chars.append(0x121E6)  #glyph00490	CUNEIFORM SIGN LAGAB TIMES U PLUS A
        chars.append(0x121E7)  #glyph00491	CUNEIFORM SIGN LAGAB TIMES U PLUS U PLUS U
        chars.append(0x121E8)  #glyph00492	CUNEIFORM SIGN LAGAB TIMES U2 PLUS ASH
        chars.append(0x121E9)  #glyph00493	CUNEIFORM SIGN LAGAB TIMES UD
        chars.append(0x121EA)  #glyph00494	CUNEIFORM SIGN LAGAB TIMES USH
        chars.append(0x121EB)  #glyph00495	CUNEIFORM SIGN LAGAB SQUARED
        chars.append(0x121EC)  #glyph00496	CUNEIFORM SIGN LAGAR
        chars.append(0x121ED)  #glyph00497	CUNEIFORM SIGN LAGAR TIMES SHE
        chars.append(0x121EE)  #glyph00498	CUNEIFORM SIGN LAGAR TIMES SHE PLUS SUM
        chars.append(0x121EF)  #glyph00499	CUNEIFORM SIGN LAGAR GUNU
        chars.append(0x121F0)  #glyph00500	CUNEIFORM SIGN LAGAR GUNU OVER LAGAR GUNU SHE
        chars.append(0x121F1)  #glyph00501	CUNEIFORM SIGN LAHSHU
        chars.append(0x121F2)  #glyph00502	CUNEIFORM SIGN LAL
        chars.append(0x121F3)  #glyph00503	CUNEIFORM SIGN LAL TIMES LAL
        chars.append(0x121F4)  #glyph00504	CUNEIFORM SIGN LAM
        chars.append(0x121F5)  #glyph00505	CUNEIFORM SIGN LAM TIMES KUR
        chars.append(0x121F6)  #glyph00506	CUNEIFORM SIGN LAM TIMES KUR PLUS RU
        chars.append(0x121F7)  #glyph00507	CUNEIFORM SIGN LI
        chars.append(0x121F8)  #glyph00508	CUNEIFORM SIGN LIL
        chars.append(0x121F9)  #glyph00509	CUNEIFORM SIGN LIMMU2
        chars.append(0x121FA)  #glyph00510	CUNEIFORM SIGN LISH
        chars.append(0x121FB)  #glyph00511	CUNEIFORM SIGN LU
        chars.append(0x121FC)  #glyph00512	CUNEIFORM SIGN LU TIMES BAD
        chars.append(0x121FD)  #glyph00513	CUNEIFORM SIGN LU2
        chars.append(0x121FE)  #glyph00514	CUNEIFORM SIGN LU2 TIMES AL
        chars.append(0x121FF)  #glyph00515	CUNEIFORM SIGN LU2 TIMES BAD
        chars.append(0x12200)  #glyph00516	CUNEIFORM SIGN LU2 TIMES ESH2
        chars.append(0x12201)  #glyph00517	CUNEIFORM SIGN LU2 TIMES ESH2 TENU
        chars.append(0x12202)  #glyph00518	CUNEIFORM SIGN LU2 TIMES GAN2 TENU
        chars.append(0x12203)  #glyph00519	CUNEIFORM SIGN LU2 TIMES HI TIMES BAD
        chars.append(0x12204)  #glyph00520	CUNEIFORM SIGN LU2 TIMES IM
        chars.append(0x12205)  #glyph00521	CUNEIFORM SIGN LU2 TIMES KAD2
        chars.append(0x12206)  #glyph00522	CUNEIFORM SIGN LU2 TIMES KAD3
        chars.append(0x12207)  #glyph00523	CUNEIFORM SIGN LU2 TIMES KAD3 PLUS ASH
        chars.append(0x12208)  #glyph00524	CUNEIFORM SIGN LU2 TIMES KI
        chars.append(0x12209)  #glyph00525	CUNEIFORM SIGN LU2 TIMES LA PLUS ASH
        chars.append(0x1220A)  #glyph00526	CUNEIFORM SIGN LU2 TIMES LAGAB
        chars.append(0x1220B)  #glyph00527	CUNEIFORM SIGN LU2 TIMES ME PLUS EN
        chars.append(0x1220C)  #glyph00528	CUNEIFORM SIGN LU2 TIMES NE
        chars.append(0x1220D)  #glyph00529	CUNEIFORM SIGN LU2 TIMES NU
        chars.append(0x1220E)  #glyph00530	CUNEIFORM SIGN LU2 TIMES SI PLUS ASH
        chars.append(0x1220F)  #glyph00531	CUNEIFORM SIGN LU2 TIMES SIK2 PLUS BU
        chars.append(0x12210)  #glyph00532	CUNEIFORM SIGN LU2 TIMES TUG2
        chars.append(0x12211)  #glyph00533	CUNEIFORM SIGN LU2 TENU
        chars.append(0x12212)  #glyph00534	CUNEIFORM SIGN LU2 CROSSING LU2
        chars.append(0x12213)  #glyph00535	CUNEIFORM SIGN LU2 OPPOSING LU2
        chars.append(0x12214)  #glyph00536	CUNEIFORM SIGN LU2 SQUARED
        chars.append(0x12215)  #glyph00537	CUNEIFORM SIGN LU2 SHESHIG
        chars.append(0x12216)  #glyph00538	CUNEIFORM SIGN LU3
        chars.append(0x12217)  #glyph00539	CUNEIFORM SIGN LUGAL
        chars.append(0x12218)  #glyph00540	CUNEIFORM SIGN LUGAL OVER LUGAL
        chars.append(0x12219)  #glyph00541	CUNEIFORM SIGN LUGAL OPPOSING LUGAL
        chars.append(0x1221A)  #glyph00542	CUNEIFORM SIGN LUGAL SHESHIG
        chars.append(0x1221B)  #glyph00543	CUNEIFORM SIGN LUH
        chars.append(0x1221C)  #glyph00544	CUNEIFORM SIGN LUL
        chars.append(0x1221D)  #glyph00545	CUNEIFORM SIGN LUM
        chars.append(0x1221E)  #glyph00546	CUNEIFORM SIGN LUM OVER LUM
        chars.append(0x1221F)  #glyph00547	CUNEIFORM SIGN LUM OVER LUM GAR OVER GAR
        chars.append(0x12220)  #glyph00548	CUNEIFORM SIGN MA
        chars.append(0x12221)  #glyph00549	CUNEIFORM SIGN MA TIMES TAK4
        chars.append(0x12222)  #glyph00550	CUNEIFORM SIGN MA GUNU
        chars.append(0x12223)  #glyph00551	CUNEIFORM SIGN MA2
        chars.append(0x12224)  #glyph00552	CUNEIFORM SIGN MAH
        chars.append(0x12225)  #glyph00553	CUNEIFORM SIGN MAR
        chars.append(0x12226)  #glyph00554	CUNEIFORM SIGN MASH
        chars.append(0x12227)  #glyph00555	CUNEIFORM SIGN MASH2
        chars.append(0x12228)  #glyph00556	CUNEIFORM SIGN ME
        chars.append(0x12229)  #glyph00557	CUNEIFORM SIGN MES
        chars.append(0x1222A)  #glyph00558	CUNEIFORM SIGN MI
        chars.append(0x1222B)  #glyph00559	CUNEIFORM SIGN MIN
        chars.append(0x1222C)  #glyph00560	CUNEIFORM SIGN MU
        chars.append(0x1222D)  #glyph00561	CUNEIFORM SIGN MU OVER MU
        chars.append(0x1222E)  #glyph00562	CUNEIFORM SIGN MUG
        chars.append(0x1222F)  #glyph00563	CUNEIFORM SIGN MUG GUNU
        chars.append(0x12230)  #glyph00564	CUNEIFORM SIGN MUNSUB
        chars.append(0x12231)  #glyph00565	CUNEIFORM SIGN MURGU2
        chars.append(0x12232)  #glyph00566	CUNEIFORM SIGN MUSH
        chars.append(0x12233)  #glyph00567	CUNEIFORM SIGN MUSH TIMES A
        chars.append(0x12234)  #glyph00568	CUNEIFORM SIGN MUSH TIMES KUR
        chars.append(0x12235)  #glyph00569	CUNEIFORM SIGN MUSH TIMES ZA
        chars.append(0x12236)  #glyph00570	CUNEIFORM SIGN MUSH OVER MUSH
        chars.append(0x12237)  #glyph00571	CUNEIFORM SIGN MUSH OVER MUSH TIMES A PLUS NA
        chars.append(0x12238)  #glyph00572	CUNEIFORM SIGN MUSH CROSSING MUSH
        chars.append(0x12239)  #glyph00573	CUNEIFORM SIGN MUSH3
        chars.append(0x1223A)  #glyph00574	CUNEIFORM SIGN MUSH3 TIMES A
        chars.append(0x1223B)  #glyph00575	CUNEIFORM SIGN MUSH3 TIMES A PLUS DI
        chars.append(0x1223C)  #glyph00576	CUNEIFORM SIGN MUSH3 TIMES DI
        chars.append(0x1223D)  #glyph00577	CUNEIFORM SIGN MUSH3 GUNU
        chars.append(0x1223E)  #glyph00578	CUNEIFORM SIGN NA
        chars.append(0x1223F)  #glyph00579	CUNEIFORM SIGN NA2
        chars.append(0x12240)  #glyph00580	CUNEIFORM SIGN NAGA
        chars.append(0x12241)  #glyph00581	CUNEIFORM SIGN NAGA INVERTED
        chars.append(0x12242)  #glyph00582	CUNEIFORM SIGN NAGA TIMES SHU TENU
        chars.append(0x12243)  #glyph00583	CUNEIFORM SIGN NAGA OPPOSING NAGA
        chars.append(0x12244)  #glyph00584	CUNEIFORM SIGN NAGAR
        chars.append(0x12245)  #glyph00585	CUNEIFORM SIGN NAM NUTILLU
        chars.append(0x12246)  #glyph00586	CUNEIFORM SIGN NAM
        chars.append(0x12247)  #glyph00587	CUNEIFORM SIGN NAM2
        chars.append(0x12248)  #glyph00588	CUNEIFORM SIGN NE
        chars.append(0x12249)  #glyph00589	CUNEIFORM SIGN NE TIMES A
        chars.append(0x1224A)  #glyph00590	CUNEIFORM SIGN NE TIMES UD
        chars.append(0x1224B)  #glyph00591	CUNEIFORM SIGN NE SHESHIG
        chars.append(0x1224C)  #glyph00592	CUNEIFORM SIGN NI
        chars.append(0x1224D)  #glyph00593	CUNEIFORM SIGN NI TIMES E
        chars.append(0x1224E)  #glyph00594	CUNEIFORM SIGN NI2
        chars.append(0x1224F)  #glyph00595	CUNEIFORM SIGN NIM
        chars.append(0x12250)  #glyph00596	CUNEIFORM SIGN NIM TIMES GAN2 TENU
        chars.append(0x12251)  #glyph00597	CUNEIFORM SIGN NIM TIMES GAR PLUS GAN2 TENU
        chars.append(0x12252)  #glyph00598	CUNEIFORM SIGN NINDA2
        chars.append(0x12253)  #glyph00599	CUNEIFORM SIGN NINDA2 TIMES AN
        chars.append(0x12254)  #glyph00600	CUNEIFORM SIGN NINDA2 TIMES ASH
        chars.append(0x12255)  #glyph00601	CUNEIFORM SIGN NINDA2 TIMES ASH PLUS ASH
        chars.append(0x12256)  #glyph00602	CUNEIFORM SIGN NINDA2 TIMES GUD
        chars.append(0x12257)  #glyph00603	CUNEIFORM SIGN NINDA2 TIMES ME PLUS GAN2 TENU
        chars.append(0x12258)  #glyph00604	CUNEIFORM SIGN NINDA2 TIMES NE
        chars.append(0x12259)  #glyph00605	CUNEIFORM SIGN NINDA2 TIMES NUN
        chars.append(0x1225A)  #glyph00606	CUNEIFORM SIGN NINDA2 TIMES SHE
        chars.append(0x1225B)  #glyph00607	CUNEIFORM SIGN NINDA2 TIMES SHE PLUS A AN
        chars.append(0x1225C)  #glyph00608	CUNEIFORM SIGN NINDA2 TIMES SHE PLUS ASH
        chars.append(0x1225D)  #glyph00609	CUNEIFORM SIGN NINDA2 TIMES SHE PLUS ASH PLUS ASH
        chars.append(0x1225E)  #glyph00610	CUNEIFORM SIGN NINDA2 TIMES U2 PLUS ASH
        chars.append(0x1225F)  #glyph00611	CUNEIFORM SIGN NINDA2 TIMES USH
        chars.append(0x12260)  #glyph00612	CUNEIFORM SIGN NISAG
        chars.append(0x12261)  #glyph00613	CUNEIFORM SIGN NU
        chars.append(0x12262)  #glyph00614	CUNEIFORM SIGN NU11
        chars.append(0x12263)  #glyph00615	CUNEIFORM SIGN NUN
        chars.append(0x12264)  #glyph00616	CUNEIFORM SIGN NUN LAGAR TIMES GAR
        chars.append(0x12265)  #glyph00617	CUNEIFORM SIGN NUN LAGAR TIMES MASH
        chars.append(0x12266)  #glyph00618	CUNEIFORM SIGN NUN LAGAR TIMES SAL
        chars.append(0x12267)  #glyph00619	CUNEIFORM SIGN NUN LAGAR TIMES SAL OVER NUN LAGAR TIMES SAL
        chars.append(0x12268)  #glyph00620	CUNEIFORM SIGN NUN LAGAR TIMES USH
        chars.append(0x12269)  #glyph00621	CUNEIFORM SIGN NUN TENU
        chars.append(0x1226A)  #glyph00622	CUNEIFORM SIGN NUN OVER NUN
        chars.append(0x1226B)  #glyph00623	CUNEIFORM SIGN NUN CROSSING NUN
        chars.append(0x1226C)  #glyph00624	CUNEIFORM SIGN NUN CROSSING NUN LAGAR OVER LAGAR
        chars.append(0x1226D)  #glyph00625	CUNEIFORM SIGN NUNUZ
        chars.append(0x1226E)  #glyph00626	CUNEIFORM SIGN NUNUZ AB2 TIMES ASHGAB
        chars.append(0x1226F)  #glyph00627	CUNEIFORM SIGN NUNUZ AB2 TIMES BI
        chars.append(0x12270)  #glyph00628	CUNEIFORM SIGN NUNUZ AB2 TIMES DUG
        chars.append(0x12271)  #glyph00629	CUNEIFORM SIGN NUNUZ AB2 TIMES GUD
        chars.append(0x12272)  #glyph00630	CUNEIFORM SIGN NUNUZ AB2 TIMES IGI GUNU
        chars.append(0x12273)  #glyph00631	CUNEIFORM SIGN NUNUZ AB2 TIMES KAD3
        chars.append(0x12274)  #glyph00632	CUNEIFORM SIGN NUNUZ AB2 TIMES LA
        chars.append(0x12275)  #glyph00633	CUNEIFORM SIGN NUNUZ AB2 TIMES NE
        chars.append(0x12276)  #glyph00634	CUNEIFORM SIGN NUNUZ AB2 TIMES SILA3
        chars.append(0x12277)  #glyph00635	CUNEIFORM SIGN NUNUZ AB2 TIMES U2
        chars.append(0x12278)  #glyph00636	CUNEIFORM SIGN NUNUZ KISIM5 TIMES BI
        chars.append(0x12279)  #glyph00637	CUNEIFORM SIGN NUNUZ KISIM5 TIMES BI U
        chars.append(0x1227A)  #glyph00638	CUNEIFORM SIGN PA
        chars.append(0x1227B)  #glyph00639	CUNEIFORM SIGN PAD
        chars.append(0x1227C)  #glyph00640	CUNEIFORM SIGN PAN
        chars.append(0x1227D)  #glyph00641	CUNEIFORM SIGN PAP
        chars.append(0x1227E)  #glyph00642	CUNEIFORM SIGN PESH2
        chars.append(0x1227F)  #glyph00643	CUNEIFORM SIGN PI
        chars.append(0x12280)  #glyph00644	CUNEIFORM SIGN PI TIMES A
        chars.append(0x12281)  #glyph00645	CUNEIFORM SIGN PI TIMES AB
        chars.append(0x12282)  #glyph00646	CUNEIFORM SIGN PI TIMES BI
        chars.append(0x12283)  #glyph00647	CUNEIFORM SIGN PI TIMES BU
        chars.append(0x12284)  #glyph00648	CUNEIFORM SIGN PI TIMES E
        chars.append(0x12285)  #glyph00649	CUNEIFORM SIGN PI TIMES I
        chars.append(0x12286)  #glyph00650	CUNEIFORM SIGN PI TIMES IB
        chars.append(0x12287)  #glyph00651	CUNEIFORM SIGN PI TIMES U
        chars.append(0x12288)  #glyph00652	CUNEIFORM SIGN PI TIMES U2
        chars.append(0x12289)  #glyph00653	CUNEIFORM SIGN PI CROSSING PI
        chars.append(0x1228A)  #glyph00654	CUNEIFORM SIGN PIRIG
        chars.append(0x1228B)  #glyph00655	CUNEIFORM SIGN PIRIG TIMES KAL
        chars.append(0x1228C)  #glyph00656	CUNEIFORM SIGN PIRIG TIMES UD
        chars.append(0x1228D)  #glyph00657	CUNEIFORM SIGN PIRIG TIMES ZA
        chars.append(0x1228E)  #glyph00658	CUNEIFORM SIGN PIRIG OPPOSING PIRIG
        chars.append(0x1228F)  #glyph00659	CUNEIFORM SIGN RA
        chars.append(0x12290)  #glyph00660	CUNEIFORM SIGN RAB
        chars.append(0x12291)  #glyph00661	CUNEIFORM SIGN RI
        chars.append(0x12292)  #glyph00662	CUNEIFORM SIGN RU
        chars.append(0x12293)  #glyph00663	CUNEIFORM SIGN SA
        chars.append(0x12294)  #glyph00664	CUNEIFORM SIGN SAG NUTILLU
        chars.append(0x12295)  #glyph00665	CUNEIFORM SIGN SAG
        chars.append(0x12296)  #glyph00666	CUNEIFORM SIGN SAG TIMES A
        chars.append(0x12297)  #glyph00667	CUNEIFORM SIGN SAG TIMES DU
        chars.append(0x12298)  #glyph00668	CUNEIFORM SIGN SAG TIMES DUB
        chars.append(0x12299)  #glyph00669	CUNEIFORM SIGN SAG TIMES HA
        chars.append(0x1229A)  #glyph00670	CUNEIFORM SIGN SAG TIMES KAK
        chars.append(0x1229B)  #glyph00671	CUNEIFORM SIGN SAG TIMES KUR
        chars.append(0x1229C)  #glyph00672	CUNEIFORM SIGN SAG TIMES LUM
        chars.append(0x1229D)  #glyph00673	CUNEIFORM SIGN SAG TIMES MI
        chars.append(0x1229E)  #glyph00674	CUNEIFORM SIGN SAG TIMES NUN
        chars.append(0x1229F)  #glyph00675	CUNEIFORM SIGN SAG TIMES SAL
        chars.append(0x122A0)  #glyph00676	CUNEIFORM SIGN SAG TIMES SHID
        chars.append(0x122A1)  #glyph00677	CUNEIFORM SIGN SAG TIMES TAB
        chars.append(0x122A2)  #glyph00678	CUNEIFORM SIGN SAG TIMES U2
        chars.append(0x122A3)  #glyph00679	CUNEIFORM SIGN SAG TIMES UB
        chars.append(0x122A4)  #glyph00680	CUNEIFORM SIGN SAG TIMES UM
        chars.append(0x122A5)  #glyph00681	CUNEIFORM SIGN SAG TIMES UR
        chars.append(0x122A6)  #glyph00682	CUNEIFORM SIGN SAG TIMES USH
        chars.append(0x122A7)  #glyph00683	CUNEIFORM SIGN SAG OVER SAG
        chars.append(0x122A8)  #glyph00684	CUNEIFORM SIGN SAG GUNU
        chars.append(0x122A9)  #glyph00685	CUNEIFORM SIGN SAL
        chars.append(0x122AA)  #glyph00686	CUNEIFORM SIGN SAL LAGAB TIMES ASH2
        chars.append(0x122AB)  #glyph00687	CUNEIFORM SIGN SANGA2
        chars.append(0x122AC)  #glyph00688	CUNEIFORM SIGN SAR
        chars.append(0x122AD)  #glyph00689	CUNEIFORM SIGN SHA
        chars.append(0x122AE)  #glyph00690	CUNEIFORM SIGN SHA3
        chars.append(0x122AF)  #glyph00691	CUNEIFORM SIGN SHA3 TIMES A
        chars.append(0x122B0)  #glyph00692	CUNEIFORM SIGN SHA3 TIMES BAD
        chars.append(0x122B1)  #glyph00693	CUNEIFORM SIGN SHA3 TIMES GISH
        chars.append(0x122B2)  #glyph00694	CUNEIFORM SIGN SHA3 TIMES NE
        chars.append(0x122B3)  #glyph00695	CUNEIFORM SIGN SHA3 TIMES SHU2
        chars.append(0x122B4)  #glyph00696	CUNEIFORM SIGN SHA3 TIMES TUR
        chars.append(0x122B5)  #glyph00697	CUNEIFORM SIGN SHA3 TIMES U
        chars.append(0x122B6)  #glyph00698	CUNEIFORM SIGN SHA3 TIMES U PLUS A
        chars.append(0x122B7)  #glyph00699	CUNEIFORM SIGN SHA6
        chars.append(0x122B8)  #glyph00700	CUNEIFORM SIGN SHAB6
        chars.append(0x122B9)  #glyph00701	CUNEIFORM SIGN SHAR2
        chars.append(0x122BA)  #glyph00702	CUNEIFORM SIGN SHE
        chars.append(0x122BB)  #glyph00703	CUNEIFORM SIGN SHE HU
        chars.append(0x122BC)  #glyph00704	CUNEIFORM SIGN SHE OVER SHE GAD OVER GAD GAR OVER GAR
        chars.append(0x122BD)  #glyph00705	CUNEIFORM SIGN SHE OVER SHE TAB OVER TAB GAR OVER GAR
        chars.append(0x122BE)  #glyph00706	CUNEIFORM SIGN SHEG9
        chars.append(0x122BF)  #glyph00707	CUNEIFORM SIGN SHEN
        chars.append(0x122C0)  #glyph00708	CUNEIFORM SIGN SHESH
        chars.append(0x122C1)  #glyph00709	CUNEIFORM SIGN SHESH2
        chars.append(0x122C2)  #glyph00710	CUNEIFORM SIGN SHESHLAM
        chars.append(0x122C3)  #glyph00711	CUNEIFORM SIGN SHID
        chars.append(0x122C4)  #glyph00712	CUNEIFORM SIGN SHID TIMES A
        chars.append(0x122C5)  #glyph00713	CUNEIFORM SIGN SHID TIMES IM
        chars.append(0x122C6)  #glyph00714	CUNEIFORM SIGN SHIM
        chars.append(0x122C7)  #glyph00715	CUNEIFORM SIGN SHIM TIMES A
        chars.append(0x122C8)  #glyph00716	CUNEIFORM SIGN SHIM TIMES BAL
        chars.append(0x122C9)  #glyph00717	CUNEIFORM SIGN SHIM TIMES BULUG
        chars.append(0x122CA)  #glyph00718	CUNEIFORM SIGN SHIM TIMES DIN
        chars.append(0x122CB)  #glyph00719	CUNEIFORM SIGN SHIM TIMES GAR
        chars.append(0x122CC)  #glyph00720	CUNEIFORM SIGN SHIM TIMES IGI
        chars.append(0x122CD)  #glyph00721	CUNEIFORM SIGN SHIM TIMES IGI GUNU
        chars.append(0x122CE)  #glyph00722	CUNEIFORM SIGN SHIM TIMES KUSHU2
        chars.append(0x122CF)  #glyph00723	CUNEIFORM SIGN SHIM TIMES LUL
        chars.append(0x122D0)  #glyph00724	CUNEIFORM SIGN SHIM TIMES MUG
        chars.append(0x122D1)  #glyph00725	CUNEIFORM SIGN SHIM TIMES SAL
        chars.append(0x122D2)  #glyph00726	CUNEIFORM SIGN SHINIG
        chars.append(0x122D3)  #glyph00727	CUNEIFORM SIGN SHIR
        chars.append(0x122D4)  #glyph00728	CUNEIFORM SIGN SHIR TENU
        chars.append(0x122D5)  #glyph00729	CUNEIFORM SIGN SHIR OVER SHIR BUR OVER BUR
        chars.append(0x122D6)  #glyph00730	CUNEIFORM SIGN SHITA
        chars.append(0x122D7)  #glyph00731	CUNEIFORM SIGN SHU
        chars.append(0x122D8)  #glyph00732	CUNEIFORM SIGN SHU OVER INVERTED SHU
        chars.append(0x122D9)  #glyph00733	CUNEIFORM SIGN SHU2
        chars.append(0x122DA)  #glyph00734	CUNEIFORM SIGN SHUBUR
        chars.append(0x122DB)  #glyph00735	CUNEIFORM SIGN SI
        chars.append(0x122DC)  #glyph00736	CUNEIFORM SIGN SI GUNU
        chars.append(0x122DD)  #glyph00737	CUNEIFORM SIGN SIG
        chars.append(0x122DE)  #glyph00738	CUNEIFORM SIGN SIG4
        chars.append(0x122DF)  #glyph00739	CUNEIFORM SIGN SIG4 OVER SIG4 SHU2
        chars.append(0x122E0)  #glyph00740	CUNEIFORM SIGN SIK2
        chars.append(0x122E1)  #glyph00741	CUNEIFORM SIGN SILA3
        chars.append(0x122E2)  #glyph00742	CUNEIFORM SIGN SU
        chars.append(0x122E3)  #glyph00743	CUNEIFORM SIGN SU OVER SU
        chars.append(0x122E4)  #glyph00744	CUNEIFORM SIGN SUD
        chars.append(0x122E5)  #glyph00745	CUNEIFORM SIGN SUD2
        chars.append(0x122E6)  #glyph00746	CUNEIFORM SIGN SUHUR
        chars.append(0x122E7)  #glyph00747	CUNEIFORM SIGN SUM
        chars.append(0x122E8)  #glyph00748	CUNEIFORM SIGN SUMASH
        chars.append(0x122E9)  #glyph00749	CUNEIFORM SIGN SUR
        chars.append(0x122EA)  #glyph00750	CUNEIFORM SIGN SUR9
        chars.append(0x122EB)  #glyph00751	CUNEIFORM SIGN TA
        chars.append(0x122EC)  #glyph00752	CUNEIFORM SIGN TA ASTERISK
        chars.append(0x122ED)  #glyph00753	CUNEIFORM SIGN TA TIMES HI
        chars.append(0x122EE)  #glyph00754	CUNEIFORM SIGN TA TIMES MI
        chars.append(0x122EF)  #glyph00755	CUNEIFORM SIGN TA GUNU
        chars.append(0x122F0)  #glyph00756	CUNEIFORM SIGN TAB
        chars.append(0x122F1)  #glyph00757	CUNEIFORM SIGN TAB OVER TAB NI OVER NI DISH OVER DISH
        chars.append(0x122F2)  #glyph00758	CUNEIFORM SIGN TAB SQUARED
        chars.append(0x122F3)  #glyph00759	CUNEIFORM SIGN TAG
        chars.append(0x122F4)  #glyph00760	CUNEIFORM SIGN TAG TIMES BI
        chars.append(0x122F5)  #glyph00761	CUNEIFORM SIGN TAG TIMES GUD
        chars.append(0x122F6)  #glyph00762	CUNEIFORM SIGN TAG TIMES SHE
        chars.append(0x122F7)  #glyph00763	CUNEIFORM SIGN TAG TIMES SHU
        chars.append(0x122F8)  #glyph00764	CUNEIFORM SIGN TAG TIMES TUG2
        chars.append(0x122F9)  #glyph00765	CUNEIFORM SIGN TAG TIMES UD
        chars.append(0x122FA)  #glyph00766	CUNEIFORM SIGN TAK4
        chars.append(0x122FB)  #glyph00767	CUNEIFORM SIGN TAR
        chars.append(0x122FC)  #glyph00768	CUNEIFORM SIGN TE
        chars.append(0x122FD)  #glyph00769	CUNEIFORM SIGN TE GUNU
        chars.append(0x122FE)  #glyph00770	CUNEIFORM SIGN TI
        chars.append(0x122FF)  #glyph00771	CUNEIFORM SIGN TI TENU
        chars.append(0x12300)  #glyph00772	CUNEIFORM SIGN TIL
        chars.append(0x12301)  #glyph00773	CUNEIFORM SIGN TIR
        chars.append(0x12302)  #glyph00774	CUNEIFORM SIGN TIR TIMES TAK4
        chars.append(0x12303)  #glyph00775	CUNEIFORM SIGN TIR OVER TIR
        chars.append(0x12304)  #glyph00776	CUNEIFORM SIGN TIR OVER TIR GAD OVER GAD GAR OVER GAR
        chars.append(0x12305)  #glyph00777	CUNEIFORM SIGN TU
        chars.append(0x12306)  #glyph00778	CUNEIFORM SIGN TUG2
        chars.append(0x12307)  #glyph00779	CUNEIFORM SIGN TUK
        chars.append(0x12308)  #glyph00780	CUNEIFORM SIGN TUM
        chars.append(0x12309)  #glyph00781	CUNEIFORM SIGN TUR
        chars.append(0x1230A)  #glyph00782	CUNEIFORM SIGN TUR OVER TUR ZA OVER ZA
        chars.append(0x1230B)  #glyph00783	CUNEIFORM SIGN U
        chars.append(0x1230C)  #glyph00784	CUNEIFORM SIGN U GUD
        chars.append(0x1230D)  #glyph00785	CUNEIFORM SIGN U U U
        chars.append(0x1230E)  #glyph00786	CUNEIFORM SIGN U OVER U PA OVER PA GAR OVER GAR
        chars.append(0x1230F)  #glyph00787	CUNEIFORM SIGN U OVER U SUR OVER SUR
        chars.append(0x12310)  #glyph00788	CUNEIFORM SIGN U OVER U U REVERSED OVER U REVERSED
        chars.append(0x12311)  #glyph00789	CUNEIFORM SIGN U2
        chars.append(0x12312)  #glyph00790	CUNEIFORM SIGN UB
        chars.append(0x12313)  #glyph00791	CUNEIFORM SIGN UD
        chars.append(0x12314)  #glyph00792	CUNEIFORM SIGN UD KUSHU2
        chars.append(0x12315)  #glyph00793	CUNEIFORM SIGN UD TIMES BAD
        chars.append(0x12316)  #glyph00794	CUNEIFORM SIGN UD TIMES MI
        chars.append(0x12317)  #glyph00795	CUNEIFORM SIGN UD TIMES U PLUS U PLUS U
        chars.append(0x12318)  #glyph00796	CUNEIFORM SIGN UD TIMES U PLUS U PLUS U GUNU
        chars.append(0x12319)  #glyph00797	CUNEIFORM SIGN UD GUNU
        chars.append(0x1231A)  #glyph00798	CUNEIFORM SIGN UD SHESHIG
        chars.append(0x1231B)  #glyph00799	CUNEIFORM SIGN UD SHESHIG TIMES BAD
        chars.append(0x1231C)  #glyph00800	CUNEIFORM SIGN UDUG
        chars.append(0x1231D)  #glyph00801	CUNEIFORM SIGN UM
        chars.append(0x1231E)  #glyph00802	CUNEIFORM SIGN UM TIMES LAGAB
        chars.append(0x1231F)  #glyph00803	CUNEIFORM SIGN UM TIMES ME PLUS DA
        chars.append(0x12320)  #glyph00804	CUNEIFORM SIGN UM TIMES SHA3
        chars.append(0x12321)  #glyph00805	CUNEIFORM SIGN UM TIMES U
        chars.append(0x12322)  #glyph00806	CUNEIFORM SIGN UMBIN
        chars.append(0x121DB)  #glyph00479	CUNEIFORM SIGN LAGAB TIMES NE
        chars.append(0x12324)  #glyph00808	CUNEIFORM SIGN UMUM TIMES KASKAL
        chars.append(0x12325)  #glyph00809	CUNEIFORM SIGN UMUM TIMES PA
        chars.append(0x12326)  #glyph00810	CUNEIFORM SIGN UN
        chars.append(0x12327)  #glyph00811	CUNEIFORM SIGN UN GUNU
        chars.append(0x12328)  #glyph00812	CUNEIFORM SIGN UR
        chars.append(0x12329)  #glyph00813	CUNEIFORM SIGN UR CROSSING UR
        chars.append(0x1232A)  #glyph00814	CUNEIFORM SIGN UR SHESHIG
        chars.append(0x1232B)  #glyph00815	CUNEIFORM SIGN UR2
        chars.append(0x1232C)  #glyph00816	CUNEIFORM SIGN UR2 TIMES A PLUS HA
        chars.append(0x1232D)  #glyph00817	CUNEIFORM SIGN UR2 TIMES A PLUS NA
        chars.append(0x1232E)  #glyph00818	CUNEIFORM SIGN UR2 TIMES AL
        chars.append(0x1232F)  #glyph00819	CUNEIFORM SIGN UR2 TIMES HA
        chars.append(0x12330)  #glyph00820	CUNEIFORM SIGN UR2 TIMES NUN
        chars.append(0x12331)  #glyph00821	CUNEIFORM SIGN UR2 TIMES U2
        chars.append(0x12332)  #glyph00822	CUNEIFORM SIGN UR2 TIMES U2 PLUS ASH
        chars.append(0x12333)  #glyph00823	CUNEIFORM SIGN UR2 TIMES U2 PLUS BI
        chars.append(0x12334)  #glyph00824	CUNEIFORM SIGN UR4
        chars.append(0x12335)  #glyph00825	CUNEIFORM SIGN URI
        chars.append(0x12336)  #glyph00826	CUNEIFORM SIGN URI3
        chars.append(0x12337)  #glyph00827	CUNEIFORM SIGN URU
        chars.append(0x12338)  #glyph00828	CUNEIFORM SIGN URU TIMES A
        chars.append(0x12339)  #glyph00829	CUNEIFORM SIGN URU TIMES ASHGAB
        chars.append(0x1233A)  #glyph00830	CUNEIFORM SIGN URU TIMES BAR
        chars.append(0x1233B)  #glyph00831	CUNEIFORM SIGN URU TIMES DUN
        chars.append(0x1233C)  #glyph00832	CUNEIFORM SIGN URU TIMES GA
        chars.append(0x1233D)  #glyph00833	CUNEIFORM SIGN URU TIMES GAL
        chars.append(0x1233E)  #glyph00834	CUNEIFORM SIGN URU TIMES GAN2 TENU
        chars.append(0x1233F)  #glyph00835	CUNEIFORM SIGN URU TIMES GAR
        chars.append(0x12340)  #glyph00836	CUNEIFORM SIGN URU TIMES GU
        chars.append(0x12341)  #glyph00837	CUNEIFORM SIGN URU TIMES HA
        chars.append(0x12342)  #glyph00838	CUNEIFORM SIGN URU TIMES IGI
        chars.append(0x12343)  #glyph00839	CUNEIFORM SIGN URU TIMES IM
        chars.append(0x12344)  #glyph00840	CUNEIFORM SIGN URU TIMES ISH
        chars.append(0x12345)  #glyph00841	CUNEIFORM SIGN URU TIMES KI
        chars.append(0x12346)  #glyph00842	CUNEIFORM SIGN URU TIMES LUM
        chars.append(0x12347)  #glyph00843	CUNEIFORM SIGN URU TIMES MIN
        chars.append(0x12348)  #glyph00844	CUNEIFORM SIGN URU TIMES PA
        chars.append(0x12349)  #glyph00845	CUNEIFORM SIGN URU TIMES SHE
        chars.append(0x1234A)  #glyph00846	CUNEIFORM SIGN URU TIMES SIG4
        chars.append(0x1234B)  #glyph00847	CUNEIFORM SIGN URU TIMES TU
        chars.append(0x1234C)  #glyph00848	CUNEIFORM SIGN URU TIMES U PLUS GUD
        chars.append(0x1234D)  #glyph00849	CUNEIFORM SIGN URU TIMES UD
        chars.append(0x1234E)  #glyph00850	CUNEIFORM SIGN URU TIMES URUDA
        chars.append(0x1234F)  #glyph00851	CUNEIFORM SIGN URUDA
        chars.append(0x12350)  #glyph00852	CUNEIFORM SIGN URUDA TIMES U
        chars.append(0x12351)  #glyph00853	CUNEIFORM SIGN USH
        chars.append(0x12352)  #glyph00854	CUNEIFORM SIGN USH TIMES A
        chars.append(0x12353)  #glyph00855	CUNEIFORM SIGN USH TIMES KU
        chars.append(0x12354)  #glyph00856	CUNEIFORM SIGN USH TIMES KUR
        chars.append(0x12355)  #glyph00857	CUNEIFORM SIGN USH TIMES TAK4
        chars.append(0x12356)  #glyph00858	CUNEIFORM SIGN USHX
        chars.append(0x12357)  #glyph00859	CUNEIFORM SIGN USH2
        chars.append(0x12358)  #glyph00860	CUNEIFORM SIGN USHUMX
        chars.append(0x12359)  #glyph00861	CUNEIFORM SIGN UTUKI
        chars.append(0x1235A)  #glyph00862	CUNEIFORM SIGN UZ3
        chars.append(0x1235B)  #glyph00863	CUNEIFORM SIGN UZ3 TIMES KASKAL
        chars.append(0x1235C)  #glyph00864	CUNEIFORM SIGN UZU
        chars.append(0x1235D)  #glyph00865	CUNEIFORM SIGN ZA
        chars.append(0x1235E)  #glyph00866	CUNEIFORM SIGN ZA TENU
        chars.append(0x1235F)  #glyph00867	CUNEIFORM SIGN ZA SQUARED TIMES KUR
        chars.append(0x12360)  #glyph00868	CUNEIFORM SIGN ZAG
        chars.append(0x12361)  #glyph00869	CUNEIFORM SIGN ZAMX
        chars.append(0x12362)  #glyph00870	CUNEIFORM SIGN ZE2
        chars.append(0x12363)  #glyph00871	CUNEIFORM SIGN ZI
        chars.append(0x12364)  #glyph00872	CUNEIFORM SIGN ZI OVER ZI
        chars.append(0x12365)  #glyph00873	CUNEIFORM SIGN ZI3
        chars.append(0x12366)  #glyph00874	CUNEIFORM SIGN ZIB
        chars.append(0x12367)  #glyph00875	CUNEIFORM SIGN ZIB KABA TENU
        chars.append(0x12368)  #glyph00876	CUNEIFORM SIGN ZIG
        chars.append(0x12369)  #glyph00877	CUNEIFORM SIGN ZIZ2
        chars.append(0x1236A)  #glyph00878	CUNEIFORM SIGN ZU
        chars.append(0x1236B)  #glyph00879	CUNEIFORM SIGN ZU5
        chars.append(0x1236C)  #glyph00880	CUNEIFORM SIGN ZU5 TIMES A
        chars.append(0x1236D)  #glyph00881	CUNEIFORM SIGN ZUBUR
        chars.append(0x1236E)  #glyph00882	CUNEIFORM SIGN ZUM
        chars.append(0x120A0)  #glyph00164	CUNEIFORM SIGN ESH2
        chars.append(0x12400)  #glyph00883	CUNEIFORM NUMERIC SIGN TWO ASH
        chars.append(0x12401)  #glyph00884	CUNEIFORM NUMERIC SIGN THREE ASH
        chars.append(0x12402)  #glyph00885	CUNEIFORM NUMERIC SIGN FOUR ASH
        chars.append(0x12403)  #glyph00886	CUNEIFORM NUMERIC SIGN FIVE ASH
        chars.append(0x12404)  #glyph00887	CUNEIFORM NUMERIC SIGN SIX ASH
        chars.append(0x12405)  #glyph00888	CUNEIFORM NUMERIC SIGN SEVEN ASH
        chars.append(0x12406)  #glyph00889	CUNEIFORM NUMERIC SIGN EIGHT ASH
        chars.append(0x12407)  #glyph00890	CUNEIFORM NUMERIC SIGN NINE ASH
        chars.append(0x12408)  #glyph00891	CUNEIFORM NUMERIC SIGN THREE DISH
        chars.append(0x12409)  #glyph00892	CUNEIFORM NUMERIC SIGN FOUR DISH
        chars.append(0x1240A)  #glyph00893	CUNEIFORM NUMERIC SIGN FIVE DISH
        chars.append(0x1240B)  #glyph00894	CUNEIFORM NUMERIC SIGN SIX DISH
        chars.append(0x1240C)  #glyph00895	CUNEIFORM NUMERIC SIGN SEVEN DISH
        chars.append(0x1240D)  #glyph00896	CUNEIFORM NUMERIC SIGN EIGHT DISH
        chars.append(0x1240E)  #glyph00897	CUNEIFORM NUMERIC SIGN NINE DISH
        chars.append(0x1240F)  #glyph00898	CUNEIFORM NUMERIC SIGN FOUR U
        chars.append(0x12410)  #glyph00899	CUNEIFORM NUMERIC SIGN FIVE U
        chars.append(0x12411)  #glyph00900	CUNEIFORM NUMERIC SIGN SIX U
        chars.append(0x12412)  #glyph00901	CUNEIFORM NUMERIC SIGN SEVEN U
        chars.append(0x12413)  #glyph00902	CUNEIFORM NUMERIC SIGN EIGHT U
        chars.append(0x12414)  #glyph00903	CUNEIFORM NUMERIC SIGN NINE U
        chars.append(0x12415)  #glyph00904	CUNEIFORM NUMERIC SIGN ONE GESH2
        chars.append(0x12416)  #glyph00905	CUNEIFORM NUMERIC SIGN TWO GESH2
        chars.append(0x12417)  #glyph00906	CUNEIFORM NUMERIC SIGN THREE GESH2
        chars.append(0x12418)  #glyph00907	CUNEIFORM NUMERIC SIGN FOUR GESH2
        chars.append(0x12419)  #glyph00908	CUNEIFORM NUMERIC SIGN FIVE GESH2
        chars.append(0x1241A)  #glyph00909	CUNEIFORM NUMERIC SIGN SIX GESH2
        chars.append(0x1241B)  #glyph00910	CUNEIFORM NUMERIC SIGN SEVEN GESH2
        chars.append(0x1241C)  #glyph00911	CUNEIFORM NUMERIC SIGN EIGHT GESH2
        chars.append(0x1241D)  #glyph00912	CUNEIFORM NUMERIC SIGN NINE GESH2
        chars.append(0x1241E)  #glyph00913	CUNEIFORM NUMERIC SIGN ONE GESHU
        chars.append(0x1241F)  #glyph00914	CUNEIFORM NUMERIC SIGN TWO GESHU
        chars.append(0x12420)  #glyph00915	CUNEIFORM NUMERIC SIGN THREE GESHU
        chars.append(0x12421)  #glyph00916	CUNEIFORM NUMERIC SIGN FOUR GESHU
        chars.append(0x12422)  #glyph00917	CUNEIFORM NUMERIC SIGN FIVE GESHU
        chars.append(0x12423)  #glyph00918	CUNEIFORM NUMERIC SIGN TWO SHAR2
        chars.append(0x12424)  #glyph00919	CUNEIFORM NUMERIC SIGN THREE SHAR2
        chars.append(0x12425)  #glyph00920	CUNEIFORM NUMERIC SIGN THREE SHAR2 VARIANT FORM
        chars.append(0x12426)  #glyph00921	CUNEIFORM NUMERIC SIGN FOUR SHAR2
        chars.append(0x12427)  #glyph00922	CUNEIFORM NUMERIC SIGN FIVE SHAR2
        chars.append(0x12428)  #glyph00923	CUNEIFORM NUMERIC SIGN SIX SHAR2
        chars.append(0x12429)  #glyph00924	CUNEIFORM NUMERIC SIGN SEVEN SHAR2
        chars.append(0x1242A)  #glyph00925	CUNEIFORM NUMERIC SIGN EIGHT SHAR2
        chars.append(0x1242B)  #glyph00926	CUNEIFORM NUMERIC SIGN NINE SHAR2
        chars.append(0x1242C)  #glyph00927	CUNEIFORM NUMERIC SIGN ONE SHARU
        chars.append(0x1242D)  #glyph00928	CUNEIFORM NUMERIC SIGN TWO SHARU
        chars.append(0x1242E)  #glyph00929	CUNEIFORM NUMERIC SIGN THREE SHARU
        chars.append(0x1242F)  #glyph00930	CUNEIFORM NUMERIC SIGN THREE SHARU VARIANT FORM
        chars.append(0x12430)  #glyph00931	CUNEIFORM NUMERIC SIGN FOUR SHARU
        chars.append(0x12431)  #glyph00932	CUNEIFORM NUMERIC SIGN FIVE SHARU
        chars.append(0x12432)  #glyph00933	CUNEIFORM NUMERIC SIGN SHAR2 TIMES GAL PLUS DISH
        chars.append(0x12433)  #glyph00934	CUNEIFORM NUMERIC SIGN SHAR2 TIMES GAL PLUS MIN
        chars.append(0x12434)  #glyph00935	CUNEIFORM NUMERIC SIGN ONE BURU
        chars.append(0x12435)  #glyph00936	CUNEIFORM NUMERIC SIGN TWO BURU
        chars.append(0x12436)  #glyph00937	CUNEIFORM NUMERIC SIGN THREE BURU
        chars.append(0x12437)  #glyph00938	CUNEIFORM NUMERIC SIGN THREE BURU VARIANT FORM
        chars.append(0x12438)  #glyph00939	CUNEIFORM NUMERIC SIGN FOUR BURU
        chars.append(0x12439)  #glyph00940	CUNEIFORM NUMERIC SIGN FIVE BURU
        chars.append(0x1243A)  #glyph00941	CUNEIFORM NUMERIC SIGN THREE VARIANT FORM ESH16
        chars.append(0x1243B)  #glyph00942	CUNEIFORM NUMERIC SIGN THREE VARIANT FORM ESH21
        chars.append(0x1243C)  #glyph00943	CUNEIFORM NUMERIC SIGN FOUR VARIANT FORM LIMMU
        chars.append(0x1243D)  #glyph00944	CUNEIFORM NUMERIC SIGN FOUR VARIANT FORM LIMMU4
        chars.append(0x1243E)  #glyph00945	CUNEIFORM NUMERIC SIGN FOUR VARIANT FORM LIMMU A
        chars.append(0x1243F)  #glyph00946	CUNEIFORM NUMERIC SIGN FOUR VARIANT FORM LIMMU B
        chars.append(0x12440)  #glyph00947	CUNEIFORM NUMERIC SIGN SIX VARIANT FORM ASH9
        chars.append(0x12441)  #glyph00948	CUNEIFORM NUMERIC SIGN SEVEN VARIANT FORM IMIN3
        chars.append(0x12442)  #glyph00949	CUNEIFORM NUMERIC SIGN SEVEN VARIANT FORM IMIN A
        chars.append(0x12443)  #glyph00950	CUNEIFORM NUMERIC SIGN SEVEN VARIANT FORM IMIN B
        chars.append(0x12444)  #glyph00951	CUNEIFORM NUMERIC SIGN EIGHT VARIANT FORM USSU
        chars.append(0x12445)  #glyph00952	CUNEIFORM NUMERIC SIGN EIGHT VARIANT FORM USSU3
        chars.append(0x12446)  #glyph00953	CUNEIFORM NUMERIC SIGN NINE VARIANT FORM ILIMMU
        chars.append(0x12447)  #glyph00954	CUNEIFORM NUMERIC SIGN NINE VARIANT FORM ILIMMU3
        chars.append(0x12448)  #glyph00955	CUNEIFORM NUMERIC SIGN NINE VARIANT FORM ILIMMU4
        chars.append(0x12449)  #glyph00956	CUNEIFORM NUMERIC SIGN NINE VARIANT FORM ILIMMU A
        chars.append(0x1244A)  #glyph00957	CUNEIFORM NUMERIC SIGN TWO ASH TENU
        chars.append(0x1244B)  #glyph00958	CUNEIFORM NUMERIC SIGN THREE ASH TENU
        chars.append(0x1244C)  #glyph00959	CUNEIFORM NUMERIC SIGN FOUR ASH TENU
        chars.append(0x1244D)  #glyph00960	CUNEIFORM NUMERIC SIGN FIVE ASH TENU
        chars.append(0x1244E)  #glyph00961	CUNEIFORM NUMERIC SIGN SIX ASH TENU
        chars.append(0x1244F)  #glyph00962	CUNEIFORM NUMERIC SIGN ONE BAN2
        chars.append(0x12450)  #glyph00963	CUNEIFORM NUMERIC SIGN TWO BAN2
        chars.append(0x12451)  #glyph00964	CUNEIFORM NUMERIC SIGN THREE BAN2
        chars.append(0x12452)  #glyph00965	CUNEIFORM NUMERIC SIGN FOUR BAN2
        chars.append(0x12453)  #glyph00966	CUNEIFORM NUMERIC SIGN FOUR BAN2 VARIANT FORM
        chars.append(0x12454)  #glyph00967	CUNEIFORM NUMERIC SIGN FIVE BAN2
        chars.append(0x12455)  #glyph00968	CUNEIFORM NUMERIC SIGN FIVE BAN2 VARIANT FORM
        chars.append(0x12456)  #glyph00969	CUNEIFORM NUMERIC SIGN NIGIDAMIN
        chars.append(0x12457)  #glyph00970	CUNEIFORM NUMERIC SIGN NIGIDAESH
        chars.append(0x12458)  #glyph00971	CUNEIFORM NUMERIC SIGN ONE ESHE3
        chars.append(0x12459)  #glyph00972	CUNEIFORM NUMERIC SIGN TWO ESHE3
        chars.append(0x1245A)  #glyph00973	CUNEIFORM NUMERIC SIGN ONE THIRD DISH
        chars.append(0x1245B)  #glyph00974	CUNEIFORM NUMERIC SIGN TWO THIRDS DISH
        chars.append(0x1245C)  #glyph00975	CUNEIFORM NUMERIC SIGN FIVE SIXTHS DISH
        chars.append(0x1245D)  #glyph00976	CUNEIFORM NUMERIC SIGN ONE THIRD VARIANT FORM A
        chars.append(0x1245E)  #glyph00977	CUNEIFORM NUMERIC SIGN TWO THIRDS VARIANT FORM A
        chars.append(0x1245F)  #glyph00978	CUNEIFORM NUMERIC SIGN ONE EIGHTH ASH
        chars.append(0x12460)  #glyph00979	CUNEIFORM NUMERIC SIGN ONE QUARTER ASH
        chars.append(0x12461)  #glyph00980	CUNEIFORM NUMERIC SIGN OLD ASSYRIAN ONE SIXTH
        chars.append(0x12462)  #glyph00981	CUNEIFORM NUMERIC SIGN OLD ASSYRIAN ONE QUARTER
        chars.append(0x12470)  #glyph00982	CUNEIFORM PUNCTUATION SIGN OLD ASSYRIAN WORD DIVIDER
        chars.append(0x12471)  #glyph00983	CUNEIFORM PUNCTUATION SIGN VERTICAL COLON
        chars.append(0x12472)  #glyph00984	CUNEIFORM PUNCTUATION SIGN DIAGONAL COLON
        chars.append(0x12473)  #glyph00985	CUNEIFORM PUNCTUATION SIGN DIAGONAL TRICOLON
        chars.append(0x120C1)  #glyph00197	CUNEIFORM SIGN GA2 TIMES BUR
        chars.append(0x12103)  #glyph00263	CUNEIFORM SIGN GI CROSSING GI
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x12323)  #glyph00807	CUNEIFORM SIGN UMUM
        return chars


