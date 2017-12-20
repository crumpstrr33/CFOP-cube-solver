import numpy as np
from datetime import datetime as dt

from solver import Solver
from cube import Cube
import algorithms.tools as tl


def analyze_cross(perm):
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
    print('Average branching factor: {:.3f}'.format(open_avg/closed_avg + 1))


def analyze_f2l(perm):
    cube = Solver(perm)

    cube.solve_cross()
    print('Cross solved with: {}\n'.format(cube.cross_alg))

    t0 = dt.now()
    cube.solve_f2l()
    t1 = dt.now()

    for alg in range(len(cube.f2l_alg)):
        print("F2L Pair '{}' is {} turns long:".format(
                cube.f2l_pairs[alg], len(cube.falg[alg])))
        print('Algorithm: {}'.format(cube.f2l_alg[alg]))
        print('Number of open/closed sets: ' +
              '{}/{}\n'.format(cube.open_setss[alg], cube.closed_setss[alg]))

    len_avg = np.average([len(alg) for alg in cube.falg])
    tot_time = (t1 - t0).total_seconds()
    print('Average turn length: {:.3f} turns'.format(len_avg))
    print('Total time for F2L: {:.3f} ms'.format(tot_time * 1000))
    print('Average number of open/closed sets: {:.0f}/{:.0f}'.format(
        np.average(cube.open_setss), np.average(cube.closed_setss)))
    print('Average branching factor: {:.3f}'.format(
        np.average(cube.open_setss) / np.average(cube.closed_setss) + 1))


if __name__ == "__main__":
    #scramble = tl.random_scramble(20)

    # Takes ~27s, 7/7/13/11 (1009/362/1858/1348) [9.50, 1144]
    # Takes ~4s, 7/8/6/8 (414/609/421/344) [7.25, 447] w/o pair_metric
    #scramble = 'URKAF!DFCE%T%KBQTLT^'

    # Takes ~8s, 6/8/12/8 (122/855/1011/291) [8.50, 570]
    # Takes ~6s, 8/8/5/8 (1038/423/301/361) [7.25, 531] w/o pair_metric
    #scramble = 'QF!@!FUK!^LR!%QUDL#K'

    # Takes ~27s, 7/7/13/11 (1009/362/1858/1348) [9.50, 1144]
    # Takes ~4s, 7/8/6/8 (414/609/421/344) [7.25, 447] w/o pair_metric
    #scramble = 'URKAF!DFCE%T%KBQTLT^'

    # Takes ~78s, 10/4/9/7 (4082/6/1088/212)  [7.50, 1347]
    # Takes ~ 4s, 8/7/7/8 (147/508/710/395) [7.50, 440] w/o pair_metric
    #scramble = '^@AU#DTKBK#R@DUR%QAK'

    # Takes ~6s, 9/10/8/9 (415/1193/91/329) [9.00, 507]
    # Takes ~150s, 8/9/8/6 (1367/5093/1404/140) [7.75, 2001] w/o pair_metric
    #scramble = 'QLFCER@E%QD$LE@CUKTA'

    # Takes ~15s, 8/8/12/10 (1743/351/674/464) [9.50, 808]
    # Takes ~4s, 6/7/9/7 (346/525/553/183) [7.25, 402] w/o pair_metric
    scramble = '@Q!^BL%FRDQK^A#$FUK$'

    # Takes ~3s, 7/10/6/6 (654/620/238/82) [7.25, 398]
    # Takes ~8s, 7/9/6/7 (860/873/560/180) [7.25, 618] w/o pair_metric
    #scramble = 'TFT%LAT@#LAQU@!RFRU@'
    cube = Cube()
    cube.apply_alg(scramble)
    perm = tl.dict_to_list(cube.perm)

    print('Use:\n{}\n'.format(tl.code_to_alg(scramble)))
    print('Start with:\n{}\n'.format(perm))

    analyze_cross(perm)
    #analyze_f2l(perm)