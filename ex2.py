import random
import time

#2.1: Implement and test both algorithms on input of 20 different sizes. 
    # The choice of sizes is yours, but it must be such that it evidences for which sizes each algorithm is faster

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Function to measure execution time of a sorting algorithm
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# 20 array sizes
array_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000,
               10000000, 20000000, 50000000]

# Determine the threshold size for switching between bubble sort and quicksort
threshold = 1000  

# Perform the experiment
for size in array_sizes:
    # Generate random input array
    arr = [random.randint(0, 100) for i in range(size)]
    
    # Measure execution time for bubble sort if the array size is below the threshold
    if size <= threshold:
        bubble_time = measure_time(bubble_sort, arr.copy())
        print(f"Bubble sort took {bubble_time:.6f} seconds for array of size {size}")
    
    # Measure execution time for quicksort if the array size is above the threshold
    else:
        quicksort_time = measure_time(quicksort, arr.copy())
        print(f"Quicksort took {quicksort_time:.6f} seconds for array of size {size}")
