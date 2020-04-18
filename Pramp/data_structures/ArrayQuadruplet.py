def findArrayQuadruplet(arr, s):
    if len(arr) < 4:
        return list()

    arr.sort()
    for i in range(len(arr)-4):
        for j in range(i+1, len(arr)-3):
            # store the complementing sum
            r = s - (arr[i] + arr[j])
            low, high = j+1, len(arr) - 1
            while low < high:
                if arr[low] + arr[high] < r:
                    low += 1
                elif arr[low] + arr[high] > r:
                    high -= 1
                else:
                    return [arr[i], arr[j], arr[low], arr[high]]
    return list()


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print(findArrayQuadruplet(arr, s))