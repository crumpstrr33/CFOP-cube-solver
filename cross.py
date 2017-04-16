from collections import deque

from algorithms.alg_dicts import turn_dict, param_dict

# So... looking good. Still some problems. Don't want to arbitrarilty restrict
# it with the 9 move cutoff. Also, flip penalty 1 or 2? I'm leaning towards 2.
# Lastly, a weight on alg length? I'm leaning towards a weight of 1

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
    CrossEdges object. The list containing the nodes is sorted via a heap sort
    where new nodes are appended and sorted up the tree since only the node
    with the lowest metric is needed.

    There is an artificial cutoff at 10 moves. Since 10+ algorithms are always
    superfluous for a cross.

    Parameters:
    perm - The full permutation of the cube in its dict form
    """

    def __init__(self, perm):
        self.perm = perm
        self.cross_color = ''.join(self.perm[(0, -1, 0)])
        self.init_perm = self._init_perm()
        self.solved_edges = self._solved_edges()
        self.solved_side_colors = self._solved_side_colors()

        self.alg, self.open_sets, self.closed_sets = self._find_path()

    def _init_perm(self):
        """
        Finds the current position of the cross edges by
        color and coordinates
        """
        cross_edges = {}

        for coord, colors in self.perm.items():
            # Look at edge pieces with cross_color color
            if (coord.count(0) == 1 and self.cross_color in colors):
                cross_edges[coord] = colors

        return cross_edges

    def _solved_edges(self):
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
        solved_edges = {}
        for color, coord in center_dict.items():
            solved_edges[color] = (coord[0], -1, coord[2])

        return solved_edges

    def _solved_side_colors(self):
        '''
        Finds side center colors in the order: F R B L
        '''
        # The order wanted
        order = [(0, -1, 1), (1, -1, 0), (0, -1, -1), (-1, -1, 0)]
        side_colors = []

        for n in range(4):
            for color, coord in self.solved_edges.items():
                if coord == order[n]:
                    side_colors.append(color)

        return side_colors

    def _find_path(self):
        """
        A* pathfinding algorithm to solve for the cube's cross.
        """
        ce = CrossEdges(self.init_perm, '', self.solved_edges,
                        self.cross_color, self.solved_side_colors)

        # Every single layer face turn
        turn_space = 'UT!LK@FE#RQ$BA%DC^'
        self.open_set = deque([ce])
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

                if new_perm in closed_set or new_alg_len == 10:
                    continue

                ce = CrossEdges(new_perm, new_alg, self.solved_edges,
                                self.cross_color, self.solved_side_colors)
                self._move_up(ce)

    def _move_up(self, ce):
        """
        Appends ce to the end of open_set and move it up the heap.
        """
        self.open_set.append(ce)

        while True:
            ce_ind = self.open_set.index(ce)
            # If index is 0, can't move up anymore
            if not ce_ind:
                return

            # The position above node n is the int half of n - 1
            ce_up_ind = (ce_ind - 1) // 2
            ce_up = self.open_set[ce_up_ind]

            # Only swap if f_cost is lower (want lowest f_costs closest to top)
            if ce.f_cost < ce_up.f_cost:
                self._swap(ce, ce_ind, ce_up, ce_up_ind)
            else:
                # If the same, compare h_costs
                if ce.h_cost < ce_up.h_cost:
                    self._swap(ce, ce_ind, ce_up, ce_up_ind)
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

        ce = self.open_set[0]

        while True:
            # One lower node for n is 2n + 1
            ce_ind = self.open_set.index(ce)
            ce_down_ind = 2 * ce_ind + 1

            # If the lower node doesn't exist (i.e. exceeds the length of
            # open_set, it's at the bottom)
            if ce_down_ind < set_len:
                ce_down = self.open_set[ce_down_ind]
            else:
                return

            # Only swap if f_cost is higher, o/w compare with other lower node
            if ce.f_cost > ce_down.f_cost:
                self._swap(ce, ce_ind, ce_down, ce_down_ind)
            else:
                # The other lower node is 2n + 2
                ce_down_ind += 1

                # Check so we're not beyond open_set length
                if ce_down_ind < set_len:
                    ce_down = self.open_set[ce_down_ind]
                else:
                    return

                # Compare with this node's f_cost
                if ce.f_cost > ce_down.f_cost:
                    self._swap(ce, ce_ind, ce_down, ce_down_ind)
                else:
                    # If not, compare with h_cost
                    if ce.h_cost > ce_down.h_cost:
                        self._swap(ce, ce_ind, ce_down, ce_down_ind)
                    else:
                        return

    def _swap(self, ce1, ind1, ce2, ind2):
        """
        Swap ce1 (with index ind1) and ce2 (with index ind2) in open_set
        """
        self.open_set[ind1], self.open_set[ind2] = ce2, ce1


class CrossEdges:
    """
    The class representing a node in the A* algorithm.

    The metric from the intial state is defined as the sum of the absolute
    value of the difference of each of the three coordinates. This metric is
    found for the one absolute and three relative positions of the cross. This
    can be imagined like rotating just the side centers and seeing how close
    the cube is to having a cross.

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
    solved_edges - The color-first dict of the permutation of the edges if they
                   were solved
    cross_color - The color of the Down face (i.e. of the cross being solved)
    solved_side_colors - A 4-element list of the side colors of the cross in
                         the order: F R D L to use as a reference for relative
                         positions of the current cross edge pieces
    """

    def __init__(self, edge_perm, alg, solved_edges, cross_color,
                 solved_side_colors):
        # Constant for every CrossEdge object
        self.solved_edges = solved_edges
        self.cross_color = cross_color

        # Constant for each CrossEdge object
        self.edge_perm = edge_perm
        self.solved_side_colors = solved_side_colors
        self.cross_edges = self._cross_edges()
        self.alg = alg

        # Metrics
        self.flip_penalty = 2 * self._bad_flipped_edges()
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
            colors_copy.remove(self.cross_color)
            colors_copy.remove('')

            cross_edge_dict[colors_copy[0]] = coord

        return cross_edge_dict

    def _bad_flipped_edges(self):
        """
        Counts number of edge pieces that are wrongly flipped.
        """
        bad_flip = 0

        for coord, colors in self.edge_perm.items():
            # Can only be wrongly flipped if on D or U face
            if coord[1] != 0:
                # But white sticker isn't on D or U face
                if self.cross_color in [colors[0], colors[2]]:
                    bad_flip += 1

        return bad_flip

    def _all_metrics(self):
        """
        Finds the metric for each relative position of the side center pieces
        and returns the value for the minimum of these along with the metric
        for the absolute position.
        """
        # Find the absolute metric
        abs_tot_distance = self._metric(self.solved_edges)

        min_tot_distance = 100
        # Try each of the 3 remaining relative positions
        # (rotations of side centers)
        for turn in range(1, 4):
            rel_solved_edges = {}
            # Rotate colors in side edge dict
            for n, color in enumerate(self.solved_side_colors):
                new_color = self.solved_side_colors[(n + turn) % 4]
                rel_solved_edges[new_color] = self.solved_edges[color]

            # Calculate metric for new dict
            tot_distance = self._metric(rel_solved_edges)

            # Keep value if is less than current minimum
            if tot_distance < min_tot_distance:
                min_tot_distance = tot_distance

        return min(min_tot_distance, abs_tot_distance), abs_tot_distance

    def _metric(self, end_pos):
        '''
        Sums the difference of each coordinate dimension
        '''
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
        p = param_dict[ttype][side]
        new_coords = {}

        turning_layers = [p[1]]

        for cubie, colors in self.edge_perm.items():
            if cubie[p[0]] in turning_layers:
                new_coords[(p[2]*cubie[p[3]],
                            p[4]*cubie[p[5]],
                            p[6]*cubie[p[7]])] = \
                            [colors[p[3]], colors[p[5]], colors[p[7]]]

            else:
                new_coords[cubie] = colors

        return new_coords

    def apply_turn(self, turn):
        """
        Analgous to Cube class method except only works for one turn at a time.
        """
        return self._turn_rotate(*turn_dict[turn])
