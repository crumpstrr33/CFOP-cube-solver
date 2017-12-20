"""
Contains the Cross class along with the CrossNode class used to find the
cross algorithm via A* pathfinding.
"""
from collections import deque

from cfop.algorithms.alg_dicts import TURN_DICT, PARAM_DICT

# So... looking good. Still some problems. Don't want to arbitrarilty restrict
# it with the 9 move cutoff.

# A FP of 2 makes sense because a bad flipped edge can be thought of as being
# one quarter turn away from a good flipped edge (and one quarter turn has a
# metric here of 2)

# Having a weight for the alg length seems arbitrary and messy if it's left up
# to me choosing one. Having no weight (i.e. a weight of 1) seems to work, so
# I'll keep it for now.


class Cross:
    """
    This class solves the cross on the Down face for a given permutation.

    It solves it using an A* pathfinding algorithm where each new node is a
    CrossNode object. The list containing the nodes is sorted via a
    breadth-first binary tree where new nodes are appended and sorted up the
    tree since only the node with the lowest metric is needed.

    There is an artificial cutoff at 11 moves. Since over 11 moves are always
    superfluous for a cross.

    Parameters:
    perm - The full permutation of the cube in its dict form
    """

    def __init__(self, perm):
        self.perm = perm

        self.d_color = ''.join(self.perm[(0, -1, 0)])
        self.init_perm = self._init_perm()
        self.solved_perm = self._solved_perm()
        self.solved_side_colors = self._solved_side_colors()

        self.alg, self.open_sets, self.closed_sets = self._find_path()

    def _init_perm(self):
        """
        Finds the current position of the cross edges by
        color and coordinates
        """
        cross_edges = {}

        for coord, colors in self.perm.items():
            # Look at edge pieces with d_color color
            if coord.count(0) == 1 and self.d_color in colors:
                cross_edges[coord] = colors

        return cross_edges

    def _solved_perm(self):
        """
        Finds the solved position of the cross edges by color
        """
        center_dict = {}
        # Find side center colors
        for coord, color in self.perm.items():
            # Look only at centers
            if coord.count(0) == 2:
                # Don't look at Up or Down centers
                if coord[1] == 0:
                    center_dict[''.join(color)] = coord

        # Dict with (k, v) = (non-white color, coordinate)
        solved_perm = {}
        for color, coord in center_dict.items():
            solved_perm[color] = (coord[0], -1, coord[2])

        return solved_perm

    def _solved_side_colors(self):
        """
        Finds side center colors in the order: F R B L
        """
        # The order wanted
        order = [(0, -1, 1), (1, -1, 0), (0, -1, -1), (-1, -1, 0)]
        side_colors = []

        for n in range(4):
            for color, coord in self.solved_perm.items():
                if coord == order[n]:
                    side_colors.append(color)

        return side_colors

    def _find_path(self):
        """
        A* pathfinding algorithm to solve for the cube's cross.
        """
        cn = CrossNode(self.init_perm, '', self.solved_perm,
                       self.d_color, self.solved_side_colors)

        # Every single layer face turn
        turn_space = 'UT!LK@FE#RQ$BA%DC^'
        self.open_set = deque([cn])
        closed_set = []

        while True:
            # Take object with lowest f_cost
            current = self.open_set[0]

            # Find current turn_space
            if current.alg:
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
            closed_set.append(current.edge_perm)

            # Return if perm is equal to solved perm
            if not current.abs_h_cost:
                return current.alg, len(self.open_set), len(closed_set)

            # Create new objects and put in open_set to
            # check next if perm hasn't already been found
            new_alg_len = len(current.alg) + 1
            for turn in turn_space_current:
                new_perm = current.apply_turn(turn)
                new_alg = current.alg + turn

                if new_perm in closed_set or new_alg_len == 11:
                    continue

                cn = CrossNode(new_perm, new_alg, self.solved_perm,
                               self.d_color, self.solved_side_colors)
                self._move_up(cn)

    def _move_up(self, cn):
        """
        Appends cn to the end of open_set and move it up the tree.
        """
        self.open_set.append(cn)

        while True:
            # Node info, compare f_cost and h_cost at the same time
            cn_ind = self.open_set.index(cn)
            cn_val = cn.f_cost + cn.h_cost/100

            # If index is 0, can't move up anymore
            if not cn_ind:
                return

            # The position above node n is int half of (n - 1)
            cn_up_ind = (cn_ind - 1) // 2
            cn_up = self.open_set[cn_up_ind]
            cn_up_val = cn_up.f_cost + cn_up.h_cost/100

            # Compare values
            if cn_val < cn_up_val:
                self._swap(cn_ind, cn_up_ind)
            else:
                return

    def _move_do1wn(self):
        """
        Sorts the top node down the tree.
        """
        set_len = len(self.open_set)

        # Don't run if open_set is empty
        if not set_len:
            return

        # Compare both f_cost and h_cost at same time
        cn = self.open_set[0]
        cn_val = cn.f_cost + cn.h_cost/100

        while True:
            cn_ind = self.open_set.index(cn)

            # Get info for left lower node, make sure we don't go over index
            if set_len > 2 * cn_ind + 1:
                cn_ld_ind = 2 * cn_ind + 1
                cn_ld = self.open_set[cn_ld_ind]
                cn_ld_val = cn_ld.f_cost + cn_ld.h_cost/100
                diff_ld = cn_val - cn_ld_val
            # We reached botom of tree if it doesn't exist
            else:
                return

            # Get info for right lower node
            if set_len > cn_ld_ind + 1:
                right_node_exists = True

                cn_rd_ind = cn_ld_ind + 1
                cn_rd = self.open_set[cn_rd_ind]
                cn_rd_val = cn_rd.f_cost + cn_rd.h_cost/100
                diff_rd = cn_val - cn_rd_val
            # We reached end of list if it doesn't exist
            else:
                right_node_exists = False

            # Swap with left lower node due to f_cost
            if diff_ld >= 1:
                self._swap(cn_ind, cn_ld_ind)
            # Swap with right lower node due to f_cost
            elif right_node_exists and diff_rd >= 1:
                self._swap(cn_ind, cn_rd_ind)
            # Swap with left lower node due to h_cost
            elif diff_ld > 0:
                self._swap(cn_ind, cn_ld_ind)
            # Swap with right lower node due to h_cost
            elif right_node_exists and diff_rd > 0:
                self._swap(cn_ind, cn_ld_ind)
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

            fn = self.open_set[0]
            fn_val = fn.f_cost + fn.h_cost/100

            while True:
                fn_ind = self.open_set.index(fn)

                left_ind = 2 * fn_ind + 1
                right_ind = left_ind + 1

                # Check if left node exists, if not we are finished
                if set_len > left_ind:
                    left = self.open_set[left_ind]
                    left_val = left.f_cost + left.h_cost/100
                else:
                    return

                # Check if right node exists
                if set_len > right_ind:
                    right = self.open_set[right_ind]
                    right_val = right.f_cost + right.h_cost/100
                else:
                    right = None

                # Left value must be less and either there is no right node or
                # the left node is the lower choice
                if (left_val < fn_val) and \
                   (right is None or left_val <= right_val):
                    self._swap(fn_ind, left_ind)
                elif right is not None and right_val < fn_val:
                    self._swap(fn_ind, right_ind)
                else:
                    return

    def _swap(self, i, j):
        """
        Swaps elements at i and j in open_set
        """
        self.open_set[i], self.open_set[j] = self.open_set[j], self.open_set[i]


