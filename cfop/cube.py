"""
Contains the Cube class.
"""
from itertools import product
import matplotlib.pyplot as plt
from numpy import meshgrid
from mpl_toolkits.mplot3d import Axes3D

from cfop.algorithms.tools import alg_to_code
from cfop.algorithms.alg_dicts import PARAM_DICT, TURN_DICT


class Cube:
    """
    Cube class which creates an object repreenting a 3x3 Rubik's cube in some
    specific permutation as described below.
    The permutation of the cube is stored as a dict with 27 entries. Each entry
    represents one cubie of the cube (a cubie is a solid piece of the cube, so
    3x3x3=27 cubies) with the key as a 3-tuple for the coordinate (e.g. (x, y,
    z)) and the value as a 3 element list of the color for each coordinate. The
    6 centers will have two 0's in the 3-tuple and two empty strings in the
    list, the 8 corners will have one 0 in the 3-tuple and one empty string in
    the list and the 12 corners will have no 0's or empty strings.

    A permutation is inputted as a 6 element list. Each element represents a
    face. This is done so in the order: Up, Left, Front, Right, Back, Down
    which was inspired by a memo technique for BLD solving using OP corners and
    M2 edges. The string of each element are the 9 stickers of that face
    starting in the upper left and going right and then repeating for the
    remaining two rows.

    This permutation is translated into the dict by the _convert_perm method
    to make the input of custom permuations simpler.

    Parameters:
    perm - (default 0) The permuation of the cube as described above. If no
           perm is given, a solved cube is assumed with a white Up face and
           green Front face. Perm can also be given as a dict that does not
           need to be converted
    """

    def __init__(self, perm=0):
        if isinstance(perm, dict):
            self.perm = perm
        else:
            if perm == 0:
                perm = ['wwwwwwwww', 'ooooooooo', 'ggggggggg',
                        'rrrrrrrrr', 'bbbbbbbbb', 'yyyyyyyyy']

            self.perm = self._convert_perm(perm)

    @staticmethod
    def _convert_perm(perm):
        """
        Converts the permuation from a six element list of
        nine char strings representing the stickers on each
        face to a 26 length dict for where each key is a
        cubie coordinate and each value are the sticker
        colors.
        """
        # Turn each string into a 2D list where each element
        # is a 3-element list representing one row of
        # stickers on the cube
        converted_perm = []
        for side in perm:
            face_list, row_str = [], ''

            for n, sticker in enumerate(side):
                row_str += sticker

                if not (n + 1) % 3:
                    face_list.append(list(row_str))
                    row_str = ''

            converted_perm.append(face_list)

        # Create dict to put in the colors
        r = range(-1, 2)
        cube_dict = {coord: ['', '', ''] for coord in product(r, r, r)}
        cube_dict.pop((0, 0, 0))

        # Adding colors to dict, it's messy and unintuitive,
        # I know. I should make it better looking
        for cubie in cube_dict:
            if cubie[0] == 1:
                i, j, k = 3, abs(cubie[1] - 1), abs(cubie[2] - 1)
                cube_dict[cubie][0] = converted_perm[i][j][k]
            if cubie[0] == -1:
                i, j, k = 1, abs(cubie[1] - 1), cubie[2] + 1
                cube_dict[cubie][0] = converted_perm[i][j][k]
            if cubie[1] == 1:
                i, j, k = 0, cubie[2] + 1, cubie[0] + 1
                cube_dict[cubie][1] = converted_perm[i][j][k]
            if cubie[1] == -1:
                i, j, k = 5, abs(cubie[2] - 1), cubie[0] + 1
                cube_dict[cubie][1] = converted_perm[i][j][k]
            if cubie[2] == 1:
                i, j, k = 2, abs(cubie[1] - 1), cubie[0] + 1
                cube_dict[cubie][2] = converted_perm[i][j][k]
            if cubie[2] == -1:
                i, j, k = 4, abs(cubie[1] - 1), abs(cubie[0] - 1)
                cube_dict[cubie][2] = converted_perm[i][j][k]

        return cube_dict

    def turn_rotate(self, ttype, side, dl=False):
        """
        Will turn or rotate the cube by 'ttype' on face
        'side'.

        Parameters:
        ttype - The type of rotation. Can be 'cw' for
                clockwise, 'ccw' for counterclockwise or 'dt'
                for a double turn
        side - The side of the face to turn or the rotation
               to do. Can be 'u', 'l', 'f', 'r', 'b', 'd',
               'm', 'x', 'y' or 'z'
        dl - (default False) Will do a double layer turn of
             'side'. This will not work with the middle slice
             'm' or rotations 'x', 'y', 'z'
        """
        if ttype not in ['cw', 'ccw', 'dt']:
            raise Exception(("A ttype of '{}' was used ").format(ttype) +
                            "which is not 'cw', 'ccw' or 'dt'.")

        if side in ['m', 'x', 'y', 'z'] and dl:
            raise Exception('A double layer turn was chosen ' +
                            ("with a side of '{}'. ").format(side) +
                            'If dl=True, side must be' +
                            "'u', 'l', 'f', 'r', 'b' or 'd'.")

        if side not in ['u', 'l', 'f', 'r', 'b', 'd', 'm', 'x', 'y', 'z']:
            raise Exception('An incorrect side of {} was chosen'.format(side) +
                            'It is not the middle slice or a rotation.')

        # Checks if it's a rotation or turn
        rotate = side in ['x', 'y', 'z']

        # Finds equivalent face to turn
        if side in ['x', 'y', 'z', 'm']:
            equiv_face = {'x': 'r', 'y': 'u', 'z': 'f', 'm': 'l'}
            face = equiv_face[side]
        else:
            face = side

        # Get the right parameters for the cubie rotation
        p = PARAM_DICT[ttype][face]
        new_coords = {}

        # Choose correct layers to rotate
        if dl:
            turning_layers = [0, p[1]]
        elif side == 'm':
            turning_layers = [0]
        elif rotate:
            turning_layers = [-1, 0, 1]
        else:
            turning_layers = [p[1]]

        for cubie, colors in self.perm.copy().items():
            if cubie[p[0]] in turning_layers:
                new_coords[(p[2]*cubie[p[3]],
                            p[4]*cubie[p[5]],
                            p[6]*cubie[p[7]])] = \
                            [colors[p[3]], colors[p[5]], colors[p[7]]]

        # Updates the coordinates and colors
        self.perm.update(new_coords)

    def apply_alg(self, alg, alg_input=False):
        """
        Applies the algorithm alg to the cube. The alg can
        either be written as a cubing algorithm or as the
        code syntax.

        Parameters:
        alg - Algorithm to apply to the cube
        alg_input - (default False) If True, will assume alg is
                    written in cubing notation. If False,
                    will assume alg is written as the
                    coding syntax
        """
        if alg_input:
            alg = alg_to_code(alg)

        for turn in alg:
            self.turn_rotate(*TURN_DICT[turn])

    def graph_cube(self, gap_color='k', gap_width=2, bg_color='w',
                   w='ghostwhite', y='gold', g='forestgreen',
                   b='midnightblue', r='crimson', o='darkorange'):
        """
        Graphs the cube for easy visualization with optional arguments for
        visual preference

        Parameters:
        gap_color - (default 'k') The color of the gap between all of the
                     stickers
        gap_width - (default 2) The width of the gap between of the stickers.
        bg_color - (default 'w') The background color of the plot
        w - (default ghostwhite) The color of the white stickers
        y - (default gold) The color of the yellow stickers
        g - (default forestgreen) The color of the green stickers
        b - (default midnightblue) The color of the blue stickers
        r - (default crimson) The color of the red stickers
        o - (default darkorange) The color of the orange stickers
        """
        X, Y = meshgrid([0, 1], [0, 1])
        Z = 0.5

        # Creating the color scheme for each cubie
        colors = {'w': w, 'y': y, 'g': g, 'b': b, 'r': r, 'o': o, '': ''}
        perm_colors = {}
        for cubie in self.perm:
            c = self.perm[cubie]
            perm_colors[cubie] = [colors[c[0]], colors[c[1]], colors[c[2]]]

        # Create figure for plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(-1, 2)
        ax.set_ylim(-1, 2)
        ax.set_zlim(-1, 2)
        ax.set_facecolor(bg_color)
        ax.axis('off')

        # Will create square of appropriate color at appropriate coordinate
        for cubie in perm_colors:
            if cubie[0] != 0:
                ax.plot_surface(Y + cubie[2], Z + cubie[0] * 1.5, X + cubie[1],
                                edgecolors=gap_color, linewidth=gap_width,
                                color=perm_colors[cubie][0])
            if cubie[1] != 0:
                ax.plot_surface(Y + cubie[2], X + cubie[0], Z + cubie[1] * 1.5,
                                edgecolors=gap_color, linewidth=gap_width,
                                color=perm_colors[cubie][1])
            if cubie[2] != 0:
                ax.plot_surface(Z + cubie[2] * 1.5, X + cubie[0], Y + cubie[1],
                                edgecolors=gap_color, linewidth=gap_width,
                                color=perm_colors[cubie][2])

        plt.show()
