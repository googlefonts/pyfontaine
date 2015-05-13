# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansCanadianAboriginal-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x18B0)  #uni18B0	CANADIAN SYLLABICS OY
        chars.append(0x18B1)  #uni18B1	CANADIAN SYLLABICS AY
        chars.append(0x18B2)  #uni18B2	CANADIAN SYLLABICS AAY
        chars.append(0x18B3)  #uni18B3	CANADIAN SYLLABICS WAY
        chars.append(0x18B4)  #uni18B4	CANADIAN SYLLABICS POY
        chars.append(0x18B5)  #uni18B5	CANADIAN SYLLABICS PAY
        chars.append(0x18B6)  #uni18B6	CANADIAN SYLLABICS PWOY
        chars.append(0x18B7)  #uni18B7	CANADIAN SYLLABICS TAY
        chars.append(0x18B8)  #uni18B8	CANADIAN SYLLABICS KAY
        chars.append(0x18B9)  #uni18B9	CANADIAN SYLLABICS KWAY
        chars.append(0x18BA)  #uni18BA	CANADIAN SYLLABICS MAY
        chars.append(0x18BB)  #uni18BB	CANADIAN SYLLABICS NOY
        chars.append(0x18BC)  #uni18BC	CANADIAN SYLLABICS NAY
        chars.append(0x18BD)  #uni18BD	CANADIAN SYLLABICS LAY
        chars.append(0x18BE)  #uni18BE	CANADIAN SYLLABICS SOY
        chars.append(0x18BF)  #uni18BF	CANADIAN SYLLABICS SAY
        chars.append(0x18C0)  #uni18C0	CANADIAN SYLLABICS SHOY
        chars.append(0x18C1)  #uni18C1	CANADIAN SYLLABICS SHAY
        chars.append(0x18C2)  #uni18C2	CANADIAN SYLLABICS SHWOY
        chars.append(0x18C3)  #uni18C3	CANADIAN SYLLABICS YOY
        chars.append(0x18C4)  #uni18C4	CANADIAN SYLLABICS YAY
        chars.append(0x18C5)  #uni18C5	CANADIAN SYLLABICS RAY
        chars.append(0x18C6)  #uni18C6	CANADIAN SYLLABICS NWI
        chars.append(0x18C7)  #uni18C7	CANADIAN SYLLABICS OJIBWAY NWI
        chars.append(0x18C8)  #uni18C8	CANADIAN SYLLABICS NWII
        chars.append(0x18C9)  #uni18C9	CANADIAN SYLLABICS OJIBWAY NWII
        chars.append(0x18CA)  #uni18CA	CANADIAN SYLLABICS NWO
        chars.append(0x18CB)  #uni18CB	CANADIAN SYLLABICS OJIBWAY NWO
        chars.append(0x18CC)  #uni18CC	CANADIAN SYLLABICS NWOO
        chars.append(0x18CD)  #uni18CD	CANADIAN SYLLABICS OJIBWAY NWOO
        chars.append(0x18CE)  #uni18CE	CANADIAN SYLLABICS RWEE
        chars.append(0x18CF)  #uni18CF	CANADIAN SYLLABICS RWI
        chars.append(0x18D0)  #uni18D0	CANADIAN SYLLABICS RWII
        chars.append(0x18D1)  #uni18D1	CANADIAN SYLLABICS RWO
        chars.append(0x18D2)  #uni18D2	CANADIAN SYLLABICS RWOO
        chars.append(0x18D3)  #uni18D3	CANADIAN SYLLABICS RWA
        chars.append(0x18D4)  #uni18D4	CANADIAN SYLLABICS OJIBWAY P
        chars.append(0x18D5)  #uni18D5	CANADIAN SYLLABICS OJIBWAY T
        chars.append(0x18D6)  #uni18D6	CANADIAN SYLLABICS OJIBWAY K
        chars.append(0x18D7)  #uni18D7	CANADIAN SYLLABICS OJIBWAY C
        chars.append(0x18D8)  #uni18D8	CANADIAN SYLLABICS OJIBWAY M
        chars.append(0x18D9)  #uni18D9	CANADIAN SYLLABICS OJIBWAY N
        chars.append(0x18DA)  #uni18DA	CANADIAN SYLLABICS OJIBWAY S
        chars.append(0x18DB)  #uni18DB	CANADIAN SYLLABICS OJIBWAY SH
        chars.append(0x18DC)  #uni18DC	CANADIAN SYLLABICS EASTERN W
        chars.append(0x18DD)  #uni18DD	CANADIAN SYLLABICS WESTERN W
        chars.append(0x18DE)  #uni18DE	CANADIAN SYLLABICS FINAL SMALL RING
        chars.append(0x18DF)  #uni18DF	CANADIAN SYLLABICS FINAL RAISED DOT
        chars.append(0x18E0)  #uni18E0	CANADIAN SYLLABICS R-CREE RWE
        chars.append(0x18E1)  #uni18E1	CANADIAN SYLLABICS WEST-CREE LOO
        chars.append(0x18E2)  #uni18E2	CANADIAN SYLLABICS WEST-CREE LAA
        chars.append(0x18E3)  #uni18E3	CANADIAN SYLLABICS THWE
        chars.append(0x18E4)  #uni18E4	CANADIAN SYLLABICS THWA
        chars.append(0x18E5)  #uni18E5	CANADIAN SYLLABICS TTHWE
        chars.append(0x18E6)  #uni18E6	CANADIAN SYLLABICS TTHOO
        chars.append(0x18E7)  #uni18E7	CANADIAN SYLLABICS TTHAA
        chars.append(0x18E8)  #uni18E8	CANADIAN SYLLABICS TLHWE
        chars.append(0x18E9)  #uni18E9	CANADIAN SYLLABICS TLHOO
        chars.append(0x18EA)  #uni18EA	CANADIAN SYLLABICS SAYISI SHWE
        chars.append(0x18EB)  #uni18EB	CANADIAN SYLLABICS SAYISI SHOO
        chars.append(0x18EC)  #uni18EC	CANADIAN SYLLABICS SAYISI HOO
        chars.append(0x18ED)  #uni18ED	CANADIAN SYLLABICS CARRIER GWU
        chars.append(0x18EE)  #uni18EE	CANADIAN SYLLABICS CARRIER DENE GEE
        chars.append(0x18EF)  #uni18EF	CANADIAN SYLLABICS CARRIER GAA
        chars.append(0x18F0)  #uni18F0	CANADIAN SYLLABICS CARRIER GWA
        chars.append(0x18F1)  #uni18F1	CANADIAN SYLLABICS SAYISI JUU
        chars.append(0x18F2)  #uni18F2	CANADIAN SYLLABICS CARRIER JWA
        chars.append(0x18F3)  #uni18F3	CANADIAN SYLLABICS BEAVER DENE L
        chars.append(0x18F4)  #uni18F4	CANADIAN SYLLABICS BEAVER DENE R
        chars.append(0x18F5)  #uni18F5	CANADIAN SYLLABICS CARRIER DENTAL S
        chars.append(0x0131)  #dotlessi	LATIN SMALL LETTER DOTLESS I
        chars.append(0x02C7)  #caron	CARON
        chars.append(0x02D8)  #breve	BREVE
        chars.append(0x02D9)  #dotaccent	DOT ABOVE
        chars.append(0x02DA)  #ring	RING ABOVE
        chars.append(0x02DB)  #ogonek	OGONEK
        chars.append(0x0307)  #uni0307	COMBINING DOT ABOVE
        chars.append(0x1400)  #uni1400	CANADIAN SYLLABICS HYPHEN
        chars.append(0x1401)  #uni1401	CANADIAN SYLLABICS E
        chars.append(0x1402)  #uni1402	CANADIAN SYLLABICS AAI
        chars.append(0x1403)  #uni1403	CANADIAN SYLLABICS I
        chars.append(0x1404)  #uni1404	CANADIAN SYLLABICS II
        chars.append(0x1405)  #uni1405	CANADIAN SYLLABICS O
        chars.append(0x1406)  #uni1406	CANADIAN SYLLABICS OO
        chars.append(0x1407)  #uni1407	CANADIAN SYLLABICS Y-CREE OO
        chars.append(0x1408)  #uni1408	CANADIAN SYLLABICS CARRIER EE
        chars.append(0x1409)  #uni1409	CANADIAN SYLLABICS CARRIER I
        chars.append(0x140A)  #uni140A	CANADIAN SYLLABICS A
        chars.append(0x140B)  #uni140B	CANADIAN SYLLABICS AA
        chars.append(0x140C)  #uni140C	CANADIAN SYLLABICS WE
        chars.append(0x140D)  #uni140D	CANADIAN SYLLABICS WEST-CREE WE
        chars.append(0x140E)  #uni140E	CANADIAN SYLLABICS WI
        chars.append(0x140F)  #uni140F	CANADIAN SYLLABICS WEST-CREE WI
        chars.append(0x1410)  #uni1410	CANADIAN SYLLABICS WII
        chars.append(0x1411)  #uni1411	CANADIAN SYLLABICS WEST-CREE WII
        chars.append(0x1412)  #uni1412	CANADIAN SYLLABICS WO
        chars.append(0x1413)  #uni1413	CANADIAN SYLLABICS WEST-CREE WO
        chars.append(0x1414)  #uni1414	CANADIAN SYLLABICS WOO
        chars.append(0x1415)  #uni1415	CANADIAN SYLLABICS WEST-CREE WOO
        chars.append(0x1416)  #uni1416	CANADIAN SYLLABICS NASKAPI WOO
        chars.append(0x1417)  #uni1417	CANADIAN SYLLABICS WA
        chars.append(0x1418)  #uni1418	CANADIAN SYLLABICS WEST-CREE WA
        chars.append(0x1419)  #uni1419	CANADIAN SYLLABICS WAA
        chars.append(0x141A)  #uni141A	CANADIAN SYLLABICS WEST-CREE WAA
        chars.append(0x141B)  #uni141B	CANADIAN SYLLABICS NASKAPI WAA
        chars.append(0x141C)  #uni141C	CANADIAN SYLLABICS AI
        chars.append(0x141D)  #uni141D	CANADIAN SYLLABICS Y-CREE W
        chars.append(0x141E)  #uni141E	CANADIAN SYLLABICS GLOTTAL STOP
        chars.append(0x141F)  #uni141F	CANADIAN SYLLABICS FINAL ACUTE
        chars.append(0x1420)  #uni1420	CANADIAN SYLLABICS FINAL GRAVE
        chars.append(0x1421)  #uni1421	CANADIAN SYLLABICS FINAL BOTTOM HALF RING
        chars.append(0x1422)  #uni1422	CANADIAN SYLLABICS FINAL TOP HALF RING
        chars.append(0x1423)  #uni1423	CANADIAN SYLLABICS FINAL RIGHT HALF RING
        chars.append(0x1424)  #uni1424	CANADIAN SYLLABICS FINAL RING
        chars.append(0x1425)  #uni1425	CANADIAN SYLLABICS FINAL DOUBLE ACUTE
        chars.append(0x1426)  #uni1426	CANADIAN SYLLABICS FINAL DOUBLE SHORT VERTICAL STROKES
        chars.append(0x1427)  #uni1427	CANADIAN SYLLABICS FINAL MIDDLE DOT
        chars.append(0x1428)  #uni1428	CANADIAN SYLLABICS FINAL SHORT HORIZONTAL STROKE
        chars.append(0x1429)  #uni1429	CANADIAN SYLLABICS FINAL PLUS
        chars.append(0x142A)  #uni142A	CANADIAN SYLLABICS FINAL DOWN TACK
        chars.append(0x142B)  #uni142B	CANADIAN SYLLABICS EN
        chars.append(0x142C)  #uni142C	CANADIAN SYLLABICS IN
        chars.append(0x142D)  #uni142D	CANADIAN SYLLABICS ON
        chars.append(0x142E)  #uni142E	CANADIAN SYLLABICS AN
        chars.append(0x142F)  #uni142F	CANADIAN SYLLABICS PE
        chars.append(0x1430)  #uni1430	CANADIAN SYLLABICS PAAI
        chars.append(0x1431)  #uni1431	CANADIAN SYLLABICS PI
        chars.append(0x1432)  #uni1432	CANADIAN SYLLABICS PII
        chars.append(0x1433)  #uni1433	CANADIAN SYLLABICS PO
        chars.append(0x1434)  #uni1434	CANADIAN SYLLABICS POO
        chars.append(0x1435)  #uni1435	CANADIAN SYLLABICS Y-CREE POO
        chars.append(0x1436)  #uni1436	CANADIAN SYLLABICS CARRIER HEE
        chars.append(0x1437)  #uni1437	CANADIAN SYLLABICS CARRIER HI
        chars.append(0x1438)  #uni1438	CANADIAN SYLLABICS PA
        chars.append(0x1439)  #uni1439	CANADIAN SYLLABICS PAA
        chars.append(0x143A)  #uni143A	CANADIAN SYLLABICS PWE
        chars.append(0x143B)  #uni143B	CANADIAN SYLLABICS WEST-CREE PWE
        chars.append(0x143C)  #uni143C	CANADIAN SYLLABICS PWI
        chars.append(0x143D)  #uni143D	CANADIAN SYLLABICS WEST-CREE PWI
        chars.append(0x143E)  #uni143E	CANADIAN SYLLABICS PWII
        chars.append(0x143F)  #uni143F	CANADIAN SYLLABICS WEST-CREE PWII
        chars.append(0x1440)  #uni1440	CANADIAN SYLLABICS PWO
        chars.append(0x1441)  #uni1441	CANADIAN SYLLABICS WEST-CREE PWO
        chars.append(0x1442)  #uni1442	CANADIAN SYLLABICS PWOO
        chars.append(0x1443)  #uni1443	CANADIAN SYLLABICS WEST-CREE PWOO
        chars.append(0x1444)  #uni1444	CANADIAN SYLLABICS PWA
        chars.append(0x1445)  #uni1445	CANADIAN SYLLABICS WEST-CREE PWA
        chars.append(0x1446)  #uni1446	CANADIAN SYLLABICS PWAA
        chars.append(0x1447)  #uni1447	CANADIAN SYLLABICS WEST-CREE PWAA
        chars.append(0x1448)  #uni1448	CANADIAN SYLLABICS Y-CREE PWAA
        chars.append(0x1449)  #uni1449	CANADIAN SYLLABICS P
        chars.append(0x144A)  #uni144A	CANADIAN SYLLABICS WEST-CREE P
        chars.append(0x144B)  #uni144B	CANADIAN SYLLABICS CARRIER H
        chars.append(0x144C)  #uni144C	CANADIAN SYLLABICS TE
        chars.append(0x144D)  #uni144D	CANADIAN SYLLABICS TAAI
        chars.append(0x144E)  #uni144E	CANADIAN SYLLABICS TI
        chars.append(0x144F)  #uni144F	CANADIAN SYLLABICS TII
        chars.append(0x1450)  #uni1450	CANADIAN SYLLABICS TO
        chars.append(0x1451)  #uni1451	CANADIAN SYLLABICS TOO
        chars.append(0x1452)  #uni1452	CANADIAN SYLLABICS Y-CREE TOO
        chars.append(0x1453)  #uni1453	CANADIAN SYLLABICS CARRIER DEE
        chars.append(0x1454)  #uni1454	CANADIAN SYLLABICS CARRIER DI
        chars.append(0x1455)  #uni1455	CANADIAN SYLLABICS TA
        chars.append(0x1456)  #uni1456	CANADIAN SYLLABICS TAA
        chars.append(0x1457)  #uni1457	CANADIAN SYLLABICS TWE
        chars.append(0x1458)  #uni1458	CANADIAN SYLLABICS WEST-CREE TWE
        chars.append(0x1459)  #uni1459	CANADIAN SYLLABICS TWI
        chars.append(0x145A)  #uni145A	CANADIAN SYLLABICS WEST-CREE TWI
        chars.append(0x145B)  #uni145B	CANADIAN SYLLABICS TWII
        chars.append(0x145C)  #uni145C	CANADIAN SYLLABICS WEST-CREE TWII
        chars.append(0x145D)  #uni145D	CANADIAN SYLLABICS TWO
        chars.append(0x145E)  #uni145E	CANADIAN SYLLABICS WEST-CREE TWO
        chars.append(0x145F)  #uni145F	CANADIAN SYLLABICS TWOO
        chars.append(0x1460)  #uni1460	CANADIAN SYLLABICS WEST-CREE TWOO
        chars.append(0x1461)  #uni1461	CANADIAN SYLLABICS TWA
        chars.append(0x1462)  #uni1462	CANADIAN SYLLABICS WEST-CREE TWA
        chars.append(0x1463)  #uni1463	CANADIAN SYLLABICS TWAA
        chars.append(0x1464)  #uni1464	CANADIAN SYLLABICS WEST-CREE TWAA
        chars.append(0x1465)  #uni1465	CANADIAN SYLLABICS NASKAPI TWAA
        chars.append(0x1466)  #uni1466	CANADIAN SYLLABICS T
        chars.append(0x1467)  #uni1467	CANADIAN SYLLABICS TTE
        chars.append(0x1468)  #uni1468	CANADIAN SYLLABICS TTI
        chars.append(0x1469)  #uni1469	CANADIAN SYLLABICS TTO
        chars.append(0x146A)  #uni146A	CANADIAN SYLLABICS TTA
        chars.append(0x146B)  #uni146B	CANADIAN SYLLABICS KE
        chars.append(0x146C)  #uni146C	CANADIAN SYLLABICS KAAI
        chars.append(0x146D)  #uni146D	CANADIAN SYLLABICS KI
        chars.append(0x146E)  #uni146E	CANADIAN SYLLABICS KII
        chars.append(0x146F)  #uni146F	CANADIAN SYLLABICS KO
        chars.append(0x1470)  #uni1470	CANADIAN SYLLABICS KOO
        chars.append(0x1471)  #uni1471	CANADIAN SYLLABICS Y-CREE KOO
        chars.append(0x1472)  #uni1472	CANADIAN SYLLABICS KA
        chars.append(0x1473)  #uni1473	CANADIAN SYLLABICS KAA
        chars.append(0x1474)  #uni1474	CANADIAN SYLLABICS KWE
        chars.append(0x1475)  #uni1475	CANADIAN SYLLABICS WEST-CREE KWE
        chars.append(0x1476)  #uni1476	CANADIAN SYLLABICS KWI
        chars.append(0x1477)  #uni1477	CANADIAN SYLLABICS WEST-CREE KWI
        chars.append(0x1478)  #uni1478	CANADIAN SYLLABICS KWII
        chars.append(0x1479)  #uni1479	CANADIAN SYLLABICS WEST-CREE KWII
        chars.append(0x147A)  #uni147A	CANADIAN SYLLABICS KWO
        chars.append(0x147B)  #uni147B	CANADIAN SYLLABICS WEST-CREE KWO
        chars.append(0x147C)  #uni147C	CANADIAN SYLLABICS KWOO
        chars.append(0x147D)  #uni147D	CANADIAN SYLLABICS WEST-CREE KWOO
        chars.append(0x147E)  #uni147E	CANADIAN SYLLABICS KWA
        chars.append(0x147F)  #uni147F	CANADIAN SYLLABICS WEST-CREE KWA
        chars.append(0x1480)  #uni1480	CANADIAN SYLLABICS KWAA
        chars.append(0x1481)  #uni1481	CANADIAN SYLLABICS WEST-CREE KWAA
        chars.append(0x1482)  #uni1482	CANADIAN SYLLABICS NASKAPI KWAA
        chars.append(0x1483)  #uni1483	CANADIAN SYLLABICS K
        chars.append(0x1484)  #uni1484	CANADIAN SYLLABICS KW
        chars.append(0x1485)  #uni1485	CANADIAN SYLLABICS SOUTH-SLAVEY KEH
        chars.append(0x1486)  #uni1486	CANADIAN SYLLABICS SOUTH-SLAVEY KIH
        chars.append(0x1487)  #uni1487	CANADIAN SYLLABICS SOUTH-SLAVEY KOH
        chars.append(0x1488)  #uni1488	CANADIAN SYLLABICS SOUTH-SLAVEY KAH
        chars.append(0x1489)  #uni1489	CANADIAN SYLLABICS CE
        chars.append(0x148A)  #uni148A	CANADIAN SYLLABICS CAAI
        chars.append(0x148B)  #uni148B	CANADIAN SYLLABICS CI
        chars.append(0x148C)  #uni148C	CANADIAN SYLLABICS CII
        chars.append(0x148D)  #uni148D	CANADIAN SYLLABICS CO
        chars.append(0x148E)  #uni148E	CANADIAN SYLLABICS COO
        chars.append(0x148F)  #uni148F	CANADIAN SYLLABICS Y-CREE COO
        chars.append(0x1490)  #uni1490	CANADIAN SYLLABICS CA
        chars.append(0x1491)  #uni1491	CANADIAN SYLLABICS CAA
        chars.append(0x1492)  #uni1492	CANADIAN SYLLABICS CWE
        chars.append(0x1493)  #uni1493	CANADIAN SYLLABICS WEST-CREE CWE
        chars.append(0x1494)  #uni1494	CANADIAN SYLLABICS CWI
        chars.append(0x1495)  #uni1495	CANADIAN SYLLABICS WEST-CREE CWI
        chars.append(0x1496)  #uni1496	CANADIAN SYLLABICS CWII
        chars.append(0x1497)  #uni1497	CANADIAN SYLLABICS WEST-CREE CWII
        chars.append(0x1498)  #uni1498	CANADIAN SYLLABICS CWO
        chars.append(0x1499)  #uni1499	CANADIAN SYLLABICS WEST-CREE CWO
        chars.append(0x149A)  #uni149A	CANADIAN SYLLABICS CWOO
        chars.append(0x149B)  #uni149B	CANADIAN SYLLABICS WEST-CREE CWOO
        chars.append(0x149C)  #uni149C	CANADIAN SYLLABICS CWA
        chars.append(0x149D)  #uni149D	CANADIAN SYLLABICS WEST-CREE CWA
        chars.append(0x149E)  #uni149E	CANADIAN SYLLABICS CWAA
        chars.append(0x149F)  #uni149F	CANADIAN SYLLABICS WEST-CREE CWAA
        chars.append(0x14A0)  #uni14A0	CANADIAN SYLLABICS NASKAPI CWAA
        chars.append(0x14A1)  #uni14A1	CANADIAN SYLLABICS C
        chars.append(0x14A2)  #uni14A2	CANADIAN SYLLABICS SAYISI TH
        chars.append(0x14A3)  #uni14A3	CANADIAN SYLLABICS ME
        chars.append(0x14A4)  #uni14A4	CANADIAN SYLLABICS MAAI
        chars.append(0x14A5)  #uni14A5	CANADIAN SYLLABICS MI
        chars.append(0x14A6)  #uni14A6	CANADIAN SYLLABICS MII
        chars.append(0x14A7)  #uni14A7	CANADIAN SYLLABICS MO
        chars.append(0x14A8)  #uni14A8	CANADIAN SYLLABICS MOO
        chars.append(0x14A9)  #uni14A9	CANADIAN SYLLABICS Y-CREE MOO
        chars.append(0x14AA)  #uni14AA	CANADIAN SYLLABICS MA
        chars.append(0x14AB)  #uni14AB	CANADIAN SYLLABICS MAA
        chars.append(0x14AC)  #uni14AC	CANADIAN SYLLABICS MWE
        chars.append(0x14AD)  #uni14AD	CANADIAN SYLLABICS WEST-CREE MWE
        chars.append(0x14AE)  #uni14AE	CANADIAN SYLLABICS MWI
        chars.append(0x14AF)  #uni14AF	CANADIAN SYLLABICS WEST-CREE MWI
        chars.append(0x14B0)  #uni14B0	CANADIAN SYLLABICS MWII
        chars.append(0x14B1)  #uni14B1	CANADIAN SYLLABICS WEST-CREE MWII
        chars.append(0x14B2)  #uni14B2	CANADIAN SYLLABICS MWO
        chars.append(0x14B3)  #uni14B3	CANADIAN SYLLABICS WEST-CREE MWO
        chars.append(0x14B4)  #uni14B4	CANADIAN SYLLABICS MWOO
        chars.append(0x14B5)  #uni14B5	CANADIAN SYLLABICS WEST-CREE MWOO
        chars.append(0x14B6)  #uni14B6	CANADIAN SYLLABICS MWA
        chars.append(0x14B7)  #uni14B7	CANADIAN SYLLABICS WEST-CREE MWA
        chars.append(0x14B8)  #uni14B8	CANADIAN SYLLABICS MWAA
        chars.append(0x14B9)  #uni14B9	CANADIAN SYLLABICS WEST-CREE MWAA
        chars.append(0x14BA)  #uni14BA	CANADIAN SYLLABICS NASKAPI MWAA
        chars.append(0x14BB)  #uni14BB	CANADIAN SYLLABICS M
        chars.append(0x14BC)  #uni14BC	CANADIAN SYLLABICS WEST-CREE M
        chars.append(0x14BD)  #uni14BD	CANADIAN SYLLABICS MH
        chars.append(0x14BE)  #uni14BE	CANADIAN SYLLABICS ATHAPASCAN M
        chars.append(0x14BF)  #uni14BF	CANADIAN SYLLABICS SAYISI M
        chars.append(0x14C0)  #uni14C0	CANADIAN SYLLABICS NE
        chars.append(0x14C1)  #uni14C1	CANADIAN SYLLABICS NAAI
        chars.append(0x14C2)  #uni14C2	CANADIAN SYLLABICS NI
        chars.append(0x14C3)  #uni14C3	CANADIAN SYLLABICS NII
        chars.append(0x14C4)  #uni14C4	CANADIAN SYLLABICS NO
        chars.append(0x14C5)  #uni14C5	CANADIAN SYLLABICS NOO
        chars.append(0x14C6)  #uni14C6	CANADIAN SYLLABICS Y-CREE NOO
        chars.append(0x14C7)  #uni14C7	CANADIAN SYLLABICS NA
        chars.append(0x14C8)  #uni14C8	CANADIAN SYLLABICS NAA
        chars.append(0x14C9)  #uni14C9	CANADIAN SYLLABICS NWE
        chars.append(0x14CA)  #uni14CA	CANADIAN SYLLABICS WEST-CREE NWE
        chars.append(0x14CB)  #uni14CB	CANADIAN SYLLABICS NWA
        chars.append(0x14CC)  #uni14CC	CANADIAN SYLLABICS WEST-CREE NWA
        chars.append(0x14CD)  #uni14CD	CANADIAN SYLLABICS NWAA
        chars.append(0x14CE)  #uni14CE	CANADIAN SYLLABICS WEST-CREE NWAA
        chars.append(0x14CF)  #uni14CF	CANADIAN SYLLABICS NASKAPI NWAA
        chars.append(0x14D0)  #uni14D0	CANADIAN SYLLABICS N
        chars.append(0x14D1)  #uni14D1	CANADIAN SYLLABICS CARRIER NG
        chars.append(0x14D2)  #uni14D2	CANADIAN SYLLABICS NH
        chars.append(0x14D3)  #uni14D3	CANADIAN SYLLABICS LE
        chars.append(0x14D4)  #uni14D4	CANADIAN SYLLABICS LAAI
        chars.append(0x14D5)  #uni14D5	CANADIAN SYLLABICS LI
        chars.append(0x14D6)  #uni14D6	CANADIAN SYLLABICS LII
        chars.append(0x14D7)  #uni14D7	CANADIAN SYLLABICS LO
        chars.append(0x14D8)  #uni14D8	CANADIAN SYLLABICS LOO
        chars.append(0x14D9)  #uni14D9	CANADIAN SYLLABICS Y-CREE LOO
        chars.append(0x14DA)  #uni14DA	CANADIAN SYLLABICS LA
        chars.append(0x14DB)  #uni14DB	CANADIAN SYLLABICS LAA
        chars.append(0x14DC)  #uni14DC	CANADIAN SYLLABICS LWE
        chars.append(0x14DD)  #uni14DD	CANADIAN SYLLABICS WEST-CREE LWE
        chars.append(0x14DE)  #uni14DE	CANADIAN SYLLABICS LWI
        chars.append(0x14DF)  #uni14DF	CANADIAN SYLLABICS WEST-CREE LWI
        chars.append(0x14E0)  #uni14E0	CANADIAN SYLLABICS LWII
        chars.append(0x14E1)  #uni14E1	CANADIAN SYLLABICS WEST-CREE LWII
        chars.append(0x14E2)  #uni14E2	CANADIAN SYLLABICS LWO
        chars.append(0x14E3)  #uni14E3	CANADIAN SYLLABICS WEST-CREE LWO
        chars.append(0x14E4)  #uni14E4	CANADIAN SYLLABICS LWOO
        chars.append(0x14E5)  #uni14E5	CANADIAN SYLLABICS WEST-CREE LWOO
        chars.append(0x14E6)  #uni14E6	CANADIAN SYLLABICS LWA
        chars.append(0x14E7)  #uni14E7	CANADIAN SYLLABICS WEST-CREE LWA
        chars.append(0x14E8)  #uni14E8	CANADIAN SYLLABICS LWAA
        chars.append(0x14E9)  #uni14E9	CANADIAN SYLLABICS WEST-CREE LWAA
        chars.append(0x14EA)  #uni14EA	CANADIAN SYLLABICS L
        chars.append(0x14EB)  #uni14EB	CANADIAN SYLLABICS WEST-CREE L
        chars.append(0x14EC)  #uni14EC	CANADIAN SYLLABICS MEDIAL L
        chars.append(0x14ED)  #uni14ED	CANADIAN SYLLABICS SE
        chars.append(0x14EE)  #uni14EE	CANADIAN SYLLABICS SAAI
        chars.append(0x14EF)  #uni14EF	CANADIAN SYLLABICS SI
        chars.append(0x14F0)  #uni14F0	CANADIAN SYLLABICS SII
        chars.append(0x14F1)  #uni14F1	CANADIAN SYLLABICS SO
        chars.append(0x14F2)  #uni14F2	CANADIAN SYLLABICS SOO
        chars.append(0x14F3)  #uni14F3	CANADIAN SYLLABICS Y-CREE SOO
        chars.append(0x14F4)  #uni14F4	CANADIAN SYLLABICS SA
        chars.append(0x14F5)  #uni14F5	CANADIAN SYLLABICS SAA
        chars.append(0x14F6)  #uni14F6	CANADIAN SYLLABICS SWE
        chars.append(0x14F7)  #uni14F7	CANADIAN SYLLABICS WEST-CREE SWE
        chars.append(0x14F8)  #uni14F8	CANADIAN SYLLABICS SWI
        chars.append(0x14F9)  #uni14F9	CANADIAN SYLLABICS WEST-CREE SWI
        chars.append(0x14FA)  #uni14FA	CANADIAN SYLLABICS SWII
        chars.append(0x14FB)  #uni14FB	CANADIAN SYLLABICS WEST-CREE SWII
        chars.append(0x14FC)  #uni14FC	CANADIAN SYLLABICS SWO
        chars.append(0x14FD)  #uni14FD	CANADIAN SYLLABICS WEST-CREE SWO
        chars.append(0x14FE)  #uni14FE	CANADIAN SYLLABICS SWOO
        chars.append(0x14FF)  #uni14FF	CANADIAN SYLLABICS WEST-CREE SWOO
        chars.append(0x1500)  #uni1500	CANADIAN SYLLABICS SWA
        chars.append(0x1501)  #uni1501	CANADIAN SYLLABICS WEST-CREE SWA
        chars.append(0x1502)  #uni1502	CANADIAN SYLLABICS SWAA
        chars.append(0x1503)  #uni1503	CANADIAN SYLLABICS WEST-CREE SWAA
        chars.append(0x1504)  #uni1504	CANADIAN SYLLABICS NASKAPI SWAA
        chars.append(0x1505)  #uni1505	CANADIAN SYLLABICS S
        chars.append(0x1506)  #uni1506	CANADIAN SYLLABICS ATHAPASCAN S
        chars.append(0x1507)  #uni1507	CANADIAN SYLLABICS SW
        chars.append(0x1508)  #uni1508	CANADIAN SYLLABICS BLACKFOOT S
        chars.append(0x1509)  #uni1509	CANADIAN SYLLABICS MOOSE-CREE SK
        chars.append(0x150A)  #uni150A	CANADIAN SYLLABICS NASKAPI SKW
        chars.append(0x150B)  #uni150B	CANADIAN SYLLABICS NASKAPI S-W
        chars.append(0x150C)  #uni150C	CANADIAN SYLLABICS NASKAPI SPWA
        chars.append(0x150D)  #uni150D	CANADIAN SYLLABICS NASKAPI STWA
        chars.append(0x150E)  #uni150E	CANADIAN SYLLABICS NASKAPI SKWA
        chars.append(0x150F)  #uni150F	CANADIAN SYLLABICS NASKAPI SCWA
        chars.append(0x1510)  #uni1510	CANADIAN SYLLABICS SHE
        chars.append(0x1511)  #uni1511	CANADIAN SYLLABICS SHI
        chars.append(0x1512)  #uni1512	CANADIAN SYLLABICS SHII
        chars.append(0x1513)  #uni1513	CANADIAN SYLLABICS SHO
        chars.append(0x1514)  #uni1514	CANADIAN SYLLABICS SHOO
        chars.append(0x1515)  #uni1515	CANADIAN SYLLABICS SHA
        chars.append(0x1516)  #uni1516	CANADIAN SYLLABICS SHAA
        chars.append(0x1517)  #uni1517	CANADIAN SYLLABICS SHWE
        chars.append(0x1518)  #uni1518	CANADIAN SYLLABICS WEST-CREE SHWE
        chars.append(0x1519)  #uni1519	CANADIAN SYLLABICS SHWI
        chars.append(0x151A)  #uni151A	CANADIAN SYLLABICS WEST-CREE SHWI
        chars.append(0x151B)  #uni151B	CANADIAN SYLLABICS SHWII
        chars.append(0x151C)  #uni151C	CANADIAN SYLLABICS WEST-CREE SHWII
        chars.append(0x151D)  #uni151D	CANADIAN SYLLABICS SHWO
        chars.append(0x151E)  #uni151E	CANADIAN SYLLABICS WEST-CREE SHWO
        chars.append(0x151F)  #uni151F	CANADIAN SYLLABICS SHWOO
        chars.append(0x1520)  #uni1520	CANADIAN SYLLABICS WEST-CREE SHWOO
        chars.append(0x1521)  #uni1521	CANADIAN SYLLABICS SHWA
        chars.append(0x1522)  #uni1522	CANADIAN SYLLABICS WEST-CREE SHWA
        chars.append(0x1523)  #uni1523	CANADIAN SYLLABICS SHWAA
        chars.append(0x1524)  #uni1524	CANADIAN SYLLABICS WEST-CREE SHWAA
        chars.append(0x1525)  #uni1525	CANADIAN SYLLABICS SH
        chars.append(0x1526)  #uni1526	CANADIAN SYLLABICS YE
        chars.append(0x1527)  #uni1527	CANADIAN SYLLABICS YAAI
        chars.append(0x1528)  #uni1528	CANADIAN SYLLABICS YI
        chars.append(0x1529)  #uni1529	CANADIAN SYLLABICS YII
        chars.append(0x152A)  #uni152A	CANADIAN SYLLABICS YO
        chars.append(0x152B)  #uni152B	CANADIAN SYLLABICS YOO
        chars.append(0x152C)  #uni152C	CANADIAN SYLLABICS Y-CREE YOO
        chars.append(0x152D)  #uni152D	CANADIAN SYLLABICS YA
        chars.append(0x152E)  #uni152E	CANADIAN SYLLABICS YAA
        chars.append(0x152F)  #uni152F	CANADIAN SYLLABICS YWE
        chars.append(0x1530)  #uni1530	CANADIAN SYLLABICS WEST-CREE YWE
        chars.append(0x1531)  #uni1531	CANADIAN SYLLABICS YWI
        chars.append(0x1532)  #uni1532	CANADIAN SYLLABICS WEST-CREE YWI
        chars.append(0x1533)  #uni1533	CANADIAN SYLLABICS YWII
        chars.append(0x1534)  #uni1534	CANADIAN SYLLABICS WEST-CREE YWII
        chars.append(0x1535)  #uni1535	CANADIAN SYLLABICS YWO
        chars.append(0x1536)  #uni1536	CANADIAN SYLLABICS WEST-CREE YWO
        chars.append(0x1537)  #uni1537	CANADIAN SYLLABICS YWOO
        chars.append(0x1538)  #uni1538	CANADIAN SYLLABICS WEST-CREE YWOO
        chars.append(0x1539)  #uni1539	CANADIAN SYLLABICS YWA
        chars.append(0x153A)  #uni153A	CANADIAN SYLLABICS WEST-CREE YWA
        chars.append(0x153B)  #uni153B	CANADIAN SYLLABICS YWAA
        chars.append(0x153C)  #uni153C	CANADIAN SYLLABICS WEST-CREE YWAA
        chars.append(0x153D)  #uni153D	CANADIAN SYLLABICS NASKAPI YWAA
        chars.append(0x153E)  #uni153E	CANADIAN SYLLABICS Y
        chars.append(0x153F)  #uni153F	CANADIAN SYLLABICS BIBLE-CREE Y
        chars.append(0x1540)  #uni1540	CANADIAN SYLLABICS WEST-CREE Y
        chars.append(0x1541)  #uni1541	CANADIAN SYLLABICS SAYISI YI
        chars.append(0x1542)  #uni1542	CANADIAN SYLLABICS RE
        chars.append(0x1543)  #uni1543	CANADIAN SYLLABICS R-CREE RE
        chars.append(0x1544)  #uni1544	CANADIAN SYLLABICS WEST-CREE LE
        chars.append(0x1545)  #uni1545	CANADIAN SYLLABICS RAAI
        chars.append(0x1546)  #uni1546	CANADIAN SYLLABICS RI
        chars.append(0x1547)  #uni1547	CANADIAN SYLLABICS RII
        chars.append(0x1548)  #uni1548	CANADIAN SYLLABICS RO
        chars.append(0x1549)  #uni1549	CANADIAN SYLLABICS ROO
        chars.append(0x154A)  #uni154A	CANADIAN SYLLABICS WEST-CREE LO
        chars.append(0x154B)  #uni154B	CANADIAN SYLLABICS RA
        chars.append(0x154C)  #uni154C	CANADIAN SYLLABICS RAA
        chars.append(0x154D)  #uni154D	CANADIAN SYLLABICS WEST-CREE LA
        chars.append(0x154E)  #uni154E	CANADIAN SYLLABICS RWAA
        chars.append(0x154F)  #uni154F	CANADIAN SYLLABICS WEST-CREE RWAA
        chars.append(0x1550)  #uni1550	CANADIAN SYLLABICS R
        chars.append(0x1551)  #uni1551	CANADIAN SYLLABICS WEST-CREE R
        chars.append(0x1552)  #uni1552	CANADIAN SYLLABICS MEDIAL R
        chars.append(0x1553)  #uni1553	CANADIAN SYLLABICS FE
        chars.append(0x1554)  #uni1554	CANADIAN SYLLABICS FAAI
        chars.append(0x1555)  #uni1555	CANADIAN SYLLABICS FI
        chars.append(0x1556)  #uni1556	CANADIAN SYLLABICS FII
        chars.append(0x1557)  #uni1557	CANADIAN SYLLABICS FO
        chars.append(0x1558)  #uni1558	CANADIAN SYLLABICS FOO
        chars.append(0x1559)  #uni1559	CANADIAN SYLLABICS FA
        chars.append(0x155A)  #uni155A	CANADIAN SYLLABICS FAA
        chars.append(0x155B)  #uni155B	CANADIAN SYLLABICS FWAA
        chars.append(0x155C)  #uni155C	CANADIAN SYLLABICS WEST-CREE FWAA
        chars.append(0x155D)  #uni155D	CANADIAN SYLLABICS F
        chars.append(0x155E)  #uni155E	CANADIAN SYLLABICS THE
        chars.append(0x155F)  #uni155F	CANADIAN SYLLABICS N-CREE THE
        chars.append(0x1560)  #uni1560	CANADIAN SYLLABICS THI
        chars.append(0x1561)  #uni1561	CANADIAN SYLLABICS N-CREE THI
        chars.append(0x1562)  #uni1562	CANADIAN SYLLABICS THII
        chars.append(0x1563)  #uni1563	CANADIAN SYLLABICS N-CREE THII
        chars.append(0x1564)  #uni1564	CANADIAN SYLLABICS THO
        chars.append(0x1565)  #uni1565	CANADIAN SYLLABICS THOO
        chars.append(0x1566)  #uni1566	CANADIAN SYLLABICS THA
        chars.append(0x1567)  #uni1567	CANADIAN SYLLABICS THAA
        chars.append(0x1568)  #uni1568	CANADIAN SYLLABICS THWAA
        chars.append(0x1569)  #uni1569	CANADIAN SYLLABICS WEST-CREE THWAA
        chars.append(0x156A)  #uni156A	CANADIAN SYLLABICS TH
        chars.append(0x156B)  #uni156B	CANADIAN SYLLABICS TTHE
        chars.append(0x156C)  #uni156C	CANADIAN SYLLABICS TTHI
        chars.append(0x156D)  #uni156D	CANADIAN SYLLABICS TTHO
        chars.append(0x156E)  #uni156E	CANADIAN SYLLABICS TTHA
        chars.append(0x156F)  #uni156F	CANADIAN SYLLABICS TTH
        chars.append(0x1570)  #uni1570	CANADIAN SYLLABICS TYE
        chars.append(0x1571)  #uni1571	CANADIAN SYLLABICS TYI
        chars.append(0x1572)  #uni1572	CANADIAN SYLLABICS TYO
        chars.append(0x1573)  #uni1573	CANADIAN SYLLABICS TYA
        chars.append(0x1574)  #uni1574	CANADIAN SYLLABICS NUNAVIK HE
        chars.append(0x1575)  #uni1575	CANADIAN SYLLABICS NUNAVIK HI
        chars.append(0x1576)  #uni1576	CANADIAN SYLLABICS NUNAVIK HII
        chars.append(0x1577)  #uni1577	CANADIAN SYLLABICS NUNAVIK HO
        chars.append(0x1578)  #uni1578	CANADIAN SYLLABICS NUNAVIK HOO
        chars.append(0x1579)  #uni1579	CANADIAN SYLLABICS NUNAVIK HA
        chars.append(0x157A)  #uni157A	CANADIAN SYLLABICS NUNAVIK HAA
        chars.append(0x157B)  #uni157B	CANADIAN SYLLABICS NUNAVIK H
        chars.append(0x157C)  #uni157C	CANADIAN SYLLABICS NUNAVUT H
        chars.append(0x157D)  #uni157D	CANADIAN SYLLABICS HK
        chars.append(0x157E)  #uni157E	CANADIAN SYLLABICS QAAI
        chars.append(0x157F)  #uni157F	CANADIAN SYLLABICS QI
        chars.append(0x1580)  #uni1580	CANADIAN SYLLABICS QII
        chars.append(0x1581)  #uni1581	CANADIAN SYLLABICS QO
        chars.append(0x1582)  #uni1582	CANADIAN SYLLABICS QOO
        chars.append(0x1583)  #uni1583	CANADIAN SYLLABICS QA
        chars.append(0x1584)  #uni1584	CANADIAN SYLLABICS QAA
        chars.append(0x1585)  #uni1585	CANADIAN SYLLABICS Q
        chars.append(0x1586)  #uni1586	CANADIAN SYLLABICS TLHE
        chars.append(0x1587)  #uni1587	CANADIAN SYLLABICS TLHI
        chars.append(0x1588)  #uni1588	CANADIAN SYLLABICS TLHO
        chars.append(0x1589)  #uni1589	CANADIAN SYLLABICS TLHA
        chars.append(0x158A)  #uni158A	CANADIAN SYLLABICS WEST-CREE RE
        chars.append(0x158B)  #uni158B	CANADIAN SYLLABICS WEST-CREE RI
        chars.append(0x158C)  #uni158C	CANADIAN SYLLABICS WEST-CREE RO
        chars.append(0x158D)  #uni158D	CANADIAN SYLLABICS WEST-CREE RA
        chars.append(0x158E)  #uni158E	CANADIAN SYLLABICS NGAAI
        chars.append(0x158F)  #uni158F	CANADIAN SYLLABICS NGI
        chars.append(0x1590)  #uni1590	CANADIAN SYLLABICS NGII
        chars.append(0x1591)  #uni1591	CANADIAN SYLLABICS NGO
        chars.append(0x1592)  #uni1592	CANADIAN SYLLABICS NGOO
        chars.append(0x1593)  #uni1593	CANADIAN SYLLABICS NGA
        chars.append(0x1594)  #uni1594	CANADIAN SYLLABICS NGAA
        chars.append(0x1595)  #uni1595	CANADIAN SYLLABICS NG
        chars.append(0x1596)  #uni1596	CANADIAN SYLLABICS NNG
        chars.append(0x1597)  #uni1597	CANADIAN SYLLABICS SAYISI SHE
        chars.append(0x1598)  #uni1598	CANADIAN SYLLABICS SAYISI SHI
        chars.append(0x1599)  #uni1599	CANADIAN SYLLABICS SAYISI SHO
        chars.append(0x159A)  #uni159A	CANADIAN SYLLABICS SAYISI SHA
        chars.append(0x159B)  #uni159B	CANADIAN SYLLABICS WOODS-CREE THE
        chars.append(0x159C)  #uni159C	CANADIAN SYLLABICS WOODS-CREE THI
        chars.append(0x159D)  #uni159D	CANADIAN SYLLABICS WOODS-CREE THO
        chars.append(0x159E)  #uni159E	CANADIAN SYLLABICS WOODS-CREE THA
        chars.append(0x159F)  #uni159F	CANADIAN SYLLABICS WOODS-CREE TH
        chars.append(0x15A0)  #uni15A0	CANADIAN SYLLABICS LHI
        chars.append(0x15A1)  #uni15A1	CANADIAN SYLLABICS LHII
        chars.append(0x15A2)  #uni15A2	CANADIAN SYLLABICS LHO
        chars.append(0x15A3)  #uni15A3	CANADIAN SYLLABICS LHOO
        chars.append(0x15A4)  #uni15A4	CANADIAN SYLLABICS LHA
        chars.append(0x15A5)  #uni15A5	CANADIAN SYLLABICS LHAA
        chars.append(0x15A6)  #uni15A6	CANADIAN SYLLABICS LH
        chars.append(0x15A7)  #uni15A7	CANADIAN SYLLABICS TH-CREE THE
        chars.append(0x15A8)  #uni15A8	CANADIAN SYLLABICS TH-CREE THI
        chars.append(0x15A9)  #uni15A9	CANADIAN SYLLABICS TH-CREE THII
        chars.append(0x15AA)  #uni15AA	CANADIAN SYLLABICS TH-CREE THO
        chars.append(0x15AB)  #uni15AB	CANADIAN SYLLABICS TH-CREE THOO
        chars.append(0x15AC)  #uni15AC	CANADIAN SYLLABICS TH-CREE THA
        chars.append(0x15AD)  #uni15AD	CANADIAN SYLLABICS TH-CREE THAA
        chars.append(0x15AE)  #uni15AE	CANADIAN SYLLABICS TH-CREE TH
        chars.append(0x15AF)  #uni15AF	CANADIAN SYLLABICS AIVILIK B
        chars.append(0x15B0)  #uni15B0	CANADIAN SYLLABICS BLACKFOOT E
        chars.append(0x15B1)  #uni15B1	CANADIAN SYLLABICS BLACKFOOT I
        chars.append(0x15B2)  #uni15B2	CANADIAN SYLLABICS BLACKFOOT O
        chars.append(0x15B3)  #uni15B3	CANADIAN SYLLABICS BLACKFOOT A
        chars.append(0x15B4)  #uni15B4	CANADIAN SYLLABICS BLACKFOOT WE
        chars.append(0x15B5)  #uni15B5	CANADIAN SYLLABICS BLACKFOOT WI
        chars.append(0x15B6)  #uni15B6	CANADIAN SYLLABICS BLACKFOOT WO
        chars.append(0x15B7)  #uni15B7	CANADIAN SYLLABICS BLACKFOOT WA
        chars.append(0x15B8)  #uni15B8	CANADIAN SYLLABICS BLACKFOOT NE
        chars.append(0x15B9)  #uni15B9	CANADIAN SYLLABICS BLACKFOOT NI
        chars.append(0x15BA)  #uni15BA	CANADIAN SYLLABICS BLACKFOOT NO
        chars.append(0x15BB)  #uni15BB	CANADIAN SYLLABICS BLACKFOOT NA
        chars.append(0x15BC)  #uni15BC	CANADIAN SYLLABICS BLACKFOOT KE
        chars.append(0x15BD)  #uni15BD	CANADIAN SYLLABICS BLACKFOOT KI
        chars.append(0x15BE)  #uni15BE	CANADIAN SYLLABICS BLACKFOOT KO
        chars.append(0x15BF)  #uni15BF	CANADIAN SYLLABICS BLACKFOOT KA
        chars.append(0x15C0)  #uni15C0	CANADIAN SYLLABICS SAYISI HE
        chars.append(0x15C1)  #uni15C1	CANADIAN SYLLABICS SAYISI HI
        chars.append(0x15C2)  #uni15C2	CANADIAN SYLLABICS SAYISI HO
        chars.append(0x15C3)  #uni15C3	CANADIAN SYLLABICS SAYISI HA
        chars.append(0x15C4)  #uni15C4	CANADIAN SYLLABICS CARRIER GHU
        chars.append(0x15C5)  #uni15C5	CANADIAN SYLLABICS CARRIER GHO
        chars.append(0x15C6)  #uni15C6	CANADIAN SYLLABICS CARRIER GHE
        chars.append(0x15C7)  #uni15C7	CANADIAN SYLLABICS CARRIER GHEE
        chars.append(0x15C8)  #uni15C8	CANADIAN SYLLABICS CARRIER GHI
        chars.append(0x15C9)  #uni15C9	CANADIAN SYLLABICS CARRIER GHA
        chars.append(0x15CA)  #uni15CA	CANADIAN SYLLABICS CARRIER RU
        chars.append(0x15CB)  #uni15CB	CANADIAN SYLLABICS CARRIER RO
        chars.append(0x15CC)  #uni15CC	CANADIAN SYLLABICS CARRIER RE
        chars.append(0x15CD)  #uni15CD	CANADIAN SYLLABICS CARRIER REE
        chars.append(0x15CE)  #uni15CE	CANADIAN SYLLABICS CARRIER RI
        chars.append(0x15CF)  #uni15CF	CANADIAN SYLLABICS CARRIER RA
        chars.append(0x15D0)  #uni15D0	CANADIAN SYLLABICS CARRIER WU
        chars.append(0x15D1)  #uni15D1	CANADIAN SYLLABICS CARRIER WO
        chars.append(0x15D2)  #uni15D2	CANADIAN SYLLABICS CARRIER WE
        chars.append(0x15D3)  #uni15D3	CANADIAN SYLLABICS CARRIER WEE
        chars.append(0x15D4)  #uni15D4	CANADIAN SYLLABICS CARRIER WI
        chars.append(0x15D5)  #uni15D5	CANADIAN SYLLABICS CARRIER WA
        chars.append(0x15D6)  #uni15D6	CANADIAN SYLLABICS CARRIER HWU
        chars.append(0x15D7)  #uni15D7	CANADIAN SYLLABICS CARRIER HWO
        chars.append(0x15D8)  #uni15D8	CANADIAN SYLLABICS CARRIER HWE
        chars.append(0x15D9)  #uni15D9	CANADIAN SYLLABICS CARRIER HWEE
        chars.append(0x15DA)  #uni15DA	CANADIAN SYLLABICS CARRIER HWI
        chars.append(0x15DB)  #uni15DB	CANADIAN SYLLABICS CARRIER HWA
        chars.append(0x15DC)  #uni15DC	CANADIAN SYLLABICS CARRIER THU
        chars.append(0x15DD)  #uni15DD	CANADIAN SYLLABICS CARRIER THO
        chars.append(0x15DE)  #uni15DE	CANADIAN SYLLABICS CARRIER THE
        chars.append(0x15DF)  #uni15DF	CANADIAN SYLLABICS CARRIER THEE
        chars.append(0x15E0)  #uni15E0	CANADIAN SYLLABICS CARRIER THI
        chars.append(0x15E1)  #uni15E1	CANADIAN SYLLABICS CARRIER THA
        chars.append(0x15E2)  #uni15E2	CANADIAN SYLLABICS CARRIER TTU
        chars.append(0x15E3)  #uni15E3	CANADIAN SYLLABICS CARRIER TTO
        chars.append(0x15E4)  #uni15E4	CANADIAN SYLLABICS CARRIER TTE
        chars.append(0x15E5)  #uni15E5	CANADIAN SYLLABICS CARRIER TTEE
        chars.append(0x15E6)  #uni15E6	CANADIAN SYLLABICS CARRIER TTI
        chars.append(0x15E7)  #uni15E7	CANADIAN SYLLABICS CARRIER TTA
        chars.append(0x15E8)  #uni15E8	CANADIAN SYLLABICS CARRIER PU
        chars.append(0x15E9)  #uni15E9	CANADIAN SYLLABICS CARRIER PO
        chars.append(0x15EA)  #uni15EA	CANADIAN SYLLABICS CARRIER PE
        chars.append(0x15EB)  #uni15EB	CANADIAN SYLLABICS CARRIER PEE
        chars.append(0x15EC)  #uni15EC	CANADIAN SYLLABICS CARRIER PI
        chars.append(0x15ED)  #uni15ED	CANADIAN SYLLABICS CARRIER PA
        chars.append(0x15EE)  #uni15EE	CANADIAN SYLLABICS CARRIER P
        chars.append(0x15EF)  #uni15EF	CANADIAN SYLLABICS CARRIER GU
        chars.append(0x15F0)  #uni15F0	CANADIAN SYLLABICS CARRIER GO
        chars.append(0x15F1)  #uni15F1	CANADIAN SYLLABICS CARRIER GE
        chars.append(0x15F2)  #uni15F2	CANADIAN SYLLABICS CARRIER GEE
        chars.append(0x15F3)  #uni15F3	CANADIAN SYLLABICS CARRIER GI
        chars.append(0x15F4)  #uni15F4	CANADIAN SYLLABICS CARRIER GA
        chars.append(0x15F5)  #uni15F5	CANADIAN SYLLABICS CARRIER KHU
        chars.append(0x15F6)  #uni15F6	CANADIAN SYLLABICS CARRIER KHO
        chars.append(0x15F7)  #uni15F7	CANADIAN SYLLABICS CARRIER KHE
        chars.append(0x15F8)  #uni15F8	CANADIAN SYLLABICS CARRIER KHEE
        chars.append(0x15F9)  #uni15F9	CANADIAN SYLLABICS CARRIER KHI
        chars.append(0x15FA)  #uni15FA	CANADIAN SYLLABICS CARRIER KHA
        chars.append(0x15FB)  #uni15FB	CANADIAN SYLLABICS CARRIER KKU
        chars.append(0x15FC)  #uni15FC	CANADIAN SYLLABICS CARRIER KKO
        chars.append(0x15FD)  #uni15FD	CANADIAN SYLLABICS CARRIER KKE
        chars.append(0x15FE)  #uni15FE	CANADIAN SYLLABICS CARRIER KKEE
        chars.append(0x15FF)  #uni15FF	CANADIAN SYLLABICS CARRIER KKI
        chars.append(0x1600)  #uni1600	CANADIAN SYLLABICS CARRIER KKA
        chars.append(0x1601)  #uni1601	CANADIAN SYLLABICS CARRIER KK
        chars.append(0x1602)  #uni1602	CANADIAN SYLLABICS CARRIER NU
        chars.append(0x1603)  #uni1603	CANADIAN SYLLABICS CARRIER NO
        chars.append(0x1604)  #uni1604	CANADIAN SYLLABICS CARRIER NE
        chars.append(0x1605)  #uni1605	CANADIAN SYLLABICS CARRIER NEE
        chars.append(0x1606)  #uni1606	CANADIAN SYLLABICS CARRIER NI
        chars.append(0x1607)  #uni1607	CANADIAN SYLLABICS CARRIER NA
        chars.append(0x1608)  #uni1608	CANADIAN SYLLABICS CARRIER MU
        chars.append(0x1609)  #uni1609	CANADIAN SYLLABICS CARRIER MO
        chars.append(0x160A)  #uni160A	CANADIAN SYLLABICS CARRIER ME
        chars.append(0x160B)  #uni160B	CANADIAN SYLLABICS CARRIER MEE
        chars.append(0x160C)  #uni160C	CANADIAN SYLLABICS CARRIER MI
        chars.append(0x160D)  #uni160D	CANADIAN SYLLABICS CARRIER MA
        chars.append(0x160E)  #uni160E	CANADIAN SYLLABICS CARRIER YU
        chars.append(0x160F)  #uni160F	CANADIAN SYLLABICS CARRIER YO
        chars.append(0x1610)  #uni1610	CANADIAN SYLLABICS CARRIER YE
        chars.append(0x1611)  #uni1611	CANADIAN SYLLABICS CARRIER YEE
        chars.append(0x1612)  #uni1612	CANADIAN SYLLABICS CARRIER YI
        chars.append(0x1613)  #uni1613	CANADIAN SYLLABICS CARRIER YA
        chars.append(0x1614)  #uni1614	CANADIAN SYLLABICS CARRIER JU
        chars.append(0x1615)  #uni1615	CANADIAN SYLLABICS SAYISI JU
        chars.append(0x1616)  #uni1616	CANADIAN SYLLABICS CARRIER JO
        chars.append(0x1617)  #uni1617	CANADIAN SYLLABICS CARRIER JE
        chars.append(0x1618)  #uni1618	CANADIAN SYLLABICS CARRIER JEE
        chars.append(0x1619)  #uni1619	CANADIAN SYLLABICS CARRIER JI
        chars.append(0x161A)  #uni161A	CANADIAN SYLLABICS SAYISI JI
        chars.append(0x161B)  #uni161B	CANADIAN SYLLABICS CARRIER JA
        chars.append(0x161C)  #uni161C	CANADIAN SYLLABICS CARRIER JJU
        chars.append(0x161D)  #uni161D	CANADIAN SYLLABICS CARRIER JJO
        chars.append(0x161E)  #uni161E	CANADIAN SYLLABICS CARRIER JJE
        chars.append(0x161F)  #uni161F	CANADIAN SYLLABICS CARRIER JJEE
        chars.append(0x1620)  #uni1620	CANADIAN SYLLABICS CARRIER JJI
        chars.append(0x1621)  #uni1621	CANADIAN SYLLABICS CARRIER JJA
        chars.append(0x1622)  #uni1622	CANADIAN SYLLABICS CARRIER LU
        chars.append(0x1623)  #uni1623	CANADIAN SYLLABICS CARRIER LO
        chars.append(0x1624)  #uni1624	CANADIAN SYLLABICS CARRIER LE
        chars.append(0x1625)  #uni1625	CANADIAN SYLLABICS CARRIER LEE
        chars.append(0x1626)  #uni1626	CANADIAN SYLLABICS CARRIER LI
        chars.append(0x1627)  #uni1627	CANADIAN SYLLABICS CARRIER LA
        chars.append(0x1628)  #uni1628	CANADIAN SYLLABICS CARRIER DLU
        chars.append(0x1629)  #uni1629	CANADIAN SYLLABICS CARRIER DLO
        chars.append(0x162A)  #uni162A	CANADIAN SYLLABICS CARRIER DLE
        chars.append(0x162B)  #uni162B	CANADIAN SYLLABICS CARRIER DLEE
        chars.append(0x162C)  #uni162C	CANADIAN SYLLABICS CARRIER DLI
        chars.append(0x162D)  #uni162D	CANADIAN SYLLABICS CARRIER DLA
        chars.append(0x162E)  #uni162E	CANADIAN SYLLABICS CARRIER LHU
        chars.append(0x162F)  #uni162F	CANADIAN SYLLABICS CARRIER LHO
        chars.append(0x1630)  #uni1630	CANADIAN SYLLABICS CARRIER LHE
        chars.append(0x1631)  #uni1631	CANADIAN SYLLABICS CARRIER LHEE
        chars.append(0x1632)  #uni1632	CANADIAN SYLLABICS CARRIER LHI
        chars.append(0x1633)  #uni1633	CANADIAN SYLLABICS CARRIER LHA
        chars.append(0x1634)  #uni1634	CANADIAN SYLLABICS CARRIER TLHU
        chars.append(0x1635)  #uni1635	CANADIAN SYLLABICS CARRIER TLHO
        chars.append(0x1636)  #uni1636	CANADIAN SYLLABICS CARRIER TLHE
        chars.append(0x1637)  #uni1637	CANADIAN SYLLABICS CARRIER TLHEE
        chars.append(0x1638)  #uni1638	CANADIAN SYLLABICS CARRIER TLHI
        chars.append(0x1639)  #uni1639	CANADIAN SYLLABICS CARRIER TLHA
        chars.append(0x163A)  #uni163A	CANADIAN SYLLABICS CARRIER TLU
        chars.append(0x163B)  #uni163B	CANADIAN SYLLABICS CARRIER TLO
        chars.append(0x163C)  #uni163C	CANADIAN SYLLABICS CARRIER TLE
        chars.append(0x163D)  #uni163D	CANADIAN SYLLABICS CARRIER TLEE
        chars.append(0x163E)  #uni163E	CANADIAN SYLLABICS CARRIER TLI
        chars.append(0x163F)  #uni163F	CANADIAN SYLLABICS CARRIER TLA
        chars.append(0x1640)  #uni1640	CANADIAN SYLLABICS CARRIER ZU
        chars.append(0x1641)  #uni1641	CANADIAN SYLLABICS CARRIER ZO
        chars.append(0x1642)  #uni1642	CANADIAN SYLLABICS CARRIER ZE
        chars.append(0x1643)  #uni1643	CANADIAN SYLLABICS CARRIER ZEE
        chars.append(0x1644)  #uni1644	CANADIAN SYLLABICS CARRIER ZI
        chars.append(0x1645)  #uni1645	CANADIAN SYLLABICS CARRIER ZA
        chars.append(0x1646)  #uni1646	CANADIAN SYLLABICS CARRIER Z
        chars.append(0x1647)  #uni1647	CANADIAN SYLLABICS CARRIER INITIAL Z
        chars.append(0x1648)  #uni1648	CANADIAN SYLLABICS CARRIER DZU
        chars.append(0x1649)  #uni1649	CANADIAN SYLLABICS CARRIER DZO
        chars.append(0x164A)  #uni164A	CANADIAN SYLLABICS CARRIER DZE
        chars.append(0x164B)  #uni164B	CANADIAN SYLLABICS CARRIER DZEE
        chars.append(0x164C)  #uni164C	CANADIAN SYLLABICS CARRIER DZI
        chars.append(0x164D)  #uni164D	CANADIAN SYLLABICS CARRIER DZA
        chars.append(0x164E)  #uni164E	CANADIAN SYLLABICS CARRIER SU
        chars.append(0x164F)  #uni164F	CANADIAN SYLLABICS CARRIER SO
        chars.append(0x1650)  #uni1650	CANADIAN SYLLABICS CARRIER SE
        chars.append(0x1651)  #uni1651	CANADIAN SYLLABICS CARRIER SEE
        chars.append(0x1652)  #uni1652	CANADIAN SYLLABICS CARRIER SI
        chars.append(0x1653)  #uni1653	CANADIAN SYLLABICS CARRIER SA
        chars.append(0x1654)  #uni1654	CANADIAN SYLLABICS CARRIER SHU
        chars.append(0x1655)  #uni1655	CANADIAN SYLLABICS CARRIER SHO
        chars.append(0x1656)  #uni1656	CANADIAN SYLLABICS CARRIER SHE
        chars.append(0x1657)  #uni1657	CANADIAN SYLLABICS CARRIER SHEE
        chars.append(0x1658)  #uni1658	CANADIAN SYLLABICS CARRIER SHI
        chars.append(0x1659)  #uni1659	CANADIAN SYLLABICS CARRIER SHA
        chars.append(0x165A)  #uni165A	CANADIAN SYLLABICS CARRIER SH
        chars.append(0x165B)  #uni165B	CANADIAN SYLLABICS CARRIER TSU
        chars.append(0x165C)  #uni165C	CANADIAN SYLLABICS CARRIER TSO
        chars.append(0x165D)  #uni165D	CANADIAN SYLLABICS CARRIER TSE
        chars.append(0x165E)  #uni165E	CANADIAN SYLLABICS CARRIER TSEE
        chars.append(0x165F)  #uni165F	CANADIAN SYLLABICS CARRIER TSI
        chars.append(0x1660)  #uni1660	CANADIAN SYLLABICS CARRIER TSA
        chars.append(0x1661)  #uni1661	CANADIAN SYLLABICS CARRIER CHU
        chars.append(0x1662)  #uni1662	CANADIAN SYLLABICS CARRIER CHO
        chars.append(0x1663)  #uni1663	CANADIAN SYLLABICS CARRIER CHE
        chars.append(0x1664)  #uni1664	CANADIAN SYLLABICS CARRIER CHEE
        chars.append(0x1665)  #uni1665	CANADIAN SYLLABICS CARRIER CHI
        chars.append(0x1666)  #uni1666	CANADIAN SYLLABICS CARRIER CHA
        chars.append(0x1667)  #uni1667	CANADIAN SYLLABICS CARRIER TTSU
        chars.append(0x1668)  #uni1668	CANADIAN SYLLABICS CARRIER TTSO
        chars.append(0x1669)  #uni1669	CANADIAN SYLLABICS CARRIER TTSE
        chars.append(0x166A)  #uni166A	CANADIAN SYLLABICS CARRIER TTSEE
        chars.append(0x166B)  #uni166B	CANADIAN SYLLABICS CARRIER TTSI
        chars.append(0x166C)  #uni166C	CANADIAN SYLLABICS CARRIER TTSA
        chars.append(0x166D)  #uni166D	CANADIAN SYLLABICS CHI SIGN
        chars.append(0x166E)  #uni166E	CANADIAN SYLLABICS FULL STOP
        chars.append(0x166F)  #uni166F	CANADIAN SYLLABICS QAI
        chars.append(0x1670)  #uni1670	CANADIAN SYLLABICS NGAI
        chars.append(0x1671)  #uni1671	CANADIAN SYLLABICS NNGI
        chars.append(0x1672)  #uni1672	CANADIAN SYLLABICS NNGII
        chars.append(0x1673)  #uni1673	CANADIAN SYLLABICS NNGO
        chars.append(0x1674)  #uni1674	CANADIAN SYLLABICS NNGOO
        chars.append(0x1675)  #uni1675	CANADIAN SYLLABICS NNGA
        chars.append(0x1676)  #uni1676	CANADIAN SYLLABICS NNGAA
        chars.append(0x1677)  #uni1677	CANADIAN SYLLABICS WOODS-CREE THWEE
        chars.append(0x1678)  #uni1678	CANADIAN SYLLABICS WOODS-CREE THWI
        chars.append(0x1679)  #uni1679	CANADIAN SYLLABICS WOODS-CREE THWII
        chars.append(0x167A)  #uni167A	CANADIAN SYLLABICS WOODS-CREE THWO
        chars.append(0x167B)  #uni167B	CANADIAN SYLLABICS WOODS-CREE THWOO
        chars.append(0x167C)  #uni167C	CANADIAN SYLLABICS WOODS-CREE THWA
        chars.append(0x167D)  #uni167D	CANADIAN SYLLABICS WOODS-CREE THWAA
        chars.append(0x167E)  #uni167E	CANADIAN SYLLABICS WOODS-CREE FINAL TH
        chars.append(0x167F)  #uni167F	CANADIAN SYLLABICS BLACKFOOT W
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


