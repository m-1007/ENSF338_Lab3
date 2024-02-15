import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(size):
    array = generate_random_array(size)
    start_time = timeit.default_timer()
    quicksort(array)
    end_time = timeit.default_timer()
    return end_time - start_time

# more complex function to fit
def complex_function(x, a, b, c):
    return a * x**2 + b * x + c

# Sizes of inputs
sizes = np.array([10, 50, 100, 200, 500, 1000])

# Measure time for each input
times = np.array([measure_time(size) for size in sizes])

params, covariance = curve_fit(complex_function, sizes, times)

# Plot
plt.plot(sizes, times, marker='o', label='Actual Times')
plt.plot(sizes, complex_function(sizes, *params), '--', label='Curve Fit')


plt.title('Quicksort Worst-Case Complexity')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')

plt.show()

