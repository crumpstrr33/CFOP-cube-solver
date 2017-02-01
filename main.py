from sys import path
DIR = 'C:\\Users\\Jacob\\Documents\\coding_stuff\\Python\\CFOP_solver_3x3'
if DIR not in path:
    path.append(DIR)

from oll import OllCases
from cube import Cube
from algorithms.tools import code_to_alg
from algorithms import oll_algs

def main():
    cube = Cube(['wgbbgrwo', 'owoooooo', 'gwrggggg', 'wwwrrrrr', 'rwbbbbbb', 'yyyyyyyy'])
    top_face = ['w', 0]

    oll = OllCases(cube.perm, top_face)


    print('Use this algorithm to complete OLL:', code_to_alg(getattr(oll_algs, oll.oll)))
    print('But first, do this rotation:', oll.rotation)


if __name__ == "__main__":
    main()