import numpy as np
import random
from time import sleep

# Create an empty board
def create_board():
    return np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])

# Check if the player has three of their marks in a row
def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

# Check if the player has three of their marks in a column
def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y, x] != player:
                win = False
                break
        if win:
            return True
    return False

# Check if the player has three of their marks in a diagonal
def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return True

    win = True
    for x in range(len(board)):
        if board[x, len(board) - 1 - x] != player:
            win = False
            break
    return win

# Evaluate the board to check for a winner or tie
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            break
    return winner

# Check for empty places on the board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i, j] == 0:
                l.append((i, j))
    return l

# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    if not selection:  # No empty spaces
        return board
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

# Main function to simulate the Tic-Tac-Toe game
def play_game():
    board = create_board()
    print("Initial Board:")
    print(board)
    winner = 0
    turn = 1

    for i in range(9):  # Maximum of 9 moves
        player = 1 if turn == 1 else 2
        print(f"Player {player}'s turn:")
        board = random_place(board, player)
        print(board)
        sleep(1)

        winner = evaluate(board)
        if winner != 0:
            print(f"Player {winner} wins!")
            return

        turn = 3 - turn  # Switch turns (1 -> 2, 2 -> 1)

    print("It's a tie!")

# Run the game
play_game()
