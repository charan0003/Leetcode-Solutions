class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        counts = [0] * 32

        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    counts[bit] += 1

        ans = 0

        for _ in range(k):
            x = 0

            for bit in range(32):
                if counts[bit] > 0:
                    x |= 1 << bit
                    counts[bit] -= 1

            ans = (ans + x * x) % MOD

        return ans
