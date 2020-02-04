

def bubble(arr):

    for i in range(len(arr)):
        for index in range(1, len(arr)):
            this = arr[index]
            prev = arr[index - 1]
            if prev <= this:
                continue
            arr[index], arr[index - 1] = prev, this
    return arr

def swap(a, b):
    # if a > b:
    a, b = b, a
    return a, b

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # swap(arr[j], arr[j+1])
    return arr


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element fou
            # nd is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
print(bubble_sort([2,3,4,3, 1, 0]))
