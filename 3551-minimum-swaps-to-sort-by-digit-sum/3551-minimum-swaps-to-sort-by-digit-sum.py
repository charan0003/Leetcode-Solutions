class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {num: i for i, num in enumerate(nums)}
        ans = 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                ans += 1

                j = position[sorted_nums[i]]

                position[nums[i]] = j
                position[nums[j]] = i

                nums[i], nums[j] = nums[j], nums[i]

        return ans