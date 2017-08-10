"""
Contains the F2L class along with the F2LNode class used to find the
F2L algorithm via A* pathfinding.
"""
from collections import deque
from operator import add
from itertools import permutations

from algorithms.alg_dicts import TURN_DICT, PARAM_DICT


class F2L:
    """
    The class solves the F2L by solving the four pairs one after each other.
    The order used is determined by f2l_pairs.

    It solves it using an A* pathfinding algorithm where each new node is an
    F2LNode object. The list containing the nodes is sorted via a heap where
    new nodes are appended and sorted up the tree since only the node with the
    lowest metric is needed.

    Parameters:
    perm - The full permutation of the cube in dict form
    f2l_pairs - The order in which to solve F2L. An example of the form is
                ['go', 'gr', 'bo', 'br'] which will solve in the order:
                green-orange, green-red, blue-orange, blue-red. The order
                of the characters in the string does not matter.
    """

    def __init__(self, perm, f2l_pairs):
        # New form to store cube, probs will use for every part but for now
        # it's just here in F2L class
        self.perm = {self._cubie_key(color): (list(coord), color)
                     for coord, color in perm.items()}

        self.algs, self.open_setss, self.closed_setss = [], [], []

        # Down and Up face colors
        self.d_color = ''.join(perm[(0, -1, 0)])
        self.u_color = ''.join(perm[(0, 1, 0)])

        # The 6 centers
        self.centers = self._centers()
        # The 4 cross edge cubies
        self.cross = self._cross()

        # The starting and ending perm. Add F2L pair to each
        # for each iteration through the for loop
        self.init_perm = self.cross.copy()
        self.goal_perm = self.cross.copy()

        for f2l_pair in f2l_pairs:
            # Add current/solved position to init_perm/goal_perm, respectively
            self._add_pair(f2l_pair)

            # Find alg to solve for F2L pair
            alg, open_sets, closed_sets = self._find_path(f2l_pair)
            self.algs.append(alg)
            self.open_setss.append(open_sets)
            self.closed_setss.append(closed_sets)

            # Update init_perm as goal_perm
            self.init_perm = self.goal_perm.copy()
            # Update perm with alg used to solve first F2L pair
            self._apply_alg(alg)

    @staticmethod
    def _cubie_key(color):
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

        centers = {frozenset(c): self.perm[frozenset(c)] for c in colors}

        return centers

    def _cross(self):
        """
        Returns a dict of the 4 cross edges
        """
        colors = ['w', 'o', 'g', 'r', 'b', 'y']
        colors.remove(self.d_color)
        colors.remove(self.u_color)

        cross = {frozenset((c + self.d_color, self.d_color + c)):
                 self.perm[frozenset((c + self.d_color, self.d_color + c))]
                 for c in colors}

        return cross

    def _add_pair(self, f2l_pair):
        """
        Adds the current position of the pieces of the F2L pair to init_perm
        and the solved position to goal_perm.

        Parameters:
        f2l_pair - F2L pair to add in the form of a 2 char string
                   (e.g. 'br' for the blue-red F2L pair)
        """
        edge_key = self._cubie_key(f2l_pair)
        corner_key = self._cubie_key(f2l_pair + self.d_color)

        # Add current position cubies to init_perm
        self.init_perm[edge_key] = self.perm[edge_key]
        self.init_perm[corner_key] = self.perm[corner_key]

        # Find centers that the F2L pair is between
        pair_centers = (self.centers[frozenset(f2l_pair[0])],
                        self.centers[frozenset(f2l_pair[1])])
        # Add coords and colors together to get solved position of edge piece
        edge_coord = list(map(add, pair_centers[0][0], pair_centers[1][0]))
        edge_color = list(map(add, pair_centers[0][1], pair_centers[1][1]))
        # Convert above for the solved position of corner piece
        corner_coord = list(map(add, edge_coord, [0, -1, 0]))
        corner_color = list(map(add, edge_color, ['', self.d_color, '']))

        # Add both pieces to goal_perm
        self.goal_perm[edge_key] = (edge_coord, edge_color)
        self.goal_perm[corner_key] = (corner_coord, corner_color)

    def _turn_rotate(self, ttype, side):
        """
        A gutted version of the turn_rotate for the Cube class. Temporary
        since eventually probably this class will inherit from Cube
        class when I standardize the form of self.perm used here.
        """
        # Get the right parameters for the cubie rotation
        p = PARAM_DICT[ttype][side]
        new_coords = {}

        for stickers, cordlor in self.perm.items():
            coord, color = cordlor[0], cordlor[1]
            if coord[p[0]] == p[1]:
                new_coords[stickers] = ([p[2] * coord[p[3]],
                                         p[4] * coord[p[5]],
                                         p[6] * coord[p[7]]],
                                        [color[p[3]],
                                         color[p[5]],
                                         color[p[7]]])

        # Updates the coordinates and colors
        self.perm.update(new_coords)

    def _apply_alg(self, alg):
        """
        Analogous to apply_alg method from the Cube class.
        """
        for turn in alg:
            self._turn_rotate(*TURN_DICT[turn])

    def _find_path(self, f2l_pair):
        """
        Completes A* pathfinding for the current F2L pair.

        Parameters:
        f2l_pair - The two colors of the F2L pair as a string
                   (e.g. 'br' for the blue-red F2L pair)
        """
        f2l_key = [self._cubie_key(f2l_pair),
                   self._cubie_key(f2l_pair + self.d_color)]
        slot_perm = {x: self.goal_perm[x] for x in f2l_key}
        fn = F2LNode(self.init_perm, self.goal_perm, slot_perm, '',
                     f2l_key, '', self.d_color)

        # Every single layer face turn
        turn_space = 'UT!LK@FE#RQ$BA%DC^'
        self.open_set = deque([fn])
        closed_set = []

        i = 0
        while True:
            i += 1

            # Take object with lowest f_cost
            current = self.open_set.popleft()
            # Helpful debugging, one print per iteration
