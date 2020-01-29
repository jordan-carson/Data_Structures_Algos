

def bubble(arr):
    w
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]

    return arr


print(bubble([2,3,4,3, 1, 0]))
