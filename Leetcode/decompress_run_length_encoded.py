from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new_list = list()
        for i in range(0, len(nums) - 1, 2):
            new_list = new_list + nums[i] * [nums[i+1]]
        return new_list



print(Solution().decompressRLElist([1,2,3,4]))


