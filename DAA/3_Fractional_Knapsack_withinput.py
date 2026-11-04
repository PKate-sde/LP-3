n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    p = int(input("Enter profit: "))
    w = int(input("Enter weight: "))

    profit.append(p)
    weight.append(w)

capacity = int(input("Enter knapsack capacity: "))

ratio = []

for i in range(n):
    ratio.append(profit[i] / weight[i])

items = sorted(
    zip(ratio, profit, weight),
    reverse=True
)

print("Sorted items:", items)

total_profit = 0

for r, p, w in items:

    if capacity >= w:
        capacity = capacity - w
        total_profit = total_profit + p

    else:
        total_profit = total_profit + r * capacity
        break

print("Maximum Profit:", total_profit)