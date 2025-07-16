import os

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
test_board = [' '] * 10
display_board(test_board)
# Function to check if the game is over
def check_winner(board):
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False
# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board[1:]
# Function to play the game
def play_game():
    board = [' '] * 10
    current_player = 'X'
    
    while True:
        display_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if move < 1 or move > 9 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
            board[move] = current_player
            
            if check_winner(board):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if is_board_full(board):
                display_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
    print("Game over!")
if __name__ == "__main__":
    play_game()
