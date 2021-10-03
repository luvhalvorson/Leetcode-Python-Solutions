class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # n = 4
        # x + y + z + w = 9 
        m = len(rolls)
        nsum = mean * (m + n) - sum(rolls)
        navg = nsum / n
        if math.floor(navg) < 1 or math.ceil(navg) > 6:
            return []
        res = [math.floor(navg)] * n
        cur = sum(res)
        i = 0
        while cur < nsum and i < n:
            #print(res)
            if res[i] < 6:
                res[i] += 1
                cur += 1
            else:
                i += 1
            
        
        if cur != nsum:
            return []
        return res
        