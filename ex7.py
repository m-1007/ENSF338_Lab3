import json
import time
import matplotlib.pyplot as plt
#7.1: Implement a standard binary search, with the following tweak: 
    # the midpoint for the first iteration must be configurable 
    # (all successive iterations will just split the array in the middle)

def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# Binary search function
def binary_search(arr, target, start, end):
    left = 0
    right = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return False

def binary_search_with_changable_mid(arr, target, start_midpoint):
    start = 0
    end = len(arr) - 1
    mid = start_midpoint
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


def main():
    array_data = read_json("ex7data.json")
    task_data = read_json("ex7tasks.json")
    array = array_data
    task = task_data

    all_times = {}

    num_midpoint = 1000

    for task_index, target in enumerate(task, start=1):

        print(f"Processing task {task_index}/{len(task)}")

        all_times [target] = []

        step_size = len(array) // num_midpoint


        total_iterations = num_midpoint

        for i in range(0, len(array), step_size):

            print(f"  Iteration {i//step_size + 1}/{total_iterations}", end="\r")
            start_time = time.time()

            binary_search_with_changable_mid(array, target, 1)

            end_time = time.time()

            elapsed_time = end_time - start_time

            all_times [target].append(elapsed_time) 
            print() # Print newline after each task

    best_midpoint = {}

    for target, times in all_times.items():

        best_index = min(range(len(times)), key=times.__getitem__)
        best_midpoint[target] = best_index * step_size
        best_time = float('inf')
        for i in range(max(0, best_index - 1) * step_size, min(len(array) ,(best_index + 2) * step_size), step_size // 2):

            start_time = time.time()

            binary_search_with_changable_mid(array, target, i)

            end_time = time.time()

            elapsed_time = end_time - start_time

            if elapsed_time < best_time:

                best_time = elapsed_time

                best_midpoint[target] = i

    for target, best_index in best_midpoint.items():

        print(f"For target {target}, best midpoint is {best_index} with time {all_times[target] [best_index // step_size]:.6f} seconds.")

    tasks_list = list(task)

    best_midpoints_list = [best_midpoint[task] for task in tasks_list]


    plt.figure(figsize = (10,6))
    plt.scatter(tasks_list, best_midpoints_list)
    plt.title('Task versus Best Midpoint')
    plt.xlabel('Task')
    plt.ylabel('Best Midpoint')
    plt.show()

if __name__ == "__main__":
    main()
# 7.4 Comment on the graph. Does the choice of initial midpoint appear to affect performance? Why do you think is that? [0.2 pts]

# The choice of the initial midpoint can in fact affect performance. The scatterplot shows variations
# in search times for different initial midpoints. Some midpoints may lead to faster convergence, while others
# may result in longer search times. The optimal initial midpoint may depend on the specific characteristics
# of the array and the element being searched. 