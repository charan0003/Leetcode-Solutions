
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            blocks = [nums[i:i + k] for i in range(0, n, k)]
            valid = True

            for i, block in enumerate(blocks):
                drops = sum(
                    block[j] > block[(j + 1) % k]
                    for j in range(k)
                )

                if drops > 1:
                    valid = False
                    break

                if i > 0 and max(blocks[i - 1]) > min(block):
                    valid = False
                    break

            if valid:
                ans += k

        return ans