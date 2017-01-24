import numpy as np
from string import ascii_lowercase, ascii_uppercase


'''
Will convert from regular algorithm syntax to the syntax used in code.
Code syntax is such that each character of the string is one move
(rather than r' being two characters but one move). The conversion works as
follows:
    1) All fat turns stay as lowercase
    2) All regular turns stay as uppercase
    3) Counterclockwise turns are the preceeding letter (e.g. u --> t)
    4) Double turns are represented by numbers (or shift-numbers for fat turns)
       where up - 1, left - 2, front - 3, right - 4, back - 5, down - 6
    6) Middle slices are lowercase for counterclockwise turns and 7 for double
       turns
    5) Rotations are capatlized for counterclockwise turns and 8, 9, 0 for
       double x, y and z rotations respectively
'''
def alg_to_code(alg):
    code = ''
    dt_alg = 'urflbdMxyzURFLBD'
    dt_code = '1234567890!@#$%^'

    alg = np.array(list(alg) + ['END'])

    for n, let in enumerate(alg):
        if let in ["'", '2', 'END']:
            continue

        if alg[n + 1] == '2':
            code += dt_code[dt_alg.index(let)]
        elif alg[n + 1] == "'":
            if let in ['x', 'y', 'z']:
                code += let.upper()
            elif let == 'M':
                code += let.lower()
            elif let.islower():
                code += ascii_lowercase[ascii_lowercase.index(let) - 1]
            else:
                code += ascii_uppercase[ascii_uppercase.index(let) - 1]
        else:
            code += let

    return code


'''
Reverses the above process
'''
def code_to_alg(code):
    alg = ''
    dt_alg = 'urflbdMxyzURFLBD'
    dt_code = '1234567890!@#$%^'
    ccw_lets = ['a', 'c', 'e', 'k', 'q', 't']

    code = np.array(list(code) + ['END'])

    for n, let in enumerate(code):
        if let == 'END':
            continue

        if let in dt_code:
            alg += dt_alg[dt_code.index(let)] + '2'
        elif let in ['X', 'Y', 'Z']:
            alg += let.lower() + "'"
        elif let == 'm':
            alg += let.upper() + "'"
        elif let.lower() in ccw_lets:
            if let.islower():
                alg += ascii_lowercase[ascii_lowercase.index(let) + 1] + "'"
            else:
                alg += ascii_uppercase[ascii_uppercase.index(let) + 1] + "'"
        else:
            alg += let

    return alg