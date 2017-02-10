from cube import Cube
from algorithms.tools import code_to_alg
from oll_pll import OLLCases, PLLCases
from algorithms.alg_dicts import oll_dict, pll_dict
from algorithms import oll_algs, pll_algs


class Solver(Cube):
    '''
    A class that inherits from the Cube class. This class primarily keeps track
    of the turns used and stores it as a cubing algorithm as solving_alg as well
    as what step the solver is current on by using self.find_step.

    Parameters:
    perm - (optional) The permutation of the cube. If no permutation is given
           then the solved cube is given following the rules laid out in the 
           Cube class
    '''
    def __init__(self, perm=0):
        Cube.__init__(self, perm)
        self.solving_alg = ''


    def apply_alg(self, alg, alg_input=False):
        '''
        Applies the algorithm alg to the cube. The alg can either be written
        as a cubing algorithm or as the code syntax. The Solver class algorithm
        will remember what algorithm was used and save that in solving_alg.

        Parameters:
        alg - Algorithm to apply to the cube
        alg_input - (optional) If True, will assume alg is written in cubing
                    notation. If False, will assume alg is written as the 
                    coding syntax
        '''
        Cube.apply_alg(self, alg, alg_input)
        self.solving_alg += alg


    def find_step(self):
        '''
        Finds which step the solve is currently at. The cross step is the first
        step. The F2L step occurs once a cross has been established. This step
        is divided into substeps of how many F2L pairs have been inserted. If
        the first two layers are solved but the top layer is not oriented, then
        it is at OLL. Then if it is oriented, then it is at PLL.
        '''
        if (self.perm == ['wwwwwwww', 'oooooooo', 'gggggggg',
                          'rrrrrrrr', 'bbbbbbbb', 'yyyyyyyy']).all():
            self.step = 'finished'
            return

        for n, side in enumerate(self.perm[1:5]):
            ## Check if second layer is solved
            if (side[3] + side[7]).count(self.centers[n + 1]) == 2:
                ## Check if top face is oriented correctly
                if self.perm[0].count(self.centers[0]) == 8:
                    self.step = 'pll'
                    return
                else:
                    self.step = 'oll'
                    return
            else:
                break

        f2l_pairs = 0
        ## Check if the bottom face has it's edges correctly
        if self.perm[5][1::2].count(self.centers[5]) == 4:
            for n, side in enumerate(self.perm[1:5]):
                ## Check lower edge pieces of sides
                if side[5] != self.centers[n + 1]:
                    self.step = 'cross'
                    return
                else:
                    ## Check for f2l pairs
                    if self.perm[5][2 * n] == self.centers[5]:
                        if (self.perm[n + 1][3] == self.centers[n + 1] and
                            self.perm[(n + 1) % 4 + 1][7] == self.centers[(n + 1) % 4 + 1]):
                                f2l_pairs += 1
            self.step = 'f2l_' + str(f2l_pairs)
        else:
            self.step = 'cross'


    def solve_oll(self):
        '''
        With the current permutation, the correct OLL will be found and
        applied to the cube.
        '''
        oll = OLLCases(self.perm)

        self.oll = oll.oll
        self.oll_algorithm = getattr(oll_algs, oll.oll)
        self.apply_alg(['', 'U', '!', 'T'][oll.rotation])
        self.apply_alg(self.oll_algorithm)


    def solve_pll(self):
        '''
        With the current permutation, the correct PLL will be found and
        applied to the cube.
        '''
        pll = PLLCases(self.perm)

        self.pll = pll.pll
        self.pll_algorithm = getattr(pll_algs, pll.pll)
        self.apply_alg(['', 'U', '!', 'T'][pll.rotation])
        self.apply_alg(self.pll_algorithm)


    def solve_it(self):
        '''
        The current step is found and the appropriate is then taken.
        '''
        self.find_step()
        if self.step == 'cross':
            print('CROSS STEP NOT DONE YET!')
        elif 'f2l' in self.step:
            print('F2L_%s STEP NOT DONE YET!' % self.step[-1])
        elif self.step == 'oll':
            self._solve_oll()
        elif self.step == 'pll':
            self._solve_pll()
        else:
            raise Exception('STEP NOT FOUND!')