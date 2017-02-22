import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from mpl_toolkits.mplot3d import Axes3D

from algorithms.tools import alg_to_code
from algorithms.alg_dicts import param_dict, turn_dict


class Cube:
    def __init__(self, perm=0):
        if perm == 0:
            perm = ['wwwwwwwww', 'ooooooooo', 'ggggggggg',
                    'rrrrrrrrr', 'bbbbbbbbb', 'yyyyyyyyy']

        self.perm = self._convert_perm(perm)


    def _convert_perm(self, perm):
        '''
        Converts the permuation from a six element list of nine char strings
        representing the stickers on each face to a 27 length dict for where
        each key is a cubie coordinate and each value are the sticker colors.
        '''
        ## Turn each string into a 2D list where each element is a 3-element
        ## list representing one row of stickers on the cube
        converted_perm = []
        for side in perm:
            face_list, row_str = [], ''
            for sticker in range(len(side)):
                row_str += side[sticker]
                if (sticker + 1) % 3 == 0:
                    face_list.append(list(row_str))
                    row_str = ''

            converted_perm.append(face_list)

        ## Create dict to put in the colors
        cube_dict = {coord : [' ', ' ', ' '] for coord in
                     product(range(-1, 2), range(-1, 2), range(-1, 2))}

        ## Adding colors to dict
        for cubie in cube_dict:
            if cubie[0] == 1:
                cube_dict[cubie][0] = converted_perm[3][abs(cubie[1] - 1)][abs(cubie[2] - 1)]
            if cubie[0] == -1:
                cube_dict[cubie][0] = converted_perm[1][abs(cubie[1] - 1)][cubie[2] + 1]
            if cubie[1] == 1:
                cube_dict[cubie][1] = converted_perm[0][cubie[2] + 1][cubie[0] + 1]
            if cubie[1] == -1:
                cube_dict[cubie][1] = converted_perm[5][abs(cubie[2] - 1)][cubie[0] + 1]
            if cubie[2] == 1:
                cube_dict[cubie][2] = converted_perm[2][abs(cubie[1] - 1)][cubie[0] + 1]
            if cubie[2] == -1:
                cube_dict[cubie][2] = converted_perm[4][abs(cubie[1] - 1)][abs(cubie[0] - 1)]

        return cube_dict


    def turn_rotate(self, ttype, side, dl=False):
        '''
        Will turn or rotate the cube by 'ttype' on face 'side'.
        
        Parameters:
        ttype - The type of rotation. Can be 'cw' for clockwise, 'ccw' for
                counterclockwise or 'dt' for a double turn
        side - The side of the face to turn or the rotation to do. Can be
               'u', 'l', 'f', 'r', 'b', 'd', 'm', 'x', 'y' or 'z'
        dl - (optional) Will do a double layer turn of 'side'. This will not 
             work with the middle slice 'm' or rotations 'x', 'y', 'z'
        '''
        ## Checks if it's a rotation or turn
        if side in ['x', 'y', 'z']:
            rotate = True
        else:
            rotate = False

        ## Finds equivalent face to turn
        if side == 'x':
            face = 'r'
        elif side == 'y':
            face = 'u'
        elif side == 'z':
            face = 'f'
        elif side == 'm':
            face = 'l'
        else:
            face = side

        p = param_dict[ttype][face]
        new_coords = {}
        perm_copy = self.perm.copy()

        ## Choose correct layers to rotate
        if dl:
            turning_layers = [0, p[1]]
        elif side == 'm':
            turning_layers = [0]
        elif rotate:
            turning_layers = [-1, 0, 1]
        else:
            turning_layers = [p[1]]

        for cubie, colors in perm_copy.items():
            if cubie[p[0]] in turning_layers:
                new_coords[(p[2]*cubie[p[3]], p[4]*cubie[p[5]], p[6]*cubie[p[7]])] = \
                          [colors[p[3]], colors[p[5]], colors[p[7]]]

        ## Updates the coordinates and colors
        self.perm.update(new_coords)


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
        if alg_input:
            alg = alg_to_code(alg)

        for turn in alg:
            self.turn_rotate(*turn_dict[turn])


    def graph_cube(self):
        '''
        Graphs the cube for easy visualization.
        '''
        X, Y = np.meshgrid([0, 1], [0, 1])
        Z = 0.5

        ## Creates a copy dict with spelt out names just in case
        cv = {}
        colors = {' ' : ' ', 'w' : 'white', 'y' : 'yellow', 'g' : 'green',
                  'b' : 'blue', 'r' : 'red', 'o' : 'orange'}
        for cubie in self.perm:
            color = self.perm[cubie]
            cv[cubie] = [colors[color[0]], colors[color[1]], colors[color[2]]]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ## If the cubie has some coordinate, it will create a square at that coordinate
        for cubie in cv:
            if cubie[0] == 1:
                ax.plot_surface(Y + cubie[2], Z + 1.5, X + cubie[1], color=cv[cubie][0])
            if cubie[0] == -1:
                ax.plot_surface(Y + cubie[2], Z - 1.5, X + cubie[1], color=cv[cubie][0])
            if cubie[1] == 1:
                ax.plot_surface(Y + cubie[2], X + cubie[0], Z + 1.5, color=cv[cubie][1])
            if cubie[1] == -1:
                ax.plot_surface(Y + cubie[2], X + cubie[0], Z - 1.5, color=cv[cubie][1])
            if cubie[2] == 1:
                ax.plot_surface(Z + 1.5, X + cubie[0], Y + cubie[1], color=cv[cubie][2])
            if cubie[2] == -1:
                ax.plot_surface(Z - 1.5, X + cubie[0], Y + cubie[1], color=cv[cubie][2])