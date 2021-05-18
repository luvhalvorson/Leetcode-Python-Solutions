class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        #print(strs)
        minlen = len(strs[0])
        for i in range(minlen, 1-1, -1):
            flag = 1
            for stri in range(1, len(strs)):
               # print(strs[0][0:i], strs[stri])
                if strs[0][0:i] != strs[stri][0:i]:
                    flag = 0
                    break
            if flag:
                return strs[0][0:i]
        return ""