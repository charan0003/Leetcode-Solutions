class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2

            total = mid * (mid + 1) // 2

            if total == n:
                return mid
            elif total < n:
                l = mid + 1
            else:
                r = mid - 1

        return r