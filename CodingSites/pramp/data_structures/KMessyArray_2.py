def sort_k_messed_array(arr, k):
    # 1 , 2 , 5, 4, 3, 7, 8, 6, 10 ,9 k = 2
    for index in range(len(arr)):
        if index == len(arr) - 1:
            break
        offset = 1
        minIndex = index
        minValue = arr[index]
        while offset < k + 1 and index + offset < len(arr):
            if arr[index + offset] < minValue:
                minIndex = index + offset
                minValue = arr[minIndex]
            offset += 1
        if minValue != arr[index]:
            temp = arr[index]
            arr[index] = minValue
            arr[minIndex] = temp
    return arr