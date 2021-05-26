from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen = len(s)
        plen = len(p)
        pc = Counter(p)
        sc = {}
        # p可以是[]?
        if slen < plen:
            return []
        res = []
        for i in range(slen):
            if s[i] in sc:
                sc[s[i]] += 1
            else:
                sc[s[i]] = 1
            if i >= plen:
                sc[s[i-plen]]-=1
                if sc[s[i-plen]] == 0:
                    sc.pop(s[i-plen])
            
            if sc == pc:
                res.append(i-plen+1)
                
        return res