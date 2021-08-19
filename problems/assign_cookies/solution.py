class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort()
        s.sort()
        i = 0
        res = 0
        for child in g:
            while i <= len(s) - 1 and s[i] < child:
                i += 1
            if i < len(s) - 1 :
                i += 1
                res += 1
            elif i == len(s) - 1:
                res +=1 
                break
            else:
                break
        return res
                