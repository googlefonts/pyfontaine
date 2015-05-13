# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansTaiTham-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x200B)  #uni200B	ZERO WIDTH SPACE
        chars.append(0x200C)  #uni200C	ZERO WIDTH NON-JOINER
        chars.append(0x000D)  #uni000D	????
        chars.append(0x2219)  #uni2219	BULLET OPERATOR
        chars.append(0x1A20)  #uni1A20	TAI THAM LETTER HIGH KA
        chars.append(0x1A21)  #uni1A21	TAI THAM LETTER HIGH KHA
        chars.append(0x1A22)  #uni1A22	TAI THAM LETTER HIGH KXA
        chars.append(0x1A23)  #uni1A23	TAI THAM LETTER LOW KA
        chars.append(0x1A24)  #uni1A24	TAI THAM LETTER LOW KXA
        chars.append(0x1A25)  #uni1A25	TAI THAM LETTER LOW KHA
        chars.append(0x1A26)  #uni1A26	TAI THAM LETTER NGA
        chars.append(0x1A27)  #uni1A27	TAI THAM LETTER HIGH CA
        chars.append(0x1A28)  #uni1A28	TAI THAM LETTER HIGH CHA
        chars.append(0x1A29)  #uni1A29	TAI THAM LETTER LOW CA
        chars.append(0x1A2A)  #uni1A2A	TAI THAM LETTER LOW SA
        chars.append(0x1A2B)  #uni1A2B	TAI THAM LETTER LOW CHA
        chars.append(0x1A2C)  #uni1A2C	TAI THAM LETTER NYA
        chars.append(0x1A2D)  #uni1A2D	TAI THAM LETTER RATA
        chars.append(0x1A2E)  #uni1A2E	TAI THAM LETTER HIGH RATHA
        chars.append(0x1A2F)  #uni1A2F	TAI THAM LETTER DA
        chars.append(0x1A30)  #uni1A30	TAI THAM LETTER LOW RATHA
        chars.append(0x1A31)  #uni1A31	TAI THAM LETTER RANA
        chars.append(0x1A32)  #uni1A32	TAI THAM LETTER HIGH TA
        chars.append(0x1A33)  #uni1A33	TAI THAM LETTER HIGH THA
        chars.append(0x1A34)  #uni1A34	TAI THAM LETTER LOW TA
        chars.append(0x1A35)  #uni1A35	TAI THAM LETTER LOW THA
        chars.append(0x1A36)  #uni1A36	TAI THAM LETTER NA
        chars.append(0x1A37)  #uni1A37	TAI THAM LETTER BA
        chars.append(0x1A38)  #uni1A38	TAI THAM LETTER HIGH PA
        chars.append(0x1A39)  #uni1A39	TAI THAM LETTER HIGH PHA
        chars.append(0x1A3A)  #uni1A3A	TAI THAM LETTER HIGH FA
        chars.append(0x1A3B)  #uni1A3B	TAI THAM LETTER LOW PA
        chars.append(0x1A3C)  #uni1A3C	TAI THAM LETTER LOW FA
        chars.append(0x1A3D)  #uni1A3D	TAI THAM LETTER LOW PHA
        chars.append(0x1A3E)  #uni1A3E	TAI THAM LETTER MA
        chars.append(0x1A3F)  #uni1A3F	TAI THAM LETTER LOW YA
        chars.append(0x1A40)  #uni1A40	TAI THAM LETTER HIGH YA
        chars.append(0x1A41)  #uni1A41	TAI THAM LETTER RA
        chars.append(0x1A42)  #uni1A42	TAI THAM LETTER RUE
        chars.append(0x1A43)  #uni1A43	TAI THAM LETTER LA
        chars.append(0x1A44)  #uni1A44	TAI THAM LETTER LUE
        chars.append(0x1A45)  #uni1A45	TAI THAM LETTER WA
        chars.append(0x1A46)  #uni1A46	TAI THAM LETTER HIGH SHA
        chars.append(0x1A47)  #uni1A47	TAI THAM LETTER HIGH SSA
        chars.append(0x1A48)  #uni1A48	TAI THAM LETTER HIGH SA
        chars.append(0x1A49)  #uni1A49	TAI THAM LETTER HIGH HA
        chars.append(0x1A4A)  #uni1A4A	TAI THAM LETTER LLA
        chars.append(0x1A4B)  #uni1A4B	TAI THAM LETTER A
        chars.append(0x1A4C)  #uni1A4C	TAI THAM LETTER LOW HA
        chars.append(0x1A4D)  #uni1A4D	TAI THAM LETTER I
        chars.append(0x1A4E)  #uni1A4E	TAI THAM LETTER II
        chars.append(0x1A4F)  #uni1A4F	TAI THAM LETTER U
        chars.append(0x1A50)  #uni1A50	TAI THAM LETTER UU
        chars.append(0x1A51)  #uni1A51	TAI THAM LETTER EE
        chars.append(0x1A52)  #uni1A52	TAI THAM LETTER OO
        chars.append(0x1A53)  #uni1A53	TAI THAM LETTER LAE
        chars.append(0x1A54)  #uni1A54	TAI THAM LETTER GREAT SA
        chars.append(0x1A55)  #uni1A55	TAI THAM CONSONANT SIGN MEDIAL RA
        chars.append(0x1A56)  #uni1A56	TAI THAM CONSONANT SIGN MEDIAL LA
        chars.append(0x1A57)  #uni1A57	TAI THAM CONSONANT SIGN LA TANG LAI
        chars.append(0x1A58)  #uni1A58	TAI THAM SIGN MAI KANG LAI
        chars.append(0x1A59)  #uni1A59	TAI THAM CONSONANT SIGN FINAL NGA
        chars.append(0x1A5A)  #uni1A5A	TAI THAM CONSONANT SIGN LOW PA
        chars.append(0x1A5B)  #uni1A5B	TAI THAM CONSONANT SIGN HIGH RATHA OR LOW PA
        chars.append(0x1A5C)  #uni1A5C	TAI THAM CONSONANT SIGN MA
        chars.append(0x1A5D)  #uni1A5D	TAI THAM CONSONANT SIGN BA
        chars.append(0x1A5E)  #uni1A5E	TAI THAM CONSONANT SIGN SA
        chars.append(0x1A60)  #uni1A60	TAI THAM SIGN SAKOT
        chars.append(0x1A61)  #uni1A61	TAI THAM VOWEL SIGN A
        chars.append(0x1A62)  #uni1A62	TAI THAM VOWEL SIGN MAI SAT
        chars.append(0x1A63)  #uni1A63	TAI THAM VOWEL SIGN AA
        chars.append(0x1A64)  #uni1A64	TAI THAM VOWEL SIGN TALL AA
        chars.append(0x1A65)  #uni1A65	TAI THAM VOWEL SIGN I
        chars.append(0x1A66)  #uni1A66	TAI THAM VOWEL SIGN II
        chars.append(0x1A67)  #uni1A67	TAI THAM VOWEL SIGN UE
        chars.append(0x1A68)  #uni1A68	TAI THAM VOWEL SIGN UUE
        chars.append(0x1A69)  #uni1A69	TAI THAM VOWEL SIGN U
        chars.append(0x1A6A)  #uni1A6A	TAI THAM VOWEL SIGN UU
        chars.append(0x1A6B)  #uni1A6B	TAI THAM VOWEL SIGN O
        chars.append(0x1A6C)  #uni1A6C	TAI THAM VOWEL SIGN OA BELOW
        chars.append(0x1A6D)  #uni1A6D	TAI THAM VOWEL SIGN OY
        chars.append(0x1A6E)  #uni1A6E	TAI THAM VOWEL SIGN E
        chars.append(0x1A6F)  #uni1A6F	TAI THAM VOWEL SIGN AE
        chars.append(0x1A70)  #uni1A70	TAI THAM VOWEL SIGN OO
        chars.append(0x1A71)  #uni1A71	TAI THAM VOWEL SIGN AI
        chars.append(0x1A72)  #uni1A72	TAI THAM VOWEL SIGN THAM AI
        chars.append(0x1A73)  #uni1A73	TAI THAM VOWEL SIGN OA ABOVE
        chars.append(0x1A74)  #uni1A74	TAI THAM SIGN MAI KANG
        chars.append(0x1A75)  #uni1A75	TAI THAM SIGN TONE-1
        chars.append(0x1A76)  #uni1A76	TAI THAM SIGN TONE-2
        chars.append(0x1A77)  #uni1A77	TAI THAM SIGN KHUEN TONE-3
        chars.append(0x1A78)  #uni1A78	TAI THAM SIGN KHUEN TONE-4
        chars.append(0x1A79)  #uni1A79	TAI THAM SIGN KHUEN TONE-5
        chars.append(0x1A7A)  #uni1A7A	TAI THAM SIGN RA HAAM
        chars.append(0x1A7B)  #uni1A7B	TAI THAM SIGN MAI SAM
        chars.append(0x1A7C)  #uni1A7C	TAI THAM SIGN KHUEN-LUE KARAN
        chars.append(0x1A7F)  #uni1A7F	TAI THAM COMBINING CRYPTOGRAMMIC DOT
        chars.append(0x1A80)  #uni1A80	TAI THAM HORA DIGIT ZERO
        chars.append(0x1A81)  #uni1A81	TAI THAM HORA DIGIT ONE
        chars.append(0x1A82)  #uni1A82	TAI THAM HORA DIGIT TWO
        chars.append(0x1A83)  #uni1A83	TAI THAM HORA DIGIT THREE
        chars.append(0x1A84)  #uni1A84	TAI THAM HORA DIGIT FOUR
        chars.append(0x1A85)  #uni1A85	TAI THAM HORA DIGIT FIVE
        chars.append(0x1A86)  #uni1A86	TAI THAM HORA DIGIT SIX
        chars.append(0x1A87)  #uni1A87	TAI THAM HORA DIGIT SEVEN
        chars.append(0x1A88)  #uni1A88	TAI THAM HORA DIGIT EIGHT
        chars.append(0x1A89)  #uni1A89	TAI THAM HORA DIGIT NINE
        chars.append(0x200D)  #uni200D	ZERO WIDTH JOINER
        chars.append(0x1A90)  #uni1A90	TAI THAM THAM DIGIT ZERO
        chars.append(0x1A91)  #uni1A91	TAI THAM THAM DIGIT ONE
        chars.append(0x1A92)  #uni1A92	TAI THAM THAM DIGIT TWO
        chars.append(0x1A93)  #uni1A93	TAI THAM THAM DIGIT THREE
        chars.append(0x1A94)  #uni1A94	TAI THAM THAM DIGIT FOUR
        chars.append(0x1A95)  #uni1A95	TAI THAM THAM DIGIT FIVE
        chars.append(0x1A96)  #uni1A96	TAI THAM THAM DIGIT SIX
        chars.append(0x1A97)  #uni1A97	TAI THAM THAM DIGIT SEVEN
        chars.append(0x1A98)  #uni1A98	TAI THAM THAM DIGIT EIGHT
        chars.append(0x1A99)  #uni1A99	TAI THAM THAM DIGIT NINE
        chars.append(0x00A0)  #space	NO-BREAK SPACE
        chars.append(0x1AA1)  #uni1AA1	TAI THAM SIGN WIANGWAAK
        chars.append(0x1AA2)  #uni1AA2	TAI THAM SIGN SAWAN
        chars.append(0x1AA3)  #uni1AA3	TAI THAM SIGN KEOW
        chars.append(0x1AA4)  #uni1AA4	TAI THAM SIGN HOY
        chars.append(0x1AA5)  #uni1AA5	TAI THAM SIGN DOKMAI
        chars.append(0x1AA6)  #uni1AA6	TAI THAM SIGN REVERSED ROTATED RANA
        chars.append(0x1AA7)  #uni1AA7	TAI THAM SIGN MAI YAMOK
        chars.append(0x1AA8)  #uni1AA8	TAI THAM SIGN KAAN
        chars.append(0x1AA9)  #uni1AA9	TAI THAM SIGN KAANKUU
        chars.append(0x1AAA)  #uni1AAA	TAI THAM SIGN SATKAAN
        chars.append(0x1AAB)  #uni1AAB	TAI THAM SIGN SATKAANKUU
        chars.append(0x1AAC)  #uni1AAC	TAI THAM SIGN HANG
        chars.append(0x1AAD)  #uni1AAD	TAI THAM SIGN CAANG
        chars.append(0x0020)  #space	SPACE
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x1AA0)  #uni1AA0	TAI THAM SIGN WIANG
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        return chars


