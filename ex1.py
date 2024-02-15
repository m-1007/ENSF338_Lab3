import sys; sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low<high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    # Create temporary arrays to hold the two halves
    Left = [0] * n1
    Right = [0] * n2

    # Copy data to temporary arrays Left[] and Right[]
    for i in range(n1):
        Left[i] = arr[low + i]

    for j in range(n2):
        Right[j] = arr[mid + 1 + j]

    # Merge the two halves back into the main array
    i = j = 0
    k = low

    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1

    # Copy the remaining elements of Left[] (if any remains)
    while i < n1:
        arr[k] = Left[i]
        i += 1
        k += 1

    # Copy the remaining elements of Right[] (if any remains)
    while j < n2:
        arr[k] = Right[j]
        j += 1
        k += 1

arr = [8, 42, 25, 3, 3, 2, 27, 3]
merge_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)