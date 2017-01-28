
u, l, f = 'turn_up', 'turn_left', 'turn_front'
r, b, d = 'turn_right', 'turn_back', 'turn_down'
m = 'turn_xmiddle'
x, y, z = 'rotate_x', 'rotate_y', 'rotate_z'

turn_dict = {'U' : [u, 1, False], 'T' : [u, -1, False], '!' : [u, 2, False],
             'L' : [l, 1, False], 'K' : [l, -1, False], '@' : [l, 2, False],
             'F' : [f, 1, False], 'E' : [f, -1, False], '#' : [f, 2, False],
             'R' : [r, 1, False], 'Q' : [r, -1, False], '$' : [r, 2, False],
             'B' : [b, 1, False], 'A' : [b, -1, False], '%' : [b, 2, False],
             'D' : [d, 1, False], 'C' : [d, -1, False], '^' : [d, 2, False],
             'u' : [u, 1, True], 't' : [u, -1, True], '1' : [u, 2, True],
             'l' : [l, 1, True], 'k' : [l, -1, True], '2' : [l, 2, True], 
             'f' : [f, 1, True], 'e' : [f, -1, True], '3' : [f, 2, True],
             'r' : [r, 1, True], 'q' : [r, -1, True], '4' : [r, 2, True],
             'b' : [b, 1, True], 'a' : [b, -1, True], '5' : [b, 2, True],
             'd' : [d, 1, True], 'c' : [d, -1, True], '6' : [d, 2, True],
             'M' : [m, 1, 'm'], 'm' : [m, -1, 'm'], '7' : [m, 2, 'm'],
             'x' : [x, True, False], 'X' : [x, False, False], '8' : [x, False, True],
             'y' : [y, True, False], 'Y' : [y, False, False], '9' : [y, False, True],
             'z' : [z, True, False], 'Z' : [z, False, False], '0' : [z, False, True]}