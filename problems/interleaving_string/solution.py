class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        #dp = [[0] * (len(s2) + 1) ] * (len(s1) + 1) # 前面有0 lens1+1 lens2+1
        dp = [ [0]*(len(s2) + 1) for i in range((len(s1) + 1))]
        targetlen = len(s3)
        dp[0][0] = 1
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])
            
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])
            
        for i in range(1, len(s1) + 1): # 選幾個 s1
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and (s1[i - 1] == s3[i - 1 + j])) or (dp[i][j - 1] and (s2[j - 1] == s3[j - 1 + i]))
                
        #print(dp)
        return True if dp[-1][-1] == 1 else False