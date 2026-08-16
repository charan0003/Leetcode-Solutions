class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        chars = "0123456789abcdef"

        if num < 0:
            num += 2**32

        result = ""

        while num:
            digit = num % 16
            result = chars[digit] + result
            num //= 16

        return result