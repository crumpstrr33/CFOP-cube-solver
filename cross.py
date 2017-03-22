from algorithms.alg_dicts import turn_dict, param_dict

LEN_WEIGHT = 3
LEN_ALG_TO_RESET = 4
NUM_OBJ_TO_NEXT_STEP = 15


class Cross:
    '''
    This class solves the cross on the Down face for a given permutation.

    It solves it using an A* pathfinding algorithm where each new node is 
    a CrossEdges object. Once a node with length LEN_ALG_TO_RESET is found,
    the algorithm empties open_set and restarts with this node as the
    initializer.

    Parameters:
    perm - The full permutation of the cube in its dict form
    '''
    def __init__(self, perm):
        self.perm = perm
        self.cross_color = ''.join(self.perm[(0, -1, 0)])
        self.init_perm = self._cross_edges()
        self.solved_dict = self._solved_edges()

        self.alg = self._find_path()


    def _cross_edges(self):
        '''
        Finds the current position of the cross edges by color and coordinates
        '''
        cross_edges = {}

        for coord, colors in self.perm.items():
            ## Look at edge pieces with cross_color sticker color
            if coord.count(0) == 1 and self.cross_color in colors:
                ## Dict with (k, v) = (coordinate, 3-element color list)
                cross_edges[coord] = colors

        return cross_edges


    def _solved_edges(self):
        '''
        Finds the solved position of the cross edges by color
        '''
        center_dict = {}
        for coord, color in self.perm.items():
            ## Look only at centers
            if coord.count(0) == 2:
                ## Don't look at Up or Down centers
                if coord[1] == 0:
                    center_dict[''.join(color)] = coord

        ## Dict with (k, v) = (non-white color, coordinate)
        solved_dict = {}
        for color, coord in center_dict.items():
            solved_dict[color] = (coord[0], -1, coord[2])

        return solved_dict


    def _find_path(self):
        '''
        A* pathfinding algorithm to solve for the cube's cross.
        '''
        ce = CrossEdges(self.init_perm, '', self.solved_dict, self.cross_color)

        ## Every single layer face turn
        turn_space = 'UT!LK@FE#RQ$BA%DC^'
        open_set = [ce]
        closed_set = []
        num_to_next_step = 0
        next_choice = []
        step = 1

        while True:
            ## Find pos with lowest f_cost, then lowest h_cost
            open_set = sorted(open_set, key=lambda ce: (ce.f_cost, ce.h_cost))
            current = open_set[0]

            ## Collect objects with limit length
            if len(current.alg) >= LEN_ALG_TO_RESET * step:
                next_choice.append(current)
                num_to_next_step += 1

            ## Then when it reaches NUM_OBJ_TO_NEXT_STEP, reset open_set 
            if num_to_next_step == NUM_OBJ_TO_NEXT_STEP:
                open_set = next_choice
                next_choice = []
                num_to_next_step = 0
                step += 1

            ## Find current turn_space
            if current.alg != '':
                last_turn = current.alg[-1]

                latest_turn = turn_space.index(last_turn)
                forbidden_moves = latest_turn - (latest_turn % 3)
                turn_space_current = turn_space[:forbidden_moves] + \
                                     turn_space[forbidden_moves + 3:]

                ## Remove half of the mirror moves (e.g. RL = LR and so on)
                if last_turn in 'UT!':
                    turn_space_current = turn_space_current.replace('DC^', '')
                elif last_turn in 'LK@':
                    turn_space_current = turn_space_current.replace('RQ$', '')
                elif last_turn in 'FE#':
                    turn_space_current = turn_space_current.replace('BA%', '')
            else:
                turn_space_current = turn_space

            ## Remove from open set, add to closed set
            open_set.remove(current)
            closed_set.append(current.edge_perm)

            ## Return if perm is equal to solved perm and undo double layer U turns
            if current.h_cost == 0:
                cw = current.alg.count('u')
                ccw = -current.alg.count('t')
                dt = 2 * current.alg.count('1')
                final_rotate_move = ['', 't', '1', 'u'][(cw + ccw + dt) % 4]

                return current.alg + final_rotate_move

            ## Create new objects and put in open_set to check next if perm 
            ## hasn't already been found
            for turn in turn_space_current:
                new_perm = current.apply_turn(turn)
                new_alg = current.alg + turn

                if new_perm in closed_set:
                    continue

                ce = CrossEdges(new_perm, new_alg, self.solved_dict, self.cross_color)

                open_set.append(ce)


