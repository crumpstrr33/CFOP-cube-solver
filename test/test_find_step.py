from datetime import datetime as dt
from sys import path
CUBE_DIR = 'C:\\Users\\Jacob\\Documents\\coding_stuff\\Python\\CFOP_solver_3x3'
if CUBE_DIR not in path:
    path.insert(1, CUBE_DIR)

from solver import Solver

# TODO don't hard-code the testing perms somehow


def test_find_step(success_dist=40, silent=False):
    """
    Checks the find_step method of the Solver class if it can find the correct
    step on the below permutations

    Parameters:
    success_dist - (default 40) Number of spaces SUCCESS is indented for a
                   successful test
    silent - (default False) If True, only a SUCCESS statement will be printed
             out for the entire group instead of for each part, if True
    """
    title = 'Checking the Solver.find_step method'
    if not silent:
        print(title + ':')
        print('-------------------------------------')
    else:
        print(title + '...', end='')

    cross_perm = ['ygggwywwg', 'brrbgywgb', 'brrrrbygo',
                  'wooybrbog', 'ywobowroo', 'rywoywgby']
    f2l_perm = ['rwwrwwygg', 'ygoobbrbg', 'bowwogyob',
                'oobwgrygw', 'orgbrbbrw', 'oyryyygyr']
    oll_perm = ['gwgogygrg', 'rgwyyyyyy', 'ogrrrrrrr',
                'wgowwwwww', 'ygyoooooo', 'bbbbbbbbb']
    pll_perm = ['ooooooooo', 'wwywwwwww', 'gbbbbbbbb',
                'ygwyyyyyy', 'byggggggg', 'rrrrrrrrr']
    solved_perm = ['ggggggggg', 'ooooooooo', 'yyyyyyyyy',
                   'rrrrrrrrr', 'wwwwwwwww', 'bbbbbbbbb']

    perms = {'cross': cross_perm, 'F2L': f2l_perm, 'OLL': oll_perm,
             'PLL': pll_perm, 'solved': solved_perm}

    for name, perm in perms.items():
        cube = Solver(perm)
        cube.find_step()

        if not silent:
            comment = 'Checking find_step for {}...'.format(name)
            print(comment, end='', flush=True)
        assert cube.step == name.lower(), \
            "The method find_step found '{}' ".format(cube.step) + \
            "when it was supposed to find '{}'.".format(name)

        if not silent:
            print(' ' * (success_dist - len(comment)), 'SUCCESS', flush=True)
    if silent:
        print(' ' * (success_dist - len(title) - 3), 'SUCCESS', flush=True)
    else:
        print('')

if __name__ == "__main__":
    t0 = dt.now()
    test_find_step()
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    path.remove(CUBE_DIR)