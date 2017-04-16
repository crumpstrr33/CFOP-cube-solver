import numpy as np
from string import ascii_lowercase, ascii_uppercase


def alg_to_code(alg):
    """
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

    Parameters:
    alg - The cubing algorithm to convet to code syntax
    """
    code = ''
    alg_len = len(alg) - 1

    ele_alg = 'ulfrbdMxyzULFRBD'
    ele_code = '1234567890!@#$%^'

    # Checks if syntax is correct
    for turn in alg:
        if turn in ele_code.replace('2', ''):
            raise Exception('Incorrect syntax;' +
                            'found {} in passed algorithm'.format(turn))

    for n, let in enumerate(alg):
        # Don't do anything for these since they are modifiers
        # and not actual turns
        if let in ["'", '2', 'END', " "]:
            continue

        if n == alg_len:
            code += let
            return code

        # Double turns
        if alg[n + 1] == '2':
            code += ele_code[ele_alg.index(let)]
        # CCW turns
        elif alg[n + 1] == "'":
            # Rotations
            if let in ['x', 'y', 'z']:
                code += let.upper()
            # Middle slice
            elif let == 'M':
                code += let.lower()
            # Turns
            elif let.islower():
                code += ascii_lowercase[ascii_lowercase.index(let) - 1]
            else:
                code += ascii_uppercase[ascii_uppercase.index(let) - 1]
        # CW turns and rotations
        else:
            code += let

    return code


def code_to_alg(code):
    """
    Does the reverse of alg_to_code. See alg_to_code for details.

    Parameters:
    code - The code syntax to convert to cubing algorithm
    """
    alg = ''
    ele_alg = 'ulfrbdMxyzULFRBD'
    ele_code = '1234567890!@#$%^'
    ccw_lets = ['a', 'c', 'e', 'k', 'q', 't']

    # Checks if syntax is correct
    for turn in alg:
        if turn in ["'", '2']:
            raise Exception('Incorrect syntax;'
                            'found {} in passed algorithm'.format(turn))

    for let in code:
        # Double turns
        if let in ele_code:
            alg += ele_alg[ele_code.index(let)] + '2'
        # CCW rotations
        elif let in ['X', 'Y', 'Z']:
            alg += let.lower() + "'"
        # Middle slice
        elif let == 'm':
            alg += let.upper() + "'"
        # CCW turns
        elif let.lower() in ccw_lets:
            if let.islower():
                alg += ascii_lowercase[ascii_lowercase.index(let) + 1] + "'"
            else:
                alg += ascii_uppercase[ascii_uppercase.index(let) + 1] + "'"
        # CW turns and rotations
        else:
            alg += let

    return alg


def dict_to_list(cube_dict):
    """
    Given a the permutation of the cube as a dict (from a Cube object), this
    returns the permuation as a 6 element list of 9 char strings representing
    the stickers on the cube. This is used to make checks.

    Parameters:
    cube_dict - The perm of a cube in dict form as described in the cube.Cube
                class
    """
    perm = np.zeros((6, 3, 3)).astype(str)

    # Create 6x3x3 lsit of the stickers, just the reverse of what is done in
    # the Cube class
    for cubie in cube_dict:
        if cubie[0] == 1:
            perm[3][abs(cubie[1] - 1)][abs(cubie[2] - 1)] = cube_dict[cubie][0]
        if cubie[0] == -1:
            perm[1][abs(cubie[1] - 1)][cubie[2] + 1] = cube_dict[cubie][0]
        if cubie[1] == 1:
            perm[0][cubie[2] + 1][cubie[0] + 1] = cube_dict[cubie][1]
        if cubie[1] == -1:
            perm[5][abs(cubie[2] - 1)][cubie[0] + 1] = cube_dict[cubie][1]
        if cubie[2] == 1:
            perm[2][abs(cubie[1] - 1)][cubie[0] + 1] = cube_dict[cubie][2]
        if cubie[2] == -1:
            perm[4][abs(cubie[1] - 1)][abs(cubie[0] - 1)] = cube_dict[cubie][2]

    # Join each 3x3 array together as one string
    str_perm = []
    for side in perm:
        str_perm.append(''.join(side.flatten()))

    return str_perm


def alg_output(alg):
    """
    Returns a string for an algorithm with spaces between each move for easy
    readability.

    Parameters:
    alg - Algorithm to add spaces to
    """
    proper_alg = ''
    alg_len = len(alg)

    for n, c in enumerate(alg):
        proper_alg += c

        if n + 1 != alg_len:
            if alg[n + 1] not in ["2", "'"]:
                proper_alg += ' '

    return proper_alg