class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        minlen = min(len(strs[0]), len(strs[-1]))

        for i in range(0, minlen):
            if strs[0][i] != strs[-1][i]:
                return strs[0][0: i]

        return strs[0]