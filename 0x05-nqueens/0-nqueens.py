#!/usr/bin/python3
"""
Program that solves the Nqueens problem
"""

import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or board[i] == row + col - i or board[i] == row - col + i:
            return False
    return True


def solve_nqueens(n):
    board = [-1] * n
    solutions = []

    def backtrack(col):
        if col == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
        else:
            for row in range(n):
                if is_safe(board, row, col):
                    board[col] = row
                    backtrack(col + 1)

    backtrack(0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
