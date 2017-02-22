from solver import Solver
from algorithms.tools import code_to_alg


def oll_pll(do_print=False):
    cube = Solver(['bwgggwbb', 'rwoooooo', 'wowggggg', 'owrrrrrr', 'wrwbbbbb', 'yyyyyyyy'])
    if do_print: print('Starting perm:', cube.perm, '\n')

    cube.solve_oll()

    if do_print: print('Case', cube.oll_name[-2:])
    if do_print: print(cube.perm)
    if do_print: print(code_to_alg(cube.solving_alg))

    cube.solve_pll()

    if do_print: print('\n' + cube.pll_name)
    if do_print: print(cube.perm)

    if do_print: print('\nTotal:', code_to_alg(cube.solving_alg))

if __name__ == "__main__":
    oll_pll(True)