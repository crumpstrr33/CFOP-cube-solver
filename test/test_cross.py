from datetime import datetime as dt
from os import getcwd
from sys import path
CUBE_DIR = '\\'.join(getcwd().split('\\')[:-1])
if CUBE_DIR not in path:
    path.insert(1, CUBE_DIR)

from solver import Solver
import algorithms.tools as tl


def test_cross(solves=10, success_dist=40, silent=False):
    """
    Check with 'solves' random permutations that the cross algorithm
    successfully finds a cross (and also the step finding Solver method)

    Parameters:
    solves - (default 10) Number of random scrambles to solve the cross for
    success_dist - (default 40) Number of spaces SUCCESS is indented for a
                   successful test
    silent - (default False) If True, only a SUCCESS statement will be printed
             out for the entire group instead of for each part.
    """
    title = 'Checking the cross finding algorithm'
    if not silent:
        print(title + ':')
        print('-' * (len(title) + 1))
    else:
        print(title + '...', end='')

    for rand in range(1, solves + 1):
        cube = Solver()
        cube.apply_alg(tl.random_scramble(20))

        start_perm = tl.dict_to_list(cube.perm)

        cube.solve_cross()
        cube.find_step()

        final_perm = tl.dict_to_list(cube.perm)

        if not silent:
            comment = 'Checking random algorithm number {:>2}...'.format(rand)
            print(comment, end='', flush=True)
        assert cube.step == 'f2l', \
            'The perm:\n{}\n\nwas solved to:'.format(start_perm) + \
            '\n{}\n\nand failed to create a cross.'.format(final_perm) + \
            ' Or the find_step Solver method could be wrong.'
        if not silent:
            print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)
    if silent:
        print(' ' * (success_dist - len(title) - 3), 'SUCCESS', flush=True)
    else:
        print('')

if __name__ == "__main__":
    t0 = dt.now()
    test_cross()
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    path.remove(CUBE_DIR)