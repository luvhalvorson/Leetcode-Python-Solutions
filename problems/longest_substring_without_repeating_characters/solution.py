class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        start = 0
        d = {}
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            maxlength = max(maxlength, i - start + 1)
        return maxlength