from cube import Cube


class Solver(Cube):
    def __init__(self, perm=0):
        Cube.__init__(self)
        if perm != 0:
            self.perm = perm

        self.solving_alg = ''

    def rotate_x(self, cw=True, dt=False):
        Cube.rotate_x(self, cw, dt)
        if dt:
            self.solving_alg += "x2"
        elif cw:
            self.solving_alg += "x"
        else:
            self.solving_alg += "x'"