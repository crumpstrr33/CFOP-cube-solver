import numpy as np
from collections import deque
from algorithms.alg_dicts import turn_dict
from algorithms.tools import alg_to_code


class Cube():
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
        for side in sides:
            deque_side = deque(self.perm[side])
            deque_side.rotate(length)
            self.perm[side] = ''.join(deque_side)


    def turn_up(self, ttype, dl=False):
        '''
        Turns the up face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        dl - (optional) Whether to perform a double turn
        '''
        if dl:
            self.turn_down(ttype)
            self.rotate_y(ttype == 1, ttype == 2)
        else:
            ## Check if correct ttype
            turn = (ttype in [1, 'cw']) - (ttype in [-1, 'ccw']) + 2 * (ttype in [2, 'dt'])
            if turn not in [-1, 1, 2]:
                raise Exception('ttype = %s, turn amount is %d which is not allowed.'
                                % (ttype, turn))
    
            layer = 3
            perm = self.perm[1:5]
            new_perm = []
    
            for n, side in enumerate(perm):
                next_side = (n + turn) % 4
                new_perm.append(perm[next_side][:layer] + perm[n][layer:])
    
            self.perm[[1, 2, 3, 4]] = new_perm
            self._rotate(0, length=2 * turn)


    def turn_left(self, ttype, dl=False):
        '''
        Turns the left face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        dl - (optional) Whether to perform a double layer turn
        '''
        if dl:
            self.turn_right(ttype)
            self.rotate_x(ttype == -1, ttype == 2)
        else:
            self.rotate_z()
            self.turn_up(ttype, dl)
            self.rotate_z(cw=False)


    def turn_front(self, ttype, dl=False):
        '''
        Turns the front face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        dl - (optional) Whether to perform a double layer turn
        '''
        if dl:
            self.turn_back(ttype)
            self.rotate_z(ttype == 1, ttype == 2)
        else:
            self.rotate_x()
            self.turn_up(ttype, dl)
            self.rotate_x(cw=False)


    def turn_right(self, ttype, dl=False):
        '''
        Turns the right face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        dl - (optional) Whether to perform a double layer turn
        '''
        if dl:
            self.turn_left(ttype)
            self.rotate_x(ttype == 1, ttype == 2)
        else:
            self.rotate_z(cw=False)
            self.turn_up(ttype, dl)
            self.rotate_z()


    def turn_back(self, ttype, dl=False):
        '''
        Turns the back face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        dl - (optional) Whether to perform a double layer turn
        '''
        if dl:
            self.turn_front(ttype)
            self.rotate_z(ttype == -1, ttype == 2)
        else:
            self.rotate_x(cw=False)
            self.turn_up(ttype, dl)
            self.rotate_x()


    def turn_down(self, ttype, dl=False):
        '''
        Turns the down face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        dl - (optional) Whether to perform a double layer turn
        '''
        if dl:
            self.turn_up(ttype)
            self.rotate_y(ttype == -1, ttype == 2)
        else:
            self.rotate_x(dt=True)
            self.turn_up(ttype, dl)
            self.rotate_x(dt=True)


    def turn_middle(self, ttype, axis='m'):
        '''
        Turns the middle slice on the z axis of the cube depending on ttype.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        '''
        if axis == 'm':
            if ttype in [1, 'cw']:
                self.turn_right('cw')
                self.turn_left('ccw')
                self.rotate_x(cw=False)
            elif ttype in [-1, 'ccw']:
                self.turn_right('ccw')
                self.turn_left('cw')
                self.rotate_x()
            elif ttype in [2, 'dt']:
                self.turn_right('dt')
                self.turn_left('dt')
                self.rotate_x(dt=True)


    def rotate_x(self, cw=True, dt=False):
        '''
        Rotates the cube with an x move. This is equivalent to the R turn.
        
        Parameters:
        cw - (optional) Whether to do a clockwise rotation or, if cw=False, a
             counterclockwise rotation
        dt - (optional) If dt=True, the cube will have a double turn rotation
             applied.
        '''
        if dt:
            self.perm = self.perm[[5, 1, 4, 3, 2, 0]]
            self._rotate(1, 2, 3, 4, length=4)
        elif cw:
            self.perm = self.perm[[2, 1, 5, 3, 0, 4]]
            self._rotate(1, length=-2)
            self._rotate(3, length=2)
            self._rotate(4, 5, length=4)
        else:
            self.perm = self.perm[[4, 1, 0, 3, 5, 2]]
            self._rotate(1, length=2)
            self._rotate(3, length=-2)
            self._rotate(0, 4, length=4)


    def rotate_y(self, cw=True, dt=False):
        '''
        Rotates the cube with an y move. This is equivalent to the U turn.
        
        Parameters:
        cw - (optional) Whether to do a clockwise rotation or, if cw=False, a
             counterclockwise rotation
        dt - (optional) If dt=True, the cube will have a double turn rotation
             applied.
        '''
        if dt:
            self.perm = self.perm[[0, 3, 4, 1, 2, 5]]
            self._rotate(0, 5, length=4)
        elif cw:
            self.perm = self.perm[[0, 2, 3, 4, 1, 5]]
            self._rotate(0, length=2)
            self._rotate(5, length=-2)
        else:
            self.perm = self.perm[[0, 4, 1, 2, 3, 5]]
            self._rotate(0, length=-2)
            self._rotate(5, length=2)


    def rotate_z(self, cw=True, dt=False):
        '''
        Rotates the cube with an z move. This is equivalent to the F turn.
        
        Parameters:
        cw - (optional) Whether to do a clockwise rotation or, if cw=False, a
             counterclockwise rotation
        dt - (optional) If dt=True, the cube will have a double turn rotation
             applied.
        '''
        if dt:
            self.perm = self.perm[[5, 3, 2, 1, 4, 0]]
            self._rotate(0, 1, 2, 3, 4, 5, length=4)
        elif cw:
            self.perm = self.perm[[1, 5, 2, 0, 4, 3]]
            self._rotate(0, 1, 2, 3, 5, length=2)
            self._rotate(4, length=-2)
        else:
            self.perm = self.perm[[3, 0, 2, 5, 4, 1]]
            self._rotate(0, 1, 2, 3, 5, length=-2)
            self._rotate(4, length=2)


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
            method = turn_dict[turn]
            getattr(self, method[0])(method[1], method[2])