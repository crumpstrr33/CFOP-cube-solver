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


oll_dict =  {'01010101' : 'flip_tshirt',        '01100011' : 'a_moustache',
             '10010001' : 'squeegee_agun',      '10011100' : 'fishsalad_mountedfish',
             '01010111' : 'a_sune',             '00010011' : 'gun_asqueegee',
             '00110100' : 'upstairs_lightning', '00011100' : 'leftysquare_rightysquare',
             '01001001' : 'a_kite',             '10110100' : 'aspotcham_dalmation', 
             '01111000' : 'couch_apee',         '00011011' : 'city_cingheadlights',  
             '10100000' : 'bunny_crown',        '00001000' : 'a_mouse',
             '00000000' : 'blank_zamboni',      '01111101' : 'chameleon_headlights', 
             '00111001' : 'key_suitup',         '10000101' : 'alightning_downstairs',
             '00111100' : 'acouch_pee',         '01101001' : 'spotcham_adalmation',
             '01000001' : 'a_breakneck_a_fryingpan_rfsqueezy_rbsqueezy',
             '01000100' : 'highway_ricecooker_streetlights_ant',
             '10001000' : 'slash', '01110111' : 'diagonal', '00110011' : 'fung',
             '10011001' : 'afung', '10101010' : 'checkers', '10111110' : 'stealth',
             '10111011' : 'brick'}