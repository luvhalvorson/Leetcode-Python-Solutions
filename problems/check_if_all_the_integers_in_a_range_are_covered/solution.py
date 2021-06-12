class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cur = left
        sr = sorted(ranges)
        
        for interval in sr:
            
            if cur >= interval[0] and cur <= interval[1]:
                cur = max(cur, interval[1])
                if cur >= right:
                    return True
                cur += 1
            
        return False