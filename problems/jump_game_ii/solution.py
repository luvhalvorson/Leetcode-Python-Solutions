class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        level = 0
        farthest = 0
        i = 0
        while i <= len(nums) - 1:
            level += 1
            cur = farthest
            while i <= cur:
                farthest = max(farthest, i + nums[i])
                if farthest >= len(nums) - 1: 
                    return level
                i += 1
            
            
        return level