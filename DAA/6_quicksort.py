import random
import time

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

if n <= 0 or len(arr) != n:
    raise ValueError("Please enter a valid number of elements.")

print("Original Array:", arr)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = []
    middle = []
    right = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)

    return (randomized_quick_sort(left) +
            middle +
            randomized_quick_sort(right))

# Deterministic Quick Sort
start = time.perf_counter()
result1 = deterministic_quick_sort(arr.copy())
time1 = time.perf_counter() - start

print("\nDeterministic Quick Sort:", result1)
print("Execution Time:", time1)

# Randomized Quick Sort
start = time.perf_counter()
result2 = randomized_quick_sort(arr.copy())
time2 = time.perf_counter() - start

print("\nRandomized Quick Sort:", result2)
print("Execution Time:", time2)