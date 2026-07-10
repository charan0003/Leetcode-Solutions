class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums, target), self.last(nums, target)]

    def first(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if l < len(nums) and nums[l] == target:
            return l
        return -1

    def last(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        if r >= 0 and nums[r] == target:
            return r
        return -1