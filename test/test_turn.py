import numpy as np
from datetime import datetime as dt
from os import getcwd
from sys import path
CUBE_DIR = '\\'.join(getcwd().split('\\')[:-1])
if CUBE_DIR not in path:
    path.insert(1, CUBE_DIR)

from solver import Solver
import algorithms.tools as tl


def test_turn(success_dist=40, silent=False):
    """
    Check the 6 different sets of turns: cwsl, cwdl, ccwsl, ccwdl, dtsl, dtdl
    cw = clockwise, ccw = counterclockwise, dt = double turn (180 degrees)
    sl = single layer, dl = double layer

    Parameters:
    success_dist - (default 40) Number of spaces SUCCESS is indented for a
                   successful test
    silent - (default False) If True, only a SUCCESS statement will be printed
             out for the entire group instead of for each part.
    """
    title = 'Checking every turning move'
    if not silent:
        print(title + ':')
        print('-' * (len(title) + 1))
    else:
        print(title + '...', end='')

    turn_sets = ["UFDBLRM", "ufdblr",
                 "U'F'D'B'L'R'M'", "u'f'd'b'l'r'",
                 "U2F2D2B2L2R2M2", "u2f2d2b2l2r2"]

    correct_perms = [
        np.array(['obrobroby', 'wwwbogbyy', 'brrwwroob',
                  'gwwgrbyyb', 'gogwyyryy', 'ggrggroow']),
        np.array(['orroryogy', 'wwwoggboy', 'brrwyboyb',
                  'ggwybbybb', 'gwgrwyrby', 'grrgowoow']),
        np.array(['ogrogryrr', 'wwgbogbyy', 'oyboywbrr',
                  'wwwgrbyyb', 'grgywwyoo', 'obgobgwbr']),
        np.array(['ooryorygr', 'wggbbybby', 'oobbywbyr',
                  'wwwggryrb', 'gwgywoybo', 'oogwrgwrr']),
        np.array(['yyyyyywww', 'rrororrro', 'gggbbbbbb',
                  'rooororoo', 'bbbgggggg', 'wwwwwwyyy']),
        np.array(['ywyywywyw', 'roooooroo', 'gggbgbbbb',
                  'rrorrrrro', 'bbbgbgggg', 'wywwywywy'])]

    turn_comments = ['regular cw turns... ',
                     'double layer cw turns... ',
                     'regular ccw turns... ',
                     'double layer ccw turns... ',
                     'regular double turns... ',
                     'double layer double turns... ']

    for i in range(6):
        cube = Solver()
        cube.apply_alg(turn_sets[i], True)

        if not silent:
            comment = 'Checking {}'.format(turn_comments[i])
            print(comment, end='', flush=True)
        assert all(tl.dict_to_list(cube.perm) == correct_perms[i]), \
            'Failed with this set of turns: ' + \
            '{}\n\n'.format(turn_sets[i]) + \
            'Got this permutation:\n' + \
            '{}\n\n'.format(tl.dict_to_list(cube.perm)) + \
            'Instead of this permutation:\n' + \
            '{}'.format(correct_perms[i])

        if not silent:
            print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)
    if silent:
        print(' ' * (success_dist - len(title) - 3), 'SUCCESS', flush=True)
    else:
        print('')


if __name__ == "__main__":
    t0 = dt.now()
    test_turn()
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    path.remove(CUBE_DIR)