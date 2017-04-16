'''
All 57 1-Look OLL cases (or 58 if counting the solved state) written out out
as cubing algorithms which were copied from http://badmephisto.com/oll.php.
'''
oll_algs = {
    # (R U R' U') Triggers
    'case_01': "FRUR'U'F'",
    'case_02': "FRUR'U'RUR'U'F'",
    'case_03': "yR'U'RU'R'URU'R'U2R",
    'case_04': "fRUR'U'f'",
    'case_05': "fRUR'U'RUR'U'f'",
    'case_06': "fL'U'LUf'",
    'case_07': "F'L'U'LUL'U'LUF",
    'case_08': "FRUR'U'F'UFRUR'U'F'",
    'case_09': "yrUR'UR'FRF'RU2r'",
    'case_10': "fRUR'U'f'UFRUR'U'F'",
    'case_11': "fRUR'U'f'U'FRUR'U'F'",
    'case_12': "FRUR'U'F'fRUR'U'f'",
    'case_13': "RU2R2U'R2U'R2U2R",
    'case_14': "rUr'RUR'U'rU'r'",
    'case_15': "l'U'lL'U'LUl'Ul",
    'case_16': "R'FRUR'U'F'UR",
    'case_17': "RUR'U'M'URU'r'",
    'case_18': "MURUR'U'M2URU'r'",
    'case_19': "FRUR'U'RF'rUR'U'r'",

    # (R' F R F') Triggers
    'case_20': "RUR'U'R'FRF'",
    'case_21': "rUR'U'r'FRF'",
    'case_22': "F'rUR'U'r'FR",
    'case_23': "R'U'R'FRF'UR",
    'case_24': "RU2R2FRF'U2R'FRF'",
    'case_25': "RU2R2FRF'RU2R'",
    'case_26': "MURUR'U'M'R'FRF'",
    'case_27': "R'FR'F'R2U2yR'FRF'",

    # (R U R' U) Triggers
    'case_28': "RUR'URU'R'U'R'FRF'",
    'case_29': "L'U'LU'L'ULULF'L'F",
    'case_30': "RUR'URd'RU'R'F'",
    'case_31': "RUR'UR'FRF'U2R'FRF'",
    'case_32': "FRUR'UF'y'U2R'FRF'",
    'case_33': "r'U2RUR'Ur",
    'case_34': "rUR'URU2r'",

    # Sune-like algorithms
    'case_35': "RUR'URU2R'",
    'case_36': "RU2R'U'RU'R'",
    'case_37': "R'FRF'R'FRF'RUR'U'RUR'",
    'case_38': "RUR'URU2R'FRUR'U'F'",

    # Misc and Awkward algorithms
    'case_39': "rUR'URU'R'URU2r'",
    'case_40': "l'U'LU'L'ULU'L'U2l",
    'case_41': "rU2R'U'RU'r'",
    'case_42': "FRU'R'U'RUR'F'",
    'case_43': "r'U'RU'R'U2r",
    'case_44': "M'UMU2M'UM",
    'case_45': "RUR2U'R'FRURU'F'",
    'case_46': "FURU'R2F'RURU'R'",
    'case_47': "R'FRUR'F'Ry'RU'R'",
    'case_48': "R2DR'U2RD'R'U2R'",
    'case_49': "R'U2R2UR'URU2x'U'R'Ux",
    'case_50': "RdL'd'R'URBR'",
    'case_51': "R'U'FURU'R'F'R",
    'case_52': "RB'R'U'RUBU'R'",
    'case_53': "R'FR2B'R2F'R2BR'",
    'case_54': "RUR'U'RU'R'F'U'FRUR'",
    'case_55': "R2UR'B'RU'R2URBR'",
    'case_56': "RUR'U'R'FR2UR'U'F'",
    'case_57': "RUR'yR'FRU'R'F'R",

    # SOLVED
    'SOLVED':  ""
}


'''
All 21 1-Look PLL cases (or 22 if counting the solved state) written out out
as cubing algorithms which were copied from http://badmephisto.com/pll.php.
'''
pll_algs = {
    # 1/18 chance of occuring
    'aa_perm': "xR'UR'D2RU'R'D2R2x'",
    'ab_perm': "x'RU'RD2R'URD2R2x",
    'ua_perm': "R2URUR'U'R'U'R'UR'",
    'ub_perm': "RU'RURURU'R'U'R2",
    'ja_perm': "R'UL'U2RU'R'U2RLU'",
    'jb_perm': "RUR'F'RUR'U'R'FR2U'R'U'",
    'ra_perm': "LU2L'U2LF'L'U'LULFL2U",
    'rb_perm': "R'U2RU2R'FRUR'U'R'F'R2U'",
    't_perm':  "RUR'U'R'FR2U'R'U'RUR'F'",
    'y_perm':  "FRU'R'U'RUR'F'RUR'U'R'FRF'",
    'v_perm':  "R'UR'd'R'F'R2U'R'UR'FRF",
    'f_perm':  "R'U2R'd'R'F'R2U'R'UR'FRU'F",
    'ga_perm': "R2uR'UR'U'Ru'R2y'R'UR",
    'gb_perm': "R'U'RyR2uR'URU'Ru'R2",
    'gc_perm': "R2u'RU'RUR'uR2yRU'R'",
    'gd_perm': "RUR'y'R2u'RU'R'UR'uR2",

    # 1/36 chance of occuring
    'z_perm':  "M2UM2UM'U2M2U2M'U2",
    'e_perm':  "x'RU'R'DRUR'D'RUR'DRU'R'D'x",

    # 1/72 chance of occuring
    'h_perm':  "M2UM2U2M2UM2",
    'na_perm': "LU'RU2L'UR'LU'RU2L'UR'U",
    'nb_perm': "R'UL'U2RU'LR'UL'U2RU'LU'",
    'SOLVED':  ""
}