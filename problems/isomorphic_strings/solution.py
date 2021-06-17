class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        d1 = {}
        d2 = {}
        f = 0
        # while p1 < len(s) and p2 < len(t):
        #     if s[p1] in d:
        #         if t[p2] != d[s[p1]]:
        #             return False
        #     elif t[p2] in d:
        #         if f:
        #             return False
        #         else:
        #             f = 1
        #     else:
        #         d[s[p1]] = t[p2]
        #     p1 += 1
        #     p2 += 1
        # return True
        for c1, c2 in zip(s, t):
            if (c1 not in d1) and (c2 not in d2):
                d1[c1] = c2
                d2[c2] = c1
            elif d1.get(c1) != c2 or d2.get(c2) != c1:
                return False
            
        return True