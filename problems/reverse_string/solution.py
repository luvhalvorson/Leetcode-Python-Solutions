class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        slen = len(s)
        for i in range(slen):
            j = slen - i - 1
            if i < j:
                s[i], s[j] = s[j], s[i]