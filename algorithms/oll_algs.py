"""
Algorithms for 1 Look OLL used from http://badmephisto.com/oll.php.
Names from https://www.speedsolving.com/wiki/index.php/OLL.
"""
from algorithms.tools import alg_to_code

'''
(R U R' U') Triggers
'''
case_01 = alg_to_code("FRUR'U'F'")              # Suitup
case_02 = alg_to_code("FRUR'U'RUR'U'F'")        # Breakneck
case_03 = alg_to_code("yR'U'RU'R'URU'R'U2R")    # Flip
case_04 = alg_to_code("fRUR'U'f'")              # P
case_05 = alg_to_code("fRUR'U'RUR'U'f'")        # Ant
case_06 = alg_to_code("fL'U'LUf'")              # AntiP
case_07 = alg_to_code("F'L'U'LUL'U'LUF")        # Antibreakneck
case_08 = alg_to_code("FRUR'U'F'UFRUR'U'F'")    # Upstairs
case_09 = alg_to_code("yrUR'UR'FRF'RU2r'")      # Downstairs
case_10 = alg_to_code("fRUR'U'f'UFRUR'U'F'")    # Mouse
case_11 = alg_to_code("fRUR'U'f'U'FRUR'U'F'")   # Antimouse
case_12 = alg_to_code("FRUR'U'F'fRUR'U'f'")     # Zamboni
case_13 = alg_to_code("RU2R2U'R2U'R2U2R")       # Tshirt
case_14 = alg_to_code("rUr'RUR'U'rU'r'")        # Antisqueegee
case_15 = alg_to_code("l'U'lL'U'LUl'Ul")        # Squeegee
case_16 = alg_to_code("R'FRUR'U'F'UR")          # Antifung
case_17 = alg_to_code("RUR'U'M'URU'r'")         # Brick
case_18 = alg_to_code("MURUR'U'M2URU'r'")       # Checkers
case_19 = alg_to_code("FRUR'U'RF'rUR'U'r'")     # Streetlights

'''
(R' F R F') Triggers
'''
case_20 = alg_to_code("RUR'U'R'FRF'")           # Key
case_21 = alg_to_code("rUR'U'r'FRF'")           # Chameleon
case_22 = alg_to_code("F'rUR'U'r'FR")           # Diagonal
case_23 = alg_to_code("R'U'R'FRF'UR")           # Seein' Headlights
case_24 = alg_to_code("RU2R2FRF'U2R'FRF'")      # Blank
case_25 = alg_to_code("RU2R2FRF'RU2R'")         # Fishsalad
case_26 = alg_to_code("MURUR'U'M'R'FRF'")       # Bunny
case_27 = alg_to_code("R'FR'F'R2U2yR'FRF'")     # Rightback Squeezy

'''
(R U R' U) Triggers
'''
case_28 = alg_to_code("RUR'URU'R'U'R'FRF'")     # Moustache
case_29 = alg_to_code("L'U'LU'L'ULULF'L'F")     # Antimoustache
case_30 = alg_to_code("RUR'URd'RU'R'F'")        # Ricecooker
case_31 = alg_to_code("RUR'UR'FRF'U2R'FRF'")    # Slash
case_32 = alg_to_code("FRUR'UF'y'U2R'FRF'")     # Crown
case_33 = alg_to_code("r'U2RUR'Ur")             # Lefty Square
case_34 = alg_to_code("rUR'URU2r'")             # Lightning

'''
Sune-like algorithms
'''
case_35 = alg_to_code("RUR'URU2R'")             # Sune
case_36 = alg_to_code("RU2R'U'RU'R'")           # Antisune
case_37 = alg_to_code("R'FRF'R'FRF'RUR'U'RUR'") # Antidalmation
case_38 = alg_to_code("RUR'URU2R'FRUR'U'F'")    # Dalmation

'''
Misc and Awkward algorithms
'''
case_39 = alg_to_code("rUR'URU'R'URU2r'")       # Antifryingpan
case_40 = alg_to_code("l'U'LU'L'ULU'L'U2l")     # Fryingpan
case_41 = alg_to_code("rU2R'U'RU'r'")           # Righty Square
case_42 = alg_to_code("FRU'R'U'RUR'F'")         # Mounted Fish
case_43 = alg_to_code("r'U'RU'R'U2r")           # Antilightning
case_44 = alg_to_code("M'UMU2M'UM")             # Stealth
case_45 = alg_to_code("RUR2U'R'FRURU'F'")       # City
case_46 = alg_to_code("FURU'R2F'RURU'R'")       # Gun
case_47 = alg_to_code("R'FRUR'F'Ry'RU'R'")      # Antigun
case_48 = alg_to_code("R2DR'U2RD'R'U2R'")       # Headlights
case_49 = alg_to_code("R'U2R2UR'URU2x'U'R'U")   # Highway
case_50 = alg_to_code("RdL'd'R'URBR'")          # Anticouch
case_51 = alg_to_code("R'U'FURU'R'F'R")         # Couch
case_52 = alg_to_code("RB'R'U'RUBU'R'")         # Fung
case_53 = alg_to_code("R'FR2B'R2F'R2BR'")       # Rightfront Squeezy
case_54 = alg_to_code("RUR'U'RU'R'F'U'FRUR'")   # Spotted Chameleon
case_55 = alg_to_code("R2UR'B'RU'R2URBR'")      # Antispotted Chameleon
case_56 = alg_to_code("RUR'U'R'FR2UR'U'F'")     # Kite
case_57 = alg_to_code("RUR'yR'FRU'R'F'R")       # Antikite

'''
SOLVED
'''
SOLVED = ''