"""
Algorithms for 1 Look OLL used from http://badmephisto.com/oll.php.
Names from https://www.speedsolving.com/wiki/index.php/OLL.
"""
from tools import alg_to_code

'''
No edges flipped correctly
'''
blank     = alg_to_code("RU2R2FRF'U2R'FRF'")                 # Case 24
zamboni   = alg_to_code("FRUR'U'F'fRUR'U'f'")                # Case 12
amouse    = alg_to_code("y'" + "fRUR'U'f'U'FRUR'U'F'" + "y") # Case 11
mouse     = alg_to_code("fRUR'U'f'UFRUR'U'F'")               # Case 10
slash     = alg_to_code("RUR'UR'FRF'U2R'FRF'")               # Case 31
crown     = alg_to_code("y2" + "FRUR'UF'y'U2R'FRF'" + "y2")  # Case 32
bunny     = alg_to_code("MURUR'U'M'R'FRF'")                  # Case 26

'''
All edges flipped correctly
'''
sune       = alg_to_code("RUR'URU2R'")                    # Case 35
asune      = alg_to_code("y2" + "RU2R'U'RU'R'" + "y2")    # Case 36
flip       = alg_to_code("yR'U'RU'R'URU'R'U2R")           # Case  3
tshirt     = alg_to_code("RU2R2U'R2U'R2U2R")              # Case 13
headlights = alg_to_code("y'" + "R2DR'U2RD'R'U2R'" + "y") # Case 48
chameleon  = alg_to_code("rUR'U'r'FRF'")                  # Case 21
diagonal   = alg_to_code("F'rUR'U'r'FR")                  # Case 22

'''
P shapes
'''
couch  = alg_to_code("R'U'FURU'R'F'R")          # Case 51
acouch = alg_to_code("RdL'd'R'URBR'")           # Case 50
pee    = alg_to_code("fRUR'U'f'")               # Case  4
apee   = alg_to_code("y2" + "fL'U'LUf'" + "y2") # Case  6

'''
W shapes
'''
moustache  = alg_to_code("RUR'URU'R'U'R'FRF'")              # Case 28
amoustache = alg_to_code("y" + "L'U'LU'L'ULULF'L'F" + "y'") # Case 29

'''
L Shapes
'''
breakneck     = alg_to_code("FRUR'U'RUR'U'F'")                 # Case  2
abreakneck    = alg_to_code("y'" + "F'L'U'LUL'U'LUF" + "y")    # Case  7
fryingpan     = alg_to_code("l'U'LU'L'ULU'L'U2l")              # Case 40
afryingpan    = alg_to_code("y'" + "rUR'URU'R'URU2r'" + "y")   # Case 39
rbsqueezy     = alg_to_code("y'" + "R'FR'F'R2U2yR'FRF'" + "y") # Case 27
rfsqueezy     = alg_to_code("R'FR2B'R2F'R2BR'")                # Case 53

'''
C Shapes
'''
city           = alg_to_code("RUR2U'R'FRURU'F'")          # Case 45
cingheadlights = alg_to_code("y'" + "R'U'R'FRF'UR" + "y") # Case 23

'''
T Shapes
'''
key    = alg_to_code("RUR'U'R'FRF'") # Case 20
suitup = alg_to_code("FRUR'U'F'")    # Case  1

'''
I Shapes
'''
highway      = alg_to_code("R'U2R2UR'URU2x'U'R'U")            # Case 49
streetlights = alg_to_code("y'" + "FRUR'U'RF'rUR'U'r'" + "y") # Case 19
ant          = alg_to_code("y' " + "fRUR'U'RUR'U'f'" + "y")   # Case  5
ricecooker   = alg_to_code("RUR'URd'RU'R'F'")                 # Case 30

'''
Square shapes
'''
leftysquare  = alg_to_code("r'U2RUR'Ur")                # Case 33
rightysquare = alg_to_code("y" + "rU2R'U'RU'r'" + "y'") # Case 41

'''
Big lightning bolt shapes
'''
fung  = alg_to_code("RB'R'U'RUBU'R'") # Case 52
afung = alg_to_code("R'FRUR'U'F'UR")  # Case 16

'''
Small lightning bolt shapes
'''
lightning     = alg_to_code("y2" + "rUR'URU2r'" + "y2") # Case 34
alightning    = alg_to_code("r'U'RU'R'U2r")             # Case 43
downstairs    = alg_to_code("yrUR'UR'FRF'RU2r'")        # Case  9
upstairs      = alg_to_code("FRUR'U'F'UFRUR'U'F'")      # Case  8

'''
Fish Shapes
'''
kite        = alg_to_code("RUR'U'R'FR2UR'U'F'")            # Case 56
akite       = alg_to_code("y" + "RUR'yR'FRU'R'F'R" + "y'") # Case 57
fishsalad   = alg_to_code("RU2R2FRF'RU2R'")                # Case 25
mountedfish = alg_to_code("y2" + "FRU'R'U'RUR'F'" + "y2")  # Case 42

'''
Knight move shapes
'''
gun       = alg_to_code("FURU'R2F'RURU'R'")                # Case 46
agun      = alg_to_code("y2" + "R'FRUR'F'Ry'RU'R'" + "y2") # Case 47
squeegee  = alg_to_code("l'U'lL'U'LUl'Ul")                 # Case 15
asqueegee = alg_to_code("y2" + "rUr'RUR'U'rU'r'" + "y2")   # Case 14

'''
Awkward shapes
'''
spotcham   = alg_to_code("RUR'U'RU'R'F'U'FRUR'")              # Case 54
aspotcham  = alg_to_code("R2UR'B'RU'R2URBR'")                 # Case 55
dalmation  = alg_to_code("y2" + "RUR'URU2R'FRUR'U'F'" + "y2") # Case 38
adalmation = alg_to_code("R'FRF'R'FRF'RUR'U'RUR'")            # Case 37

'''
All corners oriented
'''
stealth  = alg_to_code("M'UMU2M'UM")       # Case 44
brick    = alg_to_code("RUR'U'M'URU'r'")   # Case 17
checkers = alg_to_code("MURUR'U'M2URU'r'") # Case 18