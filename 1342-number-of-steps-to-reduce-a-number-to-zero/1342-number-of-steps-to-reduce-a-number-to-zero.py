class Solution:
    def numberOfSteps(self, num: int) -> int:
        return bin(num).count('1') + len(bin(num)) - 3