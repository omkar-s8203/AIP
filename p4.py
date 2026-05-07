# N-Queens Problem using Backtracking

N = 4

board = [[0]*N for _ in range(N)]

# Check if queen can be placed
def is_safe(row, col):

    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Solve using backtracking
def solve(col):

    if col >= N:
        return True

    for i in range(N):

        if is_safe(i, col):

            board[i][col] = 1

            if solve(col + 1):
                return True

            # Backtrack
            board[i][col] = 0

    return False

# Main
if solve(0):

    for row in board:
        print(row)

else:
    print("No Solution")