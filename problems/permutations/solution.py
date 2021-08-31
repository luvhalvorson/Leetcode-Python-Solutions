class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 123   1   rec([23])   2  rec(3)   
        # 132   1        23     3    2  
        # 213    2
        #
        res = []
        
        def backtrack(numlist, path):
            
            if len(numlist) == 1:
                res.append(path + numlist)
                return
            for i in range(len(numlist)):
                backtrack(numlist[:i] + numlist[i+1:], path + [numlist[i]])
        backtrack(nums, [])    
        
        return res