"""
Tests the cross solving class.
"""
import pytest

from cfop.solver import Solver
import cfop.algorithms.tools as tl


@pytest.mark.parametrize('num_repeat', range(10))
def test_cross(num_repeat):
    """
    Given a scrambled cube, it will test the cross solving from cross.py.
    """
    scramble = tl.random_scramble(20)
    cube = Solver()
    cube.apply_alg(scramble)

    start_perm = tl.dict_to_list(cube.perm)
    cube.solve_cross()
    cube.find_step()
    final_perm = tl.dict_to_list(cube.perm)

    assert cube.step == 'f2l', \
        'The test failed on solve number {}.'.format(num_repeat) + \
        ' The perm \n{}\n\n was solved to:'.format(start_perm) + \
        '\n{}\n\nand failed to create a cross.'.format(final_perm) + \
        ' Or Solver.find_step could be wrong...'
