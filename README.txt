1.	Homepage (App.py)
This is the starting page of the program in which with the help of tkinter and PIL (Python Imaging Library) two buttons are made of Start game and Quit. Start game will direct user to the validator and quit game will exit the window.
2.	Validator.py
In this page, there is a field given to the user to enter the choice of method to solve the maze. If correct input is given, it will return ‘BFS’ or ‘DFS’ to solveMaze.
3.	generateMaze.py
In this page, a maze is created by using pre-ordered DFS.
4.	maze.py
In this module, every function that are used in generateMaze and solveMaze are created. 
5.	solveMaze.py
In this page, the maze will be solved according to the method returned by validator.
