class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        maximum = max(freq.values())
        return sum(v for v in freq.values() if v == maximum)