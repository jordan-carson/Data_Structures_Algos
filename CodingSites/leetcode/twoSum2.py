import cProfile
def twoSum2(arr, target):
    if arr is None or len(arr) < 1:
        return 0, 0
    buffer = {}
    for i in range(len(arr)):
        # n = arr[i]
        if arr[i] in buffer:
            return arr[i], i
        else:
            buffer[target-arr[i]] = i


def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        print(buff_dict)
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
# cProfile.run('twoSum([1, 2, 3, 4], 7)')

print(twoSum2([1, 4, 8, 7, 3, 15], 8))


