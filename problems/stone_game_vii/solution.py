class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        total = 0 
        n = (len(stones))
        dp = [[0] * n for _ in range(n)]
        #print(dp)
        for i in range(n - 2, -1, -1):
            total = stones[i]
            for j in range(i+1, n):
                total += stones[j]
                dp[i][j] = max(total - stones[i] - dp[i+1][j] , total - stones[j] -  dp[i][j-1])
        #print(dp)
        
        return dp[0][-1]