class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num

        tot = 0

        while num > 0:
            tot += num % 10
            num //= 10

        return self.addDigits(tot)