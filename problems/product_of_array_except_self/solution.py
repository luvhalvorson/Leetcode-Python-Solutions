class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1     
        zeros = 0
        
        for n in nums:
            if n == 0:
                zeros += 1
                continue
            total *= n
            
        if zeros >= 2:
            return [0] * len(nums)
        elif zeros == 1:
            r = [0] * len(nums)
            r[nums.index(0)] = total
            return r
        else:    
            res = []
            for n in nums:
                res.append( total // n)
                
        return res