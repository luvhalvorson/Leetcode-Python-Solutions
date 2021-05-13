class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(set(s))
        
        if not s:
            return 0
        
        for i in range(l, 1-1, -1):
            print(f"i is {i}")
            for j in range(len(s)-i+1):
                print(j)
                if len(set(s[j:j+i])) == i:
                    return i
            