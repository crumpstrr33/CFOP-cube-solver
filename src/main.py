import numpy as np
from datetime import datetime as dt

from solver import Solver
from cube import Cube
import algorithms.tools as tl


def main(perm):
    cube = Solver(perm)
    n = 0
    lens, times, = np.empty(6), np.empty(6)
    opens, closeds = np.empty(6), np.empty(6)

    rotations = {(0, 0, -1): "x",  (0, 0, 1): "X", (0, -1, 0):  "",
                 (0, 1,  0): "8", (-1, 0, 0): "Z", (1,  0, 0): "z"}

    # Iterate through the six sides
    for coord, colors in cube.perm.items():
        if coord.count(0) == 2:
            t0 = dt.now()
            cube = Solver(perm)

            # Find the rotation
            inspection = rotations[coord]
            cube.apply_alg(inspection)
            cross_center = ''.join(''.join(colors))

            # Solve cross
            cube.solve_cross()
            t1 = dt.now()

            alg_len = len(tl.alg_to_code(cube.cross_alg))
            tot_time = (t1 - t0).total_seconds() * 1000

            lens[n] = alg_len
            times[n] = tot_time
            opens[n] = cube.open_sets
            closeds[n] = cube.closed_sets

            # Print stuff
            print('Solving for {} face took '.format(cross_center) +
                  '{:.3f} ms and is {} turns long:'.format(tot_time, alg_len))
            print('Algorithm: {}'.format(
                    tl.code_to_alg(cube.solving_alg)))
            print('Number of open/closed sets: ' +
                  '{}/{}\n'.format(cube.open_sets, cube.closed_sets))

            n += 1

    # Print more stuff
    len_avg = np.average(lens)
    time_avg = np.average(times)
    open_avg = np.average(opens)
    closed_avg = np.average(closeds)

    print('Average turn length:    {:.3f} turns'.format(len_avg))
    print('Average time for cross: {:.3f} ms'.format(time_avg))
    print('Average number of open/closed sets: {:.0f}/{:.0f}'.format(
            open_avg, closed_avg))

if __name__ == "__main__":
    scramble = tl.random_scramble(20)
    cube = Cube()
    cube.apply_alg(scramble)
    perm = tl.dict_to_list(cube.perm)

    print('Use:\n{}\n'.format(tl.code_to_alg(scramble)))
    print('Start with:\n{}\n'.format(perm))

    main(perm)
