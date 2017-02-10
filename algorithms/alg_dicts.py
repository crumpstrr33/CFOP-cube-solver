u, l, f = 'turn_up', 'turn_left', 'turn_front'
r, b, d = 'turn_right', 'turn_back', 'turn_down'
m = 'turn_middle'
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


oll_dict = {'10210001' : 'case_01', '10212112' : 'case_02', '20102010' : 'case_03',
            '11200001' : 'case_04', '10211011' : 'case_05', '00001121' : 'case_06',
            '21111020' : 'case_07', '11101001' : 'case_08', '00202121' : 'case_09',
            '11111101' : 'case_10', '21210121' : 'case_11', '11212111' : 'case_12',
            '10202010' : 'case_13', '10111001' : 'case_14', '00212021' : 'case_15',
            '00210011' : 'case_16', '00010001' : 'case_17', '01010101' : 'case_18',
            '10211021' : 'case_19', '20110001' : 'case_20', '20100000' : 'case_21',
            '10002000' : 'case_22', '01001120' : 'case_23', '11211121' : 'case_24',
            '01100021' : 'case_25', '01211101' : 'case_26', '11212010' : 'case_27',
            '20011100' : 'case_28', '01210010' : 'case_29', '21101120' : 'case_30',
            '01210111' : 'case_31', '21010111' : 'case_32', '21200021' : 'case_33',
            '20012120' : 'case_34', '20002020' : 'case_35', '10101000' : 'case_36',
            '10210100' : 'case_37', '20010110' : 'case_38', '11211020' : 'case_39',
            '10211120' : 'case_40', '11111000' : 'case_41', '00110120' : 'case_42',
            '00101111' : 'case_43', '01000001' : 'case_44', '10010021' : 'case_45',
            '20012021' : 'case_46', '10110011' : 'case_47', '00102000' : 'case_48',
            '11201120' : 'case_49', '21100001' : 'case_50', '21110000' : 'case_51',
            '10012001' : 'case_52', '20111120' : 'case_53', '20110100' : 'case_54',
            '01201001' : 'case_55', '10110110' : 'case_56', '20202101' : 'case_57',
            '00000000' : 'SOLVED'}


pll_dict = {'300113021232' : 'aa_perm', '001212320133' : 'ab_perm', '010121202333' : 'ua_perm', 
            '020101212333' : 'ub_perm', '330111223002' : 'ja_perm', '000122311233' : 'jb_perm',
            '320101223032' : 'ra_perm', '300121213032' : 'rb_perm', '020112301233' : 't_perm' ,
            '230113022301' : 'y_perm' , '200113032321' : 'v_perm' , '021210102333' : 'f_perm' ,
            '323011230102' : 'ga_perm', '131203022310' : 'gb_perm', '121203012330' : 'gc_perm',
            '313031220102' : 'gd_perm', '030121212303' : 'z_perm' , '103012321230' : 'e_perm' ,
            '020131202313' : 'h_perm' , '200133022311' : 'na_perm', '002331220113' : 'nb_perm',
            '000111222333' : 'SOLVED'}

