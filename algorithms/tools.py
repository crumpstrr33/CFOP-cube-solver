import numpy as np
from string import ascii_lowercase, ascii_uppercase


def alg_to_code(alg):
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

    Parameters:
    alg - The cubing algorithm to convet to code syntax
    '''
    code = ''
    ele_alg = 'ulfrbdMxyzULFRBD'
    ele_code = '1234567890!@#$%^'

    ## Checks if syntax is correct
    for turn in alg:
        if turn in ele_code.replace('2', ''):
            raise Exception('Incorrect syntax; found %s in passed algorithm' % turn)

    ## Add END element so the index of n+1 doesn't throw an error
    alg = np.array(list(alg) + ['END'])

    for n, let in enumerate(alg):
        ## Don't do anything for these since they are modifiers and not actual turns
        if let in ["'", '2', 'END']:
            continue

        if alg[n + 1] == '2':
            code += ele_code[ele_alg.index(let)]
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



def code_to_alg(code):
    '''
    Does the reverse of alg_to_code. See alg_to_code for details.

    Parameters:
    code - The code syntax to convert to cubing algorithm
    '''
    alg = ''
    ele_alg = 'ulfrbdMxyzULFRBD'
    ele_code = '1234567890!@#$%^'
    ccw_lets = ['a', 'c', 'e', 'k', 'q', 't']

    ## Checks if syntax is correct
    for turn in alg:
        if turn in ["'", '2']:
            raise Exception('Incorrect syntax; found %s in passed algorithm' % turn)

    ## Add END element so the index of n+1 doesn't throw an error
    code = np.array(list(code) + ['END'])

    for n, let in enumerate(code):
        if let == 'END':
            continue

        if let in ele_code:
            alg += ele_alg[ele_code.index(let)] + '2'
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


def opposite(corf, which_opposite):
    '''
    Gives the opposite color or face based of the cube.
    
    Parameters:
    corf - The color or face whose opposite is to be found
    which_opposite - Either 'colors' or 'faces' to choose which to find
    '''
    if which_opposite == 'colors':
        colors = ['w', 'y', 'g', 'b', 'r', 'o']
        opposite_colors = ['y', 'w', 'b', 'g', 'o', 'r']
        return opposite_colors[colors.index(corf)]
    elif which_opposite == 'faces':
        faces = ['u', 'd', 'r', 'l', 'f', 'b']
        opposite_faces = ['d', 'u', 'l', 'r', 'b', 'f']
        return opposite_faces[faces.index(corf)]


def face_to_rotation(face, dl):
    faces = ['u', 'd', 'r', 'l', 'f', 'b']

    if dl:
        rotation = ['y', 'y', 'x', 'x', 'z', 'z']
        direction = [1, -1, 1, -1, 1, -1]
        return rotation[faces.index(face)], direction[faces.index(face)]
    else:
        rotation = ['', 'x', 'z', 'z', 'x', 'x']
        direction = [2, 2, -1, 1, 1, -1]
        return rotation[faces.index(face)], direction[faces.index(face)]