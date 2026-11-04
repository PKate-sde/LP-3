profit = [60, 100, 120]
weight = [10, 20, 30]

capacity = 50
n = len(profit)



ratio = []

for i in range(n):
    ratio.append(profit[i] / weight[i])

# Sort items by ratio in descending order
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



print("Maximum profit obtained using Greedy Method:", total_profit)