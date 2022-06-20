# Sudoku Game

DOCUMENTATION FOR PYTHON PROJECT

WORKING TITLE: Sudoku 
DESCRIPTION: 
Sudoku is a classic puzzle involving a 9 cross 9 grid of cells, grouped into 9 blocks, each 3 cross 3. 
The player must fill in the empty cells ensuring that – 
No match occurs in any of the following.
(a)	Row
(b)	Column
(c)	The block containing the cell
The project goal is to create a GUI allowing the user to play a randomly generated Sudoku puzzle as well as create a puzzle, to which the game displays the correct answer.
A secondary aim is to make the interface more ergonomic and user-friendly.

DESIGN:
The window provides 3 options to the user: a game, an input solver, and ‘about’.
#	GAME
The  option will open 3 options to the user – Easy, Medium and Hard. Selecting a level will display a puzzle of suitable difficulty. 
Cells of the original puzzle are unmodifiable, unselectable and have grey colored background.
The solver provides a blank grid of 9*9 cells to the user, allowing the user to move around and select a cell of his choice and input a desired number in range(1, 10). The solver allows the user to use the numpad on the keyboard to input numbers. There is a mechanism to display warnings (X / V) if the user gives invalid inputs.
There is a timer in hh:mm:ss format.
Each window has a back button at the bottom left corner, which goes back one window. The final message window has an option to go back to the main menu.


#	SOLVER
This option will give the user an empty grid to fill in a puzzle he wants solved. 
On clicking on a cell, the cell is highlighted with a colored border, and the number entered is displayed in top left corner of cell.
If it is valid, upon pressing 'enter', the number is brought to the center, else the cell is cleared. 
The window has a back button at the bottom left corner, which goes back one window.

#	ABOUT
Some introductory test about the game and an image will be displayed in a stylistic font. There is a back button at the bottom left corner.


IMPLEMENTATION:
"""The Sudoku puzzle solver uses some Python code employing a Recursive call to function, and a Backtracking Algorithm. The Backtracking process makes the solving process much more efficient, as compared to the standard Brute Force Algorithm (which basically checks the validity of every possible combination of numbers in the grid, which involves 9^81 possible solutions!). 
Brute force evaluates all 981 possible combinations (with each cell having an equal probability of containing numbers 1 through 9. The code runs a validity check for each case, even for redundant cases containing like 9*I9 , until it hits a correct solution.)
Backtracking avoids this by building upon the present situation and using only valid test cases to proceed. If however a test case stalls the procedure, the algorithm proceeds backwards and changes the test case. In this way, we avoid several unnecessary comparisons. """

We have used Pygame 1.9 to create the GUI.
The code to create and process display surface objects and the code to solve a Sudoku puzzle are in separate files, laid in the same directory.
The main.py is at the helm of all function calls. All main files have been imported in main.py.
The main.py file contains code for the main menu. Depending on the selection, the corresponding function is called, which changes the 
display surface. 
Our program uses only one display surface until closure.
Each one of us has contributed separate files.
