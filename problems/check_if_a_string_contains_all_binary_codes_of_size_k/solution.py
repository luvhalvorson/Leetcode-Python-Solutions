class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = []
        for i in range(0, len(s)-k+1):
            a.append(s[i:i+k])
        #print(a)
        #print(len(set(a)))
        if len(set(a)) == 2**k:
            return True
        else:
            return False