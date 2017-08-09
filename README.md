# CFOP Cube Solver
This is a Python project to create a program to solve a 3x3 Rubik's cube via the CFOP method. The CFOP method is by far the most popular and well developed speedsolving method in the cubing community. It consists of four steps:

<img title="Cross" src="https://github.com/crumpstrr33/CFOP-cube-solver/blob/master/pics/before_f2l.jpg?raw=true" width="218" height="218"><img title="F2L" src="https://github.com/crumpstrr33/CFOP-cube-solver/blob/master/pics/before_oll.jpg?raw=true" width="218" height="218"><img title="OLL" src="https://github.com/crumpstrr33/CFOP-cube-solver/blob/master/pics/before_pll.jpg?raw=true" width="218" height="218"><img title="PLL" src="https://github.com/crumpstrr33/CFOP-cube-solver/blob/master/pics/solved.jpg?raw=true" width="218" height="218">

1. Cross: creating a cross on one of the six sides of the cube whereby the four involved edge pieces align with their respective colors. 
2. F2L (First Two Layers): One by one, 2x1 edge-corner pairs are created and placed into their respective places finishing the the first two layers.
3. OLL (Orientation Last Layer): The orientation of the last eight pieces (not including the center piece) are corrected such that these pieces have the same color pointing in the direction of the center piece.
4. PLL (Permutation Last Layer): The final step where the permutation of the correctly orientated pieces is solved such that they are all placed in their correct spots without affecting their orientation thus solving the cube.

For more information, there are a myriad resources on the web. Check out the [wikipedia page](https://en.wikipedia.org/wiki/CFOP_Method) or the [speedsolving wiki page](https://www.speedsolving.com/wiki/index.php/CFOP) to better understand teh CFOP method. Also here's some pages for [general information](https://www.speedsolving.com/wiki/index.php/General_Information), for [terminology](https://www.speedsolving.com/wiki/index.php/Category:Terminology) and for [notation](https://www.speedsolving.com/wiki/index.php/3x3x3_notation).
