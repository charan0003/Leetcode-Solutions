class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x : abs(x),reverse=True)
        ans=0

        for i,num in enumerate(nums):
            if i<(len(nums) + 1)//2:
                ans += num * num
            else:
                ans -= num * num
        return ans