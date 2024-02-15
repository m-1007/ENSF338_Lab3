import json
import time
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
# Define a function to time the binary search
def time_binary_search(arr, target, start_midpoint):
    start = time.time()  # get the current time in seconds
    result_index = binary_search(arr, target, start_midpoint)  # call the binary search function
    end = time.time()  # get the current time in seconds
    elapsed = end - start  # calculate the elapsed time in seconds
    return result_index, elapsed

# list of possible midpoint
midpoints = [0, len(array) // 4, len(array) // 2]


# Loop through each search task and each midpoint
for task in search_tasks:
    print(f"Searching for element {task} with different midpoints:")
    best_midpoint = None  # initialize the best midpoint as None
    best_time = float('inf')  # initialize the best time as infinity
    for midpoint in midpoints:
        result_index, elapsed = time_binary_search(array, task, midpoint)  # time the binary search
        print(f"Midpoint: {midpoint}, Result index: {result_index}, Elapsed time: {elapsed:.6f} seconds")
        
        if result_index == -1:
            print("Element not found in the array.")
            break  # exit the loop if the element is not found
        
        if result_index > 0 and array[result_index - 1] == task:
            print(f"Potential earlier occurrence found at index {result_index - 1}.")
        
        if elapsed < best_time:  # update the best midpoint and time if the current one is better
            best_midpoint = midpoint
            best_time = elapsed
    print(f"Best midpoint for element {task} is {best_midpoint} with elapsed time {best_time:.6f} seconds\n")

# Check if there are remaining search tasks
if not search_tasks:
    print("All search tasks have been processed.")
else:
    print(f"Remaining search tasks: {search_tasks}")
