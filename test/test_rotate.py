"""
Tests the rotation moves for the cube.
"""
import numpy as np
import sys
from datetime import datetime as dt

import context
from solver import Solver
import algorithms.tools as tl


def test_rotate(success_dist=40, silent=False):
    """
    Check the 3 sets of rotations: cw, ccw, dt
    cw = clockwise, ccw = counterclockwise, dt = double turn (180 degrees)

    Parameters:
    success_dist - (default 40) Number of spaces SUCCESS is indented for a
                   successful test
    silent - (default False) If True, only a SUCCESS statement will be printed
             out for the entire group instead of for each part.
    """
    title = 'Checking every rotation move'
    if not silent:
        print(title + ':')
        print('-' * (len(title) + 1))
    else:
        print(title + '...', end='')

    # Done with following algorithm on U white and F green:
    #          F2 L2 D' B2 D F2 L2 D2 U2 B' U L' F U2 R' D' R2 B' D'
    initial_perm = ['gobowrowb', 'ogbgoygwg', 'yrobgywww',
                    'wgrorrbby', 'ywwybygbo', 'rgrbyryor']

    rotation_sets = ["xyz", "x'y'z'", "x2y2z2"]

    correct_perms = [np.array(['ybroygrrr', 'obgybywwy', 'ybbrrorgw',
                               'wwwygbory', 'gwgyogbgo', 'brbowwgoo']),
                     np.array(['brbowwgoo', 'ywwybygbo', 'ogbgoygwg',
                               'yrobgywww', 'wgrorrbby', 'ybroygrrr']),
                     np.array(initial_perm)]

    turn_comments = ['cw rotations... ',
                     'ccw rotations... ',
                     'double rotations... ']

    for i in range(3):
        cube = Solver(initial_perm)
        rotate = rotation_sets[i]
        cube.apply_alg(rotate, True)

        if not silent:
            comment = 'Checking {}'.format(turn_comments[i], flush=True)
            print(comment, end='')
        assert all(tl.dict_to_list(cube.perm) == correct_perms[i]), \
            'Failed with this set of rotations: {}\n\n'.format(rotate) + \
            'Got this permutation:\n{}'.format(tl.dict_to_list(cube.perm)) + \
            '\n\nInstead of this permutation:\n{}'.format(correct_perms[i])

        if not silent:
            print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)
    if silent:
        print(' ' * (success_dist - len(title) - 3), 'SUCCESS', flush=True)
    else:
        print('')


if __name__ == "__main__":
    t0 = dt.now()
    test_rotate()
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    sys.path.remove(context.CUBE_DIR)
