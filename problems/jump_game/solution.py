class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        curmax = nums[0]
        for i in range(1, len(nums)):
            if curmax >= i: #can reach this pos
                curmax = max( i + nums[i], curmax)
            else:
                return False
            if curmax >= len(nums) - 1: # can reach last pos
                return True
        return False