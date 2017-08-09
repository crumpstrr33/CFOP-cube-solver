"""
Tests each step in the solving process.
"""
# PEP8 be damned, I must have this order to add to the path
from datetime import datetime as dt
from os import getcwd
from sys import path
CUBE_DIR = '\\'.join(getcwd().split('\\')[:-1])
if CUBE_DIR not in path:
    path.insert(1, CUBE_DIR)

from solver import Solver
import algorithms.tools as tl


def test_cross(scramble):
    start_perm = tl.dict_to_list(scramble.perm)
    scramble.solve_cross()
    scramble.find_step()
    final_perm = tl.dict_to_list(scramble.perm)

    assert scramble.step == 'f2l', \
        'The perm:\n{}\n\nwas solved to:'.format(start_perm) + \
        '\n{}\n\nand failed to create a cross.'.format(final_perm) + \
        ' Or the find_step Solver method could be wrong.'


def test_f2l(cross):
    return
    start_perm = tl.dict_to_list(cross.perm)
    cross.solve_f2l()
    cross.find_step()
    final_perm = tl.dict_to_list(cross.perm)

    assert cross.step == 'oll', \
        'The perm:\n{}\nwas solved to:'.format(start_perm) + \
        '\n{}\n\nand failed to solve F2L.'.format(final_perm) + \
        ' Or the find_step Solver method could be wrong.'


def test_oll(f2l):
    return


def test_pll(oll):
    return


def test_solve(solves=10, success_dist=40, silent=False):
    """
    Check with 'solves' random permutations that the cross algorithm
    successfully solves the cube (and also the step finding Solver method)

    Parameters:
    solves (default 10) Number of random scrambles to solve
    success_dist - (default 40) Number of spaces SUCCESS is indented for a
                   successful test
    silent - (default False) If True, onyl a SUCCESS statement will be printed
             out for the entire group intead of for each part.
    """
    title = 'Checking the solving algorithms'
    if not silent:
        print(title + ':')
        print('-' * (len(title) + 1))
    else:
        print(title + '...', end='')

    for rand in range(1, solves + 1):
        cube = Solver()
        cube.apply_alg(tl.random_scramble(20))

        if not silent:
            comment = 'Checking random algorithm number {:>2}...'.format(rand)
            print(comment, end='', flush=True)

        test_cross(cube)
        test_f2l(cube)
        test_oll(cube)
        test_pll(cube)

        if not silent:
            print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)

    if silent:
        print(' ' * (success_dist - len(title - 3)), 'SUCCESS', flush=True)
    else:
        print()


if __name__ == "__main__":
    t0 = dt.now()
    test_solve(1)
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    path.remove(CUBE_DIR)
