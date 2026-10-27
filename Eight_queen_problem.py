N = 8

# create an N X N chessboard
board = [["." for _ in range(N)] for _ in range(N)]

# Function to check whether a queen can be placed.
def is_safe(row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False
            
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
        
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
        
    return True

# backtracking function
def solve_queens(row):
    if row == N:
        return True
        
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"
            
            if solve_queens(row + 1):
                return True
                
            board[row][col] = "."
            
    return False

if solve_queens(0):
    print("Solution for 8-Queens Problem:")
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")

"""
OUTPUT:
Solution for 8-Queens Problem:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
"""
