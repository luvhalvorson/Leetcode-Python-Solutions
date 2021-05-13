class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng = len(s)
        for i in range(leng, 0, -1):
            for j in range(leng-i+1):
                ss = s[j:j+i]
                if ss == ss[::-1]:
                    return ss
            
        return s[0]
            