"""
Tests each possible turn for the cube in 7 sets of clockwise, counterclockwise
and double turns for single and double layer turns.
"""
import numpy as np

from cfop.cube import Cube
import cfop.algorithms.tools as tl


def test_cwsl():
    """
    Test clockwise single layer turns
    """
    correct_perm = np.array(['obrobroby', 'wwwbogbyy', 'brrwwroob',
                             'gwwgrbyyb', 'gogwyyryy', 'ggrggroow'])

    cube = Cube()
    cube.apply_alg("UFDBLRM", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
        "Failed with this set of turns: UFDBLRM\n\n" + \
        "Got this permutation:\n{}\n\n".format(tl.dict_to_list(cube.perm)) + \
        "Instead of this permutation:\n{}".format(correct_perm)


def test_cwdl():
    """
    Test clockwise double layer turns
    """
    correct_perm = np.array(['orroryogy', 'wwwoggboy', 'brrwyboyb',
                             'ggwybbybb', 'gwgrwyrby', 'grrgowoow'])

    cube = Cube()
    cube.apply_alg("ufdblr", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
        "Failed with this set of turns: ufdblr\n\n" + \
        "Got this permutation:\n{}\n\n".format(tl.dict_to_list(cube.perm)) + \
        "Instead of this permutation:\n{}".format(correct_perm)


def test_ccwsl():
    """
    Test counterclockwise single layer turns
    """
    correct_perm = np.array(['ogrogryrr', 'wwgbogbyy', 'oyboywbrr',
                             'wwwgrbyyb', 'grgywwyoo', 'obgobgwbr'])

    cube = Cube()
    cube.apply_alg("U'F'D'B'L'R'M'", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
        "Failed with this set of turns: U'F'D'B'L'R'M'\n\n" + \
        "Got this permutation:\n{}\n\n".format(tl.dict_to_list(cube.perm)) + \
        "Instead of this permutation:\n{}".format(correct_perm)


def test_ccwdl():
    """
    Test counterclockwise double layer turns
    """
    correct_perm = np.array(['ooryorygr', 'wggbbybby', 'oobbywbyr',
                             'wwwggryrb', 'gwgywoybo', 'oogwrgwrr'])

    cube = Cube()
    cube.apply_alg("u'f'd'b'l'r'", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
        "Failed with this set of turns: u'f'd'b'l'r'\n\n" + \
        "Got this permutation:\n{}\n\n".format(tl.dict_to_list(cube.perm)) + \
        "Instead of this permutation:\n{}".format(correct_perm)

def test_dtsl():
    """
    Test double turn single layer turns
    """
    correct_perm = np.array(['yyyyyywww', 'rrororrro', 'gggbbbbbb',
                             'rooororoo', 'bbbgggggg', 'wwwwwwyyy'])

    cube = Cube()
    cube.apply_alg("U2F2D2B2L2R2M2", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
        "Failed with this set of turns: U2F2D2B2L2R2M2\n\n" + \
        "Got this permutation:\n{}\n\n".format(tl.dict_to_list(cube.perm)) + \
        "Instead of this permutation:\n{}".format(correct_perm)

def test_dtdl():
    """
    Test double turn double layer turns
    """
    correct_perm = np.array(['ywyywywyw', 'roooooroo', 'gggbgbbbb',
                             'rrorrrrro', 'bbbgbgggg', 'wywwywywy'])

    cube = Cube()
    cube.apply_alg("u2f2d2b2l2r2", True)

    assert all(tl.dict_to_list(cube.perm) == correct_perm), \
        "Failed with this set of turns: u2f2d2b2l2r2\n\n" + \
        "Got this permutation:\n{}\n\n".format(tl.dict_to_list(cube.perm)) + \
        "Instead of this permutation:\n{}".format(correct_perm)
