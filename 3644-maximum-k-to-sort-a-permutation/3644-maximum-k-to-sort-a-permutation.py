class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        misplaced = [x for i, x in enumerate(nums) if x != i]

        if not misplaced:
            return 0

        ans = misplaced[0]
        for x in misplaced[1:]:
            ans &= x

        return ans