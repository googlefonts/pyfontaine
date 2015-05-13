# -*- coding: utf-8 -*-


class Charset(object):
    common_name = 'NotoSansSymbols-Regular'
    native_name = ''

    def glyphs(self):
        chars = []
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x000D)  #uni000D	????
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x20A0)  #uni20A0	EURO-CURRENCY SIGN
        chars.append(0x20A1)  #colonmonetary	COLON SIGN
        chars.append(0x20A2)  #uni20A2	CRUZEIRO SIGN
        chars.append(0x20A3)  #franc	FRENCH FRANC SIGN
        chars.append(0x20A4)  #lira	LIRA SIGN
        chars.append(0x20A5)  #uni20A5	MILL SIGN
        chars.append(0x20A6)  #uni20A6	NAIRA SIGN
        chars.append(0x20A7)  #peseta	PESETA SIGN
        chars.append(0x20A8)  #uni20A8	RUPEE SIGN
        chars.append(0x20A9)  #uni20A9	WON SIGN
        chars.append(0x20AA)  #uni20AA	NEW SHEQEL SIGN
        chars.append(0x20AB)  #dong	DONG SIGN
        chars.append(0x20AC)  #Euro	EURO SIGN
        chars.append(0x20AD)  #uni20AD	KIP SIGN
        chars.append(0x20AE)  #uni20AE	TUGRIK SIGN
        chars.append(0x20AF)  #uni20AF	DRACHMA SIGN
        chars.append(0x20B0)  #uni20B0	GERMAN PENNY SIGN
        chars.append(0x20B1)  #uni20B1	PESO SIGN
        chars.append(0x20B2)  #uni20B2	GUARANI SIGN
        chars.append(0x20B3)  #uni20B3	AUSTRAL SIGN
        chars.append(0x20B4)  #uni20B4	HRYVNIA SIGN
        chars.append(0x20B5)  #uni20B5	CEDI SIGN
        chars.append(0x20B6)  #uni20B6	LIVRE TOURNOIS SIGN
        chars.append(0x20B7)  #uni20B7	SPESMILO SIGN
        chars.append(0x20B8)  #uni20B8	TENGE SIGN
        chars.append(0x20B9)  #uni20B9	????
        chars.append(0x20BA)  #uni20BA	????
        chars.append(0x20BC)  #uni20BC	????
        chars.append(0x20BD)  #uni20BD	????
        chars.append(0x20BE)  #uni20BE	????
        chars.append(0x20D0)  #uni20D0	COMBINING LEFT HARPOON ABOVE
        chars.append(0x20D1)  #uni20D1	COMBINING RIGHT HARPOON ABOVE
        chars.append(0x20D2)  #uni20D2	COMBINING LONG VERTICAL LINE OVERLAY
        chars.append(0x20D3)  #uni20D3	COMBINING SHORT VERTICAL LINE OVERLAY
        chars.append(0x20D4)  #uni20D4	COMBINING ANTICLOCKWISE ARROW ABOVE
        chars.append(0x20D5)  #uni20D5	COMBINING CLOCKWISE ARROW ABOVE
        chars.append(0x20D6)  #uni20D6	COMBINING LEFT ARROW ABOVE
        chars.append(0x20D7)  #uni20D7	COMBINING RIGHT ARROW ABOVE
        chars.append(0x20D8)  #uni20D8	COMBINING RING OVERLAY
        chars.append(0x20D9)  #uni20D9	COMBINING CLOCKWISE RING OVERLAY
        chars.append(0x20DA)  #uni20DA	COMBINING ANTICLOCKWISE RING OVERLAY
        chars.append(0x20DB)  #uni20DB	COMBINING THREE DOTS ABOVE
        chars.append(0x20DC)  #uni20DC	COMBINING FOUR DOTS ABOVE
        chars.append(0x20DD)  #uni20DD	COMBINING ENCLOSING CIRCLE
        chars.append(0x20DE)  #uni20DE	COMBINING ENCLOSING SQUARE
        chars.append(0x20DF)  #uni20DF	COMBINING ENCLOSING DIAMOND
        chars.append(0x20E0)  #uni20E0	COMBINING ENCLOSING CIRCLE BACKSLASH
        chars.append(0x20E1)  #uni20E1	COMBINING LEFT RIGHT ARROW ABOVE
        chars.append(0x20E2)  #uni20E2	COMBINING ENCLOSING SCREEN
        chars.append(0x20E3)  #uni20E3	COMBINING ENCLOSING KEYCAP
        chars.append(0x20E4)  #uni20E4	COMBINING ENCLOSING UPWARD POINTING TRIANGLE
        chars.append(0x20E5)  #uni20E5	COMBINING REVERSE SOLIDUS OVERLAY
        chars.append(0x20E6)  #uni20E6	COMBINING DOUBLE VERTICAL STROKE OVERLAY
        chars.append(0x20E7)  #uni20E7	COMBINING ANNUITY SYMBOL
        chars.append(0x20E8)  #uni20E8	COMBINING TRIPLE UNDERDOT
        chars.append(0x20E9)  #uni20E9	COMBINING WIDE BRIDGE ABOVE
        chars.append(0x20EA)  #uni20EA	COMBINING LEFTWARDS ARROW OVERLAY
        chars.append(0x20EB)  #uni20EB	COMBINING LONG DOUBLE SOLIDUS OVERLAY
        chars.append(0x20EC)  #uni20EC	COMBINING RIGHTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x20ED)  #uni20ED	COMBINING LEFTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x20EE)  #uni20EE	COMBINING LEFT ARROW BELOW
        chars.append(0x20EF)  #uni20EF	COMBINING RIGHT ARROW BELOW
        chars.append(0x20F0)  #uni20F0	COMBINING ASTERISK ABOVE
        chars.append(0x2100)  #uni2100	ACCOUNT OF
        chars.append(0x2101)  #uni2101	ADDRESSED TO THE SUBJECT
        chars.append(0x2102)  #uni2102	DOUBLE-STRUCK CAPITAL C
        chars.append(0x2103)  #uni2103	DEGREE CELSIUS
        chars.append(0x2104)  #uni2104	CENTRE LINE SYMBOL
        chars.append(0x2105)  #uni2105	CARE OF
        chars.append(0x2106)  #uni2106	CADA UNA
        chars.append(0x2107)  #uni2107	EULER CONSTANT
        chars.append(0x2108)  #uni2108	SCRUPLE
        chars.append(0x2109)  #uni2109	DEGREE FAHRENHEIT
        chars.append(0x210A)  #uni210A	SCRIPT SMALL G
        chars.append(0x210B)  #uni210B	SCRIPT CAPITAL H
        chars.append(0x210C)  #uni210C	BLACK-LETTER CAPITAL H
        chars.append(0x210D)  #uni210D	DOUBLE-STRUCK CAPITAL H
        chars.append(0x210E)  #uni210E	PLANCK CONSTANT
        chars.append(0x210F)  #uni210F	PLANCK CONSTANT OVER TWO PI
        chars.append(0x2110)  #uni2110	SCRIPT CAPITAL I
        chars.append(0x2111)  #Ifraktur	BLACK-LETTER CAPITAL I
        chars.append(0x2112)  #uni2112	SCRIPT CAPITAL L
        chars.append(0x2113)  #uni2113	SCRIPT SMALL L
        chars.append(0x2114)  #uni2114	L B BAR SYMBOL
        chars.append(0x2115)  #uni2115	DOUBLE-STRUCK CAPITAL N
        chars.append(0x2116)  #uni2116	NUMERO SIGN
        chars.append(0x2117)  #uni2117	SOUND RECORDING COPYRIGHT
        chars.append(0x2118)  #weierstrass	SCRIPT CAPITAL P
        chars.append(0x2119)  #uni2119	DOUBLE-STRUCK CAPITAL P
        chars.append(0x211A)  #uni211A	DOUBLE-STRUCK CAPITAL Q
        chars.append(0x211B)  #uni211B	SCRIPT CAPITAL R
        chars.append(0x211C)  #Rfraktur	BLACK-LETTER CAPITAL R
        chars.append(0x211D)  #uni211D	DOUBLE-STRUCK CAPITAL R
        chars.append(0x211E)  #prescription	PRESCRIPTION TAKE
        chars.append(0x211F)  #uni211F	RESPONSE
        chars.append(0x2120)  #uni2120	SERVICE MARK
        chars.append(0x2121)  #uni2121	TELEPHONE SIGN
        chars.append(0x2122)  #trademark	TRADE MARK SIGN
        chars.append(0x2123)  #uni2123	VERSICLE
        chars.append(0x2124)  #uni2124	DOUBLE-STRUCK CAPITAL Z
        chars.append(0x2125)  #uni2125	OUNCE SIGN
        chars.append(0x2126)  #Omega	OHM SIGN
        chars.append(0x2127)  #uni2127	INVERTED OHM SIGN
        chars.append(0x2128)  #uni2128	BLACK-LETTER CAPITAL Z
        chars.append(0x2129)  #uni2129	TURNED GREEK SMALL LETTER IOTA
        chars.append(0x212A)  #uni212A	KELVIN SIGN
        chars.append(0x212B)  #uni212B	ANGSTROM SIGN
        chars.append(0x212C)  #uni212C	SCRIPT CAPITAL B
        chars.append(0x212D)  #uni212D	BLACK-LETTER CAPITAL C
        chars.append(0x212E)  #estimated	ESTIMATED SYMBOL
        chars.append(0x212F)  #uni212F	SCRIPT SMALL E
        chars.append(0x2130)  #uni2130	SCRIPT CAPITAL E
        chars.append(0x2131)  #uni2131	SCRIPT CAPITAL F
        chars.append(0x2132)  #uni2132	TURNED CAPITAL F
        chars.append(0x2133)  #uni2133	SCRIPT CAPITAL M
        chars.append(0x2134)  #uni2134	SCRIPT SMALL O
        chars.append(0x2135)  #aleph	ALEF SYMBOL
        chars.append(0x2136)  #uni2136	BET SYMBOL
        chars.append(0x2137)  #uni2137	GIMEL SYMBOL
        chars.append(0x2138)  #uni2138	DALET SYMBOL
        chars.append(0x2139)  #uni2139	INFORMATION SOURCE
        chars.append(0x213A)  #uni213A	ROTATED CAPITAL Q
        chars.append(0x213B)  #uni213B	FACSIMILE SIGN
        chars.append(0x213C)  #uni213C	DOUBLE-STRUCK SMALL PI
        chars.append(0x213D)  #uni213D	DOUBLE-STRUCK SMALL GAMMA
        chars.append(0x213E)  #uni213E	DOUBLE-STRUCK CAPITAL GAMMA
        chars.append(0x213F)  #uni213F	DOUBLE-STRUCK CAPITAL PI
        chars.append(0x2140)  #uni2140	DOUBLE-STRUCK N-ARY SUMMATION
        chars.append(0x2141)  #uni2141	TURNED SANS-SERIF CAPITAL G
        chars.append(0x2142)  #uni2142	TURNED SANS-SERIF CAPITAL L
        chars.append(0x2143)  #uni2143	REVERSED SANS-SERIF CAPITAL L
        chars.append(0x2144)  #uni2144	TURNED SANS-SERIF CAPITAL Y
        chars.append(0x2145)  #uni2145	DOUBLE-STRUCK ITALIC CAPITAL D
        chars.append(0x2146)  #uni2146	DOUBLE-STRUCK ITALIC SMALL D
        chars.append(0x2147)  #uni2147	DOUBLE-STRUCK ITALIC SMALL E
        chars.append(0x2148)  #uni2148	DOUBLE-STRUCK ITALIC SMALL I
        chars.append(0x2149)  #uni2149	DOUBLE-STRUCK ITALIC SMALL J
        chars.append(0x214A)  #uni214A	PROPERTY LINE
        chars.append(0x214B)  #uni214B	TURNED AMPERSAND
        chars.append(0x214C)  #uni214C	PER SIGN
        chars.append(0x214D)  #uni214D	AKTIESELSKAB
        chars.append(0x214E)  #uni214E	TURNED SMALL F
        chars.append(0x214F)  #uni214F	SYMBOL FOR SAMARITAN SOURCE
        chars.append(0x2190)  #arrowleft	LEFTWARDS ARROW
        chars.append(0x2191)  #arrowup	UPWARDS ARROW
        chars.append(0x2192)  #arrowright	RIGHTWARDS ARROW
        chars.append(0x2193)  #arrowdown	DOWNWARDS ARROW
        chars.append(0x2194)  #arrowboth	LEFT RIGHT ARROW
        chars.append(0x2195)  #arrowupdn	UP DOWN ARROW
        chars.append(0x2196)  #uni2196	NORTH WEST ARROW
        chars.append(0x2197)  #uni2197	NORTH EAST ARROW
        chars.append(0x2198)  #uni2198	SOUTH EAST ARROW
        chars.append(0x2199)  #uni2199	SOUTH WEST ARROW
        chars.append(0x219A)  #uni219A	LEFTWARDS ARROW WITH STROKE
        chars.append(0x219B)  #uni219B	RIGHTWARDS ARROW WITH STROKE
        chars.append(0x219C)  #uni219C	LEFTWARDS WAVE ARROW
        chars.append(0x219D)  #uni219D	RIGHTWARDS WAVE ARROW
        chars.append(0x219E)  #uni219E	LEFTWARDS TWO HEADED ARROW
        chars.append(0x219F)  #uni219F	UPWARDS TWO HEADED ARROW
        chars.append(0x21A0)  #uni21A0	RIGHTWARDS TWO HEADED ARROW
        chars.append(0x21A1)  #uni21A1	DOWNWARDS TWO HEADED ARROW
        chars.append(0x21A2)  #uni21A2	LEFTWARDS ARROW WITH TAIL
        chars.append(0x21A3)  #uni21A3	RIGHTWARDS ARROW WITH TAIL
        chars.append(0x21A4)  #uni21A4	LEFTWARDS ARROW FROM BAR
        chars.append(0x21A5)  #uni21A5	UPWARDS ARROW FROM BAR
        chars.append(0x21A6)  #uni21A6	RIGHTWARDS ARROW FROM BAR
        chars.append(0x21A7)  #uni21A7	DOWNWARDS ARROW FROM BAR
        chars.append(0x21A8)  #arrowupdnbse	UP DOWN ARROW WITH BASE
        chars.append(0x21A9)  #uni21A9	LEFTWARDS ARROW WITH HOOK
        chars.append(0x21AA)  #uni21AA	RIGHTWARDS ARROW WITH HOOK
        chars.append(0x21AB)  #uni21AB	LEFTWARDS ARROW WITH LOOP
        chars.append(0x21AC)  #uni21AC	RIGHTWARDS ARROW WITH LOOP
        chars.append(0x21AD)  #uni21AD	LEFT RIGHT WAVE ARROW
        chars.append(0x21AE)  #uni21AE	LEFT RIGHT ARROW WITH STROKE
        chars.append(0x21AF)  #uni21AF	DOWNWARDS ZIGZAG ARROW
        chars.append(0x21B0)  #uni21B0	UPWARDS ARROW WITH TIP LEFTWARDS
        chars.append(0x21B1)  #uni21B1	UPWARDS ARROW WITH TIP RIGHTWARDS
        chars.append(0x21B2)  #uni21B2	DOWNWARDS ARROW WITH TIP LEFTWARDS
        chars.append(0x21B3)  #uni21B3	DOWNWARDS ARROW WITH TIP RIGHTWARDS
        chars.append(0x21B4)  #uni21B4	RIGHTWARDS ARROW WITH CORNER DOWNWARDS
        chars.append(0x21B5)  #carriagereturn	DOWNWARDS ARROW WITH CORNER LEFTWARDS
        chars.append(0x21B6)  #uni21B6	ANTICLOCKWISE TOP SEMICIRCLE ARROW
        chars.append(0x21B7)  #uni21B7	CLOCKWISE TOP SEMICIRCLE ARROW
        chars.append(0x21B8)  #uni21B8	NORTH WEST ARROW TO LONG BAR
        chars.append(0x21B9)  #uni21B9	LEFTWARDS ARROW TO BAR OVER RIGHTWARDS ARROW TO BAR
        chars.append(0x21BA)  #uni21BA	ANTICLOCKWISE OPEN CIRCLE ARROW
        chars.append(0x21BB)  #uni21BB	CLOCKWISE OPEN CIRCLE ARROW
        chars.append(0x21BC)  #uni21BC	LEFTWARDS HARPOON WITH BARB UPWARDS
        chars.append(0x21BD)  #uni21BD	LEFTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x21BE)  #uni21BE	UPWARDS HARPOON WITH BARB RIGHTWARDS
        chars.append(0x21BF)  #uni21BF	UPWARDS HARPOON WITH BARB LEFTWARDS
        chars.append(0x21C0)  #uni21C0	RIGHTWARDS HARPOON WITH BARB UPWARDS
        chars.append(0x21C1)  #uni21C1	RIGHTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x21C2)  #uni21C2	DOWNWARDS HARPOON WITH BARB RIGHTWARDS
        chars.append(0x21C3)  #uni21C3	DOWNWARDS HARPOON WITH BARB LEFTWARDS
        chars.append(0x21C4)  #uni21C4	RIGHTWARDS ARROW OVER LEFTWARDS ARROW
        chars.append(0x21C5)  #uni21C5	UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW
        chars.append(0x21C6)  #uni21C6	LEFTWARDS ARROW OVER RIGHTWARDS ARROW
        chars.append(0x21C7)  #uni21C7	LEFTWARDS PAIRED ARROWS
        chars.append(0x21C8)  #uni21C8	UPWARDS PAIRED ARROWS
        chars.append(0x21C9)  #uni21C9	RIGHTWARDS PAIRED ARROWS
        chars.append(0x21CA)  #uni21CA	DOWNWARDS PAIRED ARROWS
        chars.append(0x21CB)  #uni21CB	LEFTWARDS HARPOON OVER RIGHTWARDS HARPOON
        chars.append(0x21CC)  #uni21CC	RIGHTWARDS HARPOON OVER LEFTWARDS HARPOON
        chars.append(0x21CD)  #uni21CD	LEFTWARDS DOUBLE ARROW WITH STROKE
        chars.append(0x21CE)  #uni21CE	LEFT RIGHT DOUBLE ARROW WITH STROKE
        chars.append(0x21CF)  #uni21CF	RIGHTWARDS DOUBLE ARROW WITH STROKE
        chars.append(0x21D0)  #arrowdblleft	LEFTWARDS DOUBLE ARROW
        chars.append(0x21D1)  #arrowdblup	UPWARDS DOUBLE ARROW
        chars.append(0x21D2)  #arrowdblright	RIGHTWARDS DOUBLE ARROW
        chars.append(0x21D3)  #arrowdbldown	DOWNWARDS DOUBLE ARROW
        chars.append(0x21D4)  #arrowdblboth	LEFT RIGHT DOUBLE ARROW
        chars.append(0x21D5)  #uni21D5	UP DOWN DOUBLE ARROW
        chars.append(0x21D6)  #uni21D6	NORTH WEST DOUBLE ARROW
        chars.append(0x21D7)  #uni21D7	NORTH EAST DOUBLE ARROW
        chars.append(0x21D8)  #uni21D8	SOUTH EAST DOUBLE ARROW
        chars.append(0x21D9)  #uni21D9	SOUTH WEST DOUBLE ARROW
        chars.append(0x21DA)  #uni21DA	LEFTWARDS TRIPLE ARROW
        chars.append(0x21DB)  #uni21DB	RIGHTWARDS TRIPLE ARROW
        chars.append(0x21DC)  #uni21DC	LEFTWARDS SQUIGGLE ARROW
        chars.append(0x21DD)  #uni21DD	RIGHTWARDS SQUIGGLE ARROW
        chars.append(0x21DE)  #uni21DE	UPWARDS ARROW WITH DOUBLE STROKE
        chars.append(0x21DF)  #uni21DF	DOWNWARDS ARROW WITH DOUBLE STROKE
        chars.append(0x21E0)  #uni21E0	LEFTWARDS DASHED ARROW
        chars.append(0x21E1)  #uni21E1	UPWARDS DASHED ARROW
        chars.append(0x21E2)  #uni21E2	RIGHTWARDS DASHED ARROW
        chars.append(0x21E3)  #uni21E3	DOWNWARDS DASHED ARROW
        chars.append(0x21E4)  #uni21E4	LEFTWARDS ARROW TO BAR
        chars.append(0x21E5)  #uni21E5	RIGHTWARDS ARROW TO BAR
        chars.append(0x21E6)  #uni21E6	LEFTWARDS WHITE ARROW
        chars.append(0x21E7)  #uni21E7	UPWARDS WHITE ARROW
        chars.append(0x21E8)  #uni21E8	RIGHTWARDS WHITE ARROW
        chars.append(0x21E9)  #uni21E9	DOWNWARDS WHITE ARROW
        chars.append(0x21EA)  #uni21EA	UPWARDS WHITE ARROW FROM BAR
        chars.append(0x21EB)  #uni21EB	UPWARDS WHITE ARROW ON PEDESTAL
        chars.append(0x21EC)  #uni21EC	UPWARDS WHITE ARROW ON PEDESTAL WITH HORIZONTAL BAR
        chars.append(0x21ED)  #uni21ED	UPWARDS WHITE ARROW ON PEDESTAL WITH VERTICAL BAR
        chars.append(0x21EE)  #uni21EE	UPWARDS WHITE DOUBLE ARROW
        chars.append(0x21EF)  #uni21EF	UPWARDS WHITE DOUBLE ARROW ON PEDESTAL
        chars.append(0x21F0)  #uni21F0	RIGHTWARDS WHITE ARROW FROM WALL
        chars.append(0x21F1)  #uni21F1	NORTH WEST ARROW TO CORNER
        chars.append(0x21F2)  #uni21F2	SOUTH EAST ARROW TO CORNER
        chars.append(0x21F3)  #uni21F3	UP DOWN WHITE ARROW
        chars.append(0x21F4)  #uni21F4	RIGHT ARROW WITH SMALL CIRCLE
        chars.append(0x21F5)  #uni21F5	DOWNWARDS ARROW LEFTWARDS OF UPWARDS ARROW
        chars.append(0x21F6)  #uni21F6	THREE RIGHTWARDS ARROWS
        chars.append(0x21F7)  #uni21F7	LEFTWARDS ARROW WITH VERTICAL STROKE
        chars.append(0x21F8)  #uni21F8	RIGHTWARDS ARROW WITH VERTICAL STROKE
        chars.append(0x21F9)  #uni21F9	LEFT RIGHT ARROW WITH VERTICAL STROKE
        chars.append(0x21FA)  #uni21FA	LEFTWARDS ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x21FB)  #uni21FB	RIGHTWARDS ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x21FC)  #uni21FC	LEFT RIGHT ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x21FD)  #uni21FD	LEFTWARDS OPEN-HEADED ARROW
        chars.append(0x21FE)  #uni21FE	RIGHTWARDS OPEN-HEADED ARROW
        chars.append(0x21FF)  #uni21FF	LEFT RIGHT OPEN-HEADED ARROW
        chars.append(0x2200)  #universal	FOR ALL
        chars.append(0x2201)  #uni2201	COMPLEMENT
        chars.append(0x2202)  #partialdiff	PARTIAL DIFFERENTIAL
        chars.append(0x2203)  #existential	THERE EXISTS
        chars.append(0x2204)  #uni2204	THERE DOES NOT EXIST
        chars.append(0x2205)  #emptyset	EMPTY SET
        chars.append(0x2206)  #Delta	INCREMENT
        chars.append(0x2207)  #gradient	NABLA
        chars.append(0x2208)  #element	ELEMENT OF
        chars.append(0x2209)  #notelement	NOT AN ELEMENT OF
        chars.append(0x220A)  #uni220A	SMALL ELEMENT OF
        chars.append(0x220B)  #suchthat	CONTAINS AS MEMBER
        chars.append(0x220C)  #uni220C	DOES NOT CONTAIN AS MEMBER
        chars.append(0x220D)  #uni220D	SMALL CONTAINS AS MEMBER
        chars.append(0x220E)  #uni220E	END OF PROOF
        chars.append(0x220F)  #product	N-ARY PRODUCT
        chars.append(0x2210)  #uni2210	N-ARY COPRODUCT
        chars.append(0x2211)  #summation	N-ARY SUMMATION
        chars.append(0x2212)  #minus	MINUS SIGN
        chars.append(0x2213)  #uni2213	MINUS-OR-PLUS SIGN
        chars.append(0x2214)  #uni2214	DOT PLUS
        chars.append(0x2215)  #uni0338	DIVISION SLASH
        chars.append(0x2216)  #uni2216	SET MINUS
        chars.append(0x2217)  #asteriskmath	ASTERISK OPERATOR
        chars.append(0x2218)  #uni2218	RING OPERATOR
        chars.append(0x2219)  #uni2219	BULLET OPERATOR
        chars.append(0x221A)  #radical	SQUARE ROOT
        chars.append(0x221B)  #uni221B	CUBE ROOT
        chars.append(0x221C)  #uni221C	FOURTH ROOT
        chars.append(0x221D)  #proportional	PROPORTIONAL TO
        chars.append(0x221E)  #infinity	INFINITY
        chars.append(0x221F)  #orthogonal	RIGHT ANGLE
        chars.append(0x2220)  #angle	ANGLE
        chars.append(0x2221)  #uni2221	MEASURED ANGLE
        chars.append(0x2222)  #uni2222	SPHERICAL ANGLE
        chars.append(0x2223)  #uni2223	DIVIDES
        chars.append(0x2224)  #uni2224	DOES NOT DIVIDE
        chars.append(0x2225)  #uni2225	PARALLEL TO
        chars.append(0x2226)  #uni2226	NOT PARALLEL TO
        chars.append(0x2227)  #logicaland	LOGICAL AND
        chars.append(0x2228)  #logicalor	LOGICAL OR
        chars.append(0x2229)  #intersection	INTERSECTION
        chars.append(0x222A)  #union	UNION
        chars.append(0x222B)  #integral	INTEGRAL
        chars.append(0x222C)  #uni222C	DOUBLE INTEGRAL
        chars.append(0x222D)  #uni222D	TRIPLE INTEGRAL
        chars.append(0x222E)  #uni222E	CONTOUR INTEGRAL
        chars.append(0x222F)  #uni222F	SURFACE INTEGRAL
        chars.append(0x2230)  #uni2230	VOLUME INTEGRAL
        chars.append(0x2231)  #uni2231	CLOCKWISE INTEGRAL
        chars.append(0x2232)  #uni2232	CLOCKWISE CONTOUR INTEGRAL
        chars.append(0x2233)  #uni2233	ANTICLOCKWISE CONTOUR INTEGRAL
        chars.append(0x2234)  #therefore	THEREFORE
        chars.append(0x2235)  #uni2235	BECAUSE
        chars.append(0x2236)  #uni2236	RATIO
        chars.append(0x2237)  #uni2237	PROPORTION
        chars.append(0x2238)  #uni2238	DOT MINUS
        chars.append(0x2239)  #uni2239	EXCESS
        chars.append(0x223A)  #uni223A	GEOMETRIC PROPORTION
        chars.append(0x223B)  #uni223B	HOMOTHETIC
        chars.append(0x223C)  #similar	TILDE OPERATOR
        chars.append(0x223D)  #uni223D	REVERSED TILDE
        chars.append(0x223E)  #uni223E	INVERTED LAZY S
        chars.append(0x223F)  #uni223F	SINE WAVE
        chars.append(0x2240)  #uni2240	WREATH PRODUCT
        chars.append(0x2241)  #uni2241	NOT TILDE
        chars.append(0x2242)  #uni2242	MINUS TILDE
        chars.append(0x2243)  #uni2243	ASYMPTOTICALLY EQUAL TO
        chars.append(0x2244)  #uni2244	NOT ASYMPTOTICALLY EQUAL TO
        chars.append(0x2245)  #congruent	APPROXIMATELY EQUAL TO
        chars.append(0x2246)  #uni2246	APPROXIMATELY BUT NOT ACTUALLY EQUAL TO
        chars.append(0x2247)  #uni2247	NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO
        chars.append(0x2248)  #approxequal	ALMOST EQUAL TO
        chars.append(0x2249)  #uni2249	NOT ALMOST EQUAL TO
        chars.append(0x224A)  #uni224A	ALMOST EQUAL OR EQUAL TO
        chars.append(0x224B)  #uni224B	TRIPLE TILDE
        chars.append(0x224C)  #uni224C	ALL EQUAL TO
        chars.append(0x224D)  #uni224D	EQUIVALENT TO
        chars.append(0x224E)  #uni224E	GEOMETRICALLY EQUIVALENT TO
        chars.append(0x224F)  #uni224F	DIFFERENCE BETWEEN
        chars.append(0x2250)  #uni2250	APPROACHES THE LIMIT
        chars.append(0x2251)  #uni2251	GEOMETRICALLY EQUAL TO
        chars.append(0x2252)  #uni2252	APPROXIMATELY EQUAL TO OR THE IMAGE OF
        chars.append(0x2253)  #uni2253	IMAGE OF OR APPROXIMATELY EQUAL TO
        chars.append(0x2254)  #uni2254	COLON EQUALS
        chars.append(0x2255)  #uni2255	EQUALS COLON
        chars.append(0x2256)  #uni2256	RING IN EQUAL TO
        chars.append(0x2257)  #uni2257	RING EQUAL TO
        chars.append(0x2258)  #uni2258	CORRESPONDS TO
        chars.append(0x2259)  #uni2259	ESTIMATES
        chars.append(0x225A)  #uni225A	EQUIANGULAR TO
        chars.append(0x225B)  #uni225B	STAR EQUALS
        chars.append(0x225C)  #uni225C	DELTA EQUAL TO
        chars.append(0x225D)  #uni225D	EQUAL TO BY DEFINITION
        chars.append(0x225E)  #uni225E	MEASURED BY
        chars.append(0x225F)  #uni225F	QUESTIONED EQUAL TO
        chars.append(0x2260)  #notequal	NOT EQUAL TO
        chars.append(0x2261)  #equivalence	IDENTICAL TO
        chars.append(0x2262)  #uni2262	NOT IDENTICAL TO
        chars.append(0x2263)  #uni2263	STRICTLY EQUIVALENT TO
        chars.append(0x2264)  #lessequal	LESS-THAN OR EQUAL TO
        chars.append(0x2265)  #greaterequal	GREATER-THAN OR EQUAL TO
        chars.append(0x2266)  #uni2266	LESS-THAN OVER EQUAL TO
        chars.append(0x2267)  #uni2267	GREATER-THAN OVER EQUAL TO
        chars.append(0x2268)  #uni2268	LESS-THAN BUT NOT EQUAL TO
        chars.append(0x2269)  #uni2269	GREATER-THAN BUT NOT EQUAL TO
        chars.append(0x226A)  #uni226A	MUCH LESS-THAN
        chars.append(0x226B)  #uni226B	MUCH GREATER-THAN
        chars.append(0x226C)  #uni226C	BETWEEN
        chars.append(0x226D)  #uni226D	NOT EQUIVALENT TO
        chars.append(0x226E)  #uni226E	NOT LESS-THAN
        chars.append(0x226F)  #uni226F	NOT GREATER-THAN
        chars.append(0x2270)  #uni2270	NEITHER LESS-THAN NOR EQUAL TO
        chars.append(0x2271)  #uni2271	NEITHER GREATER-THAN NOR EQUAL TO
        chars.append(0x2272)  #uni2272	LESS-THAN OR EQUIVALENT TO
        chars.append(0x2273)  #uni2273	GREATER-THAN OR EQUIVALENT TO
        chars.append(0x2274)  #uni2274	NEITHER LESS-THAN NOR EQUIVALENT TO
        chars.append(0x2275)  #uni2275	NEITHER GREATER-THAN NOR EQUIVALENT TO
        chars.append(0x2276)  #uni2276	LESS-THAN OR GREATER-THAN
        chars.append(0x2277)  #uni2277	GREATER-THAN OR LESS-THAN
        chars.append(0x2278)  #uni2278	NEITHER LESS-THAN NOR GREATER-THAN
        chars.append(0x2279)  #uni2279	NEITHER GREATER-THAN NOR LESS-THAN
        chars.append(0x227A)  #uni227A	PRECEDES
        chars.append(0x227B)  #uni227B	SUCCEEDS
        chars.append(0x227C)  #uni227C	PRECEDES OR EQUAL TO
        chars.append(0x227D)  #uni227D	SUCCEEDS OR EQUAL TO
        chars.append(0x227E)  #uni227E	PRECEDES OR EQUIVALENT TO
        chars.append(0x227F)  #uni227F	SUCCEEDS OR EQUIVALENT TO
        chars.append(0x2280)  #uni2280	DOES NOT PRECEDE
        chars.append(0x2281)  #uni2281	DOES NOT SUCCEED
        chars.append(0x2282)  #propersubset	SUBSET OF
        chars.append(0x2283)  #propersuperset	SUPERSET OF
        chars.append(0x2284)  #notsubset	NOT A SUBSET OF
        chars.append(0x2285)  #uni2285	NOT A SUPERSET OF
        chars.append(0x2286)  #reflexsubset	SUBSET OF OR EQUAL TO
        chars.append(0x2287)  #reflexsuperset	SUPERSET OF OR EQUAL TO
        chars.append(0x2288)  #uni2288	NEITHER A SUBSET OF NOR EQUAL TO
        chars.append(0x2289)  #uni2289	NEITHER A SUPERSET OF NOR EQUAL TO
        chars.append(0x228A)  #uni228A	SUBSET OF WITH NOT EQUAL TO
        chars.append(0x228B)  #uni228B	SUPERSET OF WITH NOT EQUAL TO
        chars.append(0x228C)  #uni228C	MULTISET
        chars.append(0x228D)  #uni228D	MULTISET MULTIPLICATION
        chars.append(0x228E)  #uni228E	MULTISET UNION
        chars.append(0x228F)  #uni228F	SQUARE IMAGE OF
        chars.append(0x2290)  #uni2290	SQUARE ORIGINAL OF
        chars.append(0x2291)  #uni2291	SQUARE IMAGE OF OR EQUAL TO
        chars.append(0x2292)  #uni2292	SQUARE ORIGINAL OF OR EQUAL TO
        chars.append(0x2293)  #uni2293	SQUARE CAP
        chars.append(0x2294)  #uni2294	SQUARE CUP
        chars.append(0x2295)  #circleplus	CIRCLED PLUS
        chars.append(0x2296)  #uni2296	CIRCLED MINUS
        chars.append(0x2297)  #circlemultiply	CIRCLED TIMES
        chars.append(0x2298)  #uni2298	CIRCLED DIVISION SLASH
        chars.append(0x2299)  #uni2299	CIRCLED DOT OPERATOR
        chars.append(0x229A)  #uni229A	CIRCLED RING OPERATOR
        chars.append(0x229B)  #uni229B	CIRCLED ASTERISK OPERATOR
        chars.append(0x229C)  #uni229C	CIRCLED EQUALS
        chars.append(0x229D)  #uni229D	CIRCLED DASH
        chars.append(0x229E)  #uni229E	SQUARED PLUS
        chars.append(0x229F)  #uni229F	SQUARED MINUS
        chars.append(0x22A0)  #uni22A0	SQUARED TIMES
        chars.append(0x22A1)  #uni22A1	SQUARED DOT OPERATOR
        chars.append(0x22A2)  #uni22A2	RIGHT TACK
        chars.append(0x22A3)  #uni22A3	LEFT TACK
        chars.append(0x22A4)  #uni22A4	DOWN TACK
        chars.append(0x22A5)  #perpendicular	UP TACK
        chars.append(0x22A6)  #uni22A6	ASSERTION
        chars.append(0x22A7)  #uni22A7	MODELS
        chars.append(0x22A8)  #uni22A8	TRUE
        chars.append(0x22A9)  #uni22A9	FORCES
        chars.append(0x22AA)  #uni22AA	TRIPLE VERTICAL BAR RIGHT TURNSTILE
        chars.append(0x22AB)  #uni22AB	DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE
        chars.append(0x22AC)  #uni22AC	DOES NOT PROVE
        chars.append(0x22AD)  #uni22AD	NOT TRUE
        chars.append(0x22AE)  #uni22AE	DOES NOT FORCE
        chars.append(0x22AF)  #uni22AF	NEGATED DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE
        chars.append(0x22B0)  #uni22B0	PRECEDES UNDER RELATION
        chars.append(0x22B1)  #uni22B1	SUCCEEDS UNDER RELATION
        chars.append(0x22B2)  #uni22B2	NORMAL SUBGROUP OF
        chars.append(0x22B3)  #uni22B3	CONTAINS AS NORMAL SUBGROUP
        chars.append(0x22B4)  #uni22B4	NORMAL SUBGROUP OF OR EQUAL TO
        chars.append(0x22B5)  #uni22B5	CONTAINS AS NORMAL SUBGROUP OR EQUAL TO
        chars.append(0x22B6)  #uni22B6	ORIGINAL OF
        chars.append(0x22B7)  #uni22B7	IMAGE OF
        chars.append(0x22B8)  #uni22B8	MULTIMAP
        chars.append(0x22B9)  #uni22B9	HERMITIAN CONJUGATE MATRIX
        chars.append(0x22BA)  #uni22BA	INTERCALATE
        chars.append(0x22BB)  #uni22BB	XOR
        chars.append(0x22BC)  #uni22BC	NAND
        chars.append(0x22BD)  #uni22BD	NOR
        chars.append(0x22BE)  #uni22BE	RIGHT ANGLE WITH ARC
        chars.append(0x22BF)  #uni22BF	RIGHT TRIANGLE
        chars.append(0x22C0)  #uni22C0	N-ARY LOGICAL AND
        chars.append(0x22C1)  #uni22C1	N-ARY LOGICAL OR
        chars.append(0x22C2)  #uni22C2	N-ARY INTERSECTION
        chars.append(0x22C3)  #uni22C3	N-ARY UNION
        chars.append(0x22C4)  #uni22C4	DIAMOND OPERATOR
        chars.append(0x22C5)  #dotmath	DOT OPERATOR
        chars.append(0x22C6)  #uni22C6	STAR OPERATOR
        chars.append(0x22C7)  #uni22C7	DIVISION TIMES
        chars.append(0x22C8)  #uni22C8	BOWTIE
        chars.append(0x22C9)  #uni22C9	LEFT NORMAL FACTOR SEMIDIRECT PRODUCT
        chars.append(0x22CA)  #uni22CA	RIGHT NORMAL FACTOR SEMIDIRECT PRODUCT
        chars.append(0x22CB)  #uni22CB	LEFT SEMIDIRECT PRODUCT
        chars.append(0x22CC)  #uni22CC	RIGHT SEMIDIRECT PRODUCT
        chars.append(0x22CD)  #uni22CD	REVERSED TILDE EQUALS
        chars.append(0x22CE)  #uni22CE	CURLY LOGICAL OR
        chars.append(0x22CF)  #uni22CF	CURLY LOGICAL AND
        chars.append(0x22D0)  #uni22D0	DOUBLE SUBSET
        chars.append(0x22D1)  #uni22D1	DOUBLE SUPERSET
        chars.append(0x22D2)  #uni22D2	DOUBLE INTERSECTION
        chars.append(0x22D3)  #uni22D3	DOUBLE UNION
        chars.append(0x22D4)  #uni22D4	PITCHFORK
        chars.append(0x22D5)  #uni22D5	EQUAL AND PARALLEL TO
        chars.append(0x22D6)  #uni22D6	LESS-THAN WITH DOT
        chars.append(0x22D7)  #uni22D7	GREATER-THAN WITH DOT
        chars.append(0x22D8)  #uni22D8	VERY MUCH LESS-THAN
        chars.append(0x22D9)  #uni22D9	VERY MUCH GREATER-THAN
        chars.append(0x22DA)  #uni22DA	LESS-THAN EQUAL TO OR GREATER-THAN
        chars.append(0x22DB)  #uni22DB	GREATER-THAN EQUAL TO OR LESS-THAN
        chars.append(0x22DC)  #uni22DC	EQUAL TO OR LESS-THAN
        chars.append(0x22DD)  #uni22DD	EQUAL TO OR GREATER-THAN
        chars.append(0x22DE)  #uni22DE	EQUAL TO OR PRECEDES
        chars.append(0x22DF)  #uni22DF	EQUAL TO OR SUCCEEDS
        chars.append(0x22E0)  #uni22E0	DOES NOT PRECEDE OR EQUAL
        chars.append(0x22E1)  #uni22E1	DOES NOT SUCCEED OR EQUAL
        chars.append(0x22E2)  #uni22E2	NOT SQUARE IMAGE OF OR EQUAL TO
        chars.append(0x22E3)  #uni22E3	NOT SQUARE ORIGINAL OF OR EQUAL TO
        chars.append(0x22E4)  #uni22E4	SQUARE IMAGE OF OR NOT EQUAL TO
        chars.append(0x22E5)  #uni22E5	SQUARE ORIGINAL OF OR NOT EQUAL TO
        chars.append(0x22E6)  #uni22E6	LESS-THAN BUT NOT EQUIVALENT TO
        chars.append(0x22E7)  #uni22E7	GREATER-THAN BUT NOT EQUIVALENT TO
        chars.append(0x22E8)  #uni22E8	PRECEDES BUT NOT EQUIVALENT TO
        chars.append(0x22E9)  #uni22E9	SUCCEEDS BUT NOT EQUIVALENT TO
        chars.append(0x22EA)  #uni22EA	NOT NORMAL SUBGROUP OF
        chars.append(0x22EB)  #uni22EB	DOES NOT CONTAIN AS NORMAL SUBGROUP
        chars.append(0x22EC)  #uni22EC	NOT NORMAL SUBGROUP OF OR EQUAL TO
        chars.append(0x22ED)  #uni22ED	DOES NOT CONTAIN AS NORMAL SUBGROUP OR EQUAL
        chars.append(0x22EE)  #uni22EE	VERTICAL ELLIPSIS
        chars.append(0x22EF)  #uni22EF	MIDLINE HORIZONTAL ELLIPSIS
        chars.append(0x22F0)  #uni22F0	UP RIGHT DIAGONAL ELLIPSIS
        chars.append(0x22F1)  #uni22F1	DOWN RIGHT DIAGONAL ELLIPSIS
        chars.append(0x22F2)  #uni22F2	ELEMENT OF WITH LONG HORIZONTAL STROKE
        chars.append(0x22F3)  #uni22F3	ELEMENT OF WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22F4)  #uni22F4	SMALL ELEMENT OF WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22F5)  #uni22F5	ELEMENT OF WITH DOT ABOVE
        chars.append(0x22F6)  #uni22F6	ELEMENT OF WITH OVERBAR
        chars.append(0x22F7)  #uni22F7	SMALL ELEMENT OF WITH OVERBAR
        chars.append(0x22F8)  #uni22F8	ELEMENT OF WITH UNDERBAR
        chars.append(0x22F9)  #uni22F9	ELEMENT OF WITH TWO HORIZONTAL STROKES
        chars.append(0x22FA)  #uni22FA	CONTAINS WITH LONG HORIZONTAL STROKE
        chars.append(0x22FB)  #uni22FB	CONTAINS WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22FC)  #uni22FC	SMALL CONTAINS WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22FD)  #uni22FD	CONTAINS WITH OVERBAR
        chars.append(0x22FE)  #uni22FE	SMALL CONTAINS WITH OVERBAR
        chars.append(0x22FF)  #uni22FF	Z NOTATION BAG MEMBERSHIP
        chars.append(0x2300)  #uni2300	DIAMETER SIGN
        chars.append(0x2301)  #uni2301	ELECTRIC ARROW
        chars.append(0x2302)  #house	HOUSE
        chars.append(0x2303)  #uni2303	UP ARROWHEAD
        chars.append(0x2304)  #uni2304	DOWN ARROWHEAD
        chars.append(0x2305)  #uni2305	PROJECTIVE
        chars.append(0x2306)  #uni2306	PERSPECTIVE
        chars.append(0x2307)  #uni2307	WAVY LINE
        chars.append(0x2308)  #uni2308	LEFT CEILING
        chars.append(0x2309)  #uni2309	RIGHT CEILING
        chars.append(0x230A)  #uni230A	LEFT FLOOR
        chars.append(0x230B)  #uni230B	RIGHT FLOOR
        chars.append(0x230C)  #uni230C	BOTTOM RIGHT CROP
        chars.append(0x230D)  #uni230D	BOTTOM LEFT CROP
        chars.append(0x230E)  #uni230E	TOP RIGHT CROP
        chars.append(0x230F)  #uni230F	TOP LEFT CROP
        chars.append(0x2310)  #revlogicalnot	REVERSED NOT SIGN
        chars.append(0x2311)  #uni2311	SQUARE LOZENGE
        chars.append(0x2312)  #uni2312	ARC
        chars.append(0x2313)  #uni2313	SEGMENT
        chars.append(0x2314)  #uni2314	SECTOR
        chars.append(0x2315)  #uni2315	TELEPHONE RECORDER
        chars.append(0x2316)  #uni2316	POSITION INDICATOR
        chars.append(0x2317)  #uni2317	VIEWDATA SQUARE
        chars.append(0x2318)  #uni2318	PLACE OF INTEREST SIGN
        chars.append(0x2319)  #uni2319	TURNED NOT SIGN
        chars.append(0x231A)  #uni231A	WATCH
        chars.append(0x231B)  #uni231B	HOURGLASS
        chars.append(0x231C)  #uni231C	TOP LEFT CORNER
        chars.append(0x231D)  #uni231D	TOP RIGHT CORNER
        chars.append(0x231E)  #uni231E	BOTTOM LEFT CORNER
        chars.append(0x231F)  #uni231F	BOTTOM RIGHT CORNER
        chars.append(0x2320)  #integraltp	TOP HALF INTEGRAL
        chars.append(0x2321)  #integralbt	BOTTOM HALF INTEGRAL
        chars.append(0x2322)  #uni2322	FROWN
        chars.append(0x2323)  #uni2323	SMILE
        chars.append(0x2324)  #uni2324	UP ARROWHEAD BETWEEN TWO HORIZONTAL BARS
        chars.append(0x2325)  #uni2325	OPTION KEY
        chars.append(0x2326)  #uni2326	ERASE TO THE RIGHT
        chars.append(0x2327)  #uni2327	X IN A RECTANGLE BOX
        chars.append(0x2328)  #uni2328	KEYBOARD
        chars.append(0x2329)  #uni3008	LEFT-POINTING ANGLE BRACKET
        chars.append(0x232A)  #uni3009	RIGHT-POINTING ANGLE BRACKET
        chars.append(0x232B)  #uni232B	ERASE TO THE LEFT
        chars.append(0x232C)  #uni232C	BENZENE RING
        chars.append(0x232D)  #uni232D	CYLINDRICITY
        chars.append(0x232E)  #uni232E	ALL AROUND-PROFILE
        chars.append(0x232F)  #uni232F	SYMMETRY
        chars.append(0x2330)  #uni2330	TOTAL RUNOUT
        chars.append(0x2331)  #uni2331	DIMENSION ORIGIN
        chars.append(0x2332)  #uni2332	CONICAL TAPER
        chars.append(0x2333)  #uni2333	SLOPE
        chars.append(0x2334)  #uni2334	COUNTERBORE
        chars.append(0x2335)  #uni2335	COUNTERSINK
        chars.append(0x2336)  #uni2336	APL FUNCTIONAL SYMBOL I-BEAM
        chars.append(0x2337)  #uni2337	APL FUNCTIONAL SYMBOL SQUISH QUAD
        chars.append(0x0338)  #uni0338	COMBINING LONG SOLIDUS OVERLAY
        chars.append(0x2339)  #uni2339	APL FUNCTIONAL SYMBOL QUAD DIVIDE
        chars.append(0x233A)  #uni233A	APL FUNCTIONAL SYMBOL QUAD DIAMOND
        chars.append(0x233B)  #uni233B	APL FUNCTIONAL SYMBOL QUAD JOT
        chars.append(0x233C)  #uni233C	APL FUNCTIONAL SYMBOL QUAD CIRCLE
        chars.append(0x233D)  #uni233D	APL FUNCTIONAL SYMBOL CIRCLE STILE
        chars.append(0x233E)  #uni233E	APL FUNCTIONAL SYMBOL CIRCLE JOT
        chars.append(0x233F)  #uni233F	APL FUNCTIONAL SYMBOL SLASH BAR
        chars.append(0x2340)  #uni2340	APL FUNCTIONAL SYMBOL BACKSLASH BAR
        chars.append(0x2341)  #uni2341	APL FUNCTIONAL SYMBOL QUAD SLASH
        chars.append(0x2342)  #uni2342	APL FUNCTIONAL SYMBOL QUAD BACKSLASH
        chars.append(0x2343)  #uni2343	APL FUNCTIONAL SYMBOL QUAD LESS-THAN
        chars.append(0x2344)  #uni2344	APL FUNCTIONAL SYMBOL QUAD GREATER-THAN
        chars.append(0x2345)  #uni2345	APL FUNCTIONAL SYMBOL LEFTWARDS VANE
        chars.append(0x2346)  #uni2346	APL FUNCTIONAL SYMBOL RIGHTWARDS VANE
        chars.append(0x2347)  #uni2347	APL FUNCTIONAL SYMBOL QUAD LEFTWARDS ARROW
        chars.append(0x2348)  #uni2348	APL FUNCTIONAL SYMBOL QUAD RIGHTWARDS ARROW
        chars.append(0x2349)  #uni2349	APL FUNCTIONAL SYMBOL CIRCLE BACKSLASH
        chars.append(0x234A)  #uni234A	APL FUNCTIONAL SYMBOL DOWN TACK UNDERBAR
        chars.append(0x234B)  #uni234B	APL FUNCTIONAL SYMBOL DELTA STILE
        chars.append(0x234C)  #uni234C	APL FUNCTIONAL SYMBOL QUAD DOWN CARET
        chars.append(0x234D)  #uni234D	APL FUNCTIONAL SYMBOL QUAD DELTA
        chars.append(0x234E)  #uni234E	APL FUNCTIONAL SYMBOL DOWN TACK JOT
        chars.append(0x234F)  #uni234F	APL FUNCTIONAL SYMBOL UPWARDS VANE
        chars.append(0x2350)  #uni2350	APL FUNCTIONAL SYMBOL QUAD UPWARDS ARROW
        chars.append(0x2351)  #uni2351	APL FUNCTIONAL SYMBOL UP TACK OVERBAR
        chars.append(0x2352)  #uni2352	APL FUNCTIONAL SYMBOL DEL STILE
        chars.append(0x2353)  #uni2353	APL FUNCTIONAL SYMBOL QUAD UP CARET
        chars.append(0x2354)  #uni2354	APL FUNCTIONAL SYMBOL QUAD DEL
        chars.append(0x2355)  #uni2355	APL FUNCTIONAL SYMBOL UP TACK JOT
        chars.append(0x2356)  #uni2356	APL FUNCTIONAL SYMBOL DOWNWARDS VANE
        chars.append(0x2357)  #uni2357	APL FUNCTIONAL SYMBOL QUAD DOWNWARDS ARROW
        chars.append(0x2358)  #uni2358	APL FUNCTIONAL SYMBOL QUOTE UNDERBAR
        chars.append(0x2359)  #uni2359	APL FUNCTIONAL SYMBOL DELTA UNDERBAR
        chars.append(0x235A)  #uni235A	APL FUNCTIONAL SYMBOL DIAMOND UNDERBAR
        chars.append(0x235B)  #uni235B	APL FUNCTIONAL SYMBOL JOT UNDERBAR
        chars.append(0x235C)  #uni235C	APL FUNCTIONAL SYMBOL CIRCLE UNDERBAR
        chars.append(0x235D)  #uni235D	APL FUNCTIONAL SYMBOL UP SHOE JOT
        chars.append(0x235E)  #uni235E	APL FUNCTIONAL SYMBOL QUOTE QUAD
        chars.append(0x235F)  #uni235F	APL FUNCTIONAL SYMBOL CIRCLE STAR
        chars.append(0x2360)  #uni2360	APL FUNCTIONAL SYMBOL QUAD COLON
        chars.append(0x2361)  #uni2361	APL FUNCTIONAL SYMBOL UP TACK DIAERESIS
        chars.append(0x2362)  #uni2362	APL FUNCTIONAL SYMBOL DEL DIAERESIS
        chars.append(0x2363)  #uni2363	APL FUNCTIONAL SYMBOL STAR DIAERESIS
        chars.append(0x2364)  #uni2364	APL FUNCTIONAL SYMBOL JOT DIAERESIS
        chars.append(0x2365)  #uni2365	APL FUNCTIONAL SYMBOL CIRCLE DIAERESIS
        chars.append(0x2366)  #uni2366	APL FUNCTIONAL SYMBOL DOWN SHOE STILE
        chars.append(0x2367)  #uni2367	APL FUNCTIONAL SYMBOL LEFT SHOE STILE
        chars.append(0x2368)  #uni2368	APL FUNCTIONAL SYMBOL TILDE DIAERESIS
        chars.append(0x2369)  #uni2369	APL FUNCTIONAL SYMBOL GREATER-THAN DIAERESIS
        chars.append(0x236A)  #uni236A	APL FUNCTIONAL SYMBOL COMMA BAR
        chars.append(0x236B)  #uni236B	APL FUNCTIONAL SYMBOL DEL TILDE
        chars.append(0x236C)  #uni236C	APL FUNCTIONAL SYMBOL ZILDE
        chars.append(0x236D)  #uni236D	APL FUNCTIONAL SYMBOL STILE TILDE
        chars.append(0x236E)  #uni236E	APL FUNCTIONAL SYMBOL SEMICOLON UNDERBAR
        chars.append(0x236F)  #uni236F	APL FUNCTIONAL SYMBOL QUAD NOT EQUAL
        chars.append(0x2370)  #uni2370	APL FUNCTIONAL SYMBOL QUAD QUESTION
        chars.append(0x2371)  #uni2371	APL FUNCTIONAL SYMBOL DOWN CARET TILDE
        chars.append(0x2372)  #uni2372	APL FUNCTIONAL SYMBOL UP CARET TILDE
        chars.append(0x2373)  #uni2373	APL FUNCTIONAL SYMBOL IOTA
        chars.append(0x2374)  #uni2374	APL FUNCTIONAL SYMBOL RHO
        chars.append(0x2375)  #uni2375	APL FUNCTIONAL SYMBOL OMEGA
        chars.append(0x2376)  #uni2376	APL FUNCTIONAL SYMBOL ALPHA UNDERBAR
        chars.append(0x2377)  #uni2377	APL FUNCTIONAL SYMBOL EPSILON UNDERBAR
        chars.append(0x2378)  #uni2378	APL FUNCTIONAL SYMBOL IOTA UNDERBAR
        chars.append(0x2379)  #uni2379	APL FUNCTIONAL SYMBOL OMEGA UNDERBAR
        chars.append(0x237A)  #uni237A	APL FUNCTIONAL SYMBOL ALPHA
        chars.append(0x237B)  #uni237B	NOT CHECK MARK
        chars.append(0x237C)  #uni237C	RIGHT ANGLE WITH DOWNWARDS ZIGZAG ARROW
        chars.append(0x237D)  #uni237D	SHOULDERED OPEN BOX
        chars.append(0x237E)  #uni237E	BELL SYMBOL
        chars.append(0x237F)  #uni237F	VERTICAL LINE WITH MIDDLE DOT
        chars.append(0x2380)  #uni2380	INSERTION SYMBOL
        chars.append(0x2381)  #uni2381	CONTINUOUS UNDERLINE SYMBOL
        chars.append(0x2382)  #uni2382	DISCONTINUOUS UNDERLINE SYMBOL
        chars.append(0x2383)  #uni2383	EMPHASIS SYMBOL
        chars.append(0x2384)  #uni2384	COMPOSITION SYMBOL
        chars.append(0x2385)  #uni2385	WHITE SQUARE WITH CENTRE VERTICAL LINE
        chars.append(0x2386)  #uni2386	ENTER SYMBOL
        chars.append(0x2387)  #uni2387	ALTERNATIVE KEY SYMBOL
        chars.append(0x2388)  #uni2388	HELM SYMBOL
        chars.append(0x2389)  #uni2389	CIRCLED HORIZONTAL BAR WITH NOTCH
        chars.append(0x238A)  #uni238A	CIRCLED TRIANGLE DOWN
        chars.append(0x238B)  #uni238B	BROKEN CIRCLE WITH NORTHWEST ARROW
        chars.append(0x238C)  #uni238C	UNDO SYMBOL
        chars.append(0x238D)  #uni238D	MONOSTABLE SYMBOL
        chars.append(0x238E)  #uni238E	HYSTERESIS SYMBOL
        chars.append(0x238F)  #uni238F	OPEN-CIRCUIT-OUTPUT H-TYPE SYMBOL
        chars.append(0x2390)  #uni2390	OPEN-CIRCUIT-OUTPUT L-TYPE SYMBOL
        chars.append(0x2391)  #uni2391	PASSIVE-PULL-DOWN-OUTPUT SYMBOL
        chars.append(0x2392)  #uni2392	PASSIVE-PULL-UP-OUTPUT SYMBOL
        chars.append(0x2393)  #uni2393	DIRECT CURRENT SYMBOL FORM TWO
        chars.append(0x2394)  #uni2394	SOFTWARE-FUNCTION SYMBOL
        chars.append(0x2395)  #uni2395	APL FUNCTIONAL SYMBOL QUAD
        chars.append(0x2396)  #uni2396	DECIMAL SEPARATOR KEY SYMBOL
        chars.append(0x2397)  #uni2397	PREVIOUS PAGE
        chars.append(0x2398)  #uni2398	NEXT PAGE
        chars.append(0x2399)  #uni2399	PRINT SCREEN SYMBOL
        chars.append(0x239A)  #uni239A	CLEAR SCREEN SYMBOL
        chars.append(0x239B)  #uni239B	LEFT PARENTHESIS UPPER HOOK
        chars.append(0x239C)  #uni239C	LEFT PARENTHESIS EXTENSION
        chars.append(0x239D)  #uni239D	LEFT PARENTHESIS LOWER HOOK
        chars.append(0x239E)  #uni239E	RIGHT PARENTHESIS UPPER HOOK
        chars.append(0x239F)  #uni239F	RIGHT PARENTHESIS EXTENSION
        chars.append(0x23A0)  #uni23A0	RIGHT PARENTHESIS LOWER HOOK
        chars.append(0x23A1)  #uni23A1	LEFT SQUARE BRACKET UPPER CORNER
        chars.append(0x23A2)  #uni23A2	LEFT SQUARE BRACKET EXTENSION
        chars.append(0x23A3)  #uni23A3	LEFT SQUARE BRACKET LOWER CORNER
        chars.append(0x23A4)  #uni23A4	RIGHT SQUARE BRACKET UPPER CORNER
        chars.append(0x23A5)  #uni23A5	RIGHT SQUARE BRACKET EXTENSION
        chars.append(0x23A6)  #uni23A6	RIGHT SQUARE BRACKET LOWER CORNER
        chars.append(0x23A7)  #uni23A7	LEFT CURLY BRACKET UPPER HOOK
        chars.append(0x23A8)  #uni23A8	LEFT CURLY BRACKET MIDDLE PIECE
        chars.append(0x23A9)  #uni23A9	LEFT CURLY BRACKET LOWER HOOK
        chars.append(0x23AA)  #uni23AA	CURLY BRACKET EXTENSION
        chars.append(0x23AB)  #uni23AB	RIGHT CURLY BRACKET UPPER HOOK
        chars.append(0x23AC)  #uni23AC	RIGHT CURLY BRACKET MIDDLE PIECE
        chars.append(0x23AD)  #uni23AD	RIGHT CURLY BRACKET LOWER HOOK
        chars.append(0x23AE)  #uni23AE	INTEGRAL EXTENSION
        chars.append(0x23AF)  #uni23AF	HORIZONTAL LINE EXTENSION
        chars.append(0x23B0)  #uni23B0	UPPER LEFT OR LOWER RIGHT CURLY BRACKET SECTION
        chars.append(0x23B1)  #uni23B1	UPPER RIGHT OR LOWER LEFT CURLY BRACKET SECTION
        chars.append(0x23B2)  #uni23B2	SUMMATION TOP
        chars.append(0x23B3)  #uni23B3	SUMMATION BOTTOM
        chars.append(0x23B4)  #uni23B4	TOP SQUARE BRACKET
        chars.append(0x23B5)  #uni23B5	BOTTOM SQUARE BRACKET
        chars.append(0x23B6)  #uni23B6	BOTTOM SQUARE BRACKET OVER TOP SQUARE BRACKET
        chars.append(0x23B7)  #uni23B7	RADICAL SYMBOL BOTTOM
        chars.append(0x23B8)  #uni23B8	LEFT VERTICAL BOX LINE
        chars.append(0x23B9)  #uni23B9	RIGHT VERTICAL BOX LINE
        chars.append(0x23BA)  #uni23BA	HORIZONTAL SCAN LINE-1
        chars.append(0x23BB)  #uni23BB	HORIZONTAL SCAN LINE-3
        chars.append(0x23BC)  #uni23BC	HORIZONTAL SCAN LINE-7
        chars.append(0x23BD)  #uni23BD	HORIZONTAL SCAN LINE-9
        chars.append(0x23BE)  #uni23BE	DENTISTRY SYMBOL LIGHT VERTICAL AND TOP RIGHT
        chars.append(0x23BF)  #uni23BF	DENTISTRY SYMBOL LIGHT VERTICAL AND BOTTOM RIGHT
        chars.append(0x23C0)  #uni23C0	DENTISTRY SYMBOL LIGHT VERTICAL WITH CIRCLE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x23C2)  #uni23C2	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH CIRCLE
        chars.append(0x23C3)  #uni23C3	DENTISTRY SYMBOL LIGHT VERTICAL WITH TRIANGLE
        chars.append(0x23C4)  #uni23C4	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH TRIANGLE
        chars.append(0x23C5)  #uni23C5	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH TRIANGLE
        chars.append(0x23C6)  #uni23C6	DENTISTRY SYMBOL LIGHT VERTICAL AND WAVE
        chars.append(0x23C7)  #uni23C7	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH WAVE
        chars.append(0x23C8)  #uni23C8	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH WAVE
        chars.append(0x23C9)  #uni23C9	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL
        chars.append(0x23CA)  #uni23CA	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL
        chars.append(0x23CB)  #uni23CB	DENTISTRY SYMBOL LIGHT VERTICAL AND TOP LEFT
        chars.append(0x23CC)  #uni23CC	DENTISTRY SYMBOL LIGHT VERTICAL AND BOTTOM LEFT
        chars.append(0x23CD)  #uni23CD	SQUARE FOOT
        chars.append(0x23CE)  #uni23CE	RETURN SYMBOL
        chars.append(0x23CF)  #uni23CF	EJECT SYMBOL
        chars.append(0x23D0)  #uni23D0	VERTICAL LINE EXTENSION
        chars.append(0x23D1)  #uni23D1	METRICAL BREVE
        chars.append(0x23D2)  #uni23D2	METRICAL LONG OVER SHORT
        chars.append(0x23D3)  #uni23D3	METRICAL SHORT OVER LONG
        chars.append(0x23D4)  #uni23D4	METRICAL LONG OVER TWO SHORTS
        chars.append(0x23D5)  #uni23D5	METRICAL TWO SHORTS OVER LONG
        chars.append(0x23D6)  #uni23D6	METRICAL TWO SHORTS JOINED
        chars.append(0x23D7)  #uni23D7	METRICAL TRISEME
        chars.append(0x23D8)  #uni23D8	METRICAL TETRASEME
        chars.append(0x23D9)  #uni23D9	METRICAL PENTASEME
        chars.append(0x23DA)  #uni23DA	EARTH GROUND
        chars.append(0x23DB)  #uni23DB	FUSE
        chars.append(0x23DC)  #uni23DC	TOP PARENTHESIS
        chars.append(0x23DD)  #uni23DD	BOTTOM PARENTHESIS
        chars.append(0x23DE)  #uni23DE	TOP CURLY BRACKET
        chars.append(0x23DF)  #uni23DF	BOTTOM CURLY BRACKET
        chars.append(0x23E0)  #uni23E0	TOP TORTOISE SHELL BRACKET
        chars.append(0x23E1)  #uni23E1	BOTTOM TORTOISE SHELL BRACKET
        chars.append(0x23E2)  #uni23E2	WHITE TRAPEZIUM
        chars.append(0x23E3)  #uni23E3	BENZENE RING WITH CIRCLE
        chars.append(0x23E4)  #uni23E4	STRAIGHTNESS
        chars.append(0x23E5)  #uni23E5	FLATNESS
        chars.append(0x23E6)  #uni23E6	AC CURRENT
        chars.append(0x23E7)  #uni23E7	ELECTRICAL INTERSECTION
        chars.append(0x23E8)  #uni23E8	DECIMAL EXPONENT SYMBOL
        chars.append(0x23E9)  #uni23E9	????
        chars.append(0x23EA)  #uni23EA	????
        chars.append(0x23EB)  #uni23EB	????
        chars.append(0x23EC)  #uni23EC	????
        chars.append(0x23ED)  #uni23ED	????
        chars.append(0x23EE)  #uni23EE	????
        chars.append(0x23EF)  #uni23EF	????
        chars.append(0x23F0)  #uni23F0	????
        chars.append(0x23F1)  #uni23F1	????
        chars.append(0x23F2)  #uni23F2	????
        chars.append(0x23F3)  #uni23F3	????
        chars.append(0x2400)  #uni2400	SYMBOL FOR NULL
        chars.append(0x2401)  #uni2401	SYMBOL FOR START OF HEADING
        chars.append(0x2402)  #uni2402	SYMBOL FOR START OF TEXT
        chars.append(0x2403)  #uni2403	SYMBOL FOR END OF TEXT
        chars.append(0x2404)  #uni2404	SYMBOL FOR END OF TRANSMISSION
        chars.append(0x2405)  #uni2405	SYMBOL FOR ENQUIRY
        chars.append(0x2406)  #uni2406	SYMBOL FOR ACKNOWLEDGE
        chars.append(0x2407)  #uni2407	SYMBOL FOR BELL
        chars.append(0x2408)  #uni2408	SYMBOL FOR BACKSPACE
        chars.append(0x2409)  #uni2409	SYMBOL FOR HORIZONTAL TABULATION
        chars.append(0x240A)  #uni240A	SYMBOL FOR LINE FEED
        chars.append(0x240B)  #uni240B	SYMBOL FOR VERTICAL TABULATION
        chars.append(0x240C)  #uni240C	SYMBOL FOR FORM FEED
        chars.append(0x240D)  #uni240D	SYMBOL FOR CARRIAGE RETURN
        chars.append(0x240E)  #uni240E	SYMBOL FOR SHIFT OUT
        chars.append(0x240F)  #uni240F	SYMBOL FOR SHIFT IN
        chars.append(0x2410)  #uni2410	SYMBOL FOR DATA LINK ESCAPE
        chars.append(0x2411)  #uni2411	SYMBOL FOR DEVICE CONTROL ONE
        chars.append(0x2412)  #uni2412	SYMBOL FOR DEVICE CONTROL TWO
        chars.append(0x2413)  #uni2413	SYMBOL FOR DEVICE CONTROL THREE
        chars.append(0x2414)  #uni2414	SYMBOL FOR DEVICE CONTROL FOUR
        chars.append(0x2415)  #uni2415	SYMBOL FOR NEGATIVE ACKNOWLEDGE
        chars.append(0x2416)  #uni2416	SYMBOL FOR SYNCHRONOUS IDLE
        chars.append(0x2417)  #uni2417	SYMBOL FOR END OF TRANSMISSION BLOCK
        chars.append(0x2418)  #uni2418	SYMBOL FOR CANCEL
        chars.append(0x2419)  #uni2419	SYMBOL FOR END OF MEDIUM
        chars.append(0x241A)  #uni241A	SYMBOL FOR SUBSTITUTE
        chars.append(0x241B)  #uni241B	SYMBOL FOR ESCAPE
        chars.append(0x241C)  #uni241C	SYMBOL FOR FILE SEPARATOR
        chars.append(0x241D)  #uni241D	SYMBOL FOR GROUP SEPARATOR
        chars.append(0x241E)  #uni241E	SYMBOL FOR RECORD SEPARATOR
        chars.append(0x241F)  #uni241F	SYMBOL FOR UNIT SEPARATOR
        chars.append(0x2420)  #uni2420	SYMBOL FOR SPACE
        chars.append(0x2421)  #uni2421	SYMBOL FOR DELETE
        chars.append(0x2422)  #uni2422	BLANK SYMBOL
        chars.append(0x2423)  #uni2423	OPEN BOX
        chars.append(0x2424)  #uni2424	SYMBOL FOR NEWLINE
        chars.append(0x2425)  #uni2425	SYMBOL FOR DELETE FORM TWO
        chars.append(0x2426)  #uni2426	SYMBOL FOR SUBSTITUTE FORM TWO
        chars.append(0x2440)  #uni2440	OCR HOOK
        chars.append(0x2441)  #uni2441	OCR CHAIR
        chars.append(0x2442)  #uni2442	OCR FORK
        chars.append(0x2443)  #uni2443	OCR INVERTED FORK
        chars.append(0x2444)  #uni2444	OCR BELT BUCKLE
        chars.append(0x2445)  #uni2445	OCR BOW TIE
        chars.append(0x2446)  #uni2446	OCR BRANCH BANK IDENTIFICATION
        chars.append(0x2447)  #uni2447	OCR AMOUNT OF CHECK
        chars.append(0x2448)  #uni2448	OCR DASH
        chars.append(0x2449)  #uni2449	OCR CUSTOMER ACCOUNT NUMBER
        chars.append(0x244A)  #uni244A	OCR DOUBLE BACKSLASH
        chars.append(0x2460)  #uni2460	CIRCLED DIGIT ONE
        chars.append(0x2461)  #uni2461	CIRCLED DIGIT TWO
        chars.append(0x2462)  #uni2462	CIRCLED DIGIT THREE
        chars.append(0x2463)  #uni2463	CIRCLED DIGIT FOUR
        chars.append(0x2464)  #uni2464	CIRCLED DIGIT FIVE
        chars.append(0x2465)  #uni2465	CIRCLED DIGIT SIX
        chars.append(0x2466)  #uni2466	CIRCLED DIGIT SEVEN
        chars.append(0x2467)  #uni2467	CIRCLED DIGIT EIGHT
        chars.append(0x2468)  #uni2468	CIRCLED DIGIT NINE
        chars.append(0x2469)  #uni2469	CIRCLED NUMBER TEN
        chars.append(0x246A)  #uni246A	CIRCLED NUMBER ELEVEN
        chars.append(0x246B)  #uni246B	CIRCLED NUMBER TWELVE
        chars.append(0x246C)  #uni246C	CIRCLED NUMBER THIRTEEN
        chars.append(0x246D)  #uni246D	CIRCLED NUMBER FOURTEEN
        chars.append(0x246E)  #uni246E	CIRCLED NUMBER FIFTEEN
        chars.append(0x246F)  #uni246F	CIRCLED NUMBER SIXTEEN
        chars.append(0x2470)  #uni2470	CIRCLED NUMBER SEVENTEEN
        chars.append(0x2471)  #uni2471	CIRCLED NUMBER EIGHTEEN
        chars.append(0x2472)  #uni2472	CIRCLED NUMBER NINETEEN
        chars.append(0x2473)  #uni2473	CIRCLED NUMBER TWENTY
        chars.append(0x2474)  #uni2474	PARENTHESIZED DIGIT ONE
        chars.append(0x2475)  #uni2475	PARENTHESIZED DIGIT TWO
        chars.append(0x2476)  #uni2476	PARENTHESIZED DIGIT THREE
        chars.append(0x2477)  #uni2477	PARENTHESIZED DIGIT FOUR
        chars.append(0x2478)  #uni2478	PARENTHESIZED DIGIT FIVE
        chars.append(0x2479)  #uni2479	PARENTHESIZED DIGIT SIX
        chars.append(0x247A)  #uni247A	PARENTHESIZED DIGIT SEVEN
        chars.append(0x247B)  #uni247B	PARENTHESIZED DIGIT EIGHT
        chars.append(0x247C)  #uni247C	PARENTHESIZED DIGIT NINE
        chars.append(0x247D)  #uni247D	PARENTHESIZED NUMBER TEN
        chars.append(0x247E)  #uni247E	PARENTHESIZED NUMBER ELEVEN
        chars.append(0x247F)  #uni247F	PARENTHESIZED NUMBER TWELVE
        chars.append(0x2480)  #uni2480	PARENTHESIZED NUMBER THIRTEEN
        chars.append(0x2481)  #uni2481	PARENTHESIZED NUMBER FOURTEEN
        chars.append(0x2482)  #uni2482	PARENTHESIZED NUMBER FIFTEEN
        chars.append(0x2483)  #uni2483	PARENTHESIZED NUMBER SIXTEEN
        chars.append(0x2484)  #uni2484	PARENTHESIZED NUMBER SEVENTEEN
        chars.append(0x2485)  #uni2485	PARENTHESIZED NUMBER EIGHTEEN
        chars.append(0x2486)  #uni2486	PARENTHESIZED NUMBER NINETEEN
        chars.append(0x2487)  #uni2487	PARENTHESIZED NUMBER TWENTY
        chars.append(0x2488)  #uni2488	DIGIT ONE FULL STOP
        chars.append(0x2489)  #uni2489	DIGIT TWO FULL STOP
        chars.append(0x248A)  #uni248A	DIGIT THREE FULL STOP
        chars.append(0x248B)  #uni248B	DIGIT FOUR FULL STOP
        chars.append(0x248C)  #uni248C	DIGIT FIVE FULL STOP
        chars.append(0x248D)  #uni248D	DIGIT SIX FULL STOP
        chars.append(0x248E)  #uni248E	DIGIT SEVEN FULL STOP
        chars.append(0x248F)  #uni248F	DIGIT EIGHT FULL STOP
        chars.append(0x2490)  #uni2490	DIGIT NINE FULL STOP
        chars.append(0x2491)  #uni2491	NUMBER TEN FULL STOP
        chars.append(0x2492)  #uni2492	NUMBER ELEVEN FULL STOP
        chars.append(0x2493)  #uni2493	NUMBER TWELVE FULL STOP
        chars.append(0x2494)  #uni2494	NUMBER THIRTEEN FULL STOP
        chars.append(0x2495)  #uni2495	NUMBER FOURTEEN FULL STOP
        chars.append(0x2496)  #uni2496	NUMBER FIFTEEN FULL STOP
        chars.append(0x2497)  #uni2497	NUMBER SIXTEEN FULL STOP
        chars.append(0x2498)  #uni2498	NUMBER SEVENTEEN FULL STOP
        chars.append(0x2499)  #uni2499	NUMBER EIGHTEEN FULL STOP
        chars.append(0x249A)  #uni249A	NUMBER NINETEEN FULL STOP
        chars.append(0x249B)  #uni249B	NUMBER TWENTY FULL STOP
        chars.append(0x249C)  #uni249C	PARENTHESIZED LATIN SMALL LETTER A
        chars.append(0x249D)  #uni249D	PARENTHESIZED LATIN SMALL LETTER B
        chars.append(0x249E)  #uni249E	PARENTHESIZED LATIN SMALL LETTER C
        chars.append(0x249F)  #uni249F	PARENTHESIZED LATIN SMALL LETTER D
        chars.append(0x24A0)  #uni24A0	PARENTHESIZED LATIN SMALL LETTER E
        chars.append(0x24A1)  #uni24A1	PARENTHESIZED LATIN SMALL LETTER F
        chars.append(0x24A2)  #uni24A2	PARENTHESIZED LATIN SMALL LETTER G
        chars.append(0x24A3)  #uni24A3	PARENTHESIZED LATIN SMALL LETTER H
        chars.append(0x24A4)  #uni24A4	PARENTHESIZED LATIN SMALL LETTER I
        chars.append(0x24A5)  #uni24A5	PARENTHESIZED LATIN SMALL LETTER J
        chars.append(0x24A6)  #uni24A6	PARENTHESIZED LATIN SMALL LETTER K
        chars.append(0x24A7)  #uni24A7	PARENTHESIZED LATIN SMALL LETTER L
        chars.append(0x24A8)  #uni24A8	PARENTHESIZED LATIN SMALL LETTER M
        chars.append(0x24A9)  #uni24A9	PARENTHESIZED LATIN SMALL LETTER N
        chars.append(0x24AA)  #uni24AA	PARENTHESIZED LATIN SMALL LETTER O
        chars.append(0x24AB)  #uni24AB	PARENTHESIZED LATIN SMALL LETTER P
        chars.append(0x24AC)  #uni24AC	PARENTHESIZED LATIN SMALL LETTER Q
        chars.append(0x24AD)  #uni24AD	PARENTHESIZED LATIN SMALL LETTER R
        chars.append(0x24AE)  #uni24AE	PARENTHESIZED LATIN SMALL LETTER S
        chars.append(0x24AF)  #uni24AF	PARENTHESIZED LATIN SMALL LETTER T
        chars.append(0x24B0)  #uni24B0	PARENTHESIZED LATIN SMALL LETTER U
        chars.append(0x24B1)  #uni24B1	PARENTHESIZED LATIN SMALL LETTER V
        chars.append(0x24B2)  #uni24B2	PARENTHESIZED LATIN SMALL LETTER W
        chars.append(0x24B3)  #uni24B3	PARENTHESIZED LATIN SMALL LETTER X
        chars.append(0x24B4)  #uni24B4	PARENTHESIZED LATIN SMALL LETTER Y
        chars.append(0x24B5)  #uni24B5	PARENTHESIZED LATIN SMALL LETTER Z
        chars.append(0x24B6)  #uni24B6	CIRCLED LATIN CAPITAL LETTER A
        chars.append(0x24B7)  #uni24B7	CIRCLED LATIN CAPITAL LETTER B
        chars.append(0x24B8)  #uni24B8	CIRCLED LATIN CAPITAL LETTER C
        chars.append(0x24B9)  #uni24B9	CIRCLED LATIN CAPITAL LETTER D
        chars.append(0x24BA)  #uni24BA	CIRCLED LATIN CAPITAL LETTER E
        chars.append(0x24BB)  #uni24BB	CIRCLED LATIN CAPITAL LETTER F
        chars.append(0x24BC)  #uni24BC	CIRCLED LATIN CAPITAL LETTER G
        chars.append(0x24BD)  #uni24BD	CIRCLED LATIN CAPITAL LETTER H
        chars.append(0x24BE)  #uni24BE	CIRCLED LATIN CAPITAL LETTER I
        chars.append(0x24BF)  #uni24BF	CIRCLED LATIN CAPITAL LETTER J
        chars.append(0x24C0)  #uni24C0	CIRCLED LATIN CAPITAL LETTER K
        chars.append(0x24C1)  #uni24C1	CIRCLED LATIN CAPITAL LETTER L
        chars.append(0x24C2)  #uni24C2	CIRCLED LATIN CAPITAL LETTER M
        chars.append(0x24C3)  #uni24C3	CIRCLED LATIN CAPITAL LETTER N
        chars.append(0x24C4)  #uni24C4	CIRCLED LATIN CAPITAL LETTER O
        chars.append(0x24C5)  #uni24C5	CIRCLED LATIN CAPITAL LETTER P
        chars.append(0x24C6)  #uni24C6	CIRCLED LATIN CAPITAL LETTER Q
        chars.append(0x24C7)  #uni24C7	CIRCLED LATIN CAPITAL LETTER R
        chars.append(0x24C8)  #uni24C8	CIRCLED LATIN CAPITAL LETTER S
        chars.append(0x24C9)  #uni24C9	CIRCLED LATIN CAPITAL LETTER T
        chars.append(0x24CA)  #uni24CA	CIRCLED LATIN CAPITAL LETTER U
        chars.append(0x24CB)  #uni24CB	CIRCLED LATIN CAPITAL LETTER V
        chars.append(0x24CC)  #uni24CC	CIRCLED LATIN CAPITAL LETTER W
        chars.append(0x24CD)  #uni24CD	CIRCLED LATIN CAPITAL LETTER X
        chars.append(0x24CE)  #uni24CE	CIRCLED LATIN CAPITAL LETTER Y
        chars.append(0x24CF)  #uni24CF	CIRCLED LATIN CAPITAL LETTER Z
        chars.append(0x24D0)  #uni24D0	CIRCLED LATIN SMALL LETTER A
        chars.append(0x24D1)  #uni24D1	CIRCLED LATIN SMALL LETTER B
        chars.append(0x24D2)  #uni24D2	CIRCLED LATIN SMALL LETTER C
        chars.append(0x24D3)  #uni24D3	CIRCLED LATIN SMALL LETTER D
        chars.append(0x24D4)  #uni24D4	CIRCLED LATIN SMALL LETTER E
        chars.append(0x24D5)  #uni24D5	CIRCLED LATIN SMALL LETTER F
        chars.append(0x24D6)  #uni24D6	CIRCLED LATIN SMALL LETTER G
        chars.append(0x24D7)  #uni24D7	CIRCLED LATIN SMALL LETTER H
        chars.append(0x24D8)  #uni24D8	CIRCLED LATIN SMALL LETTER I
        chars.append(0x24D9)  #uni24D9	CIRCLED LATIN SMALL LETTER J
        chars.append(0x24DA)  #uni24DA	CIRCLED LATIN SMALL LETTER K
        chars.append(0x24DB)  #uni24DB	CIRCLED LATIN SMALL LETTER L
        chars.append(0x24DC)  #uni24DC	CIRCLED LATIN SMALL LETTER M
        chars.append(0x24DD)  #uni24DD	CIRCLED LATIN SMALL LETTER N
        chars.append(0x24DE)  #uni24DE	CIRCLED LATIN SMALL LETTER O
        chars.append(0x24DF)  #uni24DF	CIRCLED LATIN SMALL LETTER P
        chars.append(0x24E0)  #uni24E0	CIRCLED LATIN SMALL LETTER Q
        chars.append(0x24E1)  #uni24E1	CIRCLED LATIN SMALL LETTER R
        chars.append(0x24E2)  #uni24E2	CIRCLED LATIN SMALL LETTER S
        chars.append(0x24E3)  #uni24E3	CIRCLED LATIN SMALL LETTER T
        chars.append(0x24E4)  #uni24E4	CIRCLED LATIN SMALL LETTER U
        chars.append(0x24E5)  #uni24E5	CIRCLED LATIN SMALL LETTER V
        chars.append(0x24E6)  #uni24E6	CIRCLED LATIN SMALL LETTER W
        chars.append(0x24E7)  #uni24E7	CIRCLED LATIN SMALL LETTER X
        chars.append(0x24E8)  #uni24E8	CIRCLED LATIN SMALL LETTER Y
        chars.append(0x24E9)  #uni24E9	CIRCLED LATIN SMALL LETTER Z
        chars.append(0x24EA)  #uni24EA	CIRCLED DIGIT ZERO
        chars.append(0x24EB)  #uni24EB	NEGATIVE CIRCLED NUMBER ELEVEN
        chars.append(0x24EC)  #uni24EC	NEGATIVE CIRCLED NUMBER TWELVE
        chars.append(0x24ED)  #uni24ED	NEGATIVE CIRCLED NUMBER THIRTEEN
        chars.append(0x24EE)  #uni24EE	NEGATIVE CIRCLED NUMBER FOURTEEN
        chars.append(0x24EF)  #uni24EF	NEGATIVE CIRCLED NUMBER FIFTEEN
        chars.append(0x24F0)  #uni24F0	NEGATIVE CIRCLED NUMBER SIXTEEN
        chars.append(0x24F1)  #uni24F1	NEGATIVE CIRCLED NUMBER SEVENTEEN
        chars.append(0x24F2)  #uni24F2	NEGATIVE CIRCLED NUMBER EIGHTEEN
        chars.append(0x24F3)  #uni24F3	NEGATIVE CIRCLED NUMBER NINETEEN
        chars.append(0x24F4)  #uni24F4	NEGATIVE CIRCLED NUMBER TWENTY
        chars.append(0x24F5)  #uni24F5	DOUBLE CIRCLED DIGIT ONE
        chars.append(0x24F6)  #uni24F6	DOUBLE CIRCLED DIGIT TWO
        chars.append(0x24F7)  #uni24F7	DOUBLE CIRCLED DIGIT THREE
        chars.append(0x24F8)  #uni24F8	DOUBLE CIRCLED DIGIT FOUR
        chars.append(0x24F9)  #uni24F9	DOUBLE CIRCLED DIGIT FIVE
        chars.append(0x24FA)  #uni24FA	DOUBLE CIRCLED DIGIT SIX
        chars.append(0x24FB)  #uni24FB	DOUBLE CIRCLED DIGIT SEVEN
        chars.append(0x24FC)  #uni24FC	DOUBLE CIRCLED DIGIT EIGHT
        chars.append(0x24FD)  #uni24FD	DOUBLE CIRCLED DIGIT NINE
        chars.append(0x24FE)  #uni24FE	DOUBLE CIRCLED NUMBER TEN
        chars.append(0x24FF)  #uni24FF	NEGATIVE CIRCLED DIGIT ZERO
        chars.append(0x2500)  #SF100000	BOX DRAWINGS LIGHT HORIZONTAL
        chars.append(0x2501)  #uni2501	BOX DRAWINGS HEAVY HORIZONTAL
        chars.append(0x2502)  #SF110000	BOX DRAWINGS LIGHT VERTICAL
        chars.append(0x2503)  #uni2503	BOX DRAWINGS HEAVY VERTICAL
        chars.append(0x2504)  #uni2504	BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL
        chars.append(0x2505)  #uni2505	BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL
        chars.append(0x2506)  #uni2506	BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL
        chars.append(0x2507)  #uni2507	BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL
        chars.append(0x2508)  #uni2508	BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL
        chars.append(0x2509)  #uni2509	BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL
        chars.append(0x250A)  #uni250A	BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL
        chars.append(0x250B)  #uni250B	BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL
        chars.append(0x250C)  #SF010000	BOX DRAWINGS LIGHT DOWN AND RIGHT
        chars.append(0x250D)  #uni250D	BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY
        chars.append(0x250E)  #uni250E	BOX DRAWINGS DOWN HEAVY AND RIGHT LIGHT
        chars.append(0x250F)  #uni250F	BOX DRAWINGS HEAVY DOWN AND RIGHT
        chars.append(0x2510)  #SF030000	BOX DRAWINGS LIGHT DOWN AND LEFT
        chars.append(0x2511)  #uni2511	BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY
        chars.append(0x2512)  #uni2512	BOX DRAWINGS DOWN HEAVY AND LEFT LIGHT
        chars.append(0x2513)  #uni2513	BOX DRAWINGS HEAVY DOWN AND LEFT
        chars.append(0x2514)  #SF020000	BOX DRAWINGS LIGHT UP AND RIGHT
        chars.append(0x2515)  #uni2515	BOX DRAWINGS UP LIGHT AND RIGHT HEAVY
        chars.append(0x2516)  #uni2516	BOX DRAWINGS UP HEAVY AND RIGHT LIGHT
        chars.append(0x2517)  #uni2517	BOX DRAWINGS HEAVY UP AND RIGHT
        chars.append(0x2518)  #SF040000	BOX DRAWINGS LIGHT UP AND LEFT
        chars.append(0x2519)  #uni2519	BOX DRAWINGS UP LIGHT AND LEFT HEAVY
        chars.append(0x251A)  #uni251A	BOX DRAWINGS UP HEAVY AND LEFT LIGHT
        chars.append(0x251B)  #uni251B	BOX DRAWINGS HEAVY UP AND LEFT
        chars.append(0x251C)  #SF080000	BOX DRAWINGS LIGHT VERTICAL AND RIGHT
        chars.append(0x251D)  #uni251D	BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY
        chars.append(0x251E)  #uni251E	BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT
        chars.append(0x251F)  #uni251F	BOX DRAWINGS DOWN HEAVY AND RIGHT UP LIGHT
        chars.append(0x2520)  #uni2520	BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT
        chars.append(0x2521)  #uni2521	BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY
        chars.append(0x2522)  #uni2522	BOX DRAWINGS UP LIGHT AND RIGHT DOWN HEAVY
        chars.append(0x2523)  #uni2523	BOX DRAWINGS HEAVY VERTICAL AND RIGHT
        chars.append(0x2524)  #SF090000	BOX DRAWINGS LIGHT VERTICAL AND LEFT
        chars.append(0x2525)  #uni2525	BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY
        chars.append(0x2526)  #uni2526	BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT
        chars.append(0x2527)  #uni2527	BOX DRAWINGS DOWN HEAVY AND LEFT UP LIGHT
        chars.append(0x2528)  #uni2528	BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT
        chars.append(0x2529)  #uni2529	BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY
        chars.append(0x252A)  #uni252A	BOX DRAWINGS UP LIGHT AND LEFT DOWN HEAVY
        chars.append(0x252B)  #uni252B	BOX DRAWINGS HEAVY VERTICAL AND LEFT
        chars.append(0x252C)  #SF060000	BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
        chars.append(0x252D)  #uni252D	BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT
        chars.append(0x252E)  #uni252E	BOX DRAWINGS RIGHT HEAVY AND LEFT DOWN LIGHT
        chars.append(0x252F)  #uni252F	BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY
        chars.append(0x2530)  #uni2530	BOX DRAWINGS DOWN HEAVY AND HORIZONTAL LIGHT
        chars.append(0x2531)  #uni2531	BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY
        chars.append(0x2532)  #uni2532	BOX DRAWINGS LEFT LIGHT AND RIGHT DOWN HEAVY
        chars.append(0x2533)  #uni2533	BOX DRAWINGS HEAVY DOWN AND HORIZONTAL
        chars.append(0x2534)  #SF070000	BOX DRAWINGS LIGHT UP AND HORIZONTAL
        chars.append(0x2535)  #uni2535	BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT
        chars.append(0x2536)  #uni2536	BOX DRAWINGS RIGHT HEAVY AND LEFT UP LIGHT
        chars.append(0x2537)  #uni2537	BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY
        chars.append(0x2538)  #uni2538	BOX DRAWINGS UP HEAVY AND HORIZONTAL LIGHT
        chars.append(0x2539)  #uni2539	BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY
        chars.append(0x253A)  #uni253A	BOX DRAWINGS LEFT LIGHT AND RIGHT UP HEAVY
        chars.append(0x253B)  #uni253B	BOX DRAWINGS HEAVY UP AND HORIZONTAL
        chars.append(0x253C)  #SF050000	BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
        chars.append(0x253D)  #uni253D	BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT
        chars.append(0x253E)  #uni253E	BOX DRAWINGS RIGHT HEAVY AND LEFT VERTICAL LIGHT
        chars.append(0x253F)  #uni253F	BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY
        chars.append(0x2540)  #uni2540	BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT
        chars.append(0x2541)  #uni2541	BOX DRAWINGS DOWN HEAVY AND UP HORIZONTAL LIGHT
        chars.append(0x2542)  #uni2542	BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT
        chars.append(0x2543)  #uni2543	BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT
        chars.append(0x2544)  #uni2544	BOX DRAWINGS RIGHT UP HEAVY AND LEFT DOWN LIGHT
        chars.append(0x2545)  #uni2545	BOX DRAWINGS LEFT DOWN HEAVY AND RIGHT UP LIGHT
        chars.append(0x2546)  #uni2546	BOX DRAWINGS RIGHT DOWN HEAVY AND LEFT UP LIGHT
        chars.append(0x2547)  #uni2547	BOX DRAWINGS DOWN LIGHT AND UP HORIZONTAL HEAVY
        chars.append(0x2548)  #uni2548	BOX DRAWINGS UP LIGHT AND DOWN HORIZONTAL HEAVY
        chars.append(0x2549)  #uni2549	BOX DRAWINGS RIGHT LIGHT AND LEFT VERTICAL HEAVY
        chars.append(0x254A)  #uni254A	BOX DRAWINGS LEFT LIGHT AND RIGHT VERTICAL HEAVY
        chars.append(0x254B)  #uni254B	BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL
        chars.append(0x254C)  #uni254C	BOX DRAWINGS LIGHT DOUBLE DASH HORIZONTAL
        chars.append(0x254D)  #uni254D	BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL
        chars.append(0x254E)  #uni254E	BOX DRAWINGS LIGHT DOUBLE DASH VERTICAL
        chars.append(0x254F)  #uni254F	BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL
        chars.append(0x2550)  #SF430000	BOX DRAWINGS DOUBLE HORIZONTAL
        chars.append(0x2551)  #SF240000	BOX DRAWINGS DOUBLE VERTICAL
        chars.append(0x2552)  #SF510000	BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
        chars.append(0x2553)  #SF520000	BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
        chars.append(0x2554)  #SF390000	BOX DRAWINGS DOUBLE DOWN AND RIGHT
        chars.append(0x2555)  #SF220000	BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
        chars.append(0x2556)  #SF210000	BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
        chars.append(0x2557)  #SF250000	BOX DRAWINGS DOUBLE DOWN AND LEFT
        chars.append(0x2558)  #SF500000	BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
        chars.append(0x2559)  #SF490000	BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
        chars.append(0x255A)  #SF380000	BOX DRAWINGS DOUBLE UP AND RIGHT
        chars.append(0x255B)  #SF280000	BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
        chars.append(0x255C)  #SF270000	BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
        chars.append(0x255D)  #SF260000	BOX DRAWINGS DOUBLE UP AND LEFT
        chars.append(0x255E)  #SF360000	BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
        chars.append(0x255F)  #SF370000	BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
        chars.append(0x2560)  #SF420000	BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
        chars.append(0x2561)  #SF190000	BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
        chars.append(0x2562)  #SF200000	BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
        chars.append(0x2563)  #SF230000	BOX DRAWINGS DOUBLE VERTICAL AND LEFT
        chars.append(0x2564)  #SF470000	BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x2565)  #SF480000	BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x2566)  #SF410000	BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
        chars.append(0x2567)  #SF450000	BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x2568)  #SF460000	BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x2569)  #SF400000	BOX DRAWINGS DOUBLE UP AND HORIZONTAL
        chars.append(0x256A)  #SF540000	BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x256B)  #SF530000	BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x256C)  #SF440000	BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
        chars.append(0x256D)  #uni256D	BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
        chars.append(0x256E)  #uni256E	BOX DRAWINGS LIGHT ARC DOWN AND LEFT
        chars.append(0x256F)  #uni256F	BOX DRAWINGS LIGHT ARC UP AND LEFT
        chars.append(0x2570)  #uni2570	BOX DRAWINGS LIGHT ARC UP AND RIGHT
        chars.append(0x2571)  #uni2571	BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
        chars.append(0x2572)  #uni2572	BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
        chars.append(0x2573)  #uni2573	BOX DRAWINGS LIGHT DIAGONAL CROSS
        chars.append(0x2574)  #uni2574	BOX DRAWINGS LIGHT LEFT
        chars.append(0x2575)  #uni2575	BOX DRAWINGS LIGHT UP
        chars.append(0x2576)  #uni2576	BOX DRAWINGS LIGHT RIGHT
        chars.append(0x2577)  #uni2577	BOX DRAWINGS LIGHT DOWN
        chars.append(0x2578)  #uni2578	BOX DRAWINGS HEAVY LEFT
        chars.append(0x2579)  #uni2579	BOX DRAWINGS HEAVY UP
        chars.append(0x257A)  #uni257A	BOX DRAWINGS HEAVY RIGHT
        chars.append(0x257B)  #uni257B	BOX DRAWINGS HEAVY DOWN
        chars.append(0x257C)  #uni257C	BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT
        chars.append(0x257D)  #uni257D	BOX DRAWINGS LIGHT UP AND HEAVY DOWN
        chars.append(0x257E)  #uni257E	BOX DRAWINGS HEAVY LEFT AND LIGHT RIGHT
        chars.append(0x257F)  #uni257F	BOX DRAWINGS HEAVY UP AND LIGHT DOWN
        chars.append(0x2580)  #upblock	UPPER HALF BLOCK
        chars.append(0x2581)  #uni2581	LOWER ONE EIGHTH BLOCK
        chars.append(0x2582)  #uni2582	LOWER ONE QUARTER BLOCK
        chars.append(0x2583)  #uni2583	LOWER THREE EIGHTHS BLOCK
        chars.append(0x2584)  #dnblock	LOWER HALF BLOCK
        chars.append(0x2585)  #uni2585	LOWER FIVE EIGHTHS BLOCK
        chars.append(0x2586)  #uni2586	LOWER THREE QUARTERS BLOCK
        chars.append(0x2587)  #uni2587	LOWER SEVEN EIGHTHS BLOCK
        chars.append(0x2588)  #block	FULL BLOCK
        chars.append(0x2589)  #uni2589	LEFT SEVEN EIGHTHS BLOCK
        chars.append(0x258A)  #uni258A	LEFT THREE QUARTERS BLOCK
        chars.append(0x258B)  #uni258B	LEFT FIVE EIGHTHS BLOCK
        chars.append(0x258C)  #lfblock	LEFT HALF BLOCK
        chars.append(0x258D)  #uni258D	LEFT THREE EIGHTHS BLOCK
        chars.append(0x258E)  #uni258E	LEFT ONE QUARTER BLOCK
        chars.append(0x258F)  #uni258F	LEFT ONE EIGHTH BLOCK
        chars.append(0x2590)  #rtblock	RIGHT HALF BLOCK
        chars.append(0x2591)  #ltshade	LIGHT SHADE
        chars.append(0x2592)  #shade	MEDIUM SHADE
        chars.append(0x2593)  #dkshade	DARK SHADE
        chars.append(0x2594)  #uni2594	UPPER ONE EIGHTH BLOCK
        chars.append(0x2595)  #uni2595	RIGHT ONE EIGHTH BLOCK
        chars.append(0x2596)  #uni2596	QUADRANT LOWER LEFT
        chars.append(0x2597)  #uni2597	QUADRANT LOWER RIGHT
        chars.append(0x2598)  #uni2598	QUADRANT UPPER LEFT
        chars.append(0x2599)  #uni2599	QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT
        chars.append(0x259A)  #uni259A	QUADRANT UPPER LEFT AND LOWER RIGHT
        chars.append(0x259B)  #uni259B	QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT
        chars.append(0x259C)  #uni259C	QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT
        chars.append(0x259D)  #uni259D	QUADRANT UPPER RIGHT
        chars.append(0x259E)  #uni259E	QUADRANT UPPER RIGHT AND LOWER LEFT
        chars.append(0x259F)  #uni259F	QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT
        chars.append(0x25A0)  #filledbox	BLACK SQUARE
        chars.append(0x25A1)  #H22073	WHITE SQUARE
        chars.append(0x25A2)  #uni25A2	WHITE SQUARE WITH ROUNDED CORNERS
        chars.append(0x25A3)  #uni25A3	WHITE SQUARE CONTAINING BLACK SMALL SQUARE
        chars.append(0x25A4)  #uni25A4	SQUARE WITH HORIZONTAL FILL
        chars.append(0x25A5)  #uni25A5	SQUARE WITH VERTICAL FILL
        chars.append(0x25A6)  #uni25A6	SQUARE WITH ORTHOGONAL CROSSHATCH FILL
        chars.append(0x25A7)  #uni25A7	SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL
        chars.append(0x25A8)  #uni25A8	SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL
        chars.append(0x25A9)  #uni25A9	SQUARE WITH DIAGONAL CROSSHATCH FILL
        chars.append(0x25AA)  #H18543	BLACK SMALL SQUARE
        chars.append(0x25AB)  #H18551	WHITE SMALL SQUARE
        chars.append(0x25AC)  #filledrect	BLACK RECTANGLE
        chars.append(0x25AD)  #uni25AD	WHITE RECTANGLE
        chars.append(0x25AE)  #uni25AE	BLACK VERTICAL RECTANGLE
        chars.append(0x25AF)  #uni25AF	WHITE VERTICAL RECTANGLE
        chars.append(0x25B0)  #uni25B0	BLACK PARALLELOGRAM
        chars.append(0x25B1)  #uni25B1	WHITE PARALLELOGRAM
        chars.append(0x25B2)  #triagup	BLACK UP-POINTING TRIANGLE
        chars.append(0x25B3)  #uni25B3	WHITE UP-POINTING TRIANGLE
        chars.append(0x25B4)  #uni25B4	BLACK UP-POINTING SMALL TRIANGLE
        chars.append(0x25B5)  #uni25B5	WHITE UP-POINTING SMALL TRIANGLE
        chars.append(0x25B6)  #uni25B6	BLACK RIGHT-POINTING TRIANGLE
        chars.append(0x25B7)  #uni25B7	WHITE RIGHT-POINTING TRIANGLE
        chars.append(0x25B8)  #uni25B8	BLACK RIGHT-POINTING SMALL TRIANGLE
        chars.append(0x25B9)  #uni25B9	WHITE RIGHT-POINTING SMALL TRIANGLE
        chars.append(0x25BA)  #triagrt	BLACK RIGHT-POINTING POINTER
        chars.append(0x25BB)  #uni25BB	WHITE RIGHT-POINTING POINTER
        chars.append(0x25BC)  #triagdn	BLACK DOWN-POINTING TRIANGLE
        chars.append(0x25BD)  #uni25BD	WHITE DOWN-POINTING TRIANGLE
        chars.append(0x25BE)  #uni25BE	BLACK DOWN-POINTING SMALL TRIANGLE
        chars.append(0x25BF)  #uni25BF	WHITE DOWN-POINTING SMALL TRIANGLE
        chars.append(0x25C0)  #uni25C0	BLACK LEFT-POINTING TRIANGLE
        chars.append(0x25C1)  #uni25C1	WHITE LEFT-POINTING TRIANGLE
        chars.append(0x25C2)  #uni25C2	BLACK LEFT-POINTING SMALL TRIANGLE
        chars.append(0x25C3)  #uni25C3	WHITE LEFT-POINTING SMALL TRIANGLE
        chars.append(0x25C4)  #triaglf	BLACK LEFT-POINTING POINTER
        chars.append(0x25C5)  #uni25C5	WHITE LEFT-POINTING POINTER
        chars.append(0x25C6)  #uni25C6	BLACK DIAMOND
        chars.append(0x25C7)  #uni25C7	WHITE DIAMOND
        chars.append(0x25C8)  #uni25C8	WHITE DIAMOND CONTAINING BLACK SMALL DIAMOND
        chars.append(0x25C9)  #uni25C9	FISHEYE
        chars.append(0x25CA)  #lozenge	LOZENGE
        chars.append(0x25CB)  #circle	WHITE CIRCLE
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x25CD)  #uni25CD	CIRCLE WITH VERTICAL FILL
        chars.append(0x25CE)  #uni25CE	BULLSEYE
        chars.append(0x25CF)  #H18533	BLACK CIRCLE
        chars.append(0x25D0)  #uni25D0	CIRCLE WITH LEFT HALF BLACK
        chars.append(0x25D1)  #uni25D1	CIRCLE WITH RIGHT HALF BLACK
        chars.append(0x25D2)  #uni25D2	CIRCLE WITH LOWER HALF BLACK
        chars.append(0x25D3)  #uni25D3	CIRCLE WITH UPPER HALF BLACK
        chars.append(0x25D4)  #uni25D4	CIRCLE WITH UPPER RIGHT QUADRANT BLACK
        chars.append(0x25D5)  #uni25D5	CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK
        chars.append(0x25D6)  #uni25D6	LEFT HALF BLACK CIRCLE
        chars.append(0x25D7)  #uni25D7	RIGHT HALF BLACK CIRCLE
        chars.append(0x25D8)  #invbullet	INVERSE BULLET
        chars.append(0x25D9)  #invcircle	INVERSE WHITE CIRCLE
        chars.append(0x25DA)  #uni25DA	UPPER HALF INVERSE WHITE CIRCLE
        chars.append(0x25DB)  #uni25DB	LOWER HALF INVERSE WHITE CIRCLE
        chars.append(0x25DC)  #uni25DC	UPPER LEFT QUADRANT CIRCULAR ARC
        chars.append(0x25DD)  #uni25DD	UPPER RIGHT QUADRANT CIRCULAR ARC
        chars.append(0x25DE)  #uni25DE	LOWER RIGHT QUADRANT CIRCULAR ARC
        chars.append(0x25DF)  #uni25DF	LOWER LEFT QUADRANT CIRCULAR ARC
        chars.append(0x25E0)  #uni25E0	UPPER HALF CIRCLE
        chars.append(0x25E1)  #uni25E1	LOWER HALF CIRCLE
        chars.append(0x25E2)  #uni25E2	BLACK LOWER RIGHT TRIANGLE
        chars.append(0x25E3)  #uni25E3	BLACK LOWER LEFT TRIANGLE
        chars.append(0x25E4)  #uni25E4	BLACK UPPER LEFT TRIANGLE
        chars.append(0x25E5)  #uni25E5	BLACK UPPER RIGHT TRIANGLE
        chars.append(0x25E6)  #openbullet	WHITE BULLET
        chars.append(0x25E7)  #uni25E7	SQUARE WITH LEFT HALF BLACK
        chars.append(0x25E8)  #uni25E8	SQUARE WITH RIGHT HALF BLACK
        chars.append(0x25E9)  #uni25E9	SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK
        chars.append(0x25EA)  #uni25EA	SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK
        chars.append(0x25EB)  #uni25EB	WHITE SQUARE WITH VERTICAL BISECTING LINE
        chars.append(0x25EC)  #uni25EC	WHITE UP-POINTING TRIANGLE WITH DOT
        chars.append(0x25ED)  #uni25ED	UP-POINTING TRIANGLE WITH LEFT HALF BLACK
        chars.append(0x25EE)  #uni25EE	UP-POINTING TRIANGLE WITH RIGHT HALF BLACK
        chars.append(0x25EF)  #uni25EF	LARGE CIRCLE
        chars.append(0x25F0)  #uni25F0	WHITE SQUARE WITH UPPER LEFT QUADRANT
        chars.append(0x25F1)  #uni25F1	WHITE SQUARE WITH LOWER LEFT QUADRANT
        chars.append(0x25F2)  #uni25F2	WHITE SQUARE WITH LOWER RIGHT QUADRANT
        chars.append(0x25F3)  #uni25F3	WHITE SQUARE WITH UPPER RIGHT QUADRANT
        chars.append(0x25F4)  #uni25F4	WHITE CIRCLE WITH UPPER LEFT QUADRANT
        chars.append(0x25F5)  #uni25F5	WHITE CIRCLE WITH LOWER LEFT QUADRANT
        chars.append(0x25F6)  #uni25F6	WHITE CIRCLE WITH LOWER RIGHT QUADRANT
        chars.append(0x25F7)  #uni25F7	WHITE CIRCLE WITH UPPER RIGHT QUADRANT
        chars.append(0x25F8)  #uni25F8	UPPER LEFT TRIANGLE
        chars.append(0x25F9)  #uni25F9	UPPER RIGHT TRIANGLE
        chars.append(0x25FA)  #uni25FA	LOWER LEFT TRIANGLE
        chars.append(0x25FB)  #uni25FB	WHITE MEDIUM SQUARE
        chars.append(0x25FC)  #uni25FC	BLACK MEDIUM SQUARE
        chars.append(0x25FD)  #uni25FD	WHITE MEDIUM SMALL SQUARE
        chars.append(0x25FE)  #uni25FE	BLACK MEDIUM SMALL SQUARE
        chars.append(0x25FF)  #uni25FF	LOWER RIGHT TRIANGLE
        chars.append(0x2600)  #uni2600	BLACK SUN WITH RAYS
        chars.append(0x2601)  #uni2601	CLOUD
        chars.append(0x2602)  #uni2602	UMBRELLA
        chars.append(0x2603)  #uni2603	SNOWMAN
        chars.append(0x2604)  #uni2604	COMET
        chars.append(0x2605)  #uni2605	BLACK STAR
        chars.append(0x2606)  #uni2606	WHITE STAR
        chars.append(0x2607)  #uni2607	LIGHTNING
        chars.append(0x2608)  #uni2608	THUNDERSTORM
        chars.append(0x2609)  #uni2609	SUN
        chars.append(0x260A)  #uni260A	ASCENDING NODE
        chars.append(0x260B)  #uni260B	DESCENDING NODE
        chars.append(0x260C)  #uni260C	CONJUNCTION
        chars.append(0x260D)  #uni260D	OPPOSITION
        chars.append(0x260E)  #uni260E	BLACK TELEPHONE
        chars.append(0x260F)  #uni260F	WHITE TELEPHONE
        chars.append(0x2610)  #uni2610	BALLOT BOX
        chars.append(0x2611)  #uni2611	BALLOT BOX WITH CHECK
        chars.append(0x2612)  #uni2612	BALLOT BOX WITH X
        chars.append(0x2613)  #uni2613	SALTIRE
        chars.append(0x2614)  #uni2614	UMBRELLA WITH RAIN DROPS
        chars.append(0x2615)  #uni2615	HOT BEVERAGE
        chars.append(0x2616)  #uni2616	WHITE SHOGI PIECE
        chars.append(0x2617)  #uni2617	BLACK SHOGI PIECE
        chars.append(0x2618)  #uni2618	SHAMROCK
        chars.append(0x2619)  #uni2619	REVERSED ROTATED FLORAL HEART BULLET
        chars.append(0x261A)  #uni261A	BLACK LEFT POINTING INDEX
        chars.append(0x261B)  #uni261B	BLACK RIGHT POINTING INDEX
        chars.append(0x261C)  #uni261C	WHITE LEFT POINTING INDEX
        chars.append(0x261D)  #uni261D	WHITE UP POINTING INDEX
        chars.append(0x261E)  #uni261E	WHITE RIGHT POINTING INDEX
        chars.append(0x261F)  #uni261F	WHITE DOWN POINTING INDEX
        chars.append(0x2620)  #uni2620	SKULL AND CROSSBONES
        chars.append(0x2621)  #uni2621	CAUTION SIGN
        chars.append(0x2622)  #uni2622	RADIOACTIVE SIGN
        chars.append(0x2623)  #uni2623	BIOHAZARD SIGN
        chars.append(0x2624)  #uni2624	CADUCEUS
        chars.append(0x2625)  #uni2625	ANKH
        chars.append(0x2626)  #uni2626	ORTHODOX CROSS
        chars.append(0x2627)  #uni2627	CHI RHO
        chars.append(0x2628)  #uni2628	CROSS OF LORRAINE
        chars.append(0x2629)  #uni2629	CROSS OF JERUSALEM
        chars.append(0x262A)  #uni262A	STAR AND CRESCENT
        chars.append(0x262B)  #uni262B	FARSI SYMBOL
        chars.append(0x262C)  #uni262C	ADI SHAKTI
        chars.append(0x262D)  #uni262D	HAMMER AND SICKLE
        chars.append(0x262E)  #uni262E	PEACE SYMBOL
        chars.append(0x262F)  #uni262F	YIN YANG
        chars.append(0x2630)  #uni2630	TRIGRAM FOR HEAVEN
        chars.append(0x2631)  #uni2631	TRIGRAM FOR LAKE
        chars.append(0x2632)  #uni2632	TRIGRAM FOR FIRE
        chars.append(0x2633)  #uni2633	TRIGRAM FOR THUNDER
        chars.append(0x2634)  #uni2634	TRIGRAM FOR WIND
        chars.append(0x2635)  #uni2635	TRIGRAM FOR WATER
        chars.append(0x2636)  #uni2636	TRIGRAM FOR MOUNTAIN
        chars.append(0x2637)  #uni2637	TRIGRAM FOR EARTH
        chars.append(0x2638)  #uni2638	WHEEL OF DHARMA
        chars.append(0x2639)  #uni2639	WHITE FROWNING FACE
        chars.append(0x263A)  #smileface	WHITE SMILING FACE
        chars.append(0x263B)  #invsmileface	BLACK SMILING FACE
        chars.append(0x263C)  #sun	WHITE SUN WITH RAYS
        chars.append(0x263D)  #uni263D	FIRST QUARTER MOON
        chars.append(0x263E)  #uni263E	LAST QUARTER MOON
        chars.append(0x263F)  #uni263F	MERCURY
        chars.append(0x2640)  #female	FEMALE SIGN
        chars.append(0x2641)  #uni2641	EARTH
        chars.append(0x2642)  #male	MALE SIGN
        chars.append(0x2643)  #uni2643	JUPITER
        chars.append(0x2644)  #uni2644	SATURN
        chars.append(0x2645)  #uni2645	URANUS
        chars.append(0x2646)  #uni2646	NEPTUNE
        chars.append(0x2647)  #uni2647	PLUTO
        chars.append(0x2648)  #uni2648	ARIES
        chars.append(0x2649)  #uni2649	TAURUS
        chars.append(0x264A)  #uni264A	GEMINI
        chars.append(0x264B)  #uni264B	CANCER
        chars.append(0x264C)  #uni264C	LEO
        chars.append(0x264D)  #uni264D	VIRGO
        chars.append(0x264E)  #uni264E	LIBRA
        chars.append(0x264F)  #uni264F	SCORPIUS
        chars.append(0x2650)  #uni2650	SAGITTARIUS
        chars.append(0x2651)  #uni2651	CAPRICORN
        chars.append(0x2652)  #uni2652	AQUARIUS
        chars.append(0x2653)  #uni2653	PISCES
        chars.append(0x2654)  #uni2654	WHITE CHESS KING
        chars.append(0x2655)  #uni2655	WHITE CHESS QUEEN
        chars.append(0x2656)  #uni2656	WHITE CHESS ROOK
        chars.append(0x2657)  #uni2657	WHITE CHESS BISHOP
        chars.append(0x2658)  #uni2658	WHITE CHESS KNIGHT
        chars.append(0x2659)  #uni2659	WHITE CHESS PAWN
        chars.append(0x265A)  #uni265A	BLACK CHESS KING
        chars.append(0x265B)  #uni265B	BLACK CHESS QUEEN
        chars.append(0x265C)  #uni265C	BLACK CHESS ROOK
        chars.append(0x265D)  #uni265D	BLACK CHESS BISHOP
        chars.append(0x265E)  #uni265E	BLACK CHESS KNIGHT
        chars.append(0x265F)  #uni265F	BLACK CHESS PAWN
        chars.append(0x2660)  #spade	BLACK SPADE SUIT
        chars.append(0x2661)  #uni2661	WHITE HEART SUIT
        chars.append(0x2662)  #uni2662	WHITE DIAMOND SUIT
        chars.append(0x2663)  #club	BLACK CLUB SUIT
        chars.append(0x2664)  #uni2664	WHITE SPADE SUIT
        chars.append(0x2665)  #heart	BLACK HEART SUIT
        chars.append(0x2666)  #diamond	BLACK DIAMOND SUIT
        chars.append(0x2667)  #uni2667	WHITE CLUB SUIT
        chars.append(0x2668)  #uni2668	HOT SPRINGS
        chars.append(0x2669)  #uni2669	QUARTER NOTE
        chars.append(0x266A)  #musicalnote	EIGHTH NOTE
        chars.append(0x266B)  #musicalnotedbl	BEAMED EIGHTH NOTES
        chars.append(0x266C)  #uni266C	BEAMED SIXTEENTH NOTES
        chars.append(0x266D)  #uni266D	MUSIC FLAT SIGN
        chars.append(0x266E)  #uni266E	MUSIC NATURAL SIGN
        chars.append(0x266F)  #uni266F	MUSIC SHARP SIGN
        chars.append(0x2670)  #uni2670	WEST SYRIAC CROSS
        chars.append(0x2671)  #uni2671	EAST SYRIAC CROSS
        chars.append(0x2672)  #uni2672	UNIVERSAL RECYCLING SYMBOL
        chars.append(0x2673)  #uni2673	RECYCLING SYMBOL FOR TYPE-1 PLASTICS
        chars.append(0x2674)  #uni2674	RECYCLING SYMBOL FOR TYPE-2 PLASTICS
        chars.append(0x2675)  #uni2675	RECYCLING SYMBOL FOR TYPE-3 PLASTICS
        chars.append(0x2676)  #uni2676	RECYCLING SYMBOL FOR TYPE-4 PLASTICS
        chars.append(0x2677)  #uni2677	RECYCLING SYMBOL FOR TYPE-5 PLASTICS
        chars.append(0x2678)  #uni2678	RECYCLING SYMBOL FOR TYPE-6 PLASTICS
        chars.append(0x2679)  #uni2679	RECYCLING SYMBOL FOR TYPE-7 PLASTICS
        chars.append(0x267A)  #uni267A	RECYCLING SYMBOL FOR GENERIC MATERIALS
        chars.append(0x267B)  #uni267B	BLACK UNIVERSAL RECYCLING SYMBOL
        chars.append(0x267C)  #uni267C	RECYCLED PAPER SYMBOL
        chars.append(0x267D)  #uni267D	PARTIALLY-RECYCLED PAPER SYMBOL
        chars.append(0x267E)  #uni267E	PERMANENT PAPER SIGN
        chars.append(0x267F)  #uni267F	WHEELCHAIR SYMBOL
        chars.append(0x2680)  #uni2680	DIE FACE-1
        chars.append(0x2681)  #uni2681	DIE FACE-2
        chars.append(0x2682)  #uni2682	DIE FACE-3
        chars.append(0x2683)  #uni2683	DIE FACE-4
        chars.append(0x2684)  #uni2684	DIE FACE-5
        chars.append(0x2685)  #uni2685	DIE FACE-6
        chars.append(0x2686)  #uni2686	WHITE CIRCLE WITH DOT RIGHT
        chars.append(0x2687)  #uni2687	WHITE CIRCLE WITH TWO DOTS
        chars.append(0x2688)  #uni2688	BLACK CIRCLE WITH WHITE DOT RIGHT
        chars.append(0x2689)  #uni2689	BLACK CIRCLE WITH TWO WHITE DOTS
        chars.append(0x268A)  #uni268A	MONOGRAM FOR YANG
        chars.append(0x268B)  #uni268B	MONOGRAM FOR YIN
        chars.append(0x268C)  #uni268C	DIGRAM FOR GREATER YANG
        chars.append(0x268D)  #uni268D	DIGRAM FOR LESSER YIN
        chars.append(0x268E)  #uni268E	DIGRAM FOR LESSER YANG
        chars.append(0x268F)  #uni268F	DIGRAM FOR GREATER YIN
        chars.append(0x2690)  #uni2690	WHITE FLAG
        chars.append(0x2691)  #uni2691	BLACK FLAG
        chars.append(0x2692)  #uni2692	HAMMER AND PICK
        chars.append(0x2693)  #uni2693	ANCHOR
        chars.append(0x2694)  #uni2694	CROSSED SWORDS
        chars.append(0x2695)  #uni2695	STAFF OF AESCULAPIUS
        chars.append(0x2696)  #uni2696	SCALES
        chars.append(0x2697)  #uni2697	ALEMBIC
        chars.append(0x2698)  #uni2698	FLOWER
        chars.append(0x2699)  #uni2699	GEAR
        chars.append(0x269A)  #uni269A	STAFF OF HERMES
        chars.append(0x269B)  #uni269B	ATOM SYMBOL
        chars.append(0x269C)  #uni269C	FLEUR-DE-LIS
        chars.append(0x269D)  #uni269D	OUTLINED WHITE STAR
        chars.append(0x269E)  #uni269E	THREE LINES CONVERGING RIGHT
        chars.append(0x269F)  #uni269F	THREE LINES CONVERGING LEFT
        chars.append(0x26A0)  #uni26A0	WARNING SIGN
        chars.append(0x26A1)  #uni26A1	HIGH VOLTAGE SIGN
        chars.append(0x26A2)  #uni26A2	DOUBLED FEMALE SIGN
        chars.append(0x26A3)  #uni26A3	DOUBLED MALE SIGN
        chars.append(0x26A4)  #uni26A4	INTERLOCKED FEMALE AND MALE SIGN
        chars.append(0x26A5)  #uni26A5	MALE AND FEMALE SIGN
        chars.append(0x26A6)  #uni26A6	MALE WITH STROKE SIGN
        chars.append(0x26A7)  #uni26A7	MALE WITH STROKE AND MALE AND FEMALE SIGN
        chars.append(0x26A8)  #uni26A8	VERTICAL MALE WITH STROKE SIGN
        chars.append(0x26A9)  #uni26A9	HORIZONTAL MALE WITH STROKE SIGN
        chars.append(0x26AA)  #uni26AA	MEDIUM WHITE CIRCLE
        chars.append(0x26AB)  #uni26AB	MEDIUM BLACK CIRCLE
        chars.append(0x26AC)  #uni26AC	MEDIUM SMALL WHITE CIRCLE
        chars.append(0x26AD)  #uni26AD	MARRIAGE SYMBOL
        chars.append(0x26AE)  #uni26AE	DIVORCE SYMBOL
        chars.append(0x26AF)  #uni26AF	UNMARRIED PARTNERSHIP SYMBOL
        chars.append(0x26B0)  #uni26B0	COFFIN
        chars.append(0x26B1)  #uni26B1	FUNERAL URN
        chars.append(0x26B2)  #uni26B2	NEUTER
        chars.append(0x26B3)  #uni26B3	CERES
        chars.append(0x26B4)  #uni26B4	PALLAS
        chars.append(0x26B5)  #uni26B5	JUNO
        chars.append(0x26B6)  #uni26B6	VESTA
        chars.append(0x26B7)  #uni26B7	CHIRON
        chars.append(0x26B8)  #uni26B8	BLACK MOON LILITH
        chars.append(0x26B9)  #uni26B9	SEXTILE
        chars.append(0x26BA)  #uni26BA	SEMISEXTILE
        chars.append(0x26BB)  #uni26BB	QUINCUNX
        chars.append(0x26BC)  #uni26BC	SESQUIQUADRATE
        chars.append(0x26BD)  #uni26BD	SOCCER BALL
        chars.append(0x26BE)  #uni26BE	BASEBALL
        chars.append(0x26BF)  #uni26BF	SQUARED KEY
        chars.append(0x26C0)  #uni26C0	WHITE DRAUGHTS MAN
        chars.append(0x26C1)  #uni26C1	WHITE DRAUGHTS KING
        chars.append(0x26C2)  #uni26C2	BLACK DRAUGHTS MAN
        chars.append(0x26C3)  #uni26C3	BLACK DRAUGHTS KING
        chars.append(0x26C4)  #uni26C4	SNOWMAN WITHOUT SNOW
        chars.append(0x26C5)  #uni26C5	SUN BEHIND CLOUD
        chars.append(0x26C6)  #uni26C6	RAIN
        chars.append(0x26C7)  #uni26C7	BLACK SNOWMAN
        chars.append(0x26C8)  #uni26C8	THUNDER CLOUD AND RAIN
        chars.append(0x26C9)  #uni26C9	TURNED WHITE SHOGI PIECE
        chars.append(0x26CA)  #uni26CA	TURNED BLACK SHOGI PIECE
        chars.append(0x26CB)  #uni26CB	WHITE DIAMOND IN SQUARE
        chars.append(0x26CC)  #uni26CC	CROSSING LANES
        chars.append(0x26CD)  #uni26CD	DISABLED CAR
        chars.append(0x26CE)  #uni26CE	????
        chars.append(0x26CF)  #uni26CF	PICK
        chars.append(0x26D0)  #uni26D0	CAR SLIDING
        chars.append(0x26D1)  #uni26D1	HELMET WITH WHITE CROSS
        chars.append(0x26D2)  #uni26D2	CIRCLED CROSSING LANES
        chars.append(0x26D3)  #uni26D3	CHAINS
        chars.append(0x26D4)  #uni26D4	NO ENTRY
        chars.append(0x26D5)  #uni26D5	ALTERNATE ONE-WAY LEFT WAY TRAFFIC
        chars.append(0x26D6)  #uni26D6	BLACK TWO-WAY LEFT WAY TRAFFIC
        chars.append(0x26D7)  #uni26D7	WHITE TWO-WAY LEFT WAY TRAFFIC
        chars.append(0x26D8)  #uni26D8	BLACK LEFT LANE MERGE
        chars.append(0x26D9)  #uni26D9	WHITE LEFT LANE MERGE
        chars.append(0x26DA)  #uni26DA	DRIVE SLOW SIGN
        chars.append(0x26DB)  #uni26DB	HEAVY WHITE DOWN-POINTING TRIANGLE
        chars.append(0x26DC)  #uni26DC	LEFT CLOSED ENTRY
        chars.append(0x26DD)  #uni26DD	SQUARED SALTIRE
        chars.append(0x26DE)  #uni26DE	FALLING DIAGONAL IN WHITE CIRCLE IN BLACK SQUARE
        chars.append(0x26DF)  #uni26DF	BLACK TRUCK
        chars.append(0x26E0)  #uni26E0	RESTRICTED LEFT ENTRY-1
        chars.append(0x26E1)  #uni26E1	RESTRICTED LEFT ENTRY-2
        chars.append(0x26E2)  #uni26E2	????
        chars.append(0x26E3)  #uni26E3	HEAVY CIRCLE WITH STROKE AND TWO DOTS ABOVE
        chars.append(0x26E4)  #uni26E4	????
        chars.append(0x26E5)  #uni26E5	????
        chars.append(0x26E6)  #uni26E6	????
        chars.append(0x26E7)  #uni26E7	????
        chars.append(0x26E8)  #uni26E8	BLACK CROSS ON SHIELD
        chars.append(0x26E9)  #uni26E9	SHINTO SHRINE
        chars.append(0x26EA)  #uni26EA	CHURCH
        chars.append(0x26EB)  #uni26EB	CASTLE
        chars.append(0x26EC)  #uni26EC	HISTORIC SITE
        chars.append(0x26ED)  #uni26ED	GEAR WITHOUT HUB
        chars.append(0x26EE)  #uni26EE	GEAR WITH HANDLES
        chars.append(0x26EF)  #uni26EF	MAP SYMBOL FOR LIGHTHOUSE
        chars.append(0x26F0)  #uni26F0	MOUNTAIN
        chars.append(0x26F1)  #uni26F1	UMBRELLA ON GROUND
        chars.append(0x26F2)  #uni26F2	FOUNTAIN
        chars.append(0x26F3)  #uni26F3	FLAG IN HOLE
        chars.append(0x26F4)  #uni26F4	FERRY
        chars.append(0x26F5)  #uni26F5	SAILBOAT
        chars.append(0x26F6)  #uni26F6	SQUARE FOUR CORNERS
        chars.append(0x26F7)  #uni26F7	SKIER
        chars.append(0x26F8)  #uni26F8	ICE SKATE
        chars.append(0x26F9)  #uni26F9	PERSON WITH BALL
        chars.append(0x26FA)  #uni26FA	TENT
        chars.append(0x26FB)  #uni26FB	JAPANESE BANK SYMBOL
        chars.append(0x26FC)  #uni26FC	HEADSTONE GRAVEYARD SYMBOL
        chars.append(0x26FD)  #uni26FD	FUEL PUMP
        chars.append(0x26FE)  #uni26FE	CUP ON BLACK SQUARE
        chars.append(0x26FF)  #uni26FF	WHITE FLAG WITH HORIZONTAL MIDDLE BLACK STRIPE
        chars.append(0xA700)  #uniA700	MODIFIER LETTER CHINESE TONE YIN PING
        chars.append(0x2701)  #uni2701	UPPER BLADE SCISSORS
        chars.append(0x2702)  #uni2702	BLACK SCISSORS
        chars.append(0x2703)  #uni2703	LOWER BLADE SCISSORS
        chars.append(0x2704)  #uni2704	WHITE SCISSORS
        chars.append(0x2705)  #uni2705	????
        chars.append(0x2706)  #uni2706	TELEPHONE LOCATION SIGN
        chars.append(0x2707)  #uni2707	TAPE DRIVE
        chars.append(0x2708)  #uni2708	AIRPLANE
        chars.append(0x2709)  #uni2709	ENVELOPE
        chars.append(0x270A)  #uni270A	????
        chars.append(0x270B)  #uni270B	????
        chars.append(0x270C)  #uni270C	VICTORY HAND
        chars.append(0x270D)  #uni270D	WRITING HAND
        chars.append(0x270E)  #uni270E	LOWER RIGHT PENCIL
        chars.append(0x270F)  #uni270F	PENCIL
        chars.append(0x2710)  #uni2710	UPPER RIGHT PENCIL
        chars.append(0x2711)  #uni2711	WHITE NIB
        chars.append(0x2712)  #uni2712	BLACK NIB
        chars.append(0x2713)  #uni2713	CHECK MARK
        chars.append(0x2714)  #uni2714	HEAVY CHECK MARK
        chars.append(0x2715)  #uni2715	MULTIPLICATION X
        chars.append(0x2716)  #uni2716	HEAVY MULTIPLICATION X
        chars.append(0x2717)  #uni2717	BALLOT X
        chars.append(0x2718)  #uni2718	HEAVY BALLOT X
        chars.append(0x2719)  #uni2719	OUTLINED GREEK CROSS
        chars.append(0x271A)  #uni271A	HEAVY GREEK CROSS
        chars.append(0x271B)  #uni271B	OPEN CENTRE CROSS
        chars.append(0x271C)  #uni271C	HEAVY OPEN CENTRE CROSS
        chars.append(0x271D)  #uni271D	LATIN CROSS
        chars.append(0x271E)  #uni271E	SHADOWED WHITE LATIN CROSS
        chars.append(0x271F)  #uni271F	OUTLINED LATIN CROSS
        chars.append(0x2720)  #uni2720	MALTESE CROSS
        chars.append(0x2721)  #uni2721	STAR OF DAVID
        chars.append(0x2722)  #uni2722	FOUR TEARDROP-SPOKED ASTERISK
        chars.append(0x2723)  #uni2723	FOUR BALLOON-SPOKED ASTERISK
        chars.append(0x2724)  #uni2724	HEAVY FOUR BALLOON-SPOKED ASTERISK
        chars.append(0x2725)  #uni2725	FOUR CLUB-SPOKED ASTERISK
        chars.append(0x2726)  #uni2726	BLACK FOUR POINTED STAR
        chars.append(0x2727)  #uni2727	WHITE FOUR POINTED STAR
        chars.append(0x2728)  #uni2728	????
        chars.append(0x2729)  #uni2729	STRESS OUTLINED WHITE STAR
        chars.append(0x272A)  #uni272A	CIRCLED WHITE STAR
        chars.append(0x272B)  #uni272B	OPEN CENTRE BLACK STAR
        chars.append(0x272C)  #uni272C	BLACK CENTRE WHITE STAR
        chars.append(0x272D)  #uni272D	OUTLINED BLACK STAR
        chars.append(0x272E)  #uni272E	HEAVY OUTLINED BLACK STAR
        chars.append(0x272F)  #uni272F	PINWHEEL STAR
        chars.append(0x2730)  #uni2730	SHADOWED WHITE STAR
        chars.append(0x2731)  #uni2731	HEAVY ASTERISK
        chars.append(0x2732)  #uni2732	OPEN CENTRE ASTERISK
        chars.append(0x2733)  #uni2733	EIGHT SPOKED ASTERISK
        chars.append(0x2734)  #uni2734	EIGHT POINTED BLACK STAR
        chars.append(0x2735)  #uni2735	EIGHT POINTED PINWHEEL STAR
        chars.append(0x2736)  #uni2736	SIX POINTED BLACK STAR
        chars.append(0x2737)  #uni2737	EIGHT POINTED RECTILINEAR BLACK STAR
        chars.append(0x2738)  #uni2738	HEAVY EIGHT POINTED RECTILINEAR BLACK STAR
        chars.append(0x2739)  #uni2739	TWELVE POINTED BLACK STAR
        chars.append(0x273A)  #uni273A	SIXTEEN POINTED ASTERISK
        chars.append(0x273B)  #uni273B	TEARDROP-SPOKED ASTERISK
        chars.append(0x273C)  #uni273C	OPEN CENTRE TEARDROP-SPOKED ASTERISK
        chars.append(0x273D)  #uni273D	HEAVY TEARDROP-SPOKED ASTERISK
        chars.append(0x273E)  #uni273E	SIX PETALLED BLACK AND WHITE FLORETTE
        chars.append(0x273F)  #uni273F	BLACK FLORETTE
        chars.append(0x2740)  #uni2740	WHITE FLORETTE
        chars.append(0x2741)  #uni2741	EIGHT PETALLED OUTLINED BLACK FLORETTE
        chars.append(0x2742)  #uni2742	CIRCLED OPEN CENTRE EIGHT POINTED STAR
        chars.append(0x2743)  #uni2743	HEAVY TEARDROP-SPOKED PINWHEEL ASTERISK
        chars.append(0x2744)  #uni2744	SNOWFLAKE
        chars.append(0x2745)  #uni2745	TIGHT TRIFOLIATE SNOWFLAKE
        chars.append(0x2746)  #uni2746	HEAVY CHEVRON SNOWFLAKE
        chars.append(0x2747)  #uni2747	SPARKLE
        chars.append(0x2748)  #uni2748	HEAVY SPARKLE
        chars.append(0x2749)  #uni2749	BALLOON-SPOKED ASTERISK
        chars.append(0x274A)  #uni274A	EIGHT TEARDROP-SPOKED PROPELLER ASTERISK
        chars.append(0x274B)  #uni274B	HEAVY EIGHT TEARDROP-SPOKED PROPELLER ASTERISK
        chars.append(0x274C)  #uni274C	????
        chars.append(0x274D)  #uni274D	SHADOWED WHITE CIRCLE
        chars.append(0x274E)  #uni274E	????
        chars.append(0x274F)  #uni274F	LOWER RIGHT DROP-SHADOWED WHITE SQUARE
        chars.append(0x2750)  #uni2750	UPPER RIGHT DROP-SHADOWED WHITE SQUARE
        chars.append(0x2751)  #uni2751	LOWER RIGHT SHADOWED WHITE SQUARE
        chars.append(0x2752)  #uni2752	UPPER RIGHT SHADOWED WHITE SQUARE
        chars.append(0x2753)  #uni2753	????
        chars.append(0x2754)  #uni2754	????
        chars.append(0x2755)  #uni2755	????
        chars.append(0x2756)  #uni2756	BLACK DIAMOND MINUS WHITE X
        chars.append(0x2757)  #uni2757	HEAVY EXCLAMATION MARK SYMBOL
        chars.append(0x2758)  #uni2758	LIGHT VERTICAL BAR
        chars.append(0x2759)  #uni2759	MEDIUM VERTICAL BAR
        chars.append(0x275A)  #uni275A	HEAVY VERTICAL BAR
        chars.append(0x275B)  #uni275B	HEAVY SINGLE TURNED COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275C)  #uni275C	HEAVY SINGLE COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275D)  #uni275D	HEAVY DOUBLE TURNED COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275E)  #uni275E	HEAVY DOUBLE COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275F)  #uni275F	????
        chars.append(0x2760)  #uni2760	????
        chars.append(0x2761)  #uni2761	CURVED STEM PARAGRAPH SIGN ORNAMENT
        chars.append(0x2762)  #uni2762	HEAVY EXCLAMATION MARK ORNAMENT
        chars.append(0x2763)  #uni2763	HEAVY HEART EXCLAMATION MARK ORNAMENT
        chars.append(0x2764)  #uni2764	HEAVY BLACK HEART
        chars.append(0x2765)  #uni2765	ROTATED HEAVY BLACK HEART BULLET
        chars.append(0x2766)  #uni2766	FLORAL HEART
        chars.append(0x2767)  #uni2767	ROTATED FLORAL HEART BULLET
        chars.append(0x2768)  #uni2768	MEDIUM LEFT PARENTHESIS ORNAMENT
        chars.append(0x2769)  #uni2769	MEDIUM RIGHT PARENTHESIS ORNAMENT
        chars.append(0x276A)  #uni276A	MEDIUM FLATTENED LEFT PARENTHESIS ORNAMENT
        chars.append(0x276B)  #uni276B	MEDIUM FLATTENED RIGHT PARENTHESIS ORNAMENT
        chars.append(0x276C)  #uni276C	MEDIUM LEFT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x276D)  #uni276D	MEDIUM RIGHT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x276E)  #uni276E	HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT
        chars.append(0x276F)  #uni276F	HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT
        chars.append(0x2770)  #uni2770	HEAVY LEFT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x2771)  #uni2771	HEAVY RIGHT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x2772)  #uni2772	LIGHT LEFT TORTOISE SHELL BRACKET ORNAMENT
        chars.append(0x2773)  #uni2773	LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT
        chars.append(0x2774)  #uni2774	MEDIUM LEFT CURLY BRACKET ORNAMENT
        chars.append(0x2775)  #uni2775	MEDIUM RIGHT CURLY BRACKET ORNAMENT
        chars.append(0x2776)  #uni2776	DINGBAT NEGATIVE CIRCLED DIGIT ONE
        chars.append(0x2777)  #uni2777	DINGBAT NEGATIVE CIRCLED DIGIT TWO
        chars.append(0x2778)  #uni2778	DINGBAT NEGATIVE CIRCLED DIGIT THREE
        chars.append(0x2779)  #uni2779	DINGBAT NEGATIVE CIRCLED DIGIT FOUR
        chars.append(0x277A)  #uni277A	DINGBAT NEGATIVE CIRCLED DIGIT FIVE
        chars.append(0x277B)  #uni277B	DINGBAT NEGATIVE CIRCLED DIGIT SIX
        chars.append(0x277C)  #uni277C	DINGBAT NEGATIVE CIRCLED DIGIT SEVEN
        chars.append(0x277D)  #uni277D	DINGBAT NEGATIVE CIRCLED DIGIT EIGHT
        chars.append(0x277E)  #uni277E	DINGBAT NEGATIVE CIRCLED DIGIT NINE
        chars.append(0x277F)  #uni277F	DINGBAT NEGATIVE CIRCLED NUMBER TEN
        chars.append(0x2780)  #uni2780	DINGBAT CIRCLED SANS-SERIF DIGIT ONE
        chars.append(0x2781)  #uni2781	DINGBAT CIRCLED SANS-SERIF DIGIT TWO
        chars.append(0x2782)  #uni2782	DINGBAT CIRCLED SANS-SERIF DIGIT THREE
        chars.append(0x2783)  #uni2783	DINGBAT CIRCLED SANS-SERIF DIGIT FOUR
        chars.append(0x2784)  #uni2784	DINGBAT CIRCLED SANS-SERIF DIGIT FIVE
        chars.append(0x2785)  #uni2785	DINGBAT CIRCLED SANS-SERIF DIGIT SIX
        chars.append(0x2786)  #uni2786	DINGBAT CIRCLED SANS-SERIF DIGIT SEVEN
        chars.append(0x2787)  #uni2787	DINGBAT CIRCLED SANS-SERIF DIGIT EIGHT
        chars.append(0x2788)  #uni2788	DINGBAT CIRCLED SANS-SERIF DIGIT NINE
        chars.append(0x2789)  #uni2789	DINGBAT CIRCLED SANS-SERIF NUMBER TEN
        chars.append(0x278A)  #uni278A	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT ONE
        chars.append(0x278B)  #uni278B	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT TWO
        chars.append(0x278C)  #uni278C	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT THREE
        chars.append(0x278D)  #uni278D	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT FOUR
        chars.append(0x278E)  #uni278E	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT FIVE
        chars.append(0x278F)  #uni278F	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT SIX
        chars.append(0x2790)  #uni2790	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT SEVEN
        chars.append(0x2791)  #uni2791	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT EIGHT
        chars.append(0x2792)  #uni2792	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT NINE
        chars.append(0x2793)  #uni2793	DINGBAT NEGATIVE CIRCLED SANS-SERIF NUMBER TEN
        chars.append(0x2794)  #uni2794	HEAVY WIDE-HEADED RIGHTWARDS ARROW
        chars.append(0x2795)  #uni2795	????
        chars.append(0x2796)  #uni2796	????
        chars.append(0x2797)  #uni2797	????
        chars.append(0x2798)  #uni2798	HEAVY SOUTH EAST ARROW
        chars.append(0x2799)  #uni2799	HEAVY RIGHTWARDS ARROW
        chars.append(0x279A)  #uni279A	HEAVY NORTH EAST ARROW
        chars.append(0x279B)  #uni279B	DRAFTING POINT RIGHTWARDS ARROW
        chars.append(0x279C)  #uni279C	HEAVY ROUND-TIPPED RIGHTWARDS ARROW
        chars.append(0x279D)  #uni279D	TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x279E)  #uni279E	HEAVY TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x279F)  #uni279F	DASHED TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x27A0)  #uni27A0	HEAVY DASHED TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x27A1)  #uni27A1	BLACK RIGHTWARDS ARROW
        chars.append(0x27A2)  #uni27A2	THREE-D TOP-LIGHTED RIGHTWARDS ARROWHEAD
        chars.append(0x27A3)  #uni27A3	THREE-D BOTTOM-LIGHTED RIGHTWARDS ARROWHEAD
        chars.append(0x27A4)  #uni27A4	BLACK RIGHTWARDS ARROWHEAD
        chars.append(0x27A5)  #uni27A5	HEAVY BLACK CURVED DOWNWARDS AND RIGHTWARDS ARROW
        chars.append(0x27A6)  #uni27A6	HEAVY BLACK CURVED UPWARDS AND RIGHTWARDS ARROW
        chars.append(0x27A7)  #uni27A7	SQUAT BLACK RIGHTWARDS ARROW
        chars.append(0x27A8)  #uni27A8	HEAVY CONCAVE-POINTED BLACK RIGHTWARDS ARROW
        chars.append(0x27A9)  #uni27A9	RIGHT-SHADED WHITE RIGHTWARDS ARROW
        chars.append(0x27AA)  #uni27AA	LEFT-SHADED WHITE RIGHTWARDS ARROW
        chars.append(0x27AB)  #uni27AB	BACK-TILTED SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AC)  #uni27AC	FRONT-TILTED SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AD)  #uni27AD	HEAVY LOWER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AE)  #uni27AE	HEAVY UPPER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AF)  #uni27AF	NOTCHED LOWER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27B0)  #uni27B0	????
        chars.append(0x27B1)  #uni27B1	NOTCHED UPPER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27B2)  #uni27B2	CIRCLED HEAVY WHITE RIGHTWARDS ARROW
        chars.append(0x27B3)  #uni27B3	WHITE-FEATHERED RIGHTWARDS ARROW
        chars.append(0x27B4)  #uni27B4	BLACK-FEATHERED SOUTH EAST ARROW
        chars.append(0x27B5)  #uni27B5	BLACK-FEATHERED RIGHTWARDS ARROW
        chars.append(0x27B6)  #uni27B6	BLACK-FEATHERED NORTH EAST ARROW
        chars.append(0x27B7)  #uni27B7	HEAVY BLACK-FEATHERED SOUTH EAST ARROW
        chars.append(0x27B8)  #uni27B8	HEAVY BLACK-FEATHERED RIGHTWARDS ARROW
        chars.append(0x27B9)  #uni27B9	HEAVY BLACK-FEATHERED NORTH EAST ARROW
        chars.append(0x27BA)  #uni27BA	TEARDROP-BARBED RIGHTWARDS ARROW
        chars.append(0x27BB)  #uni27BB	HEAVY TEARDROP-SHANKED RIGHTWARDS ARROW
        chars.append(0x27BC)  #uni27BC	WEDGE-TAILED RIGHTWARDS ARROW
        chars.append(0x27BD)  #uni27BD	HEAVY WEDGE-TAILED RIGHTWARDS ARROW
        chars.append(0x27BE)  #uni27BE	OPEN-OUTLINED RIGHTWARDS ARROW
        chars.append(0x27BF)  #uni27BF	????
        chars.append(0x27C0)  #uni27C0	THREE DIMENSIONAL ANGLE
        chars.append(0x27C1)  #uni27C1	WHITE TRIANGLE CONTAINING SMALL WHITE TRIANGLE
        chars.append(0x27C2)  #uni27C2	PERPENDICULAR
        chars.append(0x27C3)  #uni27C3	OPEN SUBSET
        chars.append(0x27C4)  #uni27C4	OPEN SUPERSET
        chars.append(0x27C5)  #uni27C5	LEFT S-SHAPED BAG DELIMITER
        chars.append(0x27C6)  #uni27C6	RIGHT S-SHAPED BAG DELIMITER
        chars.append(0x27C7)  #uni27C7	OR WITH DOT INSIDE
        chars.append(0x27C8)  #uni27C8	REVERSE SOLIDUS PRECEDING SUBSET
        chars.append(0x27C9)  #uni27C9	SUPERSET PRECEDING SOLIDUS
        chars.append(0x27CA)  #uni27CA	VERTICAL BAR WITH HORIZONTAL STROKE
        chars.append(0x27CB)  #uni27CB	????
        chars.append(0x27CC)  #uni27CC	LONG DIVISION
        chars.append(0x27CD)  #uni27CD	????
        chars.append(0x27CE)  #uni27CE	????
        chars.append(0x27CF)  #uni27CF	????
        chars.append(0x27D0)  #uni27D0	WHITE DIAMOND WITH CENTRED DOT
        chars.append(0x27D1)  #uni27D1	AND WITH DOT
        chars.append(0x27D2)  #uni27D2	ELEMENT OF OPENING UPWARDS
        chars.append(0x27D3)  #uni27D3	LOWER RIGHT CORNER WITH DOT
        chars.append(0x27D4)  #uni27D4	UPPER LEFT CORNER WITH DOT
        chars.append(0x27D5)  #uni27D5	LEFT OUTER JOIN
        chars.append(0x27D6)  #uni27D6	RIGHT OUTER JOIN
        chars.append(0x27D7)  #uni27D7	FULL OUTER JOIN
        chars.append(0x27D8)  #uni27D8	LARGE UP TACK
        chars.append(0x27D9)  #uni27D9	LARGE DOWN TACK
        chars.append(0x27DA)  #uni27DA	LEFT AND RIGHT DOUBLE TURNSTILE
        chars.append(0x27DB)  #uni27DB	LEFT AND RIGHT TACK
        chars.append(0x27DC)  #uni27DC	LEFT MULTIMAP
        chars.append(0x27DD)  #uni27DD	LONG RIGHT TACK
        chars.append(0x27DE)  #uni27DE	LONG LEFT TACK
        chars.append(0x27DF)  #uni27DF	UP TACK WITH CIRCLE ABOVE
        chars.append(0x27E0)  #uni27E0	LOZENGE DIVIDED BY HORIZONTAL RULE
        chars.append(0x27E1)  #uni27E1	WHITE CONCAVE-SIDED DIAMOND
        chars.append(0x27E2)  #uni27E2	WHITE CONCAVE-SIDED DIAMOND WITH LEFTWARDS TICK
        chars.append(0x27E3)  #uni27E3	WHITE CONCAVE-SIDED DIAMOND WITH RIGHTWARDS TICK
        chars.append(0x27E4)  #uni27E4	WHITE SQUARE WITH LEFTWARDS TICK
        chars.append(0x27E5)  #uni27E5	WHITE SQUARE WITH RIGHTWARDS TICK
        chars.append(0x27E6)  #uni27E6	MATHEMATICAL LEFT WHITE SQUARE BRACKET
        chars.append(0x27E7)  #uni27E7	MATHEMATICAL RIGHT WHITE SQUARE BRACKET
        chars.append(0x27E8)  #uni27E8	MATHEMATICAL LEFT ANGLE BRACKET
        chars.append(0x27E9)  #uni27E9	MATHEMATICAL RIGHT ANGLE BRACKET
        chars.append(0x27EA)  #uni27EA	MATHEMATICAL LEFT DOUBLE ANGLE BRACKET
        chars.append(0x27EB)  #uni27EB	MATHEMATICAL RIGHT DOUBLE ANGLE BRACKET
        chars.append(0x27EC)  #uni27EC	MATHEMATICAL LEFT WHITE TORTOISE SHELL BRACKET
        chars.append(0x27ED)  #uni27ED	MATHEMATICAL RIGHT WHITE TORTOISE SHELL BRACKET
        chars.append(0x27EE)  #uni27EE	MATHEMATICAL LEFT FLATTENED PARENTHESIS
        chars.append(0x27EF)  #uni27EF	MATHEMATICAL RIGHT FLATTENED PARENTHESIS
        chars.append(0x27F0)  #uni27F0	UPWARDS QUADRUPLE ARROW
        chars.append(0x27F1)  #uni27F1	DOWNWARDS QUADRUPLE ARROW
        chars.append(0x27F2)  #uni27F2	ANTICLOCKWISE GAPPED CIRCLE ARROW
        chars.append(0x27F3)  #uni27F3	CLOCKWISE GAPPED CIRCLE ARROW
        chars.append(0x27F4)  #uni27F4	RIGHT ARROW WITH CIRCLED PLUS
        chars.append(0x27F5)  #uni27F5	LONG LEFTWARDS ARROW
        chars.append(0x27F6)  #uni27F6	LONG RIGHTWARDS ARROW
        chars.append(0x27F7)  #uni27F7	LONG LEFT RIGHT ARROW
        chars.append(0x27F8)  #uni27F8	LONG LEFTWARDS DOUBLE ARROW
        chars.append(0x27F9)  #uni27F9	LONG RIGHTWARDS DOUBLE ARROW
        chars.append(0x27FA)  #uni27FA	LONG LEFT RIGHT DOUBLE ARROW
        chars.append(0x27FB)  #uni27FB	LONG LEFTWARDS ARROW FROM BAR
        chars.append(0x27FC)  #uni27FC	LONG RIGHTWARDS ARROW FROM BAR
        chars.append(0x27FD)  #uni27FD	LONG LEFTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x27FE)  #uni27FE	LONG RIGHTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x27FF)  #uni27FF	LONG RIGHTWARDS SQUIGGLE ARROW
        chars.append(0x2800)  #uni2800	BRAILLE PATTERN BLANK
        chars.append(0x2801)  #uni2801	BRAILLE PATTERN DOTS-1
        chars.append(0x2802)  #uni2802	BRAILLE PATTERN DOTS-2
        chars.append(0x2803)  #uni2803	BRAILLE PATTERN DOTS-12
        chars.append(0x2804)  #uni2804	BRAILLE PATTERN DOTS-3
        chars.append(0x2805)  #uni2805	BRAILLE PATTERN DOTS-13
        chars.append(0x2806)  #uni2806	BRAILLE PATTERN DOTS-23
        chars.append(0x2807)  #uni2807	BRAILLE PATTERN DOTS-123
        chars.append(0x2808)  #uni2808	BRAILLE PATTERN DOTS-4
        chars.append(0x2809)  #uni2809	BRAILLE PATTERN DOTS-14
        chars.append(0x280A)  #uni280A	BRAILLE PATTERN DOTS-24
        chars.append(0x280B)  #uni280B	BRAILLE PATTERN DOTS-124
        chars.append(0x280C)  #uni280C	BRAILLE PATTERN DOTS-34
        chars.append(0x280D)  #uni280D	BRAILLE PATTERN DOTS-134
        chars.append(0x280E)  #uni280E	BRAILLE PATTERN DOTS-234
        chars.append(0x280F)  #uni280F	BRAILLE PATTERN DOTS-1234
        chars.append(0x2810)  #uni2810	BRAILLE PATTERN DOTS-5
        chars.append(0x2811)  #uni2811	BRAILLE PATTERN DOTS-15
        chars.append(0x2812)  #uni2812	BRAILLE PATTERN DOTS-25
        chars.append(0x2813)  #uni2813	BRAILLE PATTERN DOTS-125
        chars.append(0x2814)  #uni2814	BRAILLE PATTERN DOTS-35
        chars.append(0x2815)  #uni2815	BRAILLE PATTERN DOTS-135
        chars.append(0x2816)  #uni2816	BRAILLE PATTERN DOTS-235
        chars.append(0x2817)  #uni2817	BRAILLE PATTERN DOTS-1235
        chars.append(0x2818)  #uni2818	BRAILLE PATTERN DOTS-45
        chars.append(0x2819)  #uni2819	BRAILLE PATTERN DOTS-145
        chars.append(0x281A)  #uni281A	BRAILLE PATTERN DOTS-245
        chars.append(0x281B)  #uni281B	BRAILLE PATTERN DOTS-1245
        chars.append(0x281C)  #uni281C	BRAILLE PATTERN DOTS-345
        chars.append(0x281D)  #uni281D	BRAILLE PATTERN DOTS-1345
        chars.append(0x281E)  #uni281E	BRAILLE PATTERN DOTS-2345
        chars.append(0x281F)  #uni281F	BRAILLE PATTERN DOTS-12345
        chars.append(0x2820)  #uni2820	BRAILLE PATTERN DOTS-6
        chars.append(0x2821)  #uni2821	BRAILLE PATTERN DOTS-16
        chars.append(0x2822)  #uni2822	BRAILLE PATTERN DOTS-26
        chars.append(0x2823)  #uni2823	BRAILLE PATTERN DOTS-126
        chars.append(0x2824)  #uni2824	BRAILLE PATTERN DOTS-36
        chars.append(0x2825)  #uni2825	BRAILLE PATTERN DOTS-136
        chars.append(0x2826)  #uni2826	BRAILLE PATTERN DOTS-236
        chars.append(0x2827)  #uni2827	BRAILLE PATTERN DOTS-1236
        chars.append(0x2828)  #uni2828	BRAILLE PATTERN DOTS-46
        chars.append(0x2829)  #uni2829	BRAILLE PATTERN DOTS-146
        chars.append(0x282A)  #uni282A	BRAILLE PATTERN DOTS-246
        chars.append(0x282B)  #uni282B	BRAILLE PATTERN DOTS-1246
        chars.append(0x282C)  #uni282C	BRAILLE PATTERN DOTS-346
        chars.append(0x282D)  #uni282D	BRAILLE PATTERN DOTS-1346
        chars.append(0x282E)  #uni282E	BRAILLE PATTERN DOTS-2346
        chars.append(0x282F)  #uni282F	BRAILLE PATTERN DOTS-12346
        chars.append(0x2830)  #uni2830	BRAILLE PATTERN DOTS-56
        chars.append(0x2831)  #uni2831	BRAILLE PATTERN DOTS-156
        chars.append(0x2832)  #uni2832	BRAILLE PATTERN DOTS-256
        chars.append(0x2833)  #uni2833	BRAILLE PATTERN DOTS-1256
        chars.append(0x2834)  #uni2834	BRAILLE PATTERN DOTS-356
        chars.append(0x2835)  #uni2835	BRAILLE PATTERN DOTS-1356
        chars.append(0x2836)  #uni2836	BRAILLE PATTERN DOTS-2356
        chars.append(0x2837)  #uni2837	BRAILLE PATTERN DOTS-12356
        chars.append(0x2838)  #uni2838	BRAILLE PATTERN DOTS-456
        chars.append(0x2839)  #uni2839	BRAILLE PATTERN DOTS-1456
        chars.append(0x283A)  #uni283A	BRAILLE PATTERN DOTS-2456
        chars.append(0x283B)  #uni283B	BRAILLE PATTERN DOTS-12456
        chars.append(0x283C)  #uni283C	BRAILLE PATTERN DOTS-3456
        chars.append(0x283D)  #uni283D	BRAILLE PATTERN DOTS-13456
        chars.append(0x283E)  #uni283E	BRAILLE PATTERN DOTS-23456
        chars.append(0x283F)  #uni283F	BRAILLE PATTERN DOTS-123456
        chars.append(0x2840)  #uni2840	BRAILLE PATTERN DOTS-7
        chars.append(0x2841)  #uni2841	BRAILLE PATTERN DOTS-17
        chars.append(0x2842)  #uni2842	BRAILLE PATTERN DOTS-27
        chars.append(0x2843)  #uni2843	BRAILLE PATTERN DOTS-127
        chars.append(0x2844)  #uni2844	BRAILLE PATTERN DOTS-37
        chars.append(0x2845)  #uni2845	BRAILLE PATTERN DOTS-137
        chars.append(0x2846)  #uni2846	BRAILLE PATTERN DOTS-237
        chars.append(0x2847)  #uni2847	BRAILLE PATTERN DOTS-1237
        chars.append(0x2848)  #uni2848	BRAILLE PATTERN DOTS-47
        chars.append(0x2849)  #uni2849	BRAILLE PATTERN DOTS-147
        chars.append(0x284A)  #uni284A	BRAILLE PATTERN DOTS-247
        chars.append(0x284B)  #uni284B	BRAILLE PATTERN DOTS-1247
        chars.append(0x284C)  #uni284C	BRAILLE PATTERN DOTS-347
        chars.append(0x284D)  #uni284D	BRAILLE PATTERN DOTS-1347
        chars.append(0x284E)  #uni284E	BRAILLE PATTERN DOTS-2347
        chars.append(0x284F)  #uni284F	BRAILLE PATTERN DOTS-12347
        chars.append(0x2850)  #uni2850	BRAILLE PATTERN DOTS-57
        chars.append(0x2851)  #uni2851	BRAILLE PATTERN DOTS-157
        chars.append(0x2852)  #uni2852	BRAILLE PATTERN DOTS-257
        chars.append(0x2853)  #uni2853	BRAILLE PATTERN DOTS-1257
        chars.append(0x2854)  #uni2854	BRAILLE PATTERN DOTS-357
        chars.append(0x2855)  #uni2855	BRAILLE PATTERN DOTS-1357
        chars.append(0x2856)  #uni2856	BRAILLE PATTERN DOTS-2357
        chars.append(0x2857)  #uni2857	BRAILLE PATTERN DOTS-12357
        chars.append(0x2858)  #uni2858	BRAILLE PATTERN DOTS-457
        chars.append(0x2859)  #uni2859	BRAILLE PATTERN DOTS-1457
        chars.append(0x285A)  #uni285A	BRAILLE PATTERN DOTS-2457
        chars.append(0x285B)  #uni285B	BRAILLE PATTERN DOTS-12457
        chars.append(0x285C)  #uni285C	BRAILLE PATTERN DOTS-3457
        chars.append(0x285D)  #uni285D	BRAILLE PATTERN DOTS-13457
        chars.append(0x285E)  #uni285E	BRAILLE PATTERN DOTS-23457
        chars.append(0x285F)  #uni285F	BRAILLE PATTERN DOTS-123457
        chars.append(0x2860)  #uni2860	BRAILLE PATTERN DOTS-67
        chars.append(0x2861)  #uni2861	BRAILLE PATTERN DOTS-167
        chars.append(0x2862)  #uni2862	BRAILLE PATTERN DOTS-267
        chars.append(0x2863)  #uni2863	BRAILLE PATTERN DOTS-1267
        chars.append(0x2864)  #uni2864	BRAILLE PATTERN DOTS-367
        chars.append(0x2865)  #uni2865	BRAILLE PATTERN DOTS-1367
        chars.append(0x2866)  #uni2866	BRAILLE PATTERN DOTS-2367
        chars.append(0x2867)  #uni2867	BRAILLE PATTERN DOTS-12367
        chars.append(0x2868)  #uni2868	BRAILLE PATTERN DOTS-467
        chars.append(0x2869)  #uni2869	BRAILLE PATTERN DOTS-1467
        chars.append(0x286A)  #uni286A	BRAILLE PATTERN DOTS-2467
        chars.append(0x286B)  #uni286B	BRAILLE PATTERN DOTS-12467
        chars.append(0x286C)  #uni286C	BRAILLE PATTERN DOTS-3467
        chars.append(0x286D)  #uni286D	BRAILLE PATTERN DOTS-13467
        chars.append(0x286E)  #uni286E	BRAILLE PATTERN DOTS-23467
        chars.append(0x286F)  #uni286F	BRAILLE PATTERN DOTS-123467
        chars.append(0x2870)  #uni2870	BRAILLE PATTERN DOTS-567
        chars.append(0x2871)  #uni2871	BRAILLE PATTERN DOTS-1567
        chars.append(0x2872)  #uni2872	BRAILLE PATTERN DOTS-2567
        chars.append(0x2873)  #uni2873	BRAILLE PATTERN DOTS-12567
        chars.append(0x2874)  #uni2874	BRAILLE PATTERN DOTS-3567
        chars.append(0x2875)  #uni2875	BRAILLE PATTERN DOTS-13567
        chars.append(0x2876)  #uni2876	BRAILLE PATTERN DOTS-23567
        chars.append(0x2877)  #uni2877	BRAILLE PATTERN DOTS-123567
        chars.append(0x2878)  #uni2878	BRAILLE PATTERN DOTS-4567
        chars.append(0x2879)  #uni2879	BRAILLE PATTERN DOTS-14567
        chars.append(0x287A)  #uni287A	BRAILLE PATTERN DOTS-24567
        chars.append(0x287B)  #uni287B	BRAILLE PATTERN DOTS-124567
        chars.append(0x287C)  #uni287C	BRAILLE PATTERN DOTS-34567
        chars.append(0x287D)  #uni287D	BRAILLE PATTERN DOTS-134567
        chars.append(0x287E)  #uni287E	BRAILLE PATTERN DOTS-234567
        chars.append(0x287F)  #uni287F	BRAILLE PATTERN DOTS-1234567
        chars.append(0x2880)  #uni2880	BRAILLE PATTERN DOTS-8
        chars.append(0x2881)  #uni2881	BRAILLE PATTERN DOTS-18
        chars.append(0x2882)  #uni2882	BRAILLE PATTERN DOTS-28
        chars.append(0x2883)  #uni2883	BRAILLE PATTERN DOTS-128
        chars.append(0x2884)  #uni2884	BRAILLE PATTERN DOTS-38
        chars.append(0x2885)  #uni2885	BRAILLE PATTERN DOTS-138
        chars.append(0x2886)  #uni2886	BRAILLE PATTERN DOTS-238
        chars.append(0x2887)  #uni2887	BRAILLE PATTERN DOTS-1238
        chars.append(0x2888)  #uni2888	BRAILLE PATTERN DOTS-48
        chars.append(0x2889)  #uni2889	BRAILLE PATTERN DOTS-148
        chars.append(0x288A)  #uni288A	BRAILLE PATTERN DOTS-248
        chars.append(0x288B)  #uni288B	BRAILLE PATTERN DOTS-1248
        chars.append(0x288C)  #uni288C	BRAILLE PATTERN DOTS-348
        chars.append(0x288D)  #uni288D	BRAILLE PATTERN DOTS-1348
        chars.append(0x288E)  #uni288E	BRAILLE PATTERN DOTS-2348
        chars.append(0x288F)  #uni288F	BRAILLE PATTERN DOTS-12348
        chars.append(0x2890)  #uni2890	BRAILLE PATTERN DOTS-58
        chars.append(0x2891)  #uni2891	BRAILLE PATTERN DOTS-158
        chars.append(0x2892)  #uni2892	BRAILLE PATTERN DOTS-258
        chars.append(0x2893)  #uni2893	BRAILLE PATTERN DOTS-1258
        chars.append(0x2894)  #uni2894	BRAILLE PATTERN DOTS-358
        chars.append(0x2895)  #uni2895	BRAILLE PATTERN DOTS-1358
        chars.append(0x2896)  #uni2896	BRAILLE PATTERN DOTS-2358
        chars.append(0x2897)  #uni2897	BRAILLE PATTERN DOTS-12358
        chars.append(0x2898)  #uni2898	BRAILLE PATTERN DOTS-458
        chars.append(0x2899)  #uni2899	BRAILLE PATTERN DOTS-1458
        chars.append(0x289A)  #uni289A	BRAILLE PATTERN DOTS-2458
        chars.append(0x289B)  #uni289B	BRAILLE PATTERN DOTS-12458
        chars.append(0x289C)  #uni289C	BRAILLE PATTERN DOTS-3458
        chars.append(0x289D)  #uni289D	BRAILLE PATTERN DOTS-13458
        chars.append(0x289E)  #uni289E	BRAILLE PATTERN DOTS-23458
        chars.append(0x289F)  #uni289F	BRAILLE PATTERN DOTS-123458
        chars.append(0x28A0)  #uni28A0	BRAILLE PATTERN DOTS-68
        chars.append(0x28A1)  #uni28A1	BRAILLE PATTERN DOTS-168
        chars.append(0x28A2)  #uni28A2	BRAILLE PATTERN DOTS-268
        chars.append(0x28A3)  #uni28A3	BRAILLE PATTERN DOTS-1268
        chars.append(0x28A4)  #uni28A4	BRAILLE PATTERN DOTS-368
        chars.append(0x28A5)  #uni28A5	BRAILLE PATTERN DOTS-1368
        chars.append(0x28A6)  #uni28A6	BRAILLE PATTERN DOTS-2368
        chars.append(0x28A7)  #uni28A7	BRAILLE PATTERN DOTS-12368
        chars.append(0x28A8)  #uni28A8	BRAILLE PATTERN DOTS-468
        chars.append(0x28A9)  #uni28A9	BRAILLE PATTERN DOTS-1468
        chars.append(0x28AA)  #uni28AA	BRAILLE PATTERN DOTS-2468
        chars.append(0x28AB)  #uni28AB	BRAILLE PATTERN DOTS-12468
        chars.append(0x28AC)  #uni28AC	BRAILLE PATTERN DOTS-3468
        chars.append(0x28AD)  #uni28AD	BRAILLE PATTERN DOTS-13468
        chars.append(0x28AE)  #uni28AE	BRAILLE PATTERN DOTS-23468
        chars.append(0x28AF)  #uni28AF	BRAILLE PATTERN DOTS-123468
        chars.append(0x28B0)  #uni28B0	BRAILLE PATTERN DOTS-568
        chars.append(0x28B1)  #uni28B1	BRAILLE PATTERN DOTS-1568
        chars.append(0x28B2)  #uni28B2	BRAILLE PATTERN DOTS-2568
        chars.append(0x28B3)  #uni28B3	BRAILLE PATTERN DOTS-12568
        chars.append(0x28B4)  #uni28B4	BRAILLE PATTERN DOTS-3568
        chars.append(0x28B5)  #uni28B5	BRAILLE PATTERN DOTS-13568
        chars.append(0x28B6)  #uni28B6	BRAILLE PATTERN DOTS-23568
        chars.append(0x28B7)  #uni28B7	BRAILLE PATTERN DOTS-123568
        chars.append(0x28B8)  #uni28B8	BRAILLE PATTERN DOTS-4568
        chars.append(0x28B9)  #uni28B9	BRAILLE PATTERN DOTS-14568
        chars.append(0x28BA)  #uni28BA	BRAILLE PATTERN DOTS-24568
        chars.append(0x28BB)  #uni28BB	BRAILLE PATTERN DOTS-124568
        chars.append(0x28BC)  #uni28BC	BRAILLE PATTERN DOTS-34568
        chars.append(0x28BD)  #uni28BD	BRAILLE PATTERN DOTS-134568
        chars.append(0x28BE)  #uni28BE	BRAILLE PATTERN DOTS-234568
        chars.append(0x28BF)  #uni28BF	BRAILLE PATTERN DOTS-1234568
        chars.append(0x28C0)  #uni28C0	BRAILLE PATTERN DOTS-78
        chars.append(0x28C1)  #uni28C1	BRAILLE PATTERN DOTS-178
        chars.append(0x28C2)  #uni28C2	BRAILLE PATTERN DOTS-278
        chars.append(0x28C3)  #uni28C3	BRAILLE PATTERN DOTS-1278
        chars.append(0x28C4)  #uni28C4	BRAILLE PATTERN DOTS-378
        chars.append(0x28C5)  #uni28C5	BRAILLE PATTERN DOTS-1378
        chars.append(0x28C6)  #uni28C6	BRAILLE PATTERN DOTS-2378
        chars.append(0x28C7)  #uni28C7	BRAILLE PATTERN DOTS-12378
        chars.append(0x28C8)  #uni28C8	BRAILLE PATTERN DOTS-478
        chars.append(0x28C9)  #uni28C9	BRAILLE PATTERN DOTS-1478
        chars.append(0x28CA)  #uni28CA	BRAILLE PATTERN DOTS-2478
        chars.append(0x28CB)  #uni28CB	BRAILLE PATTERN DOTS-12478
        chars.append(0x28CC)  #uni28CC	BRAILLE PATTERN DOTS-3478
        chars.append(0x28CD)  #uni28CD	BRAILLE PATTERN DOTS-13478
        chars.append(0x28CE)  #uni28CE	BRAILLE PATTERN DOTS-23478
        chars.append(0x28CF)  #uni28CF	BRAILLE PATTERN DOTS-123478
        chars.append(0x28D0)  #uni28D0	BRAILLE PATTERN DOTS-578
        chars.append(0x28D1)  #uni28D1	BRAILLE PATTERN DOTS-1578
        chars.append(0x28D2)  #uni28D2	BRAILLE PATTERN DOTS-2578
        chars.append(0x28D3)  #uni28D3	BRAILLE PATTERN DOTS-12578
        chars.append(0x28D4)  #uni28D4	BRAILLE PATTERN DOTS-3578
        chars.append(0x28D5)  #uni28D5	BRAILLE PATTERN DOTS-13578
        chars.append(0x28D6)  #uni28D6	BRAILLE PATTERN DOTS-23578
        chars.append(0x28D7)  #uni28D7	BRAILLE PATTERN DOTS-123578
        chars.append(0x28D8)  #uni28D8	BRAILLE PATTERN DOTS-4578
        chars.append(0x28D9)  #uni28D9	BRAILLE PATTERN DOTS-14578
        chars.append(0x28DA)  #uni28DA	BRAILLE PATTERN DOTS-24578
        chars.append(0x28DB)  #uni28DB	BRAILLE PATTERN DOTS-124578
        chars.append(0x28DC)  #uni28DC	BRAILLE PATTERN DOTS-34578
        chars.append(0x28DD)  #uni28DD	BRAILLE PATTERN DOTS-134578
        chars.append(0x28DE)  #uni28DE	BRAILLE PATTERN DOTS-234578
        chars.append(0x28DF)  #uni28DF	BRAILLE PATTERN DOTS-1234578
        chars.append(0x28E0)  #uni28E0	BRAILLE PATTERN DOTS-678
        chars.append(0x28E1)  #uni28E1	BRAILLE PATTERN DOTS-1678
        chars.append(0x28E2)  #uni28E2	BRAILLE PATTERN DOTS-2678
        chars.append(0x28E3)  #uni28E3	BRAILLE PATTERN DOTS-12678
        chars.append(0x28E4)  #uni28E4	BRAILLE PATTERN DOTS-3678
        chars.append(0x28E5)  #uni28E5	BRAILLE PATTERN DOTS-13678
        chars.append(0x28E6)  #uni28E6	BRAILLE PATTERN DOTS-23678
        chars.append(0x28E7)  #uni28E7	BRAILLE PATTERN DOTS-123678
        chars.append(0x28E8)  #uni28E8	BRAILLE PATTERN DOTS-4678
        chars.append(0x28E9)  #uni28E9	BRAILLE PATTERN DOTS-14678
        chars.append(0x28EA)  #uni28EA	BRAILLE PATTERN DOTS-24678
        chars.append(0x28EB)  #uni28EB	BRAILLE PATTERN DOTS-124678
        chars.append(0x28EC)  #uni28EC	BRAILLE PATTERN DOTS-34678
        chars.append(0x28ED)  #uni28ED	BRAILLE PATTERN DOTS-134678
        chars.append(0x28EE)  #uni28EE	BRAILLE PATTERN DOTS-234678
        chars.append(0x28EF)  #uni28EF	BRAILLE PATTERN DOTS-1234678
        chars.append(0x28F0)  #uni28F0	BRAILLE PATTERN DOTS-5678
        chars.append(0x28F1)  #uni28F1	BRAILLE PATTERN DOTS-15678
        chars.append(0x28F2)  #uni28F2	BRAILLE PATTERN DOTS-25678
        chars.append(0x28F3)  #uni28F3	BRAILLE PATTERN DOTS-125678
        chars.append(0x28F4)  #uni28F4	BRAILLE PATTERN DOTS-35678
        chars.append(0x28F5)  #uni28F5	BRAILLE PATTERN DOTS-135678
        chars.append(0x28F6)  #uni28F6	BRAILLE PATTERN DOTS-235678
        chars.append(0x28F7)  #uni28F7	BRAILLE PATTERN DOTS-1235678
        chars.append(0x28F8)  #uni28F8	BRAILLE PATTERN DOTS-45678
        chars.append(0x28F9)  #uni28F9	BRAILLE PATTERN DOTS-145678
        chars.append(0x28FA)  #uni28FA	BRAILLE PATTERN DOTS-245678
        chars.append(0x28FB)  #uni28FB	BRAILLE PATTERN DOTS-1245678
        chars.append(0x28FC)  #uni28FC	BRAILLE PATTERN DOTS-345678
        chars.append(0x28FD)  #uni28FD	BRAILLE PATTERN DOTS-1345678
        chars.append(0x28FE)  #uni28FE	BRAILLE PATTERN DOTS-2345678
        chars.append(0x28FF)  #uni28FF	BRAILLE PATTERN DOTS-12345678
        chars.append(0x2900)  #uni2900	RIGHTWARDS TWO-HEADED ARROW WITH VERTICAL STROKE
        chars.append(0x2901)  #uni2901	RIGHTWARDS TWO-HEADED ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x2902)  #uni2902	LEFTWARDS DOUBLE ARROW WITH VERTICAL STROKE
        chars.append(0x2903)  #uni2903	RIGHTWARDS DOUBLE ARROW WITH VERTICAL STROKE
        chars.append(0x2904)  #uni2904	LEFT RIGHT DOUBLE ARROW WITH VERTICAL STROKE
        chars.append(0x2905)  #uni2905	RIGHTWARDS TWO-HEADED ARROW FROM BAR
        chars.append(0x2906)  #uni2906	LEFTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x2907)  #uni2907	RIGHTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x2908)  #uni2908	DOWNWARDS ARROW WITH HORIZONTAL STROKE
        chars.append(0x2909)  #uni2909	UPWARDS ARROW WITH HORIZONTAL STROKE
        chars.append(0x290A)  #uni290A	UPWARDS TRIPLE ARROW
        chars.append(0x290B)  #uni290B	DOWNWARDS TRIPLE ARROW
        chars.append(0x290C)  #uni290C	LEFTWARDS DOUBLE DASH ARROW
        chars.append(0x290D)  #uni290D	RIGHTWARDS DOUBLE DASH ARROW
        chars.append(0x290E)  #uni290E	LEFTWARDS TRIPLE DASH ARROW
        chars.append(0x290F)  #uni290F	RIGHTWARDS TRIPLE DASH ARROW
        chars.append(0x2910)  #uni2910	RIGHTWARDS TWO-HEADED TRIPLE DASH ARROW
        chars.append(0x2911)  #uni2911	RIGHTWARDS ARROW WITH DOTTED STEM
        chars.append(0x2912)  #uni2912	UPWARDS ARROW TO BAR
        chars.append(0x2913)  #uni2913	DOWNWARDS ARROW TO BAR
        chars.append(0x2914)  #uni2914	RIGHTWARDS ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2915)  #uni2915	RIGHTWARDS ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2916)  #uni2916	RIGHTWARDS TWO-HEADED ARROW WITH TAIL
        chars.append(0x2917)  #uni2917	RIGHTWARDS TWO-HEADED ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2918)  #uni2918	RIGHTWARDS TWO-HEADED ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2919)  #uni2919	LEFTWARDS ARROW-TAIL
        chars.append(0x291A)  #uni291A	RIGHTWARDS ARROW-TAIL
        chars.append(0x291B)  #uni291B	LEFTWARDS DOUBLE ARROW-TAIL
        chars.append(0x291C)  #uni291C	RIGHTWARDS DOUBLE ARROW-TAIL
        chars.append(0x291D)  #uni291D	LEFTWARDS ARROW TO BLACK DIAMOND
        chars.append(0x291E)  #uni291E	RIGHTWARDS ARROW TO BLACK DIAMOND
        chars.append(0x291F)  #uni291F	LEFTWARDS ARROW FROM BAR TO BLACK DIAMOND
        chars.append(0x2920)  #uni2920	RIGHTWARDS ARROW FROM BAR TO BLACK DIAMOND
        chars.append(0x2921)  #uni2921	NORTH WEST AND SOUTH EAST ARROW
        chars.append(0x2922)  #uni2922	NORTH EAST AND SOUTH WEST ARROW
        chars.append(0x2923)  #uni2923	NORTH WEST ARROW WITH HOOK
        chars.append(0x2924)  #uni2924	NORTH EAST ARROW WITH HOOK
        chars.append(0x2925)  #uni2925	SOUTH EAST ARROW WITH HOOK
        chars.append(0x2926)  #uni2926	SOUTH WEST ARROW WITH HOOK
        chars.append(0x2927)  #uni2927	NORTH WEST ARROW AND NORTH EAST ARROW
        chars.append(0x2928)  #uni2928	NORTH EAST ARROW AND SOUTH EAST ARROW
        chars.append(0x2929)  #uni2929	SOUTH EAST ARROW AND SOUTH WEST ARROW
        chars.append(0x292A)  #uni292A	SOUTH WEST ARROW AND NORTH WEST ARROW
        chars.append(0x292B)  #uni292B	RISING DIAGONAL CROSSING FALLING DIAGONAL
        chars.append(0x292C)  #uni292C	FALLING DIAGONAL CROSSING RISING DIAGONAL
        chars.append(0x292D)  #uni292D	SOUTH EAST ARROW CROSSING NORTH EAST ARROW
        chars.append(0x292E)  #uni292E	NORTH EAST ARROW CROSSING SOUTH EAST ARROW
        chars.append(0x292F)  #uni292F	FALLING DIAGONAL CROSSING NORTH EAST ARROW
        chars.append(0x2930)  #uni2930	RISING DIAGONAL CROSSING SOUTH EAST ARROW
        chars.append(0x2931)  #uni2931	NORTH EAST ARROW CROSSING NORTH WEST ARROW
        chars.append(0x2932)  #uni2932	NORTH WEST ARROW CROSSING NORTH EAST ARROW
        chars.append(0x2933)  #uni2933	WAVE ARROW POINTING DIRECTLY RIGHT
        chars.append(0x2934)  #uni2934	ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS
        chars.append(0x2935)  #uni2935	ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS
        chars.append(0x2936)  #uni2936	ARROW POINTING DOWNWARDS THEN CURVING LEFTWARDS
        chars.append(0x2937)  #uni2937	ARROW POINTING DOWNWARDS THEN CURVING RIGHTWARDS
        chars.append(0x2938)  #uni2938	RIGHT-SIDE ARC CLOCKWISE ARROW
        chars.append(0x2939)  #uni2939	LEFT-SIDE ARC ANTICLOCKWISE ARROW
        chars.append(0x293A)  #uni293A	TOP ARC ANTICLOCKWISE ARROW
        chars.append(0x293B)  #uni293B	BOTTOM ARC ANTICLOCKWISE ARROW
        chars.append(0x293C)  #uni293C	TOP ARC CLOCKWISE ARROW WITH MINUS
        chars.append(0x293D)  #uni293D	TOP ARC ANTICLOCKWISE ARROW WITH PLUS
        chars.append(0x293E)  #uni293E	LOWER RIGHT SEMICIRCULAR CLOCKWISE ARROW
        chars.append(0x293F)  #uni293F	LOWER LEFT SEMICIRCULAR ANTICLOCKWISE ARROW
        chars.append(0x2940)  #uni2940	ANTICLOCKWISE CLOSED CIRCLE ARROW
        chars.append(0x2941)  #uni2941	CLOCKWISE CLOSED CIRCLE ARROW
        chars.append(0x2942)  #uni2942	RIGHTWARDS ARROW ABOVE SHORT LEFTWARDS ARROW
        chars.append(0x2943)  #uni2943	LEFTWARDS ARROW ABOVE SHORT RIGHTWARDS ARROW
        chars.append(0x2944)  #uni2944	SHORT RIGHTWARDS ARROW ABOVE LEFTWARDS ARROW
        chars.append(0x2945)  #uni2945	RIGHTWARDS ARROW WITH PLUS BELOW
        chars.append(0x2946)  #uni2946	LEFTWARDS ARROW WITH PLUS BELOW
        chars.append(0x2947)  #uni2947	RIGHTWARDS ARROW THROUGH X
        chars.append(0x2948)  #uni2948	LEFT RIGHT ARROW THROUGH SMALL CIRCLE
        chars.append(0x2949)  #uni2949	UPWARDS TWO-HEADED ARROW FROM SMALL CIRCLE
        chars.append(0x294A)  #uni294A	LEFT BARB UP RIGHT BARB DOWN HARPOON
        chars.append(0x294B)  #uni294B	LEFT BARB DOWN RIGHT BARB UP HARPOON
        chars.append(0x294C)  #uni294C	UP BARB RIGHT DOWN BARB LEFT HARPOON
        chars.append(0x294D)  #uni294D	UP BARB LEFT DOWN BARB RIGHT HARPOON
        chars.append(0x294E)  #uni294E	LEFT BARB UP RIGHT BARB UP HARPOON
        chars.append(0x294F)  #uni294F	UP BARB RIGHT DOWN BARB RIGHT HARPOON
        chars.append(0x2950)  #uni2950	LEFT BARB DOWN RIGHT BARB DOWN HARPOON
        chars.append(0x2951)  #uni2951	UP BARB LEFT DOWN BARB LEFT HARPOON
        chars.append(0x2952)  #uni2952	LEFTWARDS HARPOON WITH BARB UP TO BAR
        chars.append(0x2953)  #uni2953	RIGHTWARDS HARPOON WITH BARB UP TO BAR
        chars.append(0x2954)  #uni2954	UPWARDS HARPOON WITH BARB RIGHT TO BAR
        chars.append(0x2955)  #uni2955	DOWNWARDS HARPOON WITH BARB RIGHT TO BAR
        chars.append(0x2956)  #uni2956	LEFTWARDS HARPOON WITH BARB DOWN TO BAR
        chars.append(0x2957)  #uni2957	RIGHTWARDS HARPOON WITH BARB DOWN TO BAR
        chars.append(0x2958)  #uni2958	UPWARDS HARPOON WITH BARB LEFT TO BAR
        chars.append(0x2959)  #uni2959	DOWNWARDS HARPOON WITH BARB LEFT TO BAR
        chars.append(0x295A)  #uni295A	LEFTWARDS HARPOON WITH BARB UP FROM BAR
        chars.append(0x295B)  #uni295B	RIGHTWARDS HARPOON WITH BARB UP FROM BAR
        chars.append(0x295C)  #uni295C	UPWARDS HARPOON WITH BARB RIGHT FROM BAR
        chars.append(0x295D)  #uni295D	DOWNWARDS HARPOON WITH BARB RIGHT FROM BAR
        chars.append(0x295E)  #uni295E	LEFTWARDS HARPOON WITH BARB DOWN FROM BAR
        chars.append(0x295F)  #uni295F	RIGHTWARDS HARPOON WITH BARB DOWN FROM BAR
        chars.append(0x2960)  #uni2960	UPWARDS HARPOON WITH BARB LEFT FROM BAR
        chars.append(0x2961)  #uni2961	DOWNWARDS HARPOON WITH BARB LEFT FROM BAR
        chars.append(0x2962)  #uni2962	LEFTWARDS HARPOON WITH BARB UP ABOVE LEFTWARDS HARPOON WITH BARB DOWN
        chars.append(0x2963)  #uni2963	UPWARDS HARPOON WITH BARB LEFT BESIDE UPWARDS HARPOON WITH BARB RIGHT
        chars.append(0x2964)  #uni2964	RIGHTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB DOWN
        chars.append(0x2965)  #uni2965	DOWNWARDS HARPOON WITH BARB LEFT BESIDE DOWNWARDS HARPOON WITH BARB RIGHT
        chars.append(0x2966)  #uni2966	LEFTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB UP
        chars.append(0x2967)  #uni2967	LEFTWARDS HARPOON WITH BARB DOWN ABOVE RIGHTWARDS HARPOON WITH BARB DOWN
        chars.append(0x2968)  #uni2968	RIGHTWARDS HARPOON WITH BARB UP ABOVE LEFTWARDS HARPOON WITH BARB UP
        chars.append(0x2969)  #uni2969	RIGHTWARDS HARPOON WITH BARB DOWN ABOVE LEFTWARDS HARPOON WITH BARB DOWN
        chars.append(0x296A)  #uni296A	LEFTWARDS HARPOON WITH BARB UP ABOVE LONG DASH
        chars.append(0x296B)  #uni296B	LEFTWARDS HARPOON WITH BARB DOWN BELOW LONG DASH
        chars.append(0x296C)  #uni296C	RIGHTWARDS HARPOON WITH BARB UP ABOVE LONG DASH
        chars.append(0x296D)  #uni296D	RIGHTWARDS HARPOON WITH BARB DOWN BELOW LONG DASH
        chars.append(0x296E)  #uni296E	UPWARDS HARPOON WITH BARB LEFT BESIDE DOWNWARDS HARPOON WITH BARB RIGHT
        chars.append(0x296F)  #uni296F	DOWNWARDS HARPOON WITH BARB LEFT BESIDE UPWARDS HARPOON WITH BARB RIGHT
        chars.append(0x2970)  #uni2970	RIGHT DOUBLE ARROW WITH ROUNDED HEAD
        chars.append(0x2971)  #uni2971	EQUALS SIGN ABOVE RIGHTWARDS ARROW
        chars.append(0x2972)  #uni2972	TILDE OPERATOR ABOVE RIGHTWARDS ARROW
        chars.append(0x2973)  #uni2973	LEFTWARDS ARROW ABOVE TILDE OPERATOR
        chars.append(0x2974)  #uni2974	RIGHTWARDS ARROW ABOVE TILDE OPERATOR
        chars.append(0x2975)  #uni2975	RIGHTWARDS ARROW ABOVE ALMOST EQUAL TO
        chars.append(0x2976)  #uni2976	LESS-THAN ABOVE LEFTWARDS ARROW
        chars.append(0x2977)  #uni2977	LEFTWARDS ARROW THROUGH LESS-THAN
        chars.append(0x2978)  #uni2978	GREATER-THAN ABOVE RIGHTWARDS ARROW
        chars.append(0x2979)  #uni2979	SUBSET ABOVE RIGHTWARDS ARROW
        chars.append(0x297A)  #uni297A	LEFTWARDS ARROW THROUGH SUBSET
        chars.append(0x297B)  #uni297B	SUPERSET ABOVE LEFTWARDS ARROW
        chars.append(0x297C)  #uni297C	LEFT FISH TAIL
        chars.append(0x297D)  #uni297D	RIGHT FISH TAIL
        chars.append(0x297E)  #uni297E	UP FISH TAIL
        chars.append(0x297F)  #uni297F	DOWN FISH TAIL
        chars.append(0x2980)  #uni2980	TRIPLE VERTICAL BAR DELIMITER
        chars.append(0x2981)  #uni2981	Z NOTATION SPOT
        chars.append(0x2982)  #uni2982	Z NOTATION TYPE COLON
        chars.append(0x2983)  #uni2983	LEFT WHITE CURLY BRACKET
        chars.append(0x2984)  #uni2984	RIGHT WHITE CURLY BRACKET
        chars.append(0x2985)  #uni2985	LEFT WHITE PARENTHESIS
        chars.append(0x2986)  #uni2986	RIGHT WHITE PARENTHESIS
        chars.append(0x2987)  #uni2987	Z NOTATION LEFT IMAGE BRACKET
        chars.append(0x2988)  #uni2988	Z NOTATION RIGHT IMAGE BRACKET
        chars.append(0x2989)  #uni2989	Z NOTATION LEFT BINDING BRACKET
        chars.append(0x298A)  #uni298A	Z NOTATION RIGHT BINDING BRACKET
        chars.append(0x298B)  #uni298B	LEFT SQUARE BRACKET WITH UNDERBAR
        chars.append(0x298C)  #uni298C	RIGHT SQUARE BRACKET WITH UNDERBAR
        chars.append(0x298D)  #uni298D	LEFT SQUARE BRACKET WITH TICK IN TOP CORNER
        chars.append(0x298E)  #uni298E	RIGHT SQUARE BRACKET WITH TICK IN BOTTOM CORNER
        chars.append(0x298F)  #uni298F	LEFT SQUARE BRACKET WITH TICK IN BOTTOM CORNER
        chars.append(0x2990)  #uni2990	RIGHT SQUARE BRACKET WITH TICK IN TOP CORNER
        chars.append(0x2991)  #uni2991	LEFT ANGLE BRACKET WITH DOT
        chars.append(0x2992)  #uni2992	RIGHT ANGLE BRACKET WITH DOT
        chars.append(0x2993)  #uni2993	LEFT ARC LESS-THAN BRACKET
        chars.append(0x2994)  #uni2994	RIGHT ARC GREATER-THAN BRACKET
        chars.append(0x2995)  #uni2995	DOUBLE LEFT ARC GREATER-THAN BRACKET
        chars.append(0x2996)  #uni2996	DOUBLE RIGHT ARC LESS-THAN BRACKET
        chars.append(0x2997)  #uni2997	LEFT BLACK TORTOISE SHELL BRACKET
        chars.append(0x2998)  #uni2998	RIGHT BLACK TORTOISE SHELL BRACKET
        chars.append(0x2999)  #uni2999	DOTTED FENCE
        chars.append(0x299A)  #uni299A	VERTICAL ZIGZAG LINE
        chars.append(0x299B)  #uni299B	MEASURED ANGLE OPENING LEFT
        chars.append(0x299C)  #uni299C	RIGHT ANGLE VARIANT WITH SQUARE
        chars.append(0x299D)  #uni299D	MEASURED RIGHT ANGLE WITH DOT
        chars.append(0x299E)  #uni299E	ANGLE WITH S INSIDE
        chars.append(0x299F)  #uni299F	ACUTE ANGLE
        chars.append(0x29A0)  #uni29A0	SPHERICAL ANGLE OPENING LEFT
        chars.append(0x29A1)  #uni29A1	SPHERICAL ANGLE OPENING UP
        chars.append(0x29A2)  #uni29A2	TURNED ANGLE
        chars.append(0x29A3)  #uni29A3	REVERSED ANGLE
        chars.append(0x29A4)  #uni29A4	ANGLE WITH UNDERBAR
        chars.append(0x29A5)  #uni29A5	REVERSED ANGLE WITH UNDERBAR
        chars.append(0x29A6)  #uni29A6	OBLIQUE ANGLE OPENING UP
        chars.append(0x29A7)  #uni29A7	OBLIQUE ANGLE OPENING DOWN
        chars.append(0x29A8)  #uni29A8	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING UP AND RIGHT
        chars.append(0x29A9)  #uni29A9	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING UP AND LEFT
        chars.append(0x29AA)  #uni29AA	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING DOWN AND RIGHT
        chars.append(0x29AB)  #uni29AB	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING DOWN AND LEFT
        chars.append(0x29AC)  #uni29AC	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING RIGHT AND UP
        chars.append(0x29AD)  #uni29AD	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING LEFT AND UP
        chars.append(0x29AE)  #uni29AE	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING RIGHT AND DOWN
        chars.append(0x29AF)  #uni29AF	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING LEFT AND DOWN
        chars.append(0x29B0)  #uni29B0	REVERSED EMPTY SET
        chars.append(0x29B1)  #uni29B1	EMPTY SET WITH OVERBAR
        chars.append(0x29B2)  #uni29B2	EMPTY SET WITH SMALL CIRCLE ABOVE
        chars.append(0x29B3)  #uni29B3	EMPTY SET WITH RIGHT ARROW ABOVE
        chars.append(0x29B4)  #uni29B4	EMPTY SET WITH LEFT ARROW ABOVE
        chars.append(0x29B5)  #uni29B5	CIRCLE WITH HORIZONTAL BAR
        chars.append(0x29B6)  #uni29B6	CIRCLED VERTICAL BAR
        chars.append(0x29B7)  #uni29B7	CIRCLED PARALLEL
        chars.append(0x29B8)  #uni29B8	CIRCLED REVERSE SOLIDUS
        chars.append(0x29B9)  #uni29B9	CIRCLED PERPENDICULAR
        chars.append(0x29BA)  #uni29BA	CIRCLE DIVIDED BY HORIZONTAL BAR AND TOP HALF DIVIDED BY VERTICAL BAR
        chars.append(0x29BB)  #uni29BB	CIRCLE WITH SUPERIMPOSED X
        chars.append(0x29BC)  #uni29BC	CIRCLED ANTICLOCKWISE-ROTATED DIVISION SIGN
        chars.append(0x29BD)  #uni29BD	UP ARROW THROUGH CIRCLE
        chars.append(0x29BE)  #uni29BE	CIRCLED WHITE BULLET
        chars.append(0x29BF)  #uni29BF	CIRCLED BULLET
        chars.append(0x29C0)  #uni29C0	CIRCLED LESS-THAN
        chars.append(0x29C1)  #uni29C1	CIRCLED GREATER-THAN
        chars.append(0x29C2)  #uni29C2	CIRCLE WITH SMALL CIRCLE TO THE RIGHT
        chars.append(0x29C3)  #uni29C3	CIRCLE WITH TWO HORIZONTAL STROKES TO THE RIGHT
        chars.append(0x29C4)  #uni29C4	SQUARED RISING DIAGONAL SLASH
        chars.append(0x29C5)  #uni29C5	SQUARED FALLING DIAGONAL SLASH
        chars.append(0x29C6)  #uni29C6	SQUARED ASTERISK
        chars.append(0x29C7)  #uni29C7	SQUARED SMALL CIRCLE
        chars.append(0x29C8)  #uni29C8	SQUARED SQUARE
        chars.append(0x29C9)  #uni29C9	TWO JOINED SQUARES
        chars.append(0x29CA)  #uni29CA	TRIANGLE WITH DOT ABOVE
        chars.append(0x29CB)  #uni29CB	TRIANGLE WITH UNDERBAR
        chars.append(0x29CC)  #uni29CC	S IN TRIANGLE
        chars.append(0x29CD)  #uni29CD	TRIANGLE WITH SERIFS AT BOTTOM
        chars.append(0x29CE)  #uni29CE	RIGHT TRIANGLE ABOVE LEFT TRIANGLE
        chars.append(0x29CF)  #uni29CF	LEFT TRIANGLE BESIDE VERTICAL BAR
        chars.append(0x29D0)  #uni29D0	VERTICAL BAR BESIDE RIGHT TRIANGLE
        chars.append(0x29D1)  #uni29D1	BOWTIE WITH LEFT HALF BLACK
        chars.append(0x29D2)  #uni29D2	BOWTIE WITH RIGHT HALF BLACK
        chars.append(0x29D3)  #uni29D3	BLACK BOWTIE
        chars.append(0x29D4)  #uni29D4	TIMES WITH LEFT HALF BLACK
        chars.append(0x29D5)  #uni29D5	TIMES WITH RIGHT HALF BLACK
        chars.append(0x29D6)  #uni29D6	WHITE HOURGLASS
        chars.append(0x29D7)  #uni29D7	BLACK HOURGLASS
        chars.append(0x29D8)  #uni29D8	LEFT WIGGLY FENCE
        chars.append(0x29D9)  #uni29D9	RIGHT WIGGLY FENCE
        chars.append(0x29DA)  #uni29DA	LEFT DOUBLE WIGGLY FENCE
        chars.append(0x29DB)  #uni29DB	RIGHT DOUBLE WIGGLY FENCE
        chars.append(0x29DC)  #uni29DC	INCOMPLETE INFINITY
        chars.append(0x29DD)  #uni29DD	TIE OVER INFINITY
        chars.append(0x29DE)  #uni29DE	INFINITY NEGATED WITH VERTICAL BAR
        chars.append(0x29DF)  #uni29DF	DOUBLE-ENDED MULTIMAP
        chars.append(0x29E0)  #uni29E0	SQUARE WITH CONTOURED OUTLINE
        chars.append(0x29E1)  #uni29E1	INCREASES AS
        chars.append(0x29E2)  #uni29E2	SHUFFLE PRODUCT
        chars.append(0x29E3)  #uni29E3	EQUALS SIGN AND SLANTED PARALLEL
        chars.append(0x29E4)  #uni29E4	EQUALS SIGN AND SLANTED PARALLEL WITH TILDE ABOVE
        chars.append(0x29E5)  #uni29E5	IDENTICAL TO AND SLANTED PARALLEL
        chars.append(0x29E6)  #uni29E6	GLEICH STARK
        chars.append(0x29E7)  #uni29E7	THERMODYNAMIC
        chars.append(0x29E8)  #uni29E8	DOWN-POINTING TRIANGLE WITH LEFT HALF BLACK
        chars.append(0x29E9)  #uni29E9	DOWN-POINTING TRIANGLE WITH RIGHT HALF BLACK
        chars.append(0x29EA)  #uni29EA	BLACK DIAMOND WITH DOWN ARROW
        chars.append(0x29EB)  #uni29EB	BLACK LOZENGE
        chars.append(0x29EC)  #uni29EC	WHITE CIRCLE WITH DOWN ARROW
        chars.append(0x29ED)  #uni29ED	BLACK CIRCLE WITH DOWN ARROW
        chars.append(0x29EE)  #uni29EE	ERROR-BARRED WHITE SQUARE
        chars.append(0x29EF)  #uni29EF	ERROR-BARRED BLACK SQUARE
        chars.append(0x29F0)  #uni29F0	ERROR-BARRED WHITE DIAMOND
        chars.append(0x29F1)  #uni29F1	ERROR-BARRED BLACK DIAMOND
        chars.append(0x29F2)  #uni29F2	ERROR-BARRED WHITE CIRCLE
        chars.append(0x29F3)  #uni29F3	ERROR-BARRED BLACK CIRCLE
        chars.append(0x29F4)  #uni29F4	RULE-DELAYED
        chars.append(0x29F5)  #uni29F5	REVERSE SOLIDUS OPERATOR
        chars.append(0x29F6)  #uni29F6	SOLIDUS WITH OVERBAR
        chars.append(0x29F7)  #uni29F7	REVERSE SOLIDUS WITH HORIZONTAL STROKE
        chars.append(0x29F8)  #uni29F8	BIG SOLIDUS
        chars.append(0x29F9)  #uni29F9	BIG REVERSE SOLIDUS
        chars.append(0x29FA)  #uni29FA	DOUBLE PLUS
        chars.append(0x29FB)  #uni29FB	TRIPLE PLUS
        chars.append(0x29FC)  #uni29FC	LEFT-POINTING CURVED ANGLE BRACKET
        chars.append(0x29FD)  #uni29FD	RIGHT-POINTING CURVED ANGLE BRACKET
        chars.append(0x29FE)  #uni29FE	TINY
        chars.append(0x29FF)  #uni29FF	MINY
        chars.append(0x2A00)  #uni2A00	N-ARY CIRCLED DOT OPERATOR
        chars.append(0x2A01)  #uni2A01	N-ARY CIRCLED PLUS OPERATOR
        chars.append(0x2A02)  #uni2A02	N-ARY CIRCLED TIMES OPERATOR
        chars.append(0x2A03)  #uni2A03	N-ARY UNION OPERATOR WITH DOT
        chars.append(0x2A04)  #uni2A04	N-ARY UNION OPERATOR WITH PLUS
        chars.append(0x2A05)  #uni2A05	N-ARY SQUARE INTERSECTION OPERATOR
        chars.append(0x2A06)  #uni2A06	N-ARY SQUARE UNION OPERATOR
        chars.append(0x2A07)  #uni2A07	TWO LOGICAL AND OPERATOR
        chars.append(0x2A08)  #uni2A08	TWO LOGICAL OR OPERATOR
        chars.append(0x2A09)  #uni2A09	N-ARY TIMES OPERATOR
        chars.append(0x2A0A)  #uni2A0A	MODULO TWO SUM
        chars.append(0x2A0B)  #uni2A0B	SUMMATION WITH INTEGRAL
        chars.append(0x2A0C)  #uni2A0C	QUADRUPLE INTEGRAL OPERATOR
        chars.append(0x2A0D)  #uni2A0D	FINITE PART INTEGRAL
        chars.append(0x2A0E)  #uni2A0E	INTEGRAL WITH DOUBLE STROKE
        chars.append(0x2A0F)  #uni2A0F	INTEGRAL AVERAGE WITH SLASH
        chars.append(0x2A10)  #uni2A10	CIRCULATION FUNCTION
        chars.append(0x2A11)  #uni2A11	ANTICLOCKWISE INTEGRATION
        chars.append(0x2A12)  #uni2A12	LINE INTEGRATION WITH RECTANGULAR PATH AROUND POLE
        chars.append(0x2A13)  #uni2A13	LINE INTEGRATION WITH SEMICIRCULAR PATH AROUND POLE
        chars.append(0x2A14)  #uni2A14	LINE INTEGRATION NOT INCLUDING THE POLE
        chars.append(0x2A15)  #uni2A15	INTEGRAL AROUND A POINT OPERATOR
        chars.append(0x2A16)  #uni2A16	QUATERNION INTEGRAL OPERATOR
        chars.append(0x2A17)  #uni2A17	INTEGRAL WITH LEFTWARDS ARROW WITH HOOK
        chars.append(0x2A18)  #uni2A18	INTEGRAL WITH TIMES SIGN
        chars.append(0x2A19)  #uni2A19	INTEGRAL WITH INTERSECTION
        chars.append(0x2A1A)  #uni2A1A	INTEGRAL WITH UNION
        chars.append(0x2A1B)  #uni2A1B	INTEGRAL WITH OVERBAR
        chars.append(0x2A1C)  #uni2A1C	INTEGRAL WITH UNDERBAR
        chars.append(0x2A1D)  #uni2A1D	JOIN
        chars.append(0x2A1E)  #uni2A1E	LARGE LEFT TRIANGLE OPERATOR
        chars.append(0x2A1F)  #uni2A1F	Z NOTATION SCHEMA COMPOSITION
        chars.append(0x2A20)  #uni2A20	Z NOTATION SCHEMA PIPING
        chars.append(0x2A21)  #uni2A21	Z NOTATION SCHEMA PROJECTION
        chars.append(0x2A22)  #uni2A22	PLUS SIGN WITH SMALL CIRCLE ABOVE
        chars.append(0x2A23)  #uni2A23	PLUS SIGN WITH CIRCUMFLEX ACCENT ABOVE
        chars.append(0x2A24)  #uni2A24	PLUS SIGN WITH TILDE ABOVE
        chars.append(0x2A25)  #uni2A25	PLUS SIGN WITH DOT BELOW
        chars.append(0x2A26)  #uni2A26	PLUS SIGN WITH TILDE BELOW
        chars.append(0x2A27)  #uni2A27	PLUS SIGN WITH SUBSCRIPT TWO
        chars.append(0x2A28)  #uni2A28	PLUS SIGN WITH BLACK TRIANGLE
        chars.append(0x2A29)  #uni2A29	MINUS SIGN WITH COMMA ABOVE
        chars.append(0x2A2A)  #uni2A2A	MINUS SIGN WITH DOT BELOW
        chars.append(0x2A2B)  #uni2A2B	MINUS SIGN WITH FALLING DOTS
        chars.append(0x2A2C)  #uni2A2C	MINUS SIGN WITH RISING DOTS
        chars.append(0x2A2D)  #uni2A2D	PLUS SIGN IN LEFT HALF CIRCLE
        chars.append(0x2A2E)  #uni2A2E	PLUS SIGN IN RIGHT HALF CIRCLE
        chars.append(0x2A2F)  #uni2A2F	VECTOR OR CROSS PRODUCT
        chars.append(0x2A30)  #uni2A30	MULTIPLICATION SIGN WITH DOT ABOVE
        chars.append(0x2A31)  #uni2A31	MULTIPLICATION SIGN WITH UNDERBAR
        chars.append(0x2A32)  #uni2A32	SEMIDIRECT PRODUCT WITH BOTTOM CLOSED
        chars.append(0x2A33)  #uni2A33	SMASH PRODUCT
        chars.append(0x2A34)  #uni2A34	MULTIPLICATION SIGN IN LEFT HALF CIRCLE
        chars.append(0x2A35)  #uni2A35	MULTIPLICATION SIGN IN RIGHT HALF CIRCLE
        chars.append(0x2A36)  #uni2A36	CIRCLED MULTIPLICATION SIGN WITH CIRCUMFLEX ACCENT
        chars.append(0x2A37)  #uni2A37	MULTIPLICATION SIGN IN DOUBLE CIRCLE
        chars.append(0x2A38)  #uni2A38	CIRCLED DIVISION SIGN
        chars.append(0x2A39)  #uni2A39	PLUS SIGN IN TRIANGLE
        chars.append(0x2A3A)  #uni2A3A	MINUS SIGN IN TRIANGLE
        chars.append(0x2A3B)  #uni2A3B	MULTIPLICATION SIGN IN TRIANGLE
        chars.append(0x2A3C)  #uni2A3C	INTERIOR PRODUCT
        chars.append(0x2A3D)  #uni2A3D	RIGHTHAND INTERIOR PRODUCT
        chars.append(0x2A3E)  #uni2A3E	Z NOTATION RELATIONAL COMPOSITION
        chars.append(0x2A3F)  #uni2A3F	AMALGAMATION OR COPRODUCT
        chars.append(0x2A40)  #uni2A40	INTERSECTION WITH DOT
        chars.append(0x2A41)  #uni2A41	UNION WITH MINUS SIGN
        chars.append(0x2A42)  #uni2A42	UNION WITH OVERBAR
        chars.append(0x2A43)  #uni2A43	INTERSECTION WITH OVERBAR
        chars.append(0x2A44)  #uni2A44	INTERSECTION WITH LOGICAL AND
        chars.append(0x2A45)  #uni2A45	UNION WITH LOGICAL OR
        chars.append(0x2A46)  #uni2A46	UNION ABOVE INTERSECTION
        chars.append(0x2A47)  #uni2A47	INTERSECTION ABOVE UNION
        chars.append(0x2A48)  #uni2A48	UNION ABOVE BAR ABOVE INTERSECTION
        chars.append(0x2A49)  #uni2A49	INTERSECTION ABOVE BAR ABOVE UNION
        chars.append(0x2A4A)  #uni2A4A	UNION BESIDE AND JOINED WITH UNION
        chars.append(0x2A4B)  #uni2A4B	INTERSECTION BESIDE AND JOINED WITH INTERSECTION
        chars.append(0x2A4C)  #uni2A4C	CLOSED UNION WITH SERIFS
        chars.append(0x2A4D)  #uni2A4D	CLOSED INTERSECTION WITH SERIFS
        chars.append(0x2A4E)  #uni2A4E	DOUBLE SQUARE INTERSECTION
        chars.append(0x2A4F)  #uni2A4F	DOUBLE SQUARE UNION
        chars.append(0x2A50)  #uni2A50	CLOSED UNION WITH SERIFS AND SMASH PRODUCT
        chars.append(0x2A51)  #uni2A51	LOGICAL AND WITH DOT ABOVE
        chars.append(0x2A52)  #uni2A52	LOGICAL OR WITH DOT ABOVE
        chars.append(0x2A53)  #uni2A53	DOUBLE LOGICAL AND
        chars.append(0x2A54)  #uni2A54	DOUBLE LOGICAL OR
        chars.append(0x2A55)  #uni2A55	TWO INTERSECTING LOGICAL AND
        chars.append(0x2A56)  #uni2A56	TWO INTERSECTING LOGICAL OR
        chars.append(0x2A57)  #uni2A57	SLOPING LARGE OR
        chars.append(0x2A58)  #uni2A58	SLOPING LARGE AND
        chars.append(0x2A59)  #uni2A59	LOGICAL OR OVERLAPPING LOGICAL AND
        chars.append(0x2A5A)  #uni2A5A	LOGICAL AND WITH MIDDLE STEM
        chars.append(0x2A5B)  #uni2A5B	LOGICAL OR WITH MIDDLE STEM
        chars.append(0x2A5C)  #uni2A5C	LOGICAL AND WITH HORIZONTAL DASH
        chars.append(0x2A5D)  #uni2A5D	LOGICAL OR WITH HORIZONTAL DASH
        chars.append(0x2A5E)  #uni2A5E	LOGICAL AND WITH DOUBLE OVERBAR
        chars.append(0x2A5F)  #uni2A5F	LOGICAL AND WITH UNDERBAR
        chars.append(0x2A60)  #uni2A60	LOGICAL AND WITH DOUBLE UNDERBAR
        chars.append(0x2A61)  #uni2A61	SMALL VEE WITH UNDERBAR
        chars.append(0x2A62)  #uni2A62	LOGICAL OR WITH DOUBLE OVERBAR
        chars.append(0x2A63)  #uni2A63	LOGICAL OR WITH DOUBLE UNDERBAR
        chars.append(0x2A64)  #uni2A64	Z NOTATION DOMAIN ANTIRESTRICTION
        chars.append(0x2A65)  #uni2A65	Z NOTATION RANGE ANTIRESTRICTION
        chars.append(0x2A66)  #uni2A66	EQUALS SIGN WITH DOT BELOW
        chars.append(0x2A67)  #uni2A67	IDENTICAL WITH DOT ABOVE
        chars.append(0x2A68)  #uni2A68	TRIPLE HORIZONTAL BAR WITH DOUBLE VERTICAL STROKE
        chars.append(0x2A69)  #uni2A69	TRIPLE HORIZONTAL BAR WITH TRIPLE VERTICAL STROKE
        chars.append(0x2A6A)  #uni2A6A	TILDE OPERATOR WITH DOT ABOVE
        chars.append(0x2A6B)  #uni2A6B	TILDE OPERATOR WITH RISING DOTS
        chars.append(0x2A6C)  #uni2A6C	SIMILAR MINUS SIMILAR
        chars.append(0x2A6D)  #uni2A6D	CONGRUENT WITH DOT ABOVE
        chars.append(0x2A6E)  #uni2A6E	EQUALS WITH ASTERISK
        chars.append(0x2A6F)  #uni2A6F	ALMOST EQUAL TO WITH CIRCUMFLEX ACCENT
        chars.append(0x2A70)  #uni2A70	APPROXIMATELY EQUAL OR EQUAL TO
        chars.append(0x2A71)  #uni2A71	EQUALS SIGN ABOVE PLUS SIGN
        chars.append(0x2A72)  #uni2A72	PLUS SIGN ABOVE EQUALS SIGN
        chars.append(0x2A73)  #uni2A73	EQUALS SIGN ABOVE TILDE OPERATOR
        chars.append(0x2A74)  #uni2A74	DOUBLE COLON EQUAL
        chars.append(0x2A75)  #uni2A75	TWO CONSECUTIVE EQUALS SIGNS
        chars.append(0x2A76)  #uni2A76	THREE CONSECUTIVE EQUALS SIGNS
        chars.append(0x2A77)  #uni2A77	EQUALS SIGN WITH TWO DOTS ABOVE AND TWO DOTS BELOW
        chars.append(0x2A78)  #uni2A78	EQUIVALENT WITH FOUR DOTS ABOVE
        chars.append(0x2A79)  #uni2A79	LESS-THAN WITH CIRCLE INSIDE
        chars.append(0x2A7A)  #uni2A7A	GREATER-THAN WITH CIRCLE INSIDE
        chars.append(0x2A7B)  #uni2A7B	LESS-THAN WITH QUESTION MARK ABOVE
        chars.append(0x2A7C)  #uni2A7C	GREATER-THAN WITH QUESTION MARK ABOVE
        chars.append(0x2A7D)  #uni2A7D	LESS-THAN OR SLANTED EQUAL TO
        chars.append(0x2A7E)  #uni2A7E	GREATER-THAN OR SLANTED EQUAL TO
        chars.append(0x2A7F)  #uni2A7F	LESS-THAN OR SLANTED EQUAL TO WITH DOT INSIDE
        chars.append(0x2A80)  #uni2A80	GREATER-THAN OR SLANTED EQUAL TO WITH DOT INSIDE
        chars.append(0x2A81)  #uni2A81	LESS-THAN OR SLANTED EQUAL TO WITH DOT ABOVE
        chars.append(0x2A82)  #uni2A82	GREATER-THAN OR SLANTED EQUAL TO WITH DOT ABOVE
        chars.append(0x2A83)  #uni2A83	LESS-THAN OR SLANTED EQUAL TO WITH DOT ABOVE RIGHT
        chars.append(0x2A84)  #uni2A84	GREATER-THAN OR SLANTED EQUAL TO WITH DOT ABOVE LEFT
        chars.append(0x2A85)  #uni2A85	LESS-THAN OR APPROXIMATE
        chars.append(0x2A86)  #uni2A86	GREATER-THAN OR APPROXIMATE
        chars.append(0x2A87)  #uni2A87	LESS-THAN AND SINGLE-LINE NOT EQUAL TO
        chars.append(0x2A88)  #uni2A88	GREATER-THAN AND SINGLE-LINE NOT EQUAL TO
        chars.append(0x2A89)  #uni2A89	LESS-THAN AND NOT APPROXIMATE
        chars.append(0x2A8A)  #uni2A8A	GREATER-THAN AND NOT APPROXIMATE
        chars.append(0x2A8B)  #uni2A8B	LESS-THAN ABOVE DOUBLE-LINE EQUAL ABOVE GREATER-THAN
        chars.append(0x2A8C)  #uni2A8C	GREATER-THAN ABOVE DOUBLE-LINE EQUAL ABOVE LESS-THAN
        chars.append(0x2A8D)  #uni2A8D	LESS-THAN ABOVE SIMILAR OR EQUAL
        chars.append(0x2A8E)  #uni2A8E	GREATER-THAN ABOVE SIMILAR OR EQUAL
        chars.append(0x2A8F)  #uni2A8F	LESS-THAN ABOVE SIMILAR ABOVE GREATER-THAN
        chars.append(0x2A90)  #uni2A90	GREATER-THAN ABOVE SIMILAR ABOVE LESS-THAN
        chars.append(0x2A91)  #uni2A91	LESS-THAN ABOVE GREATER-THAN ABOVE DOUBLE-LINE EQUAL
        chars.append(0x2A92)  #uni2A92	GREATER-THAN ABOVE LESS-THAN ABOVE DOUBLE-LINE EQUAL
        chars.append(0x2A93)  #uni2A93	LESS-THAN ABOVE SLANTED EQUAL ABOVE GREATER-THAN ABOVE SLANTED EQUAL
        chars.append(0x2A94)  #uni2A94	GREATER-THAN ABOVE SLANTED EQUAL ABOVE LESS-THAN ABOVE SLANTED EQUAL
        chars.append(0x2A95)  #uni2A95	SLANTED EQUAL TO OR LESS-THAN
        chars.append(0x2A96)  #uni2A96	SLANTED EQUAL TO OR GREATER-THAN
        chars.append(0x2A97)  #uni2A97	SLANTED EQUAL TO OR LESS-THAN WITH DOT INSIDE
        chars.append(0x2A98)  #uni2A98	SLANTED EQUAL TO OR GREATER-THAN WITH DOT INSIDE
        chars.append(0x2A99)  #uni2A99	DOUBLE-LINE EQUAL TO OR LESS-THAN
        chars.append(0x2A9A)  #uni2A9A	DOUBLE-LINE EQUAL TO OR GREATER-THAN
        chars.append(0x2A9B)  #uni2A9B	DOUBLE-LINE SLANTED EQUAL TO OR LESS-THAN
        chars.append(0x2A9C)  #uni2A9C	DOUBLE-LINE SLANTED EQUAL TO OR GREATER-THAN
        chars.append(0x2A9D)  #uni2A9D	SIMILAR OR LESS-THAN
        chars.append(0x2A9E)  #uni2A9E	SIMILAR OR GREATER-THAN
        chars.append(0x2A9F)  #uni2A9F	SIMILAR ABOVE LESS-THAN ABOVE EQUALS SIGN
        chars.append(0x2AA0)  #uni2AA0	SIMILAR ABOVE GREATER-THAN ABOVE EQUALS SIGN
        chars.append(0x2AA1)  #uni2AA1	DOUBLE NESTED LESS-THAN
        chars.append(0x2AA2)  #uni2AA2	DOUBLE NESTED GREATER-THAN
        chars.append(0x2AA3)  #uni2AA3	DOUBLE NESTED LESS-THAN WITH UNDERBAR
        chars.append(0x2AA4)  #uni2AA4	GREATER-THAN OVERLAPPING LESS-THAN
        chars.append(0x2AA5)  #uni2AA5	GREATER-THAN BESIDE LESS-THAN
        chars.append(0x2AA6)  #uni2AA6	LESS-THAN CLOSED BY CURVE
        chars.append(0x2AA7)  #uni2AA7	GREATER-THAN CLOSED BY CURVE
        chars.append(0x2AA8)  #uni2AA8	LESS-THAN CLOSED BY CURVE ABOVE SLANTED EQUAL
        chars.append(0x2AA9)  #uni2AA9	GREATER-THAN CLOSED BY CURVE ABOVE SLANTED EQUAL
        chars.append(0x2AAA)  #uni2AAA	SMALLER THAN
        chars.append(0x2AAB)  #uni2AAB	LARGER THAN
        chars.append(0x2AAC)  #uni2AAC	SMALLER THAN OR EQUAL TO
        chars.append(0x2AAD)  #uni2AAD	LARGER THAN OR EQUAL TO
        chars.append(0x2AAE)  #uni2AAE	EQUALS SIGN WITH BUMPY ABOVE
        chars.append(0x2AAF)  #uni2AAF	PRECEDES ABOVE SINGLE-LINE EQUALS SIGN
        chars.append(0x2AB0)  #uni2AB0	SUCCEEDS ABOVE SINGLE-LINE EQUALS SIGN
        chars.append(0x2AB1)  #uni2AB1	PRECEDES ABOVE SINGLE-LINE NOT EQUAL TO
        chars.append(0x2AB2)  #uni2AB2	SUCCEEDS ABOVE SINGLE-LINE NOT EQUAL TO
        chars.append(0x2AB3)  #uni2AB3	PRECEDES ABOVE EQUALS SIGN
        chars.append(0x2AB4)  #uni2AB4	SUCCEEDS ABOVE EQUALS SIGN
        chars.append(0x2AB5)  #uni2AB5	PRECEDES ABOVE NOT EQUAL TO
        chars.append(0x2AB6)  #uni2AB6	SUCCEEDS ABOVE NOT EQUAL TO
        chars.append(0x2AB7)  #uni2AB7	PRECEDES ABOVE ALMOST EQUAL TO
        chars.append(0x2AB8)  #uni2AB8	SUCCEEDS ABOVE ALMOST EQUAL TO
        chars.append(0x2AB9)  #uni2AB9	PRECEDES ABOVE NOT ALMOST EQUAL TO
        chars.append(0x2ABA)  #uni2ABA	SUCCEEDS ABOVE NOT ALMOST EQUAL TO
        chars.append(0x2ABB)  #uni2ABB	DOUBLE PRECEDES
        chars.append(0x2ABC)  #uni2ABC	DOUBLE SUCCEEDS
        chars.append(0x2ABD)  #uni2ABD	SUBSET WITH DOT
        chars.append(0x2ABE)  #uni2ABE	SUPERSET WITH DOT
        chars.append(0x2ABF)  #uni2ABF	SUBSET WITH PLUS SIGN BELOW
        chars.append(0x2AC0)  #uni2AC0	SUPERSET WITH PLUS SIGN BELOW
        chars.append(0x2AC1)  #uni2AC1	SUBSET WITH MULTIPLICATION SIGN BELOW
        chars.append(0x2AC2)  #uni2AC2	SUPERSET WITH MULTIPLICATION SIGN BELOW
        chars.append(0x2AC3)  #uni2AC3	SUBSET OF OR EQUAL TO WITH DOT ABOVE
        chars.append(0x2AC4)  #uni2AC4	SUPERSET OF OR EQUAL TO WITH DOT ABOVE
        chars.append(0x2AC5)  #uni2AC5	SUBSET OF ABOVE EQUALS SIGN
        chars.append(0x2AC6)  #uni2AC6	SUPERSET OF ABOVE EQUALS SIGN
        chars.append(0x2AC7)  #uni2AC7	SUBSET OF ABOVE TILDE OPERATOR
        chars.append(0x2AC8)  #uni2AC8	SUPERSET OF ABOVE TILDE OPERATOR
        chars.append(0x2AC9)  #uni2AC9	SUBSET OF ABOVE ALMOST EQUAL TO
        chars.append(0x2ACA)  #uni2ACA	SUPERSET OF ABOVE ALMOST EQUAL TO
        chars.append(0x2ACB)  #uni2ACB	SUBSET OF ABOVE NOT EQUAL TO
        chars.append(0x2ACC)  #uni2ACC	SUPERSET OF ABOVE NOT EQUAL TO
        chars.append(0x2ACD)  #uni2ACD	SQUARE LEFT OPEN BOX OPERATOR
        chars.append(0x2ACE)  #uni2ACE	SQUARE RIGHT OPEN BOX OPERATOR
        chars.append(0x2ACF)  #uni2ACF	CLOSED SUBSET
        chars.append(0x2AD0)  #uni2AD0	CLOSED SUPERSET
        chars.append(0x2AD1)  #uni2AD1	CLOSED SUBSET OR EQUAL TO
        chars.append(0x2AD2)  #uni2AD2	CLOSED SUPERSET OR EQUAL TO
        chars.append(0x2AD3)  #uni2AD3	SUBSET ABOVE SUPERSET
        chars.append(0x2AD4)  #uni2AD4	SUPERSET ABOVE SUBSET
        chars.append(0x2AD5)  #uni2AD5	SUBSET ABOVE SUBSET
        chars.append(0x2AD6)  #uni2AD6	SUPERSET ABOVE SUPERSET
        chars.append(0x2AD7)  #uni2AD7	SUPERSET BESIDE SUBSET
        chars.append(0x2AD8)  #uni2AD8	SUPERSET BESIDE AND JOINED BY DASH WITH SUBSET
        chars.append(0x2AD9)  #uni2AD9	ELEMENT OF OPENING DOWNWARDS
        chars.append(0x2ADA)  #uni2ADA	PITCHFORK WITH TEE TOP
        chars.append(0x2ADB)  #uni2ADB	TRANSVERSAL INTERSECTION
        chars.append(0x2ADC)  #uni2ADC	FORKING
        chars.append(0x2ADD)  #uni2ADD	NONFORKING
        chars.append(0x2ADE)  #uni2ADE	SHORT LEFT TACK
        chars.append(0x2ADF)  #uni2ADF	SHORT DOWN TACK
        chars.append(0x2AE0)  #uni2AE0	SHORT UP TACK
        chars.append(0x2AE1)  #uni2AE1	PERPENDICULAR WITH S
        chars.append(0x2AE2)  #uni2AE2	VERTICAL BAR TRIPLE RIGHT TURNSTILE
        chars.append(0x2AE3)  #uni2AE3	DOUBLE VERTICAL BAR LEFT TURNSTILE
        chars.append(0x2AE4)  #uni2AE4	VERTICAL BAR DOUBLE LEFT TURNSTILE
        chars.append(0x2AE5)  #uni2AE5	DOUBLE VERTICAL BAR DOUBLE LEFT TURNSTILE
        chars.append(0x2AE6)  #uni2AE6	LONG DASH FROM LEFT MEMBER OF DOUBLE VERTICAL
        chars.append(0x2AE7)  #uni2AE7	SHORT DOWN TACK WITH OVERBAR
        chars.append(0x2AE8)  #uni2AE8	SHORT UP TACK WITH UNDERBAR
        chars.append(0x2AE9)  #uni2AE9	SHORT UP TACK ABOVE SHORT DOWN TACK
        chars.append(0x2AEA)  #uni2AEA	DOUBLE DOWN TACK
        chars.append(0x2AEB)  #uni2AEB	DOUBLE UP TACK
        chars.append(0x2AEC)  #uni2AEC	DOUBLE STROKE NOT SIGN
        chars.append(0x2AED)  #uni2AED	REVERSED DOUBLE STROKE NOT SIGN
        chars.append(0x2AEE)  #uni2AEE	DOES NOT DIVIDE WITH REVERSED NEGATION SLASH
        chars.append(0x2AEF)  #uni2AEF	VERTICAL LINE WITH CIRCLE ABOVE
        chars.append(0x2AF0)  #uni2AF0	VERTICAL LINE WITH CIRCLE BELOW
        chars.append(0x2AF1)  #uni2AF1	DOWN TACK WITH CIRCLE BELOW
        chars.append(0x2AF2)  #uni2AF2	PARALLEL WITH HORIZONTAL STROKE
        chars.append(0x2AF3)  #uni2AF3	PARALLEL WITH TILDE OPERATOR
        chars.append(0x2AF4)  #uni2AF4	TRIPLE VERTICAL BAR BINARY RELATION
        chars.append(0x2AF5)  #uni2AF5	TRIPLE VERTICAL BAR WITH HORIZONTAL STROKE
        chars.append(0x2AF6)  #uni2AF6	TRIPLE COLON OPERATOR
        chars.append(0x2AF7)  #uni2AF7	TRIPLE NESTED LESS-THAN
        chars.append(0x2AF8)  #uni2AF8	TRIPLE NESTED GREATER-THAN
        chars.append(0x2AF9)  #uni2AF9	DOUBLE-LINE SLANTED LESS-THAN OR EQUAL TO
        chars.append(0x2AFA)  #uni2AFA	DOUBLE-LINE SLANTED GREATER-THAN OR EQUAL TO
        chars.append(0x2AFB)  #uni2AFB	TRIPLE SOLIDUS BINARY RELATION
        chars.append(0x2AFC)  #uni2AFC	LARGE TRIPLE VERTICAL BAR OPERATOR
        chars.append(0x2AFD)  #uni2AFD	DOUBLE SOLIDUS OPERATOR
        chars.append(0x2AFE)  #uni2AFE	WHITE VERTICAL BAR
        chars.append(0x2AFF)  #uni2AFF	N-ARY WHITE VERTICAL BAR
        chars.append(0x2B00)  #uni2B00	NORTH EAST WHITE ARROW
        chars.append(0x2B01)  #uni2B01	NORTH WEST WHITE ARROW
        chars.append(0x2B02)  #uni2B02	SOUTH EAST WHITE ARROW
        chars.append(0x2B03)  #uni2B03	SOUTH WEST WHITE ARROW
        chars.append(0x2B04)  #uni2B04	LEFT RIGHT WHITE ARROW
        chars.append(0x2B05)  #uni2B05	LEFTWARDS BLACK ARROW
        chars.append(0x2B06)  #uni2B06	UPWARDS BLACK ARROW
        chars.append(0x2B07)  #uni2B07	DOWNWARDS BLACK ARROW
        chars.append(0x2B08)  #uni2B08	NORTH EAST BLACK ARROW
        chars.append(0x2B09)  #uni2B09	NORTH WEST BLACK ARROW
        chars.append(0x2B0A)  #uni2B0A	SOUTH EAST BLACK ARROW
        chars.append(0x2B0B)  #uni2B0B	SOUTH WEST BLACK ARROW
        chars.append(0x2B0C)  #uni2B0C	LEFT RIGHT BLACK ARROW
        chars.append(0x2B0D)  #uni2B0D	UP DOWN BLACK ARROW
        chars.append(0x2B0E)  #uni2B0E	RIGHTWARDS ARROW WITH TIP DOWNWARDS
        chars.append(0x2B0F)  #uni2B0F	RIGHTWARDS ARROW WITH TIP UPWARDS
        chars.append(0x2B10)  #uni2B10	LEFTWARDS ARROW WITH TIP DOWNWARDS
        chars.append(0x2B11)  #uni2B11	LEFTWARDS ARROW WITH TIP UPWARDS
        chars.append(0x2B12)  #uni2B12	SQUARE WITH TOP HALF BLACK
        chars.append(0x2B13)  #uni2B13	SQUARE WITH BOTTOM HALF BLACK
        chars.append(0x2B14)  #uni2B14	SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK
        chars.append(0x2B15)  #uni2B15	SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK
        chars.append(0x2B16)  #uni2B16	DIAMOND WITH LEFT HALF BLACK
        chars.append(0x2B17)  #uni2B17	DIAMOND WITH RIGHT HALF BLACK
        chars.append(0x2B18)  #uni2B18	DIAMOND WITH TOP HALF BLACK
        chars.append(0x2B19)  #uni2B19	DIAMOND WITH BOTTOM HALF BLACK
        chars.append(0x2B1A)  #uni2B1A	DOTTED SQUARE
        chars.append(0x2B1B)  #uni2B1B	BLACK LARGE SQUARE
        chars.append(0x2B1C)  #uni2B1C	WHITE LARGE SQUARE
        chars.append(0x2B1D)  #uni2B1D	BLACK VERY SMALL SQUARE
        chars.append(0x2B1E)  #uni2B1E	WHITE VERY SMALL SQUARE
        chars.append(0x2B1F)  #uni2B1F	BLACK PENTAGON
        chars.append(0x2B20)  #uni2B20	WHITE PENTAGON
        chars.append(0x2B21)  #uni2B21	WHITE HEXAGON
        chars.append(0x2B22)  #uni2B22	BLACK HEXAGON
        chars.append(0x2B23)  #uni2B23	HORIZONTAL BLACK HEXAGON
        chars.append(0x2B24)  #uni2B24	BLACK LARGE CIRCLE
        chars.append(0x2B25)  #uni2B25	BLACK MEDIUM DIAMOND
        chars.append(0x2B26)  #uni2B26	WHITE MEDIUM DIAMOND
        chars.append(0x2B27)  #uni2B27	BLACK MEDIUM LOZENGE
        chars.append(0x2B28)  #uni2B28	WHITE MEDIUM LOZENGE
        chars.append(0x2B29)  #uni2B29	BLACK SMALL DIAMOND
        chars.append(0x2B2A)  #uni2B2A	BLACK SMALL LOZENGE
        chars.append(0x2B2B)  #uni2B2B	WHITE SMALL LOZENGE
        chars.append(0x2B2C)  #uni2B2C	BLACK HORIZONTAL ELLIPSE
        chars.append(0x2B2D)  #uni2B2D	WHITE HORIZONTAL ELLIPSE
        chars.append(0x2B2E)  #uni2B2E	BLACK VERTICAL ELLIPSE
        chars.append(0x2B2F)  #uni2B2F	WHITE VERTICAL ELLIPSE
        chars.append(0x2B30)  #uni2B30	LEFT ARROW WITH SMALL CIRCLE
        chars.append(0x2B31)  #uni2B31	THREE LEFTWARDS ARROWS
        chars.append(0x2B32)  #uni2B32	LEFT ARROW WITH CIRCLED PLUS
        chars.append(0x2B33)  #uni2B33	LONG LEFTWARDS SQUIGGLE ARROW
        chars.append(0x2B34)  #uni2B34	LEFTWARDS TWO-HEADED ARROW WITH VERTICAL STROKE
        chars.append(0x2B35)  #uni2B35	LEFTWARDS TWO-HEADED ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x2B36)  #uni2B36	LEFTWARDS TWO-HEADED ARROW FROM BAR
        chars.append(0x2B37)  #uni2B37	LEFTWARDS TWO-HEADED TRIPLE DASH ARROW
        chars.append(0x2B38)  #uni2B38	LEFTWARDS ARROW WITH DOTTED STEM
        chars.append(0x2B39)  #uni2B39	LEFTWARDS ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2B3A)  #uni2B3A	LEFTWARDS ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2B3B)  #uni2B3B	LEFTWARDS TWO-HEADED ARROW WITH TAIL
        chars.append(0x2B3C)  #uni2B3C	LEFTWARDS TWO-HEADED ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2B3D)  #uni2B3D	LEFTWARDS TWO-HEADED ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2B3E)  #uni2B3E	LEFTWARDS ARROW THROUGH X
        chars.append(0x2B3F)  #uni2B3F	WAVE ARROW POINTING DIRECTLY LEFT
        chars.append(0x2B40)  #uni2B40	EQUALS SIGN ABOVE LEFTWARDS ARROW
        chars.append(0x2B41)  #uni2B41	REVERSE TILDE OPERATOR ABOVE LEFTWARDS ARROW
        chars.append(0x2B42)  #uni2B42	LEFTWARDS ARROW ABOVE REVERSE ALMOST EQUAL TO
        chars.append(0x2B43)  #uni2B43	RIGHTWARDS ARROW THROUGH GREATER-THAN
        chars.append(0x2B44)  #uni2B44	RIGHTWARDS ARROW THROUGH SUPERSET
        chars.append(0x2B45)  #uni2B45	LEFTWARDS QUADRUPLE ARROW
        chars.append(0x2B46)  #uni2B46	RIGHTWARDS QUADRUPLE ARROW
        chars.append(0x2B47)  #uni2B47	REVERSE TILDE OPERATOR ABOVE RIGHTWARDS ARROW
        chars.append(0x2B48)  #uni2B48	RIGHTWARDS ARROW ABOVE REVERSE ALMOST EQUAL TO
        chars.append(0x2B49)  #uni2B49	TILDE OPERATOR ABOVE LEFTWARDS ARROW
        chars.append(0x2B4A)  #uni2B4A	LEFTWARDS ARROW ABOVE ALMOST EQUAL TO
        chars.append(0x2B4B)  #uni2B4B	LEFTWARDS ARROW ABOVE REVERSE TILDE OPERATOR
        chars.append(0x2B4C)  #uni2B4C	RIGHTWARDS ARROW ABOVE REVERSE TILDE OPERATOR
        chars.append(0x2B50)  #uni2B50	WHITE MEDIUM STAR
        chars.append(0x2B51)  #uni2B51	BLACK SMALL STAR
        chars.append(0x2B52)  #uni2B52	WHITE SMALL STAR
        chars.append(0x2B53)  #uni2B53	BLACK RIGHT-POINTING PENTAGON
        chars.append(0x2B54)  #uni2B54	WHITE RIGHT-POINTING PENTAGON
        chars.append(0x2B55)  #uni2B55	HEAVY LARGE CIRCLE
        chars.append(0x2B56)  #uni2B56	HEAVY OVAL WITH OVAL INSIDE
        chars.append(0x2B57)  #uni2B57	HEAVY CIRCLE WITH CIRCLE INSIDE
        chars.append(0x2B58)  #uni2B58	HEAVY CIRCLE
        chars.append(0x2B59)  #uni2B59	HEAVY CIRCLED SALTIRE
        chars.append(0x4DC0)  #uni4DC0	HEXAGRAM FOR THE CREATIVE HEAVEN
        chars.append(0x4DC1)  #uni4DC1	HEXAGRAM FOR THE RECEPTIVE EARTH
        chars.append(0x4DC2)  #uni4DC2	HEXAGRAM FOR DIFFICULTY AT THE BEGINNING
        chars.append(0x4DC3)  #uni4DC3	HEXAGRAM FOR YOUTHFUL FOLLY
        chars.append(0x4DC4)  #uni4DC4	HEXAGRAM FOR WAITING
        chars.append(0x4DC5)  #uni4DC5	HEXAGRAM FOR CONFLICT
        chars.append(0x4DC6)  #uni4DC6	HEXAGRAM FOR THE ARMY
        chars.append(0x4DC7)  #uni4DC7	HEXAGRAM FOR HOLDING TOGETHER
        chars.append(0x4DC8)  #uni4DC8	HEXAGRAM FOR SMALL TAMING
        chars.append(0x4DC9)  #uni4DC9	HEXAGRAM FOR TREADING
        chars.append(0x4DCA)  #uni4DCA	HEXAGRAM FOR PEACE
        chars.append(0x4DCB)  #uni4DCB	HEXAGRAM FOR STANDSTILL
        chars.append(0x4DCC)  #uni4DCC	HEXAGRAM FOR FELLOWSHIP
        chars.append(0x4DCD)  #uni4DCD	HEXAGRAM FOR GREAT POSSESSION
        chars.append(0x4DCE)  #uni4DCE	HEXAGRAM FOR MODESTY
        chars.append(0x4DCF)  #uni4DCF	HEXAGRAM FOR ENTHUSIASM
        chars.append(0x4DD0)  #uni4DD0	HEXAGRAM FOR FOLLOWING
        chars.append(0x4DD1)  #uni4DD1	HEXAGRAM FOR WORK ON THE DECAYED
        chars.append(0x4DD2)  #uni4DD2	HEXAGRAM FOR APPROACH
        chars.append(0x4DD3)  #uni4DD3	HEXAGRAM FOR CONTEMPLATION
        chars.append(0x4DD4)  #uni4DD4	HEXAGRAM FOR BITING THROUGH
        chars.append(0x4DD5)  #uni4DD5	HEXAGRAM FOR GRACE
        chars.append(0x4DD6)  #uni4DD6	HEXAGRAM FOR SPLITTING APART
        chars.append(0x4DD7)  #uni4DD7	HEXAGRAM FOR RETURN
        chars.append(0x4DD8)  #uni4DD8	HEXAGRAM FOR INNOCENCE
        chars.append(0x4DD9)  #uni4DD9	HEXAGRAM FOR GREAT TAMING
        chars.append(0x4DDA)  #uni4DDA	HEXAGRAM FOR MOUTH CORNERS
        chars.append(0x4DDB)  #uni4DDB	HEXAGRAM FOR GREAT PREPONDERANCE
        chars.append(0x4DDC)  #uni4DDC	HEXAGRAM FOR THE ABYSMAL WATER
        chars.append(0x4DDD)  #uni4DDD	HEXAGRAM FOR THE CLINGING FIRE
        chars.append(0x4DDE)  #uni4DDE	HEXAGRAM FOR INFLUENCE
        chars.append(0x4DDF)  #uni4DDF	HEXAGRAM FOR DURATION
        chars.append(0x4DE0)  #uni4DE0	HEXAGRAM FOR RETREAT
        chars.append(0x4DE1)  #uni4DE1	HEXAGRAM FOR GREAT POWER
        chars.append(0x4DE2)  #uni4DE2	HEXAGRAM FOR PROGRESS
        chars.append(0x4DE3)  #uni4DE3	HEXAGRAM FOR DARKENING OF THE LIGHT
        chars.append(0x4DE4)  #uni4DE4	HEXAGRAM FOR THE FAMILY
        chars.append(0x4DE5)  #uni4DE5	HEXAGRAM FOR OPPOSITION
        chars.append(0x4DE6)  #uni4DE6	HEXAGRAM FOR OBSTRUCTION
        chars.append(0x4DE7)  #uni4DE7	HEXAGRAM FOR DELIVERANCE
        chars.append(0x4DE8)  #uni4DE8	HEXAGRAM FOR DECREASE
        chars.append(0x4DE9)  #uni4DE9	HEXAGRAM FOR INCREASE
        chars.append(0x4DEA)  #uni4DEA	HEXAGRAM FOR BREAKTHROUGH
        chars.append(0x4DEB)  #uni4DEB	HEXAGRAM FOR COMING TO MEET
        chars.append(0x4DEC)  #uni4DEC	HEXAGRAM FOR GATHERING TOGETHER
        chars.append(0x4DED)  #uni4DED	HEXAGRAM FOR PUSHING UPWARD
        chars.append(0x4DEE)  #uni4DEE	HEXAGRAM FOR OPPRESSION
        chars.append(0x4DEF)  #uni4DEF	HEXAGRAM FOR THE WELL
        chars.append(0x4DF0)  #uni4DF0	HEXAGRAM FOR REVOLUTION
        chars.append(0x4DF1)  #uni4DF1	HEXAGRAM FOR THE CAULDRON
        chars.append(0x4DF2)  #uni4DF2	HEXAGRAM FOR THE AROUSING THUNDER
        chars.append(0x4DF3)  #uni4DF3	HEXAGRAM FOR THE KEEPING STILL MOUNTAIN
        chars.append(0x4DF4)  #uni4DF4	HEXAGRAM FOR DEVELOPMENT
        chars.append(0x4DF5)  #uni4DF5	HEXAGRAM FOR THE MARRYING MAIDEN
        chars.append(0x4DF6)  #uni4DF6	HEXAGRAM FOR ABUNDANCE
        chars.append(0x4DF7)  #uni4DF7	HEXAGRAM FOR THE WANDERER
        chars.append(0x4DF8)  #uni4DF8	HEXAGRAM FOR THE GENTLE WIND
        chars.append(0x4DF9)  #uni4DF9	HEXAGRAM FOR THE JOYOUS LAKE
        chars.append(0x4DFA)  #uni4DFA	HEXAGRAM FOR DISPERSION
        chars.append(0x4DFB)  #uni4DFB	HEXAGRAM FOR LIMITATION
        chars.append(0x4DFC)  #uni4DFC	HEXAGRAM FOR INNER TRUTH
        chars.append(0x4DFD)  #uni4DFD	HEXAGRAM FOR SMALL PREPONDERANCE
        chars.append(0x4DFE)  #uni4DFE	HEXAGRAM FOR AFTER COMPLETION
        chars.append(0x4DFF)  #uni4DFF	HEXAGRAM FOR BEFORE COMPLETION
        chars.append(0x2E00)  #uni2E00	RIGHT ANGLE SUBSTITUTION MARKER
        chars.append(0x2E01)  #uni2E01	RIGHT ANGLE DOTTED SUBSTITUTION MARKER
        chars.append(0x2E02)  #uni2E02	LEFT SUBSTITUTION BRACKET
        chars.append(0x2E03)  #uni2E03	RIGHT SUBSTITUTION BRACKET
        chars.append(0x2E04)  #uni2E04	LEFT DOTTED SUBSTITUTION BRACKET
        chars.append(0x2E05)  #uni2E05	RIGHT DOTTED SUBSTITUTION BRACKET
        chars.append(0x2E06)  #uni2E06	RAISED INTERPOLATION MARKER
        chars.append(0x2E07)  #uni2E07	RAISED DOTTED INTERPOLATION MARKER
        chars.append(0x2E08)  #uni2E08	DOTTED TRANSPOSITION MARKER
        chars.append(0x2E09)  #uni2E09	LEFT TRANSPOSITION BRACKET
        chars.append(0x2E0A)  #uni2E0A	RIGHT TRANSPOSITION BRACKET
        chars.append(0x2E0B)  #uni2E0B	RAISED SQUARE
        chars.append(0x2E0C)  #uni2E0C	LEFT RAISED OMISSION BRACKET
        chars.append(0x2E0D)  #uni2E0D	RIGHT RAISED OMISSION BRACKET
        chars.append(0x2E0E)  #uni2E0E	EDITORIAL CORONIS
        chars.append(0x2E0F)  #uni2E0F	PARAGRAPHOS
        chars.append(0x2E10)  #uni2E10	FORKED PARAGRAPHOS
        chars.append(0x2E11)  #uni2E11	REVERSED FORKED PARAGRAPHOS
        chars.append(0x2E12)  #uni2E12	HYPODIASTOLE
        chars.append(0x2E13)  #uni2E13	DOTTED OBELOS
        chars.append(0x2E14)  #uni2E14	DOWNWARDS ANCORA
        chars.append(0x2E15)  #uni2E15	UPWARDS ANCORA
        chars.append(0x2E16)  #uni2E16	DOTTED RIGHT-POINTING ANGLE
        chars.append(0x2E17)  #uni2E17	DOUBLE OBLIQUE HYPHEN
        chars.append(0x2E18)  #uni2E18	INVERTED INTERROBANG
        chars.append(0x2E19)  #uni2E19	PALM BRANCH
        chars.append(0x2E1A)  #uni2E1A	HYPHEN WITH DIAERESIS
        chars.append(0x2E1B)  #uni2E1B	TILDE WITH RING ABOVE
        chars.append(0x2E1C)  #uni2E1C	LEFT LOW PARAPHRASE BRACKET
        chars.append(0x2E1D)  #uni2E1D	RIGHT LOW PARAPHRASE BRACKET
        chars.append(0x2E1E)  #uni2E1E	TILDE WITH DOT ABOVE
        chars.append(0x2E1F)  #uni2E1F	TILDE WITH DOT BELOW
        chars.append(0x2E20)  #uni2E20	LEFT VERTICAL BAR WITH QUILL
        chars.append(0x2E21)  #uni2E21	RIGHT VERTICAL BAR WITH QUILL
        chars.append(0x2E22)  #uni2E22	TOP LEFT HALF BRACKET
        chars.append(0x2E23)  #uni2E23	TOP RIGHT HALF BRACKET
        chars.append(0x2E24)  #uni2E24	BOTTOM LEFT HALF BRACKET
        chars.append(0x2E25)  #uni2E25	BOTTOM RIGHT HALF BRACKET
        chars.append(0x2E26)  #uni2E26	LEFT SIDEWAYS U BRACKET
        chars.append(0x2E27)  #uni2E27	RIGHT SIDEWAYS U BRACKET
        chars.append(0x2E28)  #uni2E28	LEFT DOUBLE PARENTHESIS
        chars.append(0x2E29)  #uni2E29	RIGHT DOUBLE PARENTHESIS
        chars.append(0x2E2A)  #uni2E2A	TWO DOTS OVER ONE DOT PUNCTUATION
        chars.append(0x2E2B)  #uni2E2B	ONE DOT OVER TWO DOTS PUNCTUATION
        chars.append(0x2E2C)  #uni2E2C	SQUARED FOUR DOT PUNCTUATION
        chars.append(0x2E2D)  #uni2E2D	FIVE DOT MARK
        chars.append(0x2E2E)  #uni2E2E	REVERSED QUESTION MARK
        chars.append(0x2E2F)  #uni2E2F	VERTICAL TILDE
        chars.append(0x2E30)  #uni2E30	RING POINT
        chars.append(0x2E31)  #uni2E31	WORD SEPARATOR MIDDLE DOT
        chars.append(0x2E32)  #uni2E32	????
        chars.append(0x2E33)  #uni2E33	????
        chars.append(0x2E34)  #uni2E34	????
        chars.append(0x2E35)  #uni2E35	????
        chars.append(0x2E36)  #uni2E36	????
        chars.append(0x2E37)  #uni2E37	????
        chars.append(0x2E38)  #uni2E38	????
        chars.append(0x2E39)  #uni2E39	????
        chars.append(0x2E3A)  #uni2E3A	????
        chars.append(0x2E3B)  #uni2E3B	????
        chars.append(0x3008)  #uni3008	LEFT ANGLE BRACKET
        chars.append(0x3009)  #uni3009	RIGHT ANGLE BRACKET
        chars.append(0x2338)  #uni2338	APL FUNCTIONAL SYMBOL QUAD EQUAL
        chars.append(0x23C1)  #uni23C1	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH CIRCLE
        chars.append(0xA701)  #uniA701	MODIFIER LETTER CHINESE TONE YANG PING
        chars.append(0xA702)  #uniA702	MODIFIER LETTER CHINESE TONE YIN SHANG
        chars.append(0xA703)  #uniA703	MODIFIER LETTER CHINESE TONE YANG SHANG
        chars.append(0xA704)  #uniA704	MODIFIER LETTER CHINESE TONE YIN QU
        chars.append(0xA705)  #uniA705	MODIFIER LETTER CHINESE TONE YANG QU
        chars.append(0xA706)  #uniA706	MODIFIER LETTER CHINESE TONE YIN RU
        chars.append(0xA707)  #uniA707	MODIFIER LETTER CHINESE TONE YANG RU
        chars.append(0xA708)  #uniA708	MODIFIER LETTER EXTRA-HIGH DOTTED TONE BAR
        chars.append(0xA709)  #uniA709	MODIFIER LETTER HIGH DOTTED TONE BAR
        chars.append(0xA70A)  #uniA70A	MODIFIER LETTER MID DOTTED TONE BAR
        chars.append(0xA70B)  #uniA70B	MODIFIER LETTER LOW DOTTED TONE BAR
        chars.append(0xA70C)  #uniA70C	MODIFIER LETTER EXTRA-LOW DOTTED TONE BAR
        chars.append(0xA70D)  #uniA70D	MODIFIER LETTER EXTRA-HIGH DOTTED LEFT-STEM TONE BAR
        chars.append(0xA70E)  #uniA70E	MODIFIER LETTER HIGH DOTTED LEFT-STEM TONE BAR
        chars.append(0xA70F)  #uniA70F	MODIFIER LETTER MID DOTTED LEFT-STEM TONE BAR
        chars.append(0xA710)  #uniA710	MODIFIER LETTER LOW DOTTED LEFT-STEM TONE BAR
        chars.append(0xA711)  #uniA711	MODIFIER LETTER EXTRA-LOW DOTTED LEFT-STEM TONE BAR
        chars.append(0xA712)  #uniA712	MODIFIER LETTER EXTRA-HIGH LEFT-STEM TONE BAR
        chars.append(0xA713)  #uniA713	MODIFIER LETTER HIGH LEFT-STEM TONE BAR
        chars.append(0xA714)  #uniA714	MODIFIER LETTER MID LEFT-STEM TONE BAR
        chars.append(0xA715)  #uniA715	MODIFIER LETTER LOW LEFT-STEM TONE BAR
        chars.append(0xA716)  #uniA716	MODIFIER LETTER EXTRA-LOW LEFT-STEM TONE BAR
        chars.append(0xA717)  #uniA717	MODIFIER LETTER DOT VERTICAL BAR
        chars.append(0xA718)  #uniA718	MODIFIER LETTER DOT SLASH
        chars.append(0xA719)  #uniA719	MODIFIER LETTER DOT HORIZONTAL BAR
        chars.append(0xA71A)  #uniA71A	MODIFIER LETTER LOWER RIGHT CORNER ANGLE
        chars.append(0xA71B)  #uniA71B	MODIFIER LETTER RAISED UP ARROW
        chars.append(0xA71C)  #uniA71C	MODIFIER LETTER RAISED DOWN ARROW
        chars.append(0xA71D)  #uniA71D	MODIFIER LETTER RAISED EXCLAMATION MARK
        chars.append(0xA71E)  #uniA71E	MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK
        chars.append(0xA71F)  #uniA71F	MODIFIER LETTER LOW INVERTED EXCLAMATION MARK
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0xFFF9)  #uniFFF9	INTERLINEAR ANNOTATION ANCHOR
        chars.append(0xFFFA)  #uniFFFA	INTERLINEAR ANNOTATION SEPARATOR
        chars.append(0xFFFB)  #uniFFFB	INTERLINEAR ANNOTATION TERMINATOR
        chars.append(0xFFFC)  #uniFFFC	OBJECT REPLACEMENT CHARACTER
        chars.append(0xFFFD)  #uniFFFD	REPLACEMENT CHARACTER
        chars.append(0x0000)  #uniFEFF	????
        chars.append(0x1F000)  #glyph04578	MAHJONG TILE EAST WIND
        chars.append(0x1F001)  #glyph04579	MAHJONG TILE SOUTH WIND
        chars.append(0x000D)  #uni000D	????
        chars.append(0x10144)  #glyph02812	GREEK ACROPHONIC ATTIC FIFTY
        chars.append(0x1F003)  #glyph04581	MAHJONG TILE NORTH WIND
        chars.append(0x101DE)  #glyph02909	PHAISTOS DISC SIGN MATTOCK
        chars.append(0x1F004)  #glyph04582	MAHJONG TILE RED DRAGON
        chars.append(0x1F005)  #glyph04583	MAHJONG TILE GREEN DRAGON
        chars.append(0x0020)  #uni00A0	SPACE
        chars.append(0x101DD)  #glyph02908	PHAISTOS DISC SIGN MANACLES
        chars.append(0x1F006)  #glyph04584	MAHJONG TILE WHITE DRAGON
        chars.append(0x1F007)  #glyph04585	MAHJONG TILE ONE OF CHARACTERS
        chars.append(0x1F08E)  #glyph04716	DOMINO TILE VERTICAL-06-01
        chars.append(0x1D008)  #glyph02949	BYZANTINE MUSICAL SYMBOL SYRMATIKI
        chars.append(0x1F70E)  #glyph05023	????
        chars.append(0x101DF)  #glyph02910	PHAISTOS DISC SIGN SAW
        chars.append(0x1D009)  #glyph02950	BYZANTINE MUSICAL SYMBOL PARAKLITIKI
        chars.append(0x1F030)  #glyph04622	DOMINO TILE HORIZONTAL BACK
        chars.append(0x1F00A)  #glyph04588	MAHJONG TILE FOUR OF CHARACTERS
        chars.append(0x1F00B)  #glyph04589	MAHJONG TILE FIVE OF CHARACTERS
        chars.append(0x1D1B0)  #glyph03361	MUSICAL SYMBOL HALF PEDAL MARK
        chars.append(0x1F00C)  #glyph04590	MAHJONG TILE SIX OF CHARACTERS
        chars.append(0x1F08F)  #glyph04717	DOMINO TILE VERTICAL-06-02
        chars.append(0x1F00D)  #glyph04591	MAHJONG TILE SEVEN OF CHARACTERS
        chars.append(0x1F71C)  #glyph05037	????
        chars.append(0x101E0)  #glyph02911	PHAISTOS DISC SIGN LID
        chars.append(0x1F00F)  #glyph04593	MAHJONG TILE NINE OF CHARACTERS
        chars.append(0x1F734)  #glyph05061	????
        chars.append(0x1F010)  #glyph04594	MAHJONG TILE ONE OF BAMBOOS
        chars.append(0x1F727)  #glyph05048	????
        chars.append(0x1D566)  #glyph03916	MATHEMATICAL DOUBLE-STRUCK SMALL U
        chars.append(0x1F011)  #glyph04595	MAHJONG TILE TWO OF BAMBOOS
        chars.append(0x1F130)  #glyph04823	????
        chars.append(0x1F090)  #glyph04718	DOMINO TILE VERTICAL-06-03
        chars.append(0x1F012)  #glyph04596	MAHJONG TILE THREE OF BAMBOOS
        chars.append(0x101E1)  #glyph02912	PHAISTOS DISC SIGN BOOMERANG
        chars.append(0x1F014)  #glyph04598	MAHJONG TILE FIVE OF BAMBOOS
        chars.append(0x1F0C3)  #glyph04753	????
        chars.append(0x1F0A8)  #glyph04730	????
        chars.append(0x1F015)  #glyph04599	MAHJONG TILE SIX OF BAMBOOS
        chars.append(0x1D016)  #glyph02963	BYZANTINE MUSICAL SYMBOL GORGON ARCHAION
        chars.append(0x1F091)  #glyph04719	DOMINO TILE VERTICAL-06-04
        chars.append(0x1F017)  #glyph04601	MAHJONG TILE EIGHT OF BAMBOOS
        chars.append(0x1F018)  #glyph04602	MAHJONG TILE NINE OF BAMBOOS
        chars.append(0x1F019)  #glyph04603	MAHJONG TILE ONE OF CIRCLES
        chars.append(0x1F01A)  #glyph04604	MAHJONG TILE TWO OF CIRCLES
        chars.append(0x20A0)  #uni20A0	EURO-CURRENCY SIGN
        chars.append(0x20A1)  #colonmonetary	COLON SIGN
        chars.append(0x20A2)  #uni20A2	CRUZEIRO SIGN
        chars.append(0x20A3)  #franc	FRENCH FRANC SIGN
        chars.append(0x20A4)  #lira	LIRA SIGN
        chars.append(0x20A5)  #uni20A5	MILL SIGN
        chars.append(0x20A6)  #uni20A6	NAIRA SIGN
        chars.append(0x20A7)  #peseta	PESETA SIGN
        chars.append(0x20A8)  #uni20A8	RUPEE SIGN
        chars.append(0x20A9)  #uni20A9	WON SIGN
        chars.append(0x20AA)  #uni20AA	NEW SHEQEL SIGN
        chars.append(0x20AB)  #dong	DONG SIGN
        chars.append(0x20AC)  #Euro	EURO SIGN
        chars.append(0x20AD)  #uni20AD	KIP SIGN
        chars.append(0x20AE)  #uni20AE	TUGRIK SIGN
        chars.append(0x20AF)  #uni20AF	DRACHMA SIGN
        chars.append(0x20B0)  #uni20B0	GERMAN PENNY SIGN
        chars.append(0x20B1)  #uni20B1	PESO SIGN
        chars.append(0x20B2)  #uni20B2	GUARANI SIGN
        chars.append(0x20B3)  #uni20B3	AUSTRAL SIGN
        chars.append(0x20B4)  #uni20B4	HRYVNIA SIGN
        chars.append(0x20B5)  #uni20B5	CEDI SIGN
        chars.append(0x20B6)  #uni20B6	LIVRE TOURNOIS SIGN
        chars.append(0x20B7)  #uni20B7	SPESMILO SIGN
        chars.append(0x20B8)  #uni20B8	TENGE SIGN
        chars.append(0x20B9)  #uni20B9	????
        chars.append(0x20BA)  #uni20BA	????
        chars.append(0x1F01F)  #glyph04609	MAHJONG TILE SEVEN OF CIRCLES
        chars.append(0x20BC)  #uni20BC	????
        chars.append(0x20BD)  #uni20BD	????
        chars.append(0x20BE)  #uni20BE	????
        chars.append(0x1F020)  #glyph04610	MAHJONG TILE EIGHT OF CIRCLES
        chars.append(0x1F093)  #glyph04721	DOMINO TILE VERTICAL-06-06
        chars.append(0x1D021)  #glyph02974	BYZANTINE MUSICAL SYMBOL VAREIAI ARCHAION
        chars.append(0x101E4)  #glyph02915	PHAISTOS DISC SIGN COMB
        chars.append(0x20D0)  #uni20D0	COMBINING LEFT HARPOON ABOVE
        chars.append(0x20D1)  #uni20D1	COMBINING RIGHT HARPOON ABOVE
        chars.append(0x20D2)  #uni20D2	COMBINING LONG VERTICAL LINE OVERLAY
        chars.append(0x20D3)  #uni20D3	COMBINING SHORT VERTICAL LINE OVERLAY
        chars.append(0x20D4)  #uni20D4	COMBINING ANTICLOCKWISE ARROW ABOVE
        chars.append(0x20D5)  #uni20D5	COMBINING CLOCKWISE ARROW ABOVE
        chars.append(0x20D6)  #uni20D6	COMBINING LEFT ARROW ABOVE
        chars.append(0x20D7)  #uni20D7	COMBINING RIGHT ARROW ABOVE
        chars.append(0x20D8)  #uni20D8	COMBINING RING OVERLAY
        chars.append(0x20D9)  #uni20D9	COMBINING CLOCKWISE RING OVERLAY
        chars.append(0x20DA)  #uni20DA	COMBINING ANTICLOCKWISE RING OVERLAY
        chars.append(0x20DB)  #uni20DB	COMBINING THREE DOTS ABOVE
        chars.append(0x20DC)  #uni20DC	COMBINING FOUR DOTS ABOVE
        chars.append(0x20DD)  #uni20DD	COMBINING ENCLOSING CIRCLE
        chars.append(0x20DE)  #uni20DE	COMBINING ENCLOSING SQUARE
        chars.append(0x20DF)  #uni20DF	COMBINING ENCLOSING DIAMOND
        chars.append(0x20E0)  #uni20E0	COMBINING ENCLOSING CIRCLE BACKSLASH
        chars.append(0x20E1)  #uni20E1	COMBINING LEFT RIGHT ARROW ABOVE
        chars.append(0x20E2)  #uni20E2	COMBINING ENCLOSING SCREEN
        chars.append(0x20E3)  #uni20E3	COMBINING ENCLOSING KEYCAP
        chars.append(0x20E4)  #uni20E4	COMBINING ENCLOSING UPWARD POINTING TRIANGLE
        chars.append(0x20E5)  #uni20E5	COMBINING REVERSE SOLIDUS OVERLAY
        chars.append(0x20E6)  #uni20E6	COMBINING DOUBLE VERTICAL STROKE OVERLAY
        chars.append(0x20E7)  #uni20E7	COMBINING ANNUITY SYMBOL
        chars.append(0x20E8)  #uni20E8	COMBINING TRIPLE UNDERDOT
        chars.append(0x20E9)  #uni20E9	COMBINING WIDE BRIDGE ABOVE
        chars.append(0x20EA)  #uni20EA	COMBINING LEFTWARDS ARROW OVERLAY
        chars.append(0x20EB)  #uni20EB	COMBINING LONG DOUBLE SOLIDUS OVERLAY
        chars.append(0x20EC)  #uni20EC	COMBINING RIGHTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x20ED)  #uni20ED	COMBINING LEFTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x20EE)  #uni20EE	COMBINING LEFT ARROW BELOW
        chars.append(0x20EF)  #uni20EF	COMBINING RIGHT ARROW BELOW
        chars.append(0x20F0)  #uni20F0	COMBINING ASTERISK ABOVE
        chars.append(0x1F028)  #glyph04618	MAHJONG TILE AUTUMN
        chars.append(0x1F029)  #glyph04619	MAHJONG TILE WINTER
        chars.append(0x1F02A)  #glyph04620	MAHJONG TILE JOKER
        chars.append(0x1F131)  #glyph04824	SQUARED LATIN CAPITAL LETTER B
        chars.append(0x2100)  #uni2100	ACCOUNT OF
        chars.append(0x2101)  #uni2101	ADDRESSED TO THE SUBJECT
        chars.append(0x2102)  #uni2102	DOUBLE-STRUCK CAPITAL C
        chars.append(0x2103)  #uni2103	DEGREE CELSIUS
        chars.append(0x2104)  #uni2104	CENTRE LINE SYMBOL
        chars.append(0x2105)  #uni2105	CARE OF
        chars.append(0x2106)  #uni2106	CADA UNA
        chars.append(0x2107)  #uni2107	EULER CONSTANT
        chars.append(0x2108)  #uni2108	SCRUPLE
        chars.append(0x2109)  #uni2109	DEGREE FAHRENHEIT
        chars.append(0x210A)  #uni210A	SCRIPT SMALL G
        chars.append(0x210B)  #uni210B	SCRIPT CAPITAL H
        chars.append(0x210C)  #uni210C	BLACK-LETTER CAPITAL H
        chars.append(0x210D)  #uni210D	DOUBLE-STRUCK CAPITAL H
        chars.append(0x210E)  #uni210E	PLANCK CONSTANT
        chars.append(0x210F)  #uni210F	PLANCK CONSTANT OVER TWO PI
        chars.append(0x2110)  #uni2110	SCRIPT CAPITAL I
        chars.append(0x2111)  #Ifraktur	BLACK-LETTER CAPITAL I
        chars.append(0x2112)  #uni2112	SCRIPT CAPITAL L
        chars.append(0x2113)  #uni2113	SCRIPT SMALL L
        chars.append(0x2114)  #uni2114	L B BAR SYMBOL
        chars.append(0x2115)  #uni2115	DOUBLE-STRUCK CAPITAL N
        chars.append(0x2116)  #uni2116	NUMERO SIGN
        chars.append(0x2117)  #uni2117	SOUND RECORDING COPYRIGHT
        chars.append(0x2118)  #weierstrass	SCRIPT CAPITAL P
        chars.append(0x2119)  #uni2119	DOUBLE-STRUCK CAPITAL P
        chars.append(0x211A)  #uni211A	DOUBLE-STRUCK CAPITAL Q
        chars.append(0x211B)  #uni211B	SCRIPT CAPITAL R
        chars.append(0x211C)  #Rfraktur	BLACK-LETTER CAPITAL R
        chars.append(0x211D)  #uni211D	DOUBLE-STRUCK CAPITAL R
        chars.append(0x211E)  #prescription	PRESCRIPTION TAKE
        chars.append(0x211F)  #uni211F	RESPONSE
        chars.append(0x2120)  #uni2120	SERVICE MARK
        chars.append(0x2121)  #uni2121	TELEPHONE SIGN
        chars.append(0x2122)  #trademark	TRADE MARK SIGN
        chars.append(0x2123)  #uni2123	VERSICLE
        chars.append(0x2124)  #uni2124	DOUBLE-STRUCK CAPITAL Z
        chars.append(0x2125)  #uni2125	OUNCE SIGN
        chars.append(0x2126)  #Omega	OHM SIGN
        chars.append(0x2127)  #uni2127	INVERTED OHM SIGN
        chars.append(0x2128)  #uni2128	BLACK-LETTER CAPITAL Z
        chars.append(0x2129)  #uni2129	TURNED GREEK SMALL LETTER IOTA
        chars.append(0x212A)  #uni212A	KELVIN SIGN
        chars.append(0x212B)  #uni212B	ANGSTROM SIGN
        chars.append(0x212C)  #uni212C	SCRIPT CAPITAL B
        chars.append(0x212D)  #uni212D	BLACK-LETTER CAPITAL C
        chars.append(0x212E)  #estimated	ESTIMATED SYMBOL
        chars.append(0x212F)  #uni212F	SCRIPT SMALL E
        chars.append(0x2130)  #uni2130	SCRIPT CAPITAL E
        chars.append(0x2131)  #uni2131	SCRIPT CAPITAL F
        chars.append(0x2132)  #uni2132	TURNED CAPITAL F
        chars.append(0x2133)  #uni2133	SCRIPT CAPITAL M
        chars.append(0x2134)  #uni2134	SCRIPT SMALL O
        chars.append(0x2135)  #aleph	ALEF SYMBOL
        chars.append(0x2136)  #uni2136	BET SYMBOL
        chars.append(0x2137)  #uni2137	GIMEL SYMBOL
        chars.append(0x2138)  #uni2138	DALET SYMBOL
        chars.append(0x2139)  #uni2139	INFORMATION SOURCE
        chars.append(0x213A)  #uni213A	ROTATED CAPITAL Q
        chars.append(0x213B)  #uni213B	FACSIMILE SIGN
        chars.append(0x213C)  #uni213C	DOUBLE-STRUCK SMALL PI
        chars.append(0x213D)  #uni213D	DOUBLE-STRUCK SMALL GAMMA
        chars.append(0x213E)  #uni213E	DOUBLE-STRUCK CAPITAL GAMMA
        chars.append(0x213F)  #uni213F	DOUBLE-STRUCK CAPITAL PI
        chars.append(0x2140)  #uni2140	DOUBLE-STRUCK N-ARY SUMMATION
        chars.append(0x2141)  #uni2141	TURNED SANS-SERIF CAPITAL G
        chars.append(0x2142)  #uni2142	TURNED SANS-SERIF CAPITAL L
        chars.append(0x2143)  #uni2143	REVERSED SANS-SERIF CAPITAL L
        chars.append(0x2144)  #uni2144	TURNED SANS-SERIF CAPITAL Y
        chars.append(0x2145)  #uni2145	DOUBLE-STRUCK ITALIC CAPITAL D
        chars.append(0x2146)  #uni2146	DOUBLE-STRUCK ITALIC SMALL D
        chars.append(0x2147)  #uni2147	DOUBLE-STRUCK ITALIC SMALL E
        chars.append(0x2148)  #uni2148	DOUBLE-STRUCK ITALIC SMALL I
        chars.append(0x2149)  #uni2149	DOUBLE-STRUCK ITALIC SMALL J
        chars.append(0x214A)  #uni214A	PROPERTY LINE
        chars.append(0x214B)  #uni214B	TURNED AMPERSAND
        chars.append(0x214C)  #uni214C	PER SIGN
        chars.append(0x214D)  #uni214D	AKTIESELSKAB
        chars.append(0x214E)  #uni214E	TURNED SMALL F
        chars.append(0x214F)  #uni214F	SYMBOL FOR SAMARITAN SOURCE
        chars.append(0x10150)  #glyph02824	GREEK ACROPHONIC ATTIC TEN STATERS
        chars.append(0x10151)  #glyph02825	GREEK ACROPHONIC ATTIC FIFTY STATERS
        chars.append(0x10152)  #glyph02826	GREEK ACROPHONIC ATTIC ONE HUNDRED STATERS
        chars.append(0x10153)  #glyph02827	GREEK ACROPHONIC ATTIC FIVE HUNDRED STATERS
        chars.append(0x10154)  #glyph02828	GREEK ACROPHONIC ATTIC ONE THOUSAND STATERS
        chars.append(0x10155)  #glyph02829	GREEK ACROPHONIC ATTIC TEN THOUSAND STATERS
        chars.append(0x10156)  #glyph02830	GREEK ACROPHONIC ATTIC FIFTY THOUSAND STATERS
        chars.append(0x10157)  #glyph02831	GREEK ACROPHONIC ATTIC TEN MNAS
        chars.append(0x10158)  #glyph02832	GREEK ACROPHONIC HERAEUM ONE PLETHRON
        chars.append(0x10159)  #glyph02833	GREEK ACROPHONIC THESPIAN ONE
        chars.append(0x1015A)  #glyph02834	GREEK ACROPHONIC HERMIONIAN ONE
        chars.append(0x1015B)  #glyph02835	GREEK ACROPHONIC EPIDAUREAN TWO
        chars.append(0x1015C)  #glyph02836	GREEK ACROPHONIC THESPIAN TWO
        chars.append(0x1015D)  #glyph02837	GREEK ACROPHONIC CYRENAIC TWO DRACHMAS
        chars.append(0x1015E)  #glyph02838	GREEK ACROPHONIC EPIDAUREAN TWO DRACHMAS
        chars.append(0x1015F)  #glyph02839	GREEK ACROPHONIC TROEZENIAN FIVE
        chars.append(0x10160)  #glyph02840	GREEK ACROPHONIC TROEZENIAN TEN
        chars.append(0x10161)  #glyph02841	GREEK ACROPHONIC TROEZENIAN TEN ALTERNATE FORM
        chars.append(0x10162)  #glyph02842	GREEK ACROPHONIC HERMIONIAN TEN
        chars.append(0x10163)  #glyph02843	GREEK ACROPHONIC MESSENIAN TEN
        chars.append(0x10164)  #glyph02844	GREEK ACROPHONIC THESPIAN TEN
        chars.append(0x10165)  #glyph02845	GREEK ACROPHONIC THESPIAN THIRTY
        chars.append(0x10166)  #glyph02846	GREEK ACROPHONIC TROEZENIAN FIFTY
        chars.append(0x10167)  #glyph02847	GREEK ACROPHONIC TROEZENIAN FIFTY ALTERNATE FORM
        chars.append(0x10168)  #glyph02848	GREEK ACROPHONIC HERMIONIAN FIFTY
        chars.append(0x10169)  #glyph02849	GREEK ACROPHONIC THESPIAN FIFTY
        chars.append(0x1016A)  #glyph02850	GREEK ACROPHONIC THESPIAN ONE HUNDRED
        chars.append(0x1016B)  #glyph02851	GREEK ACROPHONIC THESPIAN THREE HUNDRED
        chars.append(0x1016C)  #glyph02852	GREEK ACROPHONIC EPIDAUREAN FIVE HUNDRED
        chars.append(0x1016D)  #glyph02853	GREEK ACROPHONIC TROEZENIAN FIVE HUNDRED
        chars.append(0x1016E)  #glyph02854	GREEK ACROPHONIC THESPIAN FIVE HUNDRED
        chars.append(0x1016F)  #glyph02855	GREEK ACROPHONIC CARYSTIAN FIVE HUNDRED
        chars.append(0x10170)  #glyph02856	GREEK ACROPHONIC NAXIAN FIVE HUNDRED
        chars.append(0x10171)  #glyph02857	GREEK ACROPHONIC THESPIAN ONE THOUSAND
        chars.append(0x10172)  #glyph02858	GREEK ACROPHONIC THESPIAN FIVE THOUSAND
        chars.append(0x10173)  #glyph02859	GREEK ACROPHONIC DELPHIC FIVE MNAS
        chars.append(0x10174)  #glyph02860	GREEK ACROPHONIC STRATIAN FIFTY MNAS
        chars.append(0x10175)  #glyph02861	GREEK ONE HALF SIGN
        chars.append(0x10176)  #glyph02862	GREEK ONE HALF SIGN ALTERNATE FORM
        chars.append(0x10177)  #glyph02863	GREEK TWO THIRDS SIGN
        chars.append(0x10178)  #glyph02864	GREEK THREE QUARTERS SIGN
        chars.append(0x10179)  #glyph02865	GREEK YEAR SIGN
        chars.append(0x1017A)  #glyph02866	GREEK TALENT SIGN
        chars.append(0x1017B)  #glyph02867	GREEK DRACHMA SIGN
        chars.append(0x1017C)  #glyph02868	GREEK OBOL SIGN
        chars.append(0x1017D)  #glyph02869	GREEK TWO OBOLS SIGN
        chars.append(0x1017E)  #glyph02870	GREEK THREE OBOLS SIGN
        chars.append(0x1017F)  #glyph02871	GREEK FOUR OBOLS SIGN
        chars.append(0x10180)  #glyph02872	GREEK FIVE OBOLS SIGN
        chars.append(0x10181)  #glyph02873	GREEK METRETES SIGN
        chars.append(0x10182)  #glyph02874	GREEK KYATHOS BASE SIGN
        chars.append(0x10183)  #glyph02875	GREEK LITRA SIGN
        chars.append(0x10184)  #glyph02876	GREEK OUNKIA SIGN
        chars.append(0x10185)  #glyph02877	GREEK XESTES SIGN
        chars.append(0x10186)  #glyph02878	GREEK ARTABE SIGN
        chars.append(0x10187)  #glyph02879	GREEK AROURA SIGN
        chars.append(0x10188)  #glyph02880	GREEK GRAMMA SIGN
        chars.append(0x10189)  #glyph02881	GREEK TRYBLION BASE SIGN
        chars.append(0x1018A)  #glyph02882	GREEK ZERO SIGN
        chars.append(0x1F042)  #glyph04640	DOMINO TILE HORIZONTAL-02-03
        chars.append(0x2190)  #arrowleft	LEFTWARDS ARROW
        chars.append(0x2191)  #arrowup	UPWARDS ARROW
        chars.append(0x2192)  #arrowright	RIGHTWARDS ARROW
        chars.append(0x2193)  #arrowdown	DOWNWARDS ARROW
        chars.append(0x2194)  #arrowboth	LEFT RIGHT ARROW
        chars.append(0x2195)  #arrowupdn	UP DOWN ARROW
        chars.append(0x2196)  #uni2196	NORTH WEST ARROW
        chars.append(0x2197)  #uni2197	NORTH EAST ARROW
        chars.append(0x2198)  #uni2198	SOUTH EAST ARROW
        chars.append(0x2199)  #uni2199	SOUTH WEST ARROW
        chars.append(0x219A)  #uni219A	LEFTWARDS ARROW WITH STROKE
        chars.append(0x219B)  #uni219B	RIGHTWARDS ARROW WITH STROKE
        chars.append(0x219C)  #uni219C	LEFTWARDS WAVE ARROW
        chars.append(0x219D)  #uni219D	RIGHTWARDS WAVE ARROW
        chars.append(0x219E)  #uni219E	LEFTWARDS TWO HEADED ARROW
        chars.append(0x219F)  #uni219F	UPWARDS TWO HEADED ARROW
        chars.append(0x21A0)  #uni21A0	RIGHTWARDS TWO HEADED ARROW
        chars.append(0x21A1)  #uni21A1	DOWNWARDS TWO HEADED ARROW
        chars.append(0x21A2)  #uni21A2	LEFTWARDS ARROW WITH TAIL
        chars.append(0x21A3)  #uni21A3	RIGHTWARDS ARROW WITH TAIL
        chars.append(0x21A4)  #uni21A4	LEFTWARDS ARROW FROM BAR
        chars.append(0x21A5)  #uni21A5	UPWARDS ARROW FROM BAR
        chars.append(0x21A6)  #uni21A6	RIGHTWARDS ARROW FROM BAR
        chars.append(0x21A7)  #uni21A7	DOWNWARDS ARROW FROM BAR
        chars.append(0x21A8)  #arrowupdnbse	UP DOWN ARROW WITH BASE
        chars.append(0x21A9)  #uni21A9	LEFTWARDS ARROW WITH HOOK
        chars.append(0x21AA)  #uni21AA	RIGHTWARDS ARROW WITH HOOK
        chars.append(0x21AB)  #uni21AB	LEFTWARDS ARROW WITH LOOP
        chars.append(0x21AC)  #uni21AC	RIGHTWARDS ARROW WITH LOOP
        chars.append(0x21AD)  #uni21AD	LEFT RIGHT WAVE ARROW
        chars.append(0x21AE)  #uni21AE	LEFT RIGHT ARROW WITH STROKE
        chars.append(0x21AF)  #uni21AF	DOWNWARDS ZIGZAG ARROW
        chars.append(0x21B0)  #uni21B0	UPWARDS ARROW WITH TIP LEFTWARDS
        chars.append(0x21B1)  #uni21B1	UPWARDS ARROW WITH TIP RIGHTWARDS
        chars.append(0x21B2)  #uni21B2	DOWNWARDS ARROW WITH TIP LEFTWARDS
        chars.append(0x21B3)  #uni21B3	DOWNWARDS ARROW WITH TIP RIGHTWARDS
        chars.append(0x21B4)  #uni21B4	RIGHTWARDS ARROW WITH CORNER DOWNWARDS
        chars.append(0x21B5)  #carriagereturn	DOWNWARDS ARROW WITH CORNER LEFTWARDS
        chars.append(0x21B6)  #uni21B6	ANTICLOCKWISE TOP SEMICIRCLE ARROW
        chars.append(0x21B7)  #uni21B7	CLOCKWISE TOP SEMICIRCLE ARROW
        chars.append(0x21B8)  #uni21B8	NORTH WEST ARROW TO LONG BAR
        chars.append(0x21B9)  #uni21B9	LEFTWARDS ARROW TO BAR OVER RIGHTWARDS ARROW TO BAR
        chars.append(0x21BA)  #uni21BA	ANTICLOCKWISE OPEN CIRCLE ARROW
        chars.append(0x21BB)  #uni21BB	CLOCKWISE OPEN CIRCLE ARROW
        chars.append(0x21BC)  #uni21BC	LEFTWARDS HARPOON WITH BARB UPWARDS
        chars.append(0x21BD)  #uni21BD	LEFTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x21BE)  #uni21BE	UPWARDS HARPOON WITH BARB RIGHTWARDS
        chars.append(0x21BF)  #uni21BF	UPWARDS HARPOON WITH BARB LEFTWARDS
        chars.append(0x21C0)  #uni21C0	RIGHTWARDS HARPOON WITH BARB UPWARDS
        chars.append(0x21C1)  #uni21C1	RIGHTWARDS HARPOON WITH BARB DOWNWARDS
        chars.append(0x21C2)  #uni21C2	DOWNWARDS HARPOON WITH BARB RIGHTWARDS
        chars.append(0x21C3)  #uni21C3	DOWNWARDS HARPOON WITH BARB LEFTWARDS
        chars.append(0x21C4)  #uni21C4	RIGHTWARDS ARROW OVER LEFTWARDS ARROW
        chars.append(0x21C5)  #uni21C5	UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW
        chars.append(0x21C6)  #uni21C6	LEFTWARDS ARROW OVER RIGHTWARDS ARROW
        chars.append(0x21C7)  #uni21C7	LEFTWARDS PAIRED ARROWS
        chars.append(0x21C8)  #uni21C8	UPWARDS PAIRED ARROWS
        chars.append(0x21C9)  #uni21C9	RIGHTWARDS PAIRED ARROWS
        chars.append(0x21CA)  #uni21CA	DOWNWARDS PAIRED ARROWS
        chars.append(0x21CB)  #uni21CB	LEFTWARDS HARPOON OVER RIGHTWARDS HARPOON
        chars.append(0x21CC)  #uni21CC	RIGHTWARDS HARPOON OVER LEFTWARDS HARPOON
        chars.append(0x21CD)  #uni21CD	LEFTWARDS DOUBLE ARROW WITH STROKE
        chars.append(0x21CE)  #uni21CE	LEFT RIGHT DOUBLE ARROW WITH STROKE
        chars.append(0x21CF)  #uni21CF	RIGHTWARDS DOUBLE ARROW WITH STROKE
        chars.append(0x21D0)  #arrowdblleft	LEFTWARDS DOUBLE ARROW
        chars.append(0x21D1)  #arrowdblup	UPWARDS DOUBLE ARROW
        chars.append(0x21D2)  #arrowdblright	RIGHTWARDS DOUBLE ARROW
        chars.append(0x21D3)  #arrowdbldown	DOWNWARDS DOUBLE ARROW
        chars.append(0x21D4)  #arrowdblboth	LEFT RIGHT DOUBLE ARROW
        chars.append(0x21D5)  #uni21D5	UP DOWN DOUBLE ARROW
        chars.append(0x21D6)  #uni21D6	NORTH WEST DOUBLE ARROW
        chars.append(0x21D7)  #uni21D7	NORTH EAST DOUBLE ARROW
        chars.append(0x21D8)  #uni21D8	SOUTH EAST DOUBLE ARROW
        chars.append(0x21D9)  #uni21D9	SOUTH WEST DOUBLE ARROW
        chars.append(0x21DA)  #uni21DA	LEFTWARDS TRIPLE ARROW
        chars.append(0x21DB)  #uni21DB	RIGHTWARDS TRIPLE ARROW
        chars.append(0x21DC)  #uni21DC	LEFTWARDS SQUIGGLE ARROW
        chars.append(0x21DD)  #uni21DD	RIGHTWARDS SQUIGGLE ARROW
        chars.append(0x21DE)  #uni21DE	UPWARDS ARROW WITH DOUBLE STROKE
        chars.append(0x21DF)  #uni21DF	DOWNWARDS ARROW WITH DOUBLE STROKE
        chars.append(0x21E0)  #uni21E0	LEFTWARDS DASHED ARROW
        chars.append(0x21E1)  #uni21E1	UPWARDS DASHED ARROW
        chars.append(0x21E2)  #uni21E2	RIGHTWARDS DASHED ARROW
        chars.append(0x21E3)  #uni21E3	DOWNWARDS DASHED ARROW
        chars.append(0x21E4)  #uni21E4	LEFTWARDS ARROW TO BAR
        chars.append(0x21E5)  #uni21E5	RIGHTWARDS ARROW TO BAR
        chars.append(0x21E6)  #uni21E6	LEFTWARDS WHITE ARROW
        chars.append(0x21E7)  #uni21E7	UPWARDS WHITE ARROW
        chars.append(0x21E8)  #uni21E8	RIGHTWARDS WHITE ARROW
        chars.append(0x21E9)  #uni21E9	DOWNWARDS WHITE ARROW
        chars.append(0x21EA)  #uni21EA	UPWARDS WHITE ARROW FROM BAR
        chars.append(0x21EB)  #uni21EB	UPWARDS WHITE ARROW ON PEDESTAL
        chars.append(0x21EC)  #uni21EC	UPWARDS WHITE ARROW ON PEDESTAL WITH HORIZONTAL BAR
        chars.append(0x21ED)  #uni21ED	UPWARDS WHITE ARROW ON PEDESTAL WITH VERTICAL BAR
        chars.append(0x21EE)  #uni21EE	UPWARDS WHITE DOUBLE ARROW
        chars.append(0x21EF)  #uni21EF	UPWARDS WHITE DOUBLE ARROW ON PEDESTAL
        chars.append(0x21F0)  #uni21F0	RIGHTWARDS WHITE ARROW FROM WALL
        chars.append(0x21F1)  #uni21F1	NORTH WEST ARROW TO CORNER
        chars.append(0x21F2)  #uni21F2	SOUTH EAST ARROW TO CORNER
        chars.append(0x21F3)  #uni21F3	UP DOWN WHITE ARROW
        chars.append(0x21F4)  #uni21F4	RIGHT ARROW WITH SMALL CIRCLE
        chars.append(0x21F5)  #uni21F5	DOWNWARDS ARROW LEFTWARDS OF UPWARDS ARROW
        chars.append(0x21F6)  #uni21F6	THREE RIGHTWARDS ARROWS
        chars.append(0x21F7)  #uni21F7	LEFTWARDS ARROW WITH VERTICAL STROKE
        chars.append(0x21F8)  #uni21F8	RIGHTWARDS ARROW WITH VERTICAL STROKE
        chars.append(0x21F9)  #uni21F9	LEFT RIGHT ARROW WITH VERTICAL STROKE
        chars.append(0x21FA)  #uni21FA	LEFTWARDS ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x21FB)  #uni21FB	RIGHTWARDS ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x21FC)  #uni21FC	LEFT RIGHT ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x21FD)  #uni21FD	LEFTWARDS OPEN-HEADED ARROW
        chars.append(0x21FE)  #uni21FE	RIGHTWARDS OPEN-HEADED ARROW
        chars.append(0x21FF)  #uni21FF	LEFT RIGHT OPEN-HEADED ARROW
        chars.append(0x2200)  #universal	FOR ALL
        chars.append(0x2201)  #uni2201	COMPLEMENT
        chars.append(0x2202)  #partialdiff	PARTIAL DIFFERENTIAL
        chars.append(0x2203)  #existential	THERE EXISTS
        chars.append(0x2204)  #uni2204	THERE DOES NOT EXIST
        chars.append(0x2205)  #emptyset	EMPTY SET
        chars.append(0x2206)  #Delta	INCREMENT
        chars.append(0x2207)  #gradient	NABLA
        chars.append(0x2208)  #element	ELEMENT OF
        chars.append(0x2209)  #notelement	NOT AN ELEMENT OF
        chars.append(0x220A)  #uni220A	SMALL ELEMENT OF
        chars.append(0x220B)  #suchthat	CONTAINS AS MEMBER
        chars.append(0x220C)  #uni220C	DOES NOT CONTAIN AS MEMBER
        chars.append(0x220D)  #uni220D	SMALL CONTAINS AS MEMBER
        chars.append(0x220E)  #uni220E	END OF PROOF
        chars.append(0x220F)  #product	N-ARY PRODUCT
        chars.append(0x2210)  #uni2210	N-ARY COPRODUCT
        chars.append(0x2211)  #summation	N-ARY SUMMATION
        chars.append(0x2212)  #minus	MINUS SIGN
        chars.append(0x2213)  #uni2213	MINUS-OR-PLUS SIGN
        chars.append(0x2214)  #uni2214	DOT PLUS
        chars.append(0x2215)  #uni0338	DIVISION SLASH
        chars.append(0x2216)  #uni2216	SET MINUS
        chars.append(0x2217)  #asteriskmath	ASTERISK OPERATOR
        chars.append(0x2218)  #uni2218	RING OPERATOR
        chars.append(0x2219)  #uni2219	BULLET OPERATOR
        chars.append(0x221A)  #radical	SQUARE ROOT
        chars.append(0x221B)  #uni221B	CUBE ROOT
        chars.append(0x221C)  #uni221C	FOURTH ROOT
        chars.append(0x221D)  #proportional	PROPORTIONAL TO
        chars.append(0x221E)  #infinity	INFINITY
        chars.append(0x221F)  #orthogonal	RIGHT ANGLE
        chars.append(0x2220)  #angle	ANGLE
        chars.append(0x2221)  #uni2221	MEASURED ANGLE
        chars.append(0x2222)  #uni2222	SPHERICAL ANGLE
        chars.append(0x2223)  #uni2223	DIVIDES
        chars.append(0x2224)  #uni2224	DOES NOT DIVIDE
        chars.append(0x2225)  #uni2225	PARALLEL TO
        chars.append(0x2226)  #uni2226	NOT PARALLEL TO
        chars.append(0x2227)  #logicaland	LOGICAL AND
        chars.append(0x2228)  #logicalor	LOGICAL OR
        chars.append(0x2229)  #intersection	INTERSECTION
        chars.append(0x222A)  #union	UNION
        chars.append(0x222B)  #integral	INTEGRAL
        chars.append(0x222C)  #uni222C	DOUBLE INTEGRAL
        chars.append(0x222D)  #uni222D	TRIPLE INTEGRAL
        chars.append(0x222E)  #uni222E	CONTOUR INTEGRAL
        chars.append(0x222F)  #uni222F	SURFACE INTEGRAL
        chars.append(0x2230)  #uni2230	VOLUME INTEGRAL
        chars.append(0x2231)  #uni2231	CLOCKWISE INTEGRAL
        chars.append(0x2232)  #uni2232	CLOCKWISE CONTOUR INTEGRAL
        chars.append(0x2233)  #uni2233	ANTICLOCKWISE CONTOUR INTEGRAL
        chars.append(0x2234)  #therefore	THEREFORE
        chars.append(0x2235)  #uni2235	BECAUSE
        chars.append(0x2236)  #uni2236	RATIO
        chars.append(0x2237)  #uni2237	PROPORTION
        chars.append(0x2238)  #uni2238	DOT MINUS
        chars.append(0x2239)  #uni2239	EXCESS
        chars.append(0x223A)  #uni223A	GEOMETRIC PROPORTION
        chars.append(0x223B)  #uni223B	HOMOTHETIC
        chars.append(0x223C)  #similar	TILDE OPERATOR
        chars.append(0x223D)  #uni223D	REVERSED TILDE
        chars.append(0x223E)  #uni223E	INVERTED LAZY S
        chars.append(0x223F)  #uni223F	SINE WAVE
        chars.append(0x2240)  #uni2240	WREATH PRODUCT
        chars.append(0x2241)  #uni2241	NOT TILDE
        chars.append(0x2242)  #uni2242	MINUS TILDE
        chars.append(0x2243)  #uni2243	ASYMPTOTICALLY EQUAL TO
        chars.append(0x2244)  #uni2244	NOT ASYMPTOTICALLY EQUAL TO
        chars.append(0x2245)  #congruent	APPROXIMATELY EQUAL TO
        chars.append(0x2246)  #uni2246	APPROXIMATELY BUT NOT ACTUALLY EQUAL TO
        chars.append(0x2247)  #uni2247	NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO
        chars.append(0x2248)  #approxequal	ALMOST EQUAL TO
        chars.append(0x2249)  #uni2249	NOT ALMOST EQUAL TO
        chars.append(0x224A)  #uni224A	ALMOST EQUAL OR EQUAL TO
        chars.append(0x224B)  #uni224B	TRIPLE TILDE
        chars.append(0x224C)  #uni224C	ALL EQUAL TO
        chars.append(0x224D)  #uni224D	EQUIVALENT TO
        chars.append(0x224E)  #uni224E	GEOMETRICALLY EQUIVALENT TO
        chars.append(0x224F)  #uni224F	DIFFERENCE BETWEEN
        chars.append(0x2250)  #uni2250	APPROACHES THE LIMIT
        chars.append(0x2251)  #uni2251	GEOMETRICALLY EQUAL TO
        chars.append(0x2252)  #uni2252	APPROXIMATELY EQUAL TO OR THE IMAGE OF
        chars.append(0x2253)  #uni2253	IMAGE OF OR APPROXIMATELY EQUAL TO
        chars.append(0x2254)  #uni2254	COLON EQUALS
        chars.append(0x2255)  #uni2255	EQUALS COLON
        chars.append(0x2256)  #uni2256	RING IN EQUAL TO
        chars.append(0x2257)  #uni2257	RING EQUAL TO
        chars.append(0x2258)  #uni2258	CORRESPONDS TO
        chars.append(0x2259)  #uni2259	ESTIMATES
        chars.append(0x225A)  #uni225A	EQUIANGULAR TO
        chars.append(0x225B)  #uni225B	STAR EQUALS
        chars.append(0x225C)  #uni225C	DELTA EQUAL TO
        chars.append(0x225D)  #uni225D	EQUAL TO BY DEFINITION
        chars.append(0x225E)  #uni225E	MEASURED BY
        chars.append(0x225F)  #uni225F	QUESTIONED EQUAL TO
        chars.append(0x2260)  #notequal	NOT EQUAL TO
        chars.append(0x2261)  #equivalence	IDENTICAL TO
        chars.append(0x2262)  #uni2262	NOT IDENTICAL TO
        chars.append(0x2263)  #uni2263	STRICTLY EQUIVALENT TO
        chars.append(0x2264)  #lessequal	LESS-THAN OR EQUAL TO
        chars.append(0x2265)  #greaterequal	GREATER-THAN OR EQUAL TO
        chars.append(0x2266)  #uni2266	LESS-THAN OVER EQUAL TO
        chars.append(0x2267)  #uni2267	GREATER-THAN OVER EQUAL TO
        chars.append(0x2268)  #uni2268	LESS-THAN BUT NOT EQUAL TO
        chars.append(0x2269)  #uni2269	GREATER-THAN BUT NOT EQUAL TO
        chars.append(0x226A)  #uni226A	MUCH LESS-THAN
        chars.append(0x226B)  #uni226B	MUCH GREATER-THAN
        chars.append(0x226C)  #uni226C	BETWEEN
        chars.append(0x226D)  #uni226D	NOT EQUIVALENT TO
        chars.append(0x226E)  #uni226E	NOT LESS-THAN
        chars.append(0x226F)  #uni226F	NOT GREATER-THAN
        chars.append(0x2270)  #uni2270	NEITHER LESS-THAN NOR EQUAL TO
        chars.append(0x2271)  #uni2271	NEITHER GREATER-THAN NOR EQUAL TO
        chars.append(0x2272)  #uni2272	LESS-THAN OR EQUIVALENT TO
        chars.append(0x2273)  #uni2273	GREATER-THAN OR EQUIVALENT TO
        chars.append(0x2274)  #uni2274	NEITHER LESS-THAN NOR EQUIVALENT TO
        chars.append(0x2275)  #uni2275	NEITHER GREATER-THAN NOR EQUIVALENT TO
        chars.append(0x2276)  #uni2276	LESS-THAN OR GREATER-THAN
        chars.append(0x2277)  #uni2277	GREATER-THAN OR LESS-THAN
        chars.append(0x2278)  #uni2278	NEITHER LESS-THAN NOR GREATER-THAN
        chars.append(0x2279)  #uni2279	NEITHER GREATER-THAN NOR LESS-THAN
        chars.append(0x227A)  #uni227A	PRECEDES
        chars.append(0x227B)  #uni227B	SUCCEEDS
        chars.append(0x227C)  #uni227C	PRECEDES OR EQUAL TO
        chars.append(0x227D)  #uni227D	SUCCEEDS OR EQUAL TO
        chars.append(0x227E)  #uni227E	PRECEDES OR EQUIVALENT TO
        chars.append(0x227F)  #uni227F	SUCCEEDS OR EQUIVALENT TO
        chars.append(0x2280)  #uni2280	DOES NOT PRECEDE
        chars.append(0x2281)  #uni2281	DOES NOT SUCCEED
        chars.append(0x2282)  #propersubset	SUBSET OF
        chars.append(0x2283)  #propersuperset	SUPERSET OF
        chars.append(0x2284)  #notsubset	NOT A SUBSET OF
        chars.append(0x2285)  #uni2285	NOT A SUPERSET OF
        chars.append(0x2286)  #reflexsubset	SUBSET OF OR EQUAL TO
        chars.append(0x2287)  #reflexsuperset	SUPERSET OF OR EQUAL TO
        chars.append(0x2288)  #uni2288	NEITHER A SUBSET OF NOR EQUAL TO
        chars.append(0x2289)  #uni2289	NEITHER A SUPERSET OF NOR EQUAL TO
        chars.append(0x228A)  #uni228A	SUBSET OF WITH NOT EQUAL TO
        chars.append(0x228B)  #uni228B	SUPERSET OF WITH NOT EQUAL TO
        chars.append(0x228C)  #uni228C	MULTISET
        chars.append(0x228D)  #uni228D	MULTISET MULTIPLICATION
        chars.append(0x228E)  #uni228E	MULTISET UNION
        chars.append(0x228F)  #uni228F	SQUARE IMAGE OF
        chars.append(0x2290)  #uni2290	SQUARE ORIGINAL OF
        chars.append(0x2291)  #uni2291	SQUARE IMAGE OF OR EQUAL TO
        chars.append(0x2292)  #uni2292	SQUARE ORIGINAL OF OR EQUAL TO
        chars.append(0x2293)  #uni2293	SQUARE CAP
        chars.append(0x2294)  #uni2294	SQUARE CUP
        chars.append(0x2295)  #circleplus	CIRCLED PLUS
        chars.append(0x2296)  #uni2296	CIRCLED MINUS
        chars.append(0x2297)  #circlemultiply	CIRCLED TIMES
        chars.append(0x2298)  #uni2298	CIRCLED DIVISION SLASH
        chars.append(0x2299)  #uni2299	CIRCLED DOT OPERATOR
        chars.append(0x229A)  #uni229A	CIRCLED RING OPERATOR
        chars.append(0x229B)  #uni229B	CIRCLED ASTERISK OPERATOR
        chars.append(0x229C)  #uni229C	CIRCLED EQUALS
        chars.append(0x229D)  #uni229D	CIRCLED DASH
        chars.append(0x229E)  #uni229E	SQUARED PLUS
        chars.append(0x229F)  #uni229F	SQUARED MINUS
        chars.append(0x22A0)  #uni22A0	SQUARED TIMES
        chars.append(0x22A1)  #uni22A1	SQUARED DOT OPERATOR
        chars.append(0x22A2)  #uni22A2	RIGHT TACK
        chars.append(0x22A3)  #uni22A3	LEFT TACK
        chars.append(0x22A4)  #uni22A4	DOWN TACK
        chars.append(0x22A5)  #perpendicular	UP TACK
        chars.append(0x22A6)  #uni22A6	ASSERTION
        chars.append(0x22A7)  #uni22A7	MODELS
        chars.append(0x22A8)  #uni22A8	TRUE
        chars.append(0x22A9)  #uni22A9	FORCES
        chars.append(0x22AA)  #uni22AA	TRIPLE VERTICAL BAR RIGHT TURNSTILE
        chars.append(0x22AB)  #uni22AB	DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE
        chars.append(0x22AC)  #uni22AC	DOES NOT PROVE
        chars.append(0x22AD)  #uni22AD	NOT TRUE
        chars.append(0x22AE)  #uni22AE	DOES NOT FORCE
        chars.append(0x22AF)  #uni22AF	NEGATED DOUBLE VERTICAL BAR DOUBLE RIGHT TURNSTILE
        chars.append(0x22B0)  #uni22B0	PRECEDES UNDER RELATION
        chars.append(0x22B1)  #uni22B1	SUCCEEDS UNDER RELATION
        chars.append(0x22B2)  #uni22B2	NORMAL SUBGROUP OF
        chars.append(0x22B3)  #uni22B3	CONTAINS AS NORMAL SUBGROUP
        chars.append(0x22B4)  #uni22B4	NORMAL SUBGROUP OF OR EQUAL TO
        chars.append(0x22B5)  #uni22B5	CONTAINS AS NORMAL SUBGROUP OR EQUAL TO
        chars.append(0x22B6)  #uni22B6	ORIGINAL OF
        chars.append(0x22B7)  #uni22B7	IMAGE OF
        chars.append(0x22B8)  #uni22B8	MULTIMAP
        chars.append(0x22B9)  #uni22B9	HERMITIAN CONJUGATE MATRIX
        chars.append(0x22BA)  #uni22BA	INTERCALATE
        chars.append(0x22BB)  #uni22BB	XOR
        chars.append(0x22BC)  #uni22BC	NAND
        chars.append(0x22BD)  #uni22BD	NOR
        chars.append(0x22BE)  #uni22BE	RIGHT ANGLE WITH ARC
        chars.append(0x22BF)  #uni22BF	RIGHT TRIANGLE
        chars.append(0x22C0)  #uni22C0	N-ARY LOGICAL AND
        chars.append(0x22C1)  #uni22C1	N-ARY LOGICAL OR
        chars.append(0x22C2)  #uni22C2	N-ARY INTERSECTION
        chars.append(0x22C3)  #uni22C3	N-ARY UNION
        chars.append(0x22C4)  #uni22C4	DIAMOND OPERATOR
        chars.append(0x22C5)  #dotmath	DOT OPERATOR
        chars.append(0x22C6)  #uni22C6	STAR OPERATOR
        chars.append(0x22C7)  #uni22C7	DIVISION TIMES
        chars.append(0x22C8)  #uni22C8	BOWTIE
        chars.append(0x22C9)  #uni22C9	LEFT NORMAL FACTOR SEMIDIRECT PRODUCT
        chars.append(0x22CA)  #uni22CA	RIGHT NORMAL FACTOR SEMIDIRECT PRODUCT
        chars.append(0x22CB)  #uni22CB	LEFT SEMIDIRECT PRODUCT
        chars.append(0x22CC)  #uni22CC	RIGHT SEMIDIRECT PRODUCT
        chars.append(0x22CD)  #uni22CD	REVERSED TILDE EQUALS
        chars.append(0x22CE)  #uni22CE	CURLY LOGICAL OR
        chars.append(0x22CF)  #uni22CF	CURLY LOGICAL AND
        chars.append(0x22D0)  #uni22D0	DOUBLE SUBSET
        chars.append(0x22D1)  #uni22D1	DOUBLE SUPERSET
        chars.append(0x22D2)  #uni22D2	DOUBLE INTERSECTION
        chars.append(0x22D3)  #uni22D3	DOUBLE UNION
        chars.append(0x22D4)  #uni22D4	PITCHFORK
        chars.append(0x22D5)  #uni22D5	EQUAL AND PARALLEL TO
        chars.append(0x22D6)  #uni22D6	LESS-THAN WITH DOT
        chars.append(0x22D7)  #uni22D7	GREATER-THAN WITH DOT
        chars.append(0x22D8)  #uni22D8	VERY MUCH LESS-THAN
        chars.append(0x22D9)  #uni22D9	VERY MUCH GREATER-THAN
        chars.append(0x22DA)  #uni22DA	LESS-THAN EQUAL TO OR GREATER-THAN
        chars.append(0x22DB)  #uni22DB	GREATER-THAN EQUAL TO OR LESS-THAN
        chars.append(0x22DC)  #uni22DC	EQUAL TO OR LESS-THAN
        chars.append(0x22DD)  #uni22DD	EQUAL TO OR GREATER-THAN
        chars.append(0x22DE)  #uni22DE	EQUAL TO OR PRECEDES
        chars.append(0x22DF)  #uni22DF	EQUAL TO OR SUCCEEDS
        chars.append(0x22E0)  #uni22E0	DOES NOT PRECEDE OR EQUAL
        chars.append(0x22E1)  #uni22E1	DOES NOT SUCCEED OR EQUAL
        chars.append(0x22E2)  #uni22E2	NOT SQUARE IMAGE OF OR EQUAL TO
        chars.append(0x22E3)  #uni22E3	NOT SQUARE ORIGINAL OF OR EQUAL TO
        chars.append(0x22E4)  #uni22E4	SQUARE IMAGE OF OR NOT EQUAL TO
        chars.append(0x22E5)  #uni22E5	SQUARE ORIGINAL OF OR NOT EQUAL TO
        chars.append(0x22E6)  #uni22E6	LESS-THAN BUT NOT EQUIVALENT TO
        chars.append(0x22E7)  #uni22E7	GREATER-THAN BUT NOT EQUIVALENT TO
        chars.append(0x22E8)  #uni22E8	PRECEDES BUT NOT EQUIVALENT TO
        chars.append(0x22E9)  #uni22E9	SUCCEEDS BUT NOT EQUIVALENT TO
        chars.append(0x22EA)  #uni22EA	NOT NORMAL SUBGROUP OF
        chars.append(0x22EB)  #uni22EB	DOES NOT CONTAIN AS NORMAL SUBGROUP
        chars.append(0x22EC)  #uni22EC	NOT NORMAL SUBGROUP OF OR EQUAL TO
        chars.append(0x22ED)  #uni22ED	DOES NOT CONTAIN AS NORMAL SUBGROUP OR EQUAL
        chars.append(0x22EE)  #uni22EE	VERTICAL ELLIPSIS
        chars.append(0x22EF)  #uni22EF	MIDLINE HORIZONTAL ELLIPSIS
        chars.append(0x22F0)  #uni22F0	UP RIGHT DIAGONAL ELLIPSIS
        chars.append(0x22F1)  #uni22F1	DOWN RIGHT DIAGONAL ELLIPSIS
        chars.append(0x22F2)  #uni22F2	ELEMENT OF WITH LONG HORIZONTAL STROKE
        chars.append(0x22F3)  #uni22F3	ELEMENT OF WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22F4)  #uni22F4	SMALL ELEMENT OF WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22F5)  #uni22F5	ELEMENT OF WITH DOT ABOVE
        chars.append(0x22F6)  #uni22F6	ELEMENT OF WITH OVERBAR
        chars.append(0x22F7)  #uni22F7	SMALL ELEMENT OF WITH OVERBAR
        chars.append(0x22F8)  #uni22F8	ELEMENT OF WITH UNDERBAR
        chars.append(0x22F9)  #uni22F9	ELEMENT OF WITH TWO HORIZONTAL STROKES
        chars.append(0x22FA)  #uni22FA	CONTAINS WITH LONG HORIZONTAL STROKE
        chars.append(0x22FB)  #uni22FB	CONTAINS WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22FC)  #uni22FC	SMALL CONTAINS WITH VERTICAL BAR AT END OF HORIZONTAL STROKE
        chars.append(0x22FD)  #uni22FD	CONTAINS WITH OVERBAR
        chars.append(0x22FE)  #uni22FE	SMALL CONTAINS WITH OVERBAR
        chars.append(0x22FF)  #uni22FF	Z NOTATION BAG MEMBERSHIP
        chars.append(0x2300)  #uni2300	DIAMETER SIGN
        chars.append(0x2301)  #uni2301	ELECTRIC ARROW
        chars.append(0x2302)  #house	HOUSE
        chars.append(0x2303)  #uni2303	UP ARROWHEAD
        chars.append(0x2304)  #uni2304	DOWN ARROWHEAD
        chars.append(0x2305)  #uni2305	PROJECTIVE
        chars.append(0x2306)  #uni2306	PERSPECTIVE
        chars.append(0x2307)  #uni2307	WAVY LINE
        chars.append(0x2308)  #uni2308	LEFT CEILING
        chars.append(0x2309)  #uni2309	RIGHT CEILING
        chars.append(0x230A)  #uni230A	LEFT FLOOR
        chars.append(0x230B)  #uni230B	RIGHT FLOOR
        chars.append(0x230C)  #uni230C	BOTTOM RIGHT CROP
        chars.append(0x230D)  #uni230D	BOTTOM LEFT CROP
        chars.append(0x230E)  #uni230E	TOP RIGHT CROP
        chars.append(0x230F)  #uni230F	TOP LEFT CROP
        chars.append(0x2310)  #revlogicalnot	REVERSED NOT SIGN
        chars.append(0x2311)  #uni2311	SQUARE LOZENGE
        chars.append(0x2312)  #uni2312	ARC
        chars.append(0x2313)  #uni2313	SEGMENT
        chars.append(0x2314)  #uni2314	SECTOR
        chars.append(0x2315)  #uni2315	TELEPHONE RECORDER
        chars.append(0x2316)  #uni2316	POSITION INDICATOR
        chars.append(0x2317)  #uni2317	VIEWDATA SQUARE
        chars.append(0x2318)  #uni2318	PLACE OF INTEREST SIGN
        chars.append(0x2319)  #uni2319	TURNED NOT SIGN
        chars.append(0x231A)  #uni231A	WATCH
        chars.append(0x231B)  #uni231B	HOURGLASS
        chars.append(0x231C)  #uni231C	TOP LEFT CORNER
        chars.append(0x231D)  #uni231D	TOP RIGHT CORNER
        chars.append(0x231E)  #uni231E	BOTTOM LEFT CORNER
        chars.append(0x231F)  #uni231F	BOTTOM RIGHT CORNER
        chars.append(0x2320)  #integraltp	TOP HALF INTEGRAL
        chars.append(0x2321)  #integralbt	BOTTOM HALF INTEGRAL
        chars.append(0x2322)  #uni2322	FROWN
        chars.append(0x2323)  #uni2323	SMILE
        chars.append(0x2324)  #uni2324	UP ARROWHEAD BETWEEN TWO HORIZONTAL BARS
        chars.append(0x2325)  #uni2325	OPTION KEY
        chars.append(0x2326)  #uni2326	ERASE TO THE RIGHT
        chars.append(0x2327)  #uni2327	X IN A RECTANGLE BOX
        chars.append(0x2328)  #uni2328	KEYBOARD
        chars.append(0x2329)  #uni3008	LEFT-POINTING ANGLE BRACKET
        chars.append(0x232A)  #uni3009	RIGHT-POINTING ANGLE BRACKET
        chars.append(0x232B)  #uni232B	ERASE TO THE LEFT
        chars.append(0x232C)  #uni232C	BENZENE RING
        chars.append(0x232D)  #uni232D	CYLINDRICITY
        chars.append(0x232E)  #uni232E	ALL AROUND-PROFILE
        chars.append(0x232F)  #uni232F	SYMMETRY
        chars.append(0x2330)  #uni2330	TOTAL RUNOUT
        chars.append(0x2331)  #uni2331	DIMENSION ORIGIN
        chars.append(0x2332)  #uni2332	CONICAL TAPER
        chars.append(0x2333)  #uni2333	SLOPE
        chars.append(0x2334)  #uni2334	COUNTERBORE
        chars.append(0x2335)  #uni2335	COUNTERSINK
        chars.append(0x2336)  #uni2336	APL FUNCTIONAL SYMBOL I-BEAM
        chars.append(0x2337)  #uni2337	APL FUNCTIONAL SYMBOL SQUISH QUAD
        chars.append(0x0338)  #uni0338	COMBINING LONG SOLIDUS OVERLAY
        chars.append(0x2339)  #uni2339	APL FUNCTIONAL SYMBOL QUAD DIVIDE
        chars.append(0x233A)  #uni233A	APL FUNCTIONAL SYMBOL QUAD DIAMOND
        chars.append(0x233B)  #uni233B	APL FUNCTIONAL SYMBOL QUAD JOT
        chars.append(0x233C)  #uni233C	APL FUNCTIONAL SYMBOL QUAD CIRCLE
        chars.append(0x233D)  #uni233D	APL FUNCTIONAL SYMBOL CIRCLE STILE
        chars.append(0x233E)  #uni233E	APL FUNCTIONAL SYMBOL CIRCLE JOT
        chars.append(0x233F)  #uni233F	APL FUNCTIONAL SYMBOL SLASH BAR
        chars.append(0x2340)  #uni2340	APL FUNCTIONAL SYMBOL BACKSLASH BAR
        chars.append(0x2341)  #uni2341	APL FUNCTIONAL SYMBOL QUAD SLASH
        chars.append(0x2342)  #uni2342	APL FUNCTIONAL SYMBOL QUAD BACKSLASH
        chars.append(0x2343)  #uni2343	APL FUNCTIONAL SYMBOL QUAD LESS-THAN
        chars.append(0x2344)  #uni2344	APL FUNCTIONAL SYMBOL QUAD GREATER-THAN
        chars.append(0x2345)  #uni2345	APL FUNCTIONAL SYMBOL LEFTWARDS VANE
        chars.append(0x2346)  #uni2346	APL FUNCTIONAL SYMBOL RIGHTWARDS VANE
        chars.append(0x2347)  #uni2347	APL FUNCTIONAL SYMBOL QUAD LEFTWARDS ARROW
        chars.append(0x2348)  #uni2348	APL FUNCTIONAL SYMBOL QUAD RIGHTWARDS ARROW
        chars.append(0x2349)  #uni2349	APL FUNCTIONAL SYMBOL CIRCLE BACKSLASH
        chars.append(0x234A)  #uni234A	APL FUNCTIONAL SYMBOL DOWN TACK UNDERBAR
        chars.append(0x234B)  #uni234B	APL FUNCTIONAL SYMBOL DELTA STILE
        chars.append(0x234C)  #uni234C	APL FUNCTIONAL SYMBOL QUAD DOWN CARET
        chars.append(0x234D)  #uni234D	APL FUNCTIONAL SYMBOL QUAD DELTA
        chars.append(0x234E)  #uni234E	APL FUNCTIONAL SYMBOL DOWN TACK JOT
        chars.append(0x234F)  #uni234F	APL FUNCTIONAL SYMBOL UPWARDS VANE
        chars.append(0x2350)  #uni2350	APL FUNCTIONAL SYMBOL QUAD UPWARDS ARROW
        chars.append(0x2351)  #uni2351	APL FUNCTIONAL SYMBOL UP TACK OVERBAR
        chars.append(0x2352)  #uni2352	APL FUNCTIONAL SYMBOL DEL STILE
        chars.append(0x2353)  #uni2353	APL FUNCTIONAL SYMBOL QUAD UP CARET
        chars.append(0x2354)  #uni2354	APL FUNCTIONAL SYMBOL QUAD DEL
        chars.append(0x2355)  #uni2355	APL FUNCTIONAL SYMBOL UP TACK JOT
        chars.append(0x2356)  #uni2356	APL FUNCTIONAL SYMBOL DOWNWARDS VANE
        chars.append(0x2357)  #uni2357	APL FUNCTIONAL SYMBOL QUAD DOWNWARDS ARROW
        chars.append(0x2358)  #uni2358	APL FUNCTIONAL SYMBOL QUOTE UNDERBAR
        chars.append(0x2359)  #uni2359	APL FUNCTIONAL SYMBOL DELTA UNDERBAR
        chars.append(0x235A)  #uni235A	APL FUNCTIONAL SYMBOL DIAMOND UNDERBAR
        chars.append(0x235B)  #uni235B	APL FUNCTIONAL SYMBOL JOT UNDERBAR
        chars.append(0x235C)  #uni235C	APL FUNCTIONAL SYMBOL CIRCLE UNDERBAR
        chars.append(0x235D)  #uni235D	APL FUNCTIONAL SYMBOL UP SHOE JOT
        chars.append(0x235E)  #uni235E	APL FUNCTIONAL SYMBOL QUOTE QUAD
        chars.append(0x235F)  #uni235F	APL FUNCTIONAL SYMBOL CIRCLE STAR
        chars.append(0x2360)  #uni2360	APL FUNCTIONAL SYMBOL QUAD COLON
        chars.append(0x2361)  #uni2361	APL FUNCTIONAL SYMBOL UP TACK DIAERESIS
        chars.append(0x2362)  #uni2362	APL FUNCTIONAL SYMBOL DEL DIAERESIS
        chars.append(0x2363)  #uni2363	APL FUNCTIONAL SYMBOL STAR DIAERESIS
        chars.append(0x2364)  #uni2364	APL FUNCTIONAL SYMBOL JOT DIAERESIS
        chars.append(0x2365)  #uni2365	APL FUNCTIONAL SYMBOL CIRCLE DIAERESIS
        chars.append(0x2366)  #uni2366	APL FUNCTIONAL SYMBOL DOWN SHOE STILE
        chars.append(0x2367)  #uni2367	APL FUNCTIONAL SYMBOL LEFT SHOE STILE
        chars.append(0x2368)  #uni2368	APL FUNCTIONAL SYMBOL TILDE DIAERESIS
        chars.append(0x2369)  #uni2369	APL FUNCTIONAL SYMBOL GREATER-THAN DIAERESIS
        chars.append(0x236A)  #uni236A	APL FUNCTIONAL SYMBOL COMMA BAR
        chars.append(0x236B)  #uni236B	APL FUNCTIONAL SYMBOL DEL TILDE
        chars.append(0x236C)  #uni236C	APL FUNCTIONAL SYMBOL ZILDE
        chars.append(0x236D)  #uni236D	APL FUNCTIONAL SYMBOL STILE TILDE
        chars.append(0x236E)  #uni236E	APL FUNCTIONAL SYMBOL SEMICOLON UNDERBAR
        chars.append(0x236F)  #uni236F	APL FUNCTIONAL SYMBOL QUAD NOT EQUAL
        chars.append(0x2370)  #uni2370	APL FUNCTIONAL SYMBOL QUAD QUESTION
        chars.append(0x2371)  #uni2371	APL FUNCTIONAL SYMBOL DOWN CARET TILDE
        chars.append(0x2372)  #uni2372	APL FUNCTIONAL SYMBOL UP CARET TILDE
        chars.append(0x2373)  #uni2373	APL FUNCTIONAL SYMBOL IOTA
        chars.append(0x2374)  #uni2374	APL FUNCTIONAL SYMBOL RHO
        chars.append(0x2375)  #uni2375	APL FUNCTIONAL SYMBOL OMEGA
        chars.append(0x2376)  #uni2376	APL FUNCTIONAL SYMBOL ALPHA UNDERBAR
        chars.append(0x2377)  #uni2377	APL FUNCTIONAL SYMBOL EPSILON UNDERBAR
        chars.append(0x2378)  #uni2378	APL FUNCTIONAL SYMBOL IOTA UNDERBAR
        chars.append(0x2379)  #uni2379	APL FUNCTIONAL SYMBOL OMEGA UNDERBAR
        chars.append(0x237A)  #uni237A	APL FUNCTIONAL SYMBOL ALPHA
        chars.append(0x237B)  #uni237B	NOT CHECK MARK
        chars.append(0x237C)  #uni237C	RIGHT ANGLE WITH DOWNWARDS ZIGZAG ARROW
        chars.append(0x237D)  #uni237D	SHOULDERED OPEN BOX
        chars.append(0x237E)  #uni237E	BELL SYMBOL
        chars.append(0x237F)  #uni237F	VERTICAL LINE WITH MIDDLE DOT
        chars.append(0x2380)  #uni2380	INSERTION SYMBOL
        chars.append(0x2381)  #uni2381	CONTINUOUS UNDERLINE SYMBOL
        chars.append(0x2382)  #uni2382	DISCONTINUOUS UNDERLINE SYMBOL
        chars.append(0x2383)  #uni2383	EMPHASIS SYMBOL
        chars.append(0x2384)  #uni2384	COMPOSITION SYMBOL
        chars.append(0x2385)  #uni2385	WHITE SQUARE WITH CENTRE VERTICAL LINE
        chars.append(0x2386)  #uni2386	ENTER SYMBOL
        chars.append(0x2387)  #uni2387	ALTERNATIVE KEY SYMBOL
        chars.append(0x2388)  #uni2388	HELM SYMBOL
        chars.append(0x2389)  #uni2389	CIRCLED HORIZONTAL BAR WITH NOTCH
        chars.append(0x238A)  #uni238A	CIRCLED TRIANGLE DOWN
        chars.append(0x238B)  #uni238B	BROKEN CIRCLE WITH NORTHWEST ARROW
        chars.append(0x238C)  #uni238C	UNDO SYMBOL
        chars.append(0x238D)  #uni238D	MONOSTABLE SYMBOL
        chars.append(0x238E)  #uni238E	HYSTERESIS SYMBOL
        chars.append(0x238F)  #uni238F	OPEN-CIRCUIT-OUTPUT H-TYPE SYMBOL
        chars.append(0x2390)  #uni2390	OPEN-CIRCUIT-OUTPUT L-TYPE SYMBOL
        chars.append(0x2391)  #uni2391	PASSIVE-PULL-DOWN-OUTPUT SYMBOL
        chars.append(0x2392)  #uni2392	PASSIVE-PULL-UP-OUTPUT SYMBOL
        chars.append(0x2393)  #uni2393	DIRECT CURRENT SYMBOL FORM TWO
        chars.append(0x2394)  #uni2394	SOFTWARE-FUNCTION SYMBOL
        chars.append(0x2395)  #uni2395	APL FUNCTIONAL SYMBOL QUAD
        chars.append(0x2396)  #uni2396	DECIMAL SEPARATOR KEY SYMBOL
        chars.append(0x2397)  #uni2397	PREVIOUS PAGE
        chars.append(0x2398)  #uni2398	NEXT PAGE
        chars.append(0x2399)  #uni2399	PRINT SCREEN SYMBOL
        chars.append(0x239A)  #uni239A	CLEAR SCREEN SYMBOL
        chars.append(0x239B)  #uni239B	LEFT PARENTHESIS UPPER HOOK
        chars.append(0x239C)  #uni239C	LEFT PARENTHESIS EXTENSION
        chars.append(0x239D)  #uni239D	LEFT PARENTHESIS LOWER HOOK
        chars.append(0x239E)  #uni239E	RIGHT PARENTHESIS UPPER HOOK
        chars.append(0x239F)  #uni239F	RIGHT PARENTHESIS EXTENSION
        chars.append(0x23A0)  #uni23A0	RIGHT PARENTHESIS LOWER HOOK
        chars.append(0x23A1)  #uni23A1	LEFT SQUARE BRACKET UPPER CORNER
        chars.append(0x23A2)  #uni23A2	LEFT SQUARE BRACKET EXTENSION
        chars.append(0x23A3)  #uni23A3	LEFT SQUARE BRACKET LOWER CORNER
        chars.append(0x23A4)  #uni23A4	RIGHT SQUARE BRACKET UPPER CORNER
        chars.append(0x23A5)  #uni23A5	RIGHT SQUARE BRACKET EXTENSION
        chars.append(0x23A6)  #uni23A6	RIGHT SQUARE BRACKET LOWER CORNER
        chars.append(0x23A7)  #uni23A7	LEFT CURLY BRACKET UPPER HOOK
        chars.append(0x23A8)  #uni23A8	LEFT CURLY BRACKET MIDDLE PIECE
        chars.append(0x23A9)  #uni23A9	LEFT CURLY BRACKET LOWER HOOK
        chars.append(0x23AA)  #uni23AA	CURLY BRACKET EXTENSION
        chars.append(0x23AB)  #uni23AB	RIGHT CURLY BRACKET UPPER HOOK
        chars.append(0x23AC)  #uni23AC	RIGHT CURLY BRACKET MIDDLE PIECE
        chars.append(0x23AD)  #uni23AD	RIGHT CURLY BRACKET LOWER HOOK
        chars.append(0x23AE)  #uni23AE	INTEGRAL EXTENSION
        chars.append(0x23AF)  #uni23AF	HORIZONTAL LINE EXTENSION
        chars.append(0x23B0)  #uni23B0	UPPER LEFT OR LOWER RIGHT CURLY BRACKET SECTION
        chars.append(0x23B1)  #uni23B1	UPPER RIGHT OR LOWER LEFT CURLY BRACKET SECTION
        chars.append(0x23B2)  #uni23B2	SUMMATION TOP
        chars.append(0x23B3)  #uni23B3	SUMMATION BOTTOM
        chars.append(0x23B4)  #uni23B4	TOP SQUARE BRACKET
        chars.append(0x23B5)  #uni23B5	BOTTOM SQUARE BRACKET
        chars.append(0x23B6)  #uni23B6	BOTTOM SQUARE BRACKET OVER TOP SQUARE BRACKET
        chars.append(0x23B7)  #uni23B7	RADICAL SYMBOL BOTTOM
        chars.append(0x23B8)  #uni23B8	LEFT VERTICAL BOX LINE
        chars.append(0x23B9)  #uni23B9	RIGHT VERTICAL BOX LINE
        chars.append(0x23BA)  #uni23BA	HORIZONTAL SCAN LINE-1
        chars.append(0x23BB)  #uni23BB	HORIZONTAL SCAN LINE-3
        chars.append(0x23BC)  #uni23BC	HORIZONTAL SCAN LINE-7
        chars.append(0x23BD)  #uni23BD	HORIZONTAL SCAN LINE-9
        chars.append(0x23BE)  #uni23BE	DENTISTRY SYMBOL LIGHT VERTICAL AND TOP RIGHT
        chars.append(0x23BF)  #uni23BF	DENTISTRY SYMBOL LIGHT VERTICAL AND BOTTOM RIGHT
        chars.append(0x23C0)  #uni23C0	DENTISTRY SYMBOL LIGHT VERTICAL WITH CIRCLE
        chars.append(0x00A0)  #uni00A0	NO-BREAK SPACE
        chars.append(0x23C2)  #uni23C2	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH CIRCLE
        chars.append(0x23C3)  #uni23C3	DENTISTRY SYMBOL LIGHT VERTICAL WITH TRIANGLE
        chars.append(0x23C4)  #uni23C4	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH TRIANGLE
        chars.append(0x23C5)  #uni23C5	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH TRIANGLE
        chars.append(0x23C6)  #uni23C6	DENTISTRY SYMBOL LIGHT VERTICAL AND WAVE
        chars.append(0x23C7)  #uni23C7	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH WAVE
        chars.append(0x23C8)  #uni23C8	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL WITH WAVE
        chars.append(0x23C9)  #uni23C9	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL
        chars.append(0x23CA)  #uni23CA	DENTISTRY SYMBOL LIGHT UP AND HORIZONTAL
        chars.append(0x23CB)  #uni23CB	DENTISTRY SYMBOL LIGHT VERTICAL AND TOP LEFT
        chars.append(0x23CC)  #uni23CC	DENTISTRY SYMBOL LIGHT VERTICAL AND BOTTOM LEFT
        chars.append(0x23CD)  #uni23CD	SQUARE FOOT
        chars.append(0x23CE)  #uni23CE	RETURN SYMBOL
        chars.append(0x23CF)  #uni23CF	EJECT SYMBOL
        chars.append(0x23D0)  #uni23D0	VERTICAL LINE EXTENSION
        chars.append(0x23D1)  #uni23D1	METRICAL BREVE
        chars.append(0x23D2)  #uni23D2	METRICAL LONG OVER SHORT
        chars.append(0x23D3)  #uni23D3	METRICAL SHORT OVER LONG
        chars.append(0x23D4)  #uni23D4	METRICAL LONG OVER TWO SHORTS
        chars.append(0x23D5)  #uni23D5	METRICAL TWO SHORTS OVER LONG
        chars.append(0x23D6)  #uni23D6	METRICAL TWO SHORTS JOINED
        chars.append(0x23D7)  #uni23D7	METRICAL TRISEME
        chars.append(0x23D8)  #uni23D8	METRICAL TETRASEME
        chars.append(0x23D9)  #uni23D9	METRICAL PENTASEME
        chars.append(0x23DA)  #uni23DA	EARTH GROUND
        chars.append(0x23DB)  #uni23DB	FUSE
        chars.append(0x23DC)  #uni23DC	TOP PARENTHESIS
        chars.append(0x23DD)  #uni23DD	BOTTOM PARENTHESIS
        chars.append(0x23DE)  #uni23DE	TOP CURLY BRACKET
        chars.append(0x23DF)  #uni23DF	BOTTOM CURLY BRACKET
        chars.append(0x23E0)  #uni23E0	TOP TORTOISE SHELL BRACKET
        chars.append(0x23E1)  #uni23E1	BOTTOM TORTOISE SHELL BRACKET
        chars.append(0x23E2)  #uni23E2	WHITE TRAPEZIUM
        chars.append(0x23E3)  #uni23E3	BENZENE RING WITH CIRCLE
        chars.append(0x23E4)  #uni23E4	STRAIGHTNESS
        chars.append(0x23E5)  #uni23E5	FLATNESS
        chars.append(0x23E6)  #uni23E6	AC CURRENT
        chars.append(0x23E7)  #uni23E7	ELECTRICAL INTERSECTION
        chars.append(0x23E8)  #uni23E8	DECIMAL EXPONENT SYMBOL
        chars.append(0x23E9)  #uni23E9	????
        chars.append(0x23EA)  #uni23EA	????
        chars.append(0x23EB)  #uni23EB	????
        chars.append(0x23EC)  #uni23EC	????
        chars.append(0x23ED)  #uni23ED	????
        chars.append(0x23EE)  #uni23EE	????
        chars.append(0x23EF)  #uni23EF	????
        chars.append(0x23F0)  #uni23F0	????
        chars.append(0x23F1)  #uni23F1	????
        chars.append(0x23F2)  #uni23F2	????
        chars.append(0x23F3)  #uni23F3	????
        chars.append(0x1F0A9)  #glyph04731	????
        chars.append(0x1F713)  #glyph05028	????
        chars.append(0x1F105)  #glyph04786	DIGIT FOUR COMMA
        chars.append(0x1F0AA)  #glyph04732	????
        chars.append(0x1F0C9)  #glyph04759	????
        chars.append(0x2400)  #uni2400	SYMBOL FOR NULL
        chars.append(0x2401)  #uni2401	SYMBOL FOR START OF HEADING
        chars.append(0x2402)  #uni2402	SYMBOL FOR START OF TEXT
        chars.append(0x2403)  #uni2403	SYMBOL FOR END OF TEXT
        chars.append(0x2404)  #uni2404	SYMBOL FOR END OF TRANSMISSION
        chars.append(0x2405)  #uni2405	SYMBOL FOR ENQUIRY
        chars.append(0x2406)  #uni2406	SYMBOL FOR ACKNOWLEDGE
        chars.append(0x2407)  #uni2407	SYMBOL FOR BELL
        chars.append(0x2408)  #uni2408	SYMBOL FOR BACKSPACE
        chars.append(0x2409)  #uni2409	SYMBOL FOR HORIZONTAL TABULATION
        chars.append(0x240A)  #uni240A	SYMBOL FOR LINE FEED
        chars.append(0x240B)  #uni240B	SYMBOL FOR VERTICAL TABULATION
        chars.append(0x240C)  #uni240C	SYMBOL FOR FORM FEED
        chars.append(0x240D)  #uni240D	SYMBOL FOR CARRIAGE RETURN
        chars.append(0x240E)  #uni240E	SYMBOL FOR SHIFT OUT
        chars.append(0x240F)  #uni240F	SYMBOL FOR SHIFT IN
        chars.append(0x2410)  #uni2410	SYMBOL FOR DATA LINK ESCAPE
        chars.append(0x2411)  #uni2411	SYMBOL FOR DEVICE CONTROL ONE
        chars.append(0x2412)  #uni2412	SYMBOL FOR DEVICE CONTROL TWO
        chars.append(0x2413)  #uni2413	SYMBOL FOR DEVICE CONTROL THREE
        chars.append(0x2414)  #uni2414	SYMBOL FOR DEVICE CONTROL FOUR
        chars.append(0x2415)  #uni2415	SYMBOL FOR NEGATIVE ACKNOWLEDGE
        chars.append(0x2416)  #uni2416	SYMBOL FOR SYNCHRONOUS IDLE
        chars.append(0x2417)  #uni2417	SYMBOL FOR END OF TRANSMISSION BLOCK
        chars.append(0x2418)  #uni2418	SYMBOL FOR CANCEL
        chars.append(0x2419)  #uni2419	SYMBOL FOR END OF MEDIUM
        chars.append(0x241A)  #uni241A	SYMBOL FOR SUBSTITUTE
        chars.append(0x241B)  #uni241B	SYMBOL FOR ESCAPE
        chars.append(0x241C)  #uni241C	SYMBOL FOR FILE SEPARATOR
        chars.append(0x241D)  #uni241D	SYMBOL FOR GROUP SEPARATOR
        chars.append(0x241E)  #uni241E	SYMBOL FOR RECORD SEPARATOR
        chars.append(0x241F)  #uni241F	SYMBOL FOR UNIT SEPARATOR
        chars.append(0x2420)  #uni2420	SYMBOL FOR SPACE
        chars.append(0x2421)  #uni2421	SYMBOL FOR DELETE
        chars.append(0x2422)  #uni2422	BLANK SYMBOL
        chars.append(0x2423)  #uni2423	OPEN BOX
        chars.append(0x2424)  #uni2424	SYMBOL FOR NEWLINE
        chars.append(0x2425)  #uni2425	SYMBOL FOR DELETE FORM TWO
        chars.append(0x2426)  #uni2426	SYMBOL FOR SUBSTITUTE FORM TWO
        chars.append(0x1D0B1)  #glyph03118	BYZANTINE MUSICAL SYMBOL MARTYRIA VARYS ICHOS
        chars.append(0x1F0B2)  #glyph04738	????
        chars.append(0x1F0B3)  #glyph04739	????
        chars.append(0x1F715)  #glyph05030	????
        chars.append(0x1F0B4)  #glyph04740	????
        chars.append(0x1F0B5)  #glyph04741	????
        chars.append(0x2440)  #uni2440	OCR HOOK
        chars.append(0x2441)  #uni2441	OCR CHAIR
        chars.append(0x2442)  #uni2442	OCR FORK
        chars.append(0x2443)  #uni2443	OCR INVERTED FORK
        chars.append(0x2444)  #uni2444	OCR BELT BUCKLE
        chars.append(0x2445)  #uni2445	OCR BOW TIE
        chars.append(0x2446)  #uni2446	OCR BRANCH BANK IDENTIFICATION
        chars.append(0x2447)  #uni2447	OCR AMOUNT OF CHECK
        chars.append(0x2448)  #uni2448	OCR DASH
        chars.append(0x2449)  #uni2449	OCR CUSTOMER ACCOUNT NUMBER
        chars.append(0x244A)  #uni244A	OCR DOUBLE BACKSLASH
        chars.append(0x1F0B7)  #glyph04743	????
        chars.append(0x1F232)  #glyph04989	????
        chars.append(0x1F0B8)  #glyph04744	????
        chars.append(0x1F716)  #glyph05031	????
        chars.append(0x1F0B9)  #glyph04745	????
        chars.append(0x1F0BA)  #glyph04746	????
        chars.append(0x2460)  #uni2460	CIRCLED DIGIT ONE
        chars.append(0x2461)  #uni2461	CIRCLED DIGIT TWO
        chars.append(0x2462)  #uni2462	CIRCLED DIGIT THREE
        chars.append(0x2463)  #uni2463	CIRCLED DIGIT FOUR
        chars.append(0x2464)  #uni2464	CIRCLED DIGIT FIVE
        chars.append(0x2465)  #uni2465	CIRCLED DIGIT SIX
        chars.append(0x2466)  #uni2466	CIRCLED DIGIT SEVEN
        chars.append(0x2467)  #uni2467	CIRCLED DIGIT EIGHT
        chars.append(0x2468)  #uni2468	CIRCLED DIGIT NINE
        chars.append(0x2469)  #uni2469	CIRCLED NUMBER TEN
        chars.append(0x246A)  #uni246A	CIRCLED NUMBER ELEVEN
        chars.append(0x246B)  #uni246B	CIRCLED NUMBER TWELVE
        chars.append(0x246C)  #uni246C	CIRCLED NUMBER THIRTEEN
        chars.append(0x246D)  #uni246D	CIRCLED NUMBER FOURTEEN
        chars.append(0x246E)  #uni246E	CIRCLED NUMBER FIFTEEN
        chars.append(0x246F)  #uni246F	CIRCLED NUMBER SIXTEEN
        chars.append(0x2470)  #uni2470	CIRCLED NUMBER SEVENTEEN
        chars.append(0x2471)  #uni2471	CIRCLED NUMBER EIGHTEEN
        chars.append(0x2472)  #uni2472	CIRCLED NUMBER NINETEEN
        chars.append(0x2473)  #uni2473	CIRCLED NUMBER TWENTY
        chars.append(0x2474)  #uni2474	PARENTHESIZED DIGIT ONE
        chars.append(0x2475)  #uni2475	PARENTHESIZED DIGIT TWO
        chars.append(0x2476)  #uni2476	PARENTHESIZED DIGIT THREE
        chars.append(0x2477)  #uni2477	PARENTHESIZED DIGIT FOUR
        chars.append(0x2478)  #uni2478	PARENTHESIZED DIGIT FIVE
        chars.append(0x2479)  #uni2479	PARENTHESIZED DIGIT SIX
        chars.append(0x247A)  #uni247A	PARENTHESIZED DIGIT SEVEN
        chars.append(0x247B)  #uni247B	PARENTHESIZED DIGIT EIGHT
        chars.append(0x247C)  #uni247C	PARENTHESIZED DIGIT NINE
        chars.append(0x247D)  #uni247D	PARENTHESIZED NUMBER TEN
        chars.append(0x247E)  #uni247E	PARENTHESIZED NUMBER ELEVEN
        chars.append(0x247F)  #uni247F	PARENTHESIZED NUMBER TWELVE
        chars.append(0x2480)  #uni2480	PARENTHESIZED NUMBER THIRTEEN
        chars.append(0x2481)  #uni2481	PARENTHESIZED NUMBER FOURTEEN
        chars.append(0x2482)  #uni2482	PARENTHESIZED NUMBER FIFTEEN
        chars.append(0x2483)  #uni2483	PARENTHESIZED NUMBER SIXTEEN
        chars.append(0x2484)  #uni2484	PARENTHESIZED NUMBER SEVENTEEN
        chars.append(0x2485)  #uni2485	PARENTHESIZED NUMBER EIGHTEEN
        chars.append(0x2486)  #uni2486	PARENTHESIZED NUMBER NINETEEN
        chars.append(0x2487)  #uni2487	PARENTHESIZED NUMBER TWENTY
        chars.append(0x2488)  #uni2488	DIGIT ONE FULL STOP
        chars.append(0x2489)  #uni2489	DIGIT TWO FULL STOP
        chars.append(0x248A)  #uni248A	DIGIT THREE FULL STOP
        chars.append(0x248B)  #uni248B	DIGIT FOUR FULL STOP
        chars.append(0x248C)  #uni248C	DIGIT FIVE FULL STOP
        chars.append(0x248D)  #uni248D	DIGIT SIX FULL STOP
        chars.append(0x248E)  #uni248E	DIGIT SEVEN FULL STOP
        chars.append(0x248F)  #uni248F	DIGIT EIGHT FULL STOP
        chars.append(0x2490)  #uni2490	DIGIT NINE FULL STOP
        chars.append(0x2491)  #uni2491	NUMBER TEN FULL STOP
        chars.append(0x2492)  #uni2492	NUMBER ELEVEN FULL STOP
        chars.append(0x2493)  #uni2493	NUMBER TWELVE FULL STOP
        chars.append(0x2494)  #uni2494	NUMBER THIRTEEN FULL STOP
        chars.append(0x2495)  #uni2495	NUMBER FOURTEEN FULL STOP
        chars.append(0x2496)  #uni2496	NUMBER FIFTEEN FULL STOP
        chars.append(0x2497)  #uni2497	NUMBER SIXTEEN FULL STOP
        chars.append(0x2498)  #uni2498	NUMBER SEVENTEEN FULL STOP
        chars.append(0x2499)  #uni2499	NUMBER EIGHTEEN FULL STOP
        chars.append(0x249A)  #uni249A	NUMBER NINETEEN FULL STOP
        chars.append(0x249B)  #uni249B	NUMBER TWENTY FULL STOP
        chars.append(0x249C)  #uni249C	PARENTHESIZED LATIN SMALL LETTER A
        chars.append(0x249D)  #uni249D	PARENTHESIZED LATIN SMALL LETTER B
        chars.append(0x249E)  #uni249E	PARENTHESIZED LATIN SMALL LETTER C
        chars.append(0x249F)  #uni249F	PARENTHESIZED LATIN SMALL LETTER D
        chars.append(0x24A0)  #uni24A0	PARENTHESIZED LATIN SMALL LETTER E
        chars.append(0x24A1)  #uni24A1	PARENTHESIZED LATIN SMALL LETTER F
        chars.append(0x24A2)  #uni24A2	PARENTHESIZED LATIN SMALL LETTER G
        chars.append(0x24A3)  #uni24A3	PARENTHESIZED LATIN SMALL LETTER H
        chars.append(0x24A4)  #uni24A4	PARENTHESIZED LATIN SMALL LETTER I
        chars.append(0x24A5)  #uni24A5	PARENTHESIZED LATIN SMALL LETTER J
        chars.append(0x24A6)  #uni24A6	PARENTHESIZED LATIN SMALL LETTER K
        chars.append(0x24A7)  #uni24A7	PARENTHESIZED LATIN SMALL LETTER L
        chars.append(0x24A8)  #uni24A8	PARENTHESIZED LATIN SMALL LETTER M
        chars.append(0x24A9)  #uni24A9	PARENTHESIZED LATIN SMALL LETTER N
        chars.append(0x24AA)  #uni24AA	PARENTHESIZED LATIN SMALL LETTER O
        chars.append(0x24AB)  #uni24AB	PARENTHESIZED LATIN SMALL LETTER P
        chars.append(0x24AC)  #uni24AC	PARENTHESIZED LATIN SMALL LETTER Q
        chars.append(0x24AD)  #uni24AD	PARENTHESIZED LATIN SMALL LETTER R
        chars.append(0x24AE)  #uni24AE	PARENTHESIZED LATIN SMALL LETTER S
        chars.append(0x24AF)  #uni24AF	PARENTHESIZED LATIN SMALL LETTER T
        chars.append(0x24B0)  #uni24B0	PARENTHESIZED LATIN SMALL LETTER U
        chars.append(0x24B1)  #uni24B1	PARENTHESIZED LATIN SMALL LETTER V
        chars.append(0x24B2)  #uni24B2	PARENTHESIZED LATIN SMALL LETTER W
        chars.append(0x24B3)  #uni24B3	PARENTHESIZED LATIN SMALL LETTER X
        chars.append(0x24B4)  #uni24B4	PARENTHESIZED LATIN SMALL LETTER Y
        chars.append(0x24B5)  #uni24B5	PARENTHESIZED LATIN SMALL LETTER Z
        chars.append(0x24B6)  #uni24B6	CIRCLED LATIN CAPITAL LETTER A
        chars.append(0x24B7)  #uni24B7	CIRCLED LATIN CAPITAL LETTER B
        chars.append(0x24B8)  #uni24B8	CIRCLED LATIN CAPITAL LETTER C
        chars.append(0x24B9)  #uni24B9	CIRCLED LATIN CAPITAL LETTER D
        chars.append(0x24BA)  #uni24BA	CIRCLED LATIN CAPITAL LETTER E
        chars.append(0x24BB)  #uni24BB	CIRCLED LATIN CAPITAL LETTER F
        chars.append(0x24BC)  #uni24BC	CIRCLED LATIN CAPITAL LETTER G
        chars.append(0x24BD)  #uni24BD	CIRCLED LATIN CAPITAL LETTER H
        chars.append(0x24BE)  #uni24BE	CIRCLED LATIN CAPITAL LETTER I
        chars.append(0x24BF)  #uni24BF	CIRCLED LATIN CAPITAL LETTER J
        chars.append(0x24C0)  #uni24C0	CIRCLED LATIN CAPITAL LETTER K
        chars.append(0x24C1)  #uni24C1	CIRCLED LATIN CAPITAL LETTER L
        chars.append(0x24C2)  #uni24C2	CIRCLED LATIN CAPITAL LETTER M
        chars.append(0x24C3)  #uni24C3	CIRCLED LATIN CAPITAL LETTER N
        chars.append(0x24C4)  #uni24C4	CIRCLED LATIN CAPITAL LETTER O
        chars.append(0x24C5)  #uni24C5	CIRCLED LATIN CAPITAL LETTER P
        chars.append(0x24C6)  #uni24C6	CIRCLED LATIN CAPITAL LETTER Q
        chars.append(0x24C7)  #uni24C7	CIRCLED LATIN CAPITAL LETTER R
        chars.append(0x24C8)  #uni24C8	CIRCLED LATIN CAPITAL LETTER S
        chars.append(0x24C9)  #uni24C9	CIRCLED LATIN CAPITAL LETTER T
        chars.append(0x24CA)  #uni24CA	CIRCLED LATIN CAPITAL LETTER U
        chars.append(0x24CB)  #uni24CB	CIRCLED LATIN CAPITAL LETTER V
        chars.append(0x24CC)  #uni24CC	CIRCLED LATIN CAPITAL LETTER W
        chars.append(0x24CD)  #uni24CD	CIRCLED LATIN CAPITAL LETTER X
        chars.append(0x24CE)  #uni24CE	CIRCLED LATIN CAPITAL LETTER Y
        chars.append(0x24CF)  #uni24CF	CIRCLED LATIN CAPITAL LETTER Z
        chars.append(0x24D0)  #uni24D0	CIRCLED LATIN SMALL LETTER A
        chars.append(0x24D1)  #uni24D1	CIRCLED LATIN SMALL LETTER B
        chars.append(0x24D2)  #uni24D2	CIRCLED LATIN SMALL LETTER C
        chars.append(0x24D3)  #uni24D3	CIRCLED LATIN SMALL LETTER D
        chars.append(0x24D4)  #uni24D4	CIRCLED LATIN SMALL LETTER E
        chars.append(0x24D5)  #uni24D5	CIRCLED LATIN SMALL LETTER F
        chars.append(0x24D6)  #uni24D6	CIRCLED LATIN SMALL LETTER G
        chars.append(0x24D7)  #uni24D7	CIRCLED LATIN SMALL LETTER H
        chars.append(0x24D8)  #uni24D8	CIRCLED LATIN SMALL LETTER I
        chars.append(0x24D9)  #uni24D9	CIRCLED LATIN SMALL LETTER J
        chars.append(0x24DA)  #uni24DA	CIRCLED LATIN SMALL LETTER K
        chars.append(0x24DB)  #uni24DB	CIRCLED LATIN SMALL LETTER L
        chars.append(0x24DC)  #uni24DC	CIRCLED LATIN SMALL LETTER M
        chars.append(0x24DD)  #uni24DD	CIRCLED LATIN SMALL LETTER N
        chars.append(0x24DE)  #uni24DE	CIRCLED LATIN SMALL LETTER O
        chars.append(0x24DF)  #uni24DF	CIRCLED LATIN SMALL LETTER P
        chars.append(0x24E0)  #uni24E0	CIRCLED LATIN SMALL LETTER Q
        chars.append(0x24E1)  #uni24E1	CIRCLED LATIN SMALL LETTER R
        chars.append(0x24E2)  #uni24E2	CIRCLED LATIN SMALL LETTER S
        chars.append(0x24E3)  #uni24E3	CIRCLED LATIN SMALL LETTER T
        chars.append(0x24E4)  #uni24E4	CIRCLED LATIN SMALL LETTER U
        chars.append(0x24E5)  #uni24E5	CIRCLED LATIN SMALL LETTER V
        chars.append(0x24E6)  #uni24E6	CIRCLED LATIN SMALL LETTER W
        chars.append(0x24E7)  #uni24E7	CIRCLED LATIN SMALL LETTER X
        chars.append(0x24E8)  #uni24E8	CIRCLED LATIN SMALL LETTER Y
        chars.append(0x24E9)  #uni24E9	CIRCLED LATIN SMALL LETTER Z
        chars.append(0x24EA)  #uni24EA	CIRCLED DIGIT ZERO
        chars.append(0x24EB)  #uni24EB	NEGATIVE CIRCLED NUMBER ELEVEN
        chars.append(0x24EC)  #uni24EC	NEGATIVE CIRCLED NUMBER TWELVE
        chars.append(0x24ED)  #uni24ED	NEGATIVE CIRCLED NUMBER THIRTEEN
        chars.append(0x24EE)  #uni24EE	NEGATIVE CIRCLED NUMBER FOURTEEN
        chars.append(0x24EF)  #uni24EF	NEGATIVE CIRCLED NUMBER FIFTEEN
        chars.append(0x24F0)  #uni24F0	NEGATIVE CIRCLED NUMBER SIXTEEN
        chars.append(0x24F1)  #uni24F1	NEGATIVE CIRCLED NUMBER SEVENTEEN
        chars.append(0x24F2)  #uni24F2	NEGATIVE CIRCLED NUMBER EIGHTEEN
        chars.append(0x24F3)  #uni24F3	NEGATIVE CIRCLED NUMBER NINETEEN
        chars.append(0x24F4)  #uni24F4	NEGATIVE CIRCLED NUMBER TWENTY
        chars.append(0x24F5)  #uni24F5	DOUBLE CIRCLED DIGIT ONE
        chars.append(0x24F6)  #uni24F6	DOUBLE CIRCLED DIGIT TWO
        chars.append(0x24F7)  #uni24F7	DOUBLE CIRCLED DIGIT THREE
        chars.append(0x24F8)  #uni24F8	DOUBLE CIRCLED DIGIT FOUR
        chars.append(0x24F9)  #uni24F9	DOUBLE CIRCLED DIGIT FIVE
        chars.append(0x24FA)  #uni24FA	DOUBLE CIRCLED DIGIT SIX
        chars.append(0x24FB)  #uni24FB	DOUBLE CIRCLED DIGIT SEVEN
        chars.append(0x24FC)  #uni24FC	DOUBLE CIRCLED DIGIT EIGHT
        chars.append(0x24FD)  #uni24FD	DOUBLE CIRCLED DIGIT NINE
        chars.append(0x24FE)  #uni24FE	DOUBLE CIRCLED NUMBER TEN
        chars.append(0x24FF)  #uni24FF	NEGATIVE CIRCLED DIGIT ZERO
        chars.append(0x2500)  #SF100000	BOX DRAWINGS LIGHT HORIZONTAL
        chars.append(0x2501)  #uni2501	BOX DRAWINGS HEAVY HORIZONTAL
        chars.append(0x2502)  #SF110000	BOX DRAWINGS LIGHT VERTICAL
        chars.append(0x2503)  #uni2503	BOX DRAWINGS HEAVY VERTICAL
        chars.append(0x2504)  #uni2504	BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL
        chars.append(0x2505)  #uni2505	BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL
        chars.append(0x2506)  #uni2506	BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL
        chars.append(0x2507)  #uni2507	BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL
        chars.append(0x2508)  #uni2508	BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL
        chars.append(0x2509)  #uni2509	BOX DRAWINGS HEAVY QUADRUPLE DASH HORIZONTAL
        chars.append(0x250A)  #uni250A	BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL
        chars.append(0x250B)  #uni250B	BOX DRAWINGS HEAVY QUADRUPLE DASH VERTICAL
        chars.append(0x250C)  #SF010000	BOX DRAWINGS LIGHT DOWN AND RIGHT
        chars.append(0x250D)  #uni250D	BOX DRAWINGS DOWN LIGHT AND RIGHT HEAVY
        chars.append(0x250E)  #uni250E	BOX DRAWINGS DOWN HEAVY AND RIGHT LIGHT
        chars.append(0x250F)  #uni250F	BOX DRAWINGS HEAVY DOWN AND RIGHT
        chars.append(0x2510)  #SF030000	BOX DRAWINGS LIGHT DOWN AND LEFT
        chars.append(0x2511)  #uni2511	BOX DRAWINGS DOWN LIGHT AND LEFT HEAVY
        chars.append(0x2512)  #uni2512	BOX DRAWINGS DOWN HEAVY AND LEFT LIGHT
        chars.append(0x2513)  #uni2513	BOX DRAWINGS HEAVY DOWN AND LEFT
        chars.append(0x2514)  #SF020000	BOX DRAWINGS LIGHT UP AND RIGHT
        chars.append(0x2515)  #uni2515	BOX DRAWINGS UP LIGHT AND RIGHT HEAVY
        chars.append(0x2516)  #uni2516	BOX DRAWINGS UP HEAVY AND RIGHT LIGHT
        chars.append(0x2517)  #uni2517	BOX DRAWINGS HEAVY UP AND RIGHT
        chars.append(0x2518)  #SF040000	BOX DRAWINGS LIGHT UP AND LEFT
        chars.append(0x2519)  #uni2519	BOX DRAWINGS UP LIGHT AND LEFT HEAVY
        chars.append(0x251A)  #uni251A	BOX DRAWINGS UP HEAVY AND LEFT LIGHT
        chars.append(0x251B)  #uni251B	BOX DRAWINGS HEAVY UP AND LEFT
        chars.append(0x251C)  #SF080000	BOX DRAWINGS LIGHT VERTICAL AND RIGHT
        chars.append(0x251D)  #uni251D	BOX DRAWINGS VERTICAL LIGHT AND RIGHT HEAVY
        chars.append(0x251E)  #uni251E	BOX DRAWINGS UP HEAVY AND RIGHT DOWN LIGHT
        chars.append(0x251F)  #uni251F	BOX DRAWINGS DOWN HEAVY AND RIGHT UP LIGHT
        chars.append(0x2520)  #uni2520	BOX DRAWINGS VERTICAL HEAVY AND RIGHT LIGHT
        chars.append(0x2521)  #uni2521	BOX DRAWINGS DOWN LIGHT AND RIGHT UP HEAVY
        chars.append(0x2522)  #uni2522	BOX DRAWINGS UP LIGHT AND RIGHT DOWN HEAVY
        chars.append(0x2523)  #uni2523	BOX DRAWINGS HEAVY VERTICAL AND RIGHT
        chars.append(0x2524)  #SF090000	BOX DRAWINGS LIGHT VERTICAL AND LEFT
        chars.append(0x2525)  #uni2525	BOX DRAWINGS VERTICAL LIGHT AND LEFT HEAVY
        chars.append(0x2526)  #uni2526	BOX DRAWINGS UP HEAVY AND LEFT DOWN LIGHT
        chars.append(0x2527)  #uni2527	BOX DRAWINGS DOWN HEAVY AND LEFT UP LIGHT
        chars.append(0x2528)  #uni2528	BOX DRAWINGS VERTICAL HEAVY AND LEFT LIGHT
        chars.append(0x2529)  #uni2529	BOX DRAWINGS DOWN LIGHT AND LEFT UP HEAVY
        chars.append(0x252A)  #uni252A	BOX DRAWINGS UP LIGHT AND LEFT DOWN HEAVY
        chars.append(0x252B)  #uni252B	BOX DRAWINGS HEAVY VERTICAL AND LEFT
        chars.append(0x252C)  #SF060000	BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
        chars.append(0x252D)  #uni252D	BOX DRAWINGS LEFT HEAVY AND RIGHT DOWN LIGHT
        chars.append(0x252E)  #uni252E	BOX DRAWINGS RIGHT HEAVY AND LEFT DOWN LIGHT
        chars.append(0x252F)  #uni252F	BOX DRAWINGS DOWN LIGHT AND HORIZONTAL HEAVY
        chars.append(0x2530)  #uni2530	BOX DRAWINGS DOWN HEAVY AND HORIZONTAL LIGHT
        chars.append(0x2531)  #uni2531	BOX DRAWINGS RIGHT LIGHT AND LEFT DOWN HEAVY
        chars.append(0x2532)  #uni2532	BOX DRAWINGS LEFT LIGHT AND RIGHT DOWN HEAVY
        chars.append(0x2533)  #uni2533	BOX DRAWINGS HEAVY DOWN AND HORIZONTAL
        chars.append(0x2534)  #SF070000	BOX DRAWINGS LIGHT UP AND HORIZONTAL
        chars.append(0x2535)  #uni2535	BOX DRAWINGS LEFT HEAVY AND RIGHT UP LIGHT
        chars.append(0x2536)  #uni2536	BOX DRAWINGS RIGHT HEAVY AND LEFT UP LIGHT
        chars.append(0x2537)  #uni2537	BOX DRAWINGS UP LIGHT AND HORIZONTAL HEAVY
        chars.append(0x2538)  #uni2538	BOX DRAWINGS UP HEAVY AND HORIZONTAL LIGHT
        chars.append(0x2539)  #uni2539	BOX DRAWINGS RIGHT LIGHT AND LEFT UP HEAVY
        chars.append(0x253A)  #uni253A	BOX DRAWINGS LEFT LIGHT AND RIGHT UP HEAVY
        chars.append(0x253B)  #uni253B	BOX DRAWINGS HEAVY UP AND HORIZONTAL
        chars.append(0x253C)  #SF050000	BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
        chars.append(0x253D)  #uni253D	BOX DRAWINGS LEFT HEAVY AND RIGHT VERTICAL LIGHT
        chars.append(0x253E)  #uni253E	BOX DRAWINGS RIGHT HEAVY AND LEFT VERTICAL LIGHT
        chars.append(0x253F)  #uni253F	BOX DRAWINGS VERTICAL LIGHT AND HORIZONTAL HEAVY
        chars.append(0x2540)  #uni2540	BOX DRAWINGS UP HEAVY AND DOWN HORIZONTAL LIGHT
        chars.append(0x2541)  #uni2541	BOX DRAWINGS DOWN HEAVY AND UP HORIZONTAL LIGHT
        chars.append(0x2542)  #uni2542	BOX DRAWINGS VERTICAL HEAVY AND HORIZONTAL LIGHT
        chars.append(0x2543)  #uni2543	BOX DRAWINGS LEFT UP HEAVY AND RIGHT DOWN LIGHT
        chars.append(0x2544)  #uni2544	BOX DRAWINGS RIGHT UP HEAVY AND LEFT DOWN LIGHT
        chars.append(0x2545)  #uni2545	BOX DRAWINGS LEFT DOWN HEAVY AND RIGHT UP LIGHT
        chars.append(0x2546)  #uni2546	BOX DRAWINGS RIGHT DOWN HEAVY AND LEFT UP LIGHT
        chars.append(0x2547)  #uni2547	BOX DRAWINGS DOWN LIGHT AND UP HORIZONTAL HEAVY
        chars.append(0x2548)  #uni2548	BOX DRAWINGS UP LIGHT AND DOWN HORIZONTAL HEAVY
        chars.append(0x2549)  #uni2549	BOX DRAWINGS RIGHT LIGHT AND LEFT VERTICAL HEAVY
        chars.append(0x254A)  #uni254A	BOX DRAWINGS LEFT LIGHT AND RIGHT VERTICAL HEAVY
        chars.append(0x254B)  #uni254B	BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL
        chars.append(0x254C)  #uni254C	BOX DRAWINGS LIGHT DOUBLE DASH HORIZONTAL
        chars.append(0x254D)  #uni254D	BOX DRAWINGS HEAVY DOUBLE DASH HORIZONTAL
        chars.append(0x254E)  #uni254E	BOX DRAWINGS LIGHT DOUBLE DASH VERTICAL
        chars.append(0x254F)  #uni254F	BOX DRAWINGS HEAVY DOUBLE DASH VERTICAL
        chars.append(0x2550)  #SF430000	BOX DRAWINGS DOUBLE HORIZONTAL
        chars.append(0x2551)  #SF240000	BOX DRAWINGS DOUBLE VERTICAL
        chars.append(0x2552)  #SF510000	BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
        chars.append(0x2553)  #SF520000	BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
        chars.append(0x2554)  #SF390000	BOX DRAWINGS DOUBLE DOWN AND RIGHT
        chars.append(0x2555)  #SF220000	BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
        chars.append(0x2556)  #SF210000	BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
        chars.append(0x2557)  #SF250000	BOX DRAWINGS DOUBLE DOWN AND LEFT
        chars.append(0x2558)  #SF500000	BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
        chars.append(0x2559)  #SF490000	BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
        chars.append(0x255A)  #SF380000	BOX DRAWINGS DOUBLE UP AND RIGHT
        chars.append(0x255B)  #SF280000	BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
        chars.append(0x255C)  #SF270000	BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
        chars.append(0x255D)  #SF260000	BOX DRAWINGS DOUBLE UP AND LEFT
        chars.append(0x255E)  #SF360000	BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
        chars.append(0x255F)  #SF370000	BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
        chars.append(0x2560)  #SF420000	BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
        chars.append(0x2561)  #SF190000	BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
        chars.append(0x2562)  #SF200000	BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
        chars.append(0x2563)  #SF230000	BOX DRAWINGS DOUBLE VERTICAL AND LEFT
        chars.append(0x2564)  #SF470000	BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x2565)  #SF480000	BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x2566)  #SF410000	BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
        chars.append(0x2567)  #SF450000	BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x2568)  #SF460000	BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x2569)  #SF400000	BOX DRAWINGS DOUBLE UP AND HORIZONTAL
        chars.append(0x256A)  #SF540000	BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
        chars.append(0x256B)  #SF530000	BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
        chars.append(0x256C)  #SF440000	BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
        chars.append(0x256D)  #uni256D	BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
        chars.append(0x256E)  #uni256E	BOX DRAWINGS LIGHT ARC DOWN AND LEFT
        chars.append(0x256F)  #uni256F	BOX DRAWINGS LIGHT ARC UP AND LEFT
        chars.append(0x2570)  #uni2570	BOX DRAWINGS LIGHT ARC UP AND RIGHT
        chars.append(0x2571)  #uni2571	BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
        chars.append(0x2572)  #uni2572	BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
        chars.append(0x2573)  #uni2573	BOX DRAWINGS LIGHT DIAGONAL CROSS
        chars.append(0x2574)  #uni2574	BOX DRAWINGS LIGHT LEFT
        chars.append(0x2575)  #uni2575	BOX DRAWINGS LIGHT UP
        chars.append(0x2576)  #uni2576	BOX DRAWINGS LIGHT RIGHT
        chars.append(0x2577)  #uni2577	BOX DRAWINGS LIGHT DOWN
        chars.append(0x2578)  #uni2578	BOX DRAWINGS HEAVY LEFT
        chars.append(0x2579)  #uni2579	BOX DRAWINGS HEAVY UP
        chars.append(0x257A)  #uni257A	BOX DRAWINGS HEAVY RIGHT
        chars.append(0x257B)  #uni257B	BOX DRAWINGS HEAVY DOWN
        chars.append(0x257C)  #uni257C	BOX DRAWINGS LIGHT LEFT AND HEAVY RIGHT
        chars.append(0x257D)  #uni257D	BOX DRAWINGS LIGHT UP AND HEAVY DOWN
        chars.append(0x257E)  #uni257E	BOX DRAWINGS HEAVY LEFT AND LIGHT RIGHT
        chars.append(0x257F)  #uni257F	BOX DRAWINGS HEAVY UP AND LIGHT DOWN
        chars.append(0x2580)  #upblock	UPPER HALF BLOCK
        chars.append(0x2581)  #uni2581	LOWER ONE EIGHTH BLOCK
        chars.append(0x2582)  #uni2582	LOWER ONE QUARTER BLOCK
        chars.append(0x2583)  #uni2583	LOWER THREE EIGHTHS BLOCK
        chars.append(0x2584)  #dnblock	LOWER HALF BLOCK
        chars.append(0x2585)  #uni2585	LOWER FIVE EIGHTHS BLOCK
        chars.append(0x2586)  #uni2586	LOWER THREE QUARTERS BLOCK
        chars.append(0x2587)  #uni2587	LOWER SEVEN EIGHTHS BLOCK
        chars.append(0x2588)  #block	FULL BLOCK
        chars.append(0x2589)  #uni2589	LEFT SEVEN EIGHTHS BLOCK
        chars.append(0x258A)  #uni258A	LEFT THREE QUARTERS BLOCK
        chars.append(0x258B)  #uni258B	LEFT FIVE EIGHTHS BLOCK
        chars.append(0x258C)  #lfblock	LEFT HALF BLOCK
        chars.append(0x258D)  #uni258D	LEFT THREE EIGHTHS BLOCK
        chars.append(0x258E)  #uni258E	LEFT ONE QUARTER BLOCK
        chars.append(0x258F)  #uni258F	LEFT ONE EIGHTH BLOCK
        chars.append(0x2590)  #rtblock	RIGHT HALF BLOCK
        chars.append(0x2591)  #ltshade	LIGHT SHADE
        chars.append(0x2592)  #shade	MEDIUM SHADE
        chars.append(0x2593)  #dkshade	DARK SHADE
        chars.append(0x2594)  #uni2594	UPPER ONE EIGHTH BLOCK
        chars.append(0x2595)  #uni2595	RIGHT ONE EIGHTH BLOCK
        chars.append(0x2596)  #uni2596	QUADRANT LOWER LEFT
        chars.append(0x2597)  #uni2597	QUADRANT LOWER RIGHT
        chars.append(0x2598)  #uni2598	QUADRANT UPPER LEFT
        chars.append(0x2599)  #uni2599	QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT
        chars.append(0x259A)  #uni259A	QUADRANT UPPER LEFT AND LOWER RIGHT
        chars.append(0x259B)  #uni259B	QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT
        chars.append(0x259C)  #uni259C	QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT
        chars.append(0x259D)  #uni259D	QUADRANT UPPER RIGHT
        chars.append(0x259E)  #uni259E	QUADRANT UPPER RIGHT AND LOWER LEFT
        chars.append(0x259F)  #uni259F	QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT
        chars.append(0x25A0)  #filledbox	BLACK SQUARE
        chars.append(0x25A1)  #H22073	WHITE SQUARE
        chars.append(0x25A2)  #uni25A2	WHITE SQUARE WITH ROUNDED CORNERS
        chars.append(0x25A3)  #uni25A3	WHITE SQUARE CONTAINING BLACK SMALL SQUARE
        chars.append(0x25A4)  #uni25A4	SQUARE WITH HORIZONTAL FILL
        chars.append(0x25A5)  #uni25A5	SQUARE WITH VERTICAL FILL
        chars.append(0x25A6)  #uni25A6	SQUARE WITH ORTHOGONAL CROSSHATCH FILL
        chars.append(0x25A7)  #uni25A7	SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL
        chars.append(0x25A8)  #uni25A8	SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL
        chars.append(0x25A9)  #uni25A9	SQUARE WITH DIAGONAL CROSSHATCH FILL
        chars.append(0x25AA)  #H18543	BLACK SMALL SQUARE
        chars.append(0x25AB)  #H18551	WHITE SMALL SQUARE
        chars.append(0x25AC)  #filledrect	BLACK RECTANGLE
        chars.append(0x25AD)  #uni25AD	WHITE RECTANGLE
        chars.append(0x25AE)  #uni25AE	BLACK VERTICAL RECTANGLE
        chars.append(0x25AF)  #uni25AF	WHITE VERTICAL RECTANGLE
        chars.append(0x25B0)  #uni25B0	BLACK PARALLELOGRAM
        chars.append(0x25B1)  #uni25B1	WHITE PARALLELOGRAM
        chars.append(0x25B2)  #triagup	BLACK UP-POINTING TRIANGLE
        chars.append(0x25B3)  #uni25B3	WHITE UP-POINTING TRIANGLE
        chars.append(0x25B4)  #uni25B4	BLACK UP-POINTING SMALL TRIANGLE
        chars.append(0x25B5)  #uni25B5	WHITE UP-POINTING SMALL TRIANGLE
        chars.append(0x25B6)  #uni25B6	BLACK RIGHT-POINTING TRIANGLE
        chars.append(0x25B7)  #uni25B7	WHITE RIGHT-POINTING TRIANGLE
        chars.append(0x25B8)  #uni25B8	BLACK RIGHT-POINTING SMALL TRIANGLE
        chars.append(0x25B9)  #uni25B9	WHITE RIGHT-POINTING SMALL TRIANGLE
        chars.append(0x25BA)  #triagrt	BLACK RIGHT-POINTING POINTER
        chars.append(0x25BB)  #uni25BB	WHITE RIGHT-POINTING POINTER
        chars.append(0x25BC)  #triagdn	BLACK DOWN-POINTING TRIANGLE
        chars.append(0x25BD)  #uni25BD	WHITE DOWN-POINTING TRIANGLE
        chars.append(0x25BE)  #uni25BE	BLACK DOWN-POINTING SMALL TRIANGLE
        chars.append(0x25BF)  #uni25BF	WHITE DOWN-POINTING SMALL TRIANGLE
        chars.append(0x25C0)  #uni25C0	BLACK LEFT-POINTING TRIANGLE
        chars.append(0x25C1)  #uni25C1	WHITE LEFT-POINTING TRIANGLE
        chars.append(0x25C2)  #uni25C2	BLACK LEFT-POINTING SMALL TRIANGLE
        chars.append(0x25C3)  #uni25C3	WHITE LEFT-POINTING SMALL TRIANGLE
        chars.append(0x25C4)  #triaglf	BLACK LEFT-POINTING POINTER
        chars.append(0x25C5)  #uni25C5	WHITE LEFT-POINTING POINTER
        chars.append(0x25C6)  #uni25C6	BLACK DIAMOND
        chars.append(0x25C7)  #uni25C7	WHITE DIAMOND
        chars.append(0x25C8)  #uni25C8	WHITE DIAMOND CONTAINING BLACK SMALL DIAMOND
        chars.append(0x25C9)  #uni25C9	FISHEYE
        chars.append(0x25CA)  #lozenge	LOZENGE
        chars.append(0x25CB)  #circle	WHITE CIRCLE
        chars.append(0x25CC)  #uni25CC	DOTTED CIRCLE
        chars.append(0x25CD)  #uni25CD	CIRCLE WITH VERTICAL FILL
        chars.append(0x25CE)  #uni25CE	BULLSEYE
        chars.append(0x25CF)  #H18533	BLACK CIRCLE
        chars.append(0x25D0)  #uni25D0	CIRCLE WITH LEFT HALF BLACK
        chars.append(0x25D1)  #uni25D1	CIRCLE WITH RIGHT HALF BLACK
        chars.append(0x25D2)  #uni25D2	CIRCLE WITH LOWER HALF BLACK
        chars.append(0x25D3)  #uni25D3	CIRCLE WITH UPPER HALF BLACK
        chars.append(0x25D4)  #uni25D4	CIRCLE WITH UPPER RIGHT QUADRANT BLACK
        chars.append(0x25D5)  #uni25D5	CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK
        chars.append(0x25D6)  #uni25D6	LEFT HALF BLACK CIRCLE
        chars.append(0x25D7)  #uni25D7	RIGHT HALF BLACK CIRCLE
        chars.append(0x25D8)  #invbullet	INVERSE BULLET
        chars.append(0x25D9)  #invcircle	INVERSE WHITE CIRCLE
        chars.append(0x25DA)  #uni25DA	UPPER HALF INVERSE WHITE CIRCLE
        chars.append(0x25DB)  #uni25DB	LOWER HALF INVERSE WHITE CIRCLE
        chars.append(0x25DC)  #uni25DC	UPPER LEFT QUADRANT CIRCULAR ARC
        chars.append(0x25DD)  #uni25DD	UPPER RIGHT QUADRANT CIRCULAR ARC
        chars.append(0x25DE)  #uni25DE	LOWER RIGHT QUADRANT CIRCULAR ARC
        chars.append(0x25DF)  #uni25DF	LOWER LEFT QUADRANT CIRCULAR ARC
        chars.append(0x25E0)  #uni25E0	UPPER HALF CIRCLE
        chars.append(0x25E1)  #uni25E1	LOWER HALF CIRCLE
        chars.append(0x25E2)  #uni25E2	BLACK LOWER RIGHT TRIANGLE
        chars.append(0x25E3)  #uni25E3	BLACK LOWER LEFT TRIANGLE
        chars.append(0x25E4)  #uni25E4	BLACK UPPER LEFT TRIANGLE
        chars.append(0x25E5)  #uni25E5	BLACK UPPER RIGHT TRIANGLE
        chars.append(0x25E6)  #openbullet	WHITE BULLET
        chars.append(0x25E7)  #uni25E7	SQUARE WITH LEFT HALF BLACK
        chars.append(0x25E8)  #uni25E8	SQUARE WITH RIGHT HALF BLACK
        chars.append(0x25E9)  #uni25E9	SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK
        chars.append(0x25EA)  #uni25EA	SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK
        chars.append(0x25EB)  #uni25EB	WHITE SQUARE WITH VERTICAL BISECTING LINE
        chars.append(0x25EC)  #uni25EC	WHITE UP-POINTING TRIANGLE WITH DOT
        chars.append(0x25ED)  #uni25ED	UP-POINTING TRIANGLE WITH LEFT HALF BLACK
        chars.append(0x25EE)  #uni25EE	UP-POINTING TRIANGLE WITH RIGHT HALF BLACK
        chars.append(0x25EF)  #uni25EF	LARGE CIRCLE
        chars.append(0x25F0)  #uni25F0	WHITE SQUARE WITH UPPER LEFT QUADRANT
        chars.append(0x25F1)  #uni25F1	WHITE SQUARE WITH LOWER LEFT QUADRANT
        chars.append(0x25F2)  #uni25F2	WHITE SQUARE WITH LOWER RIGHT QUADRANT
        chars.append(0x25F3)  #uni25F3	WHITE SQUARE WITH UPPER RIGHT QUADRANT
        chars.append(0x25F4)  #uni25F4	WHITE CIRCLE WITH UPPER LEFT QUADRANT
        chars.append(0x25F5)  #uni25F5	WHITE CIRCLE WITH LOWER LEFT QUADRANT
        chars.append(0x25F6)  #uni25F6	WHITE CIRCLE WITH LOWER RIGHT QUADRANT
        chars.append(0x25F7)  #uni25F7	WHITE CIRCLE WITH UPPER RIGHT QUADRANT
        chars.append(0x25F8)  #uni25F8	UPPER LEFT TRIANGLE
        chars.append(0x25F9)  #uni25F9	UPPER RIGHT TRIANGLE
        chars.append(0x25FA)  #uni25FA	LOWER LEFT TRIANGLE
        chars.append(0x25FB)  #uni25FB	WHITE MEDIUM SQUARE
        chars.append(0x25FC)  #uni25FC	BLACK MEDIUM SQUARE
        chars.append(0x25FD)  #uni25FD	WHITE MEDIUM SMALL SQUARE
        chars.append(0x25FE)  #uni25FE	BLACK MEDIUM SMALL SQUARE
        chars.append(0x25FF)  #uni25FF	LOWER RIGHT TRIANGLE
        chars.append(0x2600)  #uni2600	BLACK SUN WITH RAYS
        chars.append(0x2601)  #uni2601	CLOUD
        chars.append(0x2602)  #uni2602	UMBRELLA
        chars.append(0x2603)  #uni2603	SNOWMAN
        chars.append(0x2604)  #uni2604	COMET
        chars.append(0x2605)  #uni2605	BLACK STAR
        chars.append(0x2606)  #uni2606	WHITE STAR
        chars.append(0x2607)  #uni2607	LIGHTNING
        chars.append(0x2608)  #uni2608	THUNDERSTORM
        chars.append(0x2609)  #uni2609	SUN
        chars.append(0x260A)  #uni260A	ASCENDING NODE
        chars.append(0x260B)  #uni260B	DESCENDING NODE
        chars.append(0x260C)  #uni260C	CONJUNCTION
        chars.append(0x260D)  #uni260D	OPPOSITION
        chars.append(0x260E)  #uni260E	BLACK TELEPHONE
        chars.append(0x260F)  #uni260F	WHITE TELEPHONE
        chars.append(0x2610)  #uni2610	BALLOT BOX
        chars.append(0x2611)  #uni2611	BALLOT BOX WITH CHECK
        chars.append(0x2612)  #uni2612	BALLOT BOX WITH X
        chars.append(0x2613)  #uni2613	SALTIRE
        chars.append(0x2614)  #uni2614	UMBRELLA WITH RAIN DROPS
        chars.append(0x2615)  #uni2615	HOT BEVERAGE
        chars.append(0x2616)  #uni2616	WHITE SHOGI PIECE
        chars.append(0x2617)  #uni2617	BLACK SHOGI PIECE
        chars.append(0x2618)  #uni2618	SHAMROCK
        chars.append(0x2619)  #uni2619	REVERSED ROTATED FLORAL HEART BULLET
        chars.append(0x261A)  #uni261A	BLACK LEFT POINTING INDEX
        chars.append(0x261B)  #uni261B	BLACK RIGHT POINTING INDEX
        chars.append(0x261C)  #uni261C	WHITE LEFT POINTING INDEX
        chars.append(0x261D)  #uni261D	WHITE UP POINTING INDEX
        chars.append(0x261E)  #uni261E	WHITE RIGHT POINTING INDEX
        chars.append(0x261F)  #uni261F	WHITE DOWN POINTING INDEX
        chars.append(0x2620)  #uni2620	SKULL AND CROSSBONES
        chars.append(0x2621)  #uni2621	CAUTION SIGN
        chars.append(0x2622)  #uni2622	RADIOACTIVE SIGN
        chars.append(0x2623)  #uni2623	BIOHAZARD SIGN
        chars.append(0x2624)  #uni2624	CADUCEUS
        chars.append(0x2625)  #uni2625	ANKH
        chars.append(0x2626)  #uni2626	ORTHODOX CROSS
        chars.append(0x2627)  #uni2627	CHI RHO
        chars.append(0x2628)  #uni2628	CROSS OF LORRAINE
        chars.append(0x2629)  #uni2629	CROSS OF JERUSALEM
        chars.append(0x262A)  #uni262A	STAR AND CRESCENT
        chars.append(0x262B)  #uni262B	FARSI SYMBOL
        chars.append(0x262C)  #uni262C	ADI SHAKTI
        chars.append(0x262D)  #uni262D	HAMMER AND SICKLE
        chars.append(0x262E)  #uni262E	PEACE SYMBOL
        chars.append(0x262F)  #uni262F	YIN YANG
        chars.append(0x2630)  #uni2630	TRIGRAM FOR HEAVEN
        chars.append(0x2631)  #uni2631	TRIGRAM FOR LAKE
        chars.append(0x2632)  #uni2632	TRIGRAM FOR FIRE
        chars.append(0x2633)  #uni2633	TRIGRAM FOR THUNDER
        chars.append(0x2634)  #uni2634	TRIGRAM FOR WIND
        chars.append(0x2635)  #uni2635	TRIGRAM FOR WATER
        chars.append(0x2636)  #uni2636	TRIGRAM FOR MOUNTAIN
        chars.append(0x2637)  #uni2637	TRIGRAM FOR EARTH
        chars.append(0x2638)  #uni2638	WHEEL OF DHARMA
        chars.append(0x2639)  #uni2639	WHITE FROWNING FACE
        chars.append(0x263A)  #smileface	WHITE SMILING FACE
        chars.append(0x263B)  #invsmileface	BLACK SMILING FACE
        chars.append(0x263C)  #sun	WHITE SUN WITH RAYS
        chars.append(0x263D)  #uni263D	FIRST QUARTER MOON
        chars.append(0x263E)  #uni263E	LAST QUARTER MOON
        chars.append(0x263F)  #uni263F	MERCURY
        chars.append(0x2640)  #female	FEMALE SIGN
        chars.append(0x2641)  #uni2641	EARTH
        chars.append(0x2642)  #male	MALE SIGN
        chars.append(0x2643)  #uni2643	JUPITER
        chars.append(0x2644)  #uni2644	SATURN
        chars.append(0x2645)  #uni2645	URANUS
        chars.append(0x2646)  #uni2646	NEPTUNE
        chars.append(0x2647)  #uni2647	PLUTO
        chars.append(0x2648)  #uni2648	ARIES
        chars.append(0x2649)  #uni2649	TAURUS
        chars.append(0x264A)  #uni264A	GEMINI
        chars.append(0x264B)  #uni264B	CANCER
        chars.append(0x264C)  #uni264C	LEO
        chars.append(0x264D)  #uni264D	VIRGO
        chars.append(0x264E)  #uni264E	LIBRA
        chars.append(0x264F)  #uni264F	SCORPIUS
        chars.append(0x2650)  #uni2650	SAGITTARIUS
        chars.append(0x2651)  #uni2651	CAPRICORN
        chars.append(0x2652)  #uni2652	AQUARIUS
        chars.append(0x2653)  #uni2653	PISCES
        chars.append(0x2654)  #uni2654	WHITE CHESS KING
        chars.append(0x2655)  #uni2655	WHITE CHESS QUEEN
        chars.append(0x2656)  #uni2656	WHITE CHESS ROOK
        chars.append(0x2657)  #uni2657	WHITE CHESS BISHOP
        chars.append(0x2658)  #uni2658	WHITE CHESS KNIGHT
        chars.append(0x2659)  #uni2659	WHITE CHESS PAWN
        chars.append(0x265A)  #uni265A	BLACK CHESS KING
        chars.append(0x265B)  #uni265B	BLACK CHESS QUEEN
        chars.append(0x265C)  #uni265C	BLACK CHESS ROOK
        chars.append(0x265D)  #uni265D	BLACK CHESS BISHOP
        chars.append(0x265E)  #uni265E	BLACK CHESS KNIGHT
        chars.append(0x265F)  #uni265F	BLACK CHESS PAWN
        chars.append(0x2660)  #spade	BLACK SPADE SUIT
        chars.append(0x2661)  #uni2661	WHITE HEART SUIT
        chars.append(0x2662)  #uni2662	WHITE DIAMOND SUIT
        chars.append(0x2663)  #club	BLACK CLUB SUIT
        chars.append(0x2664)  #uni2664	WHITE SPADE SUIT
        chars.append(0x2665)  #heart	BLACK HEART SUIT
        chars.append(0x2666)  #diamond	BLACK DIAMOND SUIT
        chars.append(0x2667)  #uni2667	WHITE CLUB SUIT
        chars.append(0x2668)  #uni2668	HOT SPRINGS
        chars.append(0x2669)  #uni2669	QUARTER NOTE
        chars.append(0x266A)  #musicalnote	EIGHTH NOTE
        chars.append(0x266B)  #musicalnotedbl	BEAMED EIGHTH NOTES
        chars.append(0x266C)  #uni266C	BEAMED SIXTEENTH NOTES
        chars.append(0x266D)  #uni266D	MUSIC FLAT SIGN
        chars.append(0x266E)  #uni266E	MUSIC NATURAL SIGN
        chars.append(0x266F)  #uni266F	MUSIC SHARP SIGN
        chars.append(0x2670)  #uni2670	WEST SYRIAC CROSS
        chars.append(0x2671)  #uni2671	EAST SYRIAC CROSS
        chars.append(0x2672)  #uni2672	UNIVERSAL RECYCLING SYMBOL
        chars.append(0x2673)  #uni2673	RECYCLING SYMBOL FOR TYPE-1 PLASTICS
        chars.append(0x2674)  #uni2674	RECYCLING SYMBOL FOR TYPE-2 PLASTICS
        chars.append(0x2675)  #uni2675	RECYCLING SYMBOL FOR TYPE-3 PLASTICS
        chars.append(0x2676)  #uni2676	RECYCLING SYMBOL FOR TYPE-4 PLASTICS
        chars.append(0x2677)  #uni2677	RECYCLING SYMBOL FOR TYPE-5 PLASTICS
        chars.append(0x2678)  #uni2678	RECYCLING SYMBOL FOR TYPE-6 PLASTICS
        chars.append(0x2679)  #uni2679	RECYCLING SYMBOL FOR TYPE-7 PLASTICS
        chars.append(0x267A)  #uni267A	RECYCLING SYMBOL FOR GENERIC MATERIALS
        chars.append(0x267B)  #uni267B	BLACK UNIVERSAL RECYCLING SYMBOL
        chars.append(0x267C)  #uni267C	RECYCLED PAPER SYMBOL
        chars.append(0x267D)  #uni267D	PARTIALLY-RECYCLED PAPER SYMBOL
        chars.append(0x267E)  #uni267E	PERMANENT PAPER SIGN
        chars.append(0x267F)  #uni267F	WHEELCHAIR SYMBOL
        chars.append(0x2680)  #uni2680	DIE FACE-1
        chars.append(0x2681)  #uni2681	DIE FACE-2
        chars.append(0x2682)  #uni2682	DIE FACE-3
        chars.append(0x2683)  #uni2683	DIE FACE-4
        chars.append(0x2684)  #uni2684	DIE FACE-5
        chars.append(0x2685)  #uni2685	DIE FACE-6
        chars.append(0x2686)  #uni2686	WHITE CIRCLE WITH DOT RIGHT
        chars.append(0x2687)  #uni2687	WHITE CIRCLE WITH TWO DOTS
        chars.append(0x2688)  #uni2688	BLACK CIRCLE WITH WHITE DOT RIGHT
        chars.append(0x2689)  #uni2689	BLACK CIRCLE WITH TWO WHITE DOTS
        chars.append(0x268A)  #uni268A	MONOGRAM FOR YANG
        chars.append(0x268B)  #uni268B	MONOGRAM FOR YIN
        chars.append(0x268C)  #uni268C	DIGRAM FOR GREATER YANG
        chars.append(0x268D)  #uni268D	DIGRAM FOR LESSER YIN
        chars.append(0x268E)  #uni268E	DIGRAM FOR LESSER YANG
        chars.append(0x268F)  #uni268F	DIGRAM FOR GREATER YIN
        chars.append(0x2690)  #uni2690	WHITE FLAG
        chars.append(0x2691)  #uni2691	BLACK FLAG
        chars.append(0x2692)  #uni2692	HAMMER AND PICK
        chars.append(0x2693)  #uni2693	ANCHOR
        chars.append(0x2694)  #uni2694	CROSSED SWORDS
        chars.append(0x2695)  #uni2695	STAFF OF AESCULAPIUS
        chars.append(0x2696)  #uni2696	SCALES
        chars.append(0x2697)  #uni2697	ALEMBIC
        chars.append(0x2698)  #uni2698	FLOWER
        chars.append(0x2699)  #uni2699	GEAR
        chars.append(0x269A)  #uni269A	STAFF OF HERMES
        chars.append(0x269B)  #uni269B	ATOM SYMBOL
        chars.append(0x269C)  #uni269C	FLEUR-DE-LIS
        chars.append(0x269D)  #uni269D	OUTLINED WHITE STAR
        chars.append(0x269E)  #uni269E	THREE LINES CONVERGING RIGHT
        chars.append(0x269F)  #uni269F	THREE LINES CONVERGING LEFT
        chars.append(0x26A0)  #uni26A0	WARNING SIGN
        chars.append(0x26A1)  #uni26A1	HIGH VOLTAGE SIGN
        chars.append(0x26A2)  #uni26A2	DOUBLED FEMALE SIGN
        chars.append(0x26A3)  #uni26A3	DOUBLED MALE SIGN
        chars.append(0x26A4)  #uni26A4	INTERLOCKED FEMALE AND MALE SIGN
        chars.append(0x26A5)  #uni26A5	MALE AND FEMALE SIGN
        chars.append(0x26A6)  #uni26A6	MALE WITH STROKE SIGN
        chars.append(0x26A7)  #uni26A7	MALE WITH STROKE AND MALE AND FEMALE SIGN
        chars.append(0x26A8)  #uni26A8	VERTICAL MALE WITH STROKE SIGN
        chars.append(0x26A9)  #uni26A9	HORIZONTAL MALE WITH STROKE SIGN
        chars.append(0x26AA)  #uni26AA	MEDIUM WHITE CIRCLE
        chars.append(0x26AB)  #uni26AB	MEDIUM BLACK CIRCLE
        chars.append(0x26AC)  #uni26AC	MEDIUM SMALL WHITE CIRCLE
        chars.append(0x26AD)  #uni26AD	MARRIAGE SYMBOL
        chars.append(0x26AE)  #uni26AE	DIVORCE SYMBOL
        chars.append(0x26AF)  #uni26AF	UNMARRIED PARTNERSHIP SYMBOL
        chars.append(0x26B0)  #uni26B0	COFFIN
        chars.append(0x26B1)  #uni26B1	FUNERAL URN
        chars.append(0x26B2)  #uni26B2	NEUTER
        chars.append(0x26B3)  #uni26B3	CERES
        chars.append(0x26B4)  #uni26B4	PALLAS
        chars.append(0x26B5)  #uni26B5	JUNO
        chars.append(0x26B6)  #uni26B6	VESTA
        chars.append(0x26B7)  #uni26B7	CHIRON
        chars.append(0x26B8)  #uni26B8	BLACK MOON LILITH
        chars.append(0x26B9)  #uni26B9	SEXTILE
        chars.append(0x26BA)  #uni26BA	SEMISEXTILE
        chars.append(0x26BB)  #uni26BB	QUINCUNX
        chars.append(0x26BC)  #uni26BC	SESQUIQUADRATE
        chars.append(0x26BD)  #uni26BD	SOCCER BALL
        chars.append(0x26BE)  #uni26BE	BASEBALL
        chars.append(0x26BF)  #uni26BF	SQUARED KEY
        chars.append(0x26C0)  #uni26C0	WHITE DRAUGHTS MAN
        chars.append(0x26C1)  #uni26C1	WHITE DRAUGHTS KING
        chars.append(0x26C2)  #uni26C2	BLACK DRAUGHTS MAN
        chars.append(0x26C3)  #uni26C3	BLACK DRAUGHTS KING
        chars.append(0x26C4)  #uni26C4	SNOWMAN WITHOUT SNOW
        chars.append(0x26C5)  #uni26C5	SUN BEHIND CLOUD
        chars.append(0x26C6)  #uni26C6	RAIN
        chars.append(0x26C7)  #uni26C7	BLACK SNOWMAN
        chars.append(0x26C8)  #uni26C8	THUNDER CLOUD AND RAIN
        chars.append(0x26C9)  #uni26C9	TURNED WHITE SHOGI PIECE
        chars.append(0x26CA)  #uni26CA	TURNED BLACK SHOGI PIECE
        chars.append(0x26CB)  #uni26CB	WHITE DIAMOND IN SQUARE
        chars.append(0x26CC)  #uni26CC	CROSSING LANES
        chars.append(0x26CD)  #uni26CD	DISABLED CAR
        chars.append(0x26CE)  #uni26CE	????
        chars.append(0x26CF)  #uni26CF	PICK
        chars.append(0x26D0)  #uni26D0	CAR SLIDING
        chars.append(0x26D1)  #uni26D1	HELMET WITH WHITE CROSS
        chars.append(0x26D2)  #uni26D2	CIRCLED CROSSING LANES
        chars.append(0x26D3)  #uni26D3	CHAINS
        chars.append(0x26D4)  #uni26D4	NO ENTRY
        chars.append(0x26D5)  #uni26D5	ALTERNATE ONE-WAY LEFT WAY TRAFFIC
        chars.append(0x26D6)  #uni26D6	BLACK TWO-WAY LEFT WAY TRAFFIC
        chars.append(0x26D7)  #uni26D7	WHITE TWO-WAY LEFT WAY TRAFFIC
        chars.append(0x26D8)  #uni26D8	BLACK LEFT LANE MERGE
        chars.append(0x26D9)  #uni26D9	WHITE LEFT LANE MERGE
        chars.append(0x26DA)  #uni26DA	DRIVE SLOW SIGN
        chars.append(0x26DB)  #uni26DB	HEAVY WHITE DOWN-POINTING TRIANGLE
        chars.append(0x26DC)  #uni26DC	LEFT CLOSED ENTRY
        chars.append(0x26DD)  #uni26DD	SQUARED SALTIRE
        chars.append(0x26DE)  #uni26DE	FALLING DIAGONAL IN WHITE CIRCLE IN BLACK SQUARE
        chars.append(0x26DF)  #uni26DF	BLACK TRUCK
        chars.append(0x26E0)  #uni26E0	RESTRICTED LEFT ENTRY-1
        chars.append(0x26E1)  #uni26E1	RESTRICTED LEFT ENTRY-2
        chars.append(0x26E2)  #uni26E2	????
        chars.append(0x26E3)  #uni26E3	HEAVY CIRCLE WITH STROKE AND TWO DOTS ABOVE
        chars.append(0x26E4)  #uni26E4	????
        chars.append(0x26E5)  #uni26E5	????
        chars.append(0x26E6)  #uni26E6	????
        chars.append(0x26E7)  #uni26E7	????
        chars.append(0x26E8)  #uni26E8	BLACK CROSS ON SHIELD
        chars.append(0x26E9)  #uni26E9	SHINTO SHRINE
        chars.append(0x26EA)  #uni26EA	CHURCH
        chars.append(0x26EB)  #uni26EB	CASTLE
        chars.append(0x26EC)  #uni26EC	HISTORIC SITE
        chars.append(0x26ED)  #uni26ED	GEAR WITHOUT HUB
        chars.append(0x26EE)  #uni26EE	GEAR WITH HANDLES
        chars.append(0x26EF)  #uni26EF	MAP SYMBOL FOR LIGHTHOUSE
        chars.append(0x26F0)  #uni26F0	MOUNTAIN
        chars.append(0x26F1)  #uni26F1	UMBRELLA ON GROUND
        chars.append(0x26F2)  #uni26F2	FOUNTAIN
        chars.append(0x26F3)  #uni26F3	FLAG IN HOLE
        chars.append(0x26F4)  #uni26F4	FERRY
        chars.append(0x26F5)  #uni26F5	SAILBOAT
        chars.append(0x26F6)  #uni26F6	SQUARE FOUR CORNERS
        chars.append(0x26F7)  #uni26F7	SKIER
        chars.append(0x26F8)  #uni26F8	ICE SKATE
        chars.append(0x26F9)  #uni26F9	PERSON WITH BALL
        chars.append(0x26FA)  #uni26FA	TENT
        chars.append(0x26FB)  #uni26FB	JAPANESE BANK SYMBOL
        chars.append(0x26FC)  #uni26FC	HEADSTONE GRAVEYARD SYMBOL
        chars.append(0x26FD)  #uni26FD	FUEL PUMP
        chars.append(0x26FE)  #uni26FE	CUP ON BLACK SQUARE
        chars.append(0x26FF)  #uni26FF	WHITE FLAG WITH HORIZONTAL MIDDLE BLACK STRIPE
        chars.append(0xA700)  #uniA700	MODIFIER LETTER CHINESE TONE YIN PING
        chars.append(0x2701)  #uni2701	UPPER BLADE SCISSORS
        chars.append(0x2702)  #uni2702	BLACK SCISSORS
        chars.append(0x2703)  #uni2703	LOWER BLADE SCISSORS
        chars.append(0x2704)  #uni2704	WHITE SCISSORS
        chars.append(0x2705)  #uni2705	????
        chars.append(0x2706)  #uni2706	TELEPHONE LOCATION SIGN
        chars.append(0x2707)  #uni2707	TAPE DRIVE
        chars.append(0x2708)  #uni2708	AIRPLANE
        chars.append(0x2709)  #uni2709	ENVELOPE
        chars.append(0x270A)  #uni270A	????
        chars.append(0x270B)  #uni270B	????
        chars.append(0x270C)  #uni270C	VICTORY HAND
        chars.append(0x270D)  #uni270D	WRITING HAND
        chars.append(0x270E)  #uni270E	LOWER RIGHT PENCIL
        chars.append(0x270F)  #uni270F	PENCIL
        chars.append(0x2710)  #uni2710	UPPER RIGHT PENCIL
        chars.append(0x2711)  #uni2711	WHITE NIB
        chars.append(0x2712)  #uni2712	BLACK NIB
        chars.append(0x2713)  #uni2713	CHECK MARK
        chars.append(0x2714)  #uni2714	HEAVY CHECK MARK
        chars.append(0x2715)  #uni2715	MULTIPLICATION X
        chars.append(0x2716)  #uni2716	HEAVY MULTIPLICATION X
        chars.append(0x2717)  #uni2717	BALLOT X
        chars.append(0x2718)  #uni2718	HEAVY BALLOT X
        chars.append(0x2719)  #uni2719	OUTLINED GREEK CROSS
        chars.append(0x271A)  #uni271A	HEAVY GREEK CROSS
        chars.append(0x271B)  #uni271B	OPEN CENTRE CROSS
        chars.append(0x271C)  #uni271C	HEAVY OPEN CENTRE CROSS
        chars.append(0x271D)  #uni271D	LATIN CROSS
        chars.append(0x271E)  #uni271E	SHADOWED WHITE LATIN CROSS
        chars.append(0x271F)  #uni271F	OUTLINED LATIN CROSS
        chars.append(0x2720)  #uni2720	MALTESE CROSS
        chars.append(0x2721)  #uni2721	STAR OF DAVID
        chars.append(0x2722)  #uni2722	FOUR TEARDROP-SPOKED ASTERISK
        chars.append(0x2723)  #uni2723	FOUR BALLOON-SPOKED ASTERISK
        chars.append(0x2724)  #uni2724	HEAVY FOUR BALLOON-SPOKED ASTERISK
        chars.append(0x2725)  #uni2725	FOUR CLUB-SPOKED ASTERISK
        chars.append(0x2726)  #uni2726	BLACK FOUR POINTED STAR
        chars.append(0x2727)  #uni2727	WHITE FOUR POINTED STAR
        chars.append(0x2728)  #uni2728	????
        chars.append(0x2729)  #uni2729	STRESS OUTLINED WHITE STAR
        chars.append(0x272A)  #uni272A	CIRCLED WHITE STAR
        chars.append(0x272B)  #uni272B	OPEN CENTRE BLACK STAR
        chars.append(0x272C)  #uni272C	BLACK CENTRE WHITE STAR
        chars.append(0x272D)  #uni272D	OUTLINED BLACK STAR
        chars.append(0x272E)  #uni272E	HEAVY OUTLINED BLACK STAR
        chars.append(0x272F)  #uni272F	PINWHEEL STAR
        chars.append(0x2730)  #uni2730	SHADOWED WHITE STAR
        chars.append(0x2731)  #uni2731	HEAVY ASTERISK
        chars.append(0x2732)  #uni2732	OPEN CENTRE ASTERISK
        chars.append(0x2733)  #uni2733	EIGHT SPOKED ASTERISK
        chars.append(0x2734)  #uni2734	EIGHT POINTED BLACK STAR
        chars.append(0x2735)  #uni2735	EIGHT POINTED PINWHEEL STAR
        chars.append(0x2736)  #uni2736	SIX POINTED BLACK STAR
        chars.append(0x2737)  #uni2737	EIGHT POINTED RECTILINEAR BLACK STAR
        chars.append(0x2738)  #uni2738	HEAVY EIGHT POINTED RECTILINEAR BLACK STAR
        chars.append(0x2739)  #uni2739	TWELVE POINTED BLACK STAR
        chars.append(0x273A)  #uni273A	SIXTEEN POINTED ASTERISK
        chars.append(0x273B)  #uni273B	TEARDROP-SPOKED ASTERISK
        chars.append(0x273C)  #uni273C	OPEN CENTRE TEARDROP-SPOKED ASTERISK
        chars.append(0x273D)  #uni273D	HEAVY TEARDROP-SPOKED ASTERISK
        chars.append(0x273E)  #uni273E	SIX PETALLED BLACK AND WHITE FLORETTE
        chars.append(0x273F)  #uni273F	BLACK FLORETTE
        chars.append(0x2740)  #uni2740	WHITE FLORETTE
        chars.append(0x2741)  #uni2741	EIGHT PETALLED OUTLINED BLACK FLORETTE
        chars.append(0x2742)  #uni2742	CIRCLED OPEN CENTRE EIGHT POINTED STAR
        chars.append(0x2743)  #uni2743	HEAVY TEARDROP-SPOKED PINWHEEL ASTERISK
        chars.append(0x2744)  #uni2744	SNOWFLAKE
        chars.append(0x2745)  #uni2745	TIGHT TRIFOLIATE SNOWFLAKE
        chars.append(0x2746)  #uni2746	HEAVY CHEVRON SNOWFLAKE
        chars.append(0x2747)  #uni2747	SPARKLE
        chars.append(0x2748)  #uni2748	HEAVY SPARKLE
        chars.append(0x2749)  #uni2749	BALLOON-SPOKED ASTERISK
        chars.append(0x274A)  #uni274A	EIGHT TEARDROP-SPOKED PROPELLER ASTERISK
        chars.append(0x274B)  #uni274B	HEAVY EIGHT TEARDROP-SPOKED PROPELLER ASTERISK
        chars.append(0x274C)  #uni274C	????
        chars.append(0x274D)  #uni274D	SHADOWED WHITE CIRCLE
        chars.append(0x274E)  #uni274E	????
        chars.append(0x274F)  #uni274F	LOWER RIGHT DROP-SHADOWED WHITE SQUARE
        chars.append(0x2750)  #uni2750	UPPER RIGHT DROP-SHADOWED WHITE SQUARE
        chars.append(0x2751)  #uni2751	LOWER RIGHT SHADOWED WHITE SQUARE
        chars.append(0x2752)  #uni2752	UPPER RIGHT SHADOWED WHITE SQUARE
        chars.append(0x2753)  #uni2753	????
        chars.append(0x2754)  #uni2754	????
        chars.append(0x2755)  #uni2755	????
        chars.append(0x2756)  #uni2756	BLACK DIAMOND MINUS WHITE X
        chars.append(0x2757)  #uni2757	HEAVY EXCLAMATION MARK SYMBOL
        chars.append(0x2758)  #uni2758	LIGHT VERTICAL BAR
        chars.append(0x2759)  #uni2759	MEDIUM VERTICAL BAR
        chars.append(0x275A)  #uni275A	HEAVY VERTICAL BAR
        chars.append(0x275B)  #uni275B	HEAVY SINGLE TURNED COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275C)  #uni275C	HEAVY SINGLE COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275D)  #uni275D	HEAVY DOUBLE TURNED COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275E)  #uni275E	HEAVY DOUBLE COMMA QUOTATION MARK ORNAMENT
        chars.append(0x275F)  #uni275F	????
        chars.append(0x2760)  #uni2760	????
        chars.append(0x2761)  #uni2761	CURVED STEM PARAGRAPH SIGN ORNAMENT
        chars.append(0x2762)  #uni2762	HEAVY EXCLAMATION MARK ORNAMENT
        chars.append(0x2763)  #uni2763	HEAVY HEART EXCLAMATION MARK ORNAMENT
        chars.append(0x2764)  #uni2764	HEAVY BLACK HEART
        chars.append(0x2765)  #uni2765	ROTATED HEAVY BLACK HEART BULLET
        chars.append(0x2766)  #uni2766	FLORAL HEART
        chars.append(0x2767)  #uni2767	ROTATED FLORAL HEART BULLET
        chars.append(0x2768)  #uni2768	MEDIUM LEFT PARENTHESIS ORNAMENT
        chars.append(0x2769)  #uni2769	MEDIUM RIGHT PARENTHESIS ORNAMENT
        chars.append(0x276A)  #uni276A	MEDIUM FLATTENED LEFT PARENTHESIS ORNAMENT
        chars.append(0x276B)  #uni276B	MEDIUM FLATTENED RIGHT PARENTHESIS ORNAMENT
        chars.append(0x276C)  #uni276C	MEDIUM LEFT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x276D)  #uni276D	MEDIUM RIGHT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x276E)  #uni276E	HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT
        chars.append(0x276F)  #uni276F	HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT
        chars.append(0x2770)  #uni2770	HEAVY LEFT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x2771)  #uni2771	HEAVY RIGHT-POINTING ANGLE BRACKET ORNAMENT
        chars.append(0x2772)  #uni2772	LIGHT LEFT TORTOISE SHELL BRACKET ORNAMENT
        chars.append(0x2773)  #uni2773	LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT
        chars.append(0x2774)  #uni2774	MEDIUM LEFT CURLY BRACKET ORNAMENT
        chars.append(0x2775)  #uni2775	MEDIUM RIGHT CURLY BRACKET ORNAMENT
        chars.append(0x2776)  #uni2776	DINGBAT NEGATIVE CIRCLED DIGIT ONE
        chars.append(0x2777)  #uni2777	DINGBAT NEGATIVE CIRCLED DIGIT TWO
        chars.append(0x2778)  #uni2778	DINGBAT NEGATIVE CIRCLED DIGIT THREE
        chars.append(0x2779)  #uni2779	DINGBAT NEGATIVE CIRCLED DIGIT FOUR
        chars.append(0x277A)  #uni277A	DINGBAT NEGATIVE CIRCLED DIGIT FIVE
        chars.append(0x277B)  #uni277B	DINGBAT NEGATIVE CIRCLED DIGIT SIX
        chars.append(0x277C)  #uni277C	DINGBAT NEGATIVE CIRCLED DIGIT SEVEN
        chars.append(0x277D)  #uni277D	DINGBAT NEGATIVE CIRCLED DIGIT EIGHT
        chars.append(0x277E)  #uni277E	DINGBAT NEGATIVE CIRCLED DIGIT NINE
        chars.append(0x277F)  #uni277F	DINGBAT NEGATIVE CIRCLED NUMBER TEN
        chars.append(0x2780)  #uni2780	DINGBAT CIRCLED SANS-SERIF DIGIT ONE
        chars.append(0x2781)  #uni2781	DINGBAT CIRCLED SANS-SERIF DIGIT TWO
        chars.append(0x2782)  #uni2782	DINGBAT CIRCLED SANS-SERIF DIGIT THREE
        chars.append(0x2783)  #uni2783	DINGBAT CIRCLED SANS-SERIF DIGIT FOUR
        chars.append(0x2784)  #uni2784	DINGBAT CIRCLED SANS-SERIF DIGIT FIVE
        chars.append(0x2785)  #uni2785	DINGBAT CIRCLED SANS-SERIF DIGIT SIX
        chars.append(0x2786)  #uni2786	DINGBAT CIRCLED SANS-SERIF DIGIT SEVEN
        chars.append(0x2787)  #uni2787	DINGBAT CIRCLED SANS-SERIF DIGIT EIGHT
        chars.append(0x2788)  #uni2788	DINGBAT CIRCLED SANS-SERIF DIGIT NINE
        chars.append(0x2789)  #uni2789	DINGBAT CIRCLED SANS-SERIF NUMBER TEN
        chars.append(0x278A)  #uni278A	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT ONE
        chars.append(0x278B)  #uni278B	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT TWO
        chars.append(0x278C)  #uni278C	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT THREE
        chars.append(0x278D)  #uni278D	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT FOUR
        chars.append(0x278E)  #uni278E	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT FIVE
        chars.append(0x278F)  #uni278F	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT SIX
        chars.append(0x2790)  #uni2790	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT SEVEN
        chars.append(0x2791)  #uni2791	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT EIGHT
        chars.append(0x2792)  #uni2792	DINGBAT NEGATIVE CIRCLED SANS-SERIF DIGIT NINE
        chars.append(0x2793)  #uni2793	DINGBAT NEGATIVE CIRCLED SANS-SERIF NUMBER TEN
        chars.append(0x2794)  #uni2794	HEAVY WIDE-HEADED RIGHTWARDS ARROW
        chars.append(0x2795)  #uni2795	????
        chars.append(0x2796)  #uni2796	????
        chars.append(0x2797)  #uni2797	????
        chars.append(0x2798)  #uni2798	HEAVY SOUTH EAST ARROW
        chars.append(0x2799)  #uni2799	HEAVY RIGHTWARDS ARROW
        chars.append(0x279A)  #uni279A	HEAVY NORTH EAST ARROW
        chars.append(0x279B)  #uni279B	DRAFTING POINT RIGHTWARDS ARROW
        chars.append(0x279C)  #uni279C	HEAVY ROUND-TIPPED RIGHTWARDS ARROW
        chars.append(0x279D)  #uni279D	TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x279E)  #uni279E	HEAVY TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x279F)  #uni279F	DASHED TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x27A0)  #uni27A0	HEAVY DASHED TRIANGLE-HEADED RIGHTWARDS ARROW
        chars.append(0x27A1)  #uni27A1	BLACK RIGHTWARDS ARROW
        chars.append(0x27A2)  #uni27A2	THREE-D TOP-LIGHTED RIGHTWARDS ARROWHEAD
        chars.append(0x27A3)  #uni27A3	THREE-D BOTTOM-LIGHTED RIGHTWARDS ARROWHEAD
        chars.append(0x27A4)  #uni27A4	BLACK RIGHTWARDS ARROWHEAD
        chars.append(0x27A5)  #uni27A5	HEAVY BLACK CURVED DOWNWARDS AND RIGHTWARDS ARROW
        chars.append(0x27A6)  #uni27A6	HEAVY BLACK CURVED UPWARDS AND RIGHTWARDS ARROW
        chars.append(0x27A7)  #uni27A7	SQUAT BLACK RIGHTWARDS ARROW
        chars.append(0x27A8)  #uni27A8	HEAVY CONCAVE-POINTED BLACK RIGHTWARDS ARROW
        chars.append(0x27A9)  #uni27A9	RIGHT-SHADED WHITE RIGHTWARDS ARROW
        chars.append(0x27AA)  #uni27AA	LEFT-SHADED WHITE RIGHTWARDS ARROW
        chars.append(0x27AB)  #uni27AB	BACK-TILTED SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AC)  #uni27AC	FRONT-TILTED SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AD)  #uni27AD	HEAVY LOWER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AE)  #uni27AE	HEAVY UPPER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27AF)  #uni27AF	NOTCHED LOWER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27B0)  #uni27B0	????
        chars.append(0x27B1)  #uni27B1	NOTCHED UPPER RIGHT-SHADOWED WHITE RIGHTWARDS ARROW
        chars.append(0x27B2)  #uni27B2	CIRCLED HEAVY WHITE RIGHTWARDS ARROW
        chars.append(0x27B3)  #uni27B3	WHITE-FEATHERED RIGHTWARDS ARROW
        chars.append(0x27B4)  #uni27B4	BLACK-FEATHERED SOUTH EAST ARROW
        chars.append(0x27B5)  #uni27B5	BLACK-FEATHERED RIGHTWARDS ARROW
        chars.append(0x27B6)  #uni27B6	BLACK-FEATHERED NORTH EAST ARROW
        chars.append(0x27B7)  #uni27B7	HEAVY BLACK-FEATHERED SOUTH EAST ARROW
        chars.append(0x27B8)  #uni27B8	HEAVY BLACK-FEATHERED RIGHTWARDS ARROW
        chars.append(0x27B9)  #uni27B9	HEAVY BLACK-FEATHERED NORTH EAST ARROW
        chars.append(0x27BA)  #uni27BA	TEARDROP-BARBED RIGHTWARDS ARROW
        chars.append(0x27BB)  #uni27BB	HEAVY TEARDROP-SHANKED RIGHTWARDS ARROW
        chars.append(0x27BC)  #uni27BC	WEDGE-TAILED RIGHTWARDS ARROW
        chars.append(0x27BD)  #uni27BD	HEAVY WEDGE-TAILED RIGHTWARDS ARROW
        chars.append(0x27BE)  #uni27BE	OPEN-OUTLINED RIGHTWARDS ARROW
        chars.append(0x27BF)  #uni27BF	????
        chars.append(0x27C0)  #uni27C0	THREE DIMENSIONAL ANGLE
        chars.append(0x27C1)  #uni27C1	WHITE TRIANGLE CONTAINING SMALL WHITE TRIANGLE
        chars.append(0x27C2)  #uni27C2	PERPENDICULAR
        chars.append(0x27C3)  #uni27C3	OPEN SUBSET
        chars.append(0x27C4)  #uni27C4	OPEN SUPERSET
        chars.append(0x27C5)  #uni27C5	LEFT S-SHAPED BAG DELIMITER
        chars.append(0x27C6)  #uni27C6	RIGHT S-SHAPED BAG DELIMITER
        chars.append(0x27C7)  #uni27C7	OR WITH DOT INSIDE
        chars.append(0x27C8)  #uni27C8	REVERSE SOLIDUS PRECEDING SUBSET
        chars.append(0x27C9)  #uni27C9	SUPERSET PRECEDING SOLIDUS
        chars.append(0x27CA)  #uni27CA	VERTICAL BAR WITH HORIZONTAL STROKE
        chars.append(0x27CB)  #uni27CB	????
        chars.append(0x27CC)  #uni27CC	LONG DIVISION
        chars.append(0x27CD)  #uni27CD	????
        chars.append(0x27CE)  #uni27CE	????
        chars.append(0x27CF)  #uni27CF	????
        chars.append(0x27D0)  #uni27D0	WHITE DIAMOND WITH CENTRED DOT
        chars.append(0x27D1)  #uni27D1	AND WITH DOT
        chars.append(0x27D2)  #uni27D2	ELEMENT OF OPENING UPWARDS
        chars.append(0x27D3)  #uni27D3	LOWER RIGHT CORNER WITH DOT
        chars.append(0x27D4)  #uni27D4	UPPER LEFT CORNER WITH DOT
        chars.append(0x27D5)  #uni27D5	LEFT OUTER JOIN
        chars.append(0x27D6)  #uni27D6	RIGHT OUTER JOIN
        chars.append(0x27D7)  #uni27D7	FULL OUTER JOIN
        chars.append(0x27D8)  #uni27D8	LARGE UP TACK
        chars.append(0x27D9)  #uni27D9	LARGE DOWN TACK
        chars.append(0x27DA)  #uni27DA	LEFT AND RIGHT DOUBLE TURNSTILE
        chars.append(0x27DB)  #uni27DB	LEFT AND RIGHT TACK
        chars.append(0x27DC)  #uni27DC	LEFT MULTIMAP
        chars.append(0x27DD)  #uni27DD	LONG RIGHT TACK
        chars.append(0x27DE)  #uni27DE	LONG LEFT TACK
        chars.append(0x27DF)  #uni27DF	UP TACK WITH CIRCLE ABOVE
        chars.append(0x27E0)  #uni27E0	LOZENGE DIVIDED BY HORIZONTAL RULE
        chars.append(0x27E1)  #uni27E1	WHITE CONCAVE-SIDED DIAMOND
        chars.append(0x27E2)  #uni27E2	WHITE CONCAVE-SIDED DIAMOND WITH LEFTWARDS TICK
        chars.append(0x27E3)  #uni27E3	WHITE CONCAVE-SIDED DIAMOND WITH RIGHTWARDS TICK
        chars.append(0x27E4)  #uni27E4	WHITE SQUARE WITH LEFTWARDS TICK
        chars.append(0x27E5)  #uni27E5	WHITE SQUARE WITH RIGHTWARDS TICK
        chars.append(0x27E6)  #uni27E6	MATHEMATICAL LEFT WHITE SQUARE BRACKET
        chars.append(0x27E7)  #uni27E7	MATHEMATICAL RIGHT WHITE SQUARE BRACKET
        chars.append(0x27E8)  #uni27E8	MATHEMATICAL LEFT ANGLE BRACKET
        chars.append(0x27E9)  #uni27E9	MATHEMATICAL RIGHT ANGLE BRACKET
        chars.append(0x27EA)  #uni27EA	MATHEMATICAL LEFT DOUBLE ANGLE BRACKET
        chars.append(0x27EB)  #uni27EB	MATHEMATICAL RIGHT DOUBLE ANGLE BRACKET
        chars.append(0x27EC)  #uni27EC	MATHEMATICAL LEFT WHITE TORTOISE SHELL BRACKET
        chars.append(0x27ED)  #uni27ED	MATHEMATICAL RIGHT WHITE TORTOISE SHELL BRACKET
        chars.append(0x27EE)  #uni27EE	MATHEMATICAL LEFT FLATTENED PARENTHESIS
        chars.append(0x27EF)  #uni27EF	MATHEMATICAL RIGHT FLATTENED PARENTHESIS
        chars.append(0x27F0)  #uni27F0	UPWARDS QUADRUPLE ARROW
        chars.append(0x27F1)  #uni27F1	DOWNWARDS QUADRUPLE ARROW
        chars.append(0x27F2)  #uni27F2	ANTICLOCKWISE GAPPED CIRCLE ARROW
        chars.append(0x27F3)  #uni27F3	CLOCKWISE GAPPED CIRCLE ARROW
        chars.append(0x27F4)  #uni27F4	RIGHT ARROW WITH CIRCLED PLUS
        chars.append(0x27F5)  #uni27F5	LONG LEFTWARDS ARROW
        chars.append(0x27F6)  #uni27F6	LONG RIGHTWARDS ARROW
        chars.append(0x27F7)  #uni27F7	LONG LEFT RIGHT ARROW
        chars.append(0x27F8)  #uni27F8	LONG LEFTWARDS DOUBLE ARROW
        chars.append(0x27F9)  #uni27F9	LONG RIGHTWARDS DOUBLE ARROW
        chars.append(0x27FA)  #uni27FA	LONG LEFT RIGHT DOUBLE ARROW
        chars.append(0x27FB)  #uni27FB	LONG LEFTWARDS ARROW FROM BAR
        chars.append(0x27FC)  #uni27FC	LONG RIGHTWARDS ARROW FROM BAR
        chars.append(0x27FD)  #uni27FD	LONG LEFTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x27FE)  #uni27FE	LONG RIGHTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x27FF)  #uni27FF	LONG RIGHTWARDS SQUIGGLE ARROW
        chars.append(0x2800)  #uni2800	BRAILLE PATTERN BLANK
        chars.append(0x2801)  #uni2801	BRAILLE PATTERN DOTS-1
        chars.append(0x2802)  #uni2802	BRAILLE PATTERN DOTS-2
        chars.append(0x2803)  #uni2803	BRAILLE PATTERN DOTS-12
        chars.append(0x2804)  #uni2804	BRAILLE PATTERN DOTS-3
        chars.append(0x2805)  #uni2805	BRAILLE PATTERN DOTS-13
        chars.append(0x2806)  #uni2806	BRAILLE PATTERN DOTS-23
        chars.append(0x2807)  #uni2807	BRAILLE PATTERN DOTS-123
        chars.append(0x2808)  #uni2808	BRAILLE PATTERN DOTS-4
        chars.append(0x2809)  #uni2809	BRAILLE PATTERN DOTS-14
        chars.append(0x280A)  #uni280A	BRAILLE PATTERN DOTS-24
        chars.append(0x280B)  #uni280B	BRAILLE PATTERN DOTS-124
        chars.append(0x280C)  #uni280C	BRAILLE PATTERN DOTS-34
        chars.append(0x280D)  #uni280D	BRAILLE PATTERN DOTS-134
        chars.append(0x280E)  #uni280E	BRAILLE PATTERN DOTS-234
        chars.append(0x280F)  #uni280F	BRAILLE PATTERN DOTS-1234
        chars.append(0x2810)  #uni2810	BRAILLE PATTERN DOTS-5
        chars.append(0x2811)  #uni2811	BRAILLE PATTERN DOTS-15
        chars.append(0x2812)  #uni2812	BRAILLE PATTERN DOTS-25
        chars.append(0x2813)  #uni2813	BRAILLE PATTERN DOTS-125
        chars.append(0x2814)  #uni2814	BRAILLE PATTERN DOTS-35
        chars.append(0x2815)  #uni2815	BRAILLE PATTERN DOTS-135
        chars.append(0x2816)  #uni2816	BRAILLE PATTERN DOTS-235
        chars.append(0x2817)  #uni2817	BRAILLE PATTERN DOTS-1235
        chars.append(0x2818)  #uni2818	BRAILLE PATTERN DOTS-45
        chars.append(0x2819)  #uni2819	BRAILLE PATTERN DOTS-145
        chars.append(0x281A)  #uni281A	BRAILLE PATTERN DOTS-245
        chars.append(0x281B)  #uni281B	BRAILLE PATTERN DOTS-1245
        chars.append(0x281C)  #uni281C	BRAILLE PATTERN DOTS-345
        chars.append(0x281D)  #uni281D	BRAILLE PATTERN DOTS-1345
        chars.append(0x281E)  #uni281E	BRAILLE PATTERN DOTS-2345
        chars.append(0x281F)  #uni281F	BRAILLE PATTERN DOTS-12345
        chars.append(0x2820)  #uni2820	BRAILLE PATTERN DOTS-6
        chars.append(0x2821)  #uni2821	BRAILLE PATTERN DOTS-16
        chars.append(0x2822)  #uni2822	BRAILLE PATTERN DOTS-26
        chars.append(0x2823)  #uni2823	BRAILLE PATTERN DOTS-126
        chars.append(0x2824)  #uni2824	BRAILLE PATTERN DOTS-36
        chars.append(0x2825)  #uni2825	BRAILLE PATTERN DOTS-136
        chars.append(0x2826)  #uni2826	BRAILLE PATTERN DOTS-236
        chars.append(0x2827)  #uni2827	BRAILLE PATTERN DOTS-1236
        chars.append(0x2828)  #uni2828	BRAILLE PATTERN DOTS-46
        chars.append(0x2829)  #uni2829	BRAILLE PATTERN DOTS-146
        chars.append(0x282A)  #uni282A	BRAILLE PATTERN DOTS-246
        chars.append(0x282B)  #uni282B	BRAILLE PATTERN DOTS-1246
        chars.append(0x282C)  #uni282C	BRAILLE PATTERN DOTS-346
        chars.append(0x282D)  #uni282D	BRAILLE PATTERN DOTS-1346
        chars.append(0x282E)  #uni282E	BRAILLE PATTERN DOTS-2346
        chars.append(0x282F)  #uni282F	BRAILLE PATTERN DOTS-12346
        chars.append(0x2830)  #uni2830	BRAILLE PATTERN DOTS-56
        chars.append(0x2831)  #uni2831	BRAILLE PATTERN DOTS-156
        chars.append(0x2832)  #uni2832	BRAILLE PATTERN DOTS-256
        chars.append(0x2833)  #uni2833	BRAILLE PATTERN DOTS-1256
        chars.append(0x2834)  #uni2834	BRAILLE PATTERN DOTS-356
        chars.append(0x2835)  #uni2835	BRAILLE PATTERN DOTS-1356
        chars.append(0x2836)  #uni2836	BRAILLE PATTERN DOTS-2356
        chars.append(0x2837)  #uni2837	BRAILLE PATTERN DOTS-12356
        chars.append(0x2838)  #uni2838	BRAILLE PATTERN DOTS-456
        chars.append(0x2839)  #uni2839	BRAILLE PATTERN DOTS-1456
        chars.append(0x283A)  #uni283A	BRAILLE PATTERN DOTS-2456
        chars.append(0x283B)  #uni283B	BRAILLE PATTERN DOTS-12456
        chars.append(0x283C)  #uni283C	BRAILLE PATTERN DOTS-3456
        chars.append(0x283D)  #uni283D	BRAILLE PATTERN DOTS-13456
        chars.append(0x283E)  #uni283E	BRAILLE PATTERN DOTS-23456
        chars.append(0x283F)  #uni283F	BRAILLE PATTERN DOTS-123456
        chars.append(0x2840)  #uni2840	BRAILLE PATTERN DOTS-7
        chars.append(0x2841)  #uni2841	BRAILLE PATTERN DOTS-17
        chars.append(0x2842)  #uni2842	BRAILLE PATTERN DOTS-27
        chars.append(0x2843)  #uni2843	BRAILLE PATTERN DOTS-127
        chars.append(0x2844)  #uni2844	BRAILLE PATTERN DOTS-37
        chars.append(0x2845)  #uni2845	BRAILLE PATTERN DOTS-137
        chars.append(0x2846)  #uni2846	BRAILLE PATTERN DOTS-237
        chars.append(0x2847)  #uni2847	BRAILLE PATTERN DOTS-1237
        chars.append(0x2848)  #uni2848	BRAILLE PATTERN DOTS-47
        chars.append(0x2849)  #uni2849	BRAILLE PATTERN DOTS-147
        chars.append(0x284A)  #uni284A	BRAILLE PATTERN DOTS-247
        chars.append(0x284B)  #uni284B	BRAILLE PATTERN DOTS-1247
        chars.append(0x284C)  #uni284C	BRAILLE PATTERN DOTS-347
        chars.append(0x284D)  #uni284D	BRAILLE PATTERN DOTS-1347
        chars.append(0x284E)  #uni284E	BRAILLE PATTERN DOTS-2347
        chars.append(0x284F)  #uni284F	BRAILLE PATTERN DOTS-12347
        chars.append(0x2850)  #uni2850	BRAILLE PATTERN DOTS-57
        chars.append(0x2851)  #uni2851	BRAILLE PATTERN DOTS-157
        chars.append(0x2852)  #uni2852	BRAILLE PATTERN DOTS-257
        chars.append(0x2853)  #uni2853	BRAILLE PATTERN DOTS-1257
        chars.append(0x2854)  #uni2854	BRAILLE PATTERN DOTS-357
        chars.append(0x2855)  #uni2855	BRAILLE PATTERN DOTS-1357
        chars.append(0x2856)  #uni2856	BRAILLE PATTERN DOTS-2357
        chars.append(0x2857)  #uni2857	BRAILLE PATTERN DOTS-12357
        chars.append(0x2858)  #uni2858	BRAILLE PATTERN DOTS-457
        chars.append(0x2859)  #uni2859	BRAILLE PATTERN DOTS-1457
        chars.append(0x285A)  #uni285A	BRAILLE PATTERN DOTS-2457
        chars.append(0x285B)  #uni285B	BRAILLE PATTERN DOTS-12457
        chars.append(0x285C)  #uni285C	BRAILLE PATTERN DOTS-3457
        chars.append(0x285D)  #uni285D	BRAILLE PATTERN DOTS-13457
        chars.append(0x285E)  #uni285E	BRAILLE PATTERN DOTS-23457
        chars.append(0x285F)  #uni285F	BRAILLE PATTERN DOTS-123457
        chars.append(0x2860)  #uni2860	BRAILLE PATTERN DOTS-67
        chars.append(0x2861)  #uni2861	BRAILLE PATTERN DOTS-167
        chars.append(0x2862)  #uni2862	BRAILLE PATTERN DOTS-267
        chars.append(0x2863)  #uni2863	BRAILLE PATTERN DOTS-1267
        chars.append(0x2864)  #uni2864	BRAILLE PATTERN DOTS-367
        chars.append(0x2865)  #uni2865	BRAILLE PATTERN DOTS-1367
        chars.append(0x2866)  #uni2866	BRAILLE PATTERN DOTS-2367
        chars.append(0x2867)  #uni2867	BRAILLE PATTERN DOTS-12367
        chars.append(0x2868)  #uni2868	BRAILLE PATTERN DOTS-467
        chars.append(0x2869)  #uni2869	BRAILLE PATTERN DOTS-1467
        chars.append(0x286A)  #uni286A	BRAILLE PATTERN DOTS-2467
        chars.append(0x286B)  #uni286B	BRAILLE PATTERN DOTS-12467
        chars.append(0x286C)  #uni286C	BRAILLE PATTERN DOTS-3467
        chars.append(0x286D)  #uni286D	BRAILLE PATTERN DOTS-13467
        chars.append(0x286E)  #uni286E	BRAILLE PATTERN DOTS-23467
        chars.append(0x286F)  #uni286F	BRAILLE PATTERN DOTS-123467
        chars.append(0x2870)  #uni2870	BRAILLE PATTERN DOTS-567
        chars.append(0x2871)  #uni2871	BRAILLE PATTERN DOTS-1567
        chars.append(0x2872)  #uni2872	BRAILLE PATTERN DOTS-2567
        chars.append(0x2873)  #uni2873	BRAILLE PATTERN DOTS-12567
        chars.append(0x2874)  #uni2874	BRAILLE PATTERN DOTS-3567
        chars.append(0x2875)  #uni2875	BRAILLE PATTERN DOTS-13567
        chars.append(0x2876)  #uni2876	BRAILLE PATTERN DOTS-23567
        chars.append(0x2877)  #uni2877	BRAILLE PATTERN DOTS-123567
        chars.append(0x2878)  #uni2878	BRAILLE PATTERN DOTS-4567
        chars.append(0x2879)  #uni2879	BRAILLE PATTERN DOTS-14567
        chars.append(0x287A)  #uni287A	BRAILLE PATTERN DOTS-24567
        chars.append(0x287B)  #uni287B	BRAILLE PATTERN DOTS-124567
        chars.append(0x287C)  #uni287C	BRAILLE PATTERN DOTS-34567
        chars.append(0x287D)  #uni287D	BRAILLE PATTERN DOTS-134567
        chars.append(0x287E)  #uni287E	BRAILLE PATTERN DOTS-234567
        chars.append(0x287F)  #uni287F	BRAILLE PATTERN DOTS-1234567
        chars.append(0x2880)  #uni2880	BRAILLE PATTERN DOTS-8
        chars.append(0x2881)  #uni2881	BRAILLE PATTERN DOTS-18
        chars.append(0x2882)  #uni2882	BRAILLE PATTERN DOTS-28
        chars.append(0x2883)  #uni2883	BRAILLE PATTERN DOTS-128
        chars.append(0x2884)  #uni2884	BRAILLE PATTERN DOTS-38
        chars.append(0x2885)  #uni2885	BRAILLE PATTERN DOTS-138
        chars.append(0x2886)  #uni2886	BRAILLE PATTERN DOTS-238
        chars.append(0x2887)  #uni2887	BRAILLE PATTERN DOTS-1238
        chars.append(0x2888)  #uni2888	BRAILLE PATTERN DOTS-48
        chars.append(0x2889)  #uni2889	BRAILLE PATTERN DOTS-148
        chars.append(0x288A)  #uni288A	BRAILLE PATTERN DOTS-248
        chars.append(0x288B)  #uni288B	BRAILLE PATTERN DOTS-1248
        chars.append(0x288C)  #uni288C	BRAILLE PATTERN DOTS-348
        chars.append(0x288D)  #uni288D	BRAILLE PATTERN DOTS-1348
        chars.append(0x288E)  #uni288E	BRAILLE PATTERN DOTS-2348
        chars.append(0x288F)  #uni288F	BRAILLE PATTERN DOTS-12348
        chars.append(0x2890)  #uni2890	BRAILLE PATTERN DOTS-58
        chars.append(0x2891)  #uni2891	BRAILLE PATTERN DOTS-158
        chars.append(0x2892)  #uni2892	BRAILLE PATTERN DOTS-258
        chars.append(0x2893)  #uni2893	BRAILLE PATTERN DOTS-1258
        chars.append(0x2894)  #uni2894	BRAILLE PATTERN DOTS-358
        chars.append(0x2895)  #uni2895	BRAILLE PATTERN DOTS-1358
        chars.append(0x2896)  #uni2896	BRAILLE PATTERN DOTS-2358
        chars.append(0x2897)  #uni2897	BRAILLE PATTERN DOTS-12358
        chars.append(0x2898)  #uni2898	BRAILLE PATTERN DOTS-458
        chars.append(0x2899)  #uni2899	BRAILLE PATTERN DOTS-1458
        chars.append(0x289A)  #uni289A	BRAILLE PATTERN DOTS-2458
        chars.append(0x289B)  #uni289B	BRAILLE PATTERN DOTS-12458
        chars.append(0x289C)  #uni289C	BRAILLE PATTERN DOTS-3458
        chars.append(0x289D)  #uni289D	BRAILLE PATTERN DOTS-13458
        chars.append(0x289E)  #uni289E	BRAILLE PATTERN DOTS-23458
        chars.append(0x289F)  #uni289F	BRAILLE PATTERN DOTS-123458
        chars.append(0x28A0)  #uni28A0	BRAILLE PATTERN DOTS-68
        chars.append(0x28A1)  #uni28A1	BRAILLE PATTERN DOTS-168
        chars.append(0x28A2)  #uni28A2	BRAILLE PATTERN DOTS-268
        chars.append(0x28A3)  #uni28A3	BRAILLE PATTERN DOTS-1268
        chars.append(0x28A4)  #uni28A4	BRAILLE PATTERN DOTS-368
        chars.append(0x28A5)  #uni28A5	BRAILLE PATTERN DOTS-1368
        chars.append(0x28A6)  #uni28A6	BRAILLE PATTERN DOTS-2368
        chars.append(0x28A7)  #uni28A7	BRAILLE PATTERN DOTS-12368
        chars.append(0x28A8)  #uni28A8	BRAILLE PATTERN DOTS-468
        chars.append(0x28A9)  #uni28A9	BRAILLE PATTERN DOTS-1468
        chars.append(0x28AA)  #uni28AA	BRAILLE PATTERN DOTS-2468
        chars.append(0x28AB)  #uni28AB	BRAILLE PATTERN DOTS-12468
        chars.append(0x28AC)  #uni28AC	BRAILLE PATTERN DOTS-3468
        chars.append(0x28AD)  #uni28AD	BRAILLE PATTERN DOTS-13468
        chars.append(0x28AE)  #uni28AE	BRAILLE PATTERN DOTS-23468
        chars.append(0x28AF)  #uni28AF	BRAILLE PATTERN DOTS-123468
        chars.append(0x28B0)  #uni28B0	BRAILLE PATTERN DOTS-568
        chars.append(0x28B1)  #uni28B1	BRAILLE PATTERN DOTS-1568
        chars.append(0x28B2)  #uni28B2	BRAILLE PATTERN DOTS-2568
        chars.append(0x28B3)  #uni28B3	BRAILLE PATTERN DOTS-12568
        chars.append(0x28B4)  #uni28B4	BRAILLE PATTERN DOTS-3568
        chars.append(0x28B5)  #uni28B5	BRAILLE PATTERN DOTS-13568
        chars.append(0x28B6)  #uni28B6	BRAILLE PATTERN DOTS-23568
        chars.append(0x28B7)  #uni28B7	BRAILLE PATTERN DOTS-123568
        chars.append(0x28B8)  #uni28B8	BRAILLE PATTERN DOTS-4568
        chars.append(0x28B9)  #uni28B9	BRAILLE PATTERN DOTS-14568
        chars.append(0x28BA)  #uni28BA	BRAILLE PATTERN DOTS-24568
        chars.append(0x28BB)  #uni28BB	BRAILLE PATTERN DOTS-124568
        chars.append(0x28BC)  #uni28BC	BRAILLE PATTERN DOTS-34568
        chars.append(0x28BD)  #uni28BD	BRAILLE PATTERN DOTS-134568
        chars.append(0x28BE)  #uni28BE	BRAILLE PATTERN DOTS-234568
        chars.append(0x28BF)  #uni28BF	BRAILLE PATTERN DOTS-1234568
        chars.append(0x28C0)  #uni28C0	BRAILLE PATTERN DOTS-78
        chars.append(0x28C1)  #uni28C1	BRAILLE PATTERN DOTS-178
        chars.append(0x28C2)  #uni28C2	BRAILLE PATTERN DOTS-278
        chars.append(0x28C3)  #uni28C3	BRAILLE PATTERN DOTS-1278
        chars.append(0x28C4)  #uni28C4	BRAILLE PATTERN DOTS-378
        chars.append(0x28C5)  #uni28C5	BRAILLE PATTERN DOTS-1378
        chars.append(0x28C6)  #uni28C6	BRAILLE PATTERN DOTS-2378
        chars.append(0x28C7)  #uni28C7	BRAILLE PATTERN DOTS-12378
        chars.append(0x28C8)  #uni28C8	BRAILLE PATTERN DOTS-478
        chars.append(0x28C9)  #uni28C9	BRAILLE PATTERN DOTS-1478
        chars.append(0x28CA)  #uni28CA	BRAILLE PATTERN DOTS-2478
        chars.append(0x28CB)  #uni28CB	BRAILLE PATTERN DOTS-12478
        chars.append(0x28CC)  #uni28CC	BRAILLE PATTERN DOTS-3478
        chars.append(0x28CD)  #uni28CD	BRAILLE PATTERN DOTS-13478
        chars.append(0x28CE)  #uni28CE	BRAILLE PATTERN DOTS-23478
        chars.append(0x28CF)  #uni28CF	BRAILLE PATTERN DOTS-123478
        chars.append(0x28D0)  #uni28D0	BRAILLE PATTERN DOTS-578
        chars.append(0x28D1)  #uni28D1	BRAILLE PATTERN DOTS-1578
        chars.append(0x28D2)  #uni28D2	BRAILLE PATTERN DOTS-2578
        chars.append(0x28D3)  #uni28D3	BRAILLE PATTERN DOTS-12578
        chars.append(0x28D4)  #uni28D4	BRAILLE PATTERN DOTS-3578
        chars.append(0x28D5)  #uni28D5	BRAILLE PATTERN DOTS-13578
        chars.append(0x28D6)  #uni28D6	BRAILLE PATTERN DOTS-23578
        chars.append(0x28D7)  #uni28D7	BRAILLE PATTERN DOTS-123578
        chars.append(0x28D8)  #uni28D8	BRAILLE PATTERN DOTS-4578
        chars.append(0x28D9)  #uni28D9	BRAILLE PATTERN DOTS-14578
        chars.append(0x28DA)  #uni28DA	BRAILLE PATTERN DOTS-24578
        chars.append(0x28DB)  #uni28DB	BRAILLE PATTERN DOTS-124578
        chars.append(0x28DC)  #uni28DC	BRAILLE PATTERN DOTS-34578
        chars.append(0x28DD)  #uni28DD	BRAILLE PATTERN DOTS-134578
        chars.append(0x28DE)  #uni28DE	BRAILLE PATTERN DOTS-234578
        chars.append(0x28DF)  #uni28DF	BRAILLE PATTERN DOTS-1234578
        chars.append(0x28E0)  #uni28E0	BRAILLE PATTERN DOTS-678
        chars.append(0x28E1)  #uni28E1	BRAILLE PATTERN DOTS-1678
        chars.append(0x28E2)  #uni28E2	BRAILLE PATTERN DOTS-2678
        chars.append(0x28E3)  #uni28E3	BRAILLE PATTERN DOTS-12678
        chars.append(0x28E4)  #uni28E4	BRAILLE PATTERN DOTS-3678
        chars.append(0x28E5)  #uni28E5	BRAILLE PATTERN DOTS-13678
        chars.append(0x28E6)  #uni28E6	BRAILLE PATTERN DOTS-23678
        chars.append(0x28E7)  #uni28E7	BRAILLE PATTERN DOTS-123678
        chars.append(0x28E8)  #uni28E8	BRAILLE PATTERN DOTS-4678
        chars.append(0x28E9)  #uni28E9	BRAILLE PATTERN DOTS-14678
        chars.append(0x28EA)  #uni28EA	BRAILLE PATTERN DOTS-24678
        chars.append(0x28EB)  #uni28EB	BRAILLE PATTERN DOTS-124678
        chars.append(0x28EC)  #uni28EC	BRAILLE PATTERN DOTS-34678
        chars.append(0x28ED)  #uni28ED	BRAILLE PATTERN DOTS-134678
        chars.append(0x28EE)  #uni28EE	BRAILLE PATTERN DOTS-234678
        chars.append(0x28EF)  #uni28EF	BRAILLE PATTERN DOTS-1234678
        chars.append(0x28F0)  #uni28F0	BRAILLE PATTERN DOTS-5678
        chars.append(0x28F1)  #uni28F1	BRAILLE PATTERN DOTS-15678
        chars.append(0x28F2)  #uni28F2	BRAILLE PATTERN DOTS-25678
        chars.append(0x28F3)  #uni28F3	BRAILLE PATTERN DOTS-125678
        chars.append(0x28F4)  #uni28F4	BRAILLE PATTERN DOTS-35678
        chars.append(0x28F5)  #uni28F5	BRAILLE PATTERN DOTS-135678
        chars.append(0x28F6)  #uni28F6	BRAILLE PATTERN DOTS-235678
        chars.append(0x28F7)  #uni28F7	BRAILLE PATTERN DOTS-1235678
        chars.append(0x28F8)  #uni28F8	BRAILLE PATTERN DOTS-45678
        chars.append(0x28F9)  #uni28F9	BRAILLE PATTERN DOTS-145678
        chars.append(0x28FA)  #uni28FA	BRAILLE PATTERN DOTS-245678
        chars.append(0x28FB)  #uni28FB	BRAILLE PATTERN DOTS-1245678
        chars.append(0x28FC)  #uni28FC	BRAILLE PATTERN DOTS-345678
        chars.append(0x28FD)  #uni28FD	BRAILLE PATTERN DOTS-1345678
        chars.append(0x28FE)  #uni28FE	BRAILLE PATTERN DOTS-2345678
        chars.append(0x28FF)  #uni28FF	BRAILLE PATTERN DOTS-12345678
        chars.append(0x2900)  #uni2900	RIGHTWARDS TWO-HEADED ARROW WITH VERTICAL STROKE
        chars.append(0x2901)  #uni2901	RIGHTWARDS TWO-HEADED ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x2902)  #uni2902	LEFTWARDS DOUBLE ARROW WITH VERTICAL STROKE
        chars.append(0x2903)  #uni2903	RIGHTWARDS DOUBLE ARROW WITH VERTICAL STROKE
        chars.append(0x2904)  #uni2904	LEFT RIGHT DOUBLE ARROW WITH VERTICAL STROKE
        chars.append(0x2905)  #uni2905	RIGHTWARDS TWO-HEADED ARROW FROM BAR
        chars.append(0x2906)  #uni2906	LEFTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x2907)  #uni2907	RIGHTWARDS DOUBLE ARROW FROM BAR
        chars.append(0x2908)  #uni2908	DOWNWARDS ARROW WITH HORIZONTAL STROKE
        chars.append(0x2909)  #uni2909	UPWARDS ARROW WITH HORIZONTAL STROKE
        chars.append(0x290A)  #uni290A	UPWARDS TRIPLE ARROW
        chars.append(0x290B)  #uni290B	DOWNWARDS TRIPLE ARROW
        chars.append(0x290C)  #uni290C	LEFTWARDS DOUBLE DASH ARROW
        chars.append(0x290D)  #uni290D	RIGHTWARDS DOUBLE DASH ARROW
        chars.append(0x290E)  #uni290E	LEFTWARDS TRIPLE DASH ARROW
        chars.append(0x290F)  #uni290F	RIGHTWARDS TRIPLE DASH ARROW
        chars.append(0x2910)  #uni2910	RIGHTWARDS TWO-HEADED TRIPLE DASH ARROW
        chars.append(0x2911)  #uni2911	RIGHTWARDS ARROW WITH DOTTED STEM
        chars.append(0x2912)  #uni2912	UPWARDS ARROW TO BAR
        chars.append(0x2913)  #uni2913	DOWNWARDS ARROW TO BAR
        chars.append(0x2914)  #uni2914	RIGHTWARDS ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2915)  #uni2915	RIGHTWARDS ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2916)  #uni2916	RIGHTWARDS TWO-HEADED ARROW WITH TAIL
        chars.append(0x2917)  #uni2917	RIGHTWARDS TWO-HEADED ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2918)  #uni2918	RIGHTWARDS TWO-HEADED ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2919)  #uni2919	LEFTWARDS ARROW-TAIL
        chars.append(0x291A)  #uni291A	RIGHTWARDS ARROW-TAIL
        chars.append(0x291B)  #uni291B	LEFTWARDS DOUBLE ARROW-TAIL
        chars.append(0x291C)  #uni291C	RIGHTWARDS DOUBLE ARROW-TAIL
        chars.append(0x291D)  #uni291D	LEFTWARDS ARROW TO BLACK DIAMOND
        chars.append(0x291E)  #uni291E	RIGHTWARDS ARROW TO BLACK DIAMOND
        chars.append(0x291F)  #uni291F	LEFTWARDS ARROW FROM BAR TO BLACK DIAMOND
        chars.append(0x2920)  #uni2920	RIGHTWARDS ARROW FROM BAR TO BLACK DIAMOND
        chars.append(0x2921)  #uni2921	NORTH WEST AND SOUTH EAST ARROW
        chars.append(0x2922)  #uni2922	NORTH EAST AND SOUTH WEST ARROW
        chars.append(0x2923)  #uni2923	NORTH WEST ARROW WITH HOOK
        chars.append(0x2924)  #uni2924	NORTH EAST ARROW WITH HOOK
        chars.append(0x2925)  #uni2925	SOUTH EAST ARROW WITH HOOK
        chars.append(0x2926)  #uni2926	SOUTH WEST ARROW WITH HOOK
        chars.append(0x2927)  #uni2927	NORTH WEST ARROW AND NORTH EAST ARROW
        chars.append(0x2928)  #uni2928	NORTH EAST ARROW AND SOUTH EAST ARROW
        chars.append(0x2929)  #uni2929	SOUTH EAST ARROW AND SOUTH WEST ARROW
        chars.append(0x292A)  #uni292A	SOUTH WEST ARROW AND NORTH WEST ARROW
        chars.append(0x292B)  #uni292B	RISING DIAGONAL CROSSING FALLING DIAGONAL
        chars.append(0x292C)  #uni292C	FALLING DIAGONAL CROSSING RISING DIAGONAL
        chars.append(0x292D)  #uni292D	SOUTH EAST ARROW CROSSING NORTH EAST ARROW
        chars.append(0x292E)  #uni292E	NORTH EAST ARROW CROSSING SOUTH EAST ARROW
        chars.append(0x292F)  #uni292F	FALLING DIAGONAL CROSSING NORTH EAST ARROW
        chars.append(0x2930)  #uni2930	RISING DIAGONAL CROSSING SOUTH EAST ARROW
        chars.append(0x2931)  #uni2931	NORTH EAST ARROW CROSSING NORTH WEST ARROW
        chars.append(0x2932)  #uni2932	NORTH WEST ARROW CROSSING NORTH EAST ARROW
        chars.append(0x2933)  #uni2933	WAVE ARROW POINTING DIRECTLY RIGHT
        chars.append(0x2934)  #uni2934	ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS
        chars.append(0x2935)  #uni2935	ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS
        chars.append(0x2936)  #uni2936	ARROW POINTING DOWNWARDS THEN CURVING LEFTWARDS
        chars.append(0x2937)  #uni2937	ARROW POINTING DOWNWARDS THEN CURVING RIGHTWARDS
        chars.append(0x2938)  #uni2938	RIGHT-SIDE ARC CLOCKWISE ARROW
        chars.append(0x2939)  #uni2939	LEFT-SIDE ARC ANTICLOCKWISE ARROW
        chars.append(0x293A)  #uni293A	TOP ARC ANTICLOCKWISE ARROW
        chars.append(0x293B)  #uni293B	BOTTOM ARC ANTICLOCKWISE ARROW
        chars.append(0x293C)  #uni293C	TOP ARC CLOCKWISE ARROW WITH MINUS
        chars.append(0x293D)  #uni293D	TOP ARC ANTICLOCKWISE ARROW WITH PLUS
        chars.append(0x293E)  #uni293E	LOWER RIGHT SEMICIRCULAR CLOCKWISE ARROW
        chars.append(0x293F)  #uni293F	LOWER LEFT SEMICIRCULAR ANTICLOCKWISE ARROW
        chars.append(0x2940)  #uni2940	ANTICLOCKWISE CLOSED CIRCLE ARROW
        chars.append(0x2941)  #uni2941	CLOCKWISE CLOSED CIRCLE ARROW
        chars.append(0x2942)  #uni2942	RIGHTWARDS ARROW ABOVE SHORT LEFTWARDS ARROW
        chars.append(0x2943)  #uni2943	LEFTWARDS ARROW ABOVE SHORT RIGHTWARDS ARROW
        chars.append(0x2944)  #uni2944	SHORT RIGHTWARDS ARROW ABOVE LEFTWARDS ARROW
        chars.append(0x2945)  #uni2945	RIGHTWARDS ARROW WITH PLUS BELOW
        chars.append(0x2946)  #uni2946	LEFTWARDS ARROW WITH PLUS BELOW
        chars.append(0x2947)  #uni2947	RIGHTWARDS ARROW THROUGH X
        chars.append(0x2948)  #uni2948	LEFT RIGHT ARROW THROUGH SMALL CIRCLE
        chars.append(0x2949)  #uni2949	UPWARDS TWO-HEADED ARROW FROM SMALL CIRCLE
        chars.append(0x294A)  #uni294A	LEFT BARB UP RIGHT BARB DOWN HARPOON
        chars.append(0x294B)  #uni294B	LEFT BARB DOWN RIGHT BARB UP HARPOON
        chars.append(0x294C)  #uni294C	UP BARB RIGHT DOWN BARB LEFT HARPOON
        chars.append(0x294D)  #uni294D	UP BARB LEFT DOWN BARB RIGHT HARPOON
        chars.append(0x294E)  #uni294E	LEFT BARB UP RIGHT BARB UP HARPOON
        chars.append(0x294F)  #uni294F	UP BARB RIGHT DOWN BARB RIGHT HARPOON
        chars.append(0x2950)  #uni2950	LEFT BARB DOWN RIGHT BARB DOWN HARPOON
        chars.append(0x2951)  #uni2951	UP BARB LEFT DOWN BARB LEFT HARPOON
        chars.append(0x2952)  #uni2952	LEFTWARDS HARPOON WITH BARB UP TO BAR
        chars.append(0x2953)  #uni2953	RIGHTWARDS HARPOON WITH BARB UP TO BAR
        chars.append(0x2954)  #uni2954	UPWARDS HARPOON WITH BARB RIGHT TO BAR
        chars.append(0x2955)  #uni2955	DOWNWARDS HARPOON WITH BARB RIGHT TO BAR
        chars.append(0x2956)  #uni2956	LEFTWARDS HARPOON WITH BARB DOWN TO BAR
        chars.append(0x2957)  #uni2957	RIGHTWARDS HARPOON WITH BARB DOWN TO BAR
        chars.append(0x2958)  #uni2958	UPWARDS HARPOON WITH BARB LEFT TO BAR
        chars.append(0x2959)  #uni2959	DOWNWARDS HARPOON WITH BARB LEFT TO BAR
        chars.append(0x295A)  #uni295A	LEFTWARDS HARPOON WITH BARB UP FROM BAR
        chars.append(0x295B)  #uni295B	RIGHTWARDS HARPOON WITH BARB UP FROM BAR
        chars.append(0x295C)  #uni295C	UPWARDS HARPOON WITH BARB RIGHT FROM BAR
        chars.append(0x295D)  #uni295D	DOWNWARDS HARPOON WITH BARB RIGHT FROM BAR
        chars.append(0x295E)  #uni295E	LEFTWARDS HARPOON WITH BARB DOWN FROM BAR
        chars.append(0x295F)  #uni295F	RIGHTWARDS HARPOON WITH BARB DOWN FROM BAR
        chars.append(0x2960)  #uni2960	UPWARDS HARPOON WITH BARB LEFT FROM BAR
        chars.append(0x2961)  #uni2961	DOWNWARDS HARPOON WITH BARB LEFT FROM BAR
        chars.append(0x2962)  #uni2962	LEFTWARDS HARPOON WITH BARB UP ABOVE LEFTWARDS HARPOON WITH BARB DOWN
        chars.append(0x2963)  #uni2963	UPWARDS HARPOON WITH BARB LEFT BESIDE UPWARDS HARPOON WITH BARB RIGHT
        chars.append(0x2964)  #uni2964	RIGHTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB DOWN
        chars.append(0x2965)  #uni2965	DOWNWARDS HARPOON WITH BARB LEFT BESIDE DOWNWARDS HARPOON WITH BARB RIGHT
        chars.append(0x2966)  #uni2966	LEFTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB UP
        chars.append(0x2967)  #uni2967	LEFTWARDS HARPOON WITH BARB DOWN ABOVE RIGHTWARDS HARPOON WITH BARB DOWN
        chars.append(0x2968)  #uni2968	RIGHTWARDS HARPOON WITH BARB UP ABOVE LEFTWARDS HARPOON WITH BARB UP
        chars.append(0x2969)  #uni2969	RIGHTWARDS HARPOON WITH BARB DOWN ABOVE LEFTWARDS HARPOON WITH BARB DOWN
        chars.append(0x296A)  #uni296A	LEFTWARDS HARPOON WITH BARB UP ABOVE LONG DASH
        chars.append(0x296B)  #uni296B	LEFTWARDS HARPOON WITH BARB DOWN BELOW LONG DASH
        chars.append(0x296C)  #uni296C	RIGHTWARDS HARPOON WITH BARB UP ABOVE LONG DASH
        chars.append(0x296D)  #uni296D	RIGHTWARDS HARPOON WITH BARB DOWN BELOW LONG DASH
        chars.append(0x296E)  #uni296E	UPWARDS HARPOON WITH BARB LEFT BESIDE DOWNWARDS HARPOON WITH BARB RIGHT
        chars.append(0x296F)  #uni296F	DOWNWARDS HARPOON WITH BARB LEFT BESIDE UPWARDS HARPOON WITH BARB RIGHT
        chars.append(0x2970)  #uni2970	RIGHT DOUBLE ARROW WITH ROUNDED HEAD
        chars.append(0x2971)  #uni2971	EQUALS SIGN ABOVE RIGHTWARDS ARROW
        chars.append(0x2972)  #uni2972	TILDE OPERATOR ABOVE RIGHTWARDS ARROW
        chars.append(0x2973)  #uni2973	LEFTWARDS ARROW ABOVE TILDE OPERATOR
        chars.append(0x2974)  #uni2974	RIGHTWARDS ARROW ABOVE TILDE OPERATOR
        chars.append(0x2975)  #uni2975	RIGHTWARDS ARROW ABOVE ALMOST EQUAL TO
        chars.append(0x2976)  #uni2976	LESS-THAN ABOVE LEFTWARDS ARROW
        chars.append(0x2977)  #uni2977	LEFTWARDS ARROW THROUGH LESS-THAN
        chars.append(0x2978)  #uni2978	GREATER-THAN ABOVE RIGHTWARDS ARROW
        chars.append(0x2979)  #uni2979	SUBSET ABOVE RIGHTWARDS ARROW
        chars.append(0x297A)  #uni297A	LEFTWARDS ARROW THROUGH SUBSET
        chars.append(0x297B)  #uni297B	SUPERSET ABOVE LEFTWARDS ARROW
        chars.append(0x297C)  #uni297C	LEFT FISH TAIL
        chars.append(0x297D)  #uni297D	RIGHT FISH TAIL
        chars.append(0x297E)  #uni297E	UP FISH TAIL
        chars.append(0x297F)  #uni297F	DOWN FISH TAIL
        chars.append(0x2980)  #uni2980	TRIPLE VERTICAL BAR DELIMITER
        chars.append(0x2981)  #uni2981	Z NOTATION SPOT
        chars.append(0x2982)  #uni2982	Z NOTATION TYPE COLON
        chars.append(0x2983)  #uni2983	LEFT WHITE CURLY BRACKET
        chars.append(0x2984)  #uni2984	RIGHT WHITE CURLY BRACKET
        chars.append(0x2985)  #uni2985	LEFT WHITE PARENTHESIS
        chars.append(0x2986)  #uni2986	RIGHT WHITE PARENTHESIS
        chars.append(0x2987)  #uni2987	Z NOTATION LEFT IMAGE BRACKET
        chars.append(0x2988)  #uni2988	Z NOTATION RIGHT IMAGE BRACKET
        chars.append(0x2989)  #uni2989	Z NOTATION LEFT BINDING BRACKET
        chars.append(0x298A)  #uni298A	Z NOTATION RIGHT BINDING BRACKET
        chars.append(0x298B)  #uni298B	LEFT SQUARE BRACKET WITH UNDERBAR
        chars.append(0x298C)  #uni298C	RIGHT SQUARE BRACKET WITH UNDERBAR
        chars.append(0x298D)  #uni298D	LEFT SQUARE BRACKET WITH TICK IN TOP CORNER
        chars.append(0x298E)  #uni298E	RIGHT SQUARE BRACKET WITH TICK IN BOTTOM CORNER
        chars.append(0x298F)  #uni298F	LEFT SQUARE BRACKET WITH TICK IN BOTTOM CORNER
        chars.append(0x2990)  #uni2990	RIGHT SQUARE BRACKET WITH TICK IN TOP CORNER
        chars.append(0x2991)  #uni2991	LEFT ANGLE BRACKET WITH DOT
        chars.append(0x2992)  #uni2992	RIGHT ANGLE BRACKET WITH DOT
        chars.append(0x2993)  #uni2993	LEFT ARC LESS-THAN BRACKET
        chars.append(0x2994)  #uni2994	RIGHT ARC GREATER-THAN BRACKET
        chars.append(0x2995)  #uni2995	DOUBLE LEFT ARC GREATER-THAN BRACKET
        chars.append(0x2996)  #uni2996	DOUBLE RIGHT ARC LESS-THAN BRACKET
        chars.append(0x2997)  #uni2997	LEFT BLACK TORTOISE SHELL BRACKET
        chars.append(0x2998)  #uni2998	RIGHT BLACK TORTOISE SHELL BRACKET
        chars.append(0x2999)  #uni2999	DOTTED FENCE
        chars.append(0x299A)  #uni299A	VERTICAL ZIGZAG LINE
        chars.append(0x299B)  #uni299B	MEASURED ANGLE OPENING LEFT
        chars.append(0x299C)  #uni299C	RIGHT ANGLE VARIANT WITH SQUARE
        chars.append(0x299D)  #uni299D	MEASURED RIGHT ANGLE WITH DOT
        chars.append(0x299E)  #uni299E	ANGLE WITH S INSIDE
        chars.append(0x299F)  #uni299F	ACUTE ANGLE
        chars.append(0x29A0)  #uni29A0	SPHERICAL ANGLE OPENING LEFT
        chars.append(0x29A1)  #uni29A1	SPHERICAL ANGLE OPENING UP
        chars.append(0x29A2)  #uni29A2	TURNED ANGLE
        chars.append(0x29A3)  #uni29A3	REVERSED ANGLE
        chars.append(0x29A4)  #uni29A4	ANGLE WITH UNDERBAR
        chars.append(0x29A5)  #uni29A5	REVERSED ANGLE WITH UNDERBAR
        chars.append(0x29A6)  #uni29A6	OBLIQUE ANGLE OPENING UP
        chars.append(0x29A7)  #uni29A7	OBLIQUE ANGLE OPENING DOWN
        chars.append(0x29A8)  #uni29A8	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING UP AND RIGHT
        chars.append(0x29A9)  #uni29A9	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING UP AND LEFT
        chars.append(0x29AA)  #uni29AA	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING DOWN AND RIGHT
        chars.append(0x29AB)  #uni29AB	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING DOWN AND LEFT
        chars.append(0x29AC)  #uni29AC	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING RIGHT AND UP
        chars.append(0x29AD)  #uni29AD	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING LEFT AND UP
        chars.append(0x29AE)  #uni29AE	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING RIGHT AND DOWN
        chars.append(0x29AF)  #uni29AF	MEASURED ANGLE WITH OPEN ARM ENDING IN ARROW POINTING LEFT AND DOWN
        chars.append(0x29B0)  #uni29B0	REVERSED EMPTY SET
        chars.append(0x29B1)  #uni29B1	EMPTY SET WITH OVERBAR
        chars.append(0x29B2)  #uni29B2	EMPTY SET WITH SMALL CIRCLE ABOVE
        chars.append(0x29B3)  #uni29B3	EMPTY SET WITH RIGHT ARROW ABOVE
        chars.append(0x29B4)  #uni29B4	EMPTY SET WITH LEFT ARROW ABOVE
        chars.append(0x29B5)  #uni29B5	CIRCLE WITH HORIZONTAL BAR
        chars.append(0x29B6)  #uni29B6	CIRCLED VERTICAL BAR
        chars.append(0x29B7)  #uni29B7	CIRCLED PARALLEL
        chars.append(0x29B8)  #uni29B8	CIRCLED REVERSE SOLIDUS
        chars.append(0x29B9)  #uni29B9	CIRCLED PERPENDICULAR
        chars.append(0x29BA)  #uni29BA	CIRCLE DIVIDED BY HORIZONTAL BAR AND TOP HALF DIVIDED BY VERTICAL BAR
        chars.append(0x29BB)  #uni29BB	CIRCLE WITH SUPERIMPOSED X
        chars.append(0x29BC)  #uni29BC	CIRCLED ANTICLOCKWISE-ROTATED DIVISION SIGN
        chars.append(0x29BD)  #uni29BD	UP ARROW THROUGH CIRCLE
        chars.append(0x29BE)  #uni29BE	CIRCLED WHITE BULLET
        chars.append(0x29BF)  #uni29BF	CIRCLED BULLET
        chars.append(0x29C0)  #uni29C0	CIRCLED LESS-THAN
        chars.append(0x29C1)  #uni29C1	CIRCLED GREATER-THAN
        chars.append(0x29C2)  #uni29C2	CIRCLE WITH SMALL CIRCLE TO THE RIGHT
        chars.append(0x29C3)  #uni29C3	CIRCLE WITH TWO HORIZONTAL STROKES TO THE RIGHT
        chars.append(0x29C4)  #uni29C4	SQUARED RISING DIAGONAL SLASH
        chars.append(0x29C5)  #uni29C5	SQUARED FALLING DIAGONAL SLASH
        chars.append(0x29C6)  #uni29C6	SQUARED ASTERISK
        chars.append(0x29C7)  #uni29C7	SQUARED SMALL CIRCLE
        chars.append(0x29C8)  #uni29C8	SQUARED SQUARE
        chars.append(0x29C9)  #uni29C9	TWO JOINED SQUARES
        chars.append(0x29CA)  #uni29CA	TRIANGLE WITH DOT ABOVE
        chars.append(0x29CB)  #uni29CB	TRIANGLE WITH UNDERBAR
        chars.append(0x29CC)  #uni29CC	S IN TRIANGLE
        chars.append(0x29CD)  #uni29CD	TRIANGLE WITH SERIFS AT BOTTOM
        chars.append(0x29CE)  #uni29CE	RIGHT TRIANGLE ABOVE LEFT TRIANGLE
        chars.append(0x29CF)  #uni29CF	LEFT TRIANGLE BESIDE VERTICAL BAR
        chars.append(0x29D0)  #uni29D0	VERTICAL BAR BESIDE RIGHT TRIANGLE
        chars.append(0x29D1)  #uni29D1	BOWTIE WITH LEFT HALF BLACK
        chars.append(0x29D2)  #uni29D2	BOWTIE WITH RIGHT HALF BLACK
        chars.append(0x29D3)  #uni29D3	BLACK BOWTIE
        chars.append(0x29D4)  #uni29D4	TIMES WITH LEFT HALF BLACK
        chars.append(0x29D5)  #uni29D5	TIMES WITH RIGHT HALF BLACK
        chars.append(0x29D6)  #uni29D6	WHITE HOURGLASS
        chars.append(0x29D7)  #uni29D7	BLACK HOURGLASS
        chars.append(0x29D8)  #uni29D8	LEFT WIGGLY FENCE
        chars.append(0x29D9)  #uni29D9	RIGHT WIGGLY FENCE
        chars.append(0x29DA)  #uni29DA	LEFT DOUBLE WIGGLY FENCE
        chars.append(0x29DB)  #uni29DB	RIGHT DOUBLE WIGGLY FENCE
        chars.append(0x29DC)  #uni29DC	INCOMPLETE INFINITY
        chars.append(0x29DD)  #uni29DD	TIE OVER INFINITY
        chars.append(0x29DE)  #uni29DE	INFINITY NEGATED WITH VERTICAL BAR
        chars.append(0x29DF)  #uni29DF	DOUBLE-ENDED MULTIMAP
        chars.append(0x29E0)  #uni29E0	SQUARE WITH CONTOURED OUTLINE
        chars.append(0x29E1)  #uni29E1	INCREASES AS
        chars.append(0x29E2)  #uni29E2	SHUFFLE PRODUCT
        chars.append(0x29E3)  #uni29E3	EQUALS SIGN AND SLANTED PARALLEL
        chars.append(0x29E4)  #uni29E4	EQUALS SIGN AND SLANTED PARALLEL WITH TILDE ABOVE
        chars.append(0x29E5)  #uni29E5	IDENTICAL TO AND SLANTED PARALLEL
        chars.append(0x29E6)  #uni29E6	GLEICH STARK
        chars.append(0x29E7)  #uni29E7	THERMODYNAMIC
        chars.append(0x29E8)  #uni29E8	DOWN-POINTING TRIANGLE WITH LEFT HALF BLACK
        chars.append(0x29E9)  #uni29E9	DOWN-POINTING TRIANGLE WITH RIGHT HALF BLACK
        chars.append(0x29EA)  #uni29EA	BLACK DIAMOND WITH DOWN ARROW
        chars.append(0x29EB)  #uni29EB	BLACK LOZENGE
        chars.append(0x29EC)  #uni29EC	WHITE CIRCLE WITH DOWN ARROW
        chars.append(0x29ED)  #uni29ED	BLACK CIRCLE WITH DOWN ARROW
        chars.append(0x29EE)  #uni29EE	ERROR-BARRED WHITE SQUARE
        chars.append(0x29EF)  #uni29EF	ERROR-BARRED BLACK SQUARE
        chars.append(0x29F0)  #uni29F0	ERROR-BARRED WHITE DIAMOND
        chars.append(0x29F1)  #uni29F1	ERROR-BARRED BLACK DIAMOND
        chars.append(0x29F2)  #uni29F2	ERROR-BARRED WHITE CIRCLE
        chars.append(0x29F3)  #uni29F3	ERROR-BARRED BLACK CIRCLE
        chars.append(0x29F4)  #uni29F4	RULE-DELAYED
        chars.append(0x29F5)  #uni29F5	REVERSE SOLIDUS OPERATOR
        chars.append(0x29F6)  #uni29F6	SOLIDUS WITH OVERBAR
        chars.append(0x29F7)  #uni29F7	REVERSE SOLIDUS WITH HORIZONTAL STROKE
        chars.append(0x29F8)  #uni29F8	BIG SOLIDUS
        chars.append(0x29F9)  #uni29F9	BIG REVERSE SOLIDUS
        chars.append(0x29FA)  #uni29FA	DOUBLE PLUS
        chars.append(0x29FB)  #uni29FB	TRIPLE PLUS
        chars.append(0x29FC)  #uni29FC	LEFT-POINTING CURVED ANGLE BRACKET
        chars.append(0x29FD)  #uni29FD	RIGHT-POINTING CURVED ANGLE BRACKET
        chars.append(0x29FE)  #uni29FE	TINY
        chars.append(0x29FF)  #uni29FF	MINY
        chars.append(0x2A00)  #uni2A00	N-ARY CIRCLED DOT OPERATOR
        chars.append(0x2A01)  #uni2A01	N-ARY CIRCLED PLUS OPERATOR
        chars.append(0x2A02)  #uni2A02	N-ARY CIRCLED TIMES OPERATOR
        chars.append(0x2A03)  #uni2A03	N-ARY UNION OPERATOR WITH DOT
        chars.append(0x2A04)  #uni2A04	N-ARY UNION OPERATOR WITH PLUS
        chars.append(0x2A05)  #uni2A05	N-ARY SQUARE INTERSECTION OPERATOR
        chars.append(0x2A06)  #uni2A06	N-ARY SQUARE UNION OPERATOR
        chars.append(0x2A07)  #uni2A07	TWO LOGICAL AND OPERATOR
        chars.append(0x2A08)  #uni2A08	TWO LOGICAL OR OPERATOR
        chars.append(0x2A09)  #uni2A09	N-ARY TIMES OPERATOR
        chars.append(0x2A0A)  #uni2A0A	MODULO TWO SUM
        chars.append(0x2A0B)  #uni2A0B	SUMMATION WITH INTEGRAL
        chars.append(0x2A0C)  #uni2A0C	QUADRUPLE INTEGRAL OPERATOR
        chars.append(0x2A0D)  #uni2A0D	FINITE PART INTEGRAL
        chars.append(0x2A0E)  #uni2A0E	INTEGRAL WITH DOUBLE STROKE
        chars.append(0x2A0F)  #uni2A0F	INTEGRAL AVERAGE WITH SLASH
        chars.append(0x2A10)  #uni2A10	CIRCULATION FUNCTION
        chars.append(0x2A11)  #uni2A11	ANTICLOCKWISE INTEGRATION
        chars.append(0x2A12)  #uni2A12	LINE INTEGRATION WITH RECTANGULAR PATH AROUND POLE
        chars.append(0x2A13)  #uni2A13	LINE INTEGRATION WITH SEMICIRCULAR PATH AROUND POLE
        chars.append(0x2A14)  #uni2A14	LINE INTEGRATION NOT INCLUDING THE POLE
        chars.append(0x2A15)  #uni2A15	INTEGRAL AROUND A POINT OPERATOR
        chars.append(0x2A16)  #uni2A16	QUATERNION INTEGRAL OPERATOR
        chars.append(0x2A17)  #uni2A17	INTEGRAL WITH LEFTWARDS ARROW WITH HOOK
        chars.append(0x2A18)  #uni2A18	INTEGRAL WITH TIMES SIGN
        chars.append(0x2A19)  #uni2A19	INTEGRAL WITH INTERSECTION
        chars.append(0x2A1A)  #uni2A1A	INTEGRAL WITH UNION
        chars.append(0x2A1B)  #uni2A1B	INTEGRAL WITH OVERBAR
        chars.append(0x2A1C)  #uni2A1C	INTEGRAL WITH UNDERBAR
        chars.append(0x2A1D)  #uni2A1D	JOIN
        chars.append(0x2A1E)  #uni2A1E	LARGE LEFT TRIANGLE OPERATOR
        chars.append(0x2A1F)  #uni2A1F	Z NOTATION SCHEMA COMPOSITION
        chars.append(0x2A20)  #uni2A20	Z NOTATION SCHEMA PIPING
        chars.append(0x2A21)  #uni2A21	Z NOTATION SCHEMA PROJECTION
        chars.append(0x2A22)  #uni2A22	PLUS SIGN WITH SMALL CIRCLE ABOVE
        chars.append(0x2A23)  #uni2A23	PLUS SIGN WITH CIRCUMFLEX ACCENT ABOVE
        chars.append(0x2A24)  #uni2A24	PLUS SIGN WITH TILDE ABOVE
        chars.append(0x2A25)  #uni2A25	PLUS SIGN WITH DOT BELOW
        chars.append(0x2A26)  #uni2A26	PLUS SIGN WITH TILDE BELOW
        chars.append(0x2A27)  #uni2A27	PLUS SIGN WITH SUBSCRIPT TWO
        chars.append(0x2A28)  #uni2A28	PLUS SIGN WITH BLACK TRIANGLE
        chars.append(0x2A29)  #uni2A29	MINUS SIGN WITH COMMA ABOVE
        chars.append(0x2A2A)  #uni2A2A	MINUS SIGN WITH DOT BELOW
        chars.append(0x2A2B)  #uni2A2B	MINUS SIGN WITH FALLING DOTS
        chars.append(0x2A2C)  #uni2A2C	MINUS SIGN WITH RISING DOTS
        chars.append(0x2A2D)  #uni2A2D	PLUS SIGN IN LEFT HALF CIRCLE
        chars.append(0x2A2E)  #uni2A2E	PLUS SIGN IN RIGHT HALF CIRCLE
        chars.append(0x2A2F)  #uni2A2F	VECTOR OR CROSS PRODUCT
        chars.append(0x2A30)  #uni2A30	MULTIPLICATION SIGN WITH DOT ABOVE
        chars.append(0x2A31)  #uni2A31	MULTIPLICATION SIGN WITH UNDERBAR
        chars.append(0x2A32)  #uni2A32	SEMIDIRECT PRODUCT WITH BOTTOM CLOSED
        chars.append(0x2A33)  #uni2A33	SMASH PRODUCT
        chars.append(0x2A34)  #uni2A34	MULTIPLICATION SIGN IN LEFT HALF CIRCLE
        chars.append(0x2A35)  #uni2A35	MULTIPLICATION SIGN IN RIGHT HALF CIRCLE
        chars.append(0x2A36)  #uni2A36	CIRCLED MULTIPLICATION SIGN WITH CIRCUMFLEX ACCENT
        chars.append(0x2A37)  #uni2A37	MULTIPLICATION SIGN IN DOUBLE CIRCLE
        chars.append(0x2A38)  #uni2A38	CIRCLED DIVISION SIGN
        chars.append(0x2A39)  #uni2A39	PLUS SIGN IN TRIANGLE
        chars.append(0x2A3A)  #uni2A3A	MINUS SIGN IN TRIANGLE
        chars.append(0x2A3B)  #uni2A3B	MULTIPLICATION SIGN IN TRIANGLE
        chars.append(0x2A3C)  #uni2A3C	INTERIOR PRODUCT
        chars.append(0x2A3D)  #uni2A3D	RIGHTHAND INTERIOR PRODUCT
        chars.append(0x2A3E)  #uni2A3E	Z NOTATION RELATIONAL COMPOSITION
        chars.append(0x2A3F)  #uni2A3F	AMALGAMATION OR COPRODUCT
        chars.append(0x2A40)  #uni2A40	INTERSECTION WITH DOT
        chars.append(0x2A41)  #uni2A41	UNION WITH MINUS SIGN
        chars.append(0x2A42)  #uni2A42	UNION WITH OVERBAR
        chars.append(0x2A43)  #uni2A43	INTERSECTION WITH OVERBAR
        chars.append(0x2A44)  #uni2A44	INTERSECTION WITH LOGICAL AND
        chars.append(0x2A45)  #uni2A45	UNION WITH LOGICAL OR
        chars.append(0x2A46)  #uni2A46	UNION ABOVE INTERSECTION
        chars.append(0x2A47)  #uni2A47	INTERSECTION ABOVE UNION
        chars.append(0x2A48)  #uni2A48	UNION ABOVE BAR ABOVE INTERSECTION
        chars.append(0x2A49)  #uni2A49	INTERSECTION ABOVE BAR ABOVE UNION
        chars.append(0x2A4A)  #uni2A4A	UNION BESIDE AND JOINED WITH UNION
        chars.append(0x2A4B)  #uni2A4B	INTERSECTION BESIDE AND JOINED WITH INTERSECTION
        chars.append(0x2A4C)  #uni2A4C	CLOSED UNION WITH SERIFS
        chars.append(0x2A4D)  #uni2A4D	CLOSED INTERSECTION WITH SERIFS
        chars.append(0x2A4E)  #uni2A4E	DOUBLE SQUARE INTERSECTION
        chars.append(0x2A4F)  #uni2A4F	DOUBLE SQUARE UNION
        chars.append(0x2A50)  #uni2A50	CLOSED UNION WITH SERIFS AND SMASH PRODUCT
        chars.append(0x2A51)  #uni2A51	LOGICAL AND WITH DOT ABOVE
        chars.append(0x2A52)  #uni2A52	LOGICAL OR WITH DOT ABOVE
        chars.append(0x2A53)  #uni2A53	DOUBLE LOGICAL AND
        chars.append(0x2A54)  #uni2A54	DOUBLE LOGICAL OR
        chars.append(0x2A55)  #uni2A55	TWO INTERSECTING LOGICAL AND
        chars.append(0x2A56)  #uni2A56	TWO INTERSECTING LOGICAL OR
        chars.append(0x2A57)  #uni2A57	SLOPING LARGE OR
        chars.append(0x2A58)  #uni2A58	SLOPING LARGE AND
        chars.append(0x2A59)  #uni2A59	LOGICAL OR OVERLAPPING LOGICAL AND
        chars.append(0x2A5A)  #uni2A5A	LOGICAL AND WITH MIDDLE STEM
        chars.append(0x2A5B)  #uni2A5B	LOGICAL OR WITH MIDDLE STEM
        chars.append(0x2A5C)  #uni2A5C	LOGICAL AND WITH HORIZONTAL DASH
        chars.append(0x2A5D)  #uni2A5D	LOGICAL OR WITH HORIZONTAL DASH
        chars.append(0x2A5E)  #uni2A5E	LOGICAL AND WITH DOUBLE OVERBAR
        chars.append(0x2A5F)  #uni2A5F	LOGICAL AND WITH UNDERBAR
        chars.append(0x2A60)  #uni2A60	LOGICAL AND WITH DOUBLE UNDERBAR
        chars.append(0x2A61)  #uni2A61	SMALL VEE WITH UNDERBAR
        chars.append(0x2A62)  #uni2A62	LOGICAL OR WITH DOUBLE OVERBAR
        chars.append(0x2A63)  #uni2A63	LOGICAL OR WITH DOUBLE UNDERBAR
        chars.append(0x2A64)  #uni2A64	Z NOTATION DOMAIN ANTIRESTRICTION
        chars.append(0x2A65)  #uni2A65	Z NOTATION RANGE ANTIRESTRICTION
        chars.append(0x2A66)  #uni2A66	EQUALS SIGN WITH DOT BELOW
        chars.append(0x2A67)  #uni2A67	IDENTICAL WITH DOT ABOVE
        chars.append(0x2A68)  #uni2A68	TRIPLE HORIZONTAL BAR WITH DOUBLE VERTICAL STROKE
        chars.append(0x2A69)  #uni2A69	TRIPLE HORIZONTAL BAR WITH TRIPLE VERTICAL STROKE
        chars.append(0x2A6A)  #uni2A6A	TILDE OPERATOR WITH DOT ABOVE
        chars.append(0x2A6B)  #uni2A6B	TILDE OPERATOR WITH RISING DOTS
        chars.append(0x2A6C)  #uni2A6C	SIMILAR MINUS SIMILAR
        chars.append(0x2A6D)  #uni2A6D	CONGRUENT WITH DOT ABOVE
        chars.append(0x2A6E)  #uni2A6E	EQUALS WITH ASTERISK
        chars.append(0x2A6F)  #uni2A6F	ALMOST EQUAL TO WITH CIRCUMFLEX ACCENT
        chars.append(0x2A70)  #uni2A70	APPROXIMATELY EQUAL OR EQUAL TO
        chars.append(0x2A71)  #uni2A71	EQUALS SIGN ABOVE PLUS SIGN
        chars.append(0x2A72)  #uni2A72	PLUS SIGN ABOVE EQUALS SIGN
        chars.append(0x2A73)  #uni2A73	EQUALS SIGN ABOVE TILDE OPERATOR
        chars.append(0x2A74)  #uni2A74	DOUBLE COLON EQUAL
        chars.append(0x2A75)  #uni2A75	TWO CONSECUTIVE EQUALS SIGNS
        chars.append(0x2A76)  #uni2A76	THREE CONSECUTIVE EQUALS SIGNS
        chars.append(0x2A77)  #uni2A77	EQUALS SIGN WITH TWO DOTS ABOVE AND TWO DOTS BELOW
        chars.append(0x2A78)  #uni2A78	EQUIVALENT WITH FOUR DOTS ABOVE
        chars.append(0x2A79)  #uni2A79	LESS-THAN WITH CIRCLE INSIDE
        chars.append(0x2A7A)  #uni2A7A	GREATER-THAN WITH CIRCLE INSIDE
        chars.append(0x2A7B)  #uni2A7B	LESS-THAN WITH QUESTION MARK ABOVE
        chars.append(0x2A7C)  #uni2A7C	GREATER-THAN WITH QUESTION MARK ABOVE
        chars.append(0x2A7D)  #uni2A7D	LESS-THAN OR SLANTED EQUAL TO
        chars.append(0x2A7E)  #uni2A7E	GREATER-THAN OR SLANTED EQUAL TO
        chars.append(0x2A7F)  #uni2A7F	LESS-THAN OR SLANTED EQUAL TO WITH DOT INSIDE
        chars.append(0x2A80)  #uni2A80	GREATER-THAN OR SLANTED EQUAL TO WITH DOT INSIDE
        chars.append(0x2A81)  #uni2A81	LESS-THAN OR SLANTED EQUAL TO WITH DOT ABOVE
        chars.append(0x2A82)  #uni2A82	GREATER-THAN OR SLANTED EQUAL TO WITH DOT ABOVE
        chars.append(0x2A83)  #uni2A83	LESS-THAN OR SLANTED EQUAL TO WITH DOT ABOVE RIGHT
        chars.append(0x2A84)  #uni2A84	GREATER-THAN OR SLANTED EQUAL TO WITH DOT ABOVE LEFT
        chars.append(0x2A85)  #uni2A85	LESS-THAN OR APPROXIMATE
        chars.append(0x2A86)  #uni2A86	GREATER-THAN OR APPROXIMATE
        chars.append(0x2A87)  #uni2A87	LESS-THAN AND SINGLE-LINE NOT EQUAL TO
        chars.append(0x2A88)  #uni2A88	GREATER-THAN AND SINGLE-LINE NOT EQUAL TO
        chars.append(0x2A89)  #uni2A89	LESS-THAN AND NOT APPROXIMATE
        chars.append(0x2A8A)  #uni2A8A	GREATER-THAN AND NOT APPROXIMATE
        chars.append(0x2A8B)  #uni2A8B	LESS-THAN ABOVE DOUBLE-LINE EQUAL ABOVE GREATER-THAN
        chars.append(0x2A8C)  #uni2A8C	GREATER-THAN ABOVE DOUBLE-LINE EQUAL ABOVE LESS-THAN
        chars.append(0x2A8D)  #uni2A8D	LESS-THAN ABOVE SIMILAR OR EQUAL
        chars.append(0x2A8E)  #uni2A8E	GREATER-THAN ABOVE SIMILAR OR EQUAL
        chars.append(0x2A8F)  #uni2A8F	LESS-THAN ABOVE SIMILAR ABOVE GREATER-THAN
        chars.append(0x2A90)  #uni2A90	GREATER-THAN ABOVE SIMILAR ABOVE LESS-THAN
        chars.append(0x2A91)  #uni2A91	LESS-THAN ABOVE GREATER-THAN ABOVE DOUBLE-LINE EQUAL
        chars.append(0x2A92)  #uni2A92	GREATER-THAN ABOVE LESS-THAN ABOVE DOUBLE-LINE EQUAL
        chars.append(0x2A93)  #uni2A93	LESS-THAN ABOVE SLANTED EQUAL ABOVE GREATER-THAN ABOVE SLANTED EQUAL
        chars.append(0x2A94)  #uni2A94	GREATER-THAN ABOVE SLANTED EQUAL ABOVE LESS-THAN ABOVE SLANTED EQUAL
        chars.append(0x2A95)  #uni2A95	SLANTED EQUAL TO OR LESS-THAN
        chars.append(0x2A96)  #uni2A96	SLANTED EQUAL TO OR GREATER-THAN
        chars.append(0x2A97)  #uni2A97	SLANTED EQUAL TO OR LESS-THAN WITH DOT INSIDE
        chars.append(0x2A98)  #uni2A98	SLANTED EQUAL TO OR GREATER-THAN WITH DOT INSIDE
        chars.append(0x2A99)  #uni2A99	DOUBLE-LINE EQUAL TO OR LESS-THAN
        chars.append(0x2A9A)  #uni2A9A	DOUBLE-LINE EQUAL TO OR GREATER-THAN
        chars.append(0x2A9B)  #uni2A9B	DOUBLE-LINE SLANTED EQUAL TO OR LESS-THAN
        chars.append(0x2A9C)  #uni2A9C	DOUBLE-LINE SLANTED EQUAL TO OR GREATER-THAN
        chars.append(0x2A9D)  #uni2A9D	SIMILAR OR LESS-THAN
        chars.append(0x2A9E)  #uni2A9E	SIMILAR OR GREATER-THAN
        chars.append(0x2A9F)  #uni2A9F	SIMILAR ABOVE LESS-THAN ABOVE EQUALS SIGN
        chars.append(0x2AA0)  #uni2AA0	SIMILAR ABOVE GREATER-THAN ABOVE EQUALS SIGN
        chars.append(0x2AA1)  #uni2AA1	DOUBLE NESTED LESS-THAN
        chars.append(0x2AA2)  #uni2AA2	DOUBLE NESTED GREATER-THAN
        chars.append(0x2AA3)  #uni2AA3	DOUBLE NESTED LESS-THAN WITH UNDERBAR
        chars.append(0x2AA4)  #uni2AA4	GREATER-THAN OVERLAPPING LESS-THAN
        chars.append(0x2AA5)  #uni2AA5	GREATER-THAN BESIDE LESS-THAN
        chars.append(0x2AA6)  #uni2AA6	LESS-THAN CLOSED BY CURVE
        chars.append(0x2AA7)  #uni2AA7	GREATER-THAN CLOSED BY CURVE
        chars.append(0x2AA8)  #uni2AA8	LESS-THAN CLOSED BY CURVE ABOVE SLANTED EQUAL
        chars.append(0x2AA9)  #uni2AA9	GREATER-THAN CLOSED BY CURVE ABOVE SLANTED EQUAL
        chars.append(0x2AAA)  #uni2AAA	SMALLER THAN
        chars.append(0x2AAB)  #uni2AAB	LARGER THAN
        chars.append(0x2AAC)  #uni2AAC	SMALLER THAN OR EQUAL TO
        chars.append(0x2AAD)  #uni2AAD	LARGER THAN OR EQUAL TO
        chars.append(0x2AAE)  #uni2AAE	EQUALS SIGN WITH BUMPY ABOVE
        chars.append(0x2AAF)  #uni2AAF	PRECEDES ABOVE SINGLE-LINE EQUALS SIGN
        chars.append(0x2AB0)  #uni2AB0	SUCCEEDS ABOVE SINGLE-LINE EQUALS SIGN
        chars.append(0x2AB1)  #uni2AB1	PRECEDES ABOVE SINGLE-LINE NOT EQUAL TO
        chars.append(0x2AB2)  #uni2AB2	SUCCEEDS ABOVE SINGLE-LINE NOT EQUAL TO
        chars.append(0x2AB3)  #uni2AB3	PRECEDES ABOVE EQUALS SIGN
        chars.append(0x2AB4)  #uni2AB4	SUCCEEDS ABOVE EQUALS SIGN
        chars.append(0x2AB5)  #uni2AB5	PRECEDES ABOVE NOT EQUAL TO
        chars.append(0x2AB6)  #uni2AB6	SUCCEEDS ABOVE NOT EQUAL TO
        chars.append(0x2AB7)  #uni2AB7	PRECEDES ABOVE ALMOST EQUAL TO
        chars.append(0x2AB8)  #uni2AB8	SUCCEEDS ABOVE ALMOST EQUAL TO
        chars.append(0x2AB9)  #uni2AB9	PRECEDES ABOVE NOT ALMOST EQUAL TO
        chars.append(0x2ABA)  #uni2ABA	SUCCEEDS ABOVE NOT ALMOST EQUAL TO
        chars.append(0x2ABB)  #uni2ABB	DOUBLE PRECEDES
        chars.append(0x2ABC)  #uni2ABC	DOUBLE SUCCEEDS
        chars.append(0x2ABD)  #uni2ABD	SUBSET WITH DOT
        chars.append(0x2ABE)  #uni2ABE	SUPERSET WITH DOT
        chars.append(0x2ABF)  #uni2ABF	SUBSET WITH PLUS SIGN BELOW
        chars.append(0x2AC0)  #uni2AC0	SUPERSET WITH PLUS SIGN BELOW
        chars.append(0x2AC1)  #uni2AC1	SUBSET WITH MULTIPLICATION SIGN BELOW
        chars.append(0x2AC2)  #uni2AC2	SUPERSET WITH MULTIPLICATION SIGN BELOW
        chars.append(0x2AC3)  #uni2AC3	SUBSET OF OR EQUAL TO WITH DOT ABOVE
        chars.append(0x2AC4)  #uni2AC4	SUPERSET OF OR EQUAL TO WITH DOT ABOVE
        chars.append(0x2AC5)  #uni2AC5	SUBSET OF ABOVE EQUALS SIGN
        chars.append(0x2AC6)  #uni2AC6	SUPERSET OF ABOVE EQUALS SIGN
        chars.append(0x2AC7)  #uni2AC7	SUBSET OF ABOVE TILDE OPERATOR
        chars.append(0x2AC8)  #uni2AC8	SUPERSET OF ABOVE TILDE OPERATOR
        chars.append(0x2AC9)  #uni2AC9	SUBSET OF ABOVE ALMOST EQUAL TO
        chars.append(0x2ACA)  #uni2ACA	SUPERSET OF ABOVE ALMOST EQUAL TO
        chars.append(0x2ACB)  #uni2ACB	SUBSET OF ABOVE NOT EQUAL TO
        chars.append(0x2ACC)  #uni2ACC	SUPERSET OF ABOVE NOT EQUAL TO
        chars.append(0x2ACD)  #uni2ACD	SQUARE LEFT OPEN BOX OPERATOR
        chars.append(0x2ACE)  #uni2ACE	SQUARE RIGHT OPEN BOX OPERATOR
        chars.append(0x2ACF)  #uni2ACF	CLOSED SUBSET
        chars.append(0x2AD0)  #uni2AD0	CLOSED SUPERSET
        chars.append(0x2AD1)  #uni2AD1	CLOSED SUBSET OR EQUAL TO
        chars.append(0x2AD2)  #uni2AD2	CLOSED SUPERSET OR EQUAL TO
        chars.append(0x2AD3)  #uni2AD3	SUBSET ABOVE SUPERSET
        chars.append(0x2AD4)  #uni2AD4	SUPERSET ABOVE SUBSET
        chars.append(0x2AD5)  #uni2AD5	SUBSET ABOVE SUBSET
        chars.append(0x2AD6)  #uni2AD6	SUPERSET ABOVE SUPERSET
        chars.append(0x2AD7)  #uni2AD7	SUPERSET BESIDE SUBSET
        chars.append(0x2AD8)  #uni2AD8	SUPERSET BESIDE AND JOINED BY DASH WITH SUBSET
        chars.append(0x2AD9)  #uni2AD9	ELEMENT OF OPENING DOWNWARDS
        chars.append(0x2ADA)  #uni2ADA	PITCHFORK WITH TEE TOP
        chars.append(0x2ADB)  #uni2ADB	TRANSVERSAL INTERSECTION
        chars.append(0x2ADC)  #uni2ADC	FORKING
        chars.append(0x2ADD)  #uni2ADD	NONFORKING
        chars.append(0x2ADE)  #uni2ADE	SHORT LEFT TACK
        chars.append(0x2ADF)  #uni2ADF	SHORT DOWN TACK
        chars.append(0x2AE0)  #uni2AE0	SHORT UP TACK
        chars.append(0x2AE1)  #uni2AE1	PERPENDICULAR WITH S
        chars.append(0x2AE2)  #uni2AE2	VERTICAL BAR TRIPLE RIGHT TURNSTILE
        chars.append(0x2AE3)  #uni2AE3	DOUBLE VERTICAL BAR LEFT TURNSTILE
        chars.append(0x2AE4)  #uni2AE4	VERTICAL BAR DOUBLE LEFT TURNSTILE
        chars.append(0x2AE5)  #uni2AE5	DOUBLE VERTICAL BAR DOUBLE LEFT TURNSTILE
        chars.append(0x2AE6)  #uni2AE6	LONG DASH FROM LEFT MEMBER OF DOUBLE VERTICAL
        chars.append(0x2AE7)  #uni2AE7	SHORT DOWN TACK WITH OVERBAR
        chars.append(0x2AE8)  #uni2AE8	SHORT UP TACK WITH UNDERBAR
        chars.append(0x2AE9)  #uni2AE9	SHORT UP TACK ABOVE SHORT DOWN TACK
        chars.append(0x2AEA)  #uni2AEA	DOUBLE DOWN TACK
        chars.append(0x2AEB)  #uni2AEB	DOUBLE UP TACK
        chars.append(0x2AEC)  #uni2AEC	DOUBLE STROKE NOT SIGN
        chars.append(0x2AED)  #uni2AED	REVERSED DOUBLE STROKE NOT SIGN
        chars.append(0x2AEE)  #uni2AEE	DOES NOT DIVIDE WITH REVERSED NEGATION SLASH
        chars.append(0x2AEF)  #uni2AEF	VERTICAL LINE WITH CIRCLE ABOVE
        chars.append(0x2AF0)  #uni2AF0	VERTICAL LINE WITH CIRCLE BELOW
        chars.append(0x2AF1)  #uni2AF1	DOWN TACK WITH CIRCLE BELOW
        chars.append(0x2AF2)  #uni2AF2	PARALLEL WITH HORIZONTAL STROKE
        chars.append(0x2AF3)  #uni2AF3	PARALLEL WITH TILDE OPERATOR
        chars.append(0x2AF4)  #uni2AF4	TRIPLE VERTICAL BAR BINARY RELATION
        chars.append(0x2AF5)  #uni2AF5	TRIPLE VERTICAL BAR WITH HORIZONTAL STROKE
        chars.append(0x2AF6)  #uni2AF6	TRIPLE COLON OPERATOR
        chars.append(0x2AF7)  #uni2AF7	TRIPLE NESTED LESS-THAN
        chars.append(0x2AF8)  #uni2AF8	TRIPLE NESTED GREATER-THAN
        chars.append(0x2AF9)  #uni2AF9	DOUBLE-LINE SLANTED LESS-THAN OR EQUAL TO
        chars.append(0x2AFA)  #uni2AFA	DOUBLE-LINE SLANTED GREATER-THAN OR EQUAL TO
        chars.append(0x2AFB)  #uni2AFB	TRIPLE SOLIDUS BINARY RELATION
        chars.append(0x2AFC)  #uni2AFC	LARGE TRIPLE VERTICAL BAR OPERATOR
        chars.append(0x2AFD)  #uni2AFD	DOUBLE SOLIDUS OPERATOR
        chars.append(0x2AFE)  #uni2AFE	WHITE VERTICAL BAR
        chars.append(0x2AFF)  #uni2AFF	N-ARY WHITE VERTICAL BAR
        chars.append(0x2B00)  #uni2B00	NORTH EAST WHITE ARROW
        chars.append(0x2B01)  #uni2B01	NORTH WEST WHITE ARROW
        chars.append(0x2B02)  #uni2B02	SOUTH EAST WHITE ARROW
        chars.append(0x2B03)  #uni2B03	SOUTH WEST WHITE ARROW
        chars.append(0x2B04)  #uni2B04	LEFT RIGHT WHITE ARROW
        chars.append(0x2B05)  #uni2B05	LEFTWARDS BLACK ARROW
        chars.append(0x2B06)  #uni2B06	UPWARDS BLACK ARROW
        chars.append(0x2B07)  #uni2B07	DOWNWARDS BLACK ARROW
        chars.append(0x2B08)  #uni2B08	NORTH EAST BLACK ARROW
        chars.append(0x2B09)  #uni2B09	NORTH WEST BLACK ARROW
        chars.append(0x2B0A)  #uni2B0A	SOUTH EAST BLACK ARROW
        chars.append(0x2B0B)  #uni2B0B	SOUTH WEST BLACK ARROW
        chars.append(0x2B0C)  #uni2B0C	LEFT RIGHT BLACK ARROW
        chars.append(0x2B0D)  #uni2B0D	UP DOWN BLACK ARROW
        chars.append(0x2B0E)  #uni2B0E	RIGHTWARDS ARROW WITH TIP DOWNWARDS
        chars.append(0x2B0F)  #uni2B0F	RIGHTWARDS ARROW WITH TIP UPWARDS
        chars.append(0x2B10)  #uni2B10	LEFTWARDS ARROW WITH TIP DOWNWARDS
        chars.append(0x2B11)  #uni2B11	LEFTWARDS ARROW WITH TIP UPWARDS
        chars.append(0x2B12)  #uni2B12	SQUARE WITH TOP HALF BLACK
        chars.append(0x2B13)  #uni2B13	SQUARE WITH BOTTOM HALF BLACK
        chars.append(0x2B14)  #uni2B14	SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK
        chars.append(0x2B15)  #uni2B15	SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK
        chars.append(0x2B16)  #uni2B16	DIAMOND WITH LEFT HALF BLACK
        chars.append(0x2B17)  #uni2B17	DIAMOND WITH RIGHT HALF BLACK
        chars.append(0x2B18)  #uni2B18	DIAMOND WITH TOP HALF BLACK
        chars.append(0x2B19)  #uni2B19	DIAMOND WITH BOTTOM HALF BLACK
        chars.append(0x2B1A)  #uni2B1A	DOTTED SQUARE
        chars.append(0x2B1B)  #uni2B1B	BLACK LARGE SQUARE
        chars.append(0x2B1C)  #uni2B1C	WHITE LARGE SQUARE
        chars.append(0x2B1D)  #uni2B1D	BLACK VERY SMALL SQUARE
        chars.append(0x2B1E)  #uni2B1E	WHITE VERY SMALL SQUARE
        chars.append(0x2B1F)  #uni2B1F	BLACK PENTAGON
        chars.append(0x2B20)  #uni2B20	WHITE PENTAGON
        chars.append(0x2B21)  #uni2B21	WHITE HEXAGON
        chars.append(0x2B22)  #uni2B22	BLACK HEXAGON
        chars.append(0x2B23)  #uni2B23	HORIZONTAL BLACK HEXAGON
        chars.append(0x2B24)  #uni2B24	BLACK LARGE CIRCLE
        chars.append(0x2B25)  #uni2B25	BLACK MEDIUM DIAMOND
        chars.append(0x2B26)  #uni2B26	WHITE MEDIUM DIAMOND
        chars.append(0x2B27)  #uni2B27	BLACK MEDIUM LOZENGE
        chars.append(0x2B28)  #uni2B28	WHITE MEDIUM LOZENGE
        chars.append(0x2B29)  #uni2B29	BLACK SMALL DIAMOND
        chars.append(0x2B2A)  #uni2B2A	BLACK SMALL LOZENGE
        chars.append(0x2B2B)  #uni2B2B	WHITE SMALL LOZENGE
        chars.append(0x2B2C)  #uni2B2C	BLACK HORIZONTAL ELLIPSE
        chars.append(0x2B2D)  #uni2B2D	WHITE HORIZONTAL ELLIPSE
        chars.append(0x2B2E)  #uni2B2E	BLACK VERTICAL ELLIPSE
        chars.append(0x2B2F)  #uni2B2F	WHITE VERTICAL ELLIPSE
        chars.append(0x2B30)  #uni2B30	LEFT ARROW WITH SMALL CIRCLE
        chars.append(0x2B31)  #uni2B31	THREE LEFTWARDS ARROWS
        chars.append(0x2B32)  #uni2B32	LEFT ARROW WITH CIRCLED PLUS
        chars.append(0x2B33)  #uni2B33	LONG LEFTWARDS SQUIGGLE ARROW
        chars.append(0x2B34)  #uni2B34	LEFTWARDS TWO-HEADED ARROW WITH VERTICAL STROKE
        chars.append(0x2B35)  #uni2B35	LEFTWARDS TWO-HEADED ARROW WITH DOUBLE VERTICAL STROKE
        chars.append(0x2B36)  #uni2B36	LEFTWARDS TWO-HEADED ARROW FROM BAR
        chars.append(0x2B37)  #uni2B37	LEFTWARDS TWO-HEADED TRIPLE DASH ARROW
        chars.append(0x2B38)  #uni2B38	LEFTWARDS ARROW WITH DOTTED STEM
        chars.append(0x2B39)  #uni2B39	LEFTWARDS ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2B3A)  #uni2B3A	LEFTWARDS ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2B3B)  #uni2B3B	LEFTWARDS TWO-HEADED ARROW WITH TAIL
        chars.append(0x2B3C)  #uni2B3C	LEFTWARDS TWO-HEADED ARROW WITH TAIL WITH VERTICAL STROKE
        chars.append(0x2B3D)  #uni2B3D	LEFTWARDS TWO-HEADED ARROW WITH TAIL WITH DOUBLE VERTICAL STROKE
        chars.append(0x2B3E)  #uni2B3E	LEFTWARDS ARROW THROUGH X
        chars.append(0x2B3F)  #uni2B3F	WAVE ARROW POINTING DIRECTLY LEFT
        chars.append(0x2B40)  #uni2B40	EQUALS SIGN ABOVE LEFTWARDS ARROW
        chars.append(0x2B41)  #uni2B41	REVERSE TILDE OPERATOR ABOVE LEFTWARDS ARROW
        chars.append(0x2B42)  #uni2B42	LEFTWARDS ARROW ABOVE REVERSE ALMOST EQUAL TO
        chars.append(0x2B43)  #uni2B43	RIGHTWARDS ARROW THROUGH GREATER-THAN
        chars.append(0x2B44)  #uni2B44	RIGHTWARDS ARROW THROUGH SUPERSET
        chars.append(0x2B45)  #uni2B45	LEFTWARDS QUADRUPLE ARROW
        chars.append(0x2B46)  #uni2B46	RIGHTWARDS QUADRUPLE ARROW
        chars.append(0x2B47)  #uni2B47	REVERSE TILDE OPERATOR ABOVE RIGHTWARDS ARROW
        chars.append(0x2B48)  #uni2B48	RIGHTWARDS ARROW ABOVE REVERSE ALMOST EQUAL TO
        chars.append(0x2B49)  #uni2B49	TILDE OPERATOR ABOVE LEFTWARDS ARROW
        chars.append(0x2B4A)  #uni2B4A	LEFTWARDS ARROW ABOVE ALMOST EQUAL TO
        chars.append(0x2B4B)  #uni2B4B	LEFTWARDS ARROW ABOVE REVERSE TILDE OPERATOR
        chars.append(0x2B4C)  #uni2B4C	RIGHTWARDS ARROW ABOVE REVERSE TILDE OPERATOR
        chars.append(0x101E2)  #glyph02913	PHAISTOS DISC SIGN CARPENTRY PLANE
        chars.append(0x2B50)  #uni2B50	WHITE MEDIUM STAR
        chars.append(0x2B51)  #uni2B51	BLACK SMALL STAR
        chars.append(0x2B52)  #uni2B52	WHITE SMALL STAR
        chars.append(0x2B53)  #uni2B53	BLACK RIGHT-POINTING PENTAGON
        chars.append(0x2B54)  #uni2B54	WHITE RIGHT-POINTING PENTAGON
        chars.append(0x2B55)  #uni2B55	HEAVY LARGE CIRCLE
        chars.append(0x2B56)  #uni2B56	HEAVY OVAL WITH OVAL INSIDE
        chars.append(0x2B57)  #uni2B57	HEAVY CIRCLE WITH CIRCLE INSIDE
        chars.append(0x2B58)  #uni2B58	HEAVY CIRCLE
        chars.append(0x2B59)  #uni2B59	HEAVY CIRCLED SALTIRE
        chars.append(0x1F73A)  #glyph05067	????
        chars.append(0x101E5)  #glyph02916	PHAISTOS DISC SIGN SLING
        chars.append(0x1F73B)  #glyph05068	????
        chars.append(0x101E6)  #glyph02917	PHAISTOS DISC SIGN COLUMN
        chars.append(0x1F73C)  #glyph05069	????
        chars.append(0x10116)  #glyph02769	AEGEAN NUMBER SEVENTY
        chars.append(0x1F032)  #glyph04624	DOMINO TILE HORIZONTAL-00-01
        chars.append(0x1F0D1)  #glyph04766	????
        chars.append(0x101E8)  #glyph02919	PHAISTOS DISC SIGN SHIP
        chars.append(0x1012E)  #glyph02793	AEGEAN NUMBER FORTY THOUSAND
        chars.append(0x1F73E)  #glyph05071	????
        chars.append(0x101E9)  #glyph02920	PHAISTOS DISC SIGN HORN
        chars.append(0x1F73F)  #glyph05072	????
        chars.append(0x101EA)  #glyph02921	PHAISTOS DISC SIGN HIDE
        chars.append(0x1F740)  #glyph05073	????
        chars.append(0x101EB)  #glyph02922	PHAISTOS DISC SIGN BULLS LEG
        chars.append(0x1F741)  #glyph05074	????
        chars.append(0x101EC)  #glyph02923	PHAISTOS DISC SIGN CAT
        chars.append(0x1F704)  #glyph05013	????
        chars.append(0x1F742)  #glyph05075	????
        chars.append(0x101ED)  #glyph02924	PHAISTOS DISC SIGN RAM
        chars.append(0x1012F)  #glyph02794	AEGEAN NUMBER FIFTY THOUSAND
        chars.append(0x1F743)  #glyph05076	????
        chars.append(0x101EE)  #glyph02925	PHAISTOS DISC SIGN EAGLE
        chars.append(0x1F200)  #glyph04952	SQUARE HIRAGANA HOKA
        chars.append(0x1F754)  #glyph05093	????
        chars.append(0x1F155)  #glyph04860	????
        chars.append(0x101EF)  #glyph02926	PHAISTOS DISC SIGN DOVE
        chars.append(0x1F0D6)  #glyph04771	????
        chars.append(0x1F745)  #glyph05078	????
        chars.append(0x101F0)  #glyph02927	PHAISTOS DISC SIGN TUNNY
        chars.append(0x1F746)  #glyph05079	????
        chars.append(0x101F1)  #glyph02928	PHAISTOS DISC SIGN BEE
        chars.append(0x1F747)  #glyph05080	????
        chars.append(0x101F2)  #glyph02929	PHAISTOS DISC SIGN PLANE TREE
        chars.append(0x10130)  #glyph02795	AEGEAN NUMBER SIXTY THOUSAND
        chars.append(0x1F748)  #glyph05081	????
        chars.append(0x101F3)  #glyph02930	PHAISTOS DISC SIGN VINE
        chars.append(0x1F749)  #glyph05082	????
        chars.append(0x101F4)  #glyph02931	PHAISTOS DISC SIGN PAPYRUS
        chars.append(0x1F74A)  #glyph05083	????
        chars.append(0x101F5)  #glyph02932	PHAISTOS DISC SIGN ROSETTE
        chars.append(0x1F74B)  #glyph05084	????
        chars.append(0x101F6)  #glyph02933	PHAISTOS DISC SIGN LILY
        chars.append(0x1D74C)  #glyph04400	MATHEMATICAL BOLD ITALIC SMALL CHI
        chars.append(0x101F7)  #glyph02934	PHAISTOS DISC SIGN OX BACK
        chars.append(0x10131)  #glyph02796	AEGEAN NUMBER SEVENTY THOUSAND
        chars.append(0x1F74D)  #glyph05086	????
        chars.append(0x101F8)  #glyph02935	PHAISTOS DISC SIGN FLUTE
        chars.append(0x1F74E)  #glyph05087	????
        chars.append(0x101F9)  #glyph02936	PHAISTOS DISC SIGN GRATER
        chars.append(0x1F74F)  #glyph05088	????
        chars.append(0x101FA)  #glyph02937	PHAISTOS DISC SIGN STRAINER
        chars.append(0x1F750)  #glyph05089	????
        chars.append(0x101FB)  #glyph02938	PHAISTOS DISC SIGN SMALL AXE
        chars.append(0x1F751)  #glyph05090	????
        chars.append(0x101FC)  #glyph02939	PHAISTOS DISC SIGN WAVY BAND
        chars.append(0x10132)  #glyph02797	AEGEAN NUMBER EIGHTY THOUSAND
        chars.append(0x1F752)  #glyph05091	????
        chars.append(0x101FD)  #glyph02940	PHAISTOS DISC SIGN COMBINING OBLIQUE STROKE
        chars.append(0x1F753)  #glyph05092	????
        chars.append(0x1F0A0)  #glyph04722	????
        chars.append(0x1D754)  #glyph04408	MATHEMATICAL BOLD ITALIC RHO SYMBOL
        chars.append(0x1F755)  #glyph05094	????
        chars.append(0x10117)  #glyph02770	AEGEAN NUMBER EIGHTY
        chars.append(0x1F033)  #glyph04625	DOMINO TILE HORIZONTAL-00-02
        chars.append(0x1F756)  #glyph05095	????
        chars.append(0x1F201)  #glyph04953	????
        chars.append(0x10133)  #glyph02798	AEGEAN NUMBER NINETY THOUSAND
        chars.append(0x1F757)  #glyph05096	????
        chars.append(0x1F202)  #glyph04954	????
        chars.append(0x1F758)  #glyph05097	????
        chars.append(0x1F759)  #glyph05098	????
        chars.append(0x1F72B)  #glyph05052	????
        chars.append(0x1F75A)  #glyph05099	????
        chars.append(0x1F705)  #glyph05014	????
        chars.append(0x1F75B)  #glyph05100	????
        chars.append(0x1F144)  #glyph04843	????
        chars.append(0x1D75C)  #glyph04416	MATHEMATICAL SANS-SERIF BOLD CAPITAL ETA
        chars.append(0x1F75D)  #glyph05102	????
        chars.append(0x1F0D7)  #glyph04772	????
        chars.append(0x1F75E)  #glyph05103	????
        chars.append(0x1F75F)  #glyph05104	????
        chars.append(0x1F760)  #glyph05105	????
        chars.append(0x1F761)  #glyph05106	????
        chars.append(0x1F762)  #glyph05107	????
        chars.append(0x1F763)  #glyph05108	????
        chars.append(0x1F736)  #glyph05063	????
        chars.append(0x1F764)  #glyph05109	????
        chars.append(0x1F765)  #glyph05110	????
        chars.append(0x1F210)  #glyph04955	SQUARED CJK UNIFIED IDEOGRAPH-624B
        chars.append(0x1F766)  #glyph05111	????
        chars.append(0x1F211)  #glyph04956	SQUARED CJK UNIFIED IDEOGRAPH-5B57
        chars.append(0x1F767)  #glyph05112	????
        chars.append(0x1F212)  #glyph04957	SQUARED CJK UNIFIED IDEOGRAPH-53CC
        chars.append(0x1F768)  #glyph05113	????
        chars.append(0x1F213)  #glyph04958	SQUARED KATAKANA DE
        chars.append(0x1F769)  #glyph05114	????
        chars.append(0x1F214)  #glyph04959	SQUARED CJK UNIFIED IDEOGRAPH-4E8C
        chars.append(0x1D76A)  #glyph04430	MATHEMATICAL SANS-SERIF BOLD CAPITAL UPSILON
        chars.append(0x1F215)  #glyph04960	SQUARED CJK UNIFIED IDEOGRAPH-591A
        chars.append(0x10137)  #glyph02799	AEGEAN WEIGHT BASE UNIT
        chars.append(0x1F76B)  #glyph05116	????
        chars.append(0x1F216)  #glyph04961	SQUARED CJK UNIFIED IDEOGRAPH-89E3
        chars.append(0x1F75C)  #glyph05101	????
        chars.append(0x1F76C)  #glyph05117	????
        chars.append(0x1F0A1)  #glyph04723	????
        chars.append(0x1F217)  #glyph04962	SQUARED CJK UNIFIED IDEOGRAPH-5929
        chars.append(0x1F76D)  #glyph05118	????
        chars.append(0x1F218)  #glyph04963	SQUARED CJK UNIFIED IDEOGRAPH-4EA4
        chars.append(0x1F76E)  #glyph05119	????
        chars.append(0x10118)  #glyph02771	AEGEAN NUMBER NINETY
        chars.append(0x1F034)  #glyph04626	DOMINO TILE HORIZONTAL-00-03
        chars.append(0x1F76F)  #glyph05120	????
        chars.append(0x1F21A)  #glyph04965	SQUARED CJK UNIFIED IDEOGRAPH-7121
        chars.append(0x10138)  #glyph02800	AEGEAN WEIGHT FIRST SUBUNIT
        chars.append(0x1F770)  #glyph05121	????
        chars.append(0x1F21B)  #glyph04966	SQUARED CJK UNIFIED IDEOGRAPH-6599
        chars.append(0x1F771)  #glyph05122	????
        chars.append(0x1F21C)  #glyph04967	SQUARED CJK UNIFIED IDEOGRAPH-524D
        chars.append(0x1F72F)  #glyph05056	????
        chars.append(0x1F21D)  #glyph04968	SQUARED CJK UNIFIED IDEOGRAPH-5F8C
        chars.append(0x1F773)  #glyph05124	????
        chars.append(0x1F21E)  #glyph04969	SQUARED CJK UNIFIED IDEOGRAPH-518D
        chars.append(0x1F706)  #glyph05015	????
        chars.append(0x1F145)  #glyph04844	????
        chars.append(0x10139)  #glyph02801	AEGEAN WEIGHT SECOND SUBUNIT
        chars.append(0x1F220)  #glyph04971	SQUARED CJK UNIFIED IDEOGRAPH-521D
        chars.append(0x1F221)  #glyph04972	SQUARED CJK UNIFIED IDEOGRAPH-7D42
        chars.append(0x1F0D8)  #glyph04773	????
        chars.append(0x1F222)  #glyph04973	SQUARED CJK UNIFIED IDEOGRAPH-751F
        chars.append(0x1F223)  #glyph04974	SQUARED CJK UNIFIED IDEOGRAPH-8CA9
        chars.append(0x1F224)  #glyph04975	SQUARED CJK UNIFIED IDEOGRAPH-58F0
        chars.append(0x1013A)  #glyph02802	AEGEAN WEIGHT THIRD SUBUNIT
        chars.append(0x1D77A)  #glyph04446	MATHEMATICAL SANS-SERIF BOLD SMALL LAMDA
        chars.append(0x1F225)  #glyph04976	SQUARED CJK UNIFIED IDEOGRAPH-5439
        chars.append(0x1F74C)  #glyph05085	????
        chars.append(0x1F11C)  #glyph04804	PARENTHESIZED LATIN CAPITAL LETTER M
        chars.append(0x1F226)  #glyph04977	SQUARED CJK UNIFIED IDEOGRAPH-6F14
        chars.append(0x1F227)  #glyph04978	SQUARED CJK UNIFIED IDEOGRAPH-6295
        chars.append(0x1F228)  #glyph04979	SQUARED CJK UNIFIED IDEOGRAPH-6355
        chars.append(0x1F229)  #glyph04980	SQUARED CJK UNIFIED IDEOGRAPH-4E00
        chars.append(0x1F058)  #glyph04662	DOMINO TILE HORIZONTAL-05-04
        chars.append(0x1013B)  #glyph02803	AEGEAN WEIGHT FOURTH SUBUNIT
        chars.append(0x1F22A)  #glyph04981	SQUARED CJK UNIFIED IDEOGRAPH-4E09
        chars.append(0x1F22B)  #glyph04982	SQUARED CJK UNIFIED IDEOGRAPH-904A
        chars.append(0x1F22C)  #glyph04983	SQUARED CJK UNIFIED IDEOGRAPH-5DE6
        chars.append(0x1F22D)  #glyph04984	SQUARED CJK UNIFIED IDEOGRAPH-4E2D
        chars.append(0x1F22E)  #glyph04985	SQUARED CJK UNIFIED IDEOGRAPH-53F3
        chars.append(0x1013C)  #glyph02804	AEGEAN DRY MEASURE FIRST SUBUNIT
        chars.append(0x1F156)  #glyph04861	????
        chars.append(0x1F22F)  #glyph04986	SQUARED CJK UNIFIED IDEOGRAPH-6307
        chars.append(0x1F0A2)  #glyph04724	????
        chars.append(0x1F230)  #glyph04987	SQUARED CJK UNIFIED IDEOGRAPH-8D70
        chars.append(0x1F231)  #glyph04988	SQUARED CJK UNIFIED IDEOGRAPH-6253
        chars.append(0x10107)  #glyph02754	AEGEAN NUMBER ONE
        chars.append(0x10119)  #glyph02772	AEGEAN NUMBER ONE HUNDRED
        chars.append(0x1F035)  #glyph04627	DOMINO TILE HORIZONTAL-00-04
        chars.append(0x1D788)  #glyph04460	MATHEMATICAL SANS-SERIF BOLD SMALL OMEGA
        chars.append(0x1F233)  #glyph04990	????
        chars.append(0x1013D)  #glyph02805	AEGEAN LIQUID MEASURE FIRST SUBUNIT
        chars.append(0x1F11E)  #glyph04806	PARENTHESIZED LATIN CAPITAL LETTER O
        chars.append(0x1F234)  #glyph04991	????
        chars.append(0x1F0CE)  #glyph04764	????
        chars.append(0x1F235)  #glyph04992	????
        chars.append(0x1F236)  #glyph04993	????
        chars.append(0x1F0C8)  #glyph04758	????
        chars.append(0x1F237)  #glyph04994	????
        chars.append(0x1F707)  #glyph05016	????
        chars.append(0x1F146)  #glyph04845	SQUARED LATIN CAPITAL LETTER W
        chars.append(0x1013E)  #glyph02806	AEGEAN MEASURE SECOND SUBUNIT
        chars.append(0x1F239)  #glyph04996	????
        chars.append(0x1F13E)  #glyph04837	????
        chars.append(0x1F0D9)  #glyph04774	????
        chars.append(0x10112)  #glyph02765	AEGEAN NUMBER THIRTY
        chars.append(0x1013F)  #glyph02807	AEGEAN MEASURE THIRD SUBUNIT
        chars.append(0x1F240)  #glyph04998	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-672C
        chars.append(0x1F73D)  #glyph05070	????
        chars.append(0x1F241)  #glyph04999	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-4E09
        chars.append(0x1D710)  #glyph04340	MATHEMATICAL ITALIC SMALL UPSILON
        chars.append(0x1F242)  #glyph05000	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-4E8C
        chars.append(0x1F100)  #glyph04781	DIGIT ZERO FULL STOP
        chars.append(0x10140)  #glyph02808	GREEK ACROPHONIC ATTIC ONE QUARTER
        chars.append(0x1D798)  #glyph04476	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL IOTA
        chars.append(0x1F178)  #glyph04891	????
        chars.append(0x1F0B1)  #glyph04737	????
        chars.append(0x1F244)  #glyph05002	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-70B9
        chars.append(0x1F245)  #glyph05003	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-6253
        chars.append(0x1F101)  #glyph04782	DIGIT ZERO COMMA
        chars.append(0x10141)  #glyph02809	GREEK ACROPHONIC ATTIC ONE HALF
        chars.append(0x1F0A3)  #glyph04725	????
        chars.append(0x4DC0)  #uni4DC0	HEXAGRAM FOR THE CREATIVE HEAVEN
        chars.append(0x4DC1)  #uni4DC1	HEXAGRAM FOR THE RECEPTIVE EARTH
        chars.append(0x4DC2)  #uni4DC2	HEXAGRAM FOR DIFFICULTY AT THE BEGINNING
        chars.append(0x4DC3)  #uni4DC3	HEXAGRAM FOR YOUTHFUL FOLLY
        chars.append(0x4DC4)  #uni4DC4	HEXAGRAM FOR WAITING
        chars.append(0x4DC5)  #uni4DC5	HEXAGRAM FOR CONFLICT
        chars.append(0x4DC6)  #uni4DC6	HEXAGRAM FOR THE ARMY
        chars.append(0x4DC7)  #uni4DC7	HEXAGRAM FOR HOLDING TOGETHER
        chars.append(0x4DC8)  #uni4DC8	HEXAGRAM FOR SMALL TAMING
        chars.append(0x4DC9)  #uni4DC9	HEXAGRAM FOR TREADING
        chars.append(0x4DCA)  #uni4DCA	HEXAGRAM FOR PEACE
        chars.append(0x4DCB)  #uni4DCB	HEXAGRAM FOR STANDSTILL
        chars.append(0x4DCC)  #uni4DCC	HEXAGRAM FOR FELLOWSHIP
        chars.append(0x4DCD)  #uni4DCD	HEXAGRAM FOR GREAT POSSESSION
        chars.append(0x4DCE)  #uni4DCE	HEXAGRAM FOR MODESTY
        chars.append(0x4DCF)  #uni4DCF	HEXAGRAM FOR ENTHUSIASM
        chars.append(0x4DD0)  #uni4DD0	HEXAGRAM FOR FOLLOWING
        chars.append(0x4DD1)  #uni4DD1	HEXAGRAM FOR WORK ON THE DECAYED
        chars.append(0x4DD2)  #uni4DD2	HEXAGRAM FOR APPROACH
        chars.append(0x4DD3)  #uni4DD3	HEXAGRAM FOR CONTEMPLATION
        chars.append(0x4DD4)  #uni4DD4	HEXAGRAM FOR BITING THROUGH
        chars.append(0x4DD5)  #uni4DD5	HEXAGRAM FOR GRACE
        chars.append(0x4DD6)  #uni4DD6	HEXAGRAM FOR SPLITTING APART
        chars.append(0x4DD7)  #uni4DD7	HEXAGRAM FOR RETURN
        chars.append(0x4DD8)  #uni4DD8	HEXAGRAM FOR INNOCENCE
        chars.append(0x4DD9)  #uni4DD9	HEXAGRAM FOR GREAT TAMING
        chars.append(0x4DDA)  #uni4DDA	HEXAGRAM FOR MOUTH CORNERS
        chars.append(0x4DDB)  #uni4DDB	HEXAGRAM FOR GREAT PREPONDERANCE
        chars.append(0x4DDC)  #uni4DDC	HEXAGRAM FOR THE ABYSMAL WATER
        chars.append(0x4DDD)  #uni4DDD	HEXAGRAM FOR THE CLINGING FIRE
        chars.append(0x4DDE)  #uni4DDE	HEXAGRAM FOR INFLUENCE
        chars.append(0x4DDF)  #uni4DDF	HEXAGRAM FOR DURATION
        chars.append(0x4DE0)  #uni4DE0	HEXAGRAM FOR RETREAT
        chars.append(0x4DE1)  #uni4DE1	HEXAGRAM FOR GREAT POWER
        chars.append(0x4DE2)  #uni4DE2	HEXAGRAM FOR PROGRESS
        chars.append(0x4DE3)  #uni4DE3	HEXAGRAM FOR DARKENING OF THE LIGHT
        chars.append(0x4DE4)  #uni4DE4	HEXAGRAM FOR THE FAMILY
        chars.append(0x4DE5)  #uni4DE5	HEXAGRAM FOR OPPOSITION
        chars.append(0x4DE6)  #uni4DE6	HEXAGRAM FOR OBSTRUCTION
        chars.append(0x4DE7)  #uni4DE7	HEXAGRAM FOR DELIVERANCE
        chars.append(0x4DE8)  #uni4DE8	HEXAGRAM FOR DECREASE
        chars.append(0x4DE9)  #uni4DE9	HEXAGRAM FOR INCREASE
        chars.append(0x4DEA)  #uni4DEA	HEXAGRAM FOR BREAKTHROUGH
        chars.append(0x4DEB)  #uni4DEB	HEXAGRAM FOR COMING TO MEET
        chars.append(0x4DEC)  #uni4DEC	HEXAGRAM FOR GATHERING TOGETHER
        chars.append(0x4DED)  #uni4DED	HEXAGRAM FOR PUSHING UPWARD
        chars.append(0x4DEE)  #uni4DEE	HEXAGRAM FOR OPPRESSION
        chars.append(0x4DEF)  #uni4DEF	HEXAGRAM FOR THE WELL
        chars.append(0x4DF0)  #uni4DF0	HEXAGRAM FOR REVOLUTION
        chars.append(0x4DF1)  #uni4DF1	HEXAGRAM FOR THE CAULDRON
        chars.append(0x4DF2)  #uni4DF2	HEXAGRAM FOR THE AROUSING THUNDER
        chars.append(0x4DF3)  #uni4DF3	HEXAGRAM FOR THE KEEPING STILL MOUNTAIN
        chars.append(0x4DF4)  #uni4DF4	HEXAGRAM FOR DEVELOPMENT
        chars.append(0x4DF5)  #uni4DF5	HEXAGRAM FOR THE MARRYING MAIDEN
        chars.append(0x4DF6)  #uni4DF6	HEXAGRAM FOR ABUNDANCE
        chars.append(0x4DF7)  #uni4DF7	HEXAGRAM FOR THE WANDERER
        chars.append(0x4DF8)  #uni4DF8	HEXAGRAM FOR THE GENTLE WIND
        chars.append(0x4DF9)  #uni4DF9	HEXAGRAM FOR THE JOYOUS LAKE
        chars.append(0x4DFA)  #uni4DFA	HEXAGRAM FOR DISPERSION
        chars.append(0x4DFB)  #uni4DFB	HEXAGRAM FOR LIMITATION
        chars.append(0x4DFC)  #uni4DFC	HEXAGRAM FOR INNER TRUTH
        chars.append(0x4DFD)  #uni4DFD	HEXAGRAM FOR SMALL PREPONDERANCE
        chars.append(0x4DFE)  #uni4DFE	HEXAGRAM FOR AFTER COMPLETION
        chars.append(0x4DFF)  #uni4DFF	HEXAGRAM FOR BEFORE COMPLETION
        chars.append(0x2E00)  #uni2E00	RIGHT ANGLE SUBSTITUTION MARKER
        chars.append(0x2E01)  #uni2E01	RIGHT ANGLE DOTTED SUBSTITUTION MARKER
        chars.append(0x2E02)  #uni2E02	LEFT SUBSTITUTION BRACKET
        chars.append(0x2E03)  #uni2E03	RIGHT SUBSTITUTION BRACKET
        chars.append(0x2E04)  #uni2E04	LEFT DOTTED SUBSTITUTION BRACKET
        chars.append(0x2E05)  #uni2E05	RIGHT DOTTED SUBSTITUTION BRACKET
        chars.append(0x2E06)  #uni2E06	RAISED INTERPOLATION MARKER
        chars.append(0x2E07)  #uni2E07	RAISED DOTTED INTERPOLATION MARKER
        chars.append(0x2E08)  #uni2E08	DOTTED TRANSPOSITION MARKER
        chars.append(0x2E09)  #uni2E09	LEFT TRANSPOSITION BRACKET
        chars.append(0x2E0A)  #uni2E0A	RIGHT TRANSPOSITION BRACKET
        chars.append(0x2E0B)  #uni2E0B	RAISED SQUARE
        chars.append(0x2E0C)  #uni2E0C	LEFT RAISED OMISSION BRACKET
        chars.append(0x2E0D)  #uni2E0D	RIGHT RAISED OMISSION BRACKET
        chars.append(0x2E0E)  #uni2E0E	EDITORIAL CORONIS
        chars.append(0x2E0F)  #uni2E0F	PARAGRAPHOS
        chars.append(0x2E10)  #uni2E10	FORKED PARAGRAPHOS
        chars.append(0x2E11)  #uni2E11	REVERSED FORKED PARAGRAPHOS
        chars.append(0x2E12)  #uni2E12	HYPODIASTOLE
        chars.append(0x2E13)  #uni2E13	DOTTED OBELOS
        chars.append(0x2E14)  #uni2E14	DOWNWARDS ANCORA
        chars.append(0x2E15)  #uni2E15	UPWARDS ANCORA
        chars.append(0x2E16)  #uni2E16	DOTTED RIGHT-POINTING ANGLE
        chars.append(0x2E17)  #uni2E17	DOUBLE OBLIQUE HYPHEN
        chars.append(0x2E18)  #uni2E18	INVERTED INTERROBANG
        chars.append(0x2E19)  #uni2E19	PALM BRANCH
        chars.append(0x2E1A)  #uni2E1A	HYPHEN WITH DIAERESIS
        chars.append(0x2E1B)  #uni2E1B	TILDE WITH RING ABOVE
        chars.append(0x2E1C)  #uni2E1C	LEFT LOW PARAPHRASE BRACKET
        chars.append(0x2E1D)  #uni2E1D	RIGHT LOW PARAPHRASE BRACKET
        chars.append(0x2E1E)  #uni2E1E	TILDE WITH DOT ABOVE
        chars.append(0x2E1F)  #uni2E1F	TILDE WITH DOT BELOW
        chars.append(0x2E20)  #uni2E20	LEFT VERTICAL BAR WITH QUILL
        chars.append(0x2E21)  #uni2E21	RIGHT VERTICAL BAR WITH QUILL
        chars.append(0x2E22)  #uni2E22	TOP LEFT HALF BRACKET
        chars.append(0x2E23)  #uni2E23	TOP RIGHT HALF BRACKET
        chars.append(0x2E24)  #uni2E24	BOTTOM LEFT HALF BRACKET
        chars.append(0x2E25)  #uni2E25	BOTTOM RIGHT HALF BRACKET
        chars.append(0x2E26)  #uni2E26	LEFT SIDEWAYS U BRACKET
        chars.append(0x2E27)  #uni2E27	RIGHT SIDEWAYS U BRACKET
        chars.append(0x2E28)  #uni2E28	LEFT DOUBLE PARENTHESIS
        chars.append(0x2E29)  #uni2E29	RIGHT DOUBLE PARENTHESIS
        chars.append(0x2E2A)  #uni2E2A	TWO DOTS OVER ONE DOT PUNCTUATION
        chars.append(0x2E2B)  #uni2E2B	ONE DOT OVER TWO DOTS PUNCTUATION
        chars.append(0x2E2C)  #uni2E2C	SQUARED FOUR DOT PUNCTUATION
        chars.append(0x2E2D)  #uni2E2D	FIVE DOT MARK
        chars.append(0x2E2E)  #uni2E2E	REVERSED QUESTION MARK
        chars.append(0x2E2F)  #uni2E2F	VERTICAL TILDE
        chars.append(0x2E30)  #uni2E30	RING POINT
        chars.append(0x2E31)  #uni2E31	WORD SEPARATOR MIDDLE DOT
        chars.append(0x2E32)  #uni2E32	????
        chars.append(0x2E33)  #uni2E33	????
        chars.append(0x2E34)  #uni2E34	????
        chars.append(0x2E35)  #uni2E35	????
        chars.append(0x2E36)  #uni2E36	????
        chars.append(0x2E37)  #uni2E37	????
        chars.append(0x2E38)  #uni2E38	????
        chars.append(0x2E39)  #uni2E39	????
        chars.append(0x2E3A)  #uni2E3A	????
        chars.append(0x2E3B)  #uni2E3B	????
        chars.append(0x1F106)  #glyph04787	DIGIT FIVE COMMA
        chars.append(0x10146)  #glyph02814	GREEK ACROPHONIC ATTIC FIVE THOUSAND
        chars.append(0x1D7B6)  #glyph04506	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL NU
        chars.append(0x1F0A4)  #glyph04726	????
        chars.append(0x1011B)  #glyph02774	AEGEAN NUMBER THREE HUNDRED
        chars.append(0x1F037)  #glyph04629	DOMINO TILE HORIZONTAL-00-06
        chars.append(0x1F0D2)  #glyph04767	????
        chars.append(0x1F107)  #glyph04788	DIGIT SIX COMMA
        chars.append(0x10147)  #glyph02815	GREEK ACROPHONIC ATTIC FIFTY THOUSAND
        chars.append(0x1D7BE)  #glyph04514	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL UPSILON
        chars.append(0x1F709)  #glyph05018	????
        chars.append(0x1F148)  #glyph04847	????
        chars.append(0x1F108)  #glyph04789	DIGIT SEVEN COMMA
        chars.append(0x10148)  #glyph02816	GREEK ACROPHONIC ATTIC FIVE TALENTS
        chars.append(0x1F121)  #glyph04809	PARENTHESIZED LATIN CAPITAL LETTER R
        chars.append(0x1F219)  #glyph04964	SQUARED CJK UNIFIED IDEOGRAPH-6620
        chars.append(0x1F0DB)  #glyph04776	????
        chars.append(0x1D7C4)  #glyph04520	MATHEMATICAL SANS-SERIF BOLD ITALIC EPSILON SYMBOL
        chars.append(0x1F109)  #glyph04790	DIGIT EIGHT COMMA
        chars.append(0x10149)  #glyph02817	GREEK ACROPHONIC ATTIC TEN TALENTS
        chars.append(0x1F238)  #glyph04995	????
        chars.append(0x1F11B)  #glyph04803	PARENTHESIZED LATIN CAPITAL LETTER L
        chars.append(0x1F10A)  #glyph04791	DIGIT NINE COMMA
        chars.append(0x1014A)  #glyph02818	GREEK ACROPHONIC ATTIC FIFTY TALENTS
        chars.append(0x1014B)  #glyph02819	GREEK ACROPHONIC ATTIC ONE HUNDRED TALENTS
        chars.append(0x1F08D)  #glyph04715	DOMINO TILE VERTICAL-06-00
        chars.append(0x1F0A5)  #glyph04727	????
        chars.append(0x1011C)  #glyph02775	AEGEAN NUMBER FOUR HUNDRED
        chars.append(0x1F038)  #glyph04630	DOMINO TILE HORIZONTAL-01-00
        chars.append(0x1F0C5)  #glyph04755	????
        chars.append(0x10145)  #glyph02813	GREEK ACROPHONIC ATTIC FIVE HUNDRED
        chars.append(0x1014C)  #glyph02820	GREEK ACROPHONIC ATTIC FIVE HUNDRED TALENTS
        chars.append(0x1D7D4)  #glyph04534	MATHEMATICAL BOLD DIGIT SIX
        chars.append(0x1F735)  #glyph05062	????
        chars.append(0x1F72C)  #glyph05053	????
        chars.append(0x1F70A)  #glyph05019	????
        chars.append(0x1F149)  #glyph04848	????
        chars.append(0x1014D)  #glyph02821	GREEK ACROPHONIC ATTIC ONE THOUSAND TALENTS
        chars.append(0x1F71A)  #glyph05035	????
        chars.append(0x1F772)  #glyph05123	????
        chars.append(0x1F0DC)  #glyph04777	????
        chars.append(0x1F14B)  #glyph04850	SQUARED MV
        chars.append(0x1014E)  #glyph02822	GREEK ACROPHONIC ATTIC FIVE THOUSAND TALENTS
        chars.append(0x1F21F)  #glyph04970	SQUARED CJK UNIFIED IDEOGRAPH-65B0
        chars.append(0x1F714)  #glyph05029	????
        chars.append(0x1F737)  #glyph05064	????
        chars.append(0x1D7E2)  #glyph04548	MATHEMATICAL SANS-SERIF DIGIT ZERO
        chars.append(0x1014F)  #glyph02823	GREEK ACROPHONIC ATTIC FIVE STATERS
        chars.append(0x1F732)  #glyph05059	????
        chars.append(0x1F702)  #glyph05011	????
        chars.append(0x1F110)  #glyph04792	PARENTHESIZED LATIN CAPITAL LETTER A
        chars.append(0x1D7E8)  #glyph04554	MATHEMATICAL SANS-SERIF DIGIT SIX
        chars.append(0x1F0A6)  #glyph04728	????
        chars.append(0x1011D)  #glyph02776	AEGEAN NUMBER FIVE HUNDRED
        chars.append(0x1F039)  #glyph04631	DOMINO TILE HORIZONTAL-01-01
        chars.append(0x1F111)  #glyph04793	PARENTHESIZED LATIN CAPITAL LETTER B
        chars.append(0x1F00E)  #glyph04592	MAHJONG TILE EIGHT OF CHARACTERS
        chars.append(0x1F140)  #glyph04839	????
        chars.append(0x1F70B)  #glyph05020	????
        chars.append(0x1F14A)  #glyph04849	SQUARED HV
        chars.append(0x1F112)  #glyph04794	PARENTHESIZED LATIN CAPITAL LETTER C
        chars.append(0x1D7F2)  #glyph04564	MATHEMATICAL SANS-SERIF BOLD DIGIT SIX
        chars.append(0x1F0DD)  #glyph04778	????
        chars.append(0x1F002)  #glyph04580	MAHJONG TILE WEST WIND
        chars.append(0x1F113)  #glyph04795	PARENTHESIZED LATIN CAPITAL LETTER D
        chars.append(0x1F114)  #glyph04796	PARENTHESIZED LATIN CAPITAL LETTER E
        chars.append(0x1D000)  #glyph02941	BYZANTINE MUSICAL SYMBOL PSILI
        chars.append(0x1D001)  #glyph02942	BYZANTINE MUSICAL SYMBOL DASEIA
        chars.append(0x1D002)  #glyph02943	BYZANTINE MUSICAL SYMBOL PERISPOMENI
        chars.append(0x1D003)  #glyph02944	BYZANTINE MUSICAL SYMBOL OXEIA EKFONITIKON
        chars.append(0x1D004)  #glyph02945	BYZANTINE MUSICAL SYMBOL OXEIA DIPLI
        chars.append(0x1D005)  #glyph02946	BYZANTINE MUSICAL SYMBOL VAREIA EKFONITIKON
        chars.append(0x1D006)  #glyph02947	BYZANTINE MUSICAL SYMBOL VAREIA DIPLI
        chars.append(0x1D007)  #glyph02948	BYZANTINE MUSICAL SYMBOL KATHISTI
        chars.append(0x3008)  #uni3008	LEFT ANGLE BRACKET
        chars.append(0x3009)  #uni3009	RIGHT ANGLE BRACKET
        chars.append(0x1D00A)  #glyph02951	BYZANTINE MUSICAL SYMBOL YPOKRISIS
        chars.append(0x1D00B)  #glyph02952	BYZANTINE MUSICAL SYMBOL YPOKRISIS DIPLI
        chars.append(0x1D00C)  #glyph02953	BYZANTINE MUSICAL SYMBOL KREMASTI
        chars.append(0x1D00D)  #glyph02954	BYZANTINE MUSICAL SYMBOL APESO EKFONITIKON
        chars.append(0x1D00E)  #glyph02955	BYZANTINE MUSICAL SYMBOL EXO EKFONITIKON
        chars.append(0x1D00F)  #glyph02956	BYZANTINE MUSICAL SYMBOL TELEIA
        chars.append(0x1D010)  #glyph02957	BYZANTINE MUSICAL SYMBOL KENTIMATA
        chars.append(0x1D011)  #glyph02958	BYZANTINE MUSICAL SYMBOL APOSTROFOS
        chars.append(0x1D012)  #glyph02959	BYZANTINE MUSICAL SYMBOL APOSTROFOS DIPLI
        chars.append(0x1D013)  #glyph02960	BYZANTINE MUSICAL SYMBOL SYNEVMA
        chars.append(0x1D014)  #glyph02961	BYZANTINE MUSICAL SYMBOL THITA
        chars.append(0x1D015)  #glyph02962	BYZANTINE MUSICAL SYMBOL OLIGON ARCHAION
        chars.append(0x10108)  #glyph02755	AEGEAN NUMBER TWO
        chars.append(0x1D017)  #glyph02964	BYZANTINE MUSICAL SYMBOL PSILON
        chars.append(0x1D018)  #glyph02965	BYZANTINE MUSICAL SYMBOL CHAMILON
        chars.append(0x1D019)  #glyph02966	BYZANTINE MUSICAL SYMBOL VATHY
        chars.append(0x1D01A)  #glyph02967	BYZANTINE MUSICAL SYMBOL ISON ARCHAION
        chars.append(0x1011E)  #glyph02777	AEGEAN NUMBER SIX HUNDRED
        chars.append(0x1D01C)  #glyph02969	BYZANTINE MUSICAL SYMBOL KENTIMATA ARCHAION
        chars.append(0x1D01D)  #glyph02970	BYZANTINE MUSICAL SYMBOL SAXIMATA
        chars.append(0x1D01E)  #glyph02971	BYZANTINE MUSICAL SYMBOL PARICHON
        chars.append(0x1D01F)  #glyph02972	BYZANTINE MUSICAL SYMBOL STAVROS APODEXIA
        chars.append(0x1D020)  #glyph02973	BYZANTINE MUSICAL SYMBOL OXEIAI ARCHAION
        chars.append(0x1010E)  #glyph02761	AEGEAN NUMBER EIGHT
        chars.append(0x1D022)  #glyph02975	BYZANTINE MUSICAL SYMBOL APODERMA ARCHAION
        chars.append(0x1D023)  #glyph02976	BYZANTINE MUSICAL SYMBOL APOTHEMA
        chars.append(0x1D024)  #glyph02977	BYZANTINE MUSICAL SYMBOL KLASMA
        chars.append(0x1D025)  #glyph02978	BYZANTINE MUSICAL SYMBOL REVMA
        chars.append(0x1D026)  #glyph02979	BYZANTINE MUSICAL SYMBOL PIASMA ARCHAION
        chars.append(0x1D027)  #glyph02980	BYZANTINE MUSICAL SYMBOL TINAGMA
        chars.append(0x1D028)  #glyph02981	BYZANTINE MUSICAL SYMBOL ANATRICHISMA
        chars.append(0x1D029)  #glyph02982	BYZANTINE MUSICAL SYMBOL SEISMA
        chars.append(0x1D02A)  #glyph02983	BYZANTINE MUSICAL SYMBOL SYNAGMA ARCHAION
        chars.append(0x1D02B)  #glyph02984	BYZANTINE MUSICAL SYMBOL SYNAGMA META STAVROU
        chars.append(0x1D02C)  #glyph02985	BYZANTINE MUSICAL SYMBOL OYRANISMA ARCHAION
        chars.append(0x1D02D)  #glyph02986	BYZANTINE MUSICAL SYMBOL THEMA
        chars.append(0x1D02E)  #glyph02987	BYZANTINE MUSICAL SYMBOL LEMOI
        chars.append(0x1D02F)  #glyph02988	BYZANTINE MUSICAL SYMBOL DYO
        chars.append(0x1D030)  #glyph02989	BYZANTINE MUSICAL SYMBOL TRIA
        chars.append(0x1D031)  #glyph02990	BYZANTINE MUSICAL SYMBOL TESSERA
        chars.append(0x1D032)  #glyph02991	BYZANTINE MUSICAL SYMBOL KRATIMATA
        chars.append(0x1D033)  #glyph02992	BYZANTINE MUSICAL SYMBOL APESO EXO NEO
        chars.append(0x1D034)  #glyph02993	BYZANTINE MUSICAL SYMBOL FTHORA ARCHAION
        chars.append(0x1D035)  #glyph02994	BYZANTINE MUSICAL SYMBOL IMIFTHORA
        chars.append(0x1D036)  #glyph02995	BYZANTINE MUSICAL SYMBOL TROMIKON ARCHAION
        chars.append(0x1D037)  #glyph02996	BYZANTINE MUSICAL SYMBOL KATAVA TROMIKON
        chars.append(0x1D038)  #glyph02997	BYZANTINE MUSICAL SYMBOL PELASTON
        chars.append(0x1D039)  #glyph02998	BYZANTINE MUSICAL SYMBOL PSIFISTON
        chars.append(0x1D03A)  #glyph02999	BYZANTINE MUSICAL SYMBOL KONTEVMA
        chars.append(0x1D03B)  #glyph03000	BYZANTINE MUSICAL SYMBOL CHOREVMA ARCHAION
        chars.append(0x1D03C)  #glyph03001	BYZANTINE MUSICAL SYMBOL RAPISMA
        chars.append(0x1D03D)  #glyph03002	BYZANTINE MUSICAL SYMBOL PARAKALESMA ARCHAION
        chars.append(0x1D03E)  #glyph03003	BYZANTINE MUSICAL SYMBOL PARAKLITIKI ARCHAION
        chars.append(0x1D03F)  #glyph03004	BYZANTINE MUSICAL SYMBOL ICHADIN
        chars.append(0x1D040)  #glyph03005	BYZANTINE MUSICAL SYMBOL NANA
        chars.append(0x1D041)  #glyph03006	BYZANTINE MUSICAL SYMBOL PETASMA
        chars.append(0x1D042)  #glyph03007	BYZANTINE MUSICAL SYMBOL KONTEVMA ALLO
        chars.append(0x1D043)  #glyph03008	BYZANTINE MUSICAL SYMBOL TROMIKON ALLO
        chars.append(0x1D044)  #glyph03009	BYZANTINE MUSICAL SYMBOL STRAGGISMATA
        chars.append(0x1D045)  #glyph03010	BYZANTINE MUSICAL SYMBOL GRONTHISMATA
        chars.append(0x1D046)  #glyph03011	BYZANTINE MUSICAL SYMBOL ISON NEO
        chars.append(0x1D047)  #glyph03012	BYZANTINE MUSICAL SYMBOL OLIGON NEO
        chars.append(0x1D048)  #glyph03013	BYZANTINE MUSICAL SYMBOL OXEIA NEO
        chars.append(0x1D049)  #glyph03014	BYZANTINE MUSICAL SYMBOL PETASTI
        chars.append(0x1D04A)  #glyph03015	BYZANTINE MUSICAL SYMBOL KOUFISMA
        chars.append(0x1D04B)  #glyph03016	BYZANTINE MUSICAL SYMBOL PETASTOKOUFISMA
        chars.append(0x1D04C)  #glyph03017	BYZANTINE MUSICAL SYMBOL KRATIMOKOUFISMA
        chars.append(0x1D04D)  #glyph03018	BYZANTINE MUSICAL SYMBOL PELASTON NEO
        chars.append(0x1D04E)  #glyph03019	BYZANTINE MUSICAL SYMBOL KENTIMATA NEO ANO
        chars.append(0x1D04F)  #glyph03020	BYZANTINE MUSICAL SYMBOL KENTIMA NEO ANO
        chars.append(0x10113)  #glyph02766	AEGEAN NUMBER FORTY
        chars.append(0x1D051)  #glyph03022	BYZANTINE MUSICAL SYMBOL APOSTROFOS NEO
        chars.append(0x1D052)  #glyph03023	BYZANTINE MUSICAL SYMBOL APOSTROFOI SYNDESMOS NEO
        chars.append(0x1D053)  #glyph03024	BYZANTINE MUSICAL SYMBOL YPORROI
        chars.append(0x1D054)  #glyph03025	BYZANTINE MUSICAL SYMBOL KRATIMOYPORROON
        chars.append(0x1D055)  #glyph03026	BYZANTINE MUSICAL SYMBOL ELAFRON
        chars.append(0x1D056)  #glyph03027	BYZANTINE MUSICAL SYMBOL CHAMILI
        chars.append(0x1D057)  #glyph03028	BYZANTINE MUSICAL SYMBOL MIKRON ISON
        chars.append(0x1D058)  #glyph03029	BYZANTINE MUSICAL SYMBOL VAREIA NEO
        chars.append(0x1D059)  #glyph03030	BYZANTINE MUSICAL SYMBOL PIASMA NEO
        chars.append(0x1D05A)  #glyph03031	BYZANTINE MUSICAL SYMBOL PSIFISTON NEO
        chars.append(0x1D05B)  #glyph03032	BYZANTINE MUSICAL SYMBOL OMALON
        chars.append(0x1D05C)  #glyph03033	BYZANTINE MUSICAL SYMBOL ANTIKENOMA
        chars.append(0x1D05D)  #glyph03034	BYZANTINE MUSICAL SYMBOL LYGISMA
        chars.append(0x1D05E)  #glyph03035	BYZANTINE MUSICAL SYMBOL PARAKLITIKI NEO
        chars.append(0x1D05F)  #glyph03036	BYZANTINE MUSICAL SYMBOL PARAKALESMA NEO
        chars.append(0x1D060)  #glyph03037	BYZANTINE MUSICAL SYMBOL ETERON PARAKALESMA
        chars.append(0x1D061)  #glyph03038	BYZANTINE MUSICAL SYMBOL KYLISMA
        chars.append(0x1D062)  #glyph03039	BYZANTINE MUSICAL SYMBOL ANTIKENOKYLISMA
        chars.append(0x1D063)  #glyph03040	BYZANTINE MUSICAL SYMBOL TROMIKON NEO
        chars.append(0x1D064)  #glyph03041	BYZANTINE MUSICAL SYMBOL EKSTREPTON
        chars.append(0x1D065)  #glyph03042	BYZANTINE MUSICAL SYMBOL SYNAGMA NEO
        chars.append(0x1D066)  #glyph03043	BYZANTINE MUSICAL SYMBOL SYRMA
        chars.append(0x1D067)  #glyph03044	BYZANTINE MUSICAL SYMBOL CHOREVMA NEO
        chars.append(0x1D068)  #glyph03045	BYZANTINE MUSICAL SYMBOL EPEGERMA
        chars.append(0x1D069)  #glyph03046	BYZANTINE MUSICAL SYMBOL SEISMA NEO
        chars.append(0x1D06A)  #glyph03047	BYZANTINE MUSICAL SYMBOL XIRON KLASMA
        chars.append(0x1D06B)  #glyph03048	BYZANTINE MUSICAL SYMBOL TROMIKOPSIFISTON
        chars.append(0x1D06C)  #glyph03049	BYZANTINE MUSICAL SYMBOL PSIFISTOLYGISMA
        chars.append(0x1D06D)  #glyph03050	BYZANTINE MUSICAL SYMBOL TROMIKOLYGISMA
        chars.append(0x1D06E)  #glyph03051	BYZANTINE MUSICAL SYMBOL TROMIKOPARAKALESMA
        chars.append(0x1D06F)  #glyph03052	BYZANTINE MUSICAL SYMBOL PSIFISTOPARAKALESMA
        chars.append(0x1D070)  #glyph03053	BYZANTINE MUSICAL SYMBOL TROMIKOSYNAGMA
        chars.append(0x1D071)  #glyph03054	BYZANTINE MUSICAL SYMBOL PSIFISTOSYNAGMA
        chars.append(0x1D072)  #glyph03055	BYZANTINE MUSICAL SYMBOL GORGOSYNTHETON
        chars.append(0x1D073)  #glyph03056	BYZANTINE MUSICAL SYMBOL ARGOSYNTHETON
        chars.append(0x1D074)  #glyph03057	BYZANTINE MUSICAL SYMBOL ETERON ARGOSYNTHETON
        chars.append(0x1D075)  #glyph03058	BYZANTINE MUSICAL SYMBOL OYRANISMA NEO
        chars.append(0x1D076)  #glyph03059	BYZANTINE MUSICAL SYMBOL THEMATISMOS ESO
        chars.append(0x1D077)  #glyph03060	BYZANTINE MUSICAL SYMBOL THEMATISMOS EXO
        chars.append(0x1D078)  #glyph03061	BYZANTINE MUSICAL SYMBOL THEMA APLOUN
        chars.append(0x1D079)  #glyph03062	BYZANTINE MUSICAL SYMBOL THES KAI APOTHES
        chars.append(0x1D07A)  #glyph03063	BYZANTINE MUSICAL SYMBOL KATAVASMA
        chars.append(0x1D07B)  #glyph03064	BYZANTINE MUSICAL SYMBOL ENDOFONON
        chars.append(0x1D07C)  #glyph03065	BYZANTINE MUSICAL SYMBOL YFEN KATO
        chars.append(0x1D07D)  #glyph03066	BYZANTINE MUSICAL SYMBOL YFEN ANO
        chars.append(0x1D07E)  #glyph03067	BYZANTINE MUSICAL SYMBOL STAVROS
        chars.append(0x1D07F)  #glyph03068	BYZANTINE MUSICAL SYMBOL KLASMA ANO
        chars.append(0x1D080)  #glyph03069	BYZANTINE MUSICAL SYMBOL DIPLI ARCHAION
        chars.append(0x1D081)  #glyph03070	BYZANTINE MUSICAL SYMBOL KRATIMA ARCHAION
        chars.append(0x1D082)  #glyph03071	BYZANTINE MUSICAL SYMBOL KRATIMA ALLO
        chars.append(0x1D083)  #glyph03072	BYZANTINE MUSICAL SYMBOL KRATIMA NEO
        chars.append(0x1D084)  #glyph03073	BYZANTINE MUSICAL SYMBOL APODERMA NEO
        chars.append(0x1D085)  #glyph03074	BYZANTINE MUSICAL SYMBOL APLI
        chars.append(0x1D086)  #glyph03075	BYZANTINE MUSICAL SYMBOL DIPLI
        chars.append(0x1D087)  #glyph03076	BYZANTINE MUSICAL SYMBOL TRIPLI
        chars.append(0x1D088)  #glyph03077	BYZANTINE MUSICAL SYMBOL TETRAPLI
        chars.append(0x1D089)  #glyph03078	BYZANTINE MUSICAL SYMBOL KORONIS
        chars.append(0x1D08A)  #glyph03079	BYZANTINE MUSICAL SYMBOL LEIMMA ENOS CHRONOU
        chars.append(0x1D08B)  #glyph03080	BYZANTINE MUSICAL SYMBOL LEIMMA DYO CHRONON
        chars.append(0x1D08C)  #glyph03081	BYZANTINE MUSICAL SYMBOL LEIMMA TRION CHRONON
        chars.append(0x1D08D)  #glyph03082	BYZANTINE MUSICAL SYMBOL LEIMMA TESSARON CHRONON
        chars.append(0x1D08E)  #glyph03083	BYZANTINE MUSICAL SYMBOL LEIMMA IMISEOS CHRONOU
        chars.append(0x1D08F)  #glyph03084	BYZANTINE MUSICAL SYMBOL GORGON NEO ANO
        chars.append(0x1D090)  #glyph03085	BYZANTINE MUSICAL SYMBOL GORGON PARESTIGMENON ARISTERA
        chars.append(0x1D091)  #glyph03086	BYZANTINE MUSICAL SYMBOL GORGON PARESTIGMENON DEXIA
        chars.append(0x1D092)  #glyph03087	BYZANTINE MUSICAL SYMBOL DIGORGON
        chars.append(0x1D093)  #glyph03088	BYZANTINE MUSICAL SYMBOL DIGORGON PARESTIGMENON ARISTERA KATO
        chars.append(0x1D094)  #glyph03089	BYZANTINE MUSICAL SYMBOL DIGORGON PARESTIGMENON ARISTERA ANO
        chars.append(0x1D095)  #glyph03090	BYZANTINE MUSICAL SYMBOL DIGORGON PARESTIGMENON DEXIA
        chars.append(0x1D096)  #glyph03091	BYZANTINE MUSICAL SYMBOL TRIGORGON
        chars.append(0x1D097)  #glyph03092	BYZANTINE MUSICAL SYMBOL ARGON
        chars.append(0x1D098)  #glyph03093	BYZANTINE MUSICAL SYMBOL IMIDIARGON
        chars.append(0x1D099)  #glyph03094	BYZANTINE MUSICAL SYMBOL DIARGON
        chars.append(0x1D09A)  #glyph03095	BYZANTINE MUSICAL SYMBOL AGOGI POLI ARGI
        chars.append(0x1D09B)  #glyph03096	BYZANTINE MUSICAL SYMBOL AGOGI ARGOTERI
        chars.append(0x1D09C)  #glyph03097	BYZANTINE MUSICAL SYMBOL AGOGI ARGI
        chars.append(0x1D09D)  #glyph03098	BYZANTINE MUSICAL SYMBOL AGOGI METRIA
        chars.append(0x1D09E)  #glyph03099	BYZANTINE MUSICAL SYMBOL AGOGI MESI
        chars.append(0x1D09F)  #glyph03100	BYZANTINE MUSICAL SYMBOL AGOGI GORGI
        chars.append(0x1D0A0)  #glyph03101	BYZANTINE MUSICAL SYMBOL AGOGI GORGOTERI
        chars.append(0x1D0A1)  #glyph03102	BYZANTINE MUSICAL SYMBOL AGOGI POLI GORGI
        chars.append(0x1D0A2)  #glyph03103	BYZANTINE MUSICAL SYMBOL MARTYRIA PROTOS ICHOS
        chars.append(0x1D0A3)  #glyph03104	BYZANTINE MUSICAL SYMBOL MARTYRIA ALLI PROTOS ICHOS
        chars.append(0x1D0A4)  #glyph03105	BYZANTINE MUSICAL SYMBOL MARTYRIA DEYTEROS ICHOS
        chars.append(0x1D0A5)  #glyph03106	BYZANTINE MUSICAL SYMBOL MARTYRIA ALLI DEYTEROS ICHOS
        chars.append(0x1D0A6)  #glyph03107	BYZANTINE MUSICAL SYMBOL MARTYRIA TRITOS ICHOS
        chars.append(0x1D0A7)  #glyph03108	BYZANTINE MUSICAL SYMBOL MARTYRIA TRIFONIAS
        chars.append(0x1D0A8)  #glyph03109	BYZANTINE MUSICAL SYMBOL MARTYRIA TETARTOS ICHOS
        chars.append(0x1D0A9)  #glyph03110	BYZANTINE MUSICAL SYMBOL MARTYRIA TETARTOS LEGETOS ICHOS
        chars.append(0x1D0AA)  #glyph03111	BYZANTINE MUSICAL SYMBOL MARTYRIA LEGETOS ICHOS
        chars.append(0x1D0AB)  #glyph03112	BYZANTINE MUSICAL SYMBOL MARTYRIA PLAGIOS ICHOS
        chars.append(0x1D0AC)  #glyph03113	BYZANTINE MUSICAL SYMBOL ISAKIA TELOUS ICHIMATOS
        chars.append(0x1D0AD)  #glyph03114	BYZANTINE MUSICAL SYMBOL APOSTROFOI TELOUS ICHIMATOS
        chars.append(0x1D0AE)  #glyph03115	BYZANTINE MUSICAL SYMBOL FANEROSIS TETRAFONIAS
        chars.append(0x1D0AF)  #glyph03116	BYZANTINE MUSICAL SYMBOL FANEROSIS MONOFONIAS
        chars.append(0x1D0B0)  #glyph03117	BYZANTINE MUSICAL SYMBOL FANEROSIS DIFONIAS
        chars.append(0x1011F)  #glyph02778	AEGEAN NUMBER SEVEN HUNDRED
        chars.append(0x1D0B2)  #glyph03119	BYZANTINE MUSICAL SYMBOL MARTYRIA PROTOVARYS ICHOS
        chars.append(0x1D0B3)  #glyph03120	BYZANTINE MUSICAL SYMBOL MARTYRIA PLAGIOS TETARTOS ICHOS
        chars.append(0x1D0B4)  #glyph03121	BYZANTINE MUSICAL SYMBOL GORTHMIKON N APLOUN
        chars.append(0x1D0B5)  #glyph03122	BYZANTINE MUSICAL SYMBOL GORTHMIKON N DIPLOUN
        chars.append(0x1D0B6)  #glyph03123	BYZANTINE MUSICAL SYMBOL ENARXIS KAI FTHORA VOU
        chars.append(0x1D0B7)  #glyph03124	BYZANTINE MUSICAL SYMBOL IMIFONON
        chars.append(0x1D0B8)  #glyph03125	BYZANTINE MUSICAL SYMBOL IMIFTHORON
        chars.append(0x1D0B9)  #glyph03126	BYZANTINE MUSICAL SYMBOL FTHORA ARCHAION DEYTEROU ICHOU
        chars.append(0x1D0BA)  #glyph03127	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI PA
        chars.append(0x1D0BB)  #glyph03128	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI NANA
        chars.append(0x1D0BC)  #glyph03129	BYZANTINE MUSICAL SYMBOL FTHORA NAOS ICHOS
        chars.append(0x1D0BD)  #glyph03130	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI DI
        chars.append(0x1D0BE)  #glyph03131	BYZANTINE MUSICAL SYMBOL FTHORA SKLIRON DIATONON DI
        chars.append(0x1D0BF)  #glyph03132	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI KE
        chars.append(0x1D0C0)  #glyph03133	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI ZO
        chars.append(0x1D0C1)  #glyph03134	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI NI KATO
        chars.append(0x1D0C2)  #glyph03135	BYZANTINE MUSICAL SYMBOL FTHORA DIATONIKI NI ANO
        chars.append(0x1D0C3)  #glyph03136	BYZANTINE MUSICAL SYMBOL FTHORA MALAKON CHROMA DIFONIAS
        chars.append(0x1D0C4)  #glyph03137	BYZANTINE MUSICAL SYMBOL FTHORA MALAKON CHROMA MONOFONIAS
        chars.append(0x1D0C5)  #glyph03138	BYZANTINE MUSICAL SYMBOL FHTORA SKLIRON CHROMA VASIS
        chars.append(0x1D0C6)  #glyph03139	BYZANTINE MUSICAL SYMBOL FTHORA SKLIRON CHROMA SYNAFI
        chars.append(0x1D0C7)  #glyph03140	BYZANTINE MUSICAL SYMBOL FTHORA NENANO
        chars.append(0x1D0C8)  #glyph03141	BYZANTINE MUSICAL SYMBOL CHROA ZYGOS
        chars.append(0x1D0C9)  #glyph03142	BYZANTINE MUSICAL SYMBOL CHROA KLITON
        chars.append(0x1D0CA)  #glyph03143	BYZANTINE MUSICAL SYMBOL CHROA SPATHI
        chars.append(0x1D0CB)  #glyph03144	BYZANTINE MUSICAL SYMBOL FTHORA I YFESIS TETARTIMORION
        chars.append(0x1D0CC)  #glyph03145	BYZANTINE MUSICAL SYMBOL FTHORA ENARMONIOS ANTIFONIA
        chars.append(0x1D0CD)  #glyph03146	BYZANTINE MUSICAL SYMBOL YFESIS TRITIMORION
        chars.append(0x1D0CE)  #glyph03147	BYZANTINE MUSICAL SYMBOL DIESIS TRITIMORION
        chars.append(0x1D0CF)  #glyph03148	BYZANTINE MUSICAL SYMBOL DIESIS TETARTIMORION
        chars.append(0x1D0D0)  #glyph03149	BYZANTINE MUSICAL SYMBOL DIESIS APLI DYO DODEKATA
        chars.append(0x1D0D1)  #glyph03150	BYZANTINE MUSICAL SYMBOL DIESIS MONOGRAMMOS TESSERA DODEKATA
        chars.append(0x1D0D2)  #glyph03151	BYZANTINE MUSICAL SYMBOL DIESIS DIGRAMMOS EX DODEKATA
        chars.append(0x1D0D3)  #glyph03152	BYZANTINE MUSICAL SYMBOL DIESIS TRIGRAMMOS OKTO DODEKATA
        chars.append(0x1D0D4)  #glyph03153	BYZANTINE MUSICAL SYMBOL YFESIS APLI DYO DODEKATA
        chars.append(0x1D0D5)  #glyph03154	BYZANTINE MUSICAL SYMBOL YFESIS MONOGRAMMOS TESSERA DODEKATA
        chars.append(0x1D0D6)  #glyph03155	BYZANTINE MUSICAL SYMBOL YFESIS DIGRAMMOS EX DODEKATA
        chars.append(0x1D0D7)  #glyph03156	BYZANTINE MUSICAL SYMBOL YFESIS TRIGRAMMOS OKTO DODEKATA
        chars.append(0x1D0D8)  #glyph03157	BYZANTINE MUSICAL SYMBOL GENIKI DIESIS
        chars.append(0x1D0D9)  #glyph03158	BYZANTINE MUSICAL SYMBOL GENIKI YFESIS
        chars.append(0x1D0DA)  #glyph03159	BYZANTINE MUSICAL SYMBOL DIASTOLI APLI MIKRI
        chars.append(0x1D0DB)  #glyph03160	BYZANTINE MUSICAL SYMBOL DIASTOLI APLI MEGALI
        chars.append(0x1D0DC)  #glyph03161	BYZANTINE MUSICAL SYMBOL DIASTOLI DIPLI
        chars.append(0x1D0DD)  #glyph03162	BYZANTINE MUSICAL SYMBOL DIASTOLI THESEOS
        chars.append(0x1D0DE)  #glyph03163	BYZANTINE MUSICAL SYMBOL SIMANSIS THESEOS
        chars.append(0x1D0DF)  #glyph03164	BYZANTINE MUSICAL SYMBOL SIMANSIS THESEOS DISIMOU
        chars.append(0x1D0E0)  #glyph03165	BYZANTINE MUSICAL SYMBOL SIMANSIS THESEOS TRISIMOU
        chars.append(0x1D0E1)  #glyph03166	BYZANTINE MUSICAL SYMBOL SIMANSIS THESEOS TETRASIMOU
        chars.append(0x1D0E2)  #glyph03167	BYZANTINE MUSICAL SYMBOL SIMANSIS ARSEOS
        chars.append(0x1D0E3)  #glyph03168	BYZANTINE MUSICAL SYMBOL SIMANSIS ARSEOS DISIMOU
        chars.append(0x1D0E4)  #glyph03169	BYZANTINE MUSICAL SYMBOL SIMANSIS ARSEOS TRISIMOU
        chars.append(0x1D0E5)  #glyph03170	BYZANTINE MUSICAL SYMBOL SIMANSIS ARSEOS TETRASIMOU
        chars.append(0x1D0E6)  #glyph03171	BYZANTINE MUSICAL SYMBOL DIGRAMMA GG
        chars.append(0x1D0E7)  #glyph03172	BYZANTINE MUSICAL SYMBOL DIFTOGGOS OU
        chars.append(0x1D0E8)  #glyph03173	BYZANTINE MUSICAL SYMBOL STIGMA
        chars.append(0x1D0E9)  #glyph03174	BYZANTINE MUSICAL SYMBOL ARKTIKO PA
        chars.append(0x1D0EA)  #glyph03175	BYZANTINE MUSICAL SYMBOL ARKTIKO VOU
        chars.append(0x1D0EB)  #glyph03176	BYZANTINE MUSICAL SYMBOL ARKTIKO GA
        chars.append(0x1D0EC)  #glyph03177	BYZANTINE MUSICAL SYMBOL ARKTIKO DI
        chars.append(0x1D0ED)  #glyph03178	BYZANTINE MUSICAL SYMBOL ARKTIKO KE
        chars.append(0x1D0EE)  #glyph03179	BYZANTINE MUSICAL SYMBOL ARKTIKO ZO
        chars.append(0x1D0EF)  #glyph03180	BYZANTINE MUSICAL SYMBOL ARKTIKO NI
        chars.append(0x1D0F0)  #glyph03181	BYZANTINE MUSICAL SYMBOL KENTIMATA NEO MESO
        chars.append(0x1D0F1)  #glyph03182	BYZANTINE MUSICAL SYMBOL KENTIMA NEO MESO
        chars.append(0x1D0F2)  #glyph03183	BYZANTINE MUSICAL SYMBOL KENTIMATA NEO KATO
        chars.append(0x1D0F3)  #glyph03184	BYZANTINE MUSICAL SYMBOL KENTIMA NEO KATO
        chars.append(0x1D0F4)  #glyph03185	BYZANTINE MUSICAL SYMBOL KLASMA KATO
        chars.append(0x1D0F5)  #glyph03186	BYZANTINE MUSICAL SYMBOL GORGON NEO KATO
        chars.append(0x1F701)  #glyph05010	????
        chars.append(0x1D100)  #glyph03187	MUSICAL SYMBOL SINGLE BARLINE
        chars.append(0x1D101)  #glyph03188	MUSICAL SYMBOL DOUBLE BARLINE
        chars.append(0x1D102)  #glyph03189	MUSICAL SYMBOL FINAL BARLINE
        chars.append(0x1D103)  #glyph03190	MUSICAL SYMBOL REVERSE FINAL BARLINE
        chars.append(0x1D104)  #glyph03191	MUSICAL SYMBOL DASHED BARLINE
        chars.append(0x1D105)  #glyph03192	MUSICAL SYMBOL SHORT BARLINE
        chars.append(0x1D106)  #glyph03193	MUSICAL SYMBOL LEFT REPEAT SIGN
        chars.append(0x1D107)  #glyph03194	MUSICAL SYMBOL RIGHT REPEAT SIGN
        chars.append(0x1D108)  #glyph03195	MUSICAL SYMBOL REPEAT DOTS
        chars.append(0x1D109)  #glyph03196	MUSICAL SYMBOL DAL SEGNO
        chars.append(0x1D10A)  #glyph03197	MUSICAL SYMBOL DA CAPO
        chars.append(0x1D10B)  #glyph03198	MUSICAL SYMBOL SEGNO
        chars.append(0x1D10C)  #glyph03199	MUSICAL SYMBOL CODA
        chars.append(0x1D10D)  #glyph03200	MUSICAL SYMBOL REPEATED FIGURE-1
        chars.append(0x1D10E)  #glyph03201	MUSICAL SYMBOL REPEATED FIGURE-2
        chars.append(0x1D10F)  #glyph03202	MUSICAL SYMBOL REPEATED FIGURE-3
        chars.append(0x1D110)  #glyph03203	MUSICAL SYMBOL FERMATA
        chars.append(0x1D111)  #glyph03204	MUSICAL SYMBOL FERMATA BELOW
        chars.append(0x1D112)  #glyph03205	MUSICAL SYMBOL BREATH MARK
        chars.append(0x1D113)  #glyph03206	MUSICAL SYMBOL CAESURA
        chars.append(0x1D114)  #glyph03207	MUSICAL SYMBOL BRACE
        chars.append(0x1D115)  #glyph03208	MUSICAL SYMBOL BRACKET
        chars.append(0x1D116)  #glyph03209	MUSICAL SYMBOL ONE-LINE STAFF
        chars.append(0x1D117)  #glyph03210	MUSICAL SYMBOL TWO-LINE STAFF
        chars.append(0x1D118)  #glyph03211	MUSICAL SYMBOL THREE-LINE STAFF
        chars.append(0x1D119)  #glyph03212	MUSICAL SYMBOL FOUR-LINE STAFF
        chars.append(0x1D11A)  #glyph03213	MUSICAL SYMBOL FIVE-LINE STAFF
        chars.append(0x1D11B)  #glyph03214	MUSICAL SYMBOL SIX-LINE STAFF
        chars.append(0x1D11C)  #glyph03215	MUSICAL SYMBOL SIX-STRING FRETBOARD
        chars.append(0x1D11D)  #glyph03216	MUSICAL SYMBOL FOUR-STRING FRETBOARD
        chars.append(0x1D11E)  #glyph03217	MUSICAL SYMBOL G CLEF
        chars.append(0x1D11F)  #glyph03218	MUSICAL SYMBOL G CLEF OTTAVA ALTA
        chars.append(0x1D120)  #glyph03219	MUSICAL SYMBOL G CLEF OTTAVA BASSA
        chars.append(0x1D121)  #glyph03220	MUSICAL SYMBOL C CLEF
        chars.append(0x1D122)  #glyph03221	MUSICAL SYMBOL F CLEF
        chars.append(0x1D123)  #glyph03222	MUSICAL SYMBOL F CLEF OTTAVA ALTA
        chars.append(0x1D124)  #glyph03223	MUSICAL SYMBOL F CLEF OTTAVA BASSA
        chars.append(0x1D125)  #glyph03224	MUSICAL SYMBOL DRUM CLEF-1
        chars.append(0x1D126)  #glyph03225	MUSICAL SYMBOL DRUM CLEF-2
        chars.append(0x1F116)  #glyph04798	PARENTHESIZED LATIN CAPITAL LETTER G
        chars.append(0x1F128)  #glyph04816	PARENTHESIZED LATIN CAPITAL LETTER Y
        chars.append(0x1D129)  #glyph03226	MUSICAL SYMBOL MULTIPLE MEASURE REST
        chars.append(0x1D12A)  #glyph03227	MUSICAL SYMBOL DOUBLE SHARP
        chars.append(0x1D12B)  #glyph03228	MUSICAL SYMBOL DOUBLE FLAT
        chars.append(0x1D12C)  #glyph03229	MUSICAL SYMBOL FLAT UP
        chars.append(0x1D12D)  #glyph03230	MUSICAL SYMBOL FLAT DOWN
        chars.append(0x1D12E)  #glyph03231	MUSICAL SYMBOL NATURAL UP
        chars.append(0x1D12F)  #glyph03232	MUSICAL SYMBOL NATURAL DOWN
        chars.append(0x1D130)  #glyph03233	MUSICAL SYMBOL SHARP UP
        chars.append(0x1D131)  #glyph03234	MUSICAL SYMBOL SHARP DOWN
        chars.append(0x1D132)  #glyph03235	MUSICAL SYMBOL QUARTER TONE SHARP
        chars.append(0x1D133)  #glyph03236	MUSICAL SYMBOL QUARTER TONE FLAT
        chars.append(0x1D134)  #glyph03237	MUSICAL SYMBOL COMMON TIME
        chars.append(0x1D135)  #glyph03238	MUSICAL SYMBOL CUT TIME
        chars.append(0x1D136)  #glyph03239	MUSICAL SYMBOL OTTAVA ALTA
        chars.append(0x1D137)  #glyph03240	MUSICAL SYMBOL OTTAVA BASSA
        chars.append(0x1D138)  #glyph03241	MUSICAL SYMBOL QUINDICESIMA ALTA
        chars.append(0x1D139)  #glyph03242	MUSICAL SYMBOL QUINDICESIMA BASSA
        chars.append(0x1D13A)  #glyph03243	MUSICAL SYMBOL MULTI REST
        chars.append(0x1D13B)  #glyph03244	MUSICAL SYMBOL WHOLE REST
        chars.append(0x1D13C)  #glyph03245	MUSICAL SYMBOL HALF REST
        chars.append(0x1D13D)  #glyph03246	MUSICAL SYMBOL QUARTER REST
        chars.append(0x1D13E)  #glyph03247	MUSICAL SYMBOL EIGHTH REST
        chars.append(0x1D13F)  #glyph03248	MUSICAL SYMBOL SIXTEENTH REST
        chars.append(0x1D140)  #glyph03249	MUSICAL SYMBOL THIRTY-SECOND REST
        chars.append(0x1D141)  #glyph03250	MUSICAL SYMBOL SIXTY-FOURTH REST
        chars.append(0x1D142)  #glyph03251	MUSICAL SYMBOL ONE HUNDRED TWENTY-EIGHTH REST
        chars.append(0x1D143)  #glyph03252	MUSICAL SYMBOL X NOTEHEAD
        chars.append(0x1D144)  #glyph03253	MUSICAL SYMBOL PLUS NOTEHEAD
        chars.append(0x1D145)  #glyph03254	MUSICAL SYMBOL CIRCLE X NOTEHEAD
        chars.append(0x1D146)  #glyph03255	MUSICAL SYMBOL SQUARE NOTEHEAD WHITE
        chars.append(0x1D147)  #glyph03256	MUSICAL SYMBOL SQUARE NOTEHEAD BLACK
        chars.append(0x1D148)  #glyph03257	MUSICAL SYMBOL TRIANGLE NOTEHEAD UP WHITE
        chars.append(0x1D149)  #glyph03258	MUSICAL SYMBOL TRIANGLE NOTEHEAD UP BLACK
        chars.append(0x1D14A)  #glyph03259	MUSICAL SYMBOL TRIANGLE NOTEHEAD LEFT WHITE
        chars.append(0x1D14B)  #glyph03260	MUSICAL SYMBOL TRIANGLE NOTEHEAD LEFT BLACK
        chars.append(0x10120)  #glyph02779	AEGEAN NUMBER EIGHT HUNDRED
        chars.append(0x1D14D)  #glyph03262	MUSICAL SYMBOL TRIANGLE NOTEHEAD RIGHT BLACK
        chars.append(0x1D14E)  #glyph03263	MUSICAL SYMBOL TRIANGLE NOTEHEAD DOWN WHITE
        chars.append(0x1D14F)  #glyph03264	MUSICAL SYMBOL TRIANGLE NOTEHEAD DOWN BLACK
        chars.append(0x1D150)  #glyph03265	MUSICAL SYMBOL TRIANGLE NOTEHEAD UP RIGHT WHITE
        chars.append(0x1D151)  #glyph03266	MUSICAL SYMBOL TRIANGLE NOTEHEAD UP RIGHT BLACK
        chars.append(0x1D152)  #glyph03267	MUSICAL SYMBOL MOON NOTEHEAD WHITE
        chars.append(0x1D153)  #glyph03268	MUSICAL SYMBOL MOON NOTEHEAD BLACK
        chars.append(0x1D154)  #glyph03269	MUSICAL SYMBOL TRIANGLE-ROUND NOTEHEAD DOWN WHITE
        chars.append(0x1D155)  #glyph03270	MUSICAL SYMBOL TRIANGLE-ROUND NOTEHEAD DOWN BLACK
        chars.append(0x1D156)  #glyph03271	MUSICAL SYMBOL PARENTHESIS NOTEHEAD
        chars.append(0x1D157)  #glyph03272	MUSICAL SYMBOL VOID NOTEHEAD
        chars.append(0x1D158)  #glyph03273	MUSICAL SYMBOL NOTEHEAD BLACK
        chars.append(0x1D159)  #glyph03274	MUSICAL SYMBOL NULL NOTEHEAD
        chars.append(0x1D15A)  #glyph03275	MUSICAL SYMBOL CLUSTER NOTEHEAD WHITE
        chars.append(0x1D15B)  #glyph03276	MUSICAL SYMBOL CLUSTER NOTEHEAD BLACK
        chars.append(0x1D15C)  #glyph03277	MUSICAL SYMBOL BREVE
        chars.append(0x1D15D)  #glyph03278	MUSICAL SYMBOL WHOLE NOTE
        chars.append(0x1D15E)  #glyph03279	MUSICAL SYMBOL HALF NOTE
        chars.append(0x1D15F)  #glyph03280	MUSICAL SYMBOL QUARTER NOTE
        chars.append(0x1D160)  #glyph03281	MUSICAL SYMBOL EIGHTH NOTE
        chars.append(0x1D161)  #glyph03282	MUSICAL SYMBOL SIXTEENTH NOTE
        chars.append(0x1D162)  #glyph03283	MUSICAL SYMBOL THIRTY-SECOND NOTE
        chars.append(0x1D163)  #glyph03284	MUSICAL SYMBOL SIXTY-FOURTH NOTE
        chars.append(0x1D164)  #glyph03285	MUSICAL SYMBOL ONE HUNDRED TWENTY-EIGHTH NOTE
        chars.append(0x1D165)  #glyph03286	MUSICAL SYMBOL COMBINING STEM
        chars.append(0x1D166)  #glyph03287	MUSICAL SYMBOL COMBINING SPRECHGESANG STEM
        chars.append(0x1D167)  #glyph03288	MUSICAL SYMBOL COMBINING TREMOLO-1
        chars.append(0x1D168)  #glyph03289	MUSICAL SYMBOL COMBINING TREMOLO-2
        chars.append(0x1D169)  #glyph03290	MUSICAL SYMBOL COMBINING TREMOLO-3
        chars.append(0x1D16A)  #glyph03291	MUSICAL SYMBOL FINGERED TREMOLO-1
        chars.append(0x1D16B)  #glyph03292	MUSICAL SYMBOL FINGERED TREMOLO-2
        chars.append(0x1D16C)  #glyph03293	MUSICAL SYMBOL FINGERED TREMOLO-3
        chars.append(0x1D16D)  #glyph03294	MUSICAL SYMBOL COMBINING AUGMENTATION DOT
        chars.append(0x1D16E)  #glyph03295	MUSICAL SYMBOL COMBINING FLAG-1
        chars.append(0x1D16F)  #glyph03296	MUSICAL SYMBOL COMBINING FLAG-2
        chars.append(0x1D170)  #glyph03297	MUSICAL SYMBOL COMBINING FLAG-3
        chars.append(0x1D171)  #glyph03298	MUSICAL SYMBOL COMBINING FLAG-4
        chars.append(0x1D172)  #glyph03299	MUSICAL SYMBOL COMBINING FLAG-5
        chars.append(0x1D173)  #glyph03300	MUSICAL SYMBOL BEGIN BEAM
        chars.append(0x1D174)  #glyph03301	MUSICAL SYMBOL END BEAM
        chars.append(0x1D175)  #glyph03302	MUSICAL SYMBOL BEGIN TIE
        chars.append(0x1D176)  #glyph03303	MUSICAL SYMBOL END TIE
        chars.append(0x1D177)  #glyph03304	MUSICAL SYMBOL BEGIN SLUR
        chars.append(0x1D178)  #glyph03305	MUSICAL SYMBOL END SLUR
        chars.append(0x1D179)  #glyph03306	MUSICAL SYMBOL BEGIN PHRASE
        chars.append(0x1D17A)  #glyph03307	MUSICAL SYMBOL END PHRASE
        chars.append(0x1D17B)  #glyph03308	MUSICAL SYMBOL COMBINING ACCENT
        chars.append(0x1D17C)  #glyph03309	MUSICAL SYMBOL COMBINING STACCATO
        chars.append(0x1D17D)  #glyph03310	MUSICAL SYMBOL COMBINING TENUTO
        chars.append(0x1D17E)  #glyph03311	MUSICAL SYMBOL COMBINING STACCATISSIMO
        chars.append(0x1D17F)  #glyph03312	MUSICAL SYMBOL COMBINING MARCATO
        chars.append(0x1D180)  #glyph03313	MUSICAL SYMBOL COMBINING MARCATO-STACCATO
        chars.append(0x1D181)  #glyph03314	MUSICAL SYMBOL COMBINING ACCENT-STACCATO
        chars.append(0x1D182)  #glyph03315	MUSICAL SYMBOL COMBINING LOURE
        chars.append(0x1D183)  #glyph03316	MUSICAL SYMBOL ARPEGGIATO UP
        chars.append(0x1D184)  #glyph03317	MUSICAL SYMBOL ARPEGGIATO DOWN
        chars.append(0x1D185)  #glyph03318	MUSICAL SYMBOL COMBINING DOIT
        chars.append(0x1D186)  #glyph03319	MUSICAL SYMBOL COMBINING RIP
        chars.append(0x1D187)  #glyph03320	MUSICAL SYMBOL COMBINING FLIP
        chars.append(0x1D188)  #glyph03321	MUSICAL SYMBOL COMBINING SMEAR
        chars.append(0x1D189)  #glyph03322	MUSICAL SYMBOL COMBINING BEND
        chars.append(0x1D18A)  #glyph03323	MUSICAL SYMBOL COMBINING DOUBLE TONGUE
        chars.append(0x1D18B)  #glyph03324	MUSICAL SYMBOL COMBINING TRIPLE TONGUE
        chars.append(0x1D18C)  #glyph03325	MUSICAL SYMBOL RINFORZANDO
        chars.append(0x1D18D)  #glyph03326	MUSICAL SYMBOL SUBITO
        chars.append(0x1D18E)  #glyph03327	MUSICAL SYMBOL Z
        chars.append(0x1D18F)  #glyph03328	MUSICAL SYMBOL PIANO
        chars.append(0x1D190)  #glyph03329	MUSICAL SYMBOL MEZZO
        chars.append(0x1D191)  #glyph03330	MUSICAL SYMBOL FORTE
        chars.append(0x1D192)  #glyph03331	MUSICAL SYMBOL CRESCENDO
        chars.append(0x1D193)  #glyph03332	MUSICAL SYMBOL DECRESCENDO
        chars.append(0x1D194)  #glyph03333	MUSICAL SYMBOL GRACE NOTE SLASH
        chars.append(0x1D195)  #glyph03334	MUSICAL SYMBOL GRACE NOTE NO SLASH
        chars.append(0x1D196)  #glyph03335	MUSICAL SYMBOL TR
        chars.append(0x1D197)  #glyph03336	MUSICAL SYMBOL TURN
        chars.append(0x1D198)  #glyph03337	MUSICAL SYMBOL INVERTED TURN
        chars.append(0x1D199)  #glyph03338	MUSICAL SYMBOL TURN SLASH
        chars.append(0x1D19A)  #glyph03339	MUSICAL SYMBOL TURN UP
        chars.append(0x1D19B)  #glyph03340	MUSICAL SYMBOL ORNAMENT STROKE-1
        chars.append(0x1D19C)  #glyph03341	MUSICAL SYMBOL ORNAMENT STROKE-2
        chars.append(0x1D19D)  #glyph03342	MUSICAL SYMBOL ORNAMENT STROKE-3
        chars.append(0x1D19E)  #glyph03343	MUSICAL SYMBOL ORNAMENT STROKE-4
        chars.append(0x1D19F)  #glyph03344	MUSICAL SYMBOL ORNAMENT STROKE-5
        chars.append(0x1D1A0)  #glyph03345	MUSICAL SYMBOL ORNAMENT STROKE-6
        chars.append(0x1D1A1)  #glyph03346	MUSICAL SYMBOL ORNAMENT STROKE-7
        chars.append(0x1D1A2)  #glyph03347	MUSICAL SYMBOL ORNAMENT STROKE-8
        chars.append(0x1D1A3)  #glyph03348	MUSICAL SYMBOL ORNAMENT STROKE-9
        chars.append(0x1D1A4)  #glyph03349	MUSICAL SYMBOL ORNAMENT STROKE-10
        chars.append(0x1D1A5)  #glyph03350	MUSICAL SYMBOL ORNAMENT STROKE-11
        chars.append(0x1D1A6)  #glyph03351	MUSICAL SYMBOL HAUPTSTIMME
        chars.append(0x1D1A7)  #glyph03352	MUSICAL SYMBOL NEBENSTIMME
        chars.append(0x1D1A8)  #glyph03353	MUSICAL SYMBOL END OF STIMME
        chars.append(0x1D1A9)  #glyph03354	MUSICAL SYMBOL DEGREE SLASH
        chars.append(0x1D1AA)  #glyph03355	MUSICAL SYMBOL COMBINING DOWN BOW
        chars.append(0x1D1AB)  #glyph03356	MUSICAL SYMBOL COMBINING UP BOW
        chars.append(0x1D1AC)  #glyph03357	MUSICAL SYMBOL COMBINING HARMONIC
        chars.append(0x1D1AD)  #glyph03358	MUSICAL SYMBOL COMBINING SNAP PIZZICATO
        chars.append(0x1D1AE)  #glyph03359	MUSICAL SYMBOL PEDAL MARK
        chars.append(0x1D1AF)  #glyph03360	MUSICAL SYMBOL PEDAL UP MARK
        chars.append(0x1D01B)  #glyph02968	BYZANTINE MUSICAL SYMBOL KENTIMA ARCHAION
        chars.append(0x1D1B1)  #glyph03362	MUSICAL SYMBOL GLISSANDO UP
        chars.append(0x1D1B2)  #glyph03363	MUSICAL SYMBOL GLISSANDO DOWN
        chars.append(0x1D1B3)  #glyph03364	MUSICAL SYMBOL WITH FINGERNAILS
        chars.append(0x1D1B4)  #glyph03365	MUSICAL SYMBOL DAMP
        chars.append(0x1D1B5)  #glyph03366	MUSICAL SYMBOL DAMP ALL
        chars.append(0x1D1B6)  #glyph03367	MUSICAL SYMBOL MAXIMA
        chars.append(0x1D1B7)  #glyph03368	MUSICAL SYMBOL LONGA
        chars.append(0x1D1B8)  #glyph03369	MUSICAL SYMBOL BREVIS
        chars.append(0x1D1B9)  #glyph03370	MUSICAL SYMBOL SEMIBREVIS WHITE
        chars.append(0x1D1BA)  #glyph03371	MUSICAL SYMBOL SEMIBREVIS BLACK
        chars.append(0x1D1BB)  #glyph03372	MUSICAL SYMBOL MINIMA
        chars.append(0x1D1BC)  #glyph03373	MUSICAL SYMBOL MINIMA BLACK
        chars.append(0x1D1BD)  #glyph03374	MUSICAL SYMBOL SEMIMINIMA WHITE
        chars.append(0x1D1BE)  #glyph03375	MUSICAL SYMBOL SEMIMINIMA BLACK
        chars.append(0x1D1BF)  #glyph03376	MUSICAL SYMBOL FUSA WHITE
        chars.append(0x1D1C0)  #glyph03377	MUSICAL SYMBOL FUSA BLACK
        chars.append(0x1D1C1)  #glyph03378	MUSICAL SYMBOL LONGA PERFECTA REST
        chars.append(0x1D1C2)  #glyph03379	MUSICAL SYMBOL LONGA IMPERFECTA REST
        chars.append(0x1D1C3)  #glyph03380	MUSICAL SYMBOL BREVIS REST
        chars.append(0x1D1C4)  #glyph03381	MUSICAL SYMBOL SEMIBREVIS REST
        chars.append(0x1D1C5)  #glyph03382	MUSICAL SYMBOL MINIMA REST
        chars.append(0x1D1C6)  #glyph03383	MUSICAL SYMBOL SEMIMINIMA REST
        chars.append(0x1D1C7)  #glyph03384	MUSICAL SYMBOL TEMPUS PERFECTUM CUM PROLATIONE PERFECTA
        chars.append(0x1D1C8)  #glyph03385	MUSICAL SYMBOL TEMPUS PERFECTUM CUM PROLATIONE IMPERFECTA
        chars.append(0x1D1C9)  #glyph03386	MUSICAL SYMBOL TEMPUS PERFECTUM CUM PROLATIONE PERFECTA DIMINUTION-1
        chars.append(0x1D1CA)  #glyph03387	MUSICAL SYMBOL TEMPUS IMPERFECTUM CUM PROLATIONE PERFECTA
        chars.append(0x1D1CB)  #glyph03388	MUSICAL SYMBOL TEMPUS IMPERFECTUM CUM PROLATIONE IMPERFECTA
        chars.append(0x1D1CC)  #glyph03389	MUSICAL SYMBOL TEMPUS IMPERFECTUM CUM PROLATIONE IMPERFECTA DIMINUTION-1
        chars.append(0x1D1CD)  #glyph03390	MUSICAL SYMBOL TEMPUS IMPERFECTUM CUM PROLATIONE IMPERFECTA DIMINUTION-2
        chars.append(0x1D1CE)  #glyph03391	MUSICAL SYMBOL TEMPUS IMPERFECTUM CUM PROLATIONE IMPERFECTA DIMINUTION-3
        chars.append(0x1D1CF)  #glyph03392	MUSICAL SYMBOL CROIX
        chars.append(0x1D1D0)  #glyph03393	MUSICAL SYMBOL GREGORIAN C CLEF
        chars.append(0x1D1D1)  #glyph03394	MUSICAL SYMBOL GREGORIAN F CLEF
        chars.append(0x1D1D2)  #glyph03395	MUSICAL SYMBOL SQUARE B
        chars.append(0x1D1D3)  #glyph03396	MUSICAL SYMBOL VIRGA
        chars.append(0x1D1D4)  #glyph03397	MUSICAL SYMBOL PODATUS
        chars.append(0x1D1D5)  #glyph03398	MUSICAL SYMBOL CLIVIS
        chars.append(0x1D1D6)  #glyph03399	MUSICAL SYMBOL SCANDICUS
        chars.append(0x1D1D7)  #glyph03400	MUSICAL SYMBOL CLIMACUS
        chars.append(0x1D1D8)  #glyph03401	MUSICAL SYMBOL TORCULUS
        chars.append(0x1D1D9)  #glyph03402	MUSICAL SYMBOL PORRECTUS
        chars.append(0x1D1DA)  #glyph03403	MUSICAL SYMBOL PORRECTUS FLEXUS
        chars.append(0x1D1DB)  #glyph03404	MUSICAL SYMBOL SCANDICUS FLEXUS
        chars.append(0x1D1DC)  #glyph03405	MUSICAL SYMBOL TORCULUS RESUPINUS
        chars.append(0x1D1DD)  #glyph03406	MUSICAL SYMBOL PES SUBPUNCTIS
        chars.append(0x1F03D)  #glyph04635	DOMINO TILE HORIZONTAL-01-05
        chars.append(0x1F126)  #glyph04814	PARENTHESIZED LATIN CAPITAL LETTER W
        chars.append(0x10121)  #glyph02780	AEGEAN NUMBER NINE HUNDRED
        chars.append(0x1F009)  #glyph04587	MAHJONG TILE THREE OF CHARACTERS
        chars.append(0x1F125)  #glyph04813	PARENTHESIZED LATIN CAPITAL LETTER V
        chars.append(0x1F1E6)  #glyph04926	????
        chars.append(0x1F1E7)  #glyph04927	????
        chars.append(0x1F1E8)  #glyph04928	????
        chars.append(0x1F1E9)  #glyph04929	????
        chars.append(0x1F1EA)  #glyph04930	????
        chars.append(0x1F1EB)  #glyph04931	????
        chars.append(0x1F1EC)  #glyph04932	????
        chars.append(0x1F1ED)  #glyph04933	????
        chars.append(0x1F1EE)  #glyph04934	????
        chars.append(0x1F1EF)  #glyph04935	????
        chars.append(0x1F1F0)  #glyph04936	????
        chars.append(0x1F1F1)  #glyph04937	????
        chars.append(0x1F1F2)  #glyph04938	????
        chars.append(0x1F1F3)  #glyph04939	????
        chars.append(0x1F1F4)  #glyph04940	????
        chars.append(0x1F1F5)  #glyph04941	????
        chars.append(0x1F1F6)  #glyph04942	????
        chars.append(0x1F1F7)  #glyph04943	????
        chars.append(0x1F1F8)  #glyph04944	????
        chars.append(0x1F1F9)  #glyph04945	????
        chars.append(0x1F1FA)  #glyph04946	????
        chars.append(0x1F1FB)  #glyph04947	????
        chars.append(0x1F1FC)  #glyph04948	????
        chars.append(0x1F1FD)  #glyph04949	????
        chars.append(0x1F1FE)  #glyph04950	????
        chars.append(0x1F1FF)  #glyph04951	????
        chars.append(0x1D200)  #glyph03407	GREEK VOCAL NOTATION SYMBOL-1
        chars.append(0x1D201)  #glyph03408	GREEK VOCAL NOTATION SYMBOL-2
        chars.append(0x1D202)  #glyph03409	GREEK VOCAL NOTATION SYMBOL-3
        chars.append(0x1D203)  #glyph03410	GREEK VOCAL NOTATION SYMBOL-4
        chars.append(0x1D204)  #glyph03411	GREEK VOCAL NOTATION SYMBOL-5
        chars.append(0x1D205)  #glyph03412	GREEK VOCAL NOTATION SYMBOL-6
        chars.append(0x1D206)  #glyph03413	GREEK VOCAL NOTATION SYMBOL-7
        chars.append(0x1D207)  #glyph03414	GREEK VOCAL NOTATION SYMBOL-8
        chars.append(0x1D208)  #glyph03415	GREEK VOCAL NOTATION SYMBOL-9
        chars.append(0x1D209)  #glyph03416	GREEK VOCAL NOTATION SYMBOL-10
        chars.append(0x1D20A)  #glyph03417	GREEK VOCAL NOTATION SYMBOL-11
        chars.append(0x1D20B)  #glyph03418	GREEK VOCAL NOTATION SYMBOL-12
        chars.append(0x1D20C)  #glyph03419	GREEK VOCAL NOTATION SYMBOL-13
        chars.append(0x1D20D)  #glyph03420	GREEK VOCAL NOTATION SYMBOL-14
        chars.append(0x1D20E)  #glyph03421	GREEK VOCAL NOTATION SYMBOL-15
        chars.append(0x1D20F)  #glyph03422	GREEK VOCAL NOTATION SYMBOL-16
        chars.append(0x1D210)  #glyph03423	GREEK VOCAL NOTATION SYMBOL-17
        chars.append(0x1D211)  #glyph03424	GREEK VOCAL NOTATION SYMBOL-18
        chars.append(0x1D212)  #glyph03425	GREEK VOCAL NOTATION SYMBOL-19
        chars.append(0x1D213)  #glyph03426	GREEK VOCAL NOTATION SYMBOL-20
        chars.append(0x1D214)  #glyph03427	GREEK VOCAL NOTATION SYMBOL-21
        chars.append(0x1D215)  #glyph03428	GREEK VOCAL NOTATION SYMBOL-22
        chars.append(0x1D216)  #glyph03429	GREEK VOCAL NOTATION SYMBOL-23
        chars.append(0x1D217)  #glyph03430	GREEK VOCAL NOTATION SYMBOL-24
        chars.append(0x1D218)  #glyph03431	GREEK VOCAL NOTATION SYMBOL-50
        chars.append(0x1D219)  #glyph03432	GREEK VOCAL NOTATION SYMBOL-51
        chars.append(0x1D21A)  #glyph03433	GREEK VOCAL NOTATION SYMBOL-52
        chars.append(0x1D21B)  #glyph03434	GREEK VOCAL NOTATION SYMBOL-53
        chars.append(0x1D21C)  #glyph03435	GREEK VOCAL NOTATION SYMBOL-54
        chars.append(0x1D21D)  #glyph03436	GREEK INSTRUMENTAL NOTATION SYMBOL-1
        chars.append(0x1D21E)  #glyph03437	GREEK INSTRUMENTAL NOTATION SYMBOL-2
        chars.append(0x1D21F)  #glyph03438	GREEK INSTRUMENTAL NOTATION SYMBOL-4
        chars.append(0x1D220)  #glyph03439	GREEK INSTRUMENTAL NOTATION SYMBOL-5
        chars.append(0x1D221)  #glyph03440	GREEK INSTRUMENTAL NOTATION SYMBOL-7
        chars.append(0x1D222)  #glyph03441	GREEK INSTRUMENTAL NOTATION SYMBOL-8
        chars.append(0x1D223)  #glyph03442	GREEK INSTRUMENTAL NOTATION SYMBOL-11
        chars.append(0x1D224)  #glyph03443	GREEK INSTRUMENTAL NOTATION SYMBOL-12
        chars.append(0x1D225)  #glyph03444	GREEK INSTRUMENTAL NOTATION SYMBOL-13
        chars.append(0x1D226)  #glyph03445	GREEK INSTRUMENTAL NOTATION SYMBOL-14
        chars.append(0x1D227)  #glyph03446	GREEK INSTRUMENTAL NOTATION SYMBOL-17
        chars.append(0x1D228)  #glyph03447	GREEK INSTRUMENTAL NOTATION SYMBOL-18
        chars.append(0x1D229)  #glyph03448	GREEK INSTRUMENTAL NOTATION SYMBOL-19
        chars.append(0x1D22A)  #glyph03449	GREEK INSTRUMENTAL NOTATION SYMBOL-23
        chars.append(0x1D22B)  #glyph03450	GREEK INSTRUMENTAL NOTATION SYMBOL-24
        chars.append(0x1D22C)  #glyph03451	GREEK INSTRUMENTAL NOTATION SYMBOL-25
        chars.append(0x1D22D)  #glyph03452	GREEK INSTRUMENTAL NOTATION SYMBOL-26
        chars.append(0x1D22E)  #glyph03453	GREEK INSTRUMENTAL NOTATION SYMBOL-27
        chars.append(0x1D22F)  #glyph03454	GREEK INSTRUMENTAL NOTATION SYMBOL-29
        chars.append(0x1D230)  #glyph03455	GREEK INSTRUMENTAL NOTATION SYMBOL-30
        chars.append(0x1D231)  #glyph03456	GREEK INSTRUMENTAL NOTATION SYMBOL-32
        chars.append(0x1D232)  #glyph03457	GREEK INSTRUMENTAL NOTATION SYMBOL-36
        chars.append(0x1D233)  #glyph03458	GREEK INSTRUMENTAL NOTATION SYMBOL-37
        chars.append(0x1D234)  #glyph03459	GREEK INSTRUMENTAL NOTATION SYMBOL-38
        chars.append(0x1D235)  #glyph03460	GREEK INSTRUMENTAL NOTATION SYMBOL-39
        chars.append(0x1D236)  #glyph03461	GREEK INSTRUMENTAL NOTATION SYMBOL-40
        chars.append(0x1D237)  #glyph03462	GREEK INSTRUMENTAL NOTATION SYMBOL-42
        chars.append(0x1D238)  #glyph03463	GREEK INSTRUMENTAL NOTATION SYMBOL-43
        chars.append(0x1D239)  #glyph03464	GREEK INSTRUMENTAL NOTATION SYMBOL-45
        chars.append(0x1D23A)  #glyph03465	GREEK INSTRUMENTAL NOTATION SYMBOL-47
        chars.append(0x1D23B)  #glyph03466	GREEK INSTRUMENTAL NOTATION SYMBOL-48
        chars.append(0x1D23C)  #glyph03467	GREEK INSTRUMENTAL NOTATION SYMBOL-49
        chars.append(0x1D23D)  #glyph03468	GREEK INSTRUMENTAL NOTATION SYMBOL-50
        chars.append(0x1D23E)  #glyph03469	GREEK INSTRUMENTAL NOTATION SYMBOL-51
        chars.append(0x1D23F)  #glyph03470	GREEK INSTRUMENTAL NOTATION SYMBOL-52
        chars.append(0x1D240)  #glyph03471	GREEK INSTRUMENTAL NOTATION SYMBOL-53
        chars.append(0x1D241)  #glyph03472	GREEK INSTRUMENTAL NOTATION SYMBOL-54
        chars.append(0x1D242)  #glyph03473	COMBINING GREEK MUSICAL TRISEME
        chars.append(0x1D243)  #glyph03474	COMBINING GREEK MUSICAL TETRASEME
        chars.append(0x1D244)  #glyph03475	COMBINING GREEK MUSICAL PENTASEME
        chars.append(0x1D245)  #glyph03476	GREEK MUSICAL LEIMMA
        chars.append(0x1F246)  #glyph05004	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-76D7
        chars.append(0x1F247)  #glyph05005	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-52DD
        chars.append(0x1F248)  #glyph05006	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-6557
        chars.append(0x1F250)  #glyph05007	????
        chars.append(0x1F251)  #glyph05008	????
        chars.append(0x1F118)  #glyph04800	PARENTHESIZED LATIN CAPITAL LETTER I
        chars.append(0x1D30E)  #glyph03491	TETRAGRAM FOR BRANCHING OUT
        chars.append(0x1F129)  #glyph04817	PARENTHESIZED LATIN CAPITAL LETTER Z
        chars.append(0x101E3)  #glyph02914	PHAISTOS DISC SIGN DOLIUM
        chars.append(0x1F23A)  #glyph04997	????
        chars.append(0x1F0AB)  #glyph04733	????
        chars.append(0x1F03E)  #glyph04636	DOMINO TILE HORIZONTAL-01-06
        chars.append(0x10122)  #glyph02781	AEGEAN NUMBER ONE THOUSAND
        chars.append(0x1F12A)  #glyph04818	TORTOISE SHELL BRACKETED LATIN CAPITAL LETTER S
        chars.append(0x1D687)  #glyph04205	MATHEMATICAL MONOSPACE CAPITAL X
        chars.append(0x1F710)  #glyph05025	????
        chars.append(0x1F14F)  #glyph04854	????
        chars.append(0x1F12B)  #glyph04819	CIRCLED ITALIC LATIN CAPITAL LETTER C
        chars.append(0x1F0CA)  #glyph04760	????
        chars.append(0x1F092)  #glyph04720	DOMINO TILE VERTICAL-06-05
        chars.append(0x1F01B)  #glyph04605	MAHJONG TILE THREE OF CIRCLES
        chars.append(0x1F12C)  #glyph04820	CIRCLED ITALIC LATIN CAPITAL LETTER R
        chars.append(0x1D578)  #glyph03934	MATHEMATICAL BOLD FRAKTUR CAPITAL M
        chars.append(0x1F70D)  #glyph05022	????
        chars.append(0x1F008)  #glyph04586	MAHJONG TILE TWO OF CHARACTERS
        chars.append(0x1F01C)  #glyph04606	MAHJONG TILE FOUR OF CIRCLES
        chars.append(0x1F03A)  #glyph04632	DOMINO TILE HORIZONTAL-01-02
        chars.append(0x1F12D)  #glyph04821	CIRCLED CD
        chars.append(0x1F115)  #glyph04797	PARENTHESIZED LATIN CAPITAL LETTER F
        chars.append(0x1F03C)  #glyph04634	DOMINO TILE HORIZONTAL-01-04
        chars.append(0x1F119)  #glyph04801	PARENTHESIZED LATIN CAPITAL LETTER J
        chars.append(0x1F01D)  #glyph04607	MAHJONG TILE FIVE OF CIRCLES
        chars.append(0x1F728)  #glyph05049	????
        chars.append(0x1F12E)  #glyph04822	CIRCLED WZ
        chars.append(0x1F0AC)  #glyph04734	????
        chars.append(0x1D300)  #glyph03477	MONOGRAM FOR EARTH
        chars.append(0x1D301)  #glyph03478	DIGRAM FOR HEAVENLY EARTH
        chars.append(0x1D302)  #glyph03479	DIGRAM FOR HUMAN EARTH
        chars.append(0x1D303)  #glyph03480	DIGRAM FOR EARTHLY HEAVEN
        chars.append(0x10109)  #glyph02756	AEGEAN NUMBER THREE
        chars.append(0x1D305)  #glyph03482	DIGRAM FOR EARTH
        chars.append(0x1D306)  #glyph03483	TETRAGRAM FOR CENTRE
        chars.append(0x1D307)  #glyph03484	TETRAGRAM FOR FULL CIRCLE
        chars.append(0x1D308)  #glyph03485	TETRAGRAM FOR MIRED
        chars.append(0x1D309)  #glyph03486	TETRAGRAM FOR BARRIER
        chars.append(0x1D30A)  #glyph03487	TETRAGRAM FOR KEEPING SMALL
        chars.append(0x1D30B)  #glyph03488	TETRAGRAM FOR CONTRARIETY
        chars.append(0x1D30C)  #glyph03489	TETRAGRAM FOR ASCENT
        chars.append(0x1D30D)  #glyph03490	TETRAGRAM FOR OPPOSITION
        chars.append(0x10123)  #glyph02782	AEGEAN NUMBER TWO THOUSAND
        chars.append(0x1D30F)  #glyph03492	TETRAGRAM FOR DEFECTIVENESS OR DISTORTION
        chars.append(0x1D310)  #glyph03493	TETRAGRAM FOR DIVERGENCE
        chars.append(0x1D311)  #glyph03494	TETRAGRAM FOR YOUTHFULNESS
        chars.append(0x1D312)  #glyph03495	TETRAGRAM FOR INCREASE
        chars.append(0x1D313)  #glyph03496	TETRAGRAM FOR PENETRATION
        chars.append(0x1D314)  #glyph03497	TETRAGRAM FOR REACH
        chars.append(0x1D315)  #glyph03498	TETRAGRAM FOR CONTACT
        chars.append(0x1D316)  #glyph03499	TETRAGRAM FOR HOLDING BACK
        chars.append(0x1D317)  #glyph03500	TETRAGRAM FOR WAITING
        chars.append(0x1D318)  #glyph03501	TETRAGRAM FOR FOLLOWING
        chars.append(0x1D319)  #glyph03502	TETRAGRAM FOR ADVANCE
        chars.append(0x1D31A)  #glyph03503	TETRAGRAM FOR RELEASE
        chars.append(0x1D31B)  #glyph03504	TETRAGRAM FOR RESISTANCE
        chars.append(0x1D31C)  #glyph03505	TETRAGRAM FOR EASE
        chars.append(0x1D31D)  #glyph03506	TETRAGRAM FOR JOY
        chars.append(0x1D31E)  #glyph03507	TETRAGRAM FOR CONTENTION
        chars.append(0x1D31F)  #glyph03508	TETRAGRAM FOR ENDEAVOUR
        chars.append(0x1D320)  #glyph03509	TETRAGRAM FOR DUTIES
        chars.append(0x1D321)  #glyph03510	TETRAGRAM FOR CHANGE
        chars.append(0x1D322)  #glyph03511	TETRAGRAM FOR DECISIVENESS
        chars.append(0x1D323)  #glyph03512	TETRAGRAM FOR BOLD RESOLUTION
        chars.append(0x1D324)  #glyph03513	TETRAGRAM FOR PACKING
        chars.append(0x1D325)  #glyph03514	TETRAGRAM FOR LEGION
        chars.append(0x1D326)  #glyph03515	TETRAGRAM FOR CLOSENESS
        chars.append(0x1D327)  #glyph03516	TETRAGRAM FOR KINSHIP
        chars.append(0x1D328)  #glyph03517	TETRAGRAM FOR GATHERING
        chars.append(0x1D329)  #glyph03518	TETRAGRAM FOR STRENGTH
        chars.append(0x1D32A)  #glyph03519	TETRAGRAM FOR PURITY
        chars.append(0x1D32B)  #glyph03520	TETRAGRAM FOR FULLNESS
        chars.append(0x1D32C)  #glyph03521	TETRAGRAM FOR RESIDENCE
        chars.append(0x1D32D)  #glyph03522	TETRAGRAM FOR LAW OR MODEL
        chars.append(0x1D32E)  #glyph03523	TETRAGRAM FOR RESPONSE
        chars.append(0x1D32F)  #glyph03524	TETRAGRAM FOR GOING TO MEET
        chars.append(0x1D330)  #glyph03525	TETRAGRAM FOR ENCOUNTERS
        chars.append(0x1D331)  #glyph03526	TETRAGRAM FOR STOVE
        chars.append(0x1D332)  #glyph03527	TETRAGRAM FOR GREATNESS
        chars.append(0x1D333)  #glyph03528	TETRAGRAM FOR ENLARGEMENT
        chars.append(0x1D334)  #glyph03529	TETRAGRAM FOR PATTERN
        chars.append(0x1D335)  #glyph03530	TETRAGRAM FOR RITUAL
        chars.append(0x1D336)  #glyph03531	TETRAGRAM FOR FLIGHT
        chars.append(0x1D337)  #glyph03532	TETRAGRAM FOR VASTNESS OR WASTING
        chars.append(0x1D338)  #glyph03533	TETRAGRAM FOR CONSTANCY
        chars.append(0x1D339)  #glyph03534	TETRAGRAM FOR MEASURE
        chars.append(0x1D33A)  #glyph03535	TETRAGRAM FOR ETERNITY
        chars.append(0x1D33B)  #glyph03536	TETRAGRAM FOR UNITY
        chars.append(0x1D33C)  #glyph03537	TETRAGRAM FOR DIMINISHMENT
        chars.append(0x1D33D)  #glyph03538	TETRAGRAM FOR CLOSED MOUTH
        chars.append(0x10114)  #glyph02767	AEGEAN NUMBER FIFTY
        chars.append(0x1D33F)  #glyph03540	TETRAGRAM FOR GATHERING IN
        chars.append(0x1D340)  #glyph03541	TETRAGRAM FOR MASSING
        chars.append(0x1D341)  #glyph03542	TETRAGRAM FOR ACCUMULATION
        chars.append(0x1D342)  #glyph03543	TETRAGRAM FOR EMBELLISHMENT
        chars.append(0x1D343)  #glyph03544	TETRAGRAM FOR DOUBT
        chars.append(0x1D344)  #glyph03545	TETRAGRAM FOR WATCH
        chars.append(0x1D345)  #glyph03546	TETRAGRAM FOR SINKING
        chars.append(0x1D346)  #glyph03547	TETRAGRAM FOR INNER
        chars.append(0x1D347)  #glyph03548	TETRAGRAM FOR DEPARTURE
        chars.append(0x1D348)  #glyph03549	TETRAGRAM FOR DARKENING
        chars.append(0x1D349)  #glyph03550	TETRAGRAM FOR DIMMING
        chars.append(0x1D34A)  #glyph03551	TETRAGRAM FOR EXHAUSTION
        chars.append(0x1D34B)  #glyph03552	TETRAGRAM FOR SEVERANCE
        chars.append(0x1D34C)  #glyph03553	TETRAGRAM FOR STOPPAGE
        chars.append(0x1D34D)  #glyph03554	TETRAGRAM FOR HARDNESS
        chars.append(0x1D34E)  #glyph03555	TETRAGRAM FOR COMPLETION
        chars.append(0x1D34F)  #glyph03556	TETRAGRAM FOR CLOSURE
        chars.append(0x1D350)  #glyph03557	TETRAGRAM FOR FAILURE
        chars.append(0x2338)  #uni2338	APL FUNCTIONAL SYMBOL QUAD EQUAL
        chars.append(0x1D352)  #glyph03559	TETRAGRAM FOR COMPLIANCE
        chars.append(0x1D353)  #glyph03560	TETRAGRAM FOR ON THE VERGE
        chars.append(0x1D354)  #glyph03561	TETRAGRAM FOR DIFFICULTIES
        chars.append(0x1D355)  #glyph03562	TETRAGRAM FOR LABOURING
        chars.append(0x1D356)  #glyph03563	TETRAGRAM FOR FOSTERING
        chars.append(0x1D360)  #glyph03564	COUNTING ROD UNIT DIGIT ONE
        chars.append(0x1D361)  #glyph03570	COUNTING ROD UNIT DIGIT TWO
        chars.append(0x1D362)  #glyph03571	COUNTING ROD UNIT DIGIT THREE
        chars.append(0x1D363)  #glyph03572	COUNTING ROD UNIT DIGIT FOUR
        chars.append(0x1D364)  #glyph03573	COUNTING ROD UNIT DIGIT FIVE
        chars.append(0x1D365)  #glyph03574	COUNTING ROD UNIT DIGIT SIX
        chars.append(0x1D366)  #glyph03575	COUNTING ROD UNIT DIGIT SEVEN
        chars.append(0x1D367)  #glyph03576	COUNTING ROD UNIT DIGIT EIGHT
        chars.append(0x1D368)  #glyph03577	COUNTING ROD UNIT DIGIT NINE
        chars.append(0x1D369)  #glyph03565	COUNTING ROD TENS DIGIT ONE
        chars.append(0x1D36A)  #glyph03566	COUNTING ROD TENS DIGIT TWO
        chars.append(0x1D36B)  #glyph03567	COUNTING ROD TENS DIGIT THREE
        chars.append(0x1D36C)  #glyph03568	COUNTING ROD TENS DIGIT FOUR
        chars.append(0x1D36D)  #glyph03569	COUNTING ROD TENS DIGIT FIVE
        chars.append(0x1D36E)  #glyph03578	COUNTING ROD TENS DIGIT SIX
        chars.append(0x1D36F)  #glyph03579	COUNTING ROD TENS DIGIT SEVEN
        chars.append(0x1D370)  #glyph03580	COUNTING ROD TENS DIGIT EIGHT
        chars.append(0x1D371)  #glyph03581	COUNTING ROD TENS DIGIT NINE
        chars.append(0x1F243)  #glyph05001	TORTOISE SHELL BRACKETED CJK UNIFIED IDEOGRAPH-5B89
        chars.append(0x1F02B)  #glyph04621	MAHJONG TILE BACK
        chars.append(0x1D33E)  #glyph03539	TETRAGRAM FOR GUARDEDNESS
        chars.append(0x1F03B)  #glyph04633	DOMINO TILE HORIZONTAL-01-03
        chars.append(0x1F11A)  #glyph04802	PARENTHESIZED LATIN CAPITAL LETTER K
        chars.append(0x1F022)  #glyph04612	MAHJONG TILE PLUM
        chars.append(0x1F14D)  #glyph04852	SQUARED SS
        chars.append(0x1F133)  #glyph04826	????
        chars.append(0x1F0AD)  #glyph04735	????
        chars.append(0x1F023)  #glyph04613	MAHJONG TILE ORCHID
        chars.append(0x1F11F)  #glyph04807	PARENTHESIZED LATIN CAPITAL LETTER P
        chars.append(0x10124)  #glyph02783	AEGEAN NUMBER THREE THOUSAND
        chars.append(0x1F040)  #glyph04638	DOMINO TILE HORIZONTAL-02-01
        chars.append(0x1F158)  #glyph04863	????
        chars.append(0x1F134)  #glyph04827	????
        chars.append(0x1F043)  #glyph04641	DOMINO TILE HORIZONTAL-02-04
        chars.append(0x1F024)  #glyph04614	MAHJONG TILE BAMBOO
        chars.append(0x1F712)  #glyph05027	????
        chars.append(0x1F151)  #glyph04856	????
        chars.append(0x1F0D5)  #glyph04770	????
        chars.append(0x1F135)  #glyph04828	????
        chars.append(0x1F046)  #glyph04644	DOMINO TILE HORIZONTAL-03-00
        chars.append(0x1F0AE)  #glyph04736	????
        chars.append(0x1D692)  #glyph04216	MATHEMATICAL MONOSPACE SMALL I
        chars.append(0x1F025)  #glyph04615	MAHJONG TILE CHRYSANTHEMUM
        chars.append(0x1F136)  #glyph04829	????
        chars.append(0x1F137)  #glyph04830	????
        chars.append(0x1D351)  #glyph03558	TETRAGRAM FOR AGGRAVATION
        chars.append(0x1F72E)  #glyph05055	????
        chars.append(0x1F141)  #glyph04840	????
        chars.append(0x1F026)  #glyph04616	MAHJONG TILE SPRING
        chars.append(0x1D400)  #glyph03582	MATHEMATICAL BOLD CAPITAL A
        chars.append(0x1D401)  #glyph03583	MATHEMATICAL BOLD CAPITAL B
        chars.append(0x1D402)  #glyph03584	MATHEMATICAL BOLD CAPITAL C
        chars.append(0x1D403)  #glyph03585	MATHEMATICAL BOLD CAPITAL D
        chars.append(0x1D404)  #glyph03586	MATHEMATICAL BOLD CAPITAL E
        chars.append(0x1D405)  #glyph03587	MATHEMATICAL BOLD CAPITAL F
        chars.append(0x1D406)  #glyph03588	MATHEMATICAL BOLD CAPITAL G
        chars.append(0x1D407)  #glyph03589	MATHEMATICAL BOLD CAPITAL H
        chars.append(0x1D408)  #glyph03590	MATHEMATICAL BOLD CAPITAL I
        chars.append(0x1D409)  #glyph03591	MATHEMATICAL BOLD CAPITAL J
        chars.append(0x1D40A)  #glyph03592	MATHEMATICAL BOLD CAPITAL K
        chars.append(0x1D40B)  #glyph03593	MATHEMATICAL BOLD CAPITAL L
        chars.append(0x1D40C)  #glyph03594	MATHEMATICAL BOLD CAPITAL M
        chars.append(0x1D40D)  #glyph03595	MATHEMATICAL BOLD CAPITAL N
        chars.append(0x1D40E)  #glyph03596	MATHEMATICAL BOLD CAPITAL O
        chars.append(0x1D40F)  #glyph03597	MATHEMATICAL BOLD CAPITAL P
        chars.append(0x1D410)  #glyph03598	MATHEMATICAL BOLD CAPITAL Q
        chars.append(0x1D411)  #glyph03599	MATHEMATICAL BOLD CAPITAL R
        chars.append(0x1D412)  #glyph03600	MATHEMATICAL BOLD CAPITAL S
        chars.append(0x1D413)  #glyph03601	MATHEMATICAL BOLD CAPITAL T
        chars.append(0x1D414)  #glyph03602	MATHEMATICAL BOLD CAPITAL U
        chars.append(0x1D415)  #glyph03603	MATHEMATICAL BOLD CAPITAL V
        chars.append(0x1D416)  #glyph03604	MATHEMATICAL BOLD CAPITAL W
        chars.append(0x1D417)  #glyph03605	MATHEMATICAL BOLD CAPITAL X
        chars.append(0x1D418)  #glyph03606	MATHEMATICAL BOLD CAPITAL Y
        chars.append(0x1D419)  #glyph03607	MATHEMATICAL BOLD CAPITAL Z
        chars.append(0x1D41A)  #glyph03608	MATHEMATICAL BOLD SMALL A
        chars.append(0x1D41B)  #glyph03609	MATHEMATICAL BOLD SMALL B
        chars.append(0x1D41C)  #glyph03610	MATHEMATICAL BOLD SMALL C
        chars.append(0x1D41D)  #glyph03611	MATHEMATICAL BOLD SMALL D
        chars.append(0x1D41E)  #glyph03612	MATHEMATICAL BOLD SMALL E
        chars.append(0x1D41F)  #glyph03613	MATHEMATICAL BOLD SMALL F
        chars.append(0x1D420)  #glyph03614	MATHEMATICAL BOLD SMALL G
        chars.append(0x1D421)  #glyph03615	MATHEMATICAL BOLD SMALL H
        chars.append(0x1D422)  #glyph03616	MATHEMATICAL BOLD SMALL I
        chars.append(0x1D423)  #glyph03617	MATHEMATICAL BOLD SMALL J
        chars.append(0x1D424)  #glyph03618	MATHEMATICAL BOLD SMALL K
        chars.append(0x1D425)  #glyph03619	MATHEMATICAL BOLD SMALL L
        chars.append(0x1D426)  #glyph03620	MATHEMATICAL BOLD SMALL M
        chars.append(0x1D427)  #glyph03621	MATHEMATICAL BOLD SMALL N
        chars.append(0x1D428)  #glyph03622	MATHEMATICAL BOLD SMALL O
        chars.append(0x1D429)  #glyph03623	MATHEMATICAL BOLD SMALL P
        chars.append(0x1D42A)  #glyph03624	MATHEMATICAL BOLD SMALL Q
        chars.append(0x1D42B)  #glyph03625	MATHEMATICAL BOLD SMALL R
        chars.append(0x1D42C)  #glyph03626	MATHEMATICAL BOLD SMALL S
        chars.append(0x1D42D)  #glyph03627	MATHEMATICAL BOLD SMALL T
        chars.append(0x1D42E)  #glyph03628	MATHEMATICAL BOLD SMALL U
        chars.append(0x1D42F)  #glyph03629	MATHEMATICAL BOLD SMALL V
        chars.append(0x1D430)  #glyph03630	MATHEMATICAL BOLD SMALL W
        chars.append(0x1D431)  #glyph03631	MATHEMATICAL BOLD SMALL X
        chars.append(0x1D432)  #glyph03632	MATHEMATICAL BOLD SMALL Y
        chars.append(0x1D433)  #glyph03633	MATHEMATICAL BOLD SMALL Z
        chars.append(0x1D434)  #glyph03634	MATHEMATICAL ITALIC CAPITAL A
        chars.append(0x1D435)  #glyph03635	MATHEMATICAL ITALIC CAPITAL B
        chars.append(0x1D436)  #glyph03636	MATHEMATICAL ITALIC CAPITAL C
        chars.append(0x1D437)  #glyph03637	MATHEMATICAL ITALIC CAPITAL D
        chars.append(0x1D438)  #glyph03638	MATHEMATICAL ITALIC CAPITAL E
        chars.append(0x1D439)  #glyph03639	MATHEMATICAL ITALIC CAPITAL F
        chars.append(0x10125)  #glyph02784	AEGEAN NUMBER FOUR THOUSAND
        chars.append(0x1D43B)  #glyph03641	MATHEMATICAL ITALIC CAPITAL H
        chars.append(0x1D43C)  #glyph03642	MATHEMATICAL ITALIC CAPITAL I
        chars.append(0x1D43D)  #glyph03643	MATHEMATICAL ITALIC CAPITAL J
        chars.append(0x1D43E)  #glyph03644	MATHEMATICAL ITALIC CAPITAL K
        chars.append(0x1D43F)  #glyph03645	MATHEMATICAL ITALIC CAPITAL L
        chars.append(0x1D440)  #glyph03646	MATHEMATICAL ITALIC CAPITAL M
        chars.append(0x1D441)  #glyph03647	MATHEMATICAL ITALIC CAPITAL N
        chars.append(0x1D442)  #glyph03648	MATHEMATICAL ITALIC CAPITAL O
        chars.append(0x1D443)  #glyph03649	MATHEMATICAL ITALIC CAPITAL P
        chars.append(0x1D444)  #glyph03650	MATHEMATICAL ITALIC CAPITAL Q
        chars.append(0x10111)  #glyph02764	AEGEAN NUMBER TWENTY
        chars.append(0x1D446)  #glyph03652	MATHEMATICAL ITALIC CAPITAL S
        chars.append(0x1D447)  #glyph03653	MATHEMATICAL ITALIC CAPITAL T
        chars.append(0x1D448)  #glyph03654	MATHEMATICAL ITALIC CAPITAL U
        chars.append(0x1D449)  #glyph03655	MATHEMATICAL ITALIC CAPITAL V
        chars.append(0x1D44A)  #glyph03656	MATHEMATICAL ITALIC CAPITAL W
        chars.append(0x1D44B)  #glyph03657	MATHEMATICAL ITALIC CAPITAL X
        chars.append(0x1D44C)  #glyph03658	MATHEMATICAL ITALIC CAPITAL Y
        chars.append(0x1D44D)  #glyph03659	MATHEMATICAL ITALIC CAPITAL Z
        chars.append(0x1D44E)  #glyph03660	MATHEMATICAL ITALIC SMALL A
        chars.append(0x1D44F)  #glyph03661	MATHEMATICAL ITALIC SMALL B
        chars.append(0x1D450)  #glyph03662	MATHEMATICAL ITALIC SMALL C
        chars.append(0x1D451)  #glyph03663	MATHEMATICAL ITALIC SMALL D
        chars.append(0x1D452)  #glyph03664	MATHEMATICAL ITALIC SMALL E
        chars.append(0x1D453)  #glyph03665	MATHEMATICAL ITALIC SMALL F
        chars.append(0x1D454)  #glyph03666	MATHEMATICAL ITALIC SMALL G
        chars.append(0x1D456)  #glyph03667	MATHEMATICAL ITALIC SMALL I
        chars.append(0x1D457)  #glyph03668	MATHEMATICAL ITALIC SMALL J
        chars.append(0x1D458)  #glyph03669	MATHEMATICAL ITALIC SMALL K
        chars.append(0x1D459)  #glyph03670	MATHEMATICAL ITALIC SMALL L
        chars.append(0x1D45A)  #glyph03671	MATHEMATICAL ITALIC SMALL M
        chars.append(0x1D45B)  #glyph03672	MATHEMATICAL ITALIC SMALL N
        chars.append(0x1D45C)  #glyph03673	MATHEMATICAL ITALIC SMALL O
        chars.append(0x1D45D)  #glyph03674	MATHEMATICAL ITALIC SMALL P
        chars.append(0x1D45E)  #glyph03675	MATHEMATICAL ITALIC SMALL Q
        chars.append(0x1D45F)  #glyph03676	MATHEMATICAL ITALIC SMALL R
        chars.append(0x1D460)  #glyph03677	MATHEMATICAL ITALIC SMALL S
        chars.append(0x1D461)  #glyph03678	MATHEMATICAL ITALIC SMALL T
        chars.append(0x1D462)  #glyph03679	MATHEMATICAL ITALIC SMALL U
        chars.append(0x1D463)  #glyph03680	MATHEMATICAL ITALIC SMALL V
        chars.append(0x1D464)  #glyph03681	MATHEMATICAL ITALIC SMALL W
        chars.append(0x1D465)  #glyph03682	MATHEMATICAL ITALIC SMALL X
        chars.append(0x1D466)  #glyph03683	MATHEMATICAL ITALIC SMALL Y
        chars.append(0x1D467)  #glyph03684	MATHEMATICAL ITALIC SMALL Z
        chars.append(0x1D468)  #glyph03685	MATHEMATICAL BOLD ITALIC CAPITAL A
        chars.append(0x1D469)  #glyph03686	MATHEMATICAL BOLD ITALIC CAPITAL B
        chars.append(0x1D46A)  #glyph03687	MATHEMATICAL BOLD ITALIC CAPITAL C
        chars.append(0x1D46B)  #glyph03688	MATHEMATICAL BOLD ITALIC CAPITAL D
        chars.append(0x1D46C)  #glyph03689	MATHEMATICAL BOLD ITALIC CAPITAL E
        chars.append(0x1D46D)  #glyph03690	MATHEMATICAL BOLD ITALIC CAPITAL F
        chars.append(0x1D46E)  #glyph03691	MATHEMATICAL BOLD ITALIC CAPITAL G
        chars.append(0x1D46F)  #glyph03692	MATHEMATICAL BOLD ITALIC CAPITAL H
        chars.append(0x1D470)  #glyph03693	MATHEMATICAL BOLD ITALIC CAPITAL I
        chars.append(0x1D471)  #glyph03694	MATHEMATICAL BOLD ITALIC CAPITAL J
        chars.append(0x1D472)  #glyph03695	MATHEMATICAL BOLD ITALIC CAPITAL K
        chars.append(0x1D473)  #glyph03696	MATHEMATICAL BOLD ITALIC CAPITAL L
        chars.append(0x1D474)  #glyph03697	MATHEMATICAL BOLD ITALIC CAPITAL M
        chars.append(0x1D475)  #glyph03698	MATHEMATICAL BOLD ITALIC CAPITAL N
        chars.append(0x1D476)  #glyph03699	MATHEMATICAL BOLD ITALIC CAPITAL O
        chars.append(0x1D477)  #glyph03700	MATHEMATICAL BOLD ITALIC CAPITAL P
        chars.append(0x1D478)  #glyph03701	MATHEMATICAL BOLD ITALIC CAPITAL Q
        chars.append(0x1D479)  #glyph03702	MATHEMATICAL BOLD ITALIC CAPITAL R
        chars.append(0x1D47A)  #glyph03703	MATHEMATICAL BOLD ITALIC CAPITAL S
        chars.append(0x1D47B)  #glyph03704	MATHEMATICAL BOLD ITALIC CAPITAL T
        chars.append(0x1D47C)  #glyph03705	MATHEMATICAL BOLD ITALIC CAPITAL U
        chars.append(0x1D47D)  #glyph03706	MATHEMATICAL BOLD ITALIC CAPITAL V
        chars.append(0x1D47E)  #glyph03707	MATHEMATICAL BOLD ITALIC CAPITAL W
        chars.append(0x1D47F)  #glyph03708	MATHEMATICAL BOLD ITALIC CAPITAL X
        chars.append(0x1D480)  #glyph03709	MATHEMATICAL BOLD ITALIC CAPITAL Y
        chars.append(0x1D481)  #glyph03710	MATHEMATICAL BOLD ITALIC CAPITAL Z
        chars.append(0x1D482)  #glyph03711	MATHEMATICAL BOLD ITALIC SMALL A
        chars.append(0x1D483)  #glyph03712	MATHEMATICAL BOLD ITALIC SMALL B
        chars.append(0x1D484)  #glyph03713	MATHEMATICAL BOLD ITALIC SMALL C
        chars.append(0x1D485)  #glyph03714	MATHEMATICAL BOLD ITALIC SMALL D
        chars.append(0x1D486)  #glyph03715	MATHEMATICAL BOLD ITALIC SMALL E
        chars.append(0x1D487)  #glyph03716	MATHEMATICAL BOLD ITALIC SMALL F
        chars.append(0x1D488)  #glyph03717	MATHEMATICAL BOLD ITALIC SMALL G
        chars.append(0x1D489)  #glyph03718	MATHEMATICAL BOLD ITALIC SMALL H
        chars.append(0x1D48A)  #glyph03719	MATHEMATICAL BOLD ITALIC SMALL I
        chars.append(0x1D48B)  #glyph03720	MATHEMATICAL BOLD ITALIC SMALL J
        chars.append(0x1D48C)  #glyph03721	MATHEMATICAL BOLD ITALIC SMALL K
        chars.append(0x1D48D)  #glyph03722	MATHEMATICAL BOLD ITALIC SMALL L
        chars.append(0x1D48E)  #glyph03723	MATHEMATICAL BOLD ITALIC SMALL M
        chars.append(0x1D48F)  #glyph03724	MATHEMATICAL BOLD ITALIC SMALL N
        chars.append(0x1D490)  #glyph03725	MATHEMATICAL BOLD ITALIC SMALL O
        chars.append(0x1D491)  #glyph03726	MATHEMATICAL BOLD ITALIC SMALL P
        chars.append(0x1D492)  #glyph03727	MATHEMATICAL BOLD ITALIC SMALL Q
        chars.append(0x1D493)  #glyph03728	MATHEMATICAL BOLD ITALIC SMALL R
        chars.append(0x1D494)  #glyph03729	MATHEMATICAL BOLD ITALIC SMALL S
        chars.append(0x1D495)  #glyph03730	MATHEMATICAL BOLD ITALIC SMALL T
        chars.append(0x1D496)  #glyph03731	MATHEMATICAL BOLD ITALIC SMALL U
        chars.append(0x1D497)  #glyph03732	MATHEMATICAL BOLD ITALIC SMALL V
        chars.append(0x1D498)  #glyph03733	MATHEMATICAL BOLD ITALIC SMALL W
        chars.append(0x1D499)  #glyph03734	MATHEMATICAL BOLD ITALIC SMALL X
        chars.append(0x1D49A)  #glyph03735	MATHEMATICAL BOLD ITALIC SMALL Y
        chars.append(0x1D49B)  #glyph03736	MATHEMATICAL BOLD ITALIC SMALL Z
        chars.append(0x1D49C)  #glyph03737	MATHEMATICAL SCRIPT CAPITAL A
        chars.append(0x1D49E)  #glyph03738	MATHEMATICAL SCRIPT CAPITAL C
        chars.append(0x1D49F)  #glyph03739	MATHEMATICAL SCRIPT CAPITAL D
        chars.append(0x1D4A2)  #glyph03740	MATHEMATICAL SCRIPT CAPITAL G
        chars.append(0x1D4A5)  #glyph03741	MATHEMATICAL SCRIPT CAPITAL J
        chars.append(0x1D4A6)  #glyph03742	MATHEMATICAL SCRIPT CAPITAL K
        chars.append(0x1D4A9)  #glyph03743	MATHEMATICAL SCRIPT CAPITAL N
        chars.append(0x1D4AA)  #glyph03744	MATHEMATICAL SCRIPT CAPITAL O
        chars.append(0x1D4AB)  #glyph03745	MATHEMATICAL SCRIPT CAPITAL P
        chars.append(0x1D4AC)  #glyph03746	MATHEMATICAL SCRIPT CAPITAL Q
        chars.append(0x1D4AE)  #glyph03747	MATHEMATICAL SCRIPT CAPITAL S
        chars.append(0x1D4AF)  #glyph03748	MATHEMATICAL SCRIPT CAPITAL T
        chars.append(0x1D4B0)  #glyph03749	MATHEMATICAL SCRIPT CAPITAL U
        chars.append(0x1D4B1)  #glyph03750	MATHEMATICAL SCRIPT CAPITAL V
        chars.append(0x1D4B2)  #glyph03751	MATHEMATICAL SCRIPT CAPITAL W
        chars.append(0x1D4B3)  #glyph03752	MATHEMATICAL SCRIPT CAPITAL X
        chars.append(0x1D4B4)  #glyph03753	MATHEMATICAL SCRIPT CAPITAL Y
        chars.append(0x1D4B5)  #glyph03754	MATHEMATICAL SCRIPT CAPITAL Z
        chars.append(0x1D4B6)  #glyph03755	MATHEMATICAL SCRIPT SMALL A
        chars.append(0x1D4B7)  #glyph03756	MATHEMATICAL SCRIPT SMALL B
        chars.append(0x1D4B8)  #glyph03757	MATHEMATICAL SCRIPT SMALL C
        chars.append(0x1D4B9)  #glyph03758	MATHEMATICAL SCRIPT SMALL D
        chars.append(0x1D4BB)  #glyph03759	MATHEMATICAL SCRIPT SMALL F
        chars.append(0x1D4BD)  #glyph03760	MATHEMATICAL SCRIPT SMALL H
        chars.append(0x1D4BE)  #glyph03761	MATHEMATICAL SCRIPT SMALL I
        chars.append(0x1D4BF)  #glyph03762	MATHEMATICAL SCRIPT SMALL J
        chars.append(0x1D4C0)  #glyph03763	MATHEMATICAL SCRIPT SMALL K
        chars.append(0x1D4C1)  #glyph03764	MATHEMATICAL SCRIPT SMALL L
        chars.append(0x1D4C2)  #glyph03765	MATHEMATICAL SCRIPT SMALL M
        chars.append(0x1D4C3)  #glyph03766	MATHEMATICAL SCRIPT SMALL N
        chars.append(0x1D4C5)  #glyph03767	MATHEMATICAL SCRIPT SMALL P
        chars.append(0x1D4C6)  #glyph03768	MATHEMATICAL SCRIPT SMALL Q
        chars.append(0x1D4C7)  #glyph03769	MATHEMATICAL SCRIPT SMALL R
        chars.append(0x1D4C8)  #glyph03770	MATHEMATICAL SCRIPT SMALL S
        chars.append(0x1D4C9)  #glyph03771	MATHEMATICAL SCRIPT SMALL T
        chars.append(0x1D4CA)  #glyph03772	MATHEMATICAL SCRIPT SMALL U
        chars.append(0x1D4CB)  #glyph03773	MATHEMATICAL SCRIPT SMALL V
        chars.append(0x1D4CC)  #glyph03774	MATHEMATICAL SCRIPT SMALL W
        chars.append(0x1D4CD)  #glyph03775	MATHEMATICAL SCRIPT SMALL X
        chars.append(0x1D4CE)  #glyph03776	MATHEMATICAL SCRIPT SMALL Y
        chars.append(0x1D4CF)  #glyph03777	MATHEMATICAL SCRIPT SMALL Z
        chars.append(0x10126)  #glyph02785	AEGEAN NUMBER FIVE THOUSAND
        chars.append(0x1D4D1)  #glyph03779	MATHEMATICAL BOLD SCRIPT CAPITAL B
        chars.append(0x1D4D2)  #glyph03780	MATHEMATICAL BOLD SCRIPT CAPITAL C
        chars.append(0x1D4D3)  #glyph03781	MATHEMATICAL BOLD SCRIPT CAPITAL D
        chars.append(0x1D4D4)  #glyph03782	MATHEMATICAL BOLD SCRIPT CAPITAL E
        chars.append(0x1D4D5)  #glyph03783	MATHEMATICAL BOLD SCRIPT CAPITAL F
        chars.append(0x1D4D6)  #glyph03784	MATHEMATICAL BOLD SCRIPT CAPITAL G
        chars.append(0x1D4D7)  #glyph03785	MATHEMATICAL BOLD SCRIPT CAPITAL H
        chars.append(0x1D4D8)  #glyph03786	MATHEMATICAL BOLD SCRIPT CAPITAL I
        chars.append(0x1D4D9)  #glyph03787	MATHEMATICAL BOLD SCRIPT CAPITAL J
        chars.append(0x1D4DA)  #glyph03788	MATHEMATICAL BOLD SCRIPT CAPITAL K
        chars.append(0x1D4DB)  #glyph03789	MATHEMATICAL BOLD SCRIPT CAPITAL L
        chars.append(0x1D4DC)  #glyph03790	MATHEMATICAL BOLD SCRIPT CAPITAL M
        chars.append(0x1D4DD)  #glyph03791	MATHEMATICAL BOLD SCRIPT CAPITAL N
        chars.append(0x1D4DE)  #glyph03792	MATHEMATICAL BOLD SCRIPT CAPITAL O
        chars.append(0x1D4DF)  #glyph03793	MATHEMATICAL BOLD SCRIPT CAPITAL P
        chars.append(0x1D4E0)  #glyph03794	MATHEMATICAL BOLD SCRIPT CAPITAL Q
        chars.append(0x1D4E1)  #glyph03795	MATHEMATICAL BOLD SCRIPT CAPITAL R
        chars.append(0x1D4E2)  #glyph03796	MATHEMATICAL BOLD SCRIPT CAPITAL S
        chars.append(0x1D4E3)  #glyph03797	MATHEMATICAL BOLD SCRIPT CAPITAL T
        chars.append(0x1D4E4)  #glyph03798	MATHEMATICAL BOLD SCRIPT CAPITAL U
        chars.append(0x1D4E5)  #glyph03799	MATHEMATICAL BOLD SCRIPT CAPITAL V
        chars.append(0x1D4E6)  #glyph03800	MATHEMATICAL BOLD SCRIPT CAPITAL W
        chars.append(0x1D4E7)  #glyph03801	MATHEMATICAL BOLD SCRIPT CAPITAL X
        chars.append(0x1D4E8)  #glyph03802	MATHEMATICAL BOLD SCRIPT CAPITAL Y
        chars.append(0x1D4E9)  #glyph03803	MATHEMATICAL BOLD SCRIPT CAPITAL Z
        chars.append(0x1D4EA)  #glyph03804	MATHEMATICAL BOLD SCRIPT SMALL A
        chars.append(0x1D4EB)  #glyph03805	MATHEMATICAL BOLD SCRIPT SMALL B
        chars.append(0x1D4EC)  #glyph03806	MATHEMATICAL BOLD SCRIPT SMALL C
        chars.append(0x1D4ED)  #glyph03807	MATHEMATICAL BOLD SCRIPT SMALL D
        chars.append(0x1D4EE)  #glyph03808	MATHEMATICAL BOLD SCRIPT SMALL E
        chars.append(0x1D4EF)  #glyph03809	MATHEMATICAL BOLD SCRIPT SMALL F
        chars.append(0x1D4F0)  #glyph03810	MATHEMATICAL BOLD SCRIPT SMALL G
        chars.append(0x1D4F1)  #glyph03811	MATHEMATICAL BOLD SCRIPT SMALL H
        chars.append(0x1D4F2)  #glyph03812	MATHEMATICAL BOLD SCRIPT SMALL I
        chars.append(0x1D4F3)  #glyph03813	MATHEMATICAL BOLD SCRIPT SMALL J
        chars.append(0x1D4F4)  #glyph03814	MATHEMATICAL BOLD SCRIPT SMALL K
        chars.append(0x1D4F5)  #glyph03815	MATHEMATICAL BOLD SCRIPT SMALL L
        chars.append(0x1D4F6)  #glyph03816	MATHEMATICAL BOLD SCRIPT SMALL M
        chars.append(0x1D4F7)  #glyph03817	MATHEMATICAL BOLD SCRIPT SMALL N
        chars.append(0x1D4F8)  #glyph03818	MATHEMATICAL BOLD SCRIPT SMALL O
        chars.append(0x1D4F9)  #glyph03819	MATHEMATICAL BOLD SCRIPT SMALL P
        chars.append(0x1D4FA)  #glyph03820	MATHEMATICAL BOLD SCRIPT SMALL Q
        chars.append(0x1D4FB)  #glyph03821	MATHEMATICAL BOLD SCRIPT SMALL R
        chars.append(0x1D4FC)  #glyph03822	MATHEMATICAL BOLD SCRIPT SMALL S
        chars.append(0x1D4FD)  #glyph03823	MATHEMATICAL BOLD SCRIPT SMALL T
        chars.append(0x1D4FE)  #glyph03824	MATHEMATICAL BOLD SCRIPT SMALL U
        chars.append(0x1D4FF)  #glyph03825	MATHEMATICAL BOLD SCRIPT SMALL V
        chars.append(0x1D500)  #glyph03826	MATHEMATICAL BOLD SCRIPT SMALL W
        chars.append(0x1D501)  #glyph03827	MATHEMATICAL BOLD SCRIPT SMALL X
        chars.append(0x1D502)  #glyph03828	MATHEMATICAL BOLD SCRIPT SMALL Y
        chars.append(0x1D503)  #glyph03829	MATHEMATICAL BOLD SCRIPT SMALL Z
        chars.append(0x1D504)  #glyph03830	MATHEMATICAL FRAKTUR CAPITAL A
        chars.append(0x1D505)  #glyph03831	MATHEMATICAL FRAKTUR CAPITAL B
        chars.append(0x1D507)  #glyph03832	MATHEMATICAL FRAKTUR CAPITAL D
        chars.append(0x1D508)  #glyph03833	MATHEMATICAL FRAKTUR CAPITAL E
        chars.append(0x1D509)  #glyph03834	MATHEMATICAL FRAKTUR CAPITAL F
        chars.append(0x1D50A)  #glyph03835	MATHEMATICAL FRAKTUR CAPITAL G
        chars.append(0x1D50D)  #glyph03836	MATHEMATICAL FRAKTUR CAPITAL J
        chars.append(0x1D50E)  #glyph03837	MATHEMATICAL FRAKTUR CAPITAL K
        chars.append(0x1D50F)  #glyph03838	MATHEMATICAL FRAKTUR CAPITAL L
        chars.append(0x1D510)  #glyph03839	MATHEMATICAL FRAKTUR CAPITAL M
        chars.append(0x1D511)  #glyph03840	MATHEMATICAL FRAKTUR CAPITAL N
        chars.append(0x1D512)  #glyph03841	MATHEMATICAL FRAKTUR CAPITAL O
        chars.append(0x1D513)  #glyph03842	MATHEMATICAL FRAKTUR CAPITAL P
        chars.append(0x1D514)  #glyph03843	MATHEMATICAL FRAKTUR CAPITAL Q
        chars.append(0x1D516)  #glyph03844	MATHEMATICAL FRAKTUR CAPITAL S
        chars.append(0x1D517)  #glyph03845	MATHEMATICAL FRAKTUR CAPITAL T
        chars.append(0x1D518)  #glyph03846	MATHEMATICAL FRAKTUR CAPITAL U
        chars.append(0x1D519)  #glyph03847	MATHEMATICAL FRAKTUR CAPITAL V
        chars.append(0x1D51A)  #glyph03848	MATHEMATICAL FRAKTUR CAPITAL W
        chars.append(0x1D51B)  #glyph03849	MATHEMATICAL FRAKTUR CAPITAL X
        chars.append(0x1D51C)  #glyph03850	MATHEMATICAL FRAKTUR CAPITAL Y
        chars.append(0x1D51E)  #glyph03851	MATHEMATICAL FRAKTUR SMALL A
        chars.append(0x1D51F)  #glyph03852	MATHEMATICAL FRAKTUR SMALL B
        chars.append(0x1D520)  #glyph03853	MATHEMATICAL FRAKTUR SMALL C
        chars.append(0x1D521)  #glyph03854	MATHEMATICAL FRAKTUR SMALL D
        chars.append(0x1D522)  #glyph03855	MATHEMATICAL FRAKTUR SMALL E
        chars.append(0x1D523)  #glyph03856	MATHEMATICAL FRAKTUR SMALL F
        chars.append(0x1D524)  #glyph03857	MATHEMATICAL FRAKTUR SMALL G
        chars.append(0x1D525)  #glyph03858	MATHEMATICAL FRAKTUR SMALL H
        chars.append(0x1D526)  #glyph03859	MATHEMATICAL FRAKTUR SMALL I
        chars.append(0x1D527)  #glyph03860	MATHEMATICAL FRAKTUR SMALL J
        chars.append(0x1D528)  #glyph03861	MATHEMATICAL FRAKTUR SMALL K
        chars.append(0x1D529)  #glyph03862	MATHEMATICAL FRAKTUR SMALL L
        chars.append(0x1D52A)  #glyph03863	MATHEMATICAL FRAKTUR SMALL M
        chars.append(0x1D52B)  #glyph03864	MATHEMATICAL FRAKTUR SMALL N
        chars.append(0x1D52C)  #glyph03865	MATHEMATICAL FRAKTUR SMALL O
        chars.append(0x1D52D)  #glyph03866	MATHEMATICAL FRAKTUR SMALL P
        chars.append(0x1D52E)  #glyph03867	MATHEMATICAL FRAKTUR SMALL Q
        chars.append(0x1D52F)  #glyph03868	MATHEMATICAL FRAKTUR SMALL R
        chars.append(0x1D530)  #glyph03869	MATHEMATICAL FRAKTUR SMALL S
        chars.append(0x1D531)  #glyph03870	MATHEMATICAL FRAKTUR SMALL T
        chars.append(0x1D532)  #glyph03871	MATHEMATICAL FRAKTUR SMALL U
        chars.append(0x1D533)  #glyph03872	MATHEMATICAL FRAKTUR SMALL V
        chars.append(0x1D534)  #glyph03873	MATHEMATICAL FRAKTUR SMALL W
        chars.append(0x1D535)  #glyph03874	MATHEMATICAL FRAKTUR SMALL X
        chars.append(0x1D536)  #glyph03875	MATHEMATICAL FRAKTUR SMALL Y
        chars.append(0x1D537)  #glyph03876	MATHEMATICAL FRAKTUR SMALL Z
        chars.append(0x1D538)  #glyph03877	MATHEMATICAL DOUBLE-STRUCK CAPITAL A
        chars.append(0x1D539)  #glyph03878	MATHEMATICAL DOUBLE-STRUCK CAPITAL B
        chars.append(0x1D53B)  #glyph03879	MATHEMATICAL DOUBLE-STRUCK CAPITAL D
        chars.append(0x1D53C)  #glyph03880	MATHEMATICAL DOUBLE-STRUCK CAPITAL E
        chars.append(0x1D53D)  #glyph03881	MATHEMATICAL DOUBLE-STRUCK CAPITAL F
        chars.append(0x1D53E)  #glyph03882	MATHEMATICAL DOUBLE-STRUCK CAPITAL G
        chars.append(0x1D540)  #glyph03883	MATHEMATICAL DOUBLE-STRUCK CAPITAL I
        chars.append(0x1D541)  #glyph03884	MATHEMATICAL DOUBLE-STRUCK CAPITAL J
        chars.append(0x1D542)  #glyph03885	MATHEMATICAL DOUBLE-STRUCK CAPITAL K
        chars.append(0x1D543)  #glyph03886	MATHEMATICAL DOUBLE-STRUCK CAPITAL L
        chars.append(0x1D544)  #glyph03887	MATHEMATICAL DOUBLE-STRUCK CAPITAL M
        chars.append(0x1F031)  #glyph04623	DOMINO TILE HORIZONTAL-00-00
        chars.append(0x1D546)  #glyph03888	MATHEMATICAL DOUBLE-STRUCK CAPITAL O
        chars.append(0x1D54A)  #glyph03889	MATHEMATICAL DOUBLE-STRUCK CAPITAL S
        chars.append(0x1D54B)  #glyph03890	MATHEMATICAL DOUBLE-STRUCK CAPITAL T
        chars.append(0x1D54C)  #glyph03891	MATHEMATICAL DOUBLE-STRUCK CAPITAL U
        chars.append(0x1D54D)  #glyph03892	MATHEMATICAL DOUBLE-STRUCK CAPITAL V
        chars.append(0x1D54E)  #glyph03893	MATHEMATICAL DOUBLE-STRUCK CAPITAL W
        chars.append(0x1D54F)  #glyph03894	MATHEMATICAL DOUBLE-STRUCK CAPITAL X
        chars.append(0x1D550)  #glyph03895	MATHEMATICAL DOUBLE-STRUCK CAPITAL Y
        chars.append(0x1D552)  #glyph03896	MATHEMATICAL DOUBLE-STRUCK SMALL A
        chars.append(0x1D553)  #glyph03897	MATHEMATICAL DOUBLE-STRUCK SMALL B
        chars.append(0x1D554)  #glyph03898	MATHEMATICAL DOUBLE-STRUCK SMALL C
        chars.append(0x1D555)  #glyph03899	MATHEMATICAL DOUBLE-STRUCK SMALL D
        chars.append(0x1D556)  #glyph03900	MATHEMATICAL DOUBLE-STRUCK SMALL E
        chars.append(0x1D557)  #glyph03901	MATHEMATICAL DOUBLE-STRUCK SMALL F
        chars.append(0x1D558)  #glyph03902	MATHEMATICAL DOUBLE-STRUCK SMALL G
        chars.append(0x1D559)  #glyph03903	MATHEMATICAL DOUBLE-STRUCK SMALL H
        chars.append(0x1D55A)  #glyph03904	MATHEMATICAL DOUBLE-STRUCK SMALL I
        chars.append(0x1D55B)  #glyph03905	MATHEMATICAL DOUBLE-STRUCK SMALL J
        chars.append(0x1D55C)  #glyph03906	MATHEMATICAL DOUBLE-STRUCK SMALL K
        chars.append(0x1D55D)  #glyph03907	MATHEMATICAL DOUBLE-STRUCK SMALL L
        chars.append(0x1D55E)  #glyph03908	MATHEMATICAL DOUBLE-STRUCK SMALL M
        chars.append(0x1D55F)  #glyph03909	MATHEMATICAL DOUBLE-STRUCK SMALL N
        chars.append(0x1D560)  #glyph03910	MATHEMATICAL DOUBLE-STRUCK SMALL O
        chars.append(0x1D561)  #glyph03911	MATHEMATICAL DOUBLE-STRUCK SMALL P
        chars.append(0x1D562)  #glyph03912	MATHEMATICAL DOUBLE-STRUCK SMALL Q
        chars.append(0x1D563)  #glyph03913	MATHEMATICAL DOUBLE-STRUCK SMALL R
        chars.append(0x1D564)  #glyph03914	MATHEMATICAL DOUBLE-STRUCK SMALL S
        chars.append(0x1D565)  #glyph03915	MATHEMATICAL DOUBLE-STRUCK SMALL T
        chars.append(0x10127)  #glyph02786	AEGEAN NUMBER SIX THOUSAND
        chars.append(0x1D567)  #glyph03917	MATHEMATICAL DOUBLE-STRUCK SMALL V
        chars.append(0x1D568)  #glyph03918	MATHEMATICAL DOUBLE-STRUCK SMALL W
        chars.append(0x1D569)  #glyph03919	MATHEMATICAL DOUBLE-STRUCK SMALL X
        chars.append(0x1D56A)  #glyph03920	MATHEMATICAL DOUBLE-STRUCK SMALL Y
        chars.append(0x1D56B)  #glyph03921	MATHEMATICAL DOUBLE-STRUCK SMALL Z
        chars.append(0x1D56C)  #glyph03922	MATHEMATICAL BOLD FRAKTUR CAPITAL A
        chars.append(0x1D56D)  #glyph03923	MATHEMATICAL BOLD FRAKTUR CAPITAL B
        chars.append(0x1D56E)  #glyph03924	MATHEMATICAL BOLD FRAKTUR CAPITAL C
        chars.append(0x1D56F)  #glyph03925	MATHEMATICAL BOLD FRAKTUR CAPITAL D
        chars.append(0x1D570)  #glyph03926	MATHEMATICAL BOLD FRAKTUR CAPITAL E
        chars.append(0x1D571)  #glyph03927	MATHEMATICAL BOLD FRAKTUR CAPITAL F
        chars.append(0x1D572)  #glyph03928	MATHEMATICAL BOLD FRAKTUR CAPITAL G
        chars.append(0x1D573)  #glyph03929	MATHEMATICAL BOLD FRAKTUR CAPITAL H
        chars.append(0x1D574)  #glyph03930	MATHEMATICAL BOLD FRAKTUR CAPITAL I
        chars.append(0x1D575)  #glyph03931	MATHEMATICAL BOLD FRAKTUR CAPITAL J
        chars.append(0x1D576)  #glyph03932	MATHEMATICAL BOLD FRAKTUR CAPITAL K
        chars.append(0x1D577)  #glyph03933	MATHEMATICAL BOLD FRAKTUR CAPITAL L
        chars.append(0x1D14C)  #glyph03261	MUSICAL SYMBOL TRIANGLE NOTEHEAD RIGHT WHITE
        chars.append(0x1D579)  #glyph03935	MATHEMATICAL BOLD FRAKTUR CAPITAL N
        chars.append(0x1D57A)  #glyph03936	MATHEMATICAL BOLD FRAKTUR CAPITAL O
        chars.append(0x1D57B)  #glyph03937	MATHEMATICAL BOLD FRAKTUR CAPITAL P
        chars.append(0x1D57C)  #glyph03938	MATHEMATICAL BOLD FRAKTUR CAPITAL Q
        chars.append(0x1D57D)  #glyph03939	MATHEMATICAL BOLD FRAKTUR CAPITAL R
        chars.append(0x1D57E)  #glyph03940	MATHEMATICAL BOLD FRAKTUR CAPITAL S
        chars.append(0x1D57F)  #glyph03941	MATHEMATICAL BOLD FRAKTUR CAPITAL T
        chars.append(0x1D580)  #glyph03942	MATHEMATICAL BOLD FRAKTUR CAPITAL U
        chars.append(0x1D581)  #glyph03943	MATHEMATICAL BOLD FRAKTUR CAPITAL V
        chars.append(0x1D582)  #glyph03944	MATHEMATICAL BOLD FRAKTUR CAPITAL W
        chars.append(0x1D583)  #glyph03945	MATHEMATICAL BOLD FRAKTUR CAPITAL X
        chars.append(0x1D584)  #glyph03946	MATHEMATICAL BOLD FRAKTUR CAPITAL Y
        chars.append(0x1D585)  #glyph03947	MATHEMATICAL BOLD FRAKTUR CAPITAL Z
        chars.append(0x1D586)  #glyph03948	MATHEMATICAL BOLD FRAKTUR SMALL A
        chars.append(0x1D587)  #glyph03949	MATHEMATICAL BOLD FRAKTUR SMALL B
        chars.append(0x1D588)  #glyph03950	MATHEMATICAL BOLD FRAKTUR SMALL C
        chars.append(0x1D589)  #glyph03951	MATHEMATICAL BOLD FRAKTUR SMALL D
        chars.append(0x1D58A)  #glyph03952	MATHEMATICAL BOLD FRAKTUR SMALL E
        chars.append(0x1D58B)  #glyph03953	MATHEMATICAL BOLD FRAKTUR SMALL F
        chars.append(0x1D58C)  #glyph03954	MATHEMATICAL BOLD FRAKTUR SMALL G
        chars.append(0x1D58D)  #glyph03955	MATHEMATICAL BOLD FRAKTUR SMALL H
        chars.append(0x1D58E)  #glyph03956	MATHEMATICAL BOLD FRAKTUR SMALL I
        chars.append(0x1D58F)  #glyph03957	MATHEMATICAL BOLD FRAKTUR SMALL J
        chars.append(0x1D590)  #glyph03958	MATHEMATICAL BOLD FRAKTUR SMALL K
        chars.append(0x1D591)  #glyph03959	MATHEMATICAL BOLD FRAKTUR SMALL L
        chars.append(0x1D592)  #glyph03960	MATHEMATICAL BOLD FRAKTUR SMALL M
        chars.append(0x1D593)  #glyph03961	MATHEMATICAL BOLD FRAKTUR SMALL N
        chars.append(0x1D594)  #glyph03962	MATHEMATICAL BOLD FRAKTUR SMALL O
        chars.append(0x1D595)  #glyph03963	MATHEMATICAL BOLD FRAKTUR SMALL P
        chars.append(0x1D596)  #glyph03964	MATHEMATICAL BOLD FRAKTUR SMALL Q
        chars.append(0x1D597)  #glyph03965	MATHEMATICAL BOLD FRAKTUR SMALL R
        chars.append(0x1D598)  #glyph03966	MATHEMATICAL BOLD FRAKTUR SMALL S
        chars.append(0x1D599)  #glyph03967	MATHEMATICAL BOLD FRAKTUR SMALL T
        chars.append(0x1D59A)  #glyph03968	MATHEMATICAL BOLD FRAKTUR SMALL U
        chars.append(0x1D59B)  #glyph03969	MATHEMATICAL BOLD FRAKTUR SMALL V
        chars.append(0x1D59C)  #glyph03970	MATHEMATICAL BOLD FRAKTUR SMALL W
        chars.append(0x1D59D)  #glyph03971	MATHEMATICAL BOLD FRAKTUR SMALL X
        chars.append(0x1D59E)  #glyph03972	MATHEMATICAL BOLD FRAKTUR SMALL Y
        chars.append(0x1D59F)  #glyph03973	MATHEMATICAL BOLD FRAKTUR SMALL Z
        chars.append(0x1D5A0)  #glyph03974	MATHEMATICAL SANS-SERIF CAPITAL A
        chars.append(0x1D5A1)  #glyph03975	MATHEMATICAL SANS-SERIF CAPITAL B
        chars.append(0x1D5A2)  #glyph03976	MATHEMATICAL SANS-SERIF CAPITAL C
        chars.append(0x1D5A3)  #glyph03977	MATHEMATICAL SANS-SERIF CAPITAL D
        chars.append(0x1D5A4)  #glyph03978	MATHEMATICAL SANS-SERIF CAPITAL E
        chars.append(0x1D5A5)  #glyph03979	MATHEMATICAL SANS-SERIF CAPITAL F
        chars.append(0x1D5A6)  #glyph03980	MATHEMATICAL SANS-SERIF CAPITAL G
        chars.append(0x1D5A7)  #glyph03981	MATHEMATICAL SANS-SERIF CAPITAL H
        chars.append(0x1D5A8)  #glyph03982	MATHEMATICAL SANS-SERIF CAPITAL I
        chars.append(0x1D5A9)  #glyph03983	MATHEMATICAL SANS-SERIF CAPITAL J
        chars.append(0x1D5AA)  #glyph03984	MATHEMATICAL SANS-SERIF CAPITAL K
        chars.append(0x1D5AB)  #glyph03985	MATHEMATICAL SANS-SERIF CAPITAL L
        chars.append(0x1D5AC)  #glyph03986	MATHEMATICAL SANS-SERIF CAPITAL M
        chars.append(0x1D5AD)  #glyph03987	MATHEMATICAL SANS-SERIF CAPITAL N
        chars.append(0x1D5AE)  #glyph03988	MATHEMATICAL SANS-SERIF CAPITAL O
        chars.append(0x1D5AF)  #glyph03989	MATHEMATICAL SANS-SERIF CAPITAL P
        chars.append(0x1D5B0)  #glyph03990	MATHEMATICAL SANS-SERIF CAPITAL Q
        chars.append(0x1D5B1)  #glyph03991	MATHEMATICAL SANS-SERIF CAPITAL R
        chars.append(0x1D5B2)  #glyph03992	MATHEMATICAL SANS-SERIF CAPITAL S
        chars.append(0x1D5B3)  #glyph03993	MATHEMATICAL SANS-SERIF CAPITAL T
        chars.append(0x1D5B4)  #glyph03994	MATHEMATICAL SANS-SERIF CAPITAL U
        chars.append(0x1D5B5)  #glyph03995	MATHEMATICAL SANS-SERIF CAPITAL V
        chars.append(0x1D5B6)  #glyph03996	MATHEMATICAL SANS-SERIF CAPITAL W
        chars.append(0x1D5B7)  #glyph03997	MATHEMATICAL SANS-SERIF CAPITAL X
        chars.append(0x1D5B8)  #glyph03998	MATHEMATICAL SANS-SERIF CAPITAL Y
        chars.append(0x1D5B9)  #glyph03999	MATHEMATICAL SANS-SERIF CAPITAL Z
        chars.append(0x1D5BA)  #glyph04000	MATHEMATICAL SANS-SERIF SMALL A
        chars.append(0x1D5BB)  #glyph04001	MATHEMATICAL SANS-SERIF SMALL B
        chars.append(0x1D5BC)  #glyph04002	MATHEMATICAL SANS-SERIF SMALL C
        chars.append(0x1D5BD)  #glyph04003	MATHEMATICAL SANS-SERIF SMALL D
        chars.append(0x1D5BE)  #glyph04004	MATHEMATICAL SANS-SERIF SMALL E
        chars.append(0x1D5BF)  #glyph04005	MATHEMATICAL SANS-SERIF SMALL F
        chars.append(0x1D5C0)  #glyph04006	MATHEMATICAL SANS-SERIF SMALL G
        chars.append(0x1D5C1)  #glyph04007	MATHEMATICAL SANS-SERIF SMALL H
        chars.append(0x1D5C2)  #glyph04008	MATHEMATICAL SANS-SERIF SMALL I
        chars.append(0x1D5C3)  #glyph04009	MATHEMATICAL SANS-SERIF SMALL J
        chars.append(0x1D5C4)  #glyph04010	MATHEMATICAL SANS-SERIF SMALL K
        chars.append(0x1D5C5)  #glyph04011	MATHEMATICAL SANS-SERIF SMALL L
        chars.append(0x1D5C6)  #glyph04012	MATHEMATICAL SANS-SERIF SMALL M
        chars.append(0x1D5C7)  #glyph04013	MATHEMATICAL SANS-SERIF SMALL N
        chars.append(0x1D5C8)  #glyph04014	MATHEMATICAL SANS-SERIF SMALL O
        chars.append(0x1D5C9)  #glyph04015	MATHEMATICAL SANS-SERIF SMALL P
        chars.append(0x1D5CA)  #glyph04016	MATHEMATICAL SANS-SERIF SMALL Q
        chars.append(0x1D5CB)  #glyph04017	MATHEMATICAL SANS-SERIF SMALL R
        chars.append(0x1D5CC)  #glyph04018	MATHEMATICAL SANS-SERIF SMALL S
        chars.append(0x1D5CD)  #glyph04019	MATHEMATICAL SANS-SERIF SMALL T
        chars.append(0x1D5CE)  #glyph04020	MATHEMATICAL SANS-SERIF SMALL U
        chars.append(0x1D5CF)  #glyph04021	MATHEMATICAL SANS-SERIF SMALL V
        chars.append(0x1D5D0)  #glyph04022	MATHEMATICAL SANS-SERIF SMALL W
        chars.append(0x1D5D1)  #glyph04023	MATHEMATICAL SANS-SERIF SMALL X
        chars.append(0x1D5D2)  #glyph04024	MATHEMATICAL SANS-SERIF SMALL Y
        chars.append(0x1D5D3)  #glyph04025	MATHEMATICAL SANS-SERIF SMALL Z
        chars.append(0x1D5D4)  #glyph04026	MATHEMATICAL SANS-SERIF BOLD CAPITAL A
        chars.append(0x1D5D5)  #glyph04027	MATHEMATICAL SANS-SERIF BOLD CAPITAL B
        chars.append(0x1D5D6)  #glyph04028	MATHEMATICAL SANS-SERIF BOLD CAPITAL C
        chars.append(0x1D5D7)  #glyph04029	MATHEMATICAL SANS-SERIF BOLD CAPITAL D
        chars.append(0x1D5D8)  #glyph04030	MATHEMATICAL SANS-SERIF BOLD CAPITAL E
        chars.append(0x1D5D9)  #glyph04031	MATHEMATICAL SANS-SERIF BOLD CAPITAL F
        chars.append(0x1D5DA)  #glyph04032	MATHEMATICAL SANS-SERIF BOLD CAPITAL G
        chars.append(0x1D5DB)  #glyph04033	MATHEMATICAL SANS-SERIF BOLD CAPITAL H
        chars.append(0x1D5DC)  #glyph04034	MATHEMATICAL SANS-SERIF BOLD CAPITAL I
        chars.append(0x1D5DD)  #glyph04035	MATHEMATICAL SANS-SERIF BOLD CAPITAL J
        chars.append(0x1D5DE)  #glyph04036	MATHEMATICAL SANS-SERIF BOLD CAPITAL K
        chars.append(0x1D5DF)  #glyph04037	MATHEMATICAL SANS-SERIF BOLD CAPITAL L
        chars.append(0x1D5E0)  #glyph04038	MATHEMATICAL SANS-SERIF BOLD CAPITAL M
        chars.append(0x1D5E1)  #glyph04039	MATHEMATICAL SANS-SERIF BOLD CAPITAL N
        chars.append(0x1D5E2)  #glyph04040	MATHEMATICAL SANS-SERIF BOLD CAPITAL O
        chars.append(0x1D5E3)  #glyph04041	MATHEMATICAL SANS-SERIF BOLD CAPITAL P
        chars.append(0x1D5E4)  #glyph04042	MATHEMATICAL SANS-SERIF BOLD CAPITAL Q
        chars.append(0x1D5E5)  #glyph04043	MATHEMATICAL SANS-SERIF BOLD CAPITAL R
        chars.append(0x1D5E6)  #glyph04044	MATHEMATICAL SANS-SERIF BOLD CAPITAL S
        chars.append(0x1D5E7)  #glyph04045	MATHEMATICAL SANS-SERIF BOLD CAPITAL T
        chars.append(0x1D5E8)  #glyph04046	MATHEMATICAL SANS-SERIF BOLD CAPITAL U
        chars.append(0x1D5E9)  #glyph04047	MATHEMATICAL SANS-SERIF BOLD CAPITAL V
        chars.append(0x1D5EA)  #glyph04048	MATHEMATICAL SANS-SERIF BOLD CAPITAL W
        chars.append(0x1D5EB)  #glyph04049	MATHEMATICAL SANS-SERIF BOLD CAPITAL X
        chars.append(0x1D5EC)  #glyph04050	MATHEMATICAL SANS-SERIF BOLD CAPITAL Y
        chars.append(0x1D5ED)  #glyph04051	MATHEMATICAL SANS-SERIF BOLD CAPITAL Z
        chars.append(0x1D5EE)  #glyph04052	MATHEMATICAL SANS-SERIF BOLD SMALL A
        chars.append(0x1D5EF)  #glyph04053	MATHEMATICAL SANS-SERIF BOLD SMALL B
        chars.append(0x1D5F0)  #glyph04054	MATHEMATICAL SANS-SERIF BOLD SMALL C
        chars.append(0x1D5F1)  #glyph04055	MATHEMATICAL SANS-SERIF BOLD SMALL D
        chars.append(0x1010A)  #glyph02757	AEGEAN NUMBER FOUR
        chars.append(0x1D5F3)  #glyph04057	MATHEMATICAL SANS-SERIF BOLD SMALL F
        chars.append(0x1D5F4)  #glyph04058	MATHEMATICAL SANS-SERIF BOLD SMALL G
        chars.append(0x1D5F5)  #glyph04059	MATHEMATICAL SANS-SERIF BOLD SMALL H
        chars.append(0x1D5F6)  #glyph04060	MATHEMATICAL SANS-SERIF BOLD SMALL I
        chars.append(0x1D5F7)  #glyph04061	MATHEMATICAL SANS-SERIF BOLD SMALL J
        chars.append(0x1D5F8)  #glyph04062	MATHEMATICAL SANS-SERIF BOLD SMALL K
        chars.append(0x1D5F9)  #glyph04063	MATHEMATICAL SANS-SERIF BOLD SMALL L
        chars.append(0x1D5FA)  #glyph04064	MATHEMATICAL SANS-SERIF BOLD SMALL M
        chars.append(0x1D5FB)  #glyph04065	MATHEMATICAL SANS-SERIF BOLD SMALL N
        chars.append(0x10128)  #glyph02787	AEGEAN NUMBER SEVEN THOUSAND
        chars.append(0x1D5FD)  #glyph04067	MATHEMATICAL SANS-SERIF BOLD SMALL P
        chars.append(0x1D5FE)  #glyph04068	MATHEMATICAL SANS-SERIF BOLD SMALL Q
        chars.append(0x1D5FF)  #glyph04069	MATHEMATICAL SANS-SERIF BOLD SMALL R
        chars.append(0x1D600)  #glyph04070	MATHEMATICAL SANS-SERIF BOLD SMALL S
        chars.append(0x1D601)  #glyph04071	MATHEMATICAL SANS-SERIF BOLD SMALL T
        chars.append(0x1D602)  #glyph04072	MATHEMATICAL SANS-SERIF BOLD SMALL U
        chars.append(0x1D603)  #glyph04073	MATHEMATICAL SANS-SERIF BOLD SMALL V
        chars.append(0x1D604)  #glyph04074	MATHEMATICAL SANS-SERIF BOLD SMALL W
        chars.append(0x1D605)  #glyph04075	MATHEMATICAL SANS-SERIF BOLD SMALL X
        chars.append(0x1D606)  #glyph04076	MATHEMATICAL SANS-SERIF BOLD SMALL Y
        chars.append(0x1D607)  #glyph04077	MATHEMATICAL SANS-SERIF BOLD SMALL Z
        chars.append(0x1D608)  #glyph04078	MATHEMATICAL SANS-SERIF ITALIC CAPITAL A
        chars.append(0x1D609)  #glyph04079	MATHEMATICAL SANS-SERIF ITALIC CAPITAL B
        chars.append(0x1D60A)  #glyph04080	MATHEMATICAL SANS-SERIF ITALIC CAPITAL C
        chars.append(0x1D60B)  #glyph04081	MATHEMATICAL SANS-SERIF ITALIC CAPITAL D
        chars.append(0x1D60C)  #glyph04082	MATHEMATICAL SANS-SERIF ITALIC CAPITAL E
        chars.append(0x1D60D)  #glyph04083	MATHEMATICAL SANS-SERIF ITALIC CAPITAL F
        chars.append(0x1D60E)  #glyph04084	MATHEMATICAL SANS-SERIF ITALIC CAPITAL G
        chars.append(0x1D60F)  #glyph04085	MATHEMATICAL SANS-SERIF ITALIC CAPITAL H
        chars.append(0x1D610)  #glyph04086	MATHEMATICAL SANS-SERIF ITALIC CAPITAL I
        chars.append(0x1D611)  #glyph04087	MATHEMATICAL SANS-SERIF ITALIC CAPITAL J
        chars.append(0x1D612)  #glyph04088	MATHEMATICAL SANS-SERIF ITALIC CAPITAL K
        chars.append(0x1D613)  #glyph04089	MATHEMATICAL SANS-SERIF ITALIC CAPITAL L
        chars.append(0x1D614)  #glyph04090	MATHEMATICAL SANS-SERIF ITALIC CAPITAL M
        chars.append(0x1D615)  #glyph04091	MATHEMATICAL SANS-SERIF ITALIC CAPITAL N
        chars.append(0x1D616)  #glyph04092	MATHEMATICAL SANS-SERIF ITALIC CAPITAL O
        chars.append(0x1D617)  #glyph04093	MATHEMATICAL SANS-SERIF ITALIC CAPITAL P
        chars.append(0x1D618)  #glyph04094	MATHEMATICAL SANS-SERIF ITALIC CAPITAL Q
        chars.append(0x1D619)  #glyph04095	MATHEMATICAL SANS-SERIF ITALIC CAPITAL R
        chars.append(0x1D61A)  #glyph04096	MATHEMATICAL SANS-SERIF ITALIC CAPITAL S
        chars.append(0x1D61B)  #glyph04097	MATHEMATICAL SANS-SERIF ITALIC CAPITAL T
        chars.append(0x1D61C)  #glyph04098	MATHEMATICAL SANS-SERIF ITALIC CAPITAL U
        chars.append(0x1D61D)  #glyph04099	MATHEMATICAL SANS-SERIF ITALIC CAPITAL V
        chars.append(0x1D61E)  #glyph04100	MATHEMATICAL SANS-SERIF ITALIC CAPITAL W
        chars.append(0x1D61F)  #glyph04101	MATHEMATICAL SANS-SERIF ITALIC CAPITAL X
        chars.append(0x1D620)  #glyph04102	MATHEMATICAL SANS-SERIF ITALIC CAPITAL Y
        chars.append(0x1D621)  #glyph04103	MATHEMATICAL SANS-SERIF ITALIC CAPITAL Z
        chars.append(0x1D622)  #glyph04104	MATHEMATICAL SANS-SERIF ITALIC SMALL A
        chars.append(0x1D623)  #glyph04105	MATHEMATICAL SANS-SERIF ITALIC SMALL B
        chars.append(0x1D624)  #glyph04106	MATHEMATICAL SANS-SERIF ITALIC SMALL C
        chars.append(0x1D625)  #glyph04107	MATHEMATICAL SANS-SERIF ITALIC SMALL D
        chars.append(0x1D626)  #glyph04108	MATHEMATICAL SANS-SERIF ITALIC SMALL E
        chars.append(0x1D627)  #glyph04109	MATHEMATICAL SANS-SERIF ITALIC SMALL F
        chars.append(0x1D628)  #glyph04110	MATHEMATICAL SANS-SERIF ITALIC SMALL G
        chars.append(0x1D629)  #glyph04111	MATHEMATICAL SANS-SERIF ITALIC SMALL H
        chars.append(0x1D62A)  #glyph04112	MATHEMATICAL SANS-SERIF ITALIC SMALL I
        chars.append(0x1D62B)  #glyph04113	MATHEMATICAL SANS-SERIF ITALIC SMALL J
        chars.append(0x10115)  #glyph02768	AEGEAN NUMBER SIXTY
        chars.append(0x1D62D)  #glyph04115	MATHEMATICAL SANS-SERIF ITALIC SMALL L
        chars.append(0x1D62E)  #glyph04116	MATHEMATICAL SANS-SERIF ITALIC SMALL M
        chars.append(0x1D62F)  #glyph04117	MATHEMATICAL SANS-SERIF ITALIC SMALL N
        chars.append(0x1D630)  #glyph04118	MATHEMATICAL SANS-SERIF ITALIC SMALL O
        chars.append(0x1D631)  #glyph04119	MATHEMATICAL SANS-SERIF ITALIC SMALL P
        chars.append(0x1D632)  #glyph04120	MATHEMATICAL SANS-SERIF ITALIC SMALL Q
        chars.append(0x1D633)  #glyph04121	MATHEMATICAL SANS-SERIF ITALIC SMALL R
        chars.append(0x1D634)  #glyph04122	MATHEMATICAL SANS-SERIF ITALIC SMALL S
        chars.append(0x1D635)  #glyph04123	MATHEMATICAL SANS-SERIF ITALIC SMALL T
        chars.append(0x1D636)  #glyph04124	MATHEMATICAL SANS-SERIF ITALIC SMALL U
        chars.append(0x1D637)  #glyph04125	MATHEMATICAL SANS-SERIF ITALIC SMALL V
        chars.append(0x1D638)  #glyph04126	MATHEMATICAL SANS-SERIF ITALIC SMALL W
        chars.append(0x1D639)  #glyph04127	MATHEMATICAL SANS-SERIF ITALIC SMALL X
        chars.append(0x1D63A)  #glyph04128	MATHEMATICAL SANS-SERIF ITALIC SMALL Y
        chars.append(0x1D63B)  #glyph04129	MATHEMATICAL SANS-SERIF ITALIC SMALL Z
        chars.append(0x1D63C)  #glyph04130	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL A
        chars.append(0x1D63D)  #glyph04131	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL B
        chars.append(0x1D63E)  #glyph04132	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL C
        chars.append(0x1D63F)  #glyph04133	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL D
        chars.append(0x1D640)  #glyph04134	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL E
        chars.append(0x1D641)  #glyph04135	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL F
        chars.append(0x1D642)  #glyph04136	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL G
        chars.append(0x1D643)  #glyph04137	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL H
        chars.append(0x1D644)  #glyph04138	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL I
        chars.append(0x1D645)  #glyph04139	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL J
        chars.append(0x1D646)  #glyph04140	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL K
        chars.append(0x1D647)  #glyph04141	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL L
        chars.append(0x1D648)  #glyph04142	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL M
        chars.append(0x1D649)  #glyph04143	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL N
        chars.append(0x1D64A)  #glyph04144	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL O
        chars.append(0x1D64B)  #glyph04145	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL P
        chars.append(0x1D64C)  #glyph04146	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL Q
        chars.append(0x1D64D)  #glyph04147	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL R
        chars.append(0x1D64E)  #glyph04148	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL S
        chars.append(0x1D64F)  #glyph04149	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL T
        chars.append(0x1D650)  #glyph04150	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL U
        chars.append(0x1D651)  #glyph04151	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL V
        chars.append(0x1D652)  #glyph04152	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL W
        chars.append(0x1D653)  #glyph04153	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL X
        chars.append(0x1D654)  #glyph04154	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL Y
        chars.append(0x1D655)  #glyph04155	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL Z
        chars.append(0x1D656)  #glyph04156	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL A
        chars.append(0x1D657)  #glyph04157	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL B
        chars.append(0x1D658)  #glyph04158	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL C
        chars.append(0x1D659)  #glyph04159	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL D
        chars.append(0x1D65A)  #glyph04160	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL E
        chars.append(0x1D65B)  #glyph04161	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL F
        chars.append(0x1D65C)  #glyph04162	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL G
        chars.append(0x1D65D)  #glyph04163	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL H
        chars.append(0x1D65E)  #glyph04164	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL I
        chars.append(0x1D65F)  #glyph04165	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL J
        chars.append(0x1D660)  #glyph04166	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL K
        chars.append(0x1D661)  #glyph04167	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL L
        chars.append(0x1D662)  #glyph04168	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL M
        chars.append(0x1D663)  #glyph04169	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL N
        chars.append(0x1D664)  #glyph04170	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL O
        chars.append(0x1D665)  #glyph04171	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL P
        chars.append(0x1D666)  #glyph04172	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL Q
        chars.append(0x1D667)  #glyph04173	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL R
        chars.append(0x1D668)  #glyph04174	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL S
        chars.append(0x1D669)  #glyph04175	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL T
        chars.append(0x1D66A)  #glyph04176	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL U
        chars.append(0x1D66B)  #glyph04177	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL V
        chars.append(0x1D66C)  #glyph04178	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL W
        chars.append(0x1D66D)  #glyph04179	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL X
        chars.append(0x1D66E)  #glyph04180	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL Y
        chars.append(0x1D66F)  #glyph04181	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL Z
        chars.append(0x1D670)  #glyph04182	MATHEMATICAL MONOSPACE CAPITAL A
        chars.append(0x1D671)  #glyph04183	MATHEMATICAL MONOSPACE CAPITAL B
        chars.append(0x1D672)  #glyph04184	MATHEMATICAL MONOSPACE CAPITAL C
        chars.append(0x1D673)  #glyph04185	MATHEMATICAL MONOSPACE CAPITAL D
        chars.append(0x1D674)  #glyph04186	MATHEMATICAL MONOSPACE CAPITAL E
        chars.append(0x1D675)  #glyph04187	MATHEMATICAL MONOSPACE CAPITAL F
        chars.append(0x1D676)  #glyph04188	MATHEMATICAL MONOSPACE CAPITAL G
        chars.append(0x1D677)  #glyph04189	MATHEMATICAL MONOSPACE CAPITAL H
        chars.append(0x1D678)  #glyph04190	MATHEMATICAL MONOSPACE CAPITAL I
        chars.append(0x1D679)  #glyph04191	MATHEMATICAL MONOSPACE CAPITAL J
        chars.append(0x1D67A)  #glyph04192	MATHEMATICAL MONOSPACE CAPITAL K
        chars.append(0x1D67B)  #glyph04193	MATHEMATICAL MONOSPACE CAPITAL L
        chars.append(0x1D67C)  #glyph04194	MATHEMATICAL MONOSPACE CAPITAL M
        chars.append(0x1D67D)  #glyph04195	MATHEMATICAL MONOSPACE CAPITAL N
        chars.append(0x1D67E)  #glyph04196	MATHEMATICAL MONOSPACE CAPITAL O
        chars.append(0x1D67F)  #glyph04197	MATHEMATICAL MONOSPACE CAPITAL P
        chars.append(0x1D680)  #glyph04198	MATHEMATICAL MONOSPACE CAPITAL Q
        chars.append(0x1D681)  #glyph04199	MATHEMATICAL MONOSPACE CAPITAL R
        chars.append(0x1D682)  #glyph04200	MATHEMATICAL MONOSPACE CAPITAL S
        chars.append(0x1D683)  #glyph04201	MATHEMATICAL MONOSPACE CAPITAL T
        chars.append(0x1D684)  #glyph04202	MATHEMATICAL MONOSPACE CAPITAL U
        chars.append(0x1D685)  #glyph04203	MATHEMATICAL MONOSPACE CAPITAL V
        chars.append(0x1D686)  #glyph04204	MATHEMATICAL MONOSPACE CAPITAL W
        chars.append(0x23C1)  #uni23C1	DENTISTRY SYMBOL LIGHT DOWN AND HORIZONTAL WITH CIRCLE
        chars.append(0x1D688)  #glyph04206	MATHEMATICAL MONOSPACE CAPITAL Y
        chars.append(0x1D689)  #glyph04207	MATHEMATICAL MONOSPACE CAPITAL Z
        chars.append(0x1D68A)  #glyph04208	MATHEMATICAL MONOSPACE SMALL A
        chars.append(0x1D68B)  #glyph04209	MATHEMATICAL MONOSPACE SMALL B
        chars.append(0x1D68C)  #glyph04210	MATHEMATICAL MONOSPACE SMALL C
        chars.append(0x1D68D)  #glyph04211	MATHEMATICAL MONOSPACE SMALL D
        chars.append(0x1D68E)  #glyph04212	MATHEMATICAL MONOSPACE SMALL E
        chars.append(0x1D68F)  #glyph04213	MATHEMATICAL MONOSPACE SMALL F
        chars.append(0x1D690)  #glyph04214	MATHEMATICAL MONOSPACE SMALL G
        chars.append(0x1D691)  #glyph04215	MATHEMATICAL MONOSPACE SMALL H
        chars.append(0x10129)  #glyph02788	AEGEAN NUMBER EIGHT THOUSAND
        chars.append(0x1D693)  #glyph04217	MATHEMATICAL MONOSPACE SMALL J
        chars.append(0x1D694)  #glyph04218	MATHEMATICAL MONOSPACE SMALL K
        chars.append(0x1D695)  #glyph04219	MATHEMATICAL MONOSPACE SMALL L
        chars.append(0x1D696)  #glyph04220	MATHEMATICAL MONOSPACE SMALL M
        chars.append(0x1D697)  #glyph04221	MATHEMATICAL MONOSPACE SMALL N
        chars.append(0x1D698)  #glyph04222	MATHEMATICAL MONOSPACE SMALL O
        chars.append(0x1D699)  #glyph04223	MATHEMATICAL MONOSPACE SMALL P
        chars.append(0x1D69A)  #glyph04224	MATHEMATICAL MONOSPACE SMALL Q
        chars.append(0x1D69B)  #glyph04225	MATHEMATICAL MONOSPACE SMALL R
        chars.append(0x1D69C)  #glyph04226	MATHEMATICAL MONOSPACE SMALL S
        chars.append(0x1D69D)  #glyph04227	MATHEMATICAL MONOSPACE SMALL T
        chars.append(0x1D69E)  #glyph04228	MATHEMATICAL MONOSPACE SMALL U
        chars.append(0x1D69F)  #glyph04229	MATHEMATICAL MONOSPACE SMALL V
        chars.append(0x1D6A0)  #glyph04230	MATHEMATICAL MONOSPACE SMALL W
        chars.append(0x1D6A1)  #glyph04231	MATHEMATICAL MONOSPACE SMALL X
        chars.append(0x1D6A2)  #glyph04232	MATHEMATICAL MONOSPACE SMALL Y
        chars.append(0x1D6A3)  #glyph04233	MATHEMATICAL MONOSPACE SMALL Z
        chars.append(0x1D6A4)  #glyph04234	MATHEMATICAL ITALIC SMALL DOTLESS I
        chars.append(0x1D6A5)  #glyph04235	MATHEMATICAL ITALIC SMALL DOTLESS J
        chars.append(0x1D6A8)  #glyph04236	MATHEMATICAL BOLD CAPITAL ALPHA
        chars.append(0x1D6A9)  #glyph04237	MATHEMATICAL BOLD CAPITAL BETA
        chars.append(0x1D6AA)  #glyph04238	MATHEMATICAL BOLD CAPITAL GAMMA
        chars.append(0x1D6AB)  #glyph04239	MATHEMATICAL BOLD CAPITAL DELTA
        chars.append(0x1D6AC)  #glyph04240	MATHEMATICAL BOLD CAPITAL EPSILON
        chars.append(0x1D6AD)  #glyph04241	MATHEMATICAL BOLD CAPITAL ZETA
        chars.append(0x1D6AE)  #glyph04242	MATHEMATICAL BOLD CAPITAL ETA
        chars.append(0x1D6AF)  #glyph04243	MATHEMATICAL BOLD CAPITAL THETA
        chars.append(0x1D6B0)  #glyph04244	MATHEMATICAL BOLD CAPITAL IOTA
        chars.append(0x1D6B1)  #glyph04245	MATHEMATICAL BOLD CAPITAL KAPPA
        chars.append(0x1D6B2)  #glyph04246	MATHEMATICAL BOLD CAPITAL LAMDA
        chars.append(0x1D6B3)  #glyph04247	MATHEMATICAL BOLD CAPITAL MU
        chars.append(0x1D6B4)  #glyph04248	MATHEMATICAL BOLD CAPITAL NU
        chars.append(0x1D6B5)  #glyph04249	MATHEMATICAL BOLD CAPITAL XI
        chars.append(0x1D6B6)  #glyph04250	MATHEMATICAL BOLD CAPITAL OMICRON
        chars.append(0x1D6B7)  #glyph04251	MATHEMATICAL BOLD CAPITAL PI
        chars.append(0x1D6B8)  #glyph04252	MATHEMATICAL BOLD CAPITAL RHO
        chars.append(0x1D6B9)  #glyph04253	MATHEMATICAL BOLD CAPITAL THETA SYMBOL
        chars.append(0x1D6BA)  #glyph04254	MATHEMATICAL BOLD CAPITAL SIGMA
        chars.append(0x1D6BB)  #glyph04255	MATHEMATICAL BOLD CAPITAL TAU
        chars.append(0x1D6BC)  #glyph04256	MATHEMATICAL BOLD CAPITAL UPSILON
        chars.append(0x1D6BD)  #glyph04257	MATHEMATICAL BOLD CAPITAL PHI
        chars.append(0x1D6BE)  #glyph04258	MATHEMATICAL BOLD CAPITAL CHI
        chars.append(0x1D6BF)  #glyph04259	MATHEMATICAL BOLD CAPITAL PSI
        chars.append(0x1D6C0)  #glyph04260	MATHEMATICAL BOLD CAPITAL OMEGA
        chars.append(0x1D6C1)  #glyph04261	MATHEMATICAL BOLD NABLA
        chars.append(0x1D6C2)  #glyph04262	MATHEMATICAL BOLD SMALL ALPHA
        chars.append(0x1D6C3)  #glyph04263	MATHEMATICAL BOLD SMALL BETA
        chars.append(0x1D6C4)  #glyph04264	MATHEMATICAL BOLD SMALL GAMMA
        chars.append(0x1D6C5)  #glyph04265	MATHEMATICAL BOLD SMALL DELTA
        chars.append(0x1D6C6)  #glyph04266	MATHEMATICAL BOLD SMALL EPSILON
        chars.append(0x1D6C7)  #glyph04267	MATHEMATICAL BOLD SMALL ZETA
        chars.append(0x1D6C8)  #glyph04268	MATHEMATICAL BOLD SMALL ETA
        chars.append(0x1D6C9)  #glyph04269	MATHEMATICAL BOLD SMALL THETA
        chars.append(0x1D6CA)  #glyph04270	MATHEMATICAL BOLD SMALL IOTA
        chars.append(0x1D6CB)  #glyph04271	MATHEMATICAL BOLD SMALL KAPPA
        chars.append(0x1D6CC)  #glyph04272	MATHEMATICAL BOLD SMALL LAMDA
        chars.append(0x1D6CD)  #glyph04273	MATHEMATICAL BOLD SMALL MU
        chars.append(0x1D6CE)  #glyph04274	MATHEMATICAL BOLD SMALL NU
        chars.append(0x1D6CF)  #glyph04275	MATHEMATICAL BOLD SMALL XI
        chars.append(0x1D6D0)  #glyph04276	MATHEMATICAL BOLD SMALL OMICRON
        chars.append(0x1D6D1)  #glyph04277	MATHEMATICAL BOLD SMALL PI
        chars.append(0x1D6D2)  #glyph04278	MATHEMATICAL BOLD SMALL RHO
        chars.append(0x1D6D3)  #glyph04279	MATHEMATICAL BOLD SMALL FINAL SIGMA
        chars.append(0x1D6D4)  #glyph04280	MATHEMATICAL BOLD SMALL SIGMA
        chars.append(0x1D6D5)  #glyph04281	MATHEMATICAL BOLD SMALL TAU
        chars.append(0x1D6D6)  #glyph04282	MATHEMATICAL BOLD SMALL UPSILON
        chars.append(0x1D6D7)  #glyph04283	MATHEMATICAL BOLD SMALL PHI
        chars.append(0x1D6D8)  #glyph04284	MATHEMATICAL BOLD SMALL CHI
        chars.append(0x1D6D9)  #glyph04285	MATHEMATICAL BOLD SMALL PSI
        chars.append(0x1D6DA)  #glyph04286	MATHEMATICAL BOLD SMALL OMEGA
        chars.append(0x1D6DB)  #glyph04287	MATHEMATICAL BOLD PARTIAL DIFFERENTIAL
        chars.append(0x1D6DC)  #glyph04288	MATHEMATICAL BOLD EPSILON SYMBOL
        chars.append(0x1D6DD)  #glyph04289	MATHEMATICAL BOLD THETA SYMBOL
        chars.append(0x1D6DE)  #glyph04290	MATHEMATICAL BOLD KAPPA SYMBOL
        chars.append(0x1D6DF)  #glyph04291	MATHEMATICAL BOLD PHI SYMBOL
        chars.append(0x1D6E0)  #glyph04292	MATHEMATICAL BOLD RHO SYMBOL
        chars.append(0x1D6E1)  #glyph04293	MATHEMATICAL BOLD PI SYMBOL
        chars.append(0x1D6E2)  #glyph04294	MATHEMATICAL ITALIC CAPITAL ALPHA
        chars.append(0x1D6E3)  #glyph04295	MATHEMATICAL ITALIC CAPITAL BETA
        chars.append(0x1D6E4)  #glyph04296	MATHEMATICAL ITALIC CAPITAL GAMMA
        chars.append(0x1D6E5)  #glyph04297	MATHEMATICAL ITALIC CAPITAL DELTA
        chars.append(0x1D6E6)  #glyph04298	MATHEMATICAL ITALIC CAPITAL EPSILON
        chars.append(0x1D6E7)  #glyph04299	MATHEMATICAL ITALIC CAPITAL ZETA
        chars.append(0x1D6E8)  #glyph04300	MATHEMATICAL ITALIC CAPITAL ETA
        chars.append(0x1D6E9)  #glyph04301	MATHEMATICAL ITALIC CAPITAL THETA
        chars.append(0x1D6EA)  #glyph04302	MATHEMATICAL ITALIC CAPITAL IOTA
        chars.append(0x1D6EB)  #glyph04303	MATHEMATICAL ITALIC CAPITAL KAPPA
        chars.append(0x1D6EC)  #glyph04304	MATHEMATICAL ITALIC CAPITAL LAMDA
        chars.append(0x1D6ED)  #glyph04305	MATHEMATICAL ITALIC CAPITAL MU
        chars.append(0x1D6EE)  #glyph04306	MATHEMATICAL ITALIC CAPITAL NU
        chars.append(0x1D6EF)  #glyph04307	MATHEMATICAL ITALIC CAPITAL XI
        chars.append(0x1D6F0)  #glyph04308	MATHEMATICAL ITALIC CAPITAL OMICRON
        chars.append(0x1D6F1)  #glyph04309	MATHEMATICAL ITALIC CAPITAL PI
        chars.append(0x10190)  #glyph02883	ROMAN SEXTANS SIGN
        chars.append(0x1D6F3)  #glyph04311	MATHEMATICAL ITALIC CAPITAL THETA SYMBOL
        chars.append(0x1D6F4)  #glyph04312	MATHEMATICAL ITALIC CAPITAL SIGMA
        chars.append(0x1D6F5)  #glyph04313	MATHEMATICAL ITALIC CAPITAL TAU
        chars.append(0x1D6F6)  #glyph04314	MATHEMATICAL ITALIC CAPITAL UPSILON
        chars.append(0x1D6F7)  #glyph04315	MATHEMATICAL ITALIC CAPITAL PHI
        chars.append(0x1D6F8)  #glyph04316	MATHEMATICAL ITALIC CAPITAL CHI
        chars.append(0x1010F)  #glyph02762	AEGEAN NUMBER NINE
        chars.append(0x1D6FA)  #glyph04318	MATHEMATICAL ITALIC CAPITAL OMEGA
        chars.append(0x1D6FB)  #glyph04319	MATHEMATICAL ITALIC NABLA
        chars.append(0x1D6FC)  #glyph04320	MATHEMATICAL ITALIC SMALL ALPHA
        chars.append(0x1D6FD)  #glyph04321	MATHEMATICAL ITALIC SMALL BETA
        chars.append(0x1D6FE)  #glyph04322	MATHEMATICAL ITALIC SMALL GAMMA
        chars.append(0x1D6FF)  #glyph04323	MATHEMATICAL ITALIC SMALL DELTA
        chars.append(0x1D700)  #glyph04324	MATHEMATICAL ITALIC SMALL EPSILON
        chars.append(0x1D701)  #glyph04325	MATHEMATICAL ITALIC SMALL ZETA
        chars.append(0x1D702)  #glyph04326	MATHEMATICAL ITALIC SMALL ETA
        chars.append(0x1D703)  #glyph04327	MATHEMATICAL ITALIC SMALL THETA
        chars.append(0x1D704)  #glyph04328	MATHEMATICAL ITALIC SMALL IOTA
        chars.append(0x1D705)  #glyph04329	MATHEMATICAL ITALIC SMALL KAPPA
        chars.append(0x1D706)  #glyph04330	MATHEMATICAL ITALIC SMALL LAMDA
        chars.append(0x1D707)  #glyph04331	MATHEMATICAL ITALIC SMALL MU
        chars.append(0x1D708)  #glyph04332	MATHEMATICAL ITALIC SMALL NU
        chars.append(0x1D709)  #glyph04333	MATHEMATICAL ITALIC SMALL XI
        chars.append(0x1D70A)  #glyph04334	MATHEMATICAL ITALIC SMALL OMICRON
        chars.append(0x1D70B)  #glyph04335	MATHEMATICAL ITALIC SMALL PI
        chars.append(0x1D70C)  #glyph04336	MATHEMATICAL ITALIC SMALL RHO
        chars.append(0x1D70D)  #glyph04337	MATHEMATICAL ITALIC SMALL FINAL SIGMA
        chars.append(0x1D70E)  #glyph04338	MATHEMATICAL ITALIC SMALL SIGMA
        chars.append(0x1D70F)  #glyph04339	MATHEMATICAL ITALIC SMALL TAU
        chars.append(0x10191)  #glyph02884	ROMAN UNCIA SIGN
        chars.append(0x1D711)  #glyph04341	MATHEMATICAL ITALIC SMALL PHI
        chars.append(0x1D712)  #glyph04342	MATHEMATICAL ITALIC SMALL CHI
        chars.append(0x1D713)  #glyph04343	MATHEMATICAL ITALIC SMALL PSI
        chars.append(0x1D714)  #glyph04344	MATHEMATICAL ITALIC SMALL OMEGA
        chars.append(0x1D715)  #glyph04345	MATHEMATICAL ITALIC PARTIAL DIFFERENTIAL
        chars.append(0x1D716)  #glyph04346	MATHEMATICAL ITALIC EPSILON SYMBOL
        chars.append(0x1D717)  #glyph04347	MATHEMATICAL ITALIC THETA SYMBOL
        chars.append(0x1D718)  #glyph04348	MATHEMATICAL ITALIC KAPPA SYMBOL
        chars.append(0x1D719)  #glyph04349	MATHEMATICAL ITALIC PHI SYMBOL
        chars.append(0x1D71A)  #glyph04350	MATHEMATICAL ITALIC RHO SYMBOL
        chars.append(0x1D71B)  #glyph04351	MATHEMATICAL ITALIC PI SYMBOL
        chars.append(0x1D71C)  #glyph04352	MATHEMATICAL BOLD ITALIC CAPITAL ALPHA
        chars.append(0x1D71D)  #glyph04353	MATHEMATICAL BOLD ITALIC CAPITAL BETA
        chars.append(0x1D71E)  #glyph04354	MATHEMATICAL BOLD ITALIC CAPITAL GAMMA
        chars.append(0x1D71F)  #glyph04355	MATHEMATICAL BOLD ITALIC CAPITAL DELTA
        chars.append(0x1D720)  #glyph04356	MATHEMATICAL BOLD ITALIC CAPITAL EPSILON
        chars.append(0x1D721)  #glyph04357	MATHEMATICAL BOLD ITALIC CAPITAL ZETA
        chars.append(0x1D722)  #glyph04358	MATHEMATICAL BOLD ITALIC CAPITAL ETA
        chars.append(0x1D723)  #glyph04359	MATHEMATICAL BOLD ITALIC CAPITAL THETA
        chars.append(0x1D724)  #glyph04360	MATHEMATICAL BOLD ITALIC CAPITAL IOTA
        chars.append(0x1D725)  #glyph04361	MATHEMATICAL BOLD ITALIC CAPITAL KAPPA
        chars.append(0x1D726)  #glyph04362	MATHEMATICAL BOLD ITALIC CAPITAL LAMDA
        chars.append(0x1D727)  #glyph04363	MATHEMATICAL BOLD ITALIC CAPITAL MU
        chars.append(0x1012A)  #glyph02789	AEGEAN NUMBER NINE THOUSAND
        chars.append(0x1D729)  #glyph04365	MATHEMATICAL BOLD ITALIC CAPITAL XI
        chars.append(0x1D72A)  #glyph04366	MATHEMATICAL BOLD ITALIC CAPITAL OMICRON
        chars.append(0x1D72B)  #glyph04367	MATHEMATICAL BOLD ITALIC CAPITAL PI
        chars.append(0x1D72C)  #glyph04368	MATHEMATICAL BOLD ITALIC CAPITAL RHO
        chars.append(0x1D72D)  #glyph04369	MATHEMATICAL BOLD ITALIC CAPITAL THETA SYMBOL
        chars.append(0x10192)  #glyph02885	ROMAN SEMUNCIA SIGN
        chars.append(0x1D72F)  #glyph04371	MATHEMATICAL BOLD ITALIC CAPITAL TAU
        chars.append(0x1D730)  #glyph04372	MATHEMATICAL BOLD ITALIC CAPITAL UPSILON
        chars.append(0x1D731)  #glyph04373	MATHEMATICAL BOLD ITALIC CAPITAL PHI
        chars.append(0x1D732)  #glyph04374	MATHEMATICAL BOLD ITALIC CAPITAL CHI
        chars.append(0x1D733)  #glyph04375	MATHEMATICAL BOLD ITALIC CAPITAL PSI
        chars.append(0x1D734)  #glyph04376	MATHEMATICAL BOLD ITALIC CAPITAL OMEGA
        chars.append(0x1D735)  #glyph04377	MATHEMATICAL BOLD ITALIC NABLA
        chars.append(0x1D736)  #glyph04378	MATHEMATICAL BOLD ITALIC SMALL ALPHA
        chars.append(0x1D737)  #glyph04379	MATHEMATICAL BOLD ITALIC SMALL BETA
        chars.append(0x1D738)  #glyph04380	MATHEMATICAL BOLD ITALIC SMALL GAMMA
        chars.append(0x1D739)  #glyph04381	MATHEMATICAL BOLD ITALIC SMALL DELTA
        chars.append(0x1D73A)  #glyph04382	MATHEMATICAL BOLD ITALIC SMALL EPSILON
        chars.append(0x1D73B)  #glyph04383	MATHEMATICAL BOLD ITALIC SMALL ZETA
        chars.append(0x1D73C)  #glyph04384	MATHEMATICAL BOLD ITALIC SMALL ETA
        chars.append(0x1D73D)  #glyph04385	MATHEMATICAL BOLD ITALIC SMALL THETA
        chars.append(0x1D73E)  #glyph04386	MATHEMATICAL BOLD ITALIC SMALL IOTA
        chars.append(0x1D73F)  #glyph04387	MATHEMATICAL BOLD ITALIC SMALL KAPPA
        chars.append(0x1D740)  #glyph04388	MATHEMATICAL BOLD ITALIC SMALL LAMDA
        chars.append(0x1D741)  #glyph04389	MATHEMATICAL BOLD ITALIC SMALL MU
        chars.append(0x1D742)  #glyph04390	MATHEMATICAL BOLD ITALIC SMALL NU
        chars.append(0x1D743)  #glyph04391	MATHEMATICAL BOLD ITALIC SMALL XI
        chars.append(0x1D744)  #glyph04392	MATHEMATICAL BOLD ITALIC SMALL OMICRON
        chars.append(0x1D745)  #glyph04393	MATHEMATICAL BOLD ITALIC SMALL PI
        chars.append(0x1D746)  #glyph04394	MATHEMATICAL BOLD ITALIC SMALL RHO
        chars.append(0x1D747)  #glyph04395	MATHEMATICAL BOLD ITALIC SMALL FINAL SIGMA
        chars.append(0x1D748)  #glyph04396	MATHEMATICAL BOLD ITALIC SMALL SIGMA
        chars.append(0x1D749)  #glyph04397	MATHEMATICAL BOLD ITALIC SMALL TAU
        chars.append(0x1D74A)  #glyph04398	MATHEMATICAL BOLD ITALIC SMALL UPSILON
        chars.append(0x1D74B)  #glyph04399	MATHEMATICAL BOLD ITALIC SMALL PHI
        chars.append(0x10193)  #glyph02886	ROMAN SEXTULA SIGN
        chars.append(0x1D74D)  #glyph04401	MATHEMATICAL BOLD ITALIC SMALL PSI
        chars.append(0x1D74E)  #glyph04402	MATHEMATICAL BOLD ITALIC SMALL OMEGA
        chars.append(0x1D74F)  #glyph04403	MATHEMATICAL BOLD ITALIC PARTIAL DIFFERENTIAL
        chars.append(0x1D750)  #glyph04404	MATHEMATICAL BOLD ITALIC EPSILON SYMBOL
        chars.append(0x1D751)  #glyph04405	MATHEMATICAL BOLD ITALIC THETA SYMBOL
        chars.append(0x1D752)  #glyph04406	MATHEMATICAL BOLD ITALIC KAPPA SYMBOL
        chars.append(0x1D753)  #glyph04407	MATHEMATICAL BOLD ITALIC PHI SYMBOL
        chars.append(0x1D62C)  #glyph04114	MATHEMATICAL SANS-SERIF ITALIC SMALL K
        chars.append(0x1D755)  #glyph04409	MATHEMATICAL BOLD ITALIC PI SYMBOL
        chars.append(0x1D756)  #glyph04410	MATHEMATICAL SANS-SERIF BOLD CAPITAL ALPHA
        chars.append(0x1D757)  #glyph04411	MATHEMATICAL SANS-SERIF BOLD CAPITAL BETA
        chars.append(0x1D758)  #glyph04412	MATHEMATICAL SANS-SERIF BOLD CAPITAL GAMMA
        chars.append(0x1D759)  #glyph04413	MATHEMATICAL SANS-SERIF BOLD CAPITAL DELTA
        chars.append(0x1D75A)  #glyph04414	MATHEMATICAL SANS-SERIF BOLD CAPITAL EPSILON
        chars.append(0x1D75B)  #glyph04415	MATHEMATICAL SANS-SERIF BOLD CAPITAL ZETA
        chars.append(0xA701)  #uniA701	MODIFIER LETTER CHINESE TONE YANG PING
        chars.append(0x1D75D)  #glyph04417	MATHEMATICAL SANS-SERIF BOLD CAPITAL THETA
        chars.append(0x1D75E)  #glyph04418	MATHEMATICAL SANS-SERIF BOLD CAPITAL IOTA
        chars.append(0x1D75F)  #glyph04419	MATHEMATICAL SANS-SERIF BOLD CAPITAL KAPPA
        chars.append(0x1D760)  #glyph04420	MATHEMATICAL SANS-SERIF BOLD CAPITAL LAMDA
        chars.append(0x1D761)  #glyph04421	MATHEMATICAL SANS-SERIF BOLD CAPITAL MU
        chars.append(0x1D762)  #glyph04422	MATHEMATICAL SANS-SERIF BOLD CAPITAL NU
        chars.append(0x1D763)  #glyph04423	MATHEMATICAL SANS-SERIF BOLD CAPITAL XI
        chars.append(0x1D764)  #glyph04424	MATHEMATICAL SANS-SERIF BOLD CAPITAL OMICRON
        chars.append(0x1D765)  #glyph04425	MATHEMATICAL SANS-SERIF BOLD CAPITAL PI
        chars.append(0x1D766)  #glyph04426	MATHEMATICAL SANS-SERIF BOLD CAPITAL RHO
        chars.append(0x1D767)  #glyph04427	MATHEMATICAL SANS-SERIF BOLD CAPITAL THETA SYMBOL
        chars.append(0x1D768)  #glyph04428	MATHEMATICAL SANS-SERIF BOLD CAPITAL SIGMA
        chars.append(0x1D769)  #glyph04429	MATHEMATICAL SANS-SERIF BOLD CAPITAL TAU
        chars.append(0x10194)  #glyph02887	ROMAN DIMIDIA SEXTULA SIGN
        chars.append(0x1D76B)  #glyph04431	MATHEMATICAL SANS-SERIF BOLD CAPITAL PHI
        chars.append(0x1D76C)  #glyph04432	MATHEMATICAL SANS-SERIF BOLD CAPITAL CHI
        chars.append(0x1D76D)  #glyph04433	MATHEMATICAL SANS-SERIF BOLD CAPITAL PSI
        chars.append(0x1D76E)  #glyph04434	MATHEMATICAL SANS-SERIF BOLD CAPITAL OMEGA
        chars.append(0x1D76F)  #glyph04435	MATHEMATICAL SANS-SERIF BOLD NABLA
        chars.append(0x1D770)  #glyph04436	MATHEMATICAL SANS-SERIF BOLD SMALL ALPHA
        chars.append(0x1D771)  #glyph04437	MATHEMATICAL SANS-SERIF BOLD SMALL BETA
        chars.append(0x1D772)  #glyph04438	MATHEMATICAL SANS-SERIF BOLD SMALL GAMMA
        chars.append(0x1D773)  #glyph04439	MATHEMATICAL SANS-SERIF BOLD SMALL DELTA
        chars.append(0x1D774)  #glyph04440	MATHEMATICAL SANS-SERIF BOLD SMALL EPSILON
        chars.append(0x1D775)  #glyph04441	MATHEMATICAL SANS-SERIF BOLD SMALL ZETA
        chars.append(0x1D776)  #glyph04442	MATHEMATICAL SANS-SERIF BOLD SMALL ETA
        chars.append(0x1D777)  #glyph04443	MATHEMATICAL SANS-SERIF BOLD SMALL THETA
        chars.append(0x1D778)  #glyph04444	MATHEMATICAL SANS-SERIF BOLD SMALL IOTA
        chars.append(0x1D779)  #glyph04445	MATHEMATICAL SANS-SERIF BOLD SMALL KAPPA
        chars.append(0xA702)  #uniA702	MODIFIER LETTER CHINESE TONE YIN SHANG
        chars.append(0x1D77B)  #glyph04447	MATHEMATICAL SANS-SERIF BOLD SMALL MU
        chars.append(0x1D77C)  #glyph04448	MATHEMATICAL SANS-SERIF BOLD SMALL NU
        chars.append(0x1D77D)  #glyph04449	MATHEMATICAL SANS-SERIF BOLD SMALL XI
        chars.append(0x1D77E)  #glyph04450	MATHEMATICAL SANS-SERIF BOLD SMALL OMICRON
        chars.append(0x1D77F)  #glyph04451	MATHEMATICAL SANS-SERIF BOLD SMALL PI
        chars.append(0x1D780)  #glyph04452	MATHEMATICAL SANS-SERIF BOLD SMALL RHO
        chars.append(0x1D781)  #glyph04453	MATHEMATICAL SANS-SERIF BOLD SMALL FINAL SIGMA
        chars.append(0x1D782)  #glyph04454	MATHEMATICAL SANS-SERIF BOLD SMALL SIGMA
        chars.append(0x1D783)  #glyph04455	MATHEMATICAL SANS-SERIF BOLD SMALL TAU
        chars.append(0x1D784)  #glyph04456	MATHEMATICAL SANS-SERIF BOLD SMALL UPSILON
        chars.append(0x1D785)  #glyph04457	MATHEMATICAL SANS-SERIF BOLD SMALL PHI
        chars.append(0x1D786)  #glyph04458	MATHEMATICAL SANS-SERIF BOLD SMALL CHI
        chars.append(0x1D787)  #glyph04459	MATHEMATICAL SANS-SERIF BOLD SMALL PSI
        chars.append(0x10195)  #glyph02888	ROMAN SILIQUA SIGN
        chars.append(0x1D789)  #glyph04461	MATHEMATICAL SANS-SERIF BOLD PARTIAL DIFFERENTIAL
        chars.append(0x1D78A)  #glyph04462	MATHEMATICAL SANS-SERIF BOLD EPSILON SYMBOL
        chars.append(0x1D78B)  #glyph04463	MATHEMATICAL SANS-SERIF BOLD THETA SYMBOL
        chars.append(0x1D78C)  #glyph04464	MATHEMATICAL SANS-SERIF BOLD KAPPA SYMBOL
        chars.append(0x1D78D)  #glyph04465	MATHEMATICAL SANS-SERIF BOLD PHI SYMBOL
        chars.append(0x1D78E)  #glyph04466	MATHEMATICAL SANS-SERIF BOLD RHO SYMBOL
        chars.append(0x1D78F)  #glyph04467	MATHEMATICAL SANS-SERIF BOLD PI SYMBOL
        chars.append(0x1D790)  #glyph04468	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL ALPHA
        chars.append(0x1D791)  #glyph04469	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL BETA
        chars.append(0x1D792)  #glyph04470	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL GAMMA
        chars.append(0x1D793)  #glyph04471	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL DELTA
        chars.append(0x1D794)  #glyph04472	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL EPSILON
        chars.append(0x1D795)  #glyph04473	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL ZETA
        chars.append(0x1D796)  #glyph04474	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL ETA
        chars.append(0x1D797)  #glyph04475	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL THETA
        chars.append(0xA703)  #uniA703	MODIFIER LETTER CHINESE TONE YANG SHANG
        chars.append(0x1D799)  #glyph04477	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL KAPPA
        chars.append(0x1D79A)  #glyph04478	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL LAMDA
        chars.append(0x1D79B)  #glyph04479	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL MU
        chars.append(0x1D79C)  #glyph04480	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL NU
        chars.append(0x1D79D)  #glyph04481	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL XI
        chars.append(0x1D79E)  #glyph04482	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL OMICRON
        chars.append(0x1D79F)  #glyph04483	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL PI
        chars.append(0x1D7A0)  #glyph04484	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL RHO
        chars.append(0x1D7A1)  #glyph04485	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL THETA SYMBOL
        chars.append(0x1D7A2)  #glyph04486	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL SIGMA
        chars.append(0x1D7A3)  #glyph04487	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL TAU
        chars.append(0x1D7A4)  #glyph04488	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL UPSILON
        chars.append(0x1D7A5)  #glyph04489	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL PHI
        chars.append(0x10196)  #glyph02889	ROMAN DENARIUS SIGN
        chars.append(0x1D7A7)  #glyph04491	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL PSI
        chars.append(0x1D7A8)  #glyph04492	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL OMEGA
        chars.append(0x1D7A9)  #glyph04493	MATHEMATICAL SANS-SERIF BOLD ITALIC NABLA
        chars.append(0x1D7AA)  #glyph04494	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL ALPHA
        chars.append(0x1D7AB)  #glyph04495	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL BETA
        chars.append(0x1D7AC)  #glyph04496	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL GAMMA
        chars.append(0x1D7AD)  #glyph04497	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL DELTA
        chars.append(0x1D7AE)  #glyph04498	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL EPSILON
        chars.append(0x1D7AF)  #glyph04499	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL ZETA
        chars.append(0x1D7B0)  #glyph04500	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL ETA
        chars.append(0x1D7B1)  #glyph04501	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL THETA
        chars.append(0x1D7B2)  #glyph04502	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL IOTA
        chars.append(0x1D7B3)  #glyph04503	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL KAPPA
        chars.append(0x1D7B4)  #glyph04504	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL LAMDA
        chars.append(0x1D7B5)  #glyph04505	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL MU
        chars.append(0xA704)  #uniA704	MODIFIER LETTER CHINESE TONE YIN QU
        chars.append(0x1D7B7)  #glyph04507	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL XI
        chars.append(0x1D7B8)  #glyph04508	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL OMICRON
        chars.append(0x1D7B9)  #glyph04509	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL PI
        chars.append(0x1D7BA)  #glyph04510	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL RHO
        chars.append(0x1D7BB)  #glyph04511	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL FINAL SIGMA
        chars.append(0x1D7BC)  #glyph04512	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL SIGMA
        chars.append(0x1D7BD)  #glyph04513	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL TAU
        chars.append(0x1012B)  #glyph02790	AEGEAN NUMBER TEN THOUSAND
        chars.append(0x1D7BF)  #glyph04515	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL PHI
        chars.append(0x1D7C0)  #glyph04516	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL CHI
        chars.append(0x1D7C1)  #glyph04517	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL PSI
        chars.append(0x1D7C2)  #glyph04518	MATHEMATICAL SANS-SERIF BOLD ITALIC SMALL OMEGA
        chars.append(0x1D7C3)  #glyph04519	MATHEMATICAL SANS-SERIF BOLD ITALIC PARTIAL DIFFERENTIAL
        chars.append(0x10197)  #glyph02890	ROMAN QUINARIUS SIGN
        chars.append(0x1D7C5)  #glyph04521	MATHEMATICAL SANS-SERIF BOLD ITALIC THETA SYMBOL
        chars.append(0x1D7C6)  #glyph04522	MATHEMATICAL SANS-SERIF BOLD ITALIC KAPPA SYMBOL
        chars.append(0x1D7C7)  #glyph04523	MATHEMATICAL SANS-SERIF BOLD ITALIC PHI SYMBOL
        chars.append(0x1D7C8)  #glyph04524	MATHEMATICAL SANS-SERIF BOLD ITALIC RHO SYMBOL
        chars.append(0x1D7C9)  #glyph04525	MATHEMATICAL SANS-SERIF BOLD ITALIC PI SYMBOL
        chars.append(0x1D7CA)  #glyph04526	MATHEMATICAL BOLD CAPITAL DIGAMMA
        chars.append(0x1D7CB)  #glyph04527	MATHEMATICAL BOLD SMALL DIGAMMA
        chars.append(0x1D7CE)  #glyph04528	MATHEMATICAL BOLD DIGIT ZERO
        chars.append(0x1D7CF)  #glyph04529	MATHEMATICAL BOLD DIGIT ONE
        chars.append(0x1D7D0)  #glyph04530	MATHEMATICAL BOLD DIGIT TWO
        chars.append(0x1D7D1)  #glyph04531	MATHEMATICAL BOLD DIGIT THREE
        chars.append(0x1D7D2)  #glyph04532	MATHEMATICAL BOLD DIGIT FOUR
        chars.append(0x1D7D3)  #glyph04533	MATHEMATICAL BOLD DIGIT FIVE
        chars.append(0xA705)  #uniA705	MODIFIER LETTER CHINESE TONE YANG QU
        chars.append(0x1D7D5)  #glyph04535	MATHEMATICAL BOLD DIGIT SEVEN
        chars.append(0x1D7D6)  #glyph04536	MATHEMATICAL BOLD DIGIT EIGHT
        chars.append(0x1D7D7)  #glyph04537	MATHEMATICAL BOLD DIGIT NINE
        chars.append(0x1D7D8)  #glyph04538	MATHEMATICAL DOUBLE-STRUCK DIGIT ZERO
        chars.append(0x1D7D9)  #glyph04539	MATHEMATICAL DOUBLE-STRUCK DIGIT ONE
        chars.append(0x1D7DA)  #glyph04540	MATHEMATICAL DOUBLE-STRUCK DIGIT TWO
        chars.append(0x1D7DB)  #glyph04541	MATHEMATICAL DOUBLE-STRUCK DIGIT THREE
        chars.append(0x1D7DC)  #glyph04542	MATHEMATICAL DOUBLE-STRUCK DIGIT FOUR
        chars.append(0x1D7DD)  #glyph04543	MATHEMATICAL DOUBLE-STRUCK DIGIT FIVE
        chars.append(0x1D7DE)  #glyph04544	MATHEMATICAL DOUBLE-STRUCK DIGIT SIX
        chars.append(0x1D7DF)  #glyph04545	MATHEMATICAL DOUBLE-STRUCK DIGIT SEVEN
        chars.append(0x1D7E0)  #glyph04546	MATHEMATICAL DOUBLE-STRUCK DIGIT EIGHT
        chars.append(0x1D7E1)  #glyph04547	MATHEMATICAL DOUBLE-STRUCK DIGIT NINE
        chars.append(0x10198)  #glyph02891	ROMAN SESTERTIUS SIGN
        chars.append(0x1D7E3)  #glyph04549	MATHEMATICAL SANS-SERIF DIGIT ONE
        chars.append(0x1D7E4)  #glyph04550	MATHEMATICAL SANS-SERIF DIGIT TWO
        chars.append(0x1D7E5)  #glyph04551	MATHEMATICAL SANS-SERIF DIGIT THREE
        chars.append(0x1D7E6)  #glyph04552	MATHEMATICAL SANS-SERIF DIGIT FOUR
        chars.append(0x1D7E7)  #glyph04553	MATHEMATICAL SANS-SERIF DIGIT FIVE
        chars.append(0x1D050)  #glyph03021	BYZANTINE MUSICAL SYMBOL YPSILI
        chars.append(0x1D7E9)  #glyph04555	MATHEMATICAL SANS-SERIF DIGIT SEVEN
        chars.append(0x1D7EA)  #glyph04556	MATHEMATICAL SANS-SERIF DIGIT EIGHT
        chars.append(0x1D7EB)  #glyph04557	MATHEMATICAL SANS-SERIF DIGIT NINE
        chars.append(0x1D7EC)  #glyph04558	MATHEMATICAL SANS-SERIF BOLD DIGIT ZERO
        chars.append(0x1D7ED)  #glyph04559	MATHEMATICAL SANS-SERIF BOLD DIGIT ONE
        chars.append(0x1D7EE)  #glyph04560	MATHEMATICAL SANS-SERIF BOLD DIGIT TWO
        chars.append(0x1D7EF)  #glyph04561	MATHEMATICAL SANS-SERIF BOLD DIGIT THREE
        chars.append(0x1D7F0)  #glyph04562	MATHEMATICAL SANS-SERIF BOLD DIGIT FOUR
        chars.append(0x1D7F1)  #glyph04563	MATHEMATICAL SANS-SERIF BOLD DIGIT FIVE
        chars.append(0xA706)  #uniA706	MODIFIER LETTER CHINESE TONE YIN RU
        chars.append(0x1D7F3)  #glyph04565	MATHEMATICAL SANS-SERIF BOLD DIGIT SEVEN
        chars.append(0x1D7F4)  #glyph04566	MATHEMATICAL SANS-SERIF BOLD DIGIT EIGHT
        chars.append(0x1D7F5)  #glyph04567	MATHEMATICAL SANS-SERIF BOLD DIGIT NINE
        chars.append(0x1D7F6)  #glyph04568	MATHEMATICAL MONOSPACE DIGIT ZERO
        chars.append(0x1D7F7)  #glyph04569	MATHEMATICAL MONOSPACE DIGIT ONE
        chars.append(0x1D7F8)  #glyph04570	MATHEMATICAL MONOSPACE DIGIT TWO
        chars.append(0x1D7F9)  #glyph04571	MATHEMATICAL MONOSPACE DIGIT THREE
        chars.append(0x1D7FA)  #glyph04572	MATHEMATICAL MONOSPACE DIGIT FOUR
        chars.append(0x1D7FB)  #glyph04573	MATHEMATICAL MONOSPACE DIGIT FIVE
        chars.append(0x1D7FC)  #glyph04574	MATHEMATICAL MONOSPACE DIGIT SIX
        chars.append(0x1D7FD)  #glyph04575	MATHEMATICAL MONOSPACE DIGIT SEVEN
        chars.append(0x1D7FE)  #glyph04576	MATHEMATICAL MONOSPACE DIGIT EIGHT
        chars.append(0x1D7FF)  #glyph04577	MATHEMATICAL MONOSPACE DIGIT NINE
        chars.append(0x10199)  #glyph02892	ROMAN DUPONDIUS SIGN
        chars.append(0x1F0C6)  #glyph04756	????
        chars.append(0xA707)  #uniA707	MODIFIER LETTER CHINESE TONE YANG RU
        chars.append(0x1F049)  #glyph04647	DOMINO TILE HORIZONTAL-03-03
        chars.append(0x1011A)  #glyph02773	AEGEAN NUMBER TWO HUNDRED
        chars.append(0x1F15A)  #glyph04865	????
        chars.append(0x1019A)  #glyph02893	ROMAN AS SIGN
        chars.append(0x1F744)  #glyph05077	????
        chars.append(0xA708)  #uniA708	MODIFIER LETTER EXTRA-HIGH DOTTED TONE BAR
        chars.append(0x1F04A)  #glyph04648	DOMINO TILE HORIZONTAL-03-04
        chars.append(0x1F036)  #glyph04628	DOMINO TILE HORIZONTAL-00-05
        chars.append(0x1F15B)  #glyph04866	????
        chars.append(0x1019B)  #glyph02894	ROMAN CENTURIAL SIGN
        chars.append(0xA709)  #uniA709	MODIFIER LETTER HIGH DOTTED TONE BAR
        chars.append(0x1F04B)  #glyph04649	DOMINO TILE HORIZONTAL-03-05
        chars.append(0x1012C)  #glyph02791	AEGEAN NUMBER TWENTY THOUSAND
        chars.append(0x1F048)  #glyph04646	DOMINO TILE HORIZONTAL-03-02
        chars.append(0x1F15C)  #glyph04867	????
        chars.append(0x1F76A)  #glyph05115	????
        chars.append(0xA70A)  #uniA70A	MODIFIER LETTER MID DOTTED TONE BAR
        chars.append(0x1F14C)  #glyph04851	SQUARED SD
        chars.append(0x1F04C)  #glyph04650	DOMINO TILE HORIZONTAL-03-06
        chars.append(0x1F159)  #glyph04864	????
        chars.append(0x1F15D)  #glyph04868	????
        chars.append(0xA70B)  #uniA70B	MODIFIER LETTER LOW DOTTED TONE BAR
        chars.append(0x1F04D)  #glyph04651	DOMINO TILE HORIZONTAL-04-00
        chars.append(0x1F15E)  #glyph04869	????
        chars.append(0x1F733)  #glyph05060	????
        chars.append(0xA70C)  #uniA70C	MODIFIER LETTER EXTRA-LOW DOTTED TONE BAR
        chars.append(0x1F04E)  #glyph04652	DOMINO TILE HORIZONTAL-04-01
        chars.append(0x1F047)  #glyph04645	DOMINO TILE HORIZONTAL-03-01
        chars.append(0x1F15F)  #glyph04870	NEGATIVE CIRCLED LATIN CAPITAL LETTER P
        chars.append(0x1F117)  #glyph04799	PARENTHESIZED LATIN CAPITAL LETTER H
        chars.append(0x1F0D3)  #glyph04768	????
        chars.append(0x1F13D)  #glyph04836	SQUARED LATIN CAPITAL LETTER N
        chars.append(0xA70D)  #uniA70D	MODIFIER LETTER EXTRA-HIGH DOTTED LEFT-STEM TONE BAR
        chars.append(0x1F04F)  #glyph04653	DOMINO TILE HORIZONTAL-04-02
        chars.append(0x1F160)  #glyph04871	????
        chars.append(0x1F0B6)  #glyph04742	????
        chars.append(0x1F13B)  #glyph04834	????
        chars.append(0x1010B)  #glyph02758	AEGEAN NUMBER FIVE
        chars.append(0xA70E)  #uniA70E	MODIFIER LETTER HIGH DOTTED LEFT-STEM TONE BAR
        chars.append(0x1F027)  #glyph04617	MAHJONG TILE SUMMER
        chars.append(0x1F050)  #glyph04654	DOMINO TILE HORIZONTAL-04-03
        chars.append(0x1012D)  #glyph02792	AEGEAN NUMBER THIRTY THOUSAND
        chars.append(0x1F161)  #glyph04872	????
        chars.append(0xA70F)  #uniA70F	MODIFIER LETTER MID DOTTED LEFT-STEM TONE BAR
        chars.append(0x1F051)  #glyph04655	DOMINO TILE HORIZONTAL-04-04
        chars.append(0x1F122)  #glyph04810	PARENTHESIZED LATIN CAPITAL LETTER S
        chars.append(0x1F162)  #glyph04873	????
        chars.append(0x1F153)  #glyph04858	????
        chars.append(0xA710)  #uniA710	MODIFIER LETTER LOW DOTTED LEFT-STEM TONE BAR
        chars.append(0x1F052)  #glyph04656	DOMINO TILE HORIZONTAL-04-05
        chars.append(0x1F163)  #glyph04874	????
        chars.append(0xA711)  #uniA711	MODIFIER LETTER EXTRA-LOW DOTTED LEFT-STEM TONE BAR
        chars.append(0x1F013)  #glyph04597	MAHJONG TILE FOUR OF BAMBOOS
        chars.append(0x1F053)  #glyph04657	DOMINO TILE HORIZONTAL-04-06
        chars.append(0x1F164)  #glyph04875	????
        chars.append(0xA712)  #uniA712	MODIFIER LETTER EXTRA-HIGH LEFT-STEM TONE BAR
        chars.append(0x1D43A)  #glyph03640	MATHEMATICAL ITALIC CAPITAL G
        chars.append(0x1F054)  #glyph04658	DOMINO TILE HORIZONTAL-05-00
        chars.append(0x1F165)  #glyph04876	????
        chars.append(0xA713)  #uniA713	MODIFIER LETTER HIGH LEFT-STEM TONE BAR
        chars.append(0x1F138)  #glyph04831	????
        chars.append(0x1F055)  #glyph04659	DOMINO TILE HORIZONTAL-05-01
        chars.append(0x1F166)  #glyph04877	????
        chars.append(0xA714)  #uniA714	MODIFIER LETTER MID LEFT-STEM TONE BAR
        chars.append(0x1F0D4)  #glyph04769	????
        chars.append(0x1F056)  #glyph04660	DOMINO TILE HORIZONTAL-05-02
        chars.append(0x1D445)  #glyph03651	MATHEMATICAL ITALIC CAPITAL R
        chars.append(0x1F167)  #glyph04878	????
        chars.append(0xA715)  #uniA715	MODIFIER LETTER LOW LEFT-STEM TONE BAR
        chars.append(0x1F71B)  #glyph05036	????
        chars.append(0x1F057)  #glyph04661	DOMINO TILE HORIZONTAL-05-03
        chars.append(0x1F168)  #glyph04879	????
        chars.append(0x1F143)  #glyph04842	????
        chars.append(0xA716)  #uniA716	MODIFIER LETTER EXTRA-LOW LEFT-STEM TONE BAR
        chars.append(0x1F72D)  #glyph05054	????
        chars.append(0x1F041)  #glyph04639	DOMINO TILE HORIZONTAL-02-02
        chars.append(0x1F0CB)  #glyph04761	????
        chars.append(0x1F169)  #glyph04880	????
        chars.append(0xA717)  #uniA717	MODIFIER LETTER DOT VERTICAL BAR
        chars.append(0x1F70C)  #glyph05021	????
        chars.append(0x1F059)  #glyph04663	DOMINO TILE HORIZONTAL-05-05
        chars.append(0x1F70F)  #glyph05024	????
        chars.append(0x1F16A)  #glyph04881	????
        chars.append(0x1F13C)  #glyph04835	????
        chars.append(0x1F700)  #glyph05009	????
        chars.append(0x1F14E)  #glyph04853	SQUARED PPV
        chars.append(0xA718)  #uniA718	MODIFIER LETTER DOT SLASH
        chars.append(0x1F154)  #glyph04859	????
        chars.append(0x1F05A)  #glyph04664	DOMINO TILE HORIZONTAL-05-06
        chars.append(0x1F104)  #glyph04785	DIGIT THREE COMMA
        chars.append(0x1F16B)  #glyph04882	????
        chars.append(0xA719)  #uniA719	MODIFIER LETTER DOT HORIZONTAL BAR
        chars.append(0x1F05B)  #glyph04665	DOMINO TILE HORIZONTAL-06-00
        chars.append(0x10142)  #glyph02810	GREEK ACROPHONIC ATTIC ONE DRACHMA
        chars.append(0x1D5FC)  #glyph04066	MATHEMATICAL SANS-SERIF BOLD SMALL O
        chars.append(0xA71A)  #uniA71A	MODIFIER LETTER LOWER RIGHT CORNER ANGLE
        chars.append(0x1F05C)  #glyph04666	DOMINO TILE HORIZONTAL-06-01
        chars.append(0x1F0A7)  #glyph04729	????
        chars.append(0xA71B)  #uniA71B	MODIFIER LETTER RAISED UP ARROW
        chars.append(0x1F05D)  #glyph04667	DOMINO TILE HORIZONTAL-06-02
        chars.append(0x1F124)  #glyph04812	PARENTHESIZED LATIN CAPITAL LETTER U
        chars.append(0xA71C)  #uniA71C	MODIFIER LETTER RAISED DOWN ARROW
        chars.append(0x1F703)  #glyph05012	????
        chars.append(0x1F05E)  #glyph04668	DOMINO TILE HORIZONTAL-06-03
        chars.append(0xA71D)  #uniA71D	MODIFIER LETTER RAISED EXCLAMATION MARK
        chars.append(0x1F05F)  #glyph04669	DOMINO TILE HORIZONTAL-06-04
        chars.append(0x1F170)  #glyph04883	????
        chars.append(0x1F0C4)  #glyph04754	????
        chars.append(0x1F730)  #glyph05057	????
        chars.append(0xA71E)  #uniA71E	MODIFIER LETTER RAISED INVERTED EXCLAMATION MARK
        chars.append(0x1F71E)  #glyph05039	????
        chars.append(0x1F060)  #glyph04670	DOMINO TILE HORIZONTAL-06-05
        chars.append(0x1F171)  #glyph04884	????
        chars.append(0xA71F)  #uniA71F	MODIFIER LETTER LOW INVERTED EXCLAMATION MARK
        chars.append(0x1F061)  #glyph04671	DOMINO TILE HORIZONTAL-06-06
        chars.append(0x1F172)  #glyph04885	????
        chars.append(0x1F738)  #glyph05065	????
        chars.append(0x1F016)  #glyph04600	MAHJONG TILE SEVEN OF BAMBOOS
        chars.append(0x1F062)  #glyph04672	DOMINO TILE VERTICAL BACK
        chars.append(0x1F173)  #glyph04886	????
        chars.append(0x1F72A)  #glyph05051	????
        chars.append(0x1F127)  #glyph04815	PARENTHESIZED LATIN CAPITAL LETTER X
        chars.append(0x1F063)  #glyph04673	DOMINO TILE VERTICAL-00-00
        chars.append(0x1F174)  #glyph04887	????
        chars.append(0x1F102)  #glyph04783	DIGIT ONE COMMA
        chars.append(0x1D304)  #glyph03481	DIGRAM FOR EARTHLY HUMAN
        chars.append(0x1F064)  #glyph04674	DOMINO TILE VERTICAL-00-01
        chars.append(0x1F175)  #glyph04888	????
        chars.append(0x1F708)  #glyph05017	????
        chars.append(0x1F71F)  #glyph05040	????
        chars.append(0x1F065)  #glyph04675	DOMINO TILE VERTICAL-00-02
        chars.append(0x1F176)  #glyph04889	????
        chars.append(0x1F0C7)  #glyph04757	????
        chars.append(0x1F066)  #glyph04676	DOMINO TILE VERTICAL-00-03
        chars.append(0x1F177)  #glyph04890	????
        chars.append(0x1F739)  #glyph05066	????
        chars.append(0x1F067)  #glyph04677	DOMINO TILE VERTICAL-00-04
        chars.append(0x1D728)  #glyph04364	MATHEMATICAL BOLD ITALIC CAPITAL NU
        chars.append(0x1F147)  #glyph04846	????
        chars.append(0x1D7A6)  #glyph04490	MATHEMATICAL SANS-SERIF BOLD ITALIC CAPITAL CHI
        chars.append(0x1F068)  #glyph04678	DOMINO TILE VERTICAL-00-05
        chars.append(0x1F179)  #glyph04892	NEGATIVE SQUARED LATIN CAPITAL LETTER J
        chars.append(0x1F0BB)  #glyph04747	????
        chars.append(0x1010C)  #glyph02759	AEGEAN NUMBER SIX
        chars.append(0x1F069)  #glyph04679	DOMINO TILE VERTICAL-00-06
        chars.append(0x1F17A)  #glyph04893	????
        chars.append(0x1F0CF)  #glyph04765	????
        chars.append(0x1F06A)  #glyph04680	DOMINO TILE VERTICAL-01-00
        chars.append(0x1F123)  #glyph04811	PARENTHESIZED LATIN CAPITAL LETTER T
        chars.append(0x1F720)  #glyph05041	????
        chars.append(0x1F17B)  #glyph04894	NEGATIVE SQUARED LATIN CAPITAL LETTER L
        chars.append(0x1F142)  #glyph04841	SQUARED LATIN CAPITAL LETTER S
        chars.append(0x1F06B)  #glyph04681	DOMINO TILE VERTICAL-01-01
        chars.append(0x1F17C)  #glyph04895	NEGATIVE SQUARED LATIN CAPITAL LETTER M
        chars.append(0x10110)  #glyph02763	AEGEAN NUMBER TEN
        chars.append(0x1F06C)  #glyph04682	DOMINO TILE VERTICAL-01-02
        chars.append(0x1F17D)  #glyph04896	????
        chars.append(0x1F06D)  #glyph04683	DOMINO TILE VERTICAL-01-03
        chars.append(0x1F17E)  #glyph04897	????
        chars.append(0x1F0BC)  #glyph04748	????
        chars.append(0x1F132)  #glyph04825	????
        chars.append(0x1F139)  #glyph04832	????
        chars.append(0x1F06E)  #glyph04684	DOMINO TILE VERTICAL-01-04
        chars.append(0x1F17F)  #glyph04898	NEGATIVE SQUARED LATIN CAPITAL LETTER P
        chars.append(0x1F06F)  #glyph04685	DOMINO TILE VERTICAL-01-05
        chars.append(0x1F721)  #glyph05042	????
        chars.append(0x1F180)  #glyph04899	????
        chars.append(0x1F718)  #glyph05033	????
        chars.append(0x1F070)  #glyph04686	DOMINO TILE VERTICAL-01-06
        chars.append(0x1F181)  #glyph04900	????
        chars.append(0x1F152)  #glyph04857	????
        chars.append(0x1F071)  #glyph04687	DOMINO TILE VERTICAL-02-00
        chars.append(0x1F0CC)  #glyph04762	????
        chars.append(0x1F182)  #glyph04901	????
        chars.append(0x1F11D)  #glyph04805	PARENTHESIZED LATIN CAPITAL LETTER N
        chars.append(0x1D4D0)  #glyph03778	MATHEMATICAL BOLD SCRIPT CAPITAL A
        chars.append(0x1F072)  #glyph04688	DOMINO TILE VERTICAL-02-01
        chars.append(0x1F183)  #glyph04902	????
        chars.append(0x1F0BD)  #glyph04749	????
        chars.append(0x1F044)  #glyph04642	DOMINO TILE HORIZONTAL-02-05
        chars.append(0x1D5F2)  #glyph04056	MATHEMATICAL SANS-SERIF BOLD SMALL E
        chars.append(0x1F71D)  #glyph05038	????
        chars.append(0x1F0DA)  #glyph04775	????
        chars.append(0x1F073)  #glyph04689	DOMINO TILE VERTICAL-02-02
        chars.append(0x1F184)  #glyph04903	????
        chars.append(0x1F074)  #glyph04690	DOMINO TILE VERTICAL-02-03
        chars.append(0x10143)  #glyph02811	GREEK ACROPHONIC ATTIC FIVE
        chars.append(0x1F722)  #glyph05043	????
        chars.append(0x1F185)  #glyph04904	????
        chars.append(0x1F075)  #glyph04691	DOMINO TILE VERTICAL-02-04
        chars.append(0x1F186)  #glyph04905	????
        chars.append(0x1F719)  #glyph05034	????
        chars.append(0x1F076)  #glyph04692	DOMINO TILE VERTICAL-02-05
        chars.append(0x1F150)  #glyph04855	????
        chars.append(0x1F187)  #glyph04906	????
        chars.append(0x1F077)  #glyph04693	DOMINO TILE VERTICAL-02-06
        chars.append(0x1F188)  #glyph04907	????
        chars.append(0x1F0BE)  #glyph04750	????
        chars.append(0x1F078)  #glyph04694	DOMINO TILE VERTICAL-03-00
        chars.append(0x1F189)  #glyph04908	????
        chars.append(0x1F717)  #glyph05032	????
        chars.append(0x1F731)  #glyph05058	????
        chars.append(0x1F079)  #glyph04695	DOMINO TILE VERTICAL-03-01
        chars.append(0x1F723)  #glyph05044	????
        chars.append(0x1F18A)  #glyph04909	CROSSED NEGATIVE SQUARED LATIN CAPITAL LETTER P
        chars.append(0x1F13F)  #glyph04838	SQUARED LATIN CAPITAL LETTER P
        chars.append(0x1F07A)  #glyph04696	DOMINO TILE VERTICAL-03-02
        chars.append(0x1F18B)  #glyph04910	NEGATIVE SQUARED IC
        chars.append(0x1F07B)  #glyph04697	DOMINO TILE VERTICAL-03-03
        chars.append(0x1F18C)  #glyph04911	NEGATIVE SQUARED PA
        chars.append(0x1F07C)  #glyph04698	DOMINO TILE VERTICAL-03-04
        chars.append(0x1F157)  #glyph04862	NEGATIVE CIRCLED LATIN CAPITAL LETTER H
        chars.append(0x101E7)  #glyph02918	PHAISTOS DISC SIGN BEEHIVE
        chars.append(0x1F18D)  #glyph04912	NEGATIVE SQUARED SA
        chars.append(0x1F103)  #glyph04784	DIGIT TWO COMMA
        chars.append(0x1F07D)  #glyph04699	DOMINO TILE VERTICAL-03-05
        chars.append(0x1F18E)  #glyph04913	????
        chars.append(0x1F07E)  #glyph04700	DOMINO TILE VERTICAL-03-06
        chars.append(0x1F724)  #glyph05045	????
        chars.append(0x1F18F)  #glyph04914	????
        chars.append(0x1F07F)  #glyph04701	DOMINO TILE VERTICAL-04-00
        chars.append(0x1F190)  #glyph04915	SQUARE DJ
        chars.append(0x101D0)  #glyph02895	PHAISTOS DISC SIGN PEDESTRIAN
        chars.append(0x10100)  #glyph02751	AEGEAN WORD SEPARATOR LINE
        chars.append(0x1F080)  #glyph04702	DOMINO TILE VERTICAL-04-01
        chars.append(0x1F191)  #glyph04916	????
        chars.append(0x101D1)  #glyph02896	PHAISTOS DISC SIGN PLUMED HEAD
        chars.append(0x1F081)  #glyph04703	DOMINO TILE VERTICAL-04-02
        chars.append(0x1F192)  #glyph04917	????
        chars.append(0x101D2)  #glyph02897	PHAISTOS DISC SIGN TATTOOED HEAD
        chars.append(0x1010D)  #glyph02760	AEGEAN NUMBER SEVEN
        chars.append(0x1F082)  #glyph04704	DOMINO TILE VERTICAL-04-03
        chars.append(0x1F193)  #glyph04918	????
        chars.append(0x101D3)  #glyph02898	PHAISTOS DISC SIGN CAPTIVE
        chars.append(0x1F083)  #glyph04705	DOMINO TILE VERTICAL-04-04
        chars.append(0x1F725)  #glyph05046	????
        chars.append(0x1F194)  #glyph04919	????
        chars.append(0x101D4)  #glyph02899	PHAISTOS DISC SIGN CHILD
        chars.append(0x1F045)  #glyph04643	DOMINO TILE HORIZONTAL-02-06
        chars.append(0xFEFF)  #uniFEFF	ZERO WIDTH NO-BREAK SPACE
        chars.append(0x1F084)  #glyph04706	DOMINO TILE VERTICAL-04-05
        chars.append(0x1F195)  #glyph04920	????
        chars.append(0x101D5)  #glyph02900	PHAISTOS DISC SIGN WOMAN
        chars.append(0x1D6F2)  #glyph04310	MATHEMATICAL ITALIC CAPITAL RHO
        chars.append(0x10101)  #glyph02752	AEGEAN WORD SEPARATOR DOT
        chars.append(0x1F085)  #glyph04707	DOMINO TILE VERTICAL-04-06
        chars.append(0x1D72E)  #glyph04370	MATHEMATICAL BOLD ITALIC CAPITAL SIGMA
        chars.append(0x1F196)  #glyph04921	????
        chars.append(0x101D6)  #glyph02901	PHAISTOS DISC SIGN HELMET
        chars.append(0x1F03F)  #glyph04637	DOMINO TILE HORIZONTAL-02-00
        chars.append(0x1F729)  #glyph05050	????
        chars.append(0x1F086)  #glyph04708	DOMINO TILE VERTICAL-05-00
        chars.append(0x1F0DF)  #glyph04780	????
        chars.append(0x1F197)  #glyph04922	????
        chars.append(0x101D7)  #glyph02902	PHAISTOS DISC SIGN GAUNTLET
        chars.append(0x1F0C1)  #glyph04751	????
        chars.append(0x1F13A)  #glyph04833	????
        chars.append(0x1F087)  #glyph04709	DOMINO TILE VERTICAL-05-01
        chars.append(0x1F198)  #glyph04923	????
        chars.append(0x101D8)  #glyph02903	PHAISTOS DISC SIGN TIARA
        chars.append(0x1F088)  #glyph04710	DOMINO TILE VERTICAL-05-02
        chars.append(0x1F726)  #glyph05047	????
        chars.append(0x1F199)  #glyph04924	????
        chars.append(0x101D9)  #glyph02904	PHAISTOS DISC SIGN ARROW
        chars.append(0x1F0DE)  #glyph04779	????
        chars.append(0x1F089)  #glyph04711	DOMINO TILE VERTICAL-05-03
        chars.append(0x1F19A)  #glyph04925	????
        chars.append(0x101DA)  #glyph02905	PHAISTOS DISC SIGN BOW
        chars.append(0x1F01E)  #glyph04608	MAHJONG TILE SIX OF CIRCLES
        chars.append(0x10102)  #glyph02753	AEGEAN CHECK MARK
        chars.append(0x1F08A)  #glyph04712	DOMINO TILE VERTICAL-05-04
        chars.append(0x1F0CD)  #glyph04763	????
        chars.append(0x101DB)  #glyph02906	PHAISTOS DISC SIGN SHIELD
        chars.append(0x1F021)  #glyph04611	MAHJONG TILE NINE OF CIRCLES
        chars.append(0x1F08B)  #glyph04713	DOMINO TILE VERTICAL-05-05
        chars.append(0x1F711)  #glyph05026	????
        chars.append(0x101DC)  #glyph02907	PHAISTOS DISC SIGN CLUB
        chars.append(0x1F120)  #glyph04808	PARENTHESIZED LATIN CAPITAL LETTER Q
        chars.append(0x1F0C2)  #glyph04752	????
        chars.append(0x1D6F9)  #glyph04317	MATHEMATICAL ITALIC CAPITAL PSI
        chars.append(0x1F08C)  #glyph04714	DOMINO TILE VERTICAL-05-06
        chars.append(0xFFF9)  #uniFFF9	INTERLINEAR ANNOTATION ANCHOR
        chars.append(0xFFFA)  #uniFFFA	INTERLINEAR ANNOTATION SEPARATOR
        chars.append(0xFFFB)  #uniFFFB	INTERLINEAR ANNOTATION TERMINATOR
        chars.append(0xFFFC)  #uniFFFC	OBJECT REPLACEMENT CHARACTER
        chars.append(0xFFFD)  #uniFFFD	REPLACEMENT CHARACTER
        return chars


