class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
#         d = {}

#         for c1, c2 in zip(s, t):
#             d[c1] = d.get(c1, 0) + 1
#             d[c2] = d.get(c2, 0) - 1
        
#         for v in d.values():
#             if v != 0:
#                 return False
        a = [0] * 26

        for c1, c2 in zip(s, t):
            a[ord(c1) - ord('a')] += 1
            a[ord(c2) - ord('a')] -= 1
        
        for count in a:
            if count != 0:
                return False
        return True
        