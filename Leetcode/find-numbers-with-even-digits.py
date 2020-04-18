from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        numbers = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                numbers += 1
        return numbers



if __name__ == '__main___':
    arr = [12,345,2,6,7896]

    print(Solution().findNumbers([12,345,2,6,7896]))