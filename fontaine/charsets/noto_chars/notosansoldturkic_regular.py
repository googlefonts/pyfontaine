# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansOldTurkic-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x000D)  #uni000D	????
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x10C00)  #glyph00004	OLD TURKIC LETTER ORKHON A
        chars.append(0x10C02)  #glyph00006	OLD TURKIC LETTER YENISEI AE
        chars.append(0x10C03)  #glyph00007	OLD TURKIC LETTER ORKHON I
        chars.append(0x10C04)  #glyph00008	OLD TURKIC LETTER YENISEI I
        chars.append(0x10C05)  #glyph00009	OLD TURKIC LETTER YENISEI E
        chars.append(0x10C06)  #glyph00010	OLD TURKIC LETTER ORKHON O
        chars.append(0x10C01)  #glyph00005	OLD TURKIC LETTER YENISEI A
        chars.append(0x10C08)  #glyph00012	OLD TURKIC LETTER YENISEI OE
        chars.append(0x10C09)  #glyph00013	OLD TURKIC LETTER ORKHON AB
        chars.append(0x10C0A)  #glyph00014	OLD TURKIC LETTER YENISEI AB
        chars.append(0x10C0B)  #glyph00015	OLD TURKIC LETTER ORKHON AEB
        chars.append(0x10C0C)  #glyph00016	OLD TURKIC LETTER YENISEI AEB
        chars.append(0x000D)  #uni000D	????
        chars.append(0x10C0E)  #glyph00018	OLD TURKIC LETTER YENISEI AG
        chars.append(0x10C0F)  #glyph00019	OLD TURKIC LETTER ORKHON AEG
        chars.append(0x10C10)  #glyph00020	OLD TURKIC LETTER YENISEI AEG
        chars.append(0x10C11)  #glyph00021	OLD TURKIC LETTER ORKHON AD
        chars.append(0x10C12)  #glyph00022	OLD TURKIC LETTER YENISEI AD
        chars.append(0x10C13)  #glyph00023	OLD TURKIC LETTER ORKHON AED
        chars.append(0x10C14)  #glyph00024	OLD TURKIC LETTER ORKHON EZ
        chars.append(0x10C15)  #glyph00025	OLD TURKIC LETTER YENISEI EZ
        chars.append(0x10C16)  #glyph00026	OLD TURKIC LETTER ORKHON AY
        chars.append(0x10C17)  #glyph00027	OLD TURKIC LETTER YENISEI AY
        chars.append(0x10C18)  #glyph00028	OLD TURKIC LETTER ORKHON AEY
        chars.append(0x10C19)  #glyph00029	OLD TURKIC LETTER YENISEI AEY
        chars.append(0x10C1A)  #glyph00030	OLD TURKIC LETTER ORKHON AEK
        chars.append(0x10C1B)  #glyph00031	OLD TURKIC LETTER YENISEI AEK
        chars.append(0x10C1C)  #glyph00032	OLD TURKIC LETTER ORKHON OEK
        chars.append(0x10C1D)  #glyph00033	OLD TURKIC LETTER YENISEI OEK
        chars.append(0x10C1E)  #glyph00034	OLD TURKIC LETTER ORKHON AL
        chars.append(0x10C1F)  #glyph00035	OLD TURKIC LETTER YENISEI AL
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x10C21)  #glyph00037	OLD TURKIC LETTER ORKHON ELT
        chars.append(0x10C22)  #glyph00038	OLD TURKIC LETTER ORKHON EM
        chars.append(0x10C23)  #glyph00039	OLD TURKIC LETTER ORKHON AN
        chars.append(0x10C24)  #glyph00040	OLD TURKIC LETTER ORKHON AEN
        chars.append(0x10C25)  #glyph00041	OLD TURKIC LETTER YENISEI AEN
        chars.append(0x10C26)  #glyph00042	OLD TURKIC LETTER ORKHON ENT
        chars.append(0x10C20)  #glyph00036	OLD TURKIC LETTER ORKHON AEL
        chars.append(0x10C28)  #glyph00044	OLD TURKIC LETTER ORKHON ENC
        chars.append(0x10C29)  #glyph00045	OLD TURKIC LETTER YENISEI ENC
        chars.append(0x10C2A)  #glyph00046	OLD TURKIC LETTER ORKHON ENY
        chars.append(0x10C07)  #glyph00011	OLD TURKIC LETTER ORKHON OE
        chars.append(0x10C2C)  #glyph00048	OLD TURKIC LETTER YENISEI ANG
        chars.append(0x10C2D)  #glyph00049	OLD TURKIC LETTER ORKHON ENG
        chars.append(0x10C2E)  #glyph00050	OLD TURKIC LETTER YENISEI AENG
        chars.append(0x10C2F)  #glyph00051	OLD TURKIC LETTER ORKHON EP
        chars.append(0x10C30)  #glyph00052	OLD TURKIC LETTER ORKHON OP
        chars.append(0x10C31)  #glyph00053	OLD TURKIC LETTER ORKHON IC
        chars.append(0x10C32)  #glyph00054	OLD TURKIC LETTER ORKHON EC
        chars.append(0x10C33)  #glyph00055	OLD TURKIC LETTER YENISEI EC
        chars.append(0x10C34)  #glyph00056	OLD TURKIC LETTER ORKHON AQ
        chars.append(0x10C35)  #glyph00057	OLD TURKIC LETTER YENISEI AQ
        chars.append(0x10C36)  #glyph00058	OLD TURKIC LETTER ORKHON IQ
        chars.append(0x10C37)  #glyph00059	OLD TURKIC LETTER YENISEI IQ
        chars.append(0x10C38)  #glyph00060	OLD TURKIC LETTER ORKHON OQ
        chars.append(0x10C39)  #glyph00061	OLD TURKIC LETTER YENISEI OQ
        chars.append(0x10C3A)  #glyph00062	OLD TURKIC LETTER ORKHON AR
        chars.append(0x10C3B)  #glyph00063	OLD TURKIC LETTER YENISEI AR
        chars.append(0x10C3C)  #glyph00064	OLD TURKIC LETTER ORKHON AER
        chars.append(0x10C3D)  #glyph00065	OLD TURKIC LETTER ORKHON AS
        chars.append(0x10C3E)  #glyph00066	OLD TURKIC LETTER ORKHON AES
        chars.append(0x10C3F)  #glyph00067	OLD TURKIC LETTER ORKHON ASH
        chars.append(0x10C40)  #glyph00068	OLD TURKIC LETTER YENISEI ASH
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x10C42)  #glyph00070	OLD TURKIC LETTER YENISEI ESH
        chars.append(0x10C43)  #glyph00071	OLD TURKIC LETTER ORKHON AT
        chars.append(0x10C44)  #glyph00072	OLD TURKIC LETTER YENISEI AT
        chars.append(0x10C45)  #glyph00073	OLD TURKIC LETTER ORKHON AET
        chars.append(0x10C46)  #glyph00074	OLD TURKIC LETTER YENISEI AET
        chars.append(0x10C47)  #glyph00075	OLD TURKIC LETTER ORKHON OT
        chars.append(0x10C48)  #glyph00076	OLD TURKIC LETTER ORKHON BASH
        chars.append(0x10C0D)  #glyph00017	OLD TURKIC LETTER ORKHON AG
        chars.append(0x10C41)  #glyph00069	OLD TURKIC LETTER ORKHON ESH
        chars.append(0x10C27)  #glyph00043	OLD TURKIC LETTER YENISEI ENT
        chars.append(0x10C2B)  #glyph00047	OLD TURKIC LETTER YENISEI ENY
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        return chars


