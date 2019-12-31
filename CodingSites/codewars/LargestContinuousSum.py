# find the largest continuous sum
# given an array of integers positive and negative find the largest continuous sum

def largestContinuousSum(arr):
    if len(arr) == 0:
        return 0

    maxsum = currentsum = arr[0]
    for num in arr[1:]:
        currentsum = max(currentsum + num, num)
        maxsum = max(currentsum, maxsum)
    return maxsum


print(largestContinuousSum([10, 20, 30, -10, -20]))