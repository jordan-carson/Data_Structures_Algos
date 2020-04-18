def get_different_number(arr):
    for i in range(len(arr)):
        while arr[i] != i:
            j = arr[i]
            if j >= len(arr):
                return i
            else:
                arr[i], arr[j] = arr[j], arr[i]
    return len(arr)

print(get_different_number([0,1,4,3]))

print(get_different_number([0,1,2]))

print(get_different_number([10000]))