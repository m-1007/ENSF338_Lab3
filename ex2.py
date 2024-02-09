import random
import time

#2.1: Implement and test both algorithms on input of 20 different sizes. 
    # The choice of sizes is yours, but it must be such that it evidences for which sizes each algorithm is faster

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr 


def partition(arr, low, high):
    pivot = arr[low] #choose first element as pivot
    left = low + 1 #index to go from left to right
    right = high #index to go from right to left
    done = False
    while not done:
        #move left pointer to the right until an element greater than or equal to pivot is found
        while left <= right and arr[left] <= pivot:
            left = left + 1

        #move right pointer to the left until an element lesser than or equal to pivot is found
        while arr[right] >= pivot and right >= left:
            right = right -1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

        #swap the pivot with the element at the right pointer
        arr[low], arr[right] = arr[right], arr[low]
        return right
    
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)  # Partition the array and get the pivot index
        quick_sort(arr, low, pivot - 1)     # Recursively sort elements before the pivot
        quick_sort(arr, pivot + 1, high)    # Recursively sort elements after the pivot
    return arr
    