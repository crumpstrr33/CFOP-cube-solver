"""
Tests the parsing of https://www.speedsolving.com/wiki/index.php/OLL
"""
import cfop.algorithms.oll_algs as oll

ALGS = oll.get_algs()
ALGS_COUNT = [5, 7, 5, 5, 4, 2, 4, 4, 6, 5, 4, 4, 6, 7, 3, 3, 6, 9, 7, 19, 10, +
              12, 17, 17, 29, 8, 8, 28, 10, 18, 9, 12, 4, 10, 7, 7, 11, 3, 7, +
              3, 10, 10, 7, 4, 4, 5, 3, 4, 7, 11, 3, 7, 6, 7, 15, 7, 24]

def test_len():
    """
    Test for right number of cases.
    """
    assert len(ALGS) == 57, \
        'The dictionary returned for the OLL algorithms should have 57' + \
        ' cases but instead has {} cases.'.format(len(ALGS))


def test_algs_per_OLL():
    """
    Test for right number of algorithms per case.
    """
    for case in range(1, 58):
        num_found = len(ALGS['OLL {}'.format(case)])
        num_want = ALGS_COUNT[case - 1]
        assert num_found == num_want, \
            'The case OLL {} should have {}'.format(case, num_want) + \
            ' algs, but we found {} algs.'.format(num_found)
