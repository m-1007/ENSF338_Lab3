import random
import time
import matplotlib.pyplot as plt

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

# Function to generate arrays for best, worst, and average cases
def generate_arrays(size):
    # Best case: Sorted array
    best_case = list(range(size))
    
    # Worst case: Reverse sorted array
    worst_case = list(range(size, 0, -1))
    
    # Average case: Randomly shuffled array
    average_case = random.sample(range(size * 2), size)
    
    return best_case, worst_case, average_case

# Function to measure execution time of a sorting algorithm
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Experiment with different input array sizes
array_sizes = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000,
               80000, 90000]

# Perform the experiment for both bubble sort and quicksort
for size in array_sizes:
    #print(f"Array size: {size}")
    best_case, worst_case, average_case = generate_arrays(size)
    
    # Bubble sort
    bubble_time_best = measure_time(bubble_sort, best_case.copy())
    bubble_time_worst = measure_time(bubble_sort, worst_case.copy())
    bubble_time_average = measure_time(bubble_sort, average_case.copy())
    
    print(f"Bubble sort - Best case: {bubble_time_best:.6f} seconds")
    print(f"Bubble sort - Worst case: {bubble_time_worst:.6f} seconds")
    print(f"Bubble sort - Average case: {bubble_time_average:.6f} seconds")
    
    # Quicksort
    quicksort_time_best = measure_time(quicksort, best_case.copy())
    quicksort_time_worst = measure_time(quicksort, worst_case.copy())
    quicksort_time_average = measure_time(quicksort, average_case.copy())
    
    print(f"Quicksort - Best case: {quicksort_time_best:.6f} seconds")
    print(f"Quicksort - Worst case: {quicksort_time_worst:.6f} seconds")
    print(f"Quicksort - Average case: {quicksort_time_average:.6f} seconds")


#2.3: Generate performance plots for all the six (three?) cases. 
    # Performance of both algorithms must be visualized in each plot. 
    # In the plots, highlight for which inputs one algorithm perform better than the other

for case_name in ["Best", "Worst", "Average"]:
    plt.figure(figsize=(10, 6))
    plt.title(f"Performance Comparison - {case_name} Case")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")

    for sort_func, label in [(bubble_sort, "Bubble Sort"), (quicksort, "Quicksort")]:
        execution_times = []
        for size in array_sizes:
            best_case, worst_case, average_case = generate_arrays(size)
            if case_name == "Best":
                execution_time = measure_time(sort_func, best_case.copy())
            elif case_name == "Worst":
                execution_time = measure_time(sort_func, worst_case.copy())
            else:
                execution_time = measure_time(sort_func, average_case.copy())
            execution_times.append(execution_time)
        plt.plot(array_sizes, execution_times, label=label)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


#2.4: Since quicksort consistently outperforms bubble sort for all array sizes in the worst and average cases, we can focus on the best case scenario to determine the threshold.
# From the best case scenario plot, we observe that bubble sort's performance starts to degrade noticeably as the array size increases beyond approximately 3000 elements. 
# Therefore, we could consider a threshold of around 3000 elements.
# However, since bubble sort's performance advantage over quicksort is relatively small even for small array sizes, and quicksort performs consistently better overall,
# it might be more practical to set the threshold slightly higher to benefit from quicksort's efficiency.
# Based on the analysis and to ensure a clear advantage for quicksort, we could choose a threshold of around 5000 elements.
# Therefore, I would choose a threshold of 5000 elements based on the plots' analysis and the practical benefits of leveraging quicksort's efficiency for larger array sizes.