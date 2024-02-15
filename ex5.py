import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Q1
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid - 1

        arr[left + 1:i + 1] = arr[left:i]
        arr[left] = key

# Q2
def generate_random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]

def run_experiment(max_length):
    lengths = list(range(1, max_length + 1))
    times_insertion = []
    times_binary_insertion = []

    for length in lengths:
        arr = generate_random_array(length)

        # Measure time for insertion sort
        start_time = time.time()
        insertion_sort(arr.copy())
        times_insertion.append(time.time() - start_time)

        # Measure time for binary insertion sort
        start_time = time.time()
        binary_insertion_sort(arr.copy())
        times_binary_insertion.append(time.time() - start_time)

    return lengths, times_insertion, times_binary_insertion

# Q3
def plot_results(lengths, times_insertion, times_binary_insertion):

    # Interpolating functions 
    poly_insertion = np.polyfit(lengths, times_insertion, 2)
    poly_binary_insertion = np.polyfit(lengths, times_binary_insertion, 2)
    
    plt.plot(lengths, np.polyval(poly_insertion, lengths), '--', label='Insertion Sort')
    plt.plot(lengths, np.polyval(poly_binary_insertion, lengths), '--', label='Binary Insertion Sort')

    plt.xlabel('Input Length')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort vs Binary Insertion Sort')
    plt.legend()
    plt.show()

# Example usage
max_length = 100
lengths, times_insertion, times_binary_insertion = run_experiment(max_length)
plot_results(lengths, times_insertion, times_binary_insertion)

# Q4
## In general, Binary sort is much faster than Traditional insertion sort. The main reason being becuase the number of comparisons needed to be
## done is reduced in a binary sort algorithm. Insertion sort usually revolves around EACH element being checked until the desried 
## position is found. Binary on the other hand uses binary search to find the correct position for each element. This makes it so 
## that it doesnt have to chech element over and over again till its  satisfied, unoike traditional insertion sort.