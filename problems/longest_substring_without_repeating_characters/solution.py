class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        
        startindex = 0
        res = 0
        for i, c in enumerate(s):
            if c in d:
                startindex = max(startindex, d[c] + 1)
            d[c] = i
            length = i - startindex + 1
            res = max(res, length) 
        return res