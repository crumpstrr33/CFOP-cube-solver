from cube import Cube
import numpy as np

## z  --> 1
## z' --> 3
## z2 --> 5
## x  --> 2
## x' --> 4


class Solver(Cube):
    '''
    A class that inherits from the Cube class. This class primarily keeps track
    of the turns used and stores it as a cubing algorithm as solving_alg.

    Parameters:
    perm - (optional) The permutation of the cube. If no permutation is given
           then the solved cube is given following the rules laid out in the 
           Cube class
    '''
    def __init__(self, perm=0):
        Cube.__init__(self)
        if perm != 0:
            self.perm = np.array(perm)

        self.solving_alg = ''
        self.centers = 'wogrby'


    def apply_alg(self, alg, alg_input=False):
        '''
        Applies the algorithm alg to the cube. The alg can either be written
        as a cubing algorithm or as the code syntax.

        Parameters:
        alg - Algorithm to apply to the cube
        alg_input - (optional) If True, will assume alg is written in cubing
                    notation. If False, will assume alg is written as the 
                    coding syntax
        '''
        Cube.apply_alg(self, alg, alg_input)
        self.solving_alg += alg