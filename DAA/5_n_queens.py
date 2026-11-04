n = int(input("Enter number of Queens: "))

board = [[0 for j in range(n)] for i in range(n)]

row = int(input("Enter first Queen row (0 to n-1): "))
col = int(input("Enter first Queen column (0 to n-1): "))

# Validate position
if not (0 <= row < n and 0 <= col < n):
    print("Invalid position")

else:
    board[row][col] = 1

def is_safe(board, row, col, n):

    # Check upper column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):

    if row == n:
        return True

    # Skip the row containing the first Queen
    if 1 in board[row]:
        return solve(board, row + 1, n)

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False

if solve(board, 0, n):

    print("Final N-Queens Matrix:")

    for row in board:
        print(row)

else:
    print("No solution exists for this position.")


#INPUT
#Enter number of Queens: 4
#Enter first Queen row (0 to n-1): 0
#Enter first Queen column (0 to n-1): 1