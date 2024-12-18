def is_safe(board, row, col):
    # Check column conflicts
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, solutions):
    # If all queens are placed
    if row == len(board):
        solutions.append(board[:])
        return

    # Try placing a queen in each column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            solve_n_queens(board, row + 1, solutions)  # Recur to place next queen
            board[row] = -1  # Backtrack and remove the queen

def print_board(board):
    # Print the board in a readable format
    for row in board:
        print(" ".join("Q" if col == row else "." for col in range(len(board))))

def eight_queens():
    n = 8
    board = [-1] * n  # -1 represents an empty cell
    solutions = []
    solve_n_queens(board, 0, solutions)

    print(f"Total Solutions: {len(solutions)}")
    for solution in solutions:
        print_board(solution)
        print()

if __name__ == "__main__":
    eight_queens()
