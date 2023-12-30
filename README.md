# Tic Tac Toe Game


### Built with:
python

#### Description:
This project contains a Python file named `tic_tac_toe.py` which is a simplified version of the Tic Tac Toe game. The given code is a Python script that implements a simple Tic Tac Toe game using the command line. It creates a board, defines the winning combinations, and allows the player to make a move by inputting a number corresponding to a position on the board. The computer then makes a move based on a predetermined strategy.

The code starts by defining the board, winners, and possible moves. It then includes functions to print the board, make a move, check if a move is valid, check for a winner, check if there are empty spaces, and make a move for the computer.

The game progresses with the player and computer taking turns making moves until there is a winner or the board is full, at which point the game ends. It prints the board after each move and informs the player if they won or lost. If the player enters an invalid move, they are prompted to try again.

The game utilizes concepts such as lists, loops, conditions, and functions to implement the game logic and user interaction. Here's a breakdown of the functions:

*print_board(): This function prints the current state of the tic-tac-toe board to the console. It uses the termcolor library to colorize the 'x' and 'o' marks on the board.*

*make_move(): This function is used to make a move on the board. It takes the board state, the player making the move, the position of the move, and an optional undo parameter. It checks if the move is valid and updates the board accordingly. It also checks if the move results in a win for the player.*

*can_move(): This function checks if a move is valid by verifying if the chosen position on the board is within the valid range (1-9) and if it's not already occupied.*

*is_winner(): This function checks if a player has won the game by examining all possible winning combinations. It returns True if the player has won and False otherwise.*

*has_empty_space(): This function checks if there are still empty spaces on the board, indicating whether the game is over or not.*

*computer_move(): This function implements the computer's move. It first checks if the computer can make a winning move, then if it needs to block the player's winning move, and finally makes a random move if neither of the previous conditions is met.*

*The remaining part of the code sets up the game by initializing the players, printing the starting board, and allowing the player to make a move. If the player wins or loses, it prints the result and ends the game.*


### Installation:
To run the `tic_tac_toe.py` file, you need to have Python installed on your system. You can download Python from the official website: [Python Official Website](https://www.python.org/)


## Credits:
### The Tic Tac Toe game project was developed by Farzad Mahmoudi Yekta.



