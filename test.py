import numpy as np
from datetime import datetime as dt

from solver import Solver
import algorithms.tools as tools

def test_turns():
    print('Checking every turning move:')
    print('----------------------------')

    turn_sets = ["UFDBLRM", "ufdblr", "U'F'D'B'L'R'M'", 
                 "u'f'd'b'l'r'", "U2F2D2B2L2R2M2", "u2f2d2b2l2r2"]

    correct_perms = [np.array(['obrobroby', 'wwwbogbyy', 'brrwwroob', 'gwwgrbyyb', 'gogwyyryy', 'ggrggroow']),
                     np.array(['orroryogy', 'wwwoggboy', 'brrwyboyb', 'ggwybbybb', 'gwgrwyrby', 'grrgowoow']),
                     np.array(['ogrogryrr', 'wwgbogbyy', 'oyboywbrr', 'wwwgrbyyb', 'grgywwyoo', 'obgobgwbr']),
                     np.array(['ooryorygr', 'wggbbybby', 'oobbywbyr', 'wwwggryrb', 'gwgywoybo', 'oogwrgwrr']),
                     np.array(['yyyyyywww', 'rrororrro', 'gggbbbbbb', 'rooororoo', 'bbbgggggg', 'wwwwwwyyy']),
                     np.array(['ywyywywyw', 'roooooroo', 'gggbgbbbb', 'rrorrrrro', 'bbbgbgggg', 'wywwywywy'])]

    turn_comments = ['regular cw turns... ', 'double layer cw turns... ',
                     'regular ccw turns... ', 'double layer ccw turns... ',
                     'regular double turns... ', 'double layer double turns... ']

    for i in range(6):
        cube = Solver()
        cube.apply_alg(turn_sets[i], True)

        print('Checking', turn_comments[i], end='')
        assert all(tools.reverse_convert_cube(cube.perm) == correct_perms[i])
        print('SUCCESS')
    print('')


def test_rotate():
    print('Checking every rotation move:')
    print('-----------------------------')

    ## Done with follow algorithm on U white and F green:
    ##          F2 L2 D' B2 D F2 L2 D2 U2 B' U L' F U2 R' D' R2 B' D'
    initial_perm= ['gobowrowb', 'ogbgoygwg', 'yrobgywww', 'wgrorrbby', 'ywwybygbo', 'rgrbyryor']

    rotation_sets = ["xyz", "x'y'z'", "x2y2z2"]

    correct_perms = [np.array(['ybroygrrr', 'obgybywwy', 'ybbrrorgw', 'wwwygbory', 'gwgyogbgo', 'brbowwgoo']),
                     np.array(['brbowwgoo', 'ywwybygbo', 'ogbgoygwg', 'yrobgywww', 'wgrorrbby', 'ybroygrrr']),
                     np.array(initial_perm)]

    turn_comments = ['cw rotations... ', 'ccw rotations... ', 'double rotations... ']

    for i in range(3):
        cube = Solver(initial_perm)
        cube.apply_alg(rotation_sets[i], True)

        print('Checking', turn_comments[i], end='')
        assert all(tools.reverse_convert_cube(cube.perm) == correct_perms[i])
        print('SUCCESS')
    print('')


def test_translate():
    print('Checking the translation methods:')
    print('---------------------------------')

    alg = "ULFRBDulfrbdU'L'F'R'B'D'u'l'f'r'b'd'U2L2F2R2B2D2u2l2f2r2b2d2"
    code = "ULFRBDulfrbdTKEQACtkeqac!@#$%^123456"

    print('Checking alg_to_code... ', end='')
    assert tools.alg_to_code(alg) == code
    print('SUCCESS')

    print('Checking code_to_alg... ', end='')
    assert tools.code_to_alg(code) == alg
    print('SUCCESS')



def main():
    test_turns()
    test_rotate()
    test_translate()

if __name__ == "__main__":
    t0 = dt.now()
    main()
    t1 = dt.now()

    print('\nThe checks took %.3f ms.' % ((t1 - t0).total_seconds() * 1000))