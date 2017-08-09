from datetime import datetime as dt
from os import getcwd
from sys import path
CUBE_DIR = '\\'.join(getcwd().split('\\')[:-1])
if CUBE_DIR not in path:
    path.insert(1, CUBE_DIR)

import algorithms.tools as tl


def test_translate(success_dist=40, silent=False):
    """
    Check the translation methods from the cubing algorithm syntax into the
    code syntax and vis versa

    Parameters:
    success_dist - (default 40) Number of spaces SUCCESS is indented for a
                   successful test
    silent - (default False) If True, only a SUCCESS statement will be printed
             out for the entire group instead of for each part, if True
    """
    title = 'Checking the translation methods'
    if not silent:
        print(title + ':')
        print('---------------------------------')
    else:
        print(title + '...', end='')

    alg = "U L F R B D u l f r b d U' L' F' R' B' D' " + \
          "u' l' f' r' b' d' U2 L2 F2 R2 B2 D2 u2 l2 f2 r2 b2 d2 " + \
          "x y z x' y' z' x2 y2 z2"
    alg = alg.split(' ')
    code = list("ULFRBDulfrbdTKEQACtkeqac!@#$%^123456xyzXYZ890")

    if not silent:
        comment = 'Checking alg_to_code... '
        print(comment, end='', flush=True)
    for n, turn in enumerate(alg):
        assert tl.alg_to_code(turn) == code[n], \
               '{} translated into {},'.format(turn, tl.alg_to_code(turn)) + \
               ' not {} as it should.'.format(code[n])

    if not silent:
        print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)

        comment = 'Checking code_to_alg... '
        print(comment, end='', flush=True)
    for n, turn in enumerate(code):
        assert tl.code_to_alg(turn) == alg[n], \
               '{} translated into {},'.format(turn, tl.code_to_alg(turn)) + \
               ' not {} as it should.'.format(alg[n])

    if not silent:
        print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)
        print('')
    else:
        print(' ' * (success_dist - len(title) - 3), 'SUCCESS', flush=True)


if __name__ == "__main__":
    t0 = dt.now()
    test_translate()
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    path.remove(CUBE_DIR)