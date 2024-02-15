import json

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

# Define the configurable starting midpoint
start_midpoint = 0  # can be any value?

# Perform binary search for each search task
for task in search_tasks:
    result_index = binary_search(array, task, start_midpoint)
    if result_index != -1:
        print(f"Element {task} found at index {result_index}")
    else:
        print(f"Element {task} not found in the array")

