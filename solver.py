from cube import Cube
from cross import Cross

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
        pass


    def solve_cross(self):
        cross = Cross(self.perm)

        self.cross_color = cross.cross_color
        self.cross_alg = cross.alg

        self.apply_alg(self.cross_alg)


    def solve_f2l(self):
        pass


    def solve_oll(self):
        pass


    def solve_pll(self):
        pass


    def solve_it(self):
        '''
        The current step is found and the appropriate method is called.
        '''
        self.find_step()
        if self.step == 'cross':
            self.solve_cross()
        elif 'f2l' in self.step:
            self.solve_f2l()
        elif self.step == 'oll':
            self.solve_oll()
        elif self.step == 'pll':
            self.solve_pll()
        elif self.step == 'finished':
            pass
        else:
            raise Exception('STEP NOT FOUND!')


    def is_solved(self):
        '''
        Determines if the cube is solved and returns an appropriate boolean.
        '''
        self.find_step()
        if self.step == 'finished':
            return True
        else:
            return False