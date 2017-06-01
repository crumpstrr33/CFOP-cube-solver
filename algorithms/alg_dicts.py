'''
Used in Cube's turn_rotate method to use the correct indices of the cube when
applying a turn or rotation.
'''
PARAM_DICT = {
    # Clockwise turns
    'cw': {
        'u': [1, 1, -1, 2,  1, 1,  1, 0], 'd': [1, -1,  1, 2,  1, 1, -1, 0],
        'r': [0, 1,  1, 0,  1, 2, -1, 1], 'l': [0, -1,  1, 0, -1, 2,  1, 1],
        'f': [2, 1,  1, 1, -1, 0,  1, 2], 'b': [2, -1, -1, 1,  1, 0,  1, 2]},

    # Counterclockwise turns
    'ccw': {
        'u': [1, 1,  1, 2,  1, 1, -1, 0], 'd': [1, -1, -1, 2,  1, 1,  1, 0],
        'r': [0, 1,  1, 0, -1, 2,  1, 1], 'l': [0, -1,  1, 0,  1, 2, -1, 1],
        'f': [2, 1, -1, 1,  1, 0,  1, 2], 'b': [2, -1,  1, 1, -1, 0,  1, 2]},

    # Double turns (180 degrees)
    'dt': {
        'u': [1, 1, -1, 0,  1, 1, -1, 2], 'd': [1, -1, -1, 0,  1, 1, -1, 2],
        'r': [0, 1,  1, 0, -1, 1, -1, 2], 'l': [0, -1,  1, 0, -1, 1, -1, 2],
        'f': [2, 1, -1, 0, -1, 1,  1, 2], 'b': [2, -1, -1, 0, -1, 1,  1, 2]}
}


'''
Used in Cube's and CrossEdges's apply_alg methods to conver from the code
syntax for turns to actually applying the turns.
'''
TURN_DICT = {
    # Single layer turns
    'U': ['cw', 'u'], 'T': ['ccw', 'u'], '!': ['dt', 'u'],
    'L': ['cw', 'l'], 'K': ['ccw', 'l'], '@': ['dt', 'l'],
    'F': ['cw', 'f'], 'E': ['ccw', 'f'], '#': ['dt', 'f'],
    'R': ['cw', 'r'], 'Q': ['ccw', 'r'], '$': ['dt', 'r'],
    'B': ['cw', 'b'], 'A': ['ccw', 'b'], '%': ['dt', 'b'],
    'D': ['cw', 'd'], 'C': ['ccw', 'd'], '^': ['dt', 'd'],
    'M': ['cw', 'm'], 'm': ['ccw', 'm'], '7': ['dt', 'm'],

    # Double layer turns
    'u': ['cw', 'u', True], 't': ['ccw', 'u', True], '1': ['dt', 'u', True],
    'l': ['cw', 'l', True], 'k': ['ccw', 'l', True], '2': ['dt', 'l', True],
    'f': ['cw', 'f', True], 'e': ['ccw', 'f', True], '3': ['dt', 'f', True],
    'r': ['cw', 'r', True], 'q': ['ccw', 'r', True], '4': ['dt', 'r', True],
    'b': ['cw', 'b', True], 'a': ['ccw', 'b', True], '5': ['dt', 'b', True],
    'd': ['cw', 'd', True], 'c': ['ccw', 'd', True], '6': ['dt', 'd', True],

    # Rotations
    'x': ['cw', 'x'], 'X': ['ccw', 'x'], '8': ['dt', 'x'],
    'y': ['cw', 'y'], 'Y': ['ccw', 'y'], '9': ['dt', 'y'],
    'z': ['cw', 'z'], 'Z': ['ccw', 'z'], '0': ['dt', 'z']
}
