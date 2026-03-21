#Implement Tic-Tac-Toe game using Python


import random
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)
def get_player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column: 1 2): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if row in range(3) and col in range(3):
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell is already taken. Try again.")
            else:
                print("Row and column must be between 1 and 3.")
        except:
            print("Invalid input. Please enter two numbers.")
def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)
def tic_tac_toe_vs_computer():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'  
    computer = 'O'
    print("Welcome to Tic Tac Toe: You (X) vs Computer (O)")
    print_board(board)
    current = 'X'
    while True:
        if current == player:
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)
            print(f"Computer chooses: {row + 1} {col + 1}")
        board[row][col] = current
        print_board(board)
        if check_winner(board, current):
            if current == player:
                print("You win! 🎉")
            else:
                print("Computer wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break
        current = computer if current == player else player
tic_tac_toe_vs_computer()
