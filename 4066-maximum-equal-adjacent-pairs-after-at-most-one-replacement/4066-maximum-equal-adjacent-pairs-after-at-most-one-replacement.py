class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base = 0
        pairs = {}

        for i in range(1, len(nums)):
            a = nums[i - 1]
            b = nums[i]

            if a == b:
                base += 1
            else:
                key = (min(a, b), max(a, b))
                pairs[key] = pairs.get(key, 0) + 1

        best = 0

        for count in pairs.values():
            best = max(best, count)

        return base + best