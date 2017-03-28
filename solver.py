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
        Finds the correct step that the Solver is at based on it's relation to
        a solved cube.
        '''
        up_face_color = ''.join(self.perm[(0, 1, 0)])
        front_face_color = ''.join(self.perm[(0, 0, 1)])
        solved_cube = Cube()

        ## Rotate correct top face
        rotation_xz = {'b': 'X', 'g': 'x', 'o': 'z',
                       'r': 'Z', 'w': '', 'y': '8'}[up_face_color]
        solved_cube.apply_alg(rotation_xz)

        ## Rotate correct front face
        for i in range(3):
            if ''.join(solved_cube.perm[(0, 0, 1)]) == front_face_color:
                break
            solved_cube.apply_alg('y')

        cross_edges = 0
        f2l_edges_and_corners = 0
        oll_correct = 0
        pll_correct = 0

        for coord, color in self.perm.items():
            if coord[1] == -1 and coord.count(0) == 1:
                if color == solved_cube.perm[coord]:
                    cross_edges += 1
            elif coord[1] != 1 and coord.count(0) != 2:
                if color == solved_cube.perm[coord]:
                    f2l_edges_and_corners += 1
            elif coord[1] == 1 and coord.count(0) != 2:
                if color == solved_cube.perm[coord]:
                    pll_correct += 1
                if color[1] == solved_cube.perm[coord][1]:
                    oll_correct += 1

        if cross_edges == 4:
            if f2l_edges_and_corners == 8:
                if oll_correct == 8:
                    if pll_correct == 8:
                        self.step = 'solved'
                    else:
                        self.step = 'pll'
                else:
                    self.step = 'oll'
            else:
                self.step = 'f2l'
        else:
            self.step = 'cross'


    def solve_cross(self):
        '''
        Solves for the cross on the Down face.
        '''
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