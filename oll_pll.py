from collections import deque
import numpy as np
from algorithms.alg_dicts import oll_dict, pll_dict

class OLLCases():
    '''
    This class handles the OLL cases. A permutation is is given then the correct
    OLL is found using the unique identifiers in oll_dict. This oll (written as
    'case_xx') can be found in oll_algs.py.
    
    The unique identifier is given by the rotation of each of the 8 cubies on
    the top layer. Corners can be 0, 1 or 2 where 0 represents correct
    orientation, 1 represents one clockwise twist of the cubie and 2 represents
    2 clockwise twists. For edges, it is either 0 (for correct orientation) or
    1 if incorrect. They are ordered starting in the top left and moving
    counterclockwise. In retrospect, that's inconsistent, but it works fine and
    consistency in this context isn't necessary or useful.

    The identifier is found with _tf_hash, then the OLL algorithm is
    found. If it's not found, an exception is thrown.

    Parameters:
    perm - The permutation of a cube that is at OLL
    '''
    def __init__(self, perm):
       self.tf_stickers = self._tf_hash(perm)

       try:
           self.oll, self.rotation = self._find_oll()
       except TypeError:
           raise Exception('Could not find the matching hash for %s' % self.tf_stickers +
                           'in oll_dict computed from permutation:', list(perm))


    def _tf_hash(self, perm):
        ## The correct stickers, looking for where the top face sticker is
        tf_stickers  = str((perm[0][0] + perm[1][0] + perm[4][2]).index('w'))
        tf_stickers += str((perm[0][7] + perm[1][1]).index('w'))
        tf_stickers += str((perm[0][6] + perm[2][0] + perm[1][2]).index('w'))
        tf_stickers += str((perm[0][5] + perm[2][1]).index('w'))
        tf_stickers += str((perm[0][4] + perm[3][0] + perm[2][2]).index('w'))
        tf_stickers += str((perm[0][3] + perm[3][1]).index('w'))
        tf_stickers += str((perm[0][2] + perm[4][0] + perm[3][2]).index('w'))
        tf_stickers += str((perm[0][1] + perm[4][1]).index('w'))

        return tf_stickers


    def _rotate(self, s, n):
        if (n % 2) != 0:
            raise Exception('An incorrect rotation amount (n) was entered: %d.' % n +
                            ' It must be a multiple of 2.')

        deque_s = deque(s)
        deque_s.rotate(-n)
        self.tf_stickers = ''.join(deque_s)


    def _find_oll(self):
        tf_stickers = self.tf_stickers

        ## Checks against each OLL in the dict
        for oll in oll_dict:
            rotation = 0

            ## Rotates the OLL to check if roation was wrong
            for _ in range(4):
                if  tf_stickers == oll:
                    return oll_dict[oll], rotation
                else:
                    ## If rotation was wrong, try again
                    self._rotate(tf_stickers, 2)
                    rotation += 1


class PLLCases():
    '''
    This class handles the PLL cases. A permutation is is given then the correct
    PLL is found using the unique identifiers in pll_dict. This PLL (written as
    'x_perm') can be found in pll_algs.py.
    


    The identifier is found with _ll_hash, then the PLL algorithm is
    found. If it's not found, an exception is thrown.

    Parameters:
    perm - The permutation of a cube that is at PLL
    '''
    def __init__(self, perm):
        self.ll_stickers = self._ll_hash(perm)

        try:
            self.pll, self.rotation = self._find_pll()
        except TypeError:
            raise Exception('Could not find the matching hash for %s' % self.ll_stickers +
                           'in pll_dict computed from permutation:', list(perm))


    def _ll_hash(self, perm):
        ll_stickers = ''.join(perm[1:5].astype('|S3').astype(str))
        centers = [side[-1] for side in perm[1:5]]

        for n, color in enumerate(centers):
            ll_stickers = ll_stickers.replace(color, str(n))

        return ll_stickers


    def _rotate(self, s, n):
        if (n % 3) != 0:
            raise Exception('An incorrect rotation amount (n) was entered: %d.' % n +
                            ' It must a multiple of 3.')

        deque_s = deque(s)
        deque_s.rotate(-n)
        deque_s = np.array(deque_s).astype(int)
        deque_s = ''.join(((deque_s + int(n / 3)) % 4).astype(str))

        self.ll_stickers = deque_s


    def _find_pll(self):
        for pll in pll_dict:
            rotation = 0
            for _ in range(4):
                if self.ll_stickers == pll:
                    return pll_dict[pll], rotation
                else:
                    self._rotate(self.ll_stickers, 3)
                    rotation += 1