'''
Reads the dicts from alg_config.py and converts the algorithms into the syntax
used by the code.
'''
from algorithms.alg_config import OLL_ALGS, PLL_ALGS
from algorithms.tools import alg_to_code


PLL_CODE = {}
for name, alg in PLL_ALGS.items():
    PLL_CODE[name] = alg_to_code(alg)


OLL_CODE = {}
for name, alg in OLL_ALGS.items():
    OLL_CODE[name] = alg_to_code(alg)
