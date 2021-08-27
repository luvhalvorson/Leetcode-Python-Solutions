class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0] + [float('inf')] * (amount)
        coins.sort()
        #print(coins)
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                else:
                    break
                    # 為什麼這個break會有影響？我本來以為後面都會coin>i 那就不用多跑．．

        return dp[-1] if dp[-1] <= amount else -1
                
                