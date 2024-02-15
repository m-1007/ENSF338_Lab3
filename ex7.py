import json
import timeit
#7.1: Implement a standard binary search, with the following tweak: 
    # the midpoint for the first iteration must be configurable 
    # (all successive iterations will just split the array in the middle)


# Binary search function
def binary_search(arr, target, start_midpoint=0):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = start_midpoint if left == 0 else (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Load array and search tasks from JSON files
with open('ex7data.json', 'r') as file:
    array = json.load(file)

with open('ex7tasks.json', 'r') as file:
    search_tasks = json.load(file)

# 7.2 Time the performance of each search task with different midpoints
for task in search_tasks:
    best_midpoint = None
    best_time = float('inf')
    
    for start_midpoint in range(len(array)):
        time_taken = timeit.timeit(lambda: binary_search(array, task, start_midpoint), number=100)
        
        if time_taken < best_time:
            best_time = time_taken
            best_midpoint = start_midpoint
    
    print(f"For element {task}, the best midpoint is {best_midpoint} with an average time of {best_time / 100:.6f} seconds per search")
