

#3.1: Derive the formulas for 
    # (i) number of comparisons, and 
    # (ii) average-case number of swaps for bubble sort

#Bubble Sort:
# In each pass through the array, adjacent elements are compared, and if they are in the wrong order, they are swapped.
# In the worst-case scenario, the array is sorted in reverse order, 
    # requiring n - 1 comparisons and swaps in the first pass, n - 2 in the second pass, and so on until the array is fully sorted.
# In the best-case scenario, the array is already sorted, requiring only n - 1 comparisons and 0 swaps in the first pass. 
# No further swaps are needed since the array is already sorted after the first pass.
# In the average-case scenario, each element has a probability of 0.5 of being in the wrong order with its adjacent element. 
# Therefore, the average number of comparisons can be approximated as (n - 1) / 2.

#3.2-3.3

import random
import matplotlib.pyplot as plt

# Bubble sort implementation with counting comparisons and swaps
def bubble_sort_count(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

# Function to generate arrays for average-case complexity analysis
def generate_average_case_array(size):
    return list(range(size, 0, -1))

# Run bubble sort with counting on inputs of increasing size
input_sizes = [10, 50, 100, 500, 1000, 2000, 5000, 10000]
comparisons_data = []
swaps_data = []

for size in input_sizes:
    arr = generate_average_case_array(size)
    comparisons, swaps = bubble_sort_count(arr)
    comparisons_data.append(comparisons)
    swaps_data.append(swaps)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, comparisons_data, label='Number of Comparisons', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Count')
plt.title('Number of Comparisons in Bubble Sort')
plt.legend()
plt.grid(True)
plt.show()

# Save the figure
plt.savefig('bubble_sort_comparisons.png')
plt.show()


# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, swaps_data, label='Number of Swaps', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Count')
plt.title('Performance of Bubble Sort with Counting')
plt.legend()
plt.grid(True)
plt.show()

# Save the figure
plt.savefig('bubble_sort_swaps.png')
plt.show()


#3.4: The number of comparisons shows a linear relationship with the input size, consistent with the average-case complexity of O(n^2) for bubble sort.
# The number of swaps also exhibits a similar linear relationship with the input size, indicating that bubble sort typically performs a quadratic number of swaps in the average case.
# The plots match the expected complexity analysis for bubble sort, confirming that the algorithm's performance aligns with its theoretical complexity.