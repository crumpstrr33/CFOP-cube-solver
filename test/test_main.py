"""
Unit tests for the sake of sanity
"""
from datetime import datetime as dt
import sys

import context
from test_solve import test_solve
from test_rotate import test_rotate
from test_translate import test_translate
from test_turn import test_turn


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
    test_solve(2, silent=silent)
    if silent:
        print('')


if __name__ == "__main__":
    t0 = dt.now()
    main(False)
    t1 = dt.now()

    print('The checks took {:.3f} ms.'.format(
        (t1 - t0).total_seconds() * 1000))

    sys.path.remove(context.CUBE_DIR)
