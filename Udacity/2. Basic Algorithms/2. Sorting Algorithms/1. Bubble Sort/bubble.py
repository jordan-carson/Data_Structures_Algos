

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

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    for i in range(len(l)):
        for j in range(1, len(l)):
            this_hour, this_min = l[j]
            prev_hour, prev_min = l[j - 1]
            if this_hour < prev_hour or (prev_hour == this_hour and prev_min > this_min):
                continue
            l[j], l[j - 1] = (prev_hour, prev_min), (this_hour, this_min)
    return l


bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")