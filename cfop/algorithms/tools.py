'''
Contains various useful functions that are used throughout this project.
'''
from string import ascii_lowercase, ascii_uppercase
from random import choice

import numpy as np


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

    alg_chars = 'ulfrbdMxyzULFRBD'
    code_chars = '1234567890!@#$%^'

    # Checks if syntax is correct
    for n, turn in enumerate(alg):
        if turn not in alg_chars + "2' ":
            raise Exception('Incorrect syntax; ' +
                            "found '{}' in passed algorithm: ".format(turn) +
                            '{}'.format(alg))
        elif turn == '2' and alg[n - 1] not in alg_chars:
            raise Exception('Incorrect syntax; ' +
                            "Found multiple 2's in a row in {}.".format(alg))

    for n, let in enumerate(alg):
        # Don't do anything for these since they are modifiers, not turns
        if let in ["'", '2', ' ']:
            continue

        if n == alg_len:
            code += let
            return code

        # Double turns
        if alg[n + 1] == '2':
            code += code_chars[alg_chars.index(let)]
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
        # CW turns/rotations
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
    alg_chars = 'ulfrbdMxyzULFRBD'
    code_chars = '1234567890!@#$%^'
    ccw_lets = ['a', 'c', 'e', 'k', 'q', 't']

    # Checks if syntax is correct
    for turn in code:
        if turn.lower() not in code_chars + 'ulfrbdmxyztkeqac':
            raise Exception('Incorrect syntax; '
                            "found '{}' in passed algorithm: ".format(turn) +
                            '{}'.format(code))

    for n, let in enumerate(code):
        # Double turns
        if let in code_chars:
            alg += alg_chars[code_chars.index(let)] + '2'
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

        if n + 1 != len(code):
            alg += ' '

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


def random_scramble(num_turns, alg_syntax=False):
    """
    Creates a random scramble for a cube. Duplicate moves such as D D' or F F2
    and so on are avoided along with 'sandwich moves' such as L R L2 where the
    meat of the sandwich is the opposite face of the bread.

    Parameters:
    num_turns - The length of the algorithm
    alg_syntax - (default False) If true, the function will return the scramble
                 as a human-readable algorithm otherwise it will be return as
                 the code syntax
    """
    turn_space = 'UT!LK@FE#DC^RQ$BA%'

    duplicate_turn, dupe_opp_turn = '', ''
    alg = ''
    for n in range(num_turns):
        current_turn_space = turn_space.replace(duplicate_turn, '')
        current_turn_space = current_turn_space.replace(dupe_opp_turn, '')

        turn = choice(list(current_turn_space))
        alg += turn

        # Removes certain turns for the next turn
        # Index of the triplet that the current turn belongs to
        # e.g. ^ belongs to DC^ or E belongs to FE#
        trip_ind = 3 * (turn_space.index(turn) // 3)

        # Don't turn same face twice in a row
        duplicate_turn = turn_space[trip_ind: trip_ind + 3]

        # Prevents moves like L R L or B D2 B', etc.
        if n > 1:
            # Find opposite side trip_ind
            opp_trip_ind = (trip_ind + len(turn_space) // 2) % len(turn_space)
            opp_turn = turn_space[opp_trip_ind: opp_trip_ind + 3]

            if alg[n - 1] in opp_turn:
                dupe_opp_turn = opp_turn
        else:
            dupe_opp_turn = ''

    if alg_syntax:
        return code_to_alg(alg)

    return alg
