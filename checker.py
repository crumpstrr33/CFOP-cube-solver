import numpy as np
from solver import Solver
from algorithms.tools import alg_to_code, code_to_alg

def test_turns():
    turn_sets = ["UFDBLRM", "ufdblr", "U'F'D'B'L'R'M'", 
                 "u'f'd'b'l'r'", "U2F2D2B2L2R2M2", "u2f2d2b2l2r2"]

    correct_perms = [np.array(['obrryboo', 'wwwgyybb', 'brrrboow', 'gwwbbyyg', 'gogyyyrw', 'ggrrwoog']),
                     np.array(['orryygoo', 'wwwgyobo', 'brrbbyow', 'ggwbbbyy', 'gwgyybrr', 'grrwwoog']),
                     np.array(['ogrrrryo', 'wwggyybb', 'oybwrrbo', 'wwwbbyyg', 'grgwooyy', 'obggrbwo']),
                     np.array(['oorrrgyy', 'wggyybbb', 'oobwrybb', 'wwwrbryg', 'gwgoobyy', 'ooggrrww']),
                     np.array(['yyyywwwy', 'rrororrr', 'gggbbbbb', 'roooooro', 'bbbggggg', 'wwwwyyyw']),
                     np.array(['ywyywywy', 'roooooro', 'gggbbbbb', 'rrororrr', 'bbbggggg', 'wywwywyw'])]

    turn_comments = ['regular cw turns...', 'double layer cw turns...',
                     'regular ccw turns...', 'double layer ccw turns...',
                     'regular double turns...', 'double layer double turns...']

    for i in range(6):
        cube = Solver()
        cube.apply_alg(turn_sets[i], True)
        assert all(cube.perm == correct_perms[i])
        print('Checking', turn_comments[i], 'SUCCESS')


def test_rotate():
    initial_perm= ['rrryryyb', 'wogworwy', 'obgyobbb', 'ygywwwyr', 'bwboooro', 'wrbggggg']

    rotation_sets = ["xyz", "x'y'z'", "x2y2z2"]

    correct_perms = [np.array(['ggwrbggg', 'oorobwbo', 'wwyrygyw', 'obbbobgy', 'orwywogw', 'ryryybrr']),
                     np.array(['ryryybrr', 'bwboooro', 'wogworwy', 'obgyobbb', 'ygywwwyr', 'ggwrbggg']),
                     np.array(initial_perm)]

    turn_comments = ['cw rotations...', 'ccw rotations...', 'double rotations...']

    for i in range(3):
        cube = Solver(initial_perm)
        cube.apply_alg(rotation_sets[i], True)
        assert all(cube.perm == correct_perms[i])
        print('Checking', turn_comments[i], 'SUCCESS')


def test_translate():
    alg = "ULFRBDulfrbdU'L'F'R'B'D'u'l'f'r'b'd'U2L2F2R2B2D2u2l2f2r2b2d2"
    code = "ULFRBDulfrbdTKEQACtkeqac!@#$%^123456"

    assert alg_to_code(alg) == code
    print('Checking alg_to_code... SUCCESS')

    assert code_to_alg(code) == alg
    print('Checking code_to_alg... SUCCESS')


def main():
    test_turns()
    test_rotate()
    test_translate()