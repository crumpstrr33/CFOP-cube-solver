from collections import deque
from algorithms.alg_dicts import oll_dict, pll_dict
from algorithms.tools import opposite


class OLLCases:
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
    consistency in this context isn't necssary. Plus, I use it in PLLCases().

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
        '''
        Turns the permutation into a unique identifier for each OLL
        '''
        c = opposite(perm[-1][0], 'colors')

        ## The correct stickers, looking for where the top face sticker is
        tf_stickers  = str((perm[0][0] + perm[1][0] + perm[4][2]).index(c))
        tf_stickers += str((perm[0][7] + perm[1][1]).index(c))
        tf_stickers += str((perm[0][6] + perm[2][0] + perm[1][2]).index(c))
        tf_stickers += str((perm[0][5] + perm[2][1]).index(c))
        tf_stickers += str((perm[0][4] + perm[3][0] + perm[2][2]).index(c))
        tf_stickers += str((perm[0][3] + perm[3][1]).index(c))
        tf_stickers += str((perm[0][2] + perm[4][0] + perm[3][2]).index(c))
        tf_stickers += str((perm[0][1] + perm[4][1]).index(c))

        return tf_stickers


    def _rotate(self, s, n):
        '''
        Rotates a string by an amount n.

        Parameters:
        s - String to be rotated
        n - Amount to rotate the string by
        '''
        if n == 0:
            return s

        rotated_s = s[-n:] + s[:-n]
        return rotated_s


    def _find_oll(self):
        '''
        Finds the correct OLL needed to solve the case along with the correct
        initial up face turn (if any).
        '''
        for i in range(4):
            tf_stickers_rotated = self._rotate(self.tf_stickers, 2 * i)

            if tf_stickers_rotated in oll_dict:
                return oll_dict[tf_stickers_rotated], i


class PLLCases:
    '''
    This class handles the PLL cases. A permutation is is given then the correct
    PLL is found using the unique identifiers in pll_dict. This PLL (written as
    'x_perm') can be found in pll_algs.py.
    
    This unique identifier is found by recording the last layer stickers 
    starting on the right face in the top left and move counterclockwise around
    the top face getting a string 12 long. Then each char is converted to an int
    according to which face is should be (e.g. if red is the left face and there
    is a red sticker on the left face, then that sticker will be replaced with a
    2). This gives a unique identifier as to how the stickers should be rotated
    around the cube.

    The identifier is found with _ll_hash, then the PLL algorithm is
    found. If it's not found, an exception is thrown.

    Parameters:
    perm - The permutation of a cube that is at PLL
    '''
    def __init__(self, perm):
        self.ll_stickers = ''.join(perm[1:5].astype('|S3').astype(str))
        self.centers = ''.join([side[-1] for side in perm[1:5]])
        try:
            self.pll, self.rotation_b, self.rotation_a = self._find_pll()
        except TypeError:
            raise Exception('Could not find the matching hash for %s' % self.ll_stickers +
                            ' in pll_dict computed from permutation:', list(perm))


    def _ll_hash(self, ll_stickers):
        '''
        Turns a string of stickers (the last layer stickers of which there are
        12) into a unique identifier to figure out which PLL to use by
        replacing the color with the side it should be on (left, front, right,
        back or 0, 1, 2, 3 respectively).

        Parameters:
        ll_stickers - The string of 12 stickers to be turned into a string
                      of numbers
        '''
        for n, color in enumerate(self.centers):
            ll_stickers = ll_stickers.replace(color, str(n))

        return ll_stickers


    def _rotate(self, s, n):
        '''
        Rotates a string by an amount n.

        Parameters:
        s - String to be rotated
        n - Amount to rotate the string by
        '''
        if n == 0:
            return s

        rotated_s = s[-n:] + s[:-n]
        return rotated_s


    def _add(self, s, n):
        '''
        For a string of digits, adds n to each digit.

        Parameters:
        s - String to which n will be added
        n - The amount to add to each digit of the string
        '''
        if n == 0:
            return s

        s_plus_n = [str((int(x) + n) % 4) for x in s]
        return ''.join(s_plus_n)


    def _find_pll(self):
        '''
        Finds the PLL based on the 12 character string for the stickers of
        the last layer and returns this PLL allow with the relevant rotations.
        '''
        ## Check against the 4 rotations of the top layer (AUF before PLL)
        for i in range(4):
            ll_rotated = self._rotate(self.ll_stickers, 3 * i)
            ll_code = self._ll_hash(ll_rotated)

            ## Check against the moves of the top layer (AUF after PLL)
            for j in range(4):
                added_ll_code = self._add(ll_code, j)

                ## Return correct PLL and the rotations done
                if added_ll_code in pll_dict:
                    return pll_dict[added_ll_code], i, j