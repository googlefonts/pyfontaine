# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansHebrew-Bold'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #null	????
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #nonmarkingreturn	????
        chars.append(0x200E)  #uni200E	LEFT-TO-RIGHT MARK
        chars.append(0x200F)  #uni200F	RIGHT-TO-LEFT MARK
        chars.append(0x0020)  #space	SPACE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x00A0)  #space	NO-BREAK SPACE
        chars.append(0x20AA)  #sheqel	NEW SHEQEL SIGN
        chars.append(0xFEFF)  #null	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xFB1D)  #uniFB1D	HEBREW LETTER YOD WITH HIRIQ
        chars.append(0xFB1E)  #uniFB1E	HEBREW POINT JUDEO-SPANISH VARIKA
        chars.append(0xFB1F)  #yodyod_patah	HEBREW LIGATURE YIDDISH YOD YOD PATAH
        chars.append(0xFB20)  #alternativeayin	HEBREW LETTER ALTERNATIVE AYIN
        chars.append(0xFB21)  #alefwide	HEBREW LETTER WIDE ALEF
        chars.append(0xFB22)  #daletwide	HEBREW LETTER WIDE DALET
        chars.append(0xFB23)  #hewide	HEBREW LETTER WIDE HE
        chars.append(0xFB24)  #kafwide	HEBREW LETTER WIDE KAF
        chars.append(0xFB25)  #lamedwide	HEBREW LETTER WIDE LAMED
        chars.append(0xFB26)  #finalmemwide	HEBREW LETTER WIDE FINAL MEM
        chars.append(0xFB27)  #reshwide	HEBREW LETTER WIDE RESH
        chars.append(0xFB28)  #tavwide	HEBREW LETTER WIDE TAV
        chars.append(0xFB29)  #alt_plussign	HEBREW LETTER ALTERNATIVE PLUS SIGN
        chars.append(0xFB2A)  #shinshindot	HEBREW LETTER SHIN WITH SHIN DOT
        chars.append(0xFB2B)  #shinsindot	HEBREW LETTER SHIN WITH SIN DOT
        chars.append(0xFB2C)  #shindageshshindot	HEBREW LETTER SHIN WITH DAGESH AND SHIN DOT
        chars.append(0xFB2D)  #shindageshsindot	HEBREW LETTER SHIN WITH DAGESH AND SIN DOT
        chars.append(0xFB2E)  #alefpatah	HEBREW LETTER ALEF WITH PATAH
        chars.append(0xFB2F)  #alefqamats	HEBREW LETTER ALEF WITH QAMATS
        chars.append(0xFB30)  #alefmapiq	HEBREW LETTER ALEF WITH MAPIQ
        chars.append(0xFB31)  #betdagesh	HEBREW LETTER BET WITH DAGESH
        chars.append(0xFB32)  #gimeldagesh	HEBREW LETTER GIMEL WITH DAGESH
        chars.append(0xFB33)  #daletdagesh	HEBREW LETTER DALET WITH DAGESH
        chars.append(0xFB34)  #hedagesh	HEBREW LETTER HE WITH MAPIQ
        chars.append(0xFB35)  #vavdagesh	HEBREW LETTER VAV WITH DAGESH
        chars.append(0xFB36)  #zayindagesh	HEBREW LETTER ZAYIN WITH DAGESH
        chars.append(0xFB38)  #tetdagesh	HEBREW LETTER TET WITH DAGESH
        chars.append(0xFB39)  #yoddagesh	HEBREW LETTER YOD WITH DAGESH
        chars.append(0xFB3A)  #finalkafdagesh	HEBREW LETTER FINAL KAF WITH DAGESH
        chars.append(0xFB3B)  #kafdagesh	HEBREW LETTER KAF WITH DAGESH
        chars.append(0xFB3C)  #lameddagesh	HEBREW LETTER LAMED WITH DAGESH
        chars.append(0xFB3E)  #memdagesh	HEBREW LETTER MEM WITH DAGESH
        chars.append(0xFB40)  #nundagesh	HEBREW LETTER NUN WITH DAGESH
        chars.append(0xFB41)  #samekhdagesh	HEBREW LETTER SAMEKH WITH DAGESH
        chars.append(0xFB43)  #finalpedagesh	HEBREW LETTER FINAL PE WITH DAGESH
        chars.append(0xFB44)  #pedagesh	HEBREW LETTER PE WITH DAGESH
        chars.append(0xFB46)  #tsadidagesh	HEBREW LETTER TSADI WITH DAGESH
        chars.append(0xFB47)  #qofdagesh	HEBREW LETTER QOF WITH DAGESH
        chars.append(0xFB48)  #reshdagesh	HEBREW LETTER RESH WITH DAGESH
        chars.append(0xFB49)  #shindagesh	HEBREW LETTER SHIN WITH DAGESH
        chars.append(0xFB4A)  #tavdagesh	HEBREW LETTER TAV WITH DAGESH
        chars.append(0xFB4B)  #vavholam	HEBREW LETTER VAV WITH HOLAM
        chars.append(0xFB4C)  #betrafe	HEBREW LETTER BET WITH RAFE
        chars.append(0xFB4D)  #kafrafe	HEBREW LETTER KAF WITH RAFE
        chars.append(0xFB4E)  #perafe	HEBREW LETTER PE WITH RAFE
        chars.append(0xFB4F)  #aleflamed	HEBREW LIGATURE ALEF LAMED
        chars.append(0x0591)  #uni0591	HEBREW ACCENT ETNAHTA
        chars.append(0x0592)  #uni0592	HEBREW ACCENT SEGOL
        chars.append(0x0593)  #uni0593	HEBREW ACCENT SHALSHELET
        chars.append(0x0594)  #uni0594	HEBREW ACCENT ZAQEF QATAN
        chars.append(0x0595)  #uni0595	HEBREW ACCENT ZAQEF GADOL
        chars.append(0x0596)  #uni0596	HEBREW ACCENT TIPEHA
        chars.append(0x0597)  #uni0597	HEBREW ACCENT REVIA
        chars.append(0x0598)  #uni0598	HEBREW ACCENT ZARQA
        chars.append(0x0599)  #uni0599	HEBREW ACCENT PASHTA
        chars.append(0x059A)  #uni059A	HEBREW ACCENT YETIV
        chars.append(0x059B)  #uni059B	HEBREW ACCENT TEVIR
        chars.append(0x059C)  #uni059C	HEBREW ACCENT GERESH
        chars.append(0x059D)  #uni059D	HEBREW ACCENT GERESH MUQDAM
        chars.append(0x059E)  #uni059E	HEBREW ACCENT GERSHAYIM
        chars.append(0x059F)  #uni059F	HEBREW ACCENT QARNEY PARA
        chars.append(0x05A0)  #uni05A0	HEBREW ACCENT TELISHA GEDOLA
        chars.append(0x05A1)  #uni05A1	HEBREW ACCENT PAZER
        chars.append(0x05A2)  #uni05A2	HEBREW ACCENT ATNAH HAFUKH
        chars.append(0x05A3)  #uni05A3	HEBREW ACCENT MUNAH
        chars.append(0x05A4)  #uni05A4	HEBREW ACCENT MAHAPAKH
        chars.append(0x05A5)  #uni05A5	HEBREW ACCENT MERKHA
        chars.append(0x05A6)  #uni05A6	HEBREW ACCENT MERKHA KEFULA
        chars.append(0x05A7)  #uni05A7	HEBREW ACCENT DARGA
        chars.append(0x05A8)  #uni05A8	HEBREW ACCENT QADMA
        chars.append(0x05A9)  #uni05A9	HEBREW ACCENT TELISHA QETANA
        chars.append(0x05AA)  #uni05AA	HEBREW ACCENT YERAH BEN YOMO
        chars.append(0x05AB)  #uni05AB	HEBREW ACCENT OLE
        chars.append(0x05AC)  #uni05AC	HEBREW ACCENT ILUY
        chars.append(0x05AD)  #uni05AD	HEBREW ACCENT DEHI
        chars.append(0x05AE)  #uni05AE	HEBREW ACCENT ZINOR
        chars.append(0x05AF)  #uni05AF	HEBREW MARK MASORA CIRCLE
        chars.append(0x05B0)  #sheva	HEBREW POINT SHEVA
        chars.append(0x05B1)  #hatafsegol	HEBREW POINT HATAF SEGOL
        chars.append(0x05B2)  #hatafpatah	HEBREW POINT HATAF PATAH
        chars.append(0x05B3)  #hatafqamats	HEBREW POINT HATAF QAMATS
        chars.append(0x05B4)  #hiriq	HEBREW POINT HIRIQ
        chars.append(0x05B5)  #tsere	HEBREW POINT TSERE
        chars.append(0x05B6)  #segol	HEBREW POINT SEGOL
        chars.append(0x05B7)  #patah	HEBREW POINT PATAH
        chars.append(0x05B8)  #qamats	HEBREW POINT QAMATS
        chars.append(0x05B9)  #holam	HEBREW POINT HOLAM
        chars.append(0x05BA)  #uni05BA	HEBREW POINT HOLAM HASER FOR VAV
        chars.append(0x05BB)  #qubuts	HEBREW POINT QUBUTS
        chars.append(0x05BC)  #dagesh	HEBREW POINT DAGESH OR MAPIQ
        chars.append(0x05BD)  #meteg	HEBREW POINT METEG
        chars.append(0x05BE)  #maqaf	HEBREW PUNCTUATION MAQAF
        chars.append(0x05BF)  #rafe	HEBREW POINT RAFE
        chars.append(0x05C0)  #paseq	HEBREW PUNCTUATION PASEQ
        chars.append(0x05C1)  #shindot	HEBREW POINT SHIN DOT
        chars.append(0x05C2)  #sindot	HEBREW POINT SIN DOT
        chars.append(0x05C3)  #sofpasuq	HEBREW PUNCTUATION SOF PASUQ
        chars.append(0x05C4)  #upper_dot	HEBREW MARK UPPER DOT
        chars.append(0x05C5)  #lowerdot	HEBREW MARK LOWER DOT
        chars.append(0x05C6)  #uni05C6	HEBREW PUNCTUATION NUN HAFUKHA
        chars.append(0x05C7)  #qamatsqatan	HEBREW POINT QAMATS QATAN
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x05D0)  #alef	HEBREW LETTER ALEF
        chars.append(0x05D1)  #bet	HEBREW LETTER BET
        chars.append(0x05D2)  #gimel	HEBREW LETTER GIMEL
        chars.append(0x05D3)  #dalet	HEBREW LETTER DALET
        chars.append(0x05D4)  #he	HEBREW LETTER HE
        chars.append(0x05D5)  #vav	HEBREW LETTER VAV
        chars.append(0x05D6)  #zayin	HEBREW LETTER ZAYIN
        chars.append(0x05D7)  #het	HEBREW LETTER HET
        chars.append(0x05D8)  #tet	HEBREW LETTER TET
        chars.append(0x05D9)  #yod	HEBREW LETTER YOD
        chars.append(0x05DA)  #finalkaf	HEBREW LETTER FINAL KAF
        chars.append(0x05DB)  #kaf	HEBREW LETTER KAF
        chars.append(0x05DC)  #lamed	HEBREW LETTER LAMED
        chars.append(0x05DD)  #finalmem	HEBREW LETTER FINAL MEM
        chars.append(0x05DE)  #mem	HEBREW LETTER MEM
        chars.append(0x05DF)  #finalnun	HEBREW LETTER FINAL NUN
        chars.append(0x05E0)  #nun	HEBREW LETTER NUN
        chars.append(0x05E1)  #samekh	HEBREW LETTER SAMEKH
        chars.append(0x05E2)  #ayin	HEBREW LETTER AYIN
        chars.append(0x05E3)  #finalpe	HEBREW LETTER FINAL PE
        chars.append(0x05E4)  #pe	HEBREW LETTER PE
        chars.append(0x05E5)  #finaltsadi	HEBREW LETTER FINAL TSADI
        chars.append(0x05E6)  #tsadi	HEBREW LETTER TSADI
        chars.append(0x05E7)  #qof	HEBREW LETTER QOF
        chars.append(0x05E8)  #resh	HEBREW LETTER RESH
        chars.append(0x05E9)  #shin	HEBREW LETTER SHIN
        chars.append(0x05EA)  #tav	HEBREW LETTER TAV
        chars.append(0x05F0)  #vavvav	HEBREW LIGATURE YIDDISH DOUBLE VAV
        chars.append(0x05F1)  #vavyod	HEBREW LIGATURE YIDDISH VAV YOD
        chars.append(0x05F2)  #yodyod	HEBREW LIGATURE YIDDISH DOUBLE YOD
        chars.append(0x05F3)  #geresh	HEBREW PUNCTUATION GERESH
        chars.append(0x05F4)  #gershayim	HEBREW PUNCTUATION GERSHAYIM
        return chars


