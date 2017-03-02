# CFOP Cube Solver
This is a Python project to create a program to solve a 3x3 Rubik's cube via the CFOP method. The CFOP method is by far the most popular and well developed speedsolving method in the cubing community. It consists of four steps:

1. Cross: creating a cross on one of the six sides of the cube whereby the four involved edge pieces align with their respective colors.
2. F2L (First Two Layers): One by one, 2x1 edge-corner pairs are created and placed into their respective places finishing the the first two layers.
3. OLL (Orientation Last Layer): The orientation of the last eight pieces (not including the center piece) are corrected such that these pieces have the same color pointing in the direction of the center piece.
4. PLL (Permutation Last Layer): The final step where the permutation of the correctly orientated pieces is solved such that they are all placed in their correct spots without affecting their orientation thus solving the cube.

## 1) Important Facts About the Cube
There are many small facts and details about the cube that come as second nature to speedcubing and taken largely for granted that can be quite unintuitive at first glance or even after some thought. I lay below out some of these ideas so as to give a better and quick understanding about the cube.

### 1.1) Centers and Colors
The centers of a cube are immutable. By this I mean that they do not and cannot move and their position relative to one another will always
be the same, relatively speaking. There are six colors: yellow and white, blue and green, and red and orange. They are paired up because those pairs are opposites on the cube and always will be. This color scheme is what will usually be seen but don't be surprised if other color schemes are seen.

### 1.2) Corners and Edges
Similar to centers, corner pieces and edge pieces are in a way immutable. A red-green-white corner piece will always be a red-green-white corner piece and so on. Furthermore, a piece will never have two opposite colors on it since that cannot happen.

## 2) Usual Terms and Syntax
This project is riddled with cubing terms that may be anywhere from easy to understand to obscure and mysterious. I make some explanation in the code, but it'd be more clear to lay it all out here.

### 2.1) Algorithms
To denote specific turns on the cube and to represent algorithm clearly a syntax was created and it is as follows:

- The Up, Left, Front, Right, Back and Down faces are represented by U, L, F, R, B and D respectively.
- If a clockwise turn is to be made, the uppercase letter as shown above is used.
- If a counterclockwise turn is to be made, the uppercase letter followed by an apostrophy is used (e.g. U' is "U prime").
- A double turn (i.e. 180 degree turn) is represented by a "2" follow the face that is to be turned.
- A double layer turn is represented as the lowercase letter (e.g. u is the clockwise turn of the up two layers).
- M, E and S represent middle slice turns but seldom are either E or S used. The M turn follows the direction of the left face.
- Rotations are represented by x, following the right face, y, following the top face, and z, following the front face.

### 2.2) Other terms
- AUF - Stands for Adjust Up Face. This is the adjustment of the up face for preparation of OLL or PLL since rotations of the cube are very costly in time. It is faster to turn the up face, do an algorithm and turn the up face back
- Trigger - A short move sequence that appears in many different situations and algorithms. You will often see parentheses or square brackets used in algorithms as a way of denoting different triggers. The most popular trigger is probably the sexy move: (R U R' U'). 
