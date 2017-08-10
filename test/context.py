import os
import sys


CUBE_DIR = os.path.join('\\'.join(os.getcwd().split('\\')[:-1]), 'src')
if CUBE_DIR not in sys.path:
    sys.path.insert(0, CUBE_DIR)
