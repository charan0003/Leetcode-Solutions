class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i,n):
                seen.add(nums[j])
                count = len(seen)
                ans += count*count
        return ans

