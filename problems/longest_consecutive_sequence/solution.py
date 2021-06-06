class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for num in nums:
            if num in d:
                continue
            l = d.get(num - 1, 0) 
            r = d.get(num + 1, 0) 
            d[num] = l + r + 1
            #print(num, d[num])
            res = max(res, d[num])
            d[num-l] = l + r + 1
            d[num+r] = l + r + 1
        return res