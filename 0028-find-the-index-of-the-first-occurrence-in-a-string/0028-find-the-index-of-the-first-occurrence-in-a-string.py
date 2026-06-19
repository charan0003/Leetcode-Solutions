class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    #    if needle in haystack:
    #         return haystack.index(needle)
    #     else:
    #         return -1 
    #         with using built-in functions
        if needle=="":
            return 0
        for i in range(len(haystack)+1 - len(needle)):
            if haystack[i:i + len(needle)]== needle:
                return i
        return -1
        # with using sliding window 