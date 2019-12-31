
def twoSum(nums, target, index = True):
    # O(n)
    #
    # First, create a dictionary, we are going to use to store the target - the ith number as the key
    # and the value will be the index
    #
    buffer = {}
    # Second lets loop through the array to not return the number but the indices
    for i in range(len(nums)):
        # set a variable to get a value representation to compare
        n = nums[i]
        # print(buffer)
        if n in buffer and buffer[n] != i:
            if index:
                return buffer[n], i
            else:
                return nums[buffer[n]], nums[i]
                # return nums[buffer[n]], nums[i]
        buffer[target-n] = i


def twoosums(nums, target):
        nums_dict = {}
        for i, n in enumerate(nums):
            if target-n in nums_dict:
                return [nums_dict[target-n], i]
            nums_dict[n] = i


print(twoSum([1, 4, 7, 9], 16, False))
# print(twoosums([1,2,3,4,5], 5))















