class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        n = str(n)
        for i in range(len(str(n))):
            prod *= int(n[i])

        total = 0
        for i in range(len(str(n))):
            total += int(n[i])

        return prod - total

print(Solution().subtractProductAndSum(234))
