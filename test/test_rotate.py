"""
Tests the rotation moves for the cube in three sets:
        1) x y z (Single turns)
        2) x' y' z' (Reverse turns)
        3) x2 y2 z2 (Double turns)
"""
import numpy as np

from cfop.cube import Cube
import cfop.algorithms.tools as tl

INITIAL_PERM = ['gobowrowb', 'ogbgoygwg', 'yrobgywww',
                'wgrorrbby', 'ywwybygbo', 'rgrbyryor']


def test_cw():
    """
    Test clockwise rotations
    """
    correct_perm = np.array(['ybroygrrr', 'obgybywwy', 'ybbrrorgw',
                             'wwwygbory', 'gwgyogbgo', 'brbowwgoo'])

    cube = Cube(INITIAL_PERM)
    cube.apply_alg("xyz", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
            "Failed with this set of rotations: xyz\n\n" + \
            "Got this permutation:\n{}".format(tl.dict_to_list(cube.perm)) + \
            "\n\nInstead of this permutation:\n{}".format(correct_perm)


def test_ccw():
    """
    Test counterclockwise rotations
    """
    correct_perm = np.array(['brbowwgoo', 'ywwybygbo', 'ogbgoygwg',
                             'yrobgywww', 'wgrorrbby', 'ybroygrrr'])

    cube = Cube(INITIAL_PERM)
    cube.apply_alg("x'y'z'", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
            "Failed with this set of rotations: x'y'z'\n\n" + \
            "Got this permutation:\n{}".format(tl.dict_to_list(cube.perm)) + \
            "\n\nInstead of this permutation:\n{}".format(correct_perm)


def test_dt():
    """
    Test double turn rotations
    """
    correct_perm = np.array(INITIAL_PERM)

    cube = Cube(INITIAL_PERM)
    cube.apply_alg("x2y2z2", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
            "Failed with this set of rotations: x2y2z2\n\n" + \
            "Got this permutation:\n{}".format(tl.dict_to_list(cube.perm)) + \
            "\n\nInstead of this permutation:\n{}".format(correct_perm)
