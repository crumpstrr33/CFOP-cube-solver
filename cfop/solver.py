'''
Contains the Solver class.
'''
from itertools import permutations

from cfop.cube import Cube
from cfop.cross import Cross
from cfop.f2l import F2L
from cfop.algorithms.tools import code_to_alg


class Solver(Cube):
    """
    A class that inherits from the Cube class. This class
    primarily keeps track of the turns used and stores it as
    a cubing algorithm as solving_alg as well as what step
    the solver is current on by using self.find_step.

    Parameters:
    perm - (default 0) The permutation of the cube. If no
           permutation is given then the solved cube is given
           following the rules laid out in the Cube class
    """

    def __init__(self, perm=0):
        super().__init__(perm)
        self.solving_alg = ''
        self.step = 'scrambled'

    @property
    def inspect_alg(self):
        return code_to_alg(self.ialg)

    @property
    def cross_alg(self):
        return code_to_alg(self.calg)

    @property
    def f2l_alg(self):
        return [code_to_alg(alg) for alg in self.falg]

    @property
    def oll_alg(self):
        return code_to_alg(self.oalg)

    @property
    def pll_alg(self):
        return code_to_alg(self.palg)

    @property
    def alg(self):
        return {'Inspection': self.inspect_alg,
                'Cross': self.cross_alg,
                'F2L': {'1st Pair': self.f2l_alg[0],
                        '2nd Pair': self.f2l_alg[1],
                        '3rd Pair': self.f2l_alg[2],
                        '4th Pair': self.f2l_alg[3]},
                'OLL': self.oll_alg,
                'PLL': self.pll_alg}

    def apply_alg(self, alg, alg_input=False):
        """
        Applies the algorithm alg to the cube. The alg can
        either be written as a cubing algorithm or as the
        code syntax. The Solver class algorithm will remember
        what algorithm was used and save that in solving_alg.

        Parameters:
        alg - Algorithm to apply to the cube
        alg_input - (default False) If True, will assume alg is
                    written in cubing notation. If False,
                    will assume alg is written as the coding
                    syntax
        """
        super().apply_alg(alg, alg_input)
        self.solving_alg += alg

    def find_step(self):
        """
        Finds the correct step that the Solver is at based
        on it's relation to a solved cube.
        """
        up_face_color = ''.join(self.perm[(0, 1, 0)])
        front_face_color = ''.join(self.perm[(0, 0, 1)])
        solved_cube = Cube()

        # Rotate correct top face
        rotation_xz = {'b': 'X', 'g': 'x',
                       'o': 'z', 'r': 'Z',
                       'w': '', 'y': '8'}[up_face_color]
        solved_cube.apply_alg(rotation_xz)

        # Rotate correct front face
        for _ in range(3):
            ffc = ''.join(solved_cube.perm[(0, 0, 1)])
            if ffc == front_face_color:
                break
            solved_cube.apply_alg('y')

        cross_edges = 0
        f2l_edges_and_corners = 0
        oll_correct = 0
        pll_correct = 0

        for coord, color in self.perm.items():
            # Counts number of cross edges that are correct
            if (coord[1] == -1 and
                    coord.count(0) == 1 and
                    color == solved_cube.perm[coord]):
                cross_edges += 1
            # Counts number of f2l pairs inserted
            elif (coord[1] != 1 and
                  coord.count(0) != 2 and
                  color == solved_cube.perm[coord]):
                f2l_edges_and_corners += 1
            # Counts number of correctly orientated and
            # correctly permutated U cubies
            elif coord[1] == 1 and coord.count(0) != 2:
                pll_correct += color == solved_cube.perm[coord]
                oll_correct += color[1] == solved_cube.perm[coord][1]

        correct = [cross_edges == 4, f2l_edges_and_corners == 8,
                   oll_correct == 8, pll_correct == 8]
        if all(correct):
            self.step = 'solved'
        elif all(correct[0:3]):
            self.step = 'pll'
        elif all(correct[0:2]):
            self.step = 'oll'
        elif correct[0]:
            self.step = 'f2l'
        else:
            self.step = 'cross'

    def solve_cross(self):
        """
        Solves for the cross on the Down face.
        """
        cross = Cross(self.perm)

        self.calg = cross.alg
        self.open_sets = cross.open_sets
        self.closed_sets = cross.closed_sets

        # TODO Add inspection (pick best cross)
        self.ialg = ''

        self.apply_alg(self.calg)

    def solve_f2l(self):
        side_centers, side_edges = [], []
        # Get the centers not on the U or D face
        for coord, color in self.perm.items():
            if coord.count(0) == 2 and coord[1] == 0:
                side_centers.append((coord, color))
        # For each center check with the remaining
        for n, i in enumerate(side_centers):
            for j in side_centers[n + 1:]:
                # If it's not opposite (i.e. j has a value with an abs of 1
                # as the same element of i)
                if list(map(abs, i[0])).index(1) != \
                   list(map(abs, j[0])).index(1):
                    side_edges.append(''.join(i[1]) + ''.join(j[1]))
        # Get all 24 orders for solving F2L
        f2l_orders = list(permutations(side_edges))
        for f2l_order in f2l_orders:
            # Solve for each one and continue with the lowest move count one
            # No point in mocking it up now
            pass

        self.f2l_pairs = ['go', 'gr', 'bo', 'br']
        f2l = F2L(self.perm, self.f2l_pairs)

        self.falg = f2l.algs
        self.open_setss = f2l.open_setss
        self.closed_setss = f2l.closed_setss

        self.apply_alg(''.join(self.falg))

    def solve_oll(self):
        # TODO
        self.oalg = ''

    def solve_pll(self):
        # TODO
        self.palg = ''

    def solve_it(self):
        """
        The current step is found and the appropriate method is called.
        """
        self.find_step()
        if self.step == 'cross':
            self.solve_cross()
        elif self.step == 'f2l':
            self.solve_f2l()
        elif self.step == 'oll':
            self.solve_oll()
        elif self.step == 'pll':
            self.solve_pll()
        elif self.step == 'finished':
            pass
        else:
            raise Exception('STEP NOT FOUND!')
