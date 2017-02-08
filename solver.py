from cube import Cube


class Solver(Cube):
    '''
    A class that inherits from the Cube class. This class primarily keeps track
    of the turns used and stores it as a cubing algorithm as solving_alg as well
    as what step the solver is current on by using self._find_step

    Parameters:
    perm - (optional) The permutation of the cube. If no permutation is given
           then the solved cube is given following the rules laid out in the 
           Cube class
    '''
    def __init__(self, perm=0):
        Cube.__init__(self, perm)
        self.solving_alg = ''
        self._find_step()


    def _find_step(self):
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