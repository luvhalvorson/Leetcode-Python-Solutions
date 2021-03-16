class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buying = 0
        selling = -prices[0]
        for p in prices:
            buying = max(buying, selling + p - fee)
            selling = max(selling, buying - p)
            
        return buying