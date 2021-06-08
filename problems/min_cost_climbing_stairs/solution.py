class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #dp = [0] * n
        a = cost[0]
        b = cost[1]
        c = 0 
        for i in range(2, n):
            #dp[i] = cost[i] + min(dp[i- 1], dp[i - 2])
            c = min(a,b) + cost[i]
            a = b
            b = c
           
        print(a,b,c)
        return min(a,b)