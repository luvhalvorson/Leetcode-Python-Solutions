class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        myset = set()
        for i in range(len(s) - k + 1):
            myset.add(s[i:i + k])
            if len(myset) == 2**k:
                return True
        return False