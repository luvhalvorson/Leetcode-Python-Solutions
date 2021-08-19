class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [0] * (len(grid[0]) + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    dp[j + 1] = grid[i][j] + dp[j]
                elif j == 0:
                    dp[j + 1] = grid[i][j] + dp[j + 1]
                else:
                    dp[j + 1] = grid[i][j] + min(dp[j], dp[j + 1])
            
        return dp[-1]