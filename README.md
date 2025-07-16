This is a simple two-player Tic Tac Toe game created using Python. The game runs in the terminal (command line) and allows two players to play against each other by entering numbers from 1 to 9 to mark their moves as either X or O.

The board layout is based on a number system, where each number represents a position on the 3x3 grid. This helps players to understand where they can place their moves:

7 | 8 | 9
---------
4 | 5 | 6
---------
1 | 2 | 3

When the game starts, the board is empty. Player X always starts the game. Each player takes turns entering a number to place their mark. After every move, the game checks:
If a player has won (3 in a row: horizontally, vertically, or diagonally)
If the game is a draw (the board is full and no one wins)
If a player wins, a message is displayed. If it ends in a draw, it also shows a draw message. The board is cleared and redrawn after each move to make the game look clean and updated.
This project uses simple Python concepts like:

Functions
Loops
Conditionals (if-else)
List indexing
Exception handling (try-except)
The os module (to clear the screen)

It does not require any external libraries and can be run in any Python 3 environment.
Python beginners
Practice with logic and conditions
Learning how games work with simple code

To run the game:
python tictactoe.py
Enjoy the game and feel free to improve it!
