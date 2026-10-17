class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        perm = []
        pick = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True

                    backtrack()

                    perm.pop()
                    pick[i] = False

        backtrack()
        return res