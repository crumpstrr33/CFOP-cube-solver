from collections import deque
from operator import add
from itertools import permutations

from algorithms.alg_dicts import TURN_DICT, PARAM_DICT
from algorithms.tools import code_to_alg

'''
def print_dict(d):
    for stickers, cordlor in d.items():
        print('{:<29}: ({:>2}, {:>2}, {:>2}) ({:<1}, {:<1}, {:<1})'.format(
              ', '.join(stickers), *cordlor[0], *cordlor[1]))
'''


class F2L:

    def __init__(self, perm, f2l_pair):
        self.perm = {self._sticker_val(color): (list(coord), color)
                     for coord, color in perm.items()}

        self.d_color = ''.join(perm[(0, -1, 0)])
        self.u_color = ''.join(perm[(0, 1, 0)])

        self.centers = self._centers()
        self.cross = self._cross()

        self.init_perm = self._init_perm(f2l_pair)
        self.goal_perm = self._goal_perm(f2l_pair)

        self.alg = self._find_path()

    @staticmethod
    def _sticker_val(color):
        """
        Creates the correct form the for the value of the dicts used in this
        class which is a frozenset of strings representing all the
        permutations of the stickers of the cubie. It either has 6 (corner)
        elements, 2 (edge) elements or 1 (center) elements.

        Parameters:
        color - The 3-element list of the color of a cubie
                (e.g. ['o', 'y', ''])
        """
        return frozenset(map(lambda x: ''.join(x), permutations(color)))

    def _centers(self):
        """
        Returns a dict of the 6 centers
        """
        colors = ['w', 'o', 'g', 'r', 'b', 'y']
        centers = {}

        for color in colors:
            stickers = frozenset(color)
            centers[stickers] = self.perm[stickers]

        return centers

    def _cross(self):
        """
        Returns a dict of the 4 cross edges
        """
        colors = ['w', 'o', 'g', 'r', 'b', 'y']
        colors.remove(self.d_color)
        colors.remove(self.u_color)
        cross = {}

        for color in colors:
            stickers = frozenset((color + self.d_color, self.d_color + color))
            cross[stickers] = self.perm[stickers]

        return cross

    def _init_perm(self, f2l_pair):
        """
        Returns a dict of the 4 cross edges and an F2L pair's current position

        Parameters:
        f2l_pair - F2L pair to add in the form of a 2 char string
                   (e.g. 'br' for the blue-red F2L pair)
        """
        init_perm = self.cross.copy()
        edge_val = self._sticker_val(f2l_pair)
        corner_val = self._sticker_val(f2l_pair + self.d_color)

        init_perm[edge_val] = self.perm[edge_val]
        init_perm[corner_val] = self.perm[corner_val]

        return init_perm

    def _goal_perm(self, f2l_pair):
        """
        Returns a dict of the 4 cross edges and an F2L pair's solved position

        Parameters:
        f2l_pair - F2L pair to add in the form of a 2 char string
                   (e.g. 'br' for the blue-red F2L pair)
        """
        edge_val = self._sticker_val(f2l_pair)
        corner_val = self._sticker_val(f2l_pair + self.d_color)

        pair_centers = (self.centers[frozenset(f2l_pair[0])],
                        self.centers[frozenset(f2l_pair[1])])
        goal_perm = self.init_perm.copy()

        edge_coord = list(map(add, pair_centers[0][0], pair_centers[1][0]))
        edge_color = list(map(add, pair_centers[0][1], pair_centers[1][1]))

        solved_entries = {}
        solved_entries[edge_val] = (edge_coord, edge_color)

        corner_coord = list(map(add, edge_coord, [0, -1, 0]))
        corner_color = list(map(add, edge_color, ['', self.d_color, '']))
        solved_entries[corner_val] = (corner_coord, corner_color)

        goal_perm.update(solved_entries)

        return goal_perm

    def _find_path(self):
        """
        Completes A* pathfinding for the current F2L pair
        """
        fn = F2LNode(self.init_perm, self.goal_perm, '', self.d_color)

        # Every single layer face turn
        turn_space = 'UT!LK@FE#RQ$BA%' #'UT!LK@FE#RQ$BA%DC^'
        self.open_set = deque([fn])
        closed_set = []

        while True:
            # Take object with lowest f_cost
            current = self.open_set[0]

            # Find current turn_space
            if current.alg != '':
                turn = current.alg[-1]

                last = turn_space.index(turn)
                no_turn = last - (last % 3)
                turn_space_current = (turn_space[:no_turn] +
                                      turn_space[no_turn + 3:])

                # Remove half of the mirror moves (e.g. RL = LR and so on)
                if turn in 'UT!':
                    turn_space_current = \
                        turn_space_current.replace('DC^', '')
                elif turn in 'LK@':
                    turn_space_current = \
                        turn_space_current.replace('RQ$', '')
                elif turn in 'FE#':
                    turn_space_current = \
                        turn_space_current.replace('BA%', '')
            else:
                turn_space_current = turn_space

            # Remove from open set
            self.open_set.remove(current)
            # Move last node to top of tree
            self.open_set.rotate()
            # Compare it downwards
            self._move_down()
            # Add to closed set
            closed_set.append(current.cur_perm)

            # Return if perm is equal to goal perm
            if not current.h_cost:
                print('Open/Closed sets: {}/{}'.format(
                                    len(self.open_set), len(closed_set)))
                print('Alg is:', code_to_alg(current.alg))
                print('----------------------------', flush=True)
                return current.alg

            # Create new objects and put in open_set to
            # check next if perm hasn't already been found
            for turn in turn_space_current:
                new_perm = current.apply_turn(turn)
                new_alg = current.alg + turn

                if new_perm in closed_set:
                    continue

                fn = F2LNode(new_perm, self.goal_perm, new_alg, self.d_color)
                self._move_up(fn)

    def _move_up(self, fn):
        """
        Appends fn to the end of open_set and move it up the heap.
        """
        self.open_set.append(fn)

        while True:
            # Node info, compare f_cost and h_cost at the same time
            fn_ind = self.open_set.index(fn)
            fn_val = fn.f_cost + fn.h_cost/100

            # If index is 0, can't move up anymore
            if not fn_ind:
                return

            # The position above node n is int half of (n - 1)
            fn_up_ind = (fn_ind - 1) // 2
            fn_up = self.open_set[fn_up_ind]
            fn_up_val = fn_up.f_cost + fn_up.h_cost/100

            # Compare values
            if fn_val < fn_up_val:
                self._swap(fn_ind, fn_up_ind)
            else:
                return

    def _move_down(self):
        """
        Sorts the top node down the heap.
        """
        set_len = len(self.open_set)

        # Don't run if open_set is empty
        if not set_len:
            return

        # Compare both f_cost and h_cost at same time
        fn = self.open_set[0]
        fn_val = fn.f_cost + fn.h_cost/100

        while True:
            fn_ind = self.open_set.index(fn)

            # Get info for left lower node, make sure we don't go over index
            if set_len > 2 * fn_ind + 1:
                fn_ld_ind = 2 * fn_ind + 1
                fn_ld = self.open_set[fn_ld_ind]
                fn_ld_val = fn_ld.f_cost + fn_ld.h_cost/100
                diff_ld = fn_val - fn_ld_val
            # We reached botom of tree if it doesn't exist
            else:
                return

            # Get info for right lower node
            if set_len > fn_ld_ind + 1:
                right_node_exists = True

                fn_rd_ind = fn_ld_ind + 1
                fn_rd = self.open_set[fn_rd_ind]
                fn_rd_val = fn_rd.f_cost + fn_rd.h_cost/100
                diff_rd = fn_val - fn_rd_val
            # We reached end of list if it doesn't exist
            else:
                right_node_exists = False

            # Swap with left lower node due to f_cost
            if diff_ld >= 1:
                self._swap(fn_ind, fn_ld_ind)
            # Swap with right lower node due to f_cost
            elif right_node_exists and diff_rd >= 1:
                self._swap(fn_ind, fn_rd_ind)
            # Swap with left lower node due to h_cost
            elif diff_ld > 0:
                self._swap(fn_ind, fn_ld_ind)
            # Swap with right lower node due to h_cost
            elif right_node_exists and diff_rd > 0:
                self._swap(fn_ind, fn_ld_ind)
            else:
                return

    def _swap(self, i, j):
        """
        Swaps elements at i and j in open_set
        """
        self.open_set[i], self.open_set[j] = self.open_set[j], self.open_set[i]


class F2LNode:

    def __init__(self, cur_perm, goal_perm, alg, d_color):
        # Constant for every F2LNode object
        self.goal_perm = goal_perm
        self.d_color = d_color

        # Constant for each F2LNode object
        self.cur_perm = cur_perm
        self.alg = alg

        # Metrics
        self.flip_penalty = 1 * self._flip_penalty()
        self.g_cost = 2 * len(self.alg)
        self.h_cost = self._metric() + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _flip_penalty(self):
        return 0

    def _metric(self):
        """
        Sums the difference of each coordinate dimension
        """
        tot_distance = 0

        for stickers, cordlor in self.cur_perm.items():
            distance = sum(map(lambda x, y: abs(x - y),
                               cordlor[0], self.goal_perm[stickers][0]))
            tot_distance += distance

        return tot_distance

    def _turn_rotate(self, ttype, side):
        """
        Applies a turn to analgous to the Cube class method. Here, a new dict
        is returned instead of updating current perm.
        """
        # Get the right parameters for the cubie rotation
        p = PARAM_DICT[ttype][side]
        new_perm = {}

        for stickers, cordlor in self.cur_perm.items():
            coord, color = cordlor[0], cordlor[1]
            if coord[p[0]] == p[1]:
                new_perm[stickers] = ((p[2] * coord[p[3]],
                                       p[4] * coord[p[5]],
                                       p[6] * coord[p[7]]),
                                      [color[p[3]], color[p[5]], color[p[7]]])
            else:
                new_perm[stickers] = cordlor

        return new_perm

    def apply_turn(self, turn):
        """
        Analgous to Cube class method except only works for one turn at a time.
        """
        return self._turn_rotate(*TURN_DICT[turn])