class CrossEdges:
    '''
    The class representing a node in the A* algorithm.

    The metric from the intial state is defined as the sum of the absolute
    value of the difference of each of the three coordinates. And the metric
    from the solved state is the length of the algorithm multiplied by some
    weight.

    A higher weight places more importance on finding a shorter algorithm at
    the cost of time while a lower weight does the opposite.

    The sum of these two metrics is considered when deciding which node to 
    investigate next.

    Moves are applied to the cube like usual, but only the four cross edges
    are moved since the permuation of the other cubies is irrelevant.

    Parameters:
    edge_perm - The permutation of just the four cross edges in dict form
    alg - The alg used to obtain this current edge_perm from the initial perm
          of the cube
    solved_dict - The color-first dict of the permutation of the edges if they
                  were solved
    cross_color - The color of the Down face (i.e. of the cross being solved)
    '''
    def __init__(self, edge_perm, alg, solved_dict, cross_color):
        self.solved_dict = solved_dict
        self.cross_color = cross_color

        self.edge_perm = edge_perm
        self.cross_edges = self._calc_cross_edges()
        self.alg = alg

        self.flip_penalty = self._bad_flipped_edges()
        self.g_cost = LEN_WEIGHT * len(self.alg)
        self.h_cost = self._metric_to_solved() + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost


    def _calc_cross_edges(self):
        '''
        Cross edge dict by color.
        '''
        cross_edge_dict = {}
        for coord, colors in self.edge_perm.items():
            colors_copy = colors.copy()
            colors_copy.remove(self.cross_color)
            colors_copy.remove('')

            ## Dict with (k, v) = (non-white color, coordinate)
            cross_edge_dict[colors_copy[0]] = coord

        return cross_edge_dict


    def _bad_flipped_edges(self):
        '''
        Counts number of edge pieces that are wrongly flipped.
        '''
        bad_flip = 0

        for coord, colors in self.edge_perm.items():
            ## Can only be wrongly flipped if on Down or Up face
            if coord[1] != 0:
                ## But white sticker isn't on Down or Up face
                if self.cross_color in [colors[0], colors[2]]:
                    bad_flip += 1

        return bad_flip


    def _metric_to_solved(self):
        '''
        Metric as described in the CrossEdges class description.
        '''
        tot_distance = 0

        for color, coord in self.cross_edges.items():
            tot_distance += sum(map(lambda x, y: abs(x - y), coord, self.solved_dict[color]))

        return tot_distance


    def _turn_rotate(self, ttype, side):
        '''
        Applies a turn to the 4 cubies analgous to the Cube class method. Here,
        a new dict is returned (with the 4 cubies' new coordinates) instead of
        updating current perm.        
        '''
        ## Get the right parameters for the cubie rotation
        p = param_dict[ttype][side]
        new_coords = {}

        turning_layers = [p[1]]

        for cubie, colors in self.edge_perm.items():
            if cubie[p[0]] in turning_layers:
                new_coords[(p[2]*cubie[p[3]], p[4]*cubie[p[5]], p[6]*cubie[p[7]])] = \
                          [colors[p[3]], colors[p[5]], colors[p[7]]]
            else:
                new_coords[cubie] = colors

        return new_coords


    def apply_turn(self, turn):
        '''
        Analgous to Cube class method except only works for one turn at a time.
        '''
        return self._turn_rotate(*turn_dict[turn])
