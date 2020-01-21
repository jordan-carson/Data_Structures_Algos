class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        import time
        start = time.time()
        prod = 1
        n = str(n)
        total = 0
        for i in range(len(str(n))):
            prod *= int(n[i])
            total += int(n[i])
        # for i in range(len(str(n))):
        #     total += int(n[i])

        return prod - total, time.time() - start

print(Solution().subtractProductAndSum(234))

