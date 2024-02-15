import timeit
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Step 2: Measure performance on 100 random tasks
def measure_performance(search_function, array_size):
    array = random.sample(range(array_size), array_size)
    target = random.randint(0, array_size - 1)

    start_time = timeit.default_timer()
    result = search_function(array, target)
    end_time = timeit.default_timer()

    return end_time - start_time

# Step 3: Perform measurements for different input sizes
array_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_search_times = []
binary_search_times = []

for size in array_sizes:
    linear_time = measure_performance(linear_search, size)
    binary_time = measure_performance(binary_search, size)

    linear_search_times.append(linear_time)
    binary_search_times.append(binary_time)

# Step 4: Plot the results
plt.plot(array_sizes, linear_search_times, label='Linear Search')
plt.plot(array_sizes, binary_search_times, label='Binary Search with Quicksort')
plt.title('Performance Comparison of Linear and Binary Search')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
