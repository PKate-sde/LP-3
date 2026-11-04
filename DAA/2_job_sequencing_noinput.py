jobs = [
    ('A', 2, 100),
    ('B', 1, 50),
    ('C', 2, 10),
    ('D', 1, 20),
    ('E', 3, 30)
]

# Sort jobs according to profit (descending)
jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)
slots = [None] * max_deadline

profit = 0

for job in jobs:
    for i in range(job[1] - 1, -1, -1):
        if slots[i] is None:
            slots[i] = job[0]
            profit += job[2]
            break

print("Scheduled Jobs:", slots)
print("Maximum Profit:", profit)