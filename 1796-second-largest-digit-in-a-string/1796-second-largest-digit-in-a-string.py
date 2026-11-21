class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted(set(int(ch) for ch in s if ch.isdigit()), reverse=True)

        return digits[1] if len(digits) >= 2 else -1