#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def nqueens(n):
    # Check if n is an integer greater or equal to 4
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board
    board = [["." for _ in range(n)] for _ in range(n)]

    # Define a function to check if a queen can be placed at a given position
    def is_valid(row, col):
        # Check if there is a queen in the same row or column
        for i in range(n):
            if board[i][col] == "Q" or board[row][i] == "Q":
                return False
        # Check if there is a queen on the diagonals
        for i in range(n):
            if (row+i < n and col+i < n and board[row+i][col+i] == "Q") or \
               (row-i >= 0 and col-i >= 0 and board[row-i][col-i] == "Q") or \
               (row+i < n and col-i >= 0 and board[row+i][col-i] == "Q") or \
               (row-i >= 0 and col+i < n and board[row-i][col+i] == "Q"):
                return False
        return True

    # Define a recursive function to solve the problem
    def recursive_solve(row, queens, solutions):
        # Base case: all queens have been placed
        if queens == n:
            solutions.append(["".join(row) for row in board])
            return
        # Recursive case: try to place a queen in the current row
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = "Q"
                recursive_solve(row+1, queens+1, solutions)
                board[row][col] = "."
        return

    # Solve the problem
    solutions = []
    recursive_solve(0, 0, solutions)

    # Print the solutions
    for solution in solutions:
        print("\n".join(solution))
        print()


if __name__ == "__main__":
    # Check if the program was called with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
