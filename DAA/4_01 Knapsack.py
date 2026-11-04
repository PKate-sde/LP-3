n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    p = int(input("Enter profit: "))
    w = int(input("Enter weight: "))

    profit.append(p)
    weight.append(w)

# Validate weights
if any(w <= 0 for w in weight):
    print("Weight must be positive")
else:
    capacity = int(input("Enter knapsack capacity: "))

dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weight[i-1] <= w:
            dp[i][w] = max(
                profit[i-1] + dp[i-1][w - weight[i-1]],
                dp[i-1][w]
            )

        else:
            dp[i][w] = dp[i-1][w]

print("DP Table:")

for row in dp:
    print(row)

print("Maximum Profit:", dp[n][capacity])

w = capacity
print("Selected Items:")

for i in range(n, 0, -1):

    if dp[i][w] != dp[i-1][w]:
        print("Item", i)

        w = w - weight[i-1]


#INPUT
#Enter number of items: 3
#Enter profit: 60
#Enter weight: 10
#Enter profit: 100
#Enter weight: 20
#Enter profit: 120
#Enter weight: 30
#Enter knapsack capacity: 50