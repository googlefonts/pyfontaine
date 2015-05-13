# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansBamum-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0xA6A1)  #uniA6A1	BAMUM LETTER KA
        chars.append(0xA6A2)  #uniA6A2	BAMUM LETTER U
        chars.append(0xA6A3)  #uniA6A3	BAMUM LETTER KU
        chars.append(0xA6A4)  #uniA6A4	BAMUM LETTER EE
        chars.append(0xA6A5)  #uniA6A5	BAMUM LETTER REE
        chars.append(0xA6A6)  #uniA6A6	BAMUM LETTER TAE
        chars.append(0xA6A7)  #uniA6A7	BAMUM LETTER O
        chars.append(0xA6A8)  #uniA6A8	BAMUM LETTER NYI
        chars.append(0xA6A9)  #uniA6A9	BAMUM LETTER I
        chars.append(0xA6AA)  #uniA6AA	BAMUM LETTER LA
        chars.append(0xA6AB)  #uniA6AB	BAMUM LETTER PA
        chars.append(0xA6AC)  #uniA6AC	BAMUM LETTER RII
        chars.append(0xA6AD)  #uniA6AD	BAMUM LETTER RIEE
        chars.append(0xA6AE)  #uniA6AE	BAMUM LETTER LEEEE
        chars.append(0xA6AF)  #uniA6AF	BAMUM LETTER MEEEE
        chars.append(0xA6B0)  #uniA6B0	BAMUM LETTER TAA
        chars.append(0xA6B1)  #uniA6B1	BAMUM LETTER NDAA
        chars.append(0xA6B2)  #uniA6B2	BAMUM LETTER NJAEM
        chars.append(0xA6B3)  #uniA6B3	BAMUM LETTER M
        chars.append(0xA6B4)  #uniA6B4	BAMUM LETTER SUU
        chars.append(0xA6B5)  #uniA6B5	BAMUM LETTER MU
        chars.append(0xA6B6)  #uniA6B6	BAMUM LETTER SHII
        chars.append(0xA6B7)  #uniA6B7	BAMUM LETTER SI
        chars.append(0xA6B8)  #uniA6B8	BAMUM LETTER SHEUX
        chars.append(0xA6B9)  #uniA6B9	BAMUM LETTER SEUX
        chars.append(0xA6BA)  #uniA6BA	BAMUM LETTER KYEE
        chars.append(0xA6BB)  #uniA6BB	BAMUM LETTER KET
        chars.append(0xA6BC)  #uniA6BC	BAMUM LETTER NUAE
        chars.append(0xA6BD)  #uniA6BD	BAMUM LETTER NU
        chars.append(0xA6BE)  #uniA6BE	BAMUM LETTER NJUAE
        chars.append(0xA6BF)  #uniA6BF	BAMUM LETTER YOQ
        chars.append(0xA6C0)  #uniA6C0	BAMUM LETTER SHU
        chars.append(0xA6C1)  #uniA6C1	BAMUM LETTER YUQ
        chars.append(0xA6C2)  #uniA6C2	BAMUM LETTER YA
        chars.append(0xA6C3)  #uniA6C3	BAMUM LETTER NSHA
        chars.append(0xA6C4)  #uniA6C4	BAMUM LETTER KEUX
        chars.append(0xA6C5)  #uniA6C5	BAMUM LETTER PEUX
        chars.append(0xA6C6)  #uniA6C6	BAMUM LETTER NJEE
        chars.append(0xA6C7)  #uniA6C7	BAMUM LETTER NTEE
        chars.append(0xA6C8)  #uniA6C8	BAMUM LETTER PUE
        chars.append(0xA6C9)  #uniA6C9	BAMUM LETTER WUE
        chars.append(0xA6CA)  #uniA6CA	BAMUM LETTER PEE
        chars.append(0xA6CB)  #uniA6CB	BAMUM LETTER FEE
        chars.append(0xA6CC)  #uniA6CC	BAMUM LETTER RU
        chars.append(0xA6CD)  #uniA6CD	BAMUM LETTER LU
        chars.append(0xA6CE)  #uniA6CE	BAMUM LETTER MI
        chars.append(0xA6CF)  #uniA6CF	BAMUM LETTER NI
        chars.append(0xA6D0)  #uniA6D0	BAMUM LETTER REUX
        chars.append(0xA6D1)  #uniA6D1	BAMUM LETTER RAE
        chars.append(0xA6D2)  #uniA6D2	BAMUM LETTER KEN
        chars.append(0xA6D3)  #uniA6D3	BAMUM LETTER NGKWAEN
        chars.append(0xA6D4)  #uniA6D4	BAMUM LETTER NGGA
        chars.append(0xA6D5)  #uniA6D5	BAMUM LETTER NGA
        chars.append(0xA6D6)  #uniA6D6	BAMUM LETTER SHO
        chars.append(0xA6D7)  #uniA6D7	BAMUM LETTER PUAE
        chars.append(0xA6D8)  #uniA6D8	BAMUM LETTER FU
        chars.append(0xA6D9)  #uniA6D9	BAMUM LETTER FOM
        chars.append(0xA6DA)  #uniA6DA	BAMUM LETTER WA
        chars.append(0xA6DB)  #uniA6DB	BAMUM LETTER NA
        chars.append(0xA6DC)  #uniA6DC	BAMUM LETTER LI
        chars.append(0xA6DD)  #uniA6DD	BAMUM LETTER PI
        chars.append(0xA6DE)  #uniA6DE	BAMUM LETTER LOQ
        chars.append(0xA6DF)  #uniA6DF	BAMUM LETTER KO
        chars.append(0xA6E0)  #uniA6E0	BAMUM LETTER MBEN
        chars.append(0xA6E1)  #uniA6E1	BAMUM LETTER REN
        chars.append(0xA6E2)  #uniA6E2	BAMUM LETTER MEN
        chars.append(0xA6E3)  #uniA6E3	BAMUM LETTER MA
        chars.append(0xA6E4)  #uniA6E4	BAMUM LETTER TI
        chars.append(0xA6E5)  #uniA6E5	BAMUM LETTER KI
        chars.append(0xA6E6)  #uniA6E6	BAMUM LETTER MO
        chars.append(0xA6E7)  #uniA6E7	BAMUM LETTER MBAA
        chars.append(0xA6E8)  #uniA6E8	BAMUM LETTER TET
        chars.append(0xA6E9)  #uniA6E9	BAMUM LETTER KPA
        chars.append(0xA6EA)  #uniA6EA	BAMUM LETTER TEN
        chars.append(0xA6EB)  #uniA6EB	BAMUM LETTER NTUU
        chars.append(0xA6EC)  #uniA6EC	BAMUM LETTER SAMBA
        chars.append(0xA6ED)  #uniA6ED	BAMUM LETTER FAAMAE
        chars.append(0xA6EE)  #uniA6EE	BAMUM LETTER KOVUU
        chars.append(0xA6EF)  #uniA6EF	BAMUM LETTER KOGHOM
        chars.append(0xA6F0)  #uniA6F0	BAMUM COMBINING MARK KOQNDON
        chars.append(0xA6F1)  #uniA6F1	BAMUM COMBINING MARK TUKWENTIS
        chars.append(0xA6F2)  #uniA6F2	BAMUM NJAEMLI
        chars.append(0xA6F3)  #uniA6F3	BAMUM FULL STOP
        chars.append(0xA6F4)  #uniA6F4	BAMUM COLON
        chars.append(0xA6F5)  #uniA6F5	BAMUM COMMA
        chars.append(0xA6F6)  #uniA6F6	BAMUM SEMICOLON
        chars.append(0xA6F7)  #uniA6F7	BAMUM QUESTION MARK
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xA6A0)  #uniA6A0	BAMUM LETTER A
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x16800)  #glyph00092	????
        chars.append(0x16802)  #glyph00094	????
        chars.append(0x16803)  #glyph00095	????
        chars.append(0x16804)  #glyph00096	????
        chars.append(0x16805)  #glyph00097	????
        chars.append(0x16806)  #glyph00098	????
        chars.append(0x16801)  #glyph00093	????
        chars.append(0x16808)  #glyph00100	????
        chars.append(0x16809)  #glyph00101	????
        chars.append(0x1680A)  #glyph00102	????
        chars.append(0x1680B)  #glyph00103	????
        chars.append(0x1680C)  #glyph00104	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x1680E)  #glyph00106	????
        chars.append(0x1680F)  #glyph00107	????
        chars.append(0x16810)  #glyph00108	????
        chars.append(0x16811)  #glyph00109	????
        chars.append(0x16812)  #glyph00110	????
        chars.append(0x16813)  #glyph00111	????
        chars.append(0x16814)  #glyph00112	????
        chars.append(0x16815)  #glyph00113	????
        chars.append(0x16816)  #glyph00114	????
        chars.append(0x16817)  #glyph00115	????
        chars.append(0x16818)  #glyph00116	????
        chars.append(0x16819)  #glyph00117	????
        chars.append(0x1681A)  #glyph00118	????
        chars.append(0x1681B)  #glyph00119	????
        chars.append(0x1681C)  #glyph00120	????
        chars.append(0x1681D)  #glyph00121	????
        chars.append(0x1681E)  #glyph00122	????
        chars.append(0x1681F)  #glyph00123	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x16821)  #glyph00125	????
        chars.append(0x16822)  #glyph00126	????
        chars.append(0x16823)  #glyph00127	????
        chars.append(0x16824)  #glyph00128	????
        chars.append(0x16825)  #glyph00129	????
        chars.append(0x16826)  #glyph00130	????
        chars.append(0x16827)  #glyph00131	????
        chars.append(0x16828)  #glyph00132	????
        chars.append(0x16829)  #glyph00133	????
        chars.append(0x1682A)  #glyph00134	????
        chars.append(0x16807)  #glyph00099	????
        chars.append(0x1682C)  #glyph00136	????
        chars.append(0x1682D)  #glyph00137	????
        chars.append(0x1682E)  #glyph00138	????
        chars.append(0x1682F)  #glyph00139	????
        chars.append(0x16830)  #glyph00140	????
        chars.append(0x16831)  #glyph00141	????
        chars.append(0x16832)  #glyph00142	????
        chars.append(0x16833)  #glyph00143	????
        chars.append(0x16834)  #glyph00144	????
        chars.append(0x16835)  #glyph00145	????
        chars.append(0x16836)  #glyph00146	????
        chars.append(0x16837)  #glyph00147	????
        chars.append(0x16838)  #glyph00148	????
        chars.append(0x16839)  #glyph00149	????
        chars.append(0x1683A)  #glyph00150	????
        chars.append(0x1683B)  #glyph00151	????
        chars.append(0x1683C)  #glyph00152	????
        chars.append(0x1683D)  #glyph00153	????
        chars.append(0x1683E)  #glyph00154	????
        chars.append(0x1683F)  #glyph00155	????
        chars.append(0x16840)  #glyph00156	????
        chars.append(0x16841)  #glyph00157	????
        chars.append(0x16842)  #glyph00158	????
        chars.append(0x16843)  #glyph00159	????
        chars.append(0x16844)  #glyph00160	????
        chars.append(0x16845)  #glyph00161	????
        chars.append(0x16846)  #glyph00162	????
        chars.append(0x16847)  #glyph00163	????
        chars.append(0x16848)  #glyph00164	????
        chars.append(0x16849)  #glyph00165	????
        chars.append(0x1684A)  #glyph00166	????
        chars.append(0x1684B)  #glyph00167	????
        chars.append(0x1684C)  #glyph00168	????
        chars.append(0x1684D)  #glyph00169	????
        chars.append(0x1684E)  #glyph00170	????
        chars.append(0x1680D)  #glyph00105	????
        chars.append(0x16850)  #glyph00172	????
        chars.append(0x16851)  #glyph00173	????
        chars.append(0x16852)  #glyph00174	????
        chars.append(0x16853)  #glyph00175	????
        chars.append(0x16854)  #glyph00176	????
        chars.append(0x16855)  #glyph00177	????
        chars.append(0x16856)  #glyph00178	????
        chars.append(0x16857)  #glyph00179	????
        chars.append(0x16858)  #glyph00180	????
        chars.append(0x16859)  #glyph00181	????
        chars.append(0x1685A)  #glyph00182	????
        chars.append(0x1685B)  #glyph00183	????
        chars.append(0x1685C)  #glyph00184	????
        chars.append(0x1685D)  #glyph00185	????
        chars.append(0x1685E)  #glyph00186	????
        chars.append(0x1685F)  #glyph00187	????
        chars.append(0x16860)  #glyph00188	????
        chars.append(0x16861)  #glyph00189	????
        chars.append(0x16862)  #glyph00190	????
        chars.append(0x16863)  #glyph00191	????
        chars.append(0x16864)  #glyph00192	????
        chars.append(0x16865)  #glyph00193	????
        chars.append(0x16866)  #glyph00194	????
        chars.append(0x16867)  #glyph00195	????
        chars.append(0x16868)  #glyph00196	????
        chars.append(0x16869)  #glyph00197	????
        chars.append(0x1686A)  #glyph00198	????
        chars.append(0x1686B)  #glyph00199	????
        chars.append(0x1686C)  #glyph00200	????
        chars.append(0x1686D)  #glyph00201	????
        chars.append(0x1686E)  #glyph00202	????
        chars.append(0x1686F)  #glyph00203	????
        chars.append(0x16870)  #glyph00204	????
        chars.append(0x16871)  #glyph00205	????
        chars.append(0x16872)  #glyph00206	????
        chars.append(0x16873)  #glyph00207	????
        chars.append(0x16874)  #glyph00208	????
        chars.append(0x16875)  #glyph00209	????
        chars.append(0x16876)  #glyph00210	????
        chars.append(0x16877)  #glyph00211	????
        chars.append(0x16878)  #glyph00212	????
        chars.append(0x16879)  #glyph00213	????
        chars.append(0x1687A)  #glyph00214	????
        chars.append(0x1687B)  #glyph00215	????
        chars.append(0x1687C)  #glyph00216	????
        chars.append(0x1687D)  #glyph00217	????
        chars.append(0x1687E)  #glyph00218	????
        chars.append(0x1687F)  #glyph00219	????
        chars.append(0x16880)  #glyph00220	????
        chars.append(0x16881)  #glyph00221	????
        chars.append(0x16882)  #glyph00222	????
        chars.append(0x16883)  #glyph00223	????
        chars.append(0x16884)  #glyph00224	????
        chars.append(0x16885)  #glyph00225	????
        chars.append(0x16886)  #glyph00226	????
        chars.append(0x16887)  #glyph00227	????
        chars.append(0x16888)  #glyph00228	????
        chars.append(0x16889)  #glyph00229	????
        chars.append(0x1688A)  #glyph00230	????
        chars.append(0x1688B)  #glyph00231	????
        chars.append(0x1688C)  #glyph00232	????
        chars.append(0x1688D)  #glyph00233	????
        chars.append(0x1688E)  #glyph00234	????
        chars.append(0x1688F)  #glyph00235	????
        chars.append(0x16890)  #glyph00236	????
        chars.append(0x16891)  #glyph00237	????
        chars.append(0x16892)  #glyph00238	????
        chars.append(0x16893)  #glyph00239	????
        chars.append(0x16894)  #glyph00240	????
        chars.append(0x16895)  #glyph00241	????
        chars.append(0x16896)  #glyph00242	????
        chars.append(0x16897)  #glyph00243	????
        chars.append(0x16898)  #glyph00244	????
        chars.append(0x16899)  #glyph00245	????
        chars.append(0x1689A)  #glyph00246	????
        chars.append(0x1689B)  #glyph00247	????
        chars.append(0x1689C)  #glyph00248	????
        chars.append(0x1689D)  #glyph00249	????
        chars.append(0x1689E)  #glyph00250	????
        chars.append(0x1689F)  #glyph00251	????
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x168A1)  #glyph00253	????
        chars.append(0x168A2)  #glyph00254	????
        chars.append(0x168A3)  #glyph00255	????
        chars.append(0x168A4)  #glyph00256	????
        chars.append(0x168A5)  #glyph00257	????
        chars.append(0x168A6)  #glyph00258	????
        chars.append(0x168A7)  #glyph00259	????
        chars.append(0x168A8)  #glyph00260	????
        chars.append(0x168A9)  #glyph00261	????
        chars.append(0x168AA)  #glyph00262	????
        chars.append(0x168AB)  #glyph00263	????
        chars.append(0x168AC)  #glyph00264	????
        chars.append(0x168AD)  #glyph00265	????
        chars.append(0x168AE)  #glyph00266	????
        chars.append(0x168AF)  #glyph00267	????
        chars.append(0x168B0)  #glyph00268	????
        chars.append(0x168B1)  #glyph00269	????
        chars.append(0x168B2)  #glyph00270	????
        chars.append(0x168B3)  #glyph00271	????
        chars.append(0x168B4)  #glyph00272	????
        chars.append(0x168B5)  #glyph00273	????
        chars.append(0x168B6)  #glyph00274	????
        chars.append(0x168B7)  #glyph00275	????
        chars.append(0x168B8)  #glyph00276	????
        chars.append(0x168B9)  #glyph00277	????
        chars.append(0x168BA)  #glyph00278	????
        chars.append(0x168BB)  #glyph00279	????
        chars.append(0x168BC)  #glyph00280	????
        chars.append(0x168BD)  #glyph00281	????
        chars.append(0x168BE)  #glyph00282	????
        chars.append(0x168BF)  #glyph00283	????
        chars.append(0x168C0)  #glyph00284	????
        chars.append(0x16820)  #glyph00124	????
        chars.append(0x168C2)  #glyph00286	????
        chars.append(0x168C3)  #glyph00287	????
        chars.append(0x168C4)  #glyph00288	????
        chars.append(0x168C5)  #glyph00289	????
        chars.append(0x168C6)  #glyph00290	????
        chars.append(0x168C7)  #glyph00291	????
        chars.append(0x168C8)  #glyph00292	????
        chars.append(0x168C9)  #glyph00293	????
        chars.append(0x168CA)  #glyph00294	????
        chars.append(0x168CB)  #glyph00295	????
        chars.append(0x168CC)  #glyph00296	????
        chars.append(0x168CD)  #glyph00297	????
        chars.append(0x168CE)  #glyph00298	????
        chars.append(0x168CF)  #glyph00299	????
        chars.append(0x168D0)  #glyph00300	????
        chars.append(0x168D1)  #glyph00301	????
        chars.append(0x168D2)  #glyph00302	????
        chars.append(0x168D3)  #glyph00303	????
        chars.append(0x168D4)  #glyph00304	????
        chars.append(0x168D5)  #glyph00305	????
        chars.append(0x168D6)  #glyph00306	????
        chars.append(0x168D7)  #glyph00307	????
        chars.append(0x168D8)  #glyph00308	????
        chars.append(0x168D9)  #glyph00309	????
        chars.append(0x168DA)  #glyph00310	????
        chars.append(0x168DB)  #glyph00311	????
        chars.append(0x168DC)  #glyph00312	????
        chars.append(0x168DD)  #glyph00313	????
        chars.append(0x168DE)  #glyph00314	????
        chars.append(0x168DF)  #glyph00315	????
        chars.append(0x168E0)  #glyph00316	????
        chars.append(0x168E1)  #glyph00317	????
        chars.append(0x168E2)  #glyph00318	????
        chars.append(0x168E3)  #glyph00319	????
        chars.append(0x168E4)  #glyph00320	????
        chars.append(0x168E5)  #glyph00321	????
        chars.append(0x168E6)  #glyph00322	????
        chars.append(0x168E7)  #glyph00323	????
        chars.append(0x168E8)  #glyph00324	????
        chars.append(0x168E9)  #glyph00325	????
        chars.append(0x168EA)  #glyph00326	????
        chars.append(0x168EB)  #glyph00327	????
        chars.append(0x168EC)  #glyph00328	????
        chars.append(0x168ED)  #glyph00329	????
        chars.append(0x168EE)  #glyph00330	????
        chars.append(0x168EF)  #glyph00331	????
        chars.append(0x168F0)  #glyph00332	????
        chars.append(0x168F1)  #glyph00333	????
        chars.append(0x168F2)  #glyph00334	????
        chars.append(0x168F3)  #glyph00335	????
        chars.append(0x168F4)  #glyph00336	????
        chars.append(0x168F5)  #glyph00337	????
        chars.append(0x168F6)  #glyph00338	????
        chars.append(0x168F7)  #glyph00339	????
        chars.append(0x168F8)  #glyph00340	????
        chars.append(0x168F9)  #glyph00341	????
        chars.append(0x168FA)  #glyph00342	????
        chars.append(0x168FB)  #glyph00343	????
        chars.append(0x168FC)  #glyph00344	????
        chars.append(0x168FD)  #glyph00345	????
        chars.append(0x168FE)  #glyph00346	????
        chars.append(0x168FF)  #glyph00347	????
        chars.append(0x16900)  #glyph00348	????
        chars.append(0x16901)  #glyph00349	????
        chars.append(0x16902)  #glyph00350	????
        chars.append(0x1682B)  #glyph00135	????
        chars.append(0x16904)  #glyph00352	????
        chars.append(0x16905)  #glyph00353	????
        chars.append(0x16906)  #glyph00354	????
        chars.append(0x16907)  #glyph00355	????
        chars.append(0x16908)  #glyph00356	????
        chars.append(0x16909)  #glyph00357	????
        chars.append(0x1690A)  #glyph00358	????
        chars.append(0x1690B)  #glyph00359	????
        chars.append(0x1690C)  #glyph00360	????
        chars.append(0x1690D)  #glyph00361	????
        chars.append(0x1690E)  #glyph00362	????
        chars.append(0x1690F)  #glyph00363	????
        chars.append(0x16910)  #glyph00364	????
        chars.append(0x16911)  #glyph00365	????
        chars.append(0x16912)  #glyph00366	????
        chars.append(0x16913)  #glyph00367	????
        chars.append(0x16914)  #glyph00368	????
        chars.append(0x16915)  #glyph00369	????
        chars.append(0x16916)  #glyph00370	????
        chars.append(0x16917)  #glyph00371	????
        chars.append(0x16918)  #glyph00372	????
        chars.append(0x16919)  #glyph00373	????
        chars.append(0x1691A)  #glyph00374	????
        chars.append(0x1691B)  #glyph00375	????
        chars.append(0x1691C)  #glyph00376	????
        chars.append(0x1691D)  #glyph00377	????
        chars.append(0x1691E)  #glyph00378	????
        chars.append(0x1691F)  #glyph00379	????
        chars.append(0x16920)  #glyph00380	????
        chars.append(0x16921)  #glyph00381	????
        chars.append(0x16922)  #glyph00382	????
        chars.append(0x16923)  #glyph00383	????
        chars.append(0x16924)  #glyph00384	????
        chars.append(0x16925)  #glyph00385	????
        chars.append(0x16926)  #glyph00386	????
        chars.append(0x16927)  #glyph00387	????
        chars.append(0x16928)  #glyph00388	????
        chars.append(0x16929)  #glyph00389	????
        chars.append(0x1692A)  #glyph00390	????
        chars.append(0x1692B)  #glyph00391	????
        chars.append(0x1692C)  #glyph00392	????
        chars.append(0x1692D)  #glyph00393	????
        chars.append(0x1692E)  #glyph00394	????
        chars.append(0x1692F)  #glyph00395	????
        chars.append(0x16930)  #glyph00396	????
        chars.append(0x16931)  #glyph00397	????
        chars.append(0x16932)  #glyph00398	????
        chars.append(0x16933)  #glyph00399	????
        chars.append(0x16934)  #glyph00400	????
        chars.append(0x16935)  #glyph00401	????
        chars.append(0x16936)  #glyph00402	????
        chars.append(0x16937)  #glyph00403	????
        chars.append(0x16938)  #glyph00404	????
        chars.append(0x16939)  #glyph00405	????
        chars.append(0x1693A)  #glyph00406	????
        chars.append(0x1693B)  #glyph00407	????
        chars.append(0x1693C)  #glyph00408	????
        chars.append(0x1693D)  #glyph00409	????
        chars.append(0x1693E)  #glyph00410	????
        chars.append(0x1693F)  #glyph00411	????
        chars.append(0x16940)  #glyph00412	????
        chars.append(0x16941)  #glyph00413	????
        chars.append(0x16942)  #glyph00414	????
        chars.append(0x16943)  #glyph00415	????
        chars.append(0x16944)  #glyph00416	????
        chars.append(0x16945)  #glyph00417	????
        chars.append(0x16946)  #glyph00418	????
        chars.append(0x16947)  #glyph00419	????
        chars.append(0x16948)  #glyph00420	????
        chars.append(0x16949)  #glyph00421	????
        chars.append(0x1694A)  #glyph00422	????
        chars.append(0x1694B)  #glyph00423	????
        chars.append(0x1694C)  #glyph00424	????
        chars.append(0x1694D)  #glyph00425	????
        chars.append(0x1694E)  #glyph00426	????
        chars.append(0x1694F)  #glyph00427	????
        chars.append(0x16950)  #glyph00428	????
        chars.append(0x16951)  #glyph00429	????
        chars.append(0x16952)  #glyph00430	????
        chars.append(0x16953)  #glyph00431	????
        chars.append(0x16954)  #glyph00432	????
        chars.append(0x16955)  #glyph00433	????
        chars.append(0x16956)  #glyph00434	????
        chars.append(0x16957)  #glyph00435	????
        chars.append(0x16958)  #glyph00436	????
        chars.append(0x16959)  #glyph00437	????
        chars.append(0x1695A)  #glyph00438	????
        chars.append(0x1695B)  #glyph00439	????
        chars.append(0x1695C)  #glyph00440	????
        chars.append(0x1695D)  #glyph00441	????
        chars.append(0x1695E)  #glyph00442	????
        chars.append(0x1695F)  #glyph00443	????
        chars.append(0x16960)  #glyph00444	????
        chars.append(0x16961)  #glyph00445	????
        chars.append(0x16962)  #glyph00446	????
        chars.append(0x16963)  #glyph00447	????
        chars.append(0x16964)  #glyph00448	????
        chars.append(0x16965)  #glyph00449	????
        chars.append(0x16966)  #glyph00450	????
        chars.append(0x16967)  #glyph00451	????
        chars.append(0x16968)  #glyph00452	????
        chars.append(0x16969)  #glyph00453	????
        chars.append(0x1696A)  #glyph00454	????
        chars.append(0x1696B)  #glyph00455	????
        chars.append(0x1696C)  #glyph00456	????
        chars.append(0x1696D)  #glyph00457	????
        chars.append(0x1696E)  #glyph00458	????
        chars.append(0x1696F)  #glyph00459	????
        chars.append(0x16970)  #glyph00460	????
        chars.append(0x16971)  #glyph00461	????
        chars.append(0x16972)  #glyph00462	????
        chars.append(0x16973)  #glyph00463	????
        chars.append(0x16974)  #glyph00464	????
        chars.append(0x16975)  #glyph00465	????
        chars.append(0x16976)  #glyph00466	????
        chars.append(0x16977)  #glyph00467	????
        chars.append(0x16978)  #glyph00468	????
        chars.append(0x16979)  #glyph00469	????
        chars.append(0x1697A)  #glyph00470	????
        chars.append(0x1697B)  #glyph00471	????
        chars.append(0x1697C)  #glyph00472	????
        chars.append(0x1697D)  #glyph00473	????
        chars.append(0x1697E)  #glyph00474	????
        chars.append(0x1697F)  #glyph00475	????
        chars.append(0x16980)  #glyph00476	????
        chars.append(0x16981)  #glyph00477	????
        chars.append(0x16982)  #glyph00478	????
        chars.append(0x16983)  #glyph00479	????
        chars.append(0x16984)  #glyph00480	????
        chars.append(0x16985)  #glyph00481	????
        chars.append(0x16986)  #glyph00482	????
        chars.append(0x16987)  #glyph00483	????
        chars.append(0x16988)  #glyph00484	????
        chars.append(0x16989)  #glyph00485	????
        chars.append(0x1698A)  #glyph00486	????
        chars.append(0x1698B)  #glyph00487	????
        chars.append(0x1698C)  #glyph00488	????
        chars.append(0x1698D)  #glyph00489	????
        chars.append(0x1698E)  #glyph00490	????
        chars.append(0x1698F)  #glyph00491	????
        chars.append(0x16990)  #glyph00492	????
        chars.append(0x16991)  #glyph00493	????
        chars.append(0x16992)  #glyph00494	????
        chars.append(0x16993)  #glyph00495	????
        chars.append(0x16994)  #glyph00496	????
        chars.append(0x16995)  #glyph00497	????
        chars.append(0x16996)  #glyph00498	????
        chars.append(0x16997)  #glyph00499	????
        chars.append(0x16998)  #glyph00500	????
        chars.append(0x16999)  #glyph00501	????
        chars.append(0x1699A)  #glyph00502	????
        chars.append(0x1699B)  #glyph00503	????
        chars.append(0x1699C)  #glyph00504	????
        chars.append(0x1699D)  #glyph00505	????
        chars.append(0x1699E)  #glyph00506	????
        chars.append(0x1699F)  #glyph00507	????
        chars.append(0x169A0)  #glyph00508	????
        chars.append(0x169A1)  #glyph00509	????
        chars.append(0x169A2)  #glyph00510	????
        chars.append(0x169A3)  #glyph00511	????
        chars.append(0x169A4)  #glyph00512	????
        chars.append(0x169A5)  #glyph00513	????
        chars.append(0x169A6)  #glyph00514	????
        chars.append(0x169A7)  #glyph00515	????
        chars.append(0x169A8)  #glyph00516	????
        chars.append(0x169A9)  #glyph00517	????
        chars.append(0x169AA)  #glyph00518	????
        chars.append(0x169AB)  #glyph00519	????
        chars.append(0x169AC)  #glyph00520	????
        chars.append(0x169AD)  #glyph00521	????
        chars.append(0x169AE)  #glyph00522	????
        chars.append(0x169AF)  #glyph00523	????
        chars.append(0x169B0)  #glyph00524	????
        chars.append(0x169B1)  #glyph00525	????
        chars.append(0x169B2)  #glyph00526	????
        chars.append(0x169B3)  #glyph00527	????
        chars.append(0x169B4)  #glyph00528	????
        chars.append(0x169B5)  #glyph00529	????
        chars.append(0x169B6)  #glyph00530	????
        chars.append(0x169B7)  #glyph00531	????
        chars.append(0x169B8)  #glyph00532	????
        chars.append(0x169B9)  #glyph00533	????
        chars.append(0x169BA)  #glyph00534	????
        chars.append(0x169BB)  #glyph00535	????
        chars.append(0x169BC)  #glyph00536	????
        chars.append(0x169BD)  #glyph00537	????
        chars.append(0x169BE)  #glyph00538	????
        chars.append(0x169BF)  #glyph00539	????
        chars.append(0x169C0)  #glyph00540	????
        chars.append(0x169C1)  #glyph00541	????
        chars.append(0x169C2)  #glyph00542	????
        chars.append(0x169C3)  #glyph00543	????
        chars.append(0x169C4)  #glyph00544	????
        chars.append(0x169C5)  #glyph00545	????
        chars.append(0x169C6)  #glyph00546	????
        chars.append(0x169C7)  #glyph00547	????
        chars.append(0x169C8)  #glyph00548	????
        chars.append(0x169C9)  #glyph00549	????
        chars.append(0x169CA)  #glyph00550	????
        chars.append(0x169CB)  #glyph00551	????
        chars.append(0x169CC)  #glyph00552	????
        chars.append(0x169CD)  #glyph00553	????
        chars.append(0x169CE)  #glyph00554	????
        chars.append(0x169CF)  #glyph00555	????
        chars.append(0x169D0)  #glyph00556	????
        chars.append(0x169D1)  #glyph00557	????
        chars.append(0x169D2)  #glyph00558	????
        chars.append(0x169D3)  #glyph00559	????
        chars.append(0x169D4)  #glyph00560	????
        chars.append(0x169D5)  #glyph00561	????
        chars.append(0x169D6)  #glyph00562	????
        chars.append(0x169D7)  #glyph00563	????
        chars.append(0x169D8)  #glyph00564	????
        chars.append(0x169D9)  #glyph00565	????
        chars.append(0x169DA)  #glyph00566	????
        chars.append(0x1684F)  #glyph00171	????
        chars.append(0x169DC)  #glyph00568	????
        chars.append(0x169DD)  #glyph00569	????
        chars.append(0x169DE)  #glyph00570	????
        chars.append(0x169DF)  #glyph00571	????
        chars.append(0x169E0)  #glyph00572	????
        chars.append(0x169E1)  #glyph00573	????
        chars.append(0x169E2)  #glyph00574	????
        chars.append(0x169E3)  #glyph00575	????
        chars.append(0x169E4)  #glyph00576	????
        chars.append(0x169E5)  #glyph00577	????
        chars.append(0x169E6)  #glyph00578	????
        chars.append(0x169E7)  #glyph00579	????
        chars.append(0x169E8)  #glyph00580	????
        chars.append(0x169E9)  #glyph00581	????
        chars.append(0x169EA)  #glyph00582	????
        chars.append(0x169EB)  #glyph00583	????
        chars.append(0x169EC)  #glyph00584	????
        chars.append(0x169ED)  #glyph00585	????
        chars.append(0x169EE)  #glyph00586	????
        chars.append(0x169EF)  #glyph00587	????
        chars.append(0x169F0)  #glyph00588	????
        chars.append(0x169F1)  #glyph00589	????
        chars.append(0x169F2)  #glyph00590	????
        chars.append(0x169F3)  #glyph00591	????
        chars.append(0x169F4)  #glyph00592	????
        chars.append(0x169F5)  #glyph00593	????
        chars.append(0x169F6)  #glyph00594	????
        chars.append(0x169F7)  #glyph00595	????
        chars.append(0x169F8)  #glyph00596	????
        chars.append(0x169F9)  #glyph00597	????
        chars.append(0x169FA)  #glyph00598	????
        chars.append(0x169FB)  #glyph00599	????
        chars.append(0x169FC)  #glyph00600	????
        chars.append(0x169FD)  #glyph00601	????
        chars.append(0x169FE)  #glyph00602	????
        chars.append(0x169FF)  #glyph00603	????
        chars.append(0x16A00)  #glyph00604	????
        chars.append(0x16A01)  #glyph00605	????
        chars.append(0x16A02)  #glyph00606	????
        chars.append(0x16A03)  #glyph00607	????
        chars.append(0x16A04)  #glyph00608	????
        chars.append(0x16A05)  #glyph00609	????
        chars.append(0x16A06)  #glyph00610	????
        chars.append(0x16A07)  #glyph00611	????
        chars.append(0x16A08)  #glyph00612	????
        chars.append(0x16A09)  #glyph00613	????
        chars.append(0x16A0A)  #glyph00614	????
        chars.append(0x16A0B)  #glyph00615	????
        chars.append(0x16A0C)  #glyph00616	????
        chars.append(0x16A0D)  #glyph00617	????
        chars.append(0x16A0E)  #glyph00618	????
        chars.append(0x16A0F)  #glyph00619	????
        chars.append(0x16A10)  #glyph00620	????
        chars.append(0x16A11)  #glyph00621	????
        chars.append(0x16A12)  #glyph00622	????
        chars.append(0x16A13)  #glyph00623	????
        chars.append(0x16A14)  #glyph00624	????
        chars.append(0x16A15)  #glyph00625	????
        chars.append(0x16A16)  #glyph00626	????
        chars.append(0x16A17)  #glyph00627	????
        chars.append(0x16A18)  #glyph00628	????
        chars.append(0x16A19)  #glyph00629	????
        chars.append(0x16A1A)  #glyph00630	????
        chars.append(0x16A1B)  #glyph00631	????
        chars.append(0x16A1C)  #glyph00632	????
        chars.append(0x16A1D)  #glyph00633	????
        chars.append(0x16A1E)  #glyph00634	????
        chars.append(0x16A1F)  #glyph00635	????
        chars.append(0x16A20)  #glyph00636	????
        chars.append(0x16A21)  #glyph00637	????
        chars.append(0x16A22)  #glyph00638	????
        chars.append(0x16A23)  #glyph00639	????
        chars.append(0x16A24)  #glyph00640	????
        chars.append(0x16A25)  #glyph00641	????
        chars.append(0x16A26)  #glyph00642	????
        chars.append(0x16A27)  #glyph00643	????
        chars.append(0x16A28)  #glyph00644	????
        chars.append(0x16A29)  #glyph00645	????
        chars.append(0x16A2A)  #glyph00646	????
        chars.append(0x16A2B)  #glyph00647	????
        chars.append(0x16A2C)  #glyph00648	????
        chars.append(0x16A2D)  #glyph00649	????
        chars.append(0x16A2E)  #glyph00650	????
        chars.append(0x16A2F)  #glyph00651	????
        chars.append(0x16A30)  #glyph00652	????
        chars.append(0x16A31)  #glyph00653	????
        chars.append(0x16A32)  #glyph00654	????
        chars.append(0x16A33)  #glyph00655	????
        chars.append(0x16A34)  #glyph00656	????
        chars.append(0x16A35)  #glyph00657	????
        chars.append(0x16A36)  #glyph00658	????
        chars.append(0x16A37)  #glyph00659	????
        chars.append(0x16A38)  #glyph00660	????
        chars.append(0x169DB)  #glyph00567	????
        chars.append(0x168A0)  #glyph00252	????
        chars.append(0x168C1)  #glyph00285	????
        chars.append(0x16903)  #glyph00351	????
        chars.append(0xA6A0)  #uniA6A0	BAMUM LETTER A
        chars.append(0xA6A1)  #uniA6A1	BAMUM LETTER KA
        chars.append(0xA6A2)  #uniA6A2	BAMUM LETTER U
        chars.append(0xA6A3)  #uniA6A3	BAMUM LETTER KU
        chars.append(0xA6A4)  #uniA6A4	BAMUM LETTER EE
        chars.append(0xA6A5)  #uniA6A5	BAMUM LETTER REE
        chars.append(0xA6A6)  #uniA6A6	BAMUM LETTER TAE
        chars.append(0xA6A7)  #uniA6A7	BAMUM LETTER O
        chars.append(0xA6A8)  #uniA6A8	BAMUM LETTER NYI
        chars.append(0xA6A9)  #uniA6A9	BAMUM LETTER I
        chars.append(0xA6AA)  #uniA6AA	BAMUM LETTER LA
        chars.append(0xA6AB)  #uniA6AB	BAMUM LETTER PA
        chars.append(0xA6AC)  #uniA6AC	BAMUM LETTER RII
        chars.append(0xA6AD)  #uniA6AD	BAMUM LETTER RIEE
        chars.append(0xA6AE)  #uniA6AE	BAMUM LETTER LEEEE
        chars.append(0xA6AF)  #uniA6AF	BAMUM LETTER MEEEE
        chars.append(0xA6B0)  #uniA6B0	BAMUM LETTER TAA
        chars.append(0xA6B1)  #uniA6B1	BAMUM LETTER NDAA
        chars.append(0xA6B2)  #uniA6B2	BAMUM LETTER NJAEM
        chars.append(0xA6B3)  #uniA6B3	BAMUM LETTER M
        chars.append(0xA6B4)  #uniA6B4	BAMUM LETTER SUU
        chars.append(0xA6B5)  #uniA6B5	BAMUM LETTER MU
        chars.append(0xA6B6)  #uniA6B6	BAMUM LETTER SHII
        chars.append(0xA6B7)  #uniA6B7	BAMUM LETTER SI
        chars.append(0xA6B8)  #uniA6B8	BAMUM LETTER SHEUX
        chars.append(0xA6B9)  #uniA6B9	BAMUM LETTER SEUX
        chars.append(0xA6BA)  #uniA6BA	BAMUM LETTER KYEE
        chars.append(0xA6BB)  #uniA6BB	BAMUM LETTER KET
        chars.append(0xA6BC)  #uniA6BC	BAMUM LETTER NUAE
        chars.append(0xA6BD)  #uniA6BD	BAMUM LETTER NU
        chars.append(0xA6BE)  #uniA6BE	BAMUM LETTER NJUAE
        chars.append(0xA6BF)  #uniA6BF	BAMUM LETTER YOQ
        chars.append(0xA6C0)  #uniA6C0	BAMUM LETTER SHU
        chars.append(0xA6C1)  #uniA6C1	BAMUM LETTER YUQ
        chars.append(0xA6C2)  #uniA6C2	BAMUM LETTER YA
        chars.append(0xA6C3)  #uniA6C3	BAMUM LETTER NSHA
        chars.append(0xA6C4)  #uniA6C4	BAMUM LETTER KEUX
        chars.append(0xA6C5)  #uniA6C5	BAMUM LETTER PEUX
        chars.append(0xA6C6)  #uniA6C6	BAMUM LETTER NJEE
        chars.append(0xA6C7)  #uniA6C7	BAMUM LETTER NTEE
        chars.append(0xA6C8)  #uniA6C8	BAMUM LETTER PUE
        chars.append(0xA6C9)  #uniA6C9	BAMUM LETTER WUE
        chars.append(0xA6CA)  #uniA6CA	BAMUM LETTER PEE
        chars.append(0xA6CB)  #uniA6CB	BAMUM LETTER FEE
        chars.append(0xA6CC)  #uniA6CC	BAMUM LETTER RU
        chars.append(0xA6CD)  #uniA6CD	BAMUM LETTER LU
        chars.append(0xA6CE)  #uniA6CE	BAMUM LETTER MI
        chars.append(0xA6CF)  #uniA6CF	BAMUM LETTER NI
        chars.append(0xA6D0)  #uniA6D0	BAMUM LETTER REUX
        chars.append(0xA6D1)  #uniA6D1	BAMUM LETTER RAE
        chars.append(0xA6D2)  #uniA6D2	BAMUM LETTER KEN
        chars.append(0xA6D3)  #uniA6D3	BAMUM LETTER NGKWAEN
        chars.append(0xA6D4)  #uniA6D4	BAMUM LETTER NGGA
        chars.append(0xA6D5)  #uniA6D5	BAMUM LETTER NGA
        chars.append(0xA6D6)  #uniA6D6	BAMUM LETTER SHO
        chars.append(0xA6D7)  #uniA6D7	BAMUM LETTER PUAE
        chars.append(0xA6D8)  #uniA6D8	BAMUM LETTER FU
        chars.append(0xA6D9)  #uniA6D9	BAMUM LETTER FOM
        chars.append(0xA6DA)  #uniA6DA	BAMUM LETTER WA
        chars.append(0xA6DB)  #uniA6DB	BAMUM LETTER NA
        chars.append(0xA6DC)  #uniA6DC	BAMUM LETTER LI
        chars.append(0xA6DD)  #uniA6DD	BAMUM LETTER PI
        chars.append(0xA6DE)  #uniA6DE	BAMUM LETTER LOQ
        chars.append(0xA6DF)  #uniA6DF	BAMUM LETTER KO
        chars.append(0xA6E0)  #uniA6E0	BAMUM LETTER MBEN
        chars.append(0xA6E1)  #uniA6E1	BAMUM LETTER REN
        chars.append(0xA6E2)  #uniA6E2	BAMUM LETTER MEN
        chars.append(0xA6E3)  #uniA6E3	BAMUM LETTER MA
        chars.append(0xA6E4)  #uniA6E4	BAMUM LETTER TI
        chars.append(0xA6E5)  #uniA6E5	BAMUM LETTER KI
        chars.append(0xA6E6)  #uniA6E6	BAMUM LETTER MO
        chars.append(0xA6E7)  #uniA6E7	BAMUM LETTER MBAA
        chars.append(0xA6E8)  #uniA6E8	BAMUM LETTER TET
        chars.append(0xA6E9)  #uniA6E9	BAMUM LETTER KPA
        chars.append(0xA6EA)  #uniA6EA	BAMUM LETTER TEN
        chars.append(0xA6EB)  #uniA6EB	BAMUM LETTER NTUU
        chars.append(0xA6EC)  #uniA6EC	BAMUM LETTER SAMBA
        chars.append(0xA6ED)  #uniA6ED	BAMUM LETTER FAAMAE
        chars.append(0xA6EE)  #uniA6EE	BAMUM LETTER KOVUU
        chars.append(0xA6EF)  #uniA6EF	BAMUM LETTER KOGHOM
        chars.append(0xA6F0)  #uniA6F0	BAMUM COMBINING MARK KOQNDON
        chars.append(0xA6F1)  #uniA6F1	BAMUM COMBINING MARK TUKWENTIS
        chars.append(0xA6F2)  #uniA6F2	BAMUM NJAEMLI
        chars.append(0xA6F3)  #uniA6F3	BAMUM FULL STOP
        chars.append(0xA6F4)  #uniA6F4	BAMUM COLON
        chars.append(0xA6F5)  #uniA6F5	BAMUM COMMA
        chars.append(0xA6F6)  #uniA6F6	BAMUM SEMICOLON
        chars.append(0xA6F7)  #uniA6F7	BAMUM QUESTION MARK
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


