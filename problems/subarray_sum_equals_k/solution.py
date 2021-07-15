class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        s = 0
        res = 0
        for num in nums:
            s += num
            if s == k:
                res += 1
            if s - k in d:
                res += d[s-k]
            if s in d:
                d[s] +=1 
            else:
                d[s] = 1
        #print(d)
        return res