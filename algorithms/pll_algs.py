"""
Algorithms for 1 Look PLL used from http://badmephisto.com/pll.php
"""
from algorithms.tools import alg_to_code

'''
1/18 chance of occuring
'''
aa_perm = alg_to_code("xR'UR'D2RU'R'D2R2x'")
ab_perm = alg_to_code("x'RU'RD2R'URD2R2x")
ua_perm = alg_to_code("R2URUR'U'R'U'R'UR'")
ub_perm = alg_to_code("RU'RURURU'R'U'R2")
ja_perm = alg_to_code("R'UL'U2RU'R'U2RLU'")
jb_perm = alg_to_code("RUR'F'RUR'U'R'FR2U'R'U'")
ra_perm = alg_to_code("LU2L'U2LF'L'U'LULFL2U")
rb_perm = alg_to_code("R'U2RU2R'FRUR'U'R'F'R2U'")
t_perm  = alg_to_code("RUR'U'R'FR2U'R'U'RUR'F'")
y_perm  = alg_to_code("FRU'R'U'RUR'F'RUR'U'R'FRF'")
v_perm  = alg_to_code("R'UR'd'R'F'R2U'R'UR'FRF")
f_perm  = alg_to_code("R'U2R'd'R'F'R2U'R'UR'FRU'F")
ga_perm = alg_to_code("R2uR'UR'U'Ru'R2y'R'UR")
gb_perm = alg_to_code("R'U'RyR2uR'URU'Ru'R2")
gc_perm = alg_to_code("R2u'RU'RUR'uR2yRU'R'")
gd_perm = alg_to_code("RUR'y'R2u'RU'R'UR'uR2")

'''
1/36 chance of occuring
'''
z_perm  = alg_to_code("M2UM2UM'U2M2U2M'U2")
e_perm  = alg_to_code("x'RU'R'DRUR'D'RUR'DRU'R'D'x")

'''
1/72 chance of occuring
'''
h_perm  = alg_to_code("M2UM2U2M2UM2")
na_perm = alg_to_code("LU'RU2L'UR'LU'RU2L'UR'U")
nb_perm = alg_to_code("R'UL'U2RU'LR'UL'U2RU'LU'")
SOLVED  = ''