class CrossNode:
    """
    The class represents a node in the A* algorithm.

    The metric from the intial state is defined as the sum of the absolute
    value of the difference of each of the three coordinates. (e.g. the
    difference between [-1, 1, -1] and [1, 1, 1] is 2 + 0 + 2 = 4]. This metric
    is found for the one absolute and three relative positions of the cross.
    This can be imagined like rotating just the side centers and seeing how
    close the cube is to having a cross.

    The absolute measure (abs_h_cost) is used to determine if a cross has been
    found. The relative measure (rel_h_cost) is used with the flip_penatly for
    the h_cost which is used everywhere else. The f_cost is the total metric
    which also sums the current length of the algorithm as a factor.

    Moves are applied to the cube like usual, but only the four cross edges
    are moved since the permuation of the other cubies is irrelevant.

    Parameters:
    edge_perm - The permutation of just the four cross edges in dict form
    alg - The alg used to obtain this current edge_perm from the initial perm
          of the cube
    solved_perm - The color-first dict of the permutation of the edges if they
                   were solved
    d_color - The color of the Down face (i.e. of the cross being solved)
    solved_side_colors - A 4-element list of the side colors of the cross in
                         the order: F R D L to use as a reference for relative
                         positions of the current cross edge pieces
    """

    def __init__(self, edge_perm, alg, solved_perm, d_color,
                 solved_side_colors):
        # Constant for every CrossNode object
        self.solved_perm = solved_perm
        self.d_color = d_color

        # Constant for each CrossNode object
        self.edge_perm = edge_perm
        self.solved_side_colors = solved_side_colors
        self.cross_edges = self._cross_edges()
        self.alg = alg

        # Metrics
        # A factor of 2 because a bad flip is equivalent to a metric score
        # of 2. So each bad edge adds 2 to the metric
        self.flip_penalty = 2 * self._flip_penalty()
        self.g_cost = len(self.alg)
        self.rel_h_cost, self.abs_h_cost = self._all_metrics()
        self.abs_h_cost += self.flip_penalty
        self.h_cost = self.rel_h_cost + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _cross_edges(self):
        """
        Cross edge dict by (k, v) = (color, coord).
        """
        cross_edge_dict = {}
        for coord, colors in self.edge_perm.items():
            colors_copy = colors.copy()
            colors_copy.remove(self.d_color)
            colors_copy.remove('')

            cross_edge_dict[colors_copy[0]] = coord

        return cross_edge_dict

    def _flip_penalty(self):
        """
        Counts number of edge pieces that are wrongly flipped.
        """
        bad_flip = 0

        for coord, colors in self.edge_perm.items():
            # Can only be wrongly flipped if on D or U face
            if coord[1] != 0:
                # But white sticker isn't on D or U face
                if self.d_color in [colors[0], colors[2]]:
                    bad_flip += 1

        return bad_flip

    def _all_metrics(self):
        """
        Finds the metric for each relative position of the side center pieces
        and returns the value for the minimum of these along with the metric
        for the absolute position.
        """
        # Find the absolute metric
        abs_tot_distance = self._metric(self.solved_perm)

        min_tot_distance = 100
        # Try each of the 3 remaining relative positions
        # (rotations of side centers)
        for turn in range(1, 4):
            rel_solved_perm = {}
            # Rotate colors in side edge dict
            for n, color in enumerate(self.solved_side_colors):
                new_color = self.solved_side_colors[(n + turn) % 4]
                rel_solved_perm[new_color] = self.solved_perm[color]

            # Calculate metric for new dict
            tot_distance = self._metric(rel_solved_perm)

            # Keep value if is less than current minimum
            if tot_distance < min_tot_distance:
                min_tot_distance = tot_distance

        return min(min_tot_distance, abs_tot_distance), abs_tot_distance

    def _metric(self, end_pos):
        """
        Sums the difference of each coordinate dimension
        """
        tot_distance = 0

        for color, coord in self.cross_edges.items():
            tot_distance += sum(map(lambda x, y: abs(x - y),
                                    coord, end_pos[color]))

        return tot_distance

    def _turn_rotate(self, ttype, side):
        """
        Applies a turn to the 4 cubies analgous to the Cube class method. Here,
        a new dict is returned (with the 4 cubies' new coordinates) instead of
        updating current perm.
        """
        # Get the right parameters for the cubie rotation
        p = PARAM_DICT[ttype][side]
        new_perm = {}

        turning_layers = [p[1]]

        for coord, color in self.edge_perm.items():
            if coord[p[0]] in turning_layers:
                new_perm[(p[2]*coord[p[3]],
                          p[4]*coord[p[5]],
                          p[6]*coord[p[7]])] = \
                          [color[p[3]], color[p[5]], color[p[7]]]
            else:
                new_perm[coord] = color

        return new_perm

    def apply_turn(self, turn):
        """
        Analgous to Cube class method except only works for one turn at a time.
        """
        return self._turn_rotate(*TURN_DICT[turn])
