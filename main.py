import numpy as np
import matplotlib.pyplot as plt

from solver import Solver
from cube import Cube
from cross import Cross
from algorithms.tools import code_to_alg, alg_output, dict_to_list
from datetime import datetime as dt


def main(perm=0, scramble='No scramble given.'):
    if perm == 0:
        # Create a randomly scrambled cube
        scramble = ''.join(np.random.choice(list('UT!LK@FE#RQ$BA%DC^xyz'), 20))

        scrambled_cube = Solver()
        scrambled_cube.apply_alg(''.join(scramble))

        perm = dict_to_list(scrambled_cube.perm)
        print('Use:\n{}\n'.format(alg_output(code_to_alg(scramble))))
        print('Start with:\n{}\n'.format(perm))
    else:
        print('Use:\n{}\n'.format(scramble))
        print('Start with:\n{}\n'.format(perm))

    cube = Solver(perm)
    cross_list = []

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

            # Print stuff
            alg_len = len(cube.cross_alg)
            cross_list.append([alg_len, (t1 - t0).total_seconds() * 1000])

            print('Solving for {} face took '.format(cross_center) +
                  '{:>7.3f} ms and is {:>2} turns long:'.format(
                          (t1 - t0).total_seconds() * 1000, alg_len))
            print('Algorithm: {}\n'.format(
                    alg_output(code_to_alg(cube.solving_alg))))

    # Print more stuff
    cross_list = np.array(cross_list)
    turn_len_avg = np.average(cross_list[:, 0])
    time_avg = np.average(cross_list[:, 1])

    print('Average turn length:    {:.3f} turns'.format(turn_len_avg))
    print('Average time for cross: {:.3f} ms'.format(time_avg))


def graph_time(n):
    iterations, time = [], []

    for i in range(n):
        scramble = ''.join(np.random.choice(list('UT!LK@FE#RQ$BA%DC^xyz'), 20))

        scrambled_cube = Cube()
        scrambled_cube.apply_alg(''.join(scramble))

        cross = Cross(scrambled_cube.perm)

        iterations.append(cross.iterations)
        time.append(cross.tot_ms)

    plt.figure()
    plt.scatter(iterations, time)
    plt.xlabel('Iterations')
    plt.ylabel('Time (ms)')
    plt.xlim(0, max(iterations) * 1.1)
    plt.ylim(0, max(time) * 1.1)
    plt.show()

    return iterations, time


if __name__ == "__main__":
    p = ['bbrgoogyg', 'owwoyoggr', 'obobgwwoo',
         'ygyrwbbyg', 'brywbyrrr', 'bwwrrgwyy']
    s = "z L2 R2 U' D' R' U2 D B2 R2 D' R' F B'"
    main(p, s)
    # main()
'''
t0 = dt.now()
while not cube.step == 'finished':
    cube.solve_it()
t1 = dt.now()
'''
