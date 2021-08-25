class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * (n + 1)
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]  == 1:            
            return 0
        dp[1] = 1
        for i in range(m):
            for j in range(n):
                
                if obstacleGrid[i][j] == 1:
                    dp[j + 1] = 0
                else:
                    dp[j + 1] += dp[j]
        return dp[-1]