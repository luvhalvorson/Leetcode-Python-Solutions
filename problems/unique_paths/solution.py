class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m < n: m, n = n, m
        ans = 1
        for i in range(m+n, m, -1):
            ans *= i
        
        for i in range(1, n + 1):
            ans //= i
        return ans
#         if m < n: m, n = n, m
#         dp = [0] * (n + 1)
#         dp[1] = 1
#         for i in range(m):           
#             for j in range(n):
#                 dp[j + 1] += dp[j]                
            
#         return dp[-1]