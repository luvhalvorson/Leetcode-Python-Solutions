class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5
        if n == 1:
            return sum(dp) % (10**9 + 7)
        relation = [[1,2,4], [0,2], [1,3], [2], [2,3]]
        for leng in range(n-1):
            last = dp.copy()
            for i in range(5): 
                dp[i] = sum(last[j] for j in relation[i])
                
        return sum(dp) % (10**9 + 7)
        