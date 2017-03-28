import numpy as np
from datetime import datetime as dt

from solver import Solver
import algorithms.tools as t

SUCCESS_DIST = 40


def test_turns():
    print('Checking every turning move:')
    print('----------------------------')

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

        comment = 'Checking {}'.format(turn_comments[i])
        print(comment, end='', flush=True)
        assert all(t.dict_to_list(cube.perm) == correct_perms[i]), \
            'Failed with this set of turns: ' + \
            '{}\n\n'.format(turn_sets[i]) + \
            'Got this permutation:\n' + \
            '{}\n\n'.format(t.dict_to_list(cube.perm)) + \
            'Instead of this permutation:\n' + \
            '{}'.format(correct_perms[i])

        print(' ' * (SUCCESS_DIST - len(comment)), 'SUCCESS', flush=True)
    print('')


def test_rotate():
    print('Checking every rotation move:')
    print('-----------------------------')

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

        comment = 'Checking {}'.format(turn_comments[i], flush=True)
        print(comment, end='')
        assert all(t.dict_to_list(cube.perm) == correct_perms[i]), \
            'Failed with this set of rotations: {}\n\n'.format(rotate) + \
            'Got this permutation:\n{}'.format(t.dict_to_list(cube.perm)) + \
            '\n\nInstead of this permutation:\n{}'.format(correct_perms[i])

        print(' ' * (SUCCESS_DIST - len(comment)), 'SUCCESS', flush=True)
    print('')


def test_translate():
    print('Checking the translation methods:')
    print('---------------------------------')

    alg = "U L F R B D u l f r b d U' L' F' R' B' D' " + \
          "u' l' f' r' b' d' U2 L2 F2 R2 B2 D2 u2 l2 f2 r2 b2 d2 " + \
          "x y z x' y' z' x2 y2 z2"
    alg = alg.split(' ')
    code = list("ULFRBDulfrbdTKEQACtkeqac!@#$%^123456xyzXYZ890")

    comment = 'Checking alg_to_code... '
    print(comment, end='', flush=True)
    for n, turn in enumerate(alg):
        assert t.alg_to_code(turn) == code[n], \
               '{} translated into {},'.format(turn, t.alg_to_code(turn)) + \
               ' not {} as it should.'.format(code[n])

    print(' ' * (SUCCESS_DIST - len(comment)), 'SUCCESS', flush=True)

    comment = 'Checking code_to_alg... '
    print(comment, end='', flush=True)
    for n, turn in enumerate(code):
        assert t.code_to_alg(turn) == alg[n], \
               '{} translated into {},'.format(turn, t.code_to_alg(turn)) + \
               ' not {} as it should.'.format(alg[n])

    print(' ' * (SUCCESS_DIST - len(comment)), 'SUCCESS', flush=True)
    print('')


def test_cross():
    print('Checking the cross finding algorithm:')
    print('-------------------------------------')

    turn_space = list('UT!LK@FE#RQ$BA%DC^xyz')

    for rand in range(10):
        cube = Solver()
        cube.apply_alg(''.join(np.random.choice(turn_space, 30)))

        start_perm = t.dict_to_list(cube.perm)

        cube.solve_cross()
        cube.find_step()

        final_perm = t.dict_to_list(cube.perm)
        comment = 'Checking random algorithm number {:>2}...'.format(rand + 1)
        print(comment, end='', flush=True)
        assert cube.step == 'f2l', \
            'The perm:\n{}\n\nwas solved to:'.format(start_perm) + \
            '\n{}\n\nand failed to create a cross.'.format(final_perm) + \
            ' Or the find_step Solver method could be wrong.'

        print(' ' * (SUCCESS_DIST - len(comment)), 'SUCCESS')


def test_f2l():
    pass


def test_oll():
    pass


def test_pll():
    pass


def main():
    test_turns()
    test_rotate()
    test_translate()
    test_cross()
    test_f2l()
    test_oll()
    test_pll()


if __name__ == "__main__":
    t0 = dt.now()
    main()
    t1 = dt.now()

    print('\nThe checks took {:.3f} seconds.'.format(
            (t1 - t0).total_seconds()))
