"""
Unit tests for the sake of sanity
"""
from test_solve import test_solve
from test_rotate import test_rotate
from test_translate import test_translate
from test_turn import test_turn

from datetime import datetime as dt
from os import getcwd
from sys import path
CUBE_DIR = '\\'.join(getcwd().split('\\')[:-1])


def main(silent=True):
    """
    Runs every unit test.

    Parameters:
    silent - (default True) will not print out the result of each section of
             each unit test, only the final result of each
    """
    test_turn(silent=silent)
    test_rotate(silent=silent)
    test_translate(silent=silent)
    test_solve(silent=silent)
    if silent:
        print('')


if __name__ == "__main__":
    t0 = dt.now()
    main(False)
    t1 = dt.now()

    print('The checks took {:.3f} seconds.'.format(
        (t1 - t0).total_seconds()))

    path.remove(CUBE_DIR)
