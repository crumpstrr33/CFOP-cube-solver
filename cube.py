import numpy as np
from collections import deque


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
    def __init__(self, perm=0):
        if perm == 0:
            self.perm = np.array(['wwwwwwww', 'oooooooo', 'gggggggg',
                         'rrrrrrrr', 'bbbbbbbb', 'yyyyyyyy'])
        else:
            self.perm = np.array(perm)


    def _rotate(self, *sides, length):
        for side in sides:
            deque_side = deque(self.perm[side])
            deque_side.rotate(length)
            self.perm[side] = ''.join(deque_side)


    def turn_up(self, ttype, fs=False):
        '''
        Turns the up face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        fs - (optional) Whether to perform a fat slice (i.e. a turn of two
             layers of the cube rather than one)
        '''
        turn = (ttype == 'cw') - (ttype == 'ccw') + 2 * (ttype == 'dt')
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)


    def turn_left(self, ttype, fs=False):
        '''
        Turns the left face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        fs - (optional) Whether to perform a fat slice (i.e. a turn of two
             layers of the cube rather than one)
        '''
        self.rotate_z()

        turn = (ttype == 'cw') - (ttype == 'ccw') + 2 * (ttype == 'dt')
        if turn not in [-1, 1, 2]:
            print('ttype = %s, turn amount is %d which is not allowed.'
                  % (ttype, turn))

        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_z(cw=False)


    def turn_front(self, ttype, fs=False):
        '''
        Turns the front face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        fs - (optional) Whether to perform a fat slice (i.e. a turn of two
             layers of the cube rather than one)
        '''
        self.rotate_x()

        turn = (ttype == 'cw') - (ttype == 'ccw') + 2 * (ttype == 'dt')
        if turn not in [-1, 1, 2]:
            print('ttype = %s, turn amount is %d which is not allowed.'
                  % (ttype, turn))

        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_x(cw=False)


    def turn_right(self, ttype, fs=False):
        '''
        Turns the right face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        fs - (optional) Whether to perform a fat slice (i.e. a turn of two
             layers of the cube rather than one)
        '''
        self.rotate_z(cw=False)

        turn = (ttype == 'cw') - (ttype == 'ccw') + 2 * (ttype == 'dt')
        if turn not in [-1, 1, 2]:
            print('ttype = %s, turn amount is %d which is not allowed.'
                  % (ttype, turn))

        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_z()


    def turn_back(self, ttype, fs=False):
        '''
        Turns the back face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        fs - (optional) Whether to perform a fat slice (i.e. a turn of two
             layers of the cube rather than one)
        '''
        self.rotate_x(cw=False)

        turn = (ttype == 'cw') - (ttype == 'ccw') + 2 * (ttype == 'dt')
        if turn not in [-1, 1, 2]:
            print('ttype = %s, turn amount is %d which is not allowed.'
                  % (ttype, turn))

        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_x()

    def turn_down(self, ttype, fs=False):
        '''
        Turns the down face of the cube depending on the args.
        
        Parameters:
        ttype - The turn type. For a clockwise turn, use 'cw' or 1. For a 
                counterclockwise turn, use 'ccw' or -1. And for a double turn,
                use 'dt' or 2. The number represents the number of clockwise
                turns that will be applied
        fs - (optional) Whether to perform a fat slice (i.e. a turn of two
             layers of the cube rather than one)
        '''
        self.rotate_x(dt=True)

        turn = (ttype == 'cw') - (ttype == 'ccw') + 2 * (ttype == 'dt')
        if turn not in [-1, 1, 2]:
            print('ttype = %s, turn amount is %d which is not allowed.'
                  % (ttype, turn))

        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

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