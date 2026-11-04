n = int(input("Enter number of rows: "))

C = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i-1][j-1] + C[i-1][j]

# Print Pascal's Triangle
for i in range(n):
    for j in range(i + 1):
        print(C[i][j], end=" ")
    print()