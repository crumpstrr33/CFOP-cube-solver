from algorithms.alg_dicts import turn_dict, param_dict

LEN_WEIGHT = 4
LEN_ALG_TO_RESET = 4


class Cross:
    def __init__(self, perm):
        self.perm = perm
        self.cross_color = ''.join(self.perm[(0, -1, 0)])

        self.init_dict = self._cross_edges_color()
        self.init_perm = self._cross_edges_coord()
        self.solved_dict = self._solved_edges()

        self.alg = self._find_path()
        

    def _cross_edges_color(self):
        '''
        Finds the current position of the cross edges by color
        '''
        cross_edge_dict = {}
        for coord, colors in self.perm.items():
            if coord.count(0) == 1 and self.cross_color in colors:
                edge_color = ''.join(''.join(colors).split(self.cross_color))
                cross_edge_dict[edge_color] = coord

        return cross_edge_dict


    def _cross_edges_coord(self):
        cross_edge_dict = {}
        for coord, colors in self.perm.items():
            if coord.count(0) == 1 and self.cross_color in colors:
                cross_edge_dict[coord] = colors

        return cross_edge_dict

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

        solved_dict = {}
        for color, coord in center_dict.items():
            solved_dict[color] = (coord[0], -1, coord[2])

        return solved_dict


    def _find_path(self):
        ce = CrossEdges(self.init_perm, '', LEN_WEIGHT, self.solved_dict, self.cross_color)

        turn_space = 'UT!ut1LK@FE#RQ$BA%'
        open_set = [ce]
        closed_set_perms = []
        step = 1
    
        while True:
            ## Find pos with lowest f_cost
            current = sorted(open_set, key=lambda perm: (perm.f_cost, perm.h_cost))[0]
    
            if len(current.alg) == LEN_ALG_TO_RESET * step:
                open_set = [current]
                step += 1
    
            ## Find current turn_space
            if current.alg != '':
                latest_turn = turn_space.index(current.alg[-1])
                forbidden_moves = latest_turn - (latest_turn % 3)
                turn_space_current = turn_space[:forbidden_moves] + turn_space[forbidden_moves + 3:]
            else:
                turn_space_current = turn_space
    
            ## Remove from open set, add to closed set
            open_set.remove(current)
            closed_set_perms.append(current.edge_perm)
    
            ## Return if perm is equal to solved perm and undo double layer U turns
            if current.h_cost == 0:
                dl_turns = (current.alg.count("u") - current.alg.count("t") + 2 * current.alg.count("1")) % 4
                current.alg += ['', 't', '1', 'u'][dl_turns]
                return current.alg
    
            for turn in turn_space_current:
                ce = CrossEdges(current.apply_turn(turn), current.alg + turn, current.len_weight,
                                self.solved_dict, self.cross_color)
                if ce.edge_perm in closed_set_perms:
                    continue

                open_set.append(ce)

## NEEDED CONSTANTS:
## cross_color
## solved_dict


class CrossEdges:
    def __init__(self, edge_perm, alg, len_weight, solved_dict, cross_color):
        ## Constants
        self.len_weight = len_weight
        self.solved_dict = solved_dict
        self.cross_color = cross_color

        self.edge_perm = edge_perm
        self.alg = alg
        self.flip_penalty = self._bad_flipped_edges()
        self.g_cost = self.len_weight * len(self.alg)
        self.h_cost = self._metric_to_solved() + self.flip_penalty


    @property
    def f_cost(self):
        return self.h_cost + self.g_cost


    @property
    def cross_edges(self):
        cross_edge_dict = {}
        for coord, colors in self.edge_perm.items():
            cross_edge_dict[''.join(''.join(colors).split(self.cross_color))] = coord

        return cross_edge_dict


    def _bad_flipped_edges(self):
        bad_flip = 0

        for coord, colors in self.edge_perm.items():
            if coord[1] != 0:
                if colors[0] == 'w' or colors[2] == 'w':
                    bad_flip += 1

        return bad_flip


    def _metric_to_solved(self):
        tot_distance = 0

        for color, coord in self.solved_dict.items():
            tot_distance += sum([abs(self.cross_edges[color][i] - coord[i])
                                        for i in range(3)])

        return tot_distance


    def turn_rotate(self, ttype, side, dl=False):
        ## Get the right parameters for the cubie rotation
        p = param_dict[ttype][side]
        new_coords = {}

        ## Choose correct layers to rotate
        if dl:
            turning_layers = [0, p[1]]
        elif side == 'm':
            turning_layers = [0]
        else:
            turning_layers = [p[1]]

        for cubie, colors in self.edge_perm.items():
            if cubie[p[0]] in turning_layers:
                new_coords[(p[2]*cubie[p[3]], p[4]*cubie[p[5]], p[6]*cubie[p[7]])] = \
                          [colors[p[3]], colors[p[5]], colors[p[7]]]
            else:
                new_coords[cubie] = colors

        return new_coords


    def apply_turn(self, turn):
        return self.turn_rotate(*turn_dict[turn])
