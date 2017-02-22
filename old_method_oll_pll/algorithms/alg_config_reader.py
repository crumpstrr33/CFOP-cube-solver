from algorithms.alg_config import oll_algs, pll_algs
from algorithms.tools import alg_to_code

pll_code = {}
for name, alg in pll_algs.items():
    pll_code[name] = alg_to_code(alg)


oll_code = {}
for name, alg in oll_algs.items():
    oll_code[name] = alg_to_code(alg)