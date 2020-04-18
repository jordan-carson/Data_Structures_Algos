from typing import List
import os


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
