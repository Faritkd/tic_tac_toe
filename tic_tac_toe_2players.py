board = [' ' for _ in range(9)]


# Check if any player has won. These are the patterns for winning in tic_tac_toe.
def check_win(player):
    return (
            (board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)
    )


# Check if the board is full
def is_board_full():
    return ' ' not in board


# Main game loop
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()

        # Get player's move
        move = int(input("Player " + current_player + ", choose a position (1-9): "))

        # Place the player's mark on the board
        board[move - 1] = current_player

        # Check if the player has won
        if check_win(current_player):
            print_board()
            print("Player " + current_player + " wins!")
            game_over = True
        # Check if the game is a tie
        elif is_board_full():
            print_board()
            print("It's a tie!")
            game_over = True
        else:
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'


# Function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')


play_game()