#            print('{:>3} == F Cost - {:>2} | H Cost - {:>2}'.format(
#                    i, current.f_cost, current.h_cost) +
#                  '| Loc - {:>2} | Alg - {}'.format(
#                    current.slot_metric, code_to_alg(current.alg)))

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

            # Move last node to top of tree
            self.open_set.rotate()
            # Compare it downwards
            self._move_down()
            # Add to closed set
            closed_set.append(current.cur_perm)

            # Return if perm is equal to goal perm
            if not current.abs_h_cost:
                return current.alg, len(self.open_set), len(closed_set)

            # Create new objects and put in open_set to check next if
            # perm hasn't already been found
            for turn in turn_space_current:
                new_perm = current.apply_turn(turn)
                new_alg = current.alg + turn

                if new_perm in closed_set:
                    continue

                fn = F2LNode(new_perm, self.goal_perm, current.slot_perm,
                             current.slot_turn, f2l_key, new_alg, self.d_color)
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


class F2LNode:
    """
    This class represents a node in the A* algorithm.

    The metric from the initial state is defined as the sum of the absolute
    value of the difference of each of the three coordinates. (e.g. the
    difference between [-1, 1, -1] and [1, 1, 1] is 2 + 0 + 2 = 4]. This metric
    is found both for its absolute final position and its relative final
    position.

    Its relative final position is where the slot currently is as determined by
    the _slot method. The absolute final position (abs_h_cost) is used to
    determined if the F2L pair has been solved. The relative final position
    (rel_h_cost) is used with the flip_penatly for the h_cost which is used
    everywhere else. The f_cost is the total metric which also sums the
    current length of the algorithm as a factor.

    Moves are applied to the cube like usual, but only the relevant cubies
    (the four cross edges, any previously solved pairs and the current pair)
    are moved since the permutation of the other cubies is irrelevant.

    Parameters:
    cur_perm - The current permutation of the cube
    goal_perm - The permutation that the pathfinder is trying to reach
    slot_perm - The permutation of just the slot (i.e. where the F2L pair
                is to be inserted)
    slot_turn - The turn that moved the slot out of position (or empty string
                if slot is not out of position)
    f2l_key - The keys of two cubies of the F2L pair (used to pull the pair
              from a perm)
    alg - Current alg used to obtain cur_perm from its initial state
    d_color - The color of the Down face
    """

    def __init__(self, cur_perm, goal_perm, slot_perm, slot_turn,
                 f2l_key, alg, d_color):
        self.d_color = d_color
        self.alg = alg
        self.f2l_key = f2l_key

        self.goal_perm = goal_perm
        self.cur_perm = cur_perm
        self.slot_perm, self.slot_turn = self._slot(slot_perm, slot_turn)

        # Metrics
        self.flip_penalty = 2 * self._flip_penalty()
        self.rel_h_cost = self._slot_metric()
        self.pair_metric = self._pair_metric()
        self.g_cost = len(self.alg)

        self.h_cost = self.rel_h_cost + self.flip_penalty
        self.abs_h_cost = self._metric() + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _slot(self, slot_perm, slot_turn):
        """
        Finds the permutation of the slot for the current F2L_pair and the
        turn in question.

        For example, if the green-orange F2L pair is being solved for a yellow
        cross, then this keeps track of the slot that the green-orange F2L
        pair would go into. If there is an L turn, then the slot is now on the
        U face, but, at this point, only an L' turn would return the slot
        into it's original position. In this example, it's analogous for an F
        turn moving the slot to the U face or an L or F' turn moving it to the
        bottom.

        Paramters:
        slot_perm - The perm (of two cubies) of the slot of the current F2L
                    pair
        slot_turn - The turn that has resulted in slot_perm
        """
        if not len(self.alg):
            return slot_perm, slot_turn

        turns = ['K', 'L', 'E', 'F', 'Q', 'R', 'A', 'B']
        turn = self.alg[-1]

        # Slot is in correct place
        if not slot_turn:
            # If we have a single side turn, now it's on the U or D face, so
            # we must update for that
            if turn in turns:
                return self.apply_turn(turn, slot_perm), turn
            # Any other move doesn't change slots position
            else:
                return slot_perm, slot_turn
        # Slot is on the U or D face
        else:
            inv_alg = turns[(turns.index(slot_turn) // 2) * 2 +
                            (not turns.index(slot_turn) % 2)]
            # If we have a turn that will reverse the turn that place it in
            # that top face, then the slot is back in its correct face
            if turn == inv_alg:
                return {x: self.goal_perm[x] for x in self.f2l_key}, ''
            # Otherwise, we don't change anything
            else:
                return slot_perm, slot_turn

    def _flip_penalty(self):
        """
        Counts number of cubies that are in the correct position but are
        flipped incorrectly.
        """
        bad_flip = 0

        for stickers, cordlor in self.cur_perm.items():
            # The 0th element is coords and 1st element is color
            # So incorrect color but correct coords means it's flipped
            if (self.goal_perm[stickers][0] == cordlor[0] and
               self.goal_perm[stickers][1] != cordlor[1]):
                bad_flip += 1

        return bad_flip

    def _pair_metric(self):
        return 0

    def _slot_metric(self):
        """
        The metric but reletive to the slot as determined by self._slot
        """
        if not len(self.alg):
            return self._metric()

        # Create a copy of goal_perm and update it with where the slot is
        new_goal_perm = self.goal_perm.copy()
        new_goal_perm.update(self.slot_perm)

        return self._metric(new_goal_perm)

    def _metric(self, goal_perm=None):
        """
        Sums the difference of each coordinate dimension

        Parameters:
        goal_perm - (default None) The permutation to compare self.cur_perm
                    against. Defaults to self.goal_perm.
        """
        goal_perm = goal_perm or self.goal_perm
        tot_distance = 0

        for stickers, cordlor in self.cur_perm.items():
            distance = sum(map(lambda x, y: abs(x - y),
                               cordlor[0], goal_perm[stickers][0]))
            tot_distance += distance

        return tot_distance

    def _turn_rotate(self, ttype, side, perm):
        """
        Applies a turn to analgous to the Cube class method. Here, a new dict
        is returned instead of updating current perm.
        """
        # Get the right parameters for the cubie rotation
        p = PARAM_DICT[ttype][side]
        new_perm = {}

        for stickers, cordlor in perm.items():
            coord, color = cordlor[0], cordlor[1]
            if coord[p[0]] == p[1]:
                new_perm[stickers] = ([p[2] * coord[p[3]],
                                       p[4] * coord[p[5]],
                                       p[6] * coord[p[7]]],
                                      [color[p[3]], color[p[5]], color[p[7]]])
            else:
                new_perm[stickers] = cordlor

        return new_perm

    def apply_turn(self, turn, perm=None):
        """
        Analgous to Cube class method except only works for one turn at a time.
        """
        perm = perm or self.cur_perm
        return self._turn_rotate(*TURN_DICT[turn], perm)
