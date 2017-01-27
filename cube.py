import numpy as np
from collections import deque

class Cube():
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


    def turn_up(self, cw=False, ccw=False, dt=False, fs=False):
        if cw + ccw + dt != 1:
            print('cw = %s, ccw = %s and dt = %s. Only one can have a truth value.'
                  % (cw, ccw, dt))

        turn = cw + 2 * dt - ccw
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=turn)


    def turn_left(self, cw=False, ccw=False, dt=False, fs=False):
        self.rotate_z()

        if cw + ccw + dt != 1:
            print('cw = %s, ccw = %s and dt = %s. Only one can have a truth value.'
                  % (cw, ccw, dt))

        turn = cw + 2 * dt - ccw
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_z(cw=False)


    def turn_front(self, cw=False, ccw=False, dt=False, fs=False):
        self.rotate_x()

        if cw + ccw + dt != 1:
            print('cw = %s, ccw = %s and dt = %s. Only one can have a truth value.'
                  % (cw, ccw, dt))

        turn = cw + 2 * dt - ccw
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_x(cw=False)


    def turn_right(self, cw=False, ccw=False, dt=False, fs=False):
        self.rotate_z(cw=False)

        if cw + ccw + dt != 1:
            print('cw = %s, ccw = %s and dt = %s. Only one can have a truth value.'
                  % (cw, ccw, dt))

        turn = cw + 2 * dt - ccw
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []
        print(self.perm)
        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)
        print(self.perm)
        self.rotate_z()


    def turn_back(self, cw=False, ccw=False, dt=False, fs=False):
        self.rotate_x(cw=False)

        if cw + ccw + dt != 1:
            print('cw = %s, ccw = %s and dt = %s. Only one can have a truth value.'
                  % (cw, ccw, dt))

        turn = cw + 2 * dt - ccw
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_x()

    def turn_down(self, cw=False, ccw=False, dt=False, fs=False):
        self.rotate_x(dt=True)

        if cw + ccw + dt != 1:
            print('cw = %s, ccw = %s and dt = %s. Only one can have a truth value.'
                  % (cw, ccw, dt))

        turn = cw + 2 * dt - ccw
        layer = 3 + 2*fs
        perm_temp = self.perm[[1, 2, 3, 4]]
        new_perm = []

        for n, side in enumerate(perm_temp):
            new_perm.append(perm_temp[(n + turn) % 4][:layer] + perm_temp[n][layer:])

        self.perm[[1, 2, 3, 4]] = new_perm
        self._rotate(0, length=2 * turn)

        self.rotate_x(dt=True)


    def rotate_x(self, cw=True, dt=False):
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