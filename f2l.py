from collections import deque
from operator import add
import itertools

from algorithms.alg_dicts import TURN_DICT, PARAM_DICT
from algorithms.tools import code_to_alg

scramble = "R2 D B2 U L2 F2 D2 L2 F2 D' U L' D' B' D U B2 L2 F' L' B2"


class F2L:

    def __init__(self, perm, f2l_order):
        self.perm = {tuple(color): coord for coord, color in perm.items()}
        self.f2l_order = f2l_order

        self.alg = []
        self.d_color = ''.join(perm[(0, -1, 0)])
        self.u_color = ''.join(perm[(0, 1, 0)])
        # The 6 centers of the cube
        self.centers = self._centers()
        # The 4 solved cross edges
        self.cross = self._cross()
        # The permutation of the 12 relevant cubies before any moves
        self.abs_init_perm = self._abs_init_perm()
        self.abs_init_perm.update(self.cross)
        # The permutation to reach for each f2l pair
        self.goal_perm = self.cross.copy()
        # The initial permutation for each f2l pair
        self.init_perm = self.cross.copy()

        for f2l_pair in self.f2l_order:
            # Inital state before F2L
            self.init_perm.update(self._init_f2l_pair(f2l_pair))

            # Find correct permutation of current f2l pair
            self.goal_perm.update(self._goal_f2l_pair(f2l_pair))

            print('Solving for:', f2l_pair)
            if False:  # 'r' in f2l_pair:
                print('INIT_PERM')
                print(self.init_perm)
                print('GOAL_PERM')
                print(self.goal_perm, flush=True)

            alg, next_f2l_perm = self._find_path()
            self.alg.append(alg)
            self.init_perm = next_f2l_perm

    def _centers(self):
        centers = {}

        for color, coord in self.perm.items():
            # Two zeros means it's a center
            if coord.count(0) == 2:
                centers[color] = coord

        return centers

    def _cross(self):
        cross = {}
        for color, coord in self.perm.items():
            if coord.count(0) == 1 and self.d_color in color:
                cross[color] = coord

        return cross

    def _abs_init_perm(self):
        init_perm = {}

        # Find corners
        for color, coord in self.perm.items():
            # Make sure it's a corner piece
            if 0 not in coord:
                # Make sure it's a piece of the down face
                if self.d_color in color:
                    init_perm[color] = coord

        # Find middle edges
        for color, coord in self.perm.items():
            # Make sure it's an edge piece
            if coord.count(0) == 1:
                # Make sure it's not on the up or down face
                if self.d_color not in color and self.u_color not in color:
                    init_perm[color] = coord

        return init_perm

    def _init_f2l_pair(self, corner_colors):
        init_f2l_pair = {}
        edge_colors = ''.join(corner_colors).replace(self.d_color, '')

        for color, coord in self.abs_init_perm.items():
            if edge_colors[0] in color and edge_colors[1] in color:
                if self.u_color not in color:
                    init_f2l_pair[color] = coord

        return init_f2l_pair

    def _goal_f2l_pair(self, f2l_pair):
        corner_coord, corner_color = (0, 0, 0), ['', '', '']

        for color, coord in self.centers.items():
            sticker = ''.join(color)

            # Find correct position and color order based on where centers are
            if ''.join(color) in f2l_pair:
                corner_coord = tuple((map(add, corner_coord, coord)))
                corner_color[color.index(sticker)] = sticker

        corner_color = tuple(corner_color)
        edge_color = (corner_color[0], '', corner_color[2])
        edge_coord = (corner_coord[0], 0, corner_coord[2])
        goal_coord = {corner_color: corner_coord, edge_color: edge_coord}

        return goal_coord

    def _find_path(self):
        fn = F2LNode(self.init_perm, self.goal_perm, '', self.d_color)

        # Every single layer face turn
        turn_space = 'UT!LK@FE#RQ$BA%DC^'
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
            closed_set.append(current.f2l_perm)

            # Return if perm is equal to goal perm
            if not current.h_cost:
                print('Open/Closed sets: {}/{}'.format(
                                    len(self.open_set), len(closed_set)))
                print('Alg is:', code_to_alg(current.alg))
                print('----------------------------', flush=True)
                return current.alg, current.f2l_perm

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

    def __init__(self, f2l_perm, goal_perm, alg, d_color):
        # Constant for every F2LNode object
        self.goal_perm = goal_perm
        self.d_color = d_color

        # Constant for each F2LNode object
        self.f2l_perm = f2l_perm
        self.alg = alg

        # Metrics
        self.flip_penalty = 1 * self._flip_penalty()
        self.g_cost = 2 * len(self.alg)
        self.h_cost = self._metric() + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _flip_penalty(self):
        bad_flip = 0

        for colors, coord in self.f2l_perm.items():
            # Check F2L edge piece
            if coord[1] == 0 and self.d_color not in colors:
                # Edge piece is flipped
                if colors not in self.goal_perm:
                    bad_flip += 1
            # Check F2L corner piece
            if coord[1] == -1 and self.d_color in colors:
                if colors[1] != self.d_color:
                    bad_flip += 1

        return bad_flip

    def _metric(self):
        tot_distance = 0

        for color, coord in self.f2l_perm.items():
            for color_rand in itertools.permutations(color):
                try:
                    distance = sum(map(lambda x, y: abs(x - y),
                                       coord, self.goal_perm[color_rand]))
                    tot_distance += distance
                    break
                except:
                    pass

        return tot_distance

    def _turn_rotate(self, ttype, side):
        # Get the right parameters for the cubie rotation
        p = PARAM_DICT[ttype][side]
        new_perm = {}

        for color, coord in self.f2l_perm.items():
            if coord[p[0]] == p[1]:
                new_perm[(color[p[3]], color[p[5]], color[p[7]])] = \
                         (p[2] * coord[p[3]],
                          p[4] * coord[p[5]],
                          p[6] * coord[p[7]])
            else:
                new_perm[color] = coord

        return new_perm

    def apply_turn(self, turn):
        return self._turn_rotate(*TURN_DICT[turn])
