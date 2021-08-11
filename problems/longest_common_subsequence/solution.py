class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is text2:
            return len(text1)      
        dp = [0] * len(text1) + [0]
        for i in range(len(text2)):
            prev = 0
            for j in range(len(text1)):
                cur = dp[j + 1]
                dp[j + 1] = max(dp[j], dp[j+1],  prev + (text1[j] == text2[i]))
                prev = cur
            #print(dp)
        return dp[-1]