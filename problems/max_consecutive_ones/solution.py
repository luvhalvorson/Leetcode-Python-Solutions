class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc, curc = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                curc += 1
            else:
                maxc = max(maxc, curc)
                curc = 0
            
        maxc = max(maxc, curc)    
        return maxc