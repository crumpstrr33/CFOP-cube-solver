"""
Algorithms used from http://badmephisto.com/oll.php.
Names from https://www.speedsolving.com/wiki/index.php/OLL.
"""
from tools import alg_to_code

'''
No edges flipped correctly (dot)
'''
blank     = alg_to_code("RU2R2FRF'U2R'FRF'")    # Case 24
zamboni   = alg_to_code("FRUR'U'F'fRUR'U'f'")   # Case 12
antimouse = alg_to_code("fRUR'U'f'U'FRUR'U'F'") # Case 11
mouse     = alg_to_code("fRUR'U'f'UFRUR'U'F'")  # Case 10
slash     = alg_to_code("RUR'UR'FRF'U2R'FRF'")  # Case 31
crown     = alg_to_code("FRUR'UF'y'U2R'FRF'")   # Case 32
bunny     = alg_to_code("MURUR'U'M'R'FRF'")     # Case 26

'''
All edges flipped correctly (cross)
'''
sune       = alg_to_code("RUR'URU2R'")          # Case 35
antisune   = alg_to_code("RU2R'U'RU'R'")        # Case 36
flip       = alg_to_code("yR'U'RU'R'URU'R'U2R") # Case  3
tshirt     = alg_to_code("RU2R2U'R2U'R2U2R")    # Case 13
headlights = alg_to_code("R2DR'U2RD'R'U2R'")    # Case 48
chameleon  = alg_to_code("rUR'U'r'FRF'")        # Case 21
diagonal   = alg_to_code("F'rUR'U'r'FR")        # Case 22

'''
P shapes
'''
couch     = alg_to_code("R'U'FURU'R'F'R") # Case 51
anticouch = alg_to_code("RdL'd'R'URBR'")  # Case 50
pee       = alg_to_code("fRUR'U'f'")      # Case  4
antipee   = alg_to_code("fL'U'LUf'")      # Case  6

'''
W shapes
'''
moustache     = alg_to_code("RUR'URU'R'U'R'FRF'") # Case 28
antimoustache = alg_to_code("L'U'LU'L'ULULF'L'F") # Case 29

'''
L Shapes
'''
breakneck     = alg_to_code("FRUR'U'RUR'U'F'")    # Case  2
antibreakneck = alg_to_code("F'L'U'LUL'U'LUF")    # Case  7
fryingpan     = alg_to_code("l'U'LU'L'ULU'L'U2l") # Case 40
antifryingpan = alg_to_code("rUR'URU'R'URU2r'")   # Case 39
rbsqueezy     = alg_to_code("R'FR'F'R2U2yR'FRF'") # Case 27
rfsqueezy     = alg_to_code("R'FR2B'R2F'R2BR'")   # Case 53

'''
C Shapes
'''
city           = alg_to_code("RUR2U'R'FRURU'F'") # Case 45
cingheadlights = alg_to_code("R'U'R'FRF'UR")     # Case 23

'''
T Shapes
'''
key    = alg_to_code("RUR'U'R'FRF'") # Case 20
suitup = alg_to_code("FRUR'U'F'")    # Case  1

'''
I Shapes
'''
highway      = alg_to_code("R'U2R2UR'URU2x'U'R'U") # Case 49
streetlights = alg_to_code("FRUR'U'RF'rUR'U'r'")   # Case 19
ant          = alg_to_code("fRUR'U'RUR'U'f'")      # Case  5
ricecooker   = alg_to_code("RUR'URd'RU'R'F'")      # Case 30

'''
Square shapes
'''
leftysquare  = alg_to_code("r'U2RUR'Ur")   # Case 33
rightysquare = alg_to_code("rU2R'U'RU'r'") # Case 41

'''
Big lightning bolt shapes
'''
fung     = alg_to_code("RB'R'U'RUBU'R'") # Case 52
antifung = alg_to_code("R'FRUR'U'F'UR")  # Case 16

'''
Small lightning bolt shapes
'''
lightning     = alg_to_code("rUR'URU2r'")          # Case 34
antilightning = alg_to_code("r'U'RU'R'U2r")        # Case 43
downstairs    = alg_to_code("yrUR'UR'FRF'RU2r'")   # Case  9
upstairs      = alg_to_code("FRUR'U'F'UFRUR'U'F'") # Case  8

'''
Fish Shapes
'''
kite        = alg_to_code("RUR'U'R'FR2UR'U'F'") # Case 56
antikite    = alg_to_code("RUR'yR'FRU'R'F'R")   # Case 57
fishsalad   = alg_to_code("RU2R2FRF'RU2R'")     # Case 25
mountedfish = alg_to_code("FRU'R'U'RUR'F'")     # Case 42

'''
Knight move shapes
'''
gun          = alg_to_code("FURU'R2F'RURU'R'")  # Case 46
antigun      = alg_to_code("R'FRUR'F'Ry'RU'R'") # Case 47
squeegee     = alg_to_code("l'U'lL'U'LUl'Ul")   # Case 15
antisqueegee = alg_to_code("rUr'RUR'U'rU'r'")   # Case 14

'''
Awkward shapes
'''
spottedchameleon     = alg_to_code("RUR'U'RU'R'F'U'FRUR'")   # Case 39
antispottedchameleon = alg_to_code("R2UR'B'RU'R2URBR'")      # Case 55
dalmation            = alg_to_code("RUR'URU2R'FRUR'U'F'")    # Case 38
antidalmation        = alg_to_code("R'FRF'R'FRF'RUR'U'RUR'") # Case 37

'''
All corners oriented
'''
stealth  = alg_to_code("M'UMU2M'UM")       # Case 44
brick    = alg_to_code("RUR'U'M'URU'r'")   # Case 17
checkers = alg_to_code("MURUR'U'M2URU'r'") # Case 18