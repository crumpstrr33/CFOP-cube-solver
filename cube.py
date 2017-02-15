import numpy as np
from algorithms.alg_dicts import turn_dict
from algorithms.tools import alg_to_code, opposite, face_to_rotation


class Cube:
    '''
    Cube class which creates an object representing a 3x3 Rubik's cube in some
    specific permutation as described below.

    The permutation of the cube is stored in the form of a six element numpy
    array in order of faces: [up, left, front, right, back, down].

    Each element is an 8 char string representing the 8 noncenter stickers
    going clockwise starting at the upperleft corner. (To those wondering,
    this orientation is inspired by the memo techniques for BLD solving
    using OP corners and M2 edges, probably the best beginner BLD method)

    Also, the center pieces follows the list perm like: [white, orange,
    green, red, blue, yellow]. (Again, for those curious people, this comes
    from the official WCA scrambling rules which is white on up face and
    green on front face)

    Parameters:
    perm - (optional) the permutation of the cube as described above. If no
           perm is given, a solved cube is assumed which is given as:
           ['wwwwwwww', 'oooooooo', 'gggggggg', 'rrrrrrrr', 'bbbbbbbb', 'yyyyyyyy']
    '''
    def __init__(self, perm=0, centers=0):
        if centers == 0:
            self.centers = np.array(['w','o', 'g', 'r', 'b', 'y'])
        else:
            ## Check if there's a right number of centers
            if len(centers) != 6:
                raise Exception('There were %d centers given but need 6.' % len(centers))

            ## Check if the center colors make sense
            for center in centers:
                if centers.count(center) != 1:
                    raise Exception('Found %d centers of color:' % centers.count(center), center)

            self.centers = centers

        if perm == 0:
            self.perm = np.array(['wwwwwwww', 'oooooooo', 'gggggggg',
                                  'rrrrrrrr', 'bbbbbbbb', 'yyyyyyyy'])
        else:
            perm = np.array(perm)

            ## Check if the permuation has 6 sides
            if len(perm) != 6:
                raise Exception('There were %d sides given but need 6.' % len(perm))

            ## Check if each side has 8 stickers
            for side in perm:
                if len(side) != 8:
                    raise Exception('Side %s has %d stickers but need 8.' % (side, len(side)))

            ## Check if there are 8 stickers for each color
            for center in self.centers:
                if ''.join(perm).count(center) != 8:
                    raise Exception('Found %d stickers for color:' % ''.join(perm).count(center), center)

            self.perm = perm


    def _rotate(self, *sides, length):
        '''
        Rotates the sides of the cube by length.
        '''
        for side in sides:
            rotated_side = self.perm[side][-length:] + self.perm[side][:-length]
            self.perm[side] = rotated_side


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
            turn_info = turn_dict[turn]
            if turn_info[0] in ['x', 'y', 'z']:
                self.rotate_cube(*turn_info)
            else:
                self.turn_rotate(*turn_info)


    def rotate_cube(self, axis, ttype):
        '''
        Does a rotation of the cube

        Parameters:
        axis - The axis of the cube to do the rotation, either x, y or z
               with x being rotation like the R face, y is like rotation of
               the U face and z is like the rotation of the F face
        ttype - The type of rotation, either 1 for a clockwise turn, -1
                for a counterclockwise turn or 2 for a double turn
        '''
        ## An x rotation is just a combination of y and z rotations
        if axis == 'x':
            self.rotate_cube('y', 1)
            self.rotate_cube('z', ttype)
            self.rotate_cube('y', -1)
            return
        ## Setup the correct faces to switch and rotate
        elif axis == 'y':
            face_switch = [[0, 2, 3, 4, 1, 5],
                           [0, 3, 4, 1, 2, 5],
                           [0, 4, 1, 2, 3, 5]]
            dt_rotate = [0, 5]
            st_rotate = [[0], [5]]
        elif axis == 'z':
            face_switch = [[1, 5, 2, 0, 4, 3],
                           [5, 3, 2, 1, 4, 0],
                           [3, 0, 2, 5, 4, 1]]
            dt_rotate = [0, 1, 2, 3, 4, 5]
            st_rotate = [[0, 1, 2, 3, 5], [4]]

        ## Use lists from above to do the switching and string rotations
        if ttype == 2 or ttype == -2:
            self.perm = self.perm[face_switch[1]]
            self._rotate(*dt_rotate, length=4)
        elif ttype == 1:
            self.perm = self.perm[face_switch[0]]
            self._rotate(*st_rotate[0], length=2)
            self._rotate(*st_rotate[1], length=-2)
        else:
            self.perm = self.perm[face_switch[2]]
            self._rotate(*st_rotate[1], length=2)
            self._rotate(*st_rotate[0], length=-2)


    def turn_rotate(self, face, ttype, dl=False):
        '''
        Does the rotation necessary to rotate face to the up face to do a turn
        by using self.turn.

        Parameters:
        face - The face to rotate, either 'u', 'l', 'f', 'r', 'b' or 'd'
        ttype - The type of turn, either 1 for clockwise, -1 for 
                counterclockwise or 2 for a double turn
        dl - (optional) If true a double layer turn will be done
        '''
        ## Rotate and then turn opposite face for a dl turn
        if dl:
            ## Get correct axis to rotate and type of rotation based on face
            rotation, direction = face_to_rotation(face, True)
            
            self.turn_rotate(opposite(face, 'faces'), ttype)
            self.rotate_cube(rotation, ttype * direction)
        ## Middle slice is a special case
        elif face == 'm':
            self.turn_rotate('r', ttype)
            self.turn_rotate('l', -ttype)
            self.rotate_cube('x', -ttype)
        else:
            ## Get correct axis to rotate and type of rotation based on face
            rotation, direction = face_to_rotation(face, False)

            ## Since turns are done to up face, up and down faces are special
            if face == 'u':
                self.turn(ttype)
            elif face == 'd':
                self.rotate_cube('x', 2)
                self.turn(ttype)
                self.rotate_cube('x', 2)
            else:
                self.rotate_cube(rotation, direction)
                self.turn(ttype)
                self.rotate_cube(rotation, -direction)


    def turn(self, ttype):
        '''
        Does a turn of the up face
        
        Parameters:
        ttype - The type of turn, either 1 for clockwise, -1 for 
                counterclockwise or 2 for a double turn
        '''
        ## Check if correct ttype
        turn = (ttype in [1, 'cw']) - (ttype in [-1, 'ccw']) + 2 * (ttype in [2, -2, 'dt'])
        if turn not in [-1, 1, 2]:
            raise Exception('ttype = %s, turn amount is %d which is not allowed.'
                            % (ttype, turn))

        perm_sides = self.perm[1:5]
        new_perm = []

        ## Rotate the first three stickers of the side faces
        for n, side in enumerate(perm_sides):
            next_side = (n + turn) % 4
            new_perm.append(perm_sides[next_side][:3] + perm_sides[n][3:])

        self.perm[[1, 2, 3, 4]] = new_perm
        ## Rotate top face stickers
        self._rotate(0, length=2 * turn)