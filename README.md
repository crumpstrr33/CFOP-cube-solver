# CFOP Cube Solver
This is a Python project to create a program to solve a 3x3 Rubik's cube via the CFOP method. The CFOP method is by far the most popular and well developed speedsolving method in the cubing community. It consists of four steps:

1. Cross: creating a cross on one of the six sides of the cube whereby the four involved edge pieces align with their respective colors.
2. F2L (First Two Layers): One by one, 2x1 edge-corner pairs are created and placed into their respective places finishing the the first two layers.
3. OLL (Orientation Last Layer): The orientation of the last eight pieces (not including the center piece) are corrected such that these pieces have the same color pointing in the direction of the center piece.
4. PLL (Permutation Last Layer): The final step where the permutation of the correctly orientated pieces is solved such that they are all placed in their correct spots without affecting their orientation thus solving the cube.

### Current Progress
- Syntax for algorithms has been implemented
- OLL and PLL algorithms now reside in `oll_algs.py` and `pll_algs.py` respectively
- A Cube class has been created which holds the permutation of the cube as in a six element list
- A method to apply an algorithm (either written as a cubing algorithm or in the code syntax) can now be applied to `Cube()`
- OLL cases can now be solved with the `OLLCases` class in `oll_pll.py`. There may be errors since I haven't test every one of the 57 cases.
- PLL cases can now be solved with the `OLLCases` class in `oll_pll.py`. Similar to `OLLCases`.
