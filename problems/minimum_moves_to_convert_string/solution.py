class Solution:
    def minimumMoves(self, s: str) -> int:
        r = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                i += 3
                r += 1
            else:
                i +=1
        
        return r