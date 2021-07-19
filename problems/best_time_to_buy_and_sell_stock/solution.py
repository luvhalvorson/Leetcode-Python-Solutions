import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpast = prices[0]
        maxprofit = 0
        for price in prices[1:]:
            
            maxprofit = max(maxprofit, price - minpast)
            minpast = min(minpast, price)
        return maxprofit