import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for p in prices:
            if p < minprice:
                minprice = p
            maxprofit = max(maxprofit, p - minprice)
        return maxprofit
        