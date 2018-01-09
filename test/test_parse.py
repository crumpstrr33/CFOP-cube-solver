"""
Tests the parsing of https://www.speedsolving.com/wiki/index.php/OLL and
https://www.speedsolving.com/wiki/index.php/PLL
"""
import cfop.algorithms.oll_algs as oll
import cfop.algorithms.pll_algs as pll

OLL_ALGS = oll.get_algs()
PLL_ALGS = pll.get_algs()
OLL_COUNT = [5, 7, 5, 5, 4, 2, 4, 4, 6, 5, 4, 4, 6, 7, 3, 3, 6, 9, 7, 19, 10,
             12, 17, 17, 29, 8, 8, 28, 10, 18, 9, 12, 4, 10, 7, 7, 11, 3, 7,
             3, 10, 10, 7, 4, 4, 5, 3, 4, 7, 11, 3, 7, 6, 7, 15, 7, 24]
PLL_COUNT = {'H': 22, 'Ua': 15, 'Ub': 17, 'Z': 29, 'Aa': 18, 'Ab': 14,
             'E': 28, 'F': 25, 'Ga': 7, 'Gb': 7, 'Gc': 11, 'Gd': 9,
             'Ja': 36, 'Jb': 36, 'Na': 25, 'Nb': 25, 'Ra': 26, 'Rb': 26,
             'T': 22, 'V': 23, 'Y': 29}


def test_oll_len():
    """
    Test for right number of cases for OLL.
    """
    assert len(OLL_ALGS) == 57, \
        'The dictionary returned for the OLL algorithms should have 57' + \
        ' cases but instead has {} cases.'.format(len(OLL_ALGS))


def test_algs_per_oll():
    """
    Test for right number of algorithms per OLL case.
    """
    for case in range(1, 58):
        num_found = len(OLL_ALGS['OLL {}'.format(case)])
        num_want = OLL_COUNT[case - 1]
        assert num_found == num_want, \
            'The case OLL {} should have {}'.format(case, num_want) + \
            ' algs, but we found {} algs.'.format(num_found)


def test_pll_len():
    """
    Test for right number of cases for PLL.
    """
    assert len(PLL_ALGS) == 21, \
        'The dictionary returned for the PLL algorithms should have 21' + \
        ' cases but instead has {} cases.'.format(len(PLL_ALGS))


def test_algs_per_pll():
    """
    Test for right number of algorithms per PLL case.
    """
    for case, count in PLL_COUNT.items():
        num_found = len(PLL_ALGS[case + ' Permutation'])
        assert num_found == count